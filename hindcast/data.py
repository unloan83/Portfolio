"""Price cache loading, ticker stitching and corporate-action repair (offline)."""
from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PRICE_DIR = ROOT / "data" / "prices"
CA_FILE = ROOT / "data" / "corporate_actions.csv"
BENCHMARK_TICKER = "NIFTYBEES.NS"

# Renamed listings: new ticker -> (old ticker, change date). History before the
# change lives under the old ticker on Yahoo.
RENAMES = {
    "VIYASH.NS": ("SEQUENT.NS", "2026-01-23"),
    "GUJENERGY.NS": ("GUJGASLTD.NS", "2026-05-14"),
}

# Broker symbols whose TICKER_MAP entry has a thin series; the alternatives are
# tried and the longest history wins.
ALTERNATE_TICKERS = {
    "ICINIF": ["537007.BO", "NIFTYIETF.NS"],
}

PRICE_COLS = ["Open", "High", "Low", "Close"]
# A one-day move outside this band that no known event explains is logged as suspect.
SUSPECT_JUMP = 0.35
# How close an observed one-day ratio must be to the event factor to count as the event.
EVENT_TOLERANCE = 0.15
EVENT_WINDOW_SESSIONS = 5


@dataclass
class SeriesInfo:
    ticker: str
    tags: list[str] = field(default_factory=list)
    log: list[str] = field(default_factory=list)


def _read_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
    df.index = pd.DatetimeIndex(df.index).tz_localize(None).normalize()
    df = df[~df.index.duplicated(keep="last")].sort_index()
    return df[[c for c in PRICE_COLS if c in df.columns]].dropna(subset=["Close"])


def load_adjusted(ticker: str, price_dir: Path = PRICE_DIR) -> Optional[pd.DataFrame]:
    path = price_dir / "adj" / f"{ticker}.csv"
    if not path.exists():
        return None
    df = _read_csv(path)
    return df if not df.empty else None


def stitch(new: Optional[pd.DataFrame], old: Optional[pd.DataFrame], change_date: str) -> Optional[pd.DataFrame]:
    """Old-ticker bars before the first new-ticker bar, scaled to meet the new series."""
    if old is None:
        return new
    if new is None:
        return old
    first_new = new.index[0]
    head = old[old.index < first_new]
    if head.empty:
        return new
    common = old.index.intersection(new.index)
    if len(common):
        scale = new.loc[common[0], "Close"] / old.loc[common[0], "Close"]
        head = head * scale
    return pd.concat([head, new]).sort_index()


def load_corporate_actions(path: Path = CA_FILE) -> list[dict]:
    if not path.exists():
        return []
    with open(path, newline="") as fh:
        return [row for row in csv.DictReader(fh)]


def apply_corporate_actions(df: pd.DataFrame, ticker: str, events: list[dict], info: SeriesInfo) -> pd.DataFrame:
    """Back-adjust bars before any known split/bonus/demerger that the series still shows.

    Splits and bonuses use the table factor (new/old price) once the observed
    one-day ratio near the ex-date matches it. Demergers use the observed drop,
    which treats the value passed to the child company as retained.
    """
    out = df.copy()
    ratios = (out["Close"] / out["Close"].shift(1)).dropna()
    explained: set[pd.Timestamp] = set()
    for ev in events:
        if ev.get("symbol") != ticker:
            continue
        ex = pd.Timestamp(ev["ex_date"])
        pos = out.index.searchsorted(ex)
        lo, hi = max(1, pos - EVENT_WINDOW_SESSIONS), min(len(out), pos + EVENT_WINDOW_SESSIONS + 1)
        window = ratios.loc[out.index[lo]:out.index[hi - 1]] if hi > lo else ratios.iloc[0:0]
        kind = ev.get("type", "").strip().lower()
        status = ev.get("status", "").strip().lower()
        label = f"{ticker} {kind} {ev['ex_date']} ({status})"
        if window.empty:
            info.log.append(f"{label}: outside data range")
            continue
        if kind == "demerger":
            day = window.idxmin()
            r = float(window.loc[day])
            if r < 0.97:
                out.loc[out.index < day, PRICE_COLS] *= r
                explained.add(day)
                info.tags.append("ADJ_DEMERGER_OBSERVED")
                info.log.append(f"{label}: observed drop x{r:.3f} on {day.date()} back-adjusted")
            else:
                info.log.append(f"{label}: no drop found; assumed already adjusted")
            continue
        factor = float(ev["ratio"])
        distance = (window / factor - 1.0).abs()
        day = distance.idxmin()
        if float(distance.loc[day]) <= EVENT_TOLERANCE:
            out.loc[out.index < day, PRICE_COLS] *= factor
            explained.add(day)
            info.tags.append("ADJ_FIXED")
            info.log.append(f"{label}: unadjusted x{float(window.loc[day]):.3f} on {day.date()} fixed with factor {factor:.4f}")
        else:
            info.log.append(f"{label}: series already adjusted (max one-day move in window x{float(window.min()):.3f})")
    # Anything still jumping beyond the suspect band is reported, not repaired.
    new_ratios = (out["Close"] / out["Close"].shift(1)).dropna()
    suspect = new_ratios[((new_ratios - 1.0).abs() > SUSPECT_JUMP) & ~new_ratios.index.isin(list(explained))]
    for day, r in suspect.items():
        info.tags.append("CA_SUSPECT")
        info.log.append(f"{ticker}: unexplained one-day move x{float(r):.3f} on {day.date()}")
    return out


def load_symbol(broker_symbol: str, ticker: str, events: list[dict], price_dir: Path = PRICE_DIR) -> tuple[Optional[pd.DataFrame], SeriesInfo]:
    candidates = ALTERNATE_TICKERS.get(broker_symbol, [ticker])
    best, best_ticker = None, ticker
    for cand in candidates:
        df = load_adjusted(cand, price_dir)
        if cand in RENAMES:
            old_ticker, change = RENAMES[cand]
            df = stitch(df, load_adjusted(old_ticker, price_dir), change)
        if df is not None and (best is None or len(df) > len(best)):
            best, best_ticker = df, cand
    info = SeriesInfo(ticker=best_ticker)
    if best is None:
        info.tags.append("MISSING")
        return None, info
    if best_ticker in RENAMES:
        info.tags.append("STITCHED")
    return apply_corporate_actions(best, best_ticker, events, info), info
