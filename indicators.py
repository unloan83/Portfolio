"""Dependency-light technical indicators for pandas market-data frames."""
import numpy as np
import pandas as pd


def sma(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window).mean()


def ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False).mean()


def rsi(series: pd.Series, window: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / window, min_periods=window, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / window, min_periods=window, adjust=False).mean()
    relative_strength = avg_gain / avg_loss.replace(0, np.nan)
    return (100 - (100 / (1 + relative_strength))).fillna(50)


def atr(df: pd.DataFrame, window: int = 14) -> pd.Series:
    high, low, close = df["high"], df["low"], df["close"]
    previous_close = close.shift(1)
    true_range = pd.concat(
        [
            high - low,
            (high - previous_close).abs(),
            (low - previous_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    return true_range.ewm(alpha=1 / window, min_periods=window, adjust=False).mean()


def macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    macd_line = ema(series, fast) - ema(series, slow)
    signal_line = ema(macd_line, signal)
    return macd_line, signal_line, macd_line - signal_line


def bollinger_bands(series: pd.Series, window: int = 20, num_std: float = 2.0):
    middle = sma(series, window)
    standard_deviation = series.rolling(window).std()
    return middle + num_std * standard_deviation, middle, middle - num_std * standard_deviation


def vwap(df: pd.DataFrame) -> pd.Series:
    """Session VWAP; callers must reset the frame at session boundaries."""
    typical_price = (df["high"] + df["low"] + df["close"]) / 3
    cumulative_volume = df["volume"].cumsum()
    return (typical_price * df["volume"]).cumsum() / cumulative_volume.replace(0, np.nan)


def momentum_score(series: pd.Series, lookback: int = 126) -> float:
    window = series.tail(lookback)
    if len(window) < lookback // 2:
        return float("nan")
    total_return = window.iloc[-1] / window.iloc[0] - 1
    volatility = window.pct_change().dropna().std() * np.sqrt(252)
    if volatility == 0 or np.isnan(volatility):
        return float("nan")
    return total_return / volatility


def trend_state(df: pd.DataFrame) -> str:
    """Return ``uptrend``, ``downtrend``, or ``choppy`` from EMA structure."""
    close = df["close"]
    ema_20, ema_50, ema_200 = ema(close, 20), ema(close, 50), ema(close, 200)
    latest = close.iloc[-1]
    if ema_20.iloc[-1] > ema_50.iloc[-1] > ema_200.iloc[-1] and latest > ema_20.iloc[-1]:
        return "uptrend"
    if ema_20.iloc[-1] < ema_50.iloc[-1] < ema_200.iloc[-1] and latest < ema_20.iloc[-1]:
        return "downtrend"
    return "choppy"
