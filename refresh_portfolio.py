"""
refresh_portfolio.py

Recomputes portfolio.csv's Qty, Average Cost Price, and dependent valuation
columns directly from trades.csv for symbols with complete trade history (e.g. ETFs),
while explicitly skipping PARTIAL_HISTORY_SYMBOLS whose trade history is incomplete.

Preserves exact file structure, trailing commas, and formatting for untouched rows.

USAGE:
    python3 refresh_portfolio.py [trades.csv] [portfolio.csv]
"""

import sys
import pandas as pd

TRADES_FILE = "trades.csv"
PORTFOLIO_FILE = "portfolio.csv"

# Symbols with known-incomplete trade history in trades.csv
PARTIAL_HISTORY_SYMBOLS = {
    'ASHLEY', 'HDFBAN', 'BHAELE', 'JIOFIN', 'WIPRO',
    'LIC', 'RELIND', 'TATCAP', 'LGELEC', 'NTPGRE', 'GUJPPL'
}

# Known exited positions or external trades present in trades.csv but not held in portfolio.csv
KNOWN_EXITED_OR_EXTERNAL_SYMBOLS = {'AWL', 'KOTAKBKETF'}


def calculate_trades_positions(trades_df: pd.DataFrame) -> dict:
    """
    Computes net quantity and average cost price per symbol from trades.csv.
    Uses rolling position average cost basis:
      - BUY: total_cost += qty * price, net_qty += qty
      - SELL: avg_cost preserved, net_qty -= qty, total_cost = net_qty * avg_cost
    Returns dict: {symbol: {'qty': float, 'avg_cost': float}}
    """
    if trades_df.empty:
        return {}

    clean = trades_df.copy()
    clean["Action"] = clean["Action"].astype(str).str.strip().str.upper()

    numeric_trades = clean[
        clean["Action"].isin(["BUY", "SELL"]) & 
        pd.to_numeric(clean["Qty"], errors="coerce").notna() &
        pd.to_numeric(clean["Price"], errors="coerce").notna()
    ].copy()

    numeric_trades["Date_dt"] = pd.to_datetime(numeric_trades["Date"], errors="coerce")
    numeric_trades["Qty_num"] = numeric_trades["Qty"].astype(float)
    numeric_trades["Price_num"] = numeric_trades["Price"].astype(float)
    
    numeric_trades = numeric_trades.sort_values("Date_dt")

    positions = {}
    for sym, group in numeric_trades.groupby("Stock Symbol"):
        sym = str(sym).strip()
        net_qty = 0.0
        total_cost = 0.0
        
        for _, row in group.iterrows():
            action = row["Action"]
            t_qty = row["Qty_num"]
            t_price = row["Price_num"]
            
            if action == "BUY":
                total_cost += t_qty * t_price
                net_qty += t_qty
            elif action == "SELL":
                if net_qty > 0:
                    avg_cost_before = total_cost / net_qty
                    net_qty = max(0.0, net_qty - t_qty)
                    total_cost = net_qty * avg_cost_before
                else:
                    net_qty = 0.0
                    total_cost = 0.0
                    
        avg_cost = (total_cost / net_qty) if net_qty > 0 else 0.0
        positions[sym] = {"qty": net_qty, "avg_cost": avg_cost}
        
    return positions


def refresh_row(row_dict: dict, calc_qty: float, calc_avg_cost: float) -> dict:
    """
    Refreshes a portfolio row dictionary based on calc_qty and calc_avg_cost from trades.csv.
    Symbols in PARTIAL_HISTORY_SYMBOLS are never overwritten or reformatted, regardless of calc_qty.
    """
    row = dict(row_dict)
    sym = str(row["Stock Symbol"]).strip()

    if sym in PARTIAL_HISTORY_SYMBOLS:
        return row  # trades.csv known incomplete for this symbol — return original row completely untouched

    existing_qty = float(row["Qty"])
    if calc_qty != existing_qty:
        row["Qty"] = int(round(calc_qty))
        row["Average Cost Price"] = round(calc_avg_cost, 2)

    qty = float(row["Qty"])
    avg_cost = float(row["Average Cost Price"])
    cmp = float(row.get("Current Market Price", 0.0)) if pd.notna(row.get("Current Market Price")) else 0.0

    val_at_cost = round(qty * avg_cost, 2)
    val_at_mkt = round(qty * cmp, 2)
    unrealized_pnl = round(val_at_mkt - val_at_cost, 2)
    unrealized_pnl_pct = round((unrealized_pnl / val_at_cost) * 100, 2) if val_at_cost > 0 else 0.0

    row["Value At Cost"] = val_at_cost
    row["Value At Market Price"] = val_at_mkt
    row["Unrealized Profit/Loss"] = unrealized_pnl
    row["Unrealized Profit/Loss %"] = f"{unrealized_pnl_pct:.2f}" if unrealized_pnl_pct >= 0 else f"({abs(unrealized_pnl_pct):.2f})"

    return row


def refresh_portfolio(trades_path: str = TRADES_FILE, portfolio_path: str = PORTFOLIO_FILE) -> pd.DataFrame:
    trades_df = pd.read_csv(trades_path)
    positions = calculate_trades_positions(trades_df)

    with open(portfolio_path, "r", newline="") as f:
        lines = f.readlines()

    if not lines:
        return pd.DataFrame()

    header_line = lines[0]
    header_cols = [c.strip() for c in header_line.split(",") if c.strip()]
    
    sym_idx = header_cols.index("Stock Symbol") if "Stock Symbol" in header_cols else 0

    known_port_symbols = set()
    for line in lines[1:]:
        if line.strip():
            parts = [p.strip() for p in line.split(",")]
            if len(parts) > sym_idx and parts[sym_idx]:
                known_port_symbols.add(parts[sym_idx])

    allowed_symbols = known_port_symbols | PARTIAL_HISTORY_SYMBOLS | KNOWN_EXITED_OR_EXTERNAL_SYMBOLS
    unclassified = set(positions.keys()) - allowed_symbols
    if unclassified:
        raise ValueError(
            f"Unclassified symbol(s) {sorted(list(unclassified))} found in trades.csv "
            f"that are missing from portfolio.csv!"
        )

    qty_idx = header_cols.index("Qty")
    avg_idx = header_cols.index("Average Cost Price")
    cmp_idx = header_cols.index("Current Market Price") if "Current Market Price" in header_cols else -1
    cost_idx = header_cols.index("Value At Cost") if "Value At Cost" in header_cols else -1
    mkt_idx = header_cols.index("Value At Market Price") if "Value At Market Price" in header_cols else -1
    pnl_idx = header_cols.index("Unrealized Profit/Loss") if "Unrealized Profit/Loss" in header_cols else -1
    pnl_pct_idx = header_cols.index("Unrealized Profit/Loss %") if "Unrealized Profit/Loss %" in header_cols else -1

    new_lines = [header_line]
    for line in lines[1:]:
        if not line.strip():
            new_lines.append(line)
            continue

        raw_parts = line.split(",")
        parts = [p.strip() for p in raw_parts]
        sym = parts[sym_idx]

        if sym in PARTIAL_HISTORY_SYMBOLS or sym not in positions:
            new_lines.append(line)
            continue

        pos = positions[sym]
        calc_qty = pos["qty"]
        calc_avg_cost = pos["avg_cost"]
        existing_qty = float(parts[qty_idx])

        if calc_qty != existing_qty:
            new_qty = int(round(calc_qty))
            new_avg_cost = round(calc_avg_cost, 2)
            cmp = float(parts[cmp_idx]) if (cmp_idx >= 0 and cmp_idx < len(parts) and parts[cmp_idx]) else 0.0

            val_at_cost = round(new_qty * new_avg_cost, 2)
            val_at_mkt = round(new_qty * cmp, 2)
            unrealized_pnl = round(val_at_mkt - val_at_cost, 2)
            unrealized_pnl_pct = round((unrealized_pnl / val_at_cost) * 100, 2) if val_at_cost > 0 else 0.0

            parts[qty_idx] = str(new_qty)
            parts[avg_idx] = f"{new_avg_cost:.2f}"
            if cost_idx >= 0: parts[cost_idx] = f"{val_at_cost:.2f}"
            if mkt_idx >= 0: parts[mkt_idx] = f"{val_at_mkt:.2f}"
            if pnl_idx >= 0: parts[pnl_idx] = f"{unrealized_pnl:.2f}"
            if pnl_pct_idx >= 0: parts[pnl_pct_idx] = f"{unrealized_pnl_pct:.2f}" if unrealized_pnl_pct >= 0 else f"({abs(unrealized_pnl_pct):.2f})"

            trailing = ",\n" if line.endswith(",\n") or line.endswith(",\r\n") else ("\r\n" if line.endswith("\r\n") else "\n")
            new_lines.append(",".join(parts[:len(header_cols)]) + trailing)
        else:
            new_lines.append(line)

    with open(portfolio_path, "w", newline="") as f:
        f.writelines(new_lines)

    return pd.read_csv(portfolio_path)


def main():
    trades_path = sys.argv[1] if len(sys.argv) > 1 else TRADES_FILE
    portfolio_path = sys.argv[2] if len(sys.argv) > 2 else PORTFOLIO_FILE
    
    refresh_portfolio(trades_path, portfolio_path)
    print(f"Successfully refreshed {portfolio_path} from {trades_path}")


if __name__ == "__main__":
    main()
