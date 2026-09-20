"""Validated Yahoo Finance history adapter for backtests."""
from __future__ import annotations

import pandas as pd
import yfinance as yf


REQUIRED_COLUMNS = ("open", "high", "low", "close", "volume")


def fetch_history(symbol: str, period: str = "3y") -> pd.DataFrame:
    """Fetch adjusted daily history and normalize it for the backtester."""
    try:
        frame = yf.Ticker(symbol).history(period=period, auto_adjust=True)
    except Exception as exc:
        raise RuntimeError(
            f"Yahoo history fetch failed for {symbol}: {type(exc).__name__}: {exc}"
        ) from exc

    if frame.empty:
        raise ValueError(f"Yahoo returned no {period} history for {symbol}")

    frame = frame.rename(columns=str.lower)
    missing = [column for column in REQUIRED_COLUMNS if column not in frame.columns]
    if missing:
        raise ValueError(f"Yahoo history for {symbol} is missing columns: {missing}")

    frame = frame.loc[:, REQUIRED_COLUMNS].copy()
    if frame.index.has_duplicates:
        raise ValueError(f"Yahoo history for {symbol} contains duplicate dates")
    if not frame.index.is_monotonic_increasing:
        frame = frame.sort_index()
    invalid_ohlc = (
        (frame["low"] > frame["open"])
        | (frame["low"] > frame["close"])
        | (frame["high"] < frame["open"])
        | (frame["high"] < frame["close"])
        | (frame["high"] < frame["low"])
        | (frame["volume"] < 0)
    )
    if invalid_ohlc.any():
        raise ValueError(f"Yahoo history for {symbol} contains invalid OHLCV rows")
    return frame.dropna(subset=["open", "high", "low", "close"])
