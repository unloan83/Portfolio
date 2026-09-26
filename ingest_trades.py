"""
ingest_trades.py

Builds a REAL trades.csv from one or more Upstox order book or tradebook CSV exports,
and reconciles the resulting quantities against portfolio.csv so silent
mismatches (bonus/split/merger/partial history effects) surface cleanly.

USAGE:
    python3 ingest_trades.py reports/orderBook_Equity_1790345624080.csv
"""

import sys
import pandas as pd

OUTPUT_FILE = "trades.csv"
PORTFOLIO_FILE = "portfolio.csv"

# Upstox export column names map
UPSTOX_COLUMN_MAP = {
    "Date": "Date",
    "Stock": "Stock Symbol",
    "Action": "Action",       # values: 'Buy' / 'Sell'
    "Qty": "Qty",
    "Price": "Price",
}

HEADER_ALIASES = {
    "Date": ["trade date", "date", "trade_date", "tradedate"],
    "Stock Symbol": ["stock", "symbol", "stock symbol", "scrip name", "scrip_name", "trading symbol", "scrip"],
    "Action": ["action", "trade type", "type", "transaction type", "buy/sell", "trade_type", "side"],
    "Qty": ["qty", "quantity", "trade qty", "shares"],
    "Price": ["price", "rate", "trade price", "avg price", "average price"]
}

# Mapping Upstox broker stock names to portfolio.csv Stock Symbol names
UPSTOX_SYMBOL_MAP = {
    "ASHOKLEY": "ASHLEY",
    "BEL": "BHAELE",
    "DRREDDY": "DRREDD",
    "ENGINERSIN": "ENGIND",
    "FEDERALBNK": "FEDBAN",
    "GAIL": "GAIL",
    "GPPL": "GUJPPL",
    "GUJENERGY": "GUJGA",
    "HDFCBANK": "HDFBAN",
    "HDFCSML250": "HDF250",
    "HINDPETRO": "HINPET",
    "ICICIGOLD": "ICIGOL",
    "ICICINIFTY": "ICINIF",
    "ICICISILVE": "ICIPSE",
    "IDEA": "IDECEL",
    "ITBEES": "NIPNIT",
    "JIOFIN": "JIOFIN",
    "JSWENERGY": "JSWENE",
    "LICI": "LIC",
    "MIDCAPETF": "MIR150",
    "NHPC": "NHPC",
    "NTPC": "NTPC",
    "ONGC": "ONGC",
    "PETRONET": "PETLNG",
    "RELIANCE": "RELIND",
    "SJVN": "SJVLIM",
    "TATACONSUM": "TATGLO",
    "TATAPOWER": "TATPOW",
    "VIYASH": "SEQSCI",
    "WIPRO": "WIPRO",
}


def load_upstox_exports(paths: list[str]) -> pd.DataFrame:
    frames = []
    for p in paths:
        raw = pd.read_csv(p)
        raw.columns = raw.columns.str.strip()
        
        # Check direct UPSTOX_COLUMN_MAP matches
        col_map = {}
        for orig_col, target_col in UPSTOX_COLUMN_MAP.items():
            if orig_col in raw.columns:
                col_map[orig_col] = target_col
        
        # Fallback to alias matching if needed
        if len(col_map) < len(UPSTOX_COLUMN_MAP):
            raw_cols_lower = {c.lower(): c for c in raw.columns}
            col_map = {}
            missing_targets = []
            for target_col, aliases in HEADER_ALIASES.items():
                matched_col = None
                for alias in aliases:
                    if alias in raw_cols_lower:
                        matched_col = raw_cols_lower[alias]
                        break
                if matched_col:
                    col_map[matched_col] = target_col
                else:
                    missing_targets.append(target_col)
            
            if missing_targets:
                raise ValueError(
                    f"{p}: expected fields for {missing_targets} not found. "
                    f"Actual columns: {list(raw.columns)}."
                )

        norm = raw.rename(columns=col_map)[[c for c in col_map.values() if c in ("Date", "Stock Symbol", "Action", "Qty", "Price")]]
        norm["Stock Symbol"] = norm["Stock Symbol"].astype(str).str.strip()
        norm["Stock Symbol"] = norm["Stock Symbol"].map(lambda s: UPSTOX_SYMBOL_MAP.get(s, s))
        norm["Action"] = norm["Action"].astype(str).str.strip().str.upper()
        norm["Notes"] = "upstox order book import"
        frames.append(norm)
        
    combined = pd.concat(frames, ignore_index=True)
    combined = combined.drop_duplicates()
    combined["Date"] = pd.to_datetime(combined["Date"], format="mixed").dt.strftime("%Y-%m-%d")
    return combined.sort_values(["Stock Symbol", "Date"])


def reconcile(trades: pd.DataFrame, portfolio_path: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    port = pd.read_csv(portfolio_path)
    port.columns = port.columns.str.strip()
    port_symbols = set(port["Stock Symbol"].astype(str).str.strip())

    if trades.empty:
        net_qty = pd.Series(dtype=float)
    else:
        clean_trades = trades.copy()
        clean_trades["Stock Symbol"] = clean_trades["Stock Symbol"].astype(str).str.strip()
        clean_trades["Action"] = clean_trades["Action"].astype(str).str.strip().str.upper()
        
        numeric_trades = clean_trades[pd.to_numeric(clean_trades["Qty"], errors="coerce").notna()].copy()
        numeric_trades["Qty_num"] = numeric_trades["Qty"].astype(float)
        numeric_trades["signed_qty"] = numeric_trades.apply(
            lambda r: r["Qty_num"] if r["Action"] == "BUY" else (-r["Qty_num"] if r["Action"] == "SELL" else 0.0),
            axis=1
        )
        net_qty = numeric_trades.groupby("Stock Symbol")["signed_qty"].sum()

    report_rows = []
    for _, row in port.iterrows():
        sym = str(row["Stock Symbol"]).strip()
        held_qty = float(row["Qty"])
        computed_qty = net_qty.get(sym, None)
        
        if computed_qty is None or computed_qty == 0:
            status = "PARTIAL HISTORY"
        elif abs(computed_qty - held_qty) < 0.01:
            status = "OK"
        elif computed_qty < held_qty:
            status = "PARTIAL HISTORY"
        else:
            status = "MISMATCH"
            
        report_rows.append({"Stock Symbol": sym, "Portfolio Qty": int(held_qty), "Extracted Qty": int(computed_qty) if computed_qty is not None else 0, "Status": status})

    missing_syms = port_symbols - set(net_qty.index if not net_qty.empty else [])
    for sym in missing_syms:
        trades = pd.concat([trades, pd.DataFrame([{
            "Date": "",
            "Stock Symbol": sym,
            "Action": "",
            "Qty": "",
            "Price": "",
            "Notes": "NO TRADE HISTORY FOUND - manual entry required",
        }])], ignore_index=True)

    return trades, pd.DataFrame(report_rows)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ingest_trades.py <upstox_export_1.csv> [more...]")
        sys.exit(1)

    trades = load_upstox_exports(sys.argv[1:])
    trades, reconciliation = reconcile(trades, PORTFOLIO_FILE)

    trades.to_csv(OUTPUT_FILE, index=False)

    print(f"\nWrote {len(trades)} rows to {OUTPUT_FILE}\n")
    print("=== RECONCILIATION REPORT (portfolio.csv vs order book) ===")
    print(reconciliation.to_string(index=False))

    # Auto-refresh portfolio.csv to ensure portfolio.csv and trades.csv never silently drift apart
    from refresh_portfolio import refresh_portfolio
    refresh_portfolio(OUTPUT_FILE, PORTFOLIO_FILE)
    print(f"\nSuccessfully refreshed {PORTFOLIO_FILE} from {OUTPUT_FILE}")


if __name__ == "__main__":
    main()


