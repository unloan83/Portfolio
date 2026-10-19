"""
performance.py

Calculates portfolio and per-holding XIRR against benchmark (^NSEI)
using trade cash flows from trades.csv and current holdings valuation.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple
import numpy as np
import pandas as pd
import scipy.optimize
import yfinance as yf


def xirr(cash_flows: List[float], dates: List[Any]) -> Optional[float]:
    """Computes Extended Internal Rate of Return (XIRR) for irregular cash flows."""
    if len(cash_flows) < 2 or len(cash_flows) != len(dates):
        return None

    clean_dates = [pd.to_datetime(d).tz_localize(None) if hasattr(pd.to_datetime(d), "tz_localize") else pd.to_datetime(d) for d in dates]
    cfs = np.array(cash_flows, dtype=float)

    # Need at least one positive and one negative cash flow
    has_pos = np.any(cfs > 0)
    has_neg = np.any(cfs < 0)
    if not (has_pos and has_neg):
        return None

    # Sort chronologically
    sort_idx = np.argsort(clean_dates)
    clean_dates = [clean_dates[i] for i in sort_idx]
    cfs = cfs[sort_idx]

    d0 = clean_dates[0]
    years = np.array([(d - d0).days / 365.0 for d in clean_dates])

    def npv(r: float) -> float:
        if r <= -0.999:
            return float("inf")
        return float(np.sum(cfs / ((1.0 + r) ** years)))

    try:
        f_low = npv(-0.99)
        f_high = npv(10.0)
        if f_low * f_high <= 0:
            return float(scipy.optimize.brentq(npv, -0.99, 10.0))
        return float(scipy.optimize.newton(npv, 0.1, maxiter=200))
    except Exception:
        return None


def calculate_portfolio_and_benchmark_xirr(
    trades_df: pd.DataFrame,
    portfolio_df: pd.DataFrame,
    current_prices: Optional[Dict[str, float]] = None,
    benchmark_history: Optional[pd.DataFrame] = None,
    valuation_date: Optional[datetime] = None,
) -> Dict[str, Any]:
    """Calculates portfolio XIRR, benchmark XIRR, per-holding XIRRs, and coverage gaps."""
    if valuation_date is None:
        valuation_date = datetime.now()
    val_date = pd.to_datetime(valuation_date).tz_localize(None).normalize()

    # Clean and filter valid trades
    trades = trades_df.copy()
    valid_trades = trades[
        pd.to_datetime(trades["Date"], errors="coerce").notna()
        & pd.to_numeric(trades["Qty"], errors="coerce").notna()
        & pd.to_numeric(trades["Price"], errors="coerce").notna()
    ].copy()
    valid_trades["Date"] = pd.to_datetime(valid_trades["Date"]).dt.tz_localize(None).dt.normalize()
    valid_trades["Qty"] = valid_trades["Qty"].astype(float)
    valid_trades["Price"] = valid_trades["Price"].astype(float)
    valid_trades["Action"] = valid_trades["Action"].astype(str).str.strip().str.upper()
    valid_trades = valid_trades.sort_values("Date")

    # Map current prices
    prices: Dict[str, float] = {}
    if current_prices:
        prices.update(current_prices)
    for _, row in portfolio_df.iterrows():
        sym = str(row["Stock Symbol"]).strip()
        if sym not in prices and "Current Market Price" in row and pd.notna(row["Current Market Price"]):
            prices[sym] = float(row["Current Market Price"])

    # Fetch benchmark history if not provided
    benchmark_note = "Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)"
    if benchmark_history is None or benchmark_history.empty:
        try:
            t = yf.Ticker("^NSEI")
            earliest_date = valid_trades["Date"].min() if not valid_trades.empty else val_date
            bench_raw = t.history(start=earliest_date.strftime("%Y-%m-%d"))
            if not bench_raw.empty:
                benchmark_history = bench_raw
        except Exception:
            benchmark_history = pd.DataFrame()

    if benchmark_history is not None and not benchmark_history.empty:
        bench_df = benchmark_history.copy()
        bench_df.index = pd.to_datetime(bench_df.index).tz_localize(None).normalize()
        bench_close = bench_df["Close"].dropna()
    else:
        bench_close = pd.Series(dtype=float)

    # Cash flows tracking
    portfolio_cfs: List[float] = []
    portfolio_dates: List[pd.Timestamp] = []
    benchmark_cfs: List[float] = []
    benchmark_dates: List[pd.Timestamp] = []
    bench_units = 0.0

    symbol_trades: Dict[str, List[Tuple[pd.Timestamp, float, float, str]]] = {}

    for _, r in valid_trades.iterrows():
        d = r["Date"]
        q = r["Qty"]
        p = r["Price"]
        act = r["Action"]
        sym = str(r["Stock Symbol"]).strip()
        amt = q * p

        symbol_trades.setdefault(sym, []).append((d, q, p, act))

        if act == "BUY":
            portfolio_cfs.append(-amt)
            portfolio_dates.append(d)
            if not bench_close.empty:
                sub = bench_close[bench_close.index <= d]
                bp = sub.iloc[-1] if not sub.empty else bench_close.iloc[0]
                bench_units += amt / bp
                benchmark_cfs.append(-amt)
                benchmark_dates.append(d)
        elif act == "SELL":
            portfolio_cfs.append(amt)
            portfolio_dates.append(d)
            if not bench_close.empty:
                sub = bench_close[bench_close.index <= d]
                bp = sub.iloc[-1] if not sub.empty else bench_close.iloc[0]
                bench_units -= amt / bp
                benchmark_cfs.append(amt)
                benchmark_dates.append(d)

    # Determine terminal values from trades
    net_qty_from_trades: Dict[str, float] = {}
    for sym, tr_list in symbol_trades.items():
        net_q = sum(q if act == "BUY" else -q for _, q, _, act in tr_list)
        net_qty_from_trades[sym] = max(0.0, net_q)

    # Terminal valuation for portfolio
    terminal_portfolio_val = 0.0
    for sym, net_q in net_qty_from_trades.items():
        if net_q > 0:
            px = prices.get(sym, 0.0)
            terminal_portfolio_val += net_q * px

    if portfolio_cfs:
        portfolio_cfs.append(terminal_portfolio_val)
        portfolio_dates.append(val_date)
        port_xirr_val = xirr(portfolio_cfs, portfolio_dates)
    else:
        port_xirr_val = None

    # Benchmark terminal valuation
    if benchmark_cfs and not bench_close.empty:
        val_bench_px = bench_close.iloc[-1]
        terminal_bench_val = bench_units * val_bench_px
        benchmark_cfs.append(terminal_bench_val)
        benchmark_dates.append(val_date)
        bench_xirr_val = xirr(benchmark_cfs, benchmark_dates)
    else:
        bench_xirr_val = None
        terminal_bench_val = 0.0

    # Per-holding XIRR
    holding_xirrs: List[Dict[str, Any]] = []
    for _, prow in portfolio_df.iterrows():
        sym = str(prow["Stock Symbol"]).strip()
        held_qty = float(prow["Qty"])
        px = prices.get(sym, float(prow.get("Current Market Price", 0.0)))
        tr_list = symbol_trades.get(sym, [])

        if not tr_list:
            continue

        sym_cfs: List[float] = []
        sym_dates: List[pd.Timestamp] = []
        net_q = 0.0
        for td, tq, tp, tact in tr_list:
            if tact == "BUY":
                sym_cfs.append(-(tq * tp))
                sym_dates.append(td)
                net_q += tq
            elif tact == "SELL":
                sym_cfs.append(tq * tp)
                sym_dates.append(td)
                net_q -= tq

        if net_q > 0:
            sym_cfs.append(net_q * px)
            sym_dates.append(val_date)

        h_xirr = xirr(sym_cfs, sym_dates)
        holding_xirrs.append({
            "Stock Symbol": sym,
            "Held Qty": held_qty,
            "Trades Qty": net_q,
            "Current Price": px,
            "Current Value": net_q * px,
            "XIRR": h_xirr,
        })

    # Coverage gaps
    port_syms = set(portfolio_df["Stock Symbol"].astype(str).str.strip())
    traded_syms = set(symbol_trades.keys())
    missing_completely = sorted(list(port_syms - traded_syms))

    partial_history: List[Dict[str, Any]] = []
    for _, prow in portfolio_df.iterrows():
        sym = str(prow["Stock Symbol"]).strip()
        held_qty = float(prow["Qty"])
        extracted_qty = net_qty_from_trades.get(sym, 0.0)
        if sym in traded_syms and abs(held_qty - extracted_qty) > 0.01:
            partial_history.append({
                "Stock Symbol": sym,
                "Portfolio Qty": held_qty,
                "Trades Qty": extracted_qty,
                "Difference": held_qty - extracted_qty,
            })

    return {
        "portfolio_xirr": port_xirr_val,
        "benchmark_xirr": bench_xirr_val,
        "benchmark_note": benchmark_note,
        "terminal_portfolio_val": terminal_portfolio_val,
        "terminal_benchmark_val": terminal_bench_val,
        "first_trade_date": valid_trades["Date"].min().strftime("%Y-%m-%d") if not valid_trades.empty else "N/A",
        "valuation_date": val_date.strftime("%Y-%m-%d"),
        "holding_xirrs": holding_xirrs,
        "missing_completely": missing_completely,
        "partial_history": partial_history,
    }


def format_performance_markdown(perf: Dict[str, Any]) -> str:
    """Formats performance calculations into markdown for README.md."""
    p_xirr = f"{perf['portfolio_xirr']:.2%}" if perf.get("portfolio_xirr") is not None else "N/A"
    b_xirr = f"{perf['benchmark_xirr']:.2%}" if perf.get("benchmark_xirr") is not None else "N/A"
    p_term = f"₹{perf['terminal_portfolio_val']:,.0f}" if perf.get("terminal_portfolio_val") is not None else "N/A"
    b_term = f"₹{perf['terminal_benchmark_val']:,.0f}" if perf.get("terminal_benchmark_val") is not None else "N/A"

    md = "### Portfolio Performance vs Benchmark\n\n"
    md += f"* **First Recorded Trade**: {perf.get('first_trade_date', 'N/A')}\n"
    md += f"* **Valuation Date**: {perf.get('valuation_date', 'N/A')}\n"
    md += f"* **Portfolio XIRR**: **{p_xirr}** (Current Traded Positions Value: {p_term})\n"
    md += f"* **Benchmark XIRR**: **{b_xirr}** (Simulated Benchmark Value: {b_term})\n"
    md += f"* *{perf.get('benchmark_note', '')}*\n\n"

    # Per-holding XIRR table
    hx = perf.get("holding_xirrs", [])
    if hx:
        md += "#### Holding-Level XIRR (From Trade Cash Flows)\n\n"
        rows = []
        for h in sorted(hx, key=lambda x: (x["XIRR"] is None, -(x["XIRR"] or -999))):
            xirr_str = f"{h['XIRR']:.2%}" if h["XIRR"] is not None else "N/A"
            held = int(h["Held Qty"])
            traded = int(h["Trades Qty"])
            status = "Full" if held == traded else f"Partial ({traded}/{held} sh)"
            rows.append({
                "Symbol": h["Stock Symbol"],
                "Held Qty": held,
                "Traded Qty": traded,
                "Current Value": f"₹{h['Current Value']:,.0f}",
                "XIRR": xirr_str,
                "History": status,
            })
        md += pd.DataFrame(rows).to_markdown(index=False) + "\n\n"

    # Coverage gaps
    missing = perf.get("missing_completely", [])
    partial = perf.get("partial_history", [])
    if missing or partial:
        md += "#### Trade History Coverage Gaps\n\n"
        if missing:
            md += f"* **Missing Holdings (No trades recorded in `trades.csv`)**: {', '.join(f'`{m}`' for m in missing)}\n"
        if partial:
            md += "* **Partial Trade History (`trades.csv` shares < `portfolio.csv` shares)**:\n"
            for p in partial:
                md += f"  - `{p['Stock Symbol']}`: Portfolio has {int(p['Portfolio Qty'])} sh, trades record {int(p['Trades Qty'])} sh (unrecorded: {int(p['Difference'])} sh)\n"
        md += "\n"

    return md

