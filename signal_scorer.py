"""Signal Scorer for evaluating historical signals against N-day forward returns."""
from datetime import datetime
import os
from zoneinfo import ZoneInfo
import pandas as pd
import yfinance as yf

from analysis import TICKER_MAP

FAILURE_TRENDS = {"NO_DATA", "FETCH_ERROR", "NO_TICKER"}


def load_price_history(symbol: str) -> pd.DataFrame:
    yf_symbol = TICKER_MAP.get(symbol, f"{symbol}.NS")
    if yf_symbol in ("UNLISTED", "TODO_VERIFY"):
        return pd.DataFrame()
    try:
        data = yf.Ticker(yf_symbol).history(period="1y")
        if data.empty:
            return pd.DataFrame()
        data.index = pd.to_datetime(data.index).tz_localize(None).normalize()
        return data.sort_index()
    except Exception as exc:
        print(f"[warn] Failed fetching history for {symbol} ({yf_symbol}): {exc}")
        return pd.DataFrame()


def score_signals(
    tracking_file: str = "re-engineering.csv",
    output_file: str = "reports/signal_scores.csv",
    ticker_history_loader=load_price_history,
) -> pd.DataFrame:
    if not os.path.exists(tracking_file):
        print(f"[warn] Tracking file {tracking_file} does not exist.")
        return pd.DataFrame()

    tracking_df = pd.read_csv(tracking_file)
    if tracking_df.empty:
        return pd.DataFrame()

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Load existing scores to prevent re-scoring
    existing_scores = {}
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        scores_df = pd.read_csv(output_file)
        for _, r in scores_df.iterrows():
            key = (str(r["symbol"]).strip(), str(r["original_run_timestamp"]).strip())
            existing_scores[key] = r.to_dict()

    now_ist = datetime.now(ZoneInfo("Asia/Kolkata"))
    scored_at_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    # Filter out failure states
    evaluable_mask = (
        ~tracking_df["technical_trend"].astype(str).isin(FAILURE_TRENDS)
    ) & (tracking_df["Model_Signal"].astype(str) != "⚪ NO DATA")

    if "Price_At_Signal" in tracking_df.columns:
        evaluable_mask &= tracking_df["Price_At_Signal"].notna()

    evaluable_df = tracking_df[evaluable_mask].copy()

    # Pre-fetch market history for required symbols
    symbols_needed = evaluable_df["Stock_Symbol"].astype(str).str.strip().unique()
    price_histories = {}
    for sym in symbols_needed:
        hist = ticker_history_loader(sym)
        if not hist.empty:
            price_histories[sym] = hist

    updated_scores = dict(existing_scores)

    for _, row in evaluable_df.iterrows():
        symbol = str(row["Stock_Symbol"]).strip()

        # Determine original timestamp
        if "run_timestamp_ist" in row and pd.notna(row["run_timestamp_ist"]):
            orig_ts = str(row["run_timestamp_ist"]).strip()
        else:
            orig_ts = str(row["Analysis_Date"]).strip()

        key = (symbol, orig_ts)

        # Check if already fully scored in existing_scores
        if key in existing_scores:
            existing = existing_scores[key]
            if (
                pd.notna(existing.get("return_5d_pct"))
                and pd.notna(existing.get("return_10d_pct"))
                and pd.notna(existing.get("return_20d_pct"))
            ):
                continue

        hist = price_histories.get(symbol)
        if hist is None or hist.empty:
            continue

        # Find signal date in history
        signal_date = pd.to_datetime(row["Analysis_Date"]).normalize()

        # Locate entry bar (signal_date or first available bar on/after signal_date)
        entry_bars = hist.index[hist.index >= signal_date]
        if entry_bars.empty:
            continue

        entry_idx = hist.index.get_loc(entry_bars[0])

        # Available trading bars after entry bar
        bars_after = len(hist) - 1 - entry_idx
        if bars_after < 5:
            # Not old enough yet for even 5 trading days
            continue

        # Get price at signal
        if "Price_At_Signal" in row and pd.notna(row["Price_At_Signal"]):
            price_at_signal = float(row["Price_At_Signal"])
        else:
            price_at_signal = float(hist.iloc[entry_idx]["Close"])

        if price_at_signal <= 0:
            continue

        signal_str = str(row["Model_Signal"]).strip()

        # Compute 5d
        price_5d, ret_5d = None, None
        if bars_after >= 5:
            close_col = "Close" if "Close" in hist.columns else "close"
            price_5d = round(float(hist.iloc[entry_idx + 5][close_col]), 2)
            ret_5d = round(((price_5d - price_at_signal) / price_at_signal) * 100, 2)

        # Compute 10d
        price_10d, ret_10d = None, None
        if bars_after >= 10:
            close_col = "Close" if "Close" in hist.columns else "close"
            price_10d = round(float(hist.iloc[entry_idx + 10][close_col]), 2)
            ret_10d = round(((price_10d - price_at_signal) / price_at_signal) * 100, 2)

        # Compute 20d
        price_20d, ret_20d = None, None
        if bars_after >= 20:
            close_col = "Close" if "Close" in hist.columns else "close"
            price_20d = round(float(hist.iloc[entry_idx + 20][close_col]), 2)
            ret_20d = round(((price_20d - price_at_signal) / price_at_signal) * 100, 2)

        existing_rec = updated_scores.get(key, {})
        row_scored_at = existing_rec.get("scored_at", scored_at_str)

        updated_scores[key] = {
            "symbol": symbol,
            "original_run_timestamp": orig_ts,
            "signal": signal_str,
            "price_at_signal": round(price_at_signal, 2),
            "price_5d_after": price_5d,
            "return_5d_pct": ret_5d,
            "price_10d_after": price_10d,
            "return_10d_pct": ret_10d,
            "price_20d_after": price_20d,
            "return_20d_pct": ret_20d,
            "scored_at": row_scored_at,
        }

    cols = [
        "symbol",
        "original_run_timestamp",
        "signal",
        "price_at_signal",
        "price_5d_after",
        "return_5d_pct",
        "price_10d_after",
        "return_10d_pct",
        "price_20d_after",
        "return_20d_pct",
        "scored_at",
    ]

    out_df = (
        pd.DataFrame(list(updated_scores.values()), columns=cols)
        if updated_scores
        else pd.DataFrame(columns=cols)
    )
    out_df.to_csv(output_file, index=False)
    return out_df


if __name__ == "__main__":
    score_signals()
