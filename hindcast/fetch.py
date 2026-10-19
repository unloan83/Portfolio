"""Download daily prices once into data/prices/ (the only networked step).

Usage: python -m hindcast.fetch [--start 2017-06-01]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from analysis import TICKER_MAP  # noqa: E402
from hindcast.data import ALTERNATE_TICKERS, BENCHMARK_TICKER, PRICE_DIR, RENAMES  # noqa: E402


def tickers_to_fetch(portfolio_csv: Path = ROOT / "portfolio.csv") -> list[str]:
    symbols = pd.read_csv(portfolio_csv)["Stock Symbol"].astype(str).str.strip()
    out = {BENCHMARK_TICKER}
    for sym in symbols:
        out.update(ALTERNATE_TICKERS.get(sym, [TICKER_MAP.get(sym, f"{sym}.NS")]))
    for new, (old, _) in RENAMES.items():
        if new in out:
            out.add(old)
    return sorted(t for t in out if t not in ("UNLISTED", "TODO_VERIFY"))


def _save(df: pd.DataFrame, path: Path) -> int:
    if df is None or df.empty:
        return 0
    df = df.copy()
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df.index = pd.DatetimeIndex(df.index).tz_localize(None).normalize()
    df.index.name = "Date"
    cols = [c for c in ("Open", "High", "Low", "Close", "Volume") if c in df.columns]
    df = df[cols].dropna(subset=["Close"])
    path.parent.mkdir(parents=True, exist_ok=True)
    df.round(6).to_csv(path)
    return len(df)


def main(argv=None) -> int:
    import yfinance as yf

    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="2017-06-01")
    args = ap.parse_args(argv)

    manifest = {
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "yfinance_version": getattr(yf, "__version__", "unknown"),
        "start": args.start,
        "files": {},
    }
    for ticker in tickers_to_fetch():
        for kind, auto in (("adj", True), ("raw", False)):
            path = PRICE_DIR / kind / f"{ticker}.csv"
            try:
                df = yf.Ticker(ticker).history(start=args.start, auto_adjust=auto, actions=False)
            except Exception as exc:  # recorded, never fatal: the run marks the symbol MISSING
                print(f"[warn] {ticker} ({kind}): {type(exc).__name__}: {exc}")
                df = None
            rows = _save(df, path)
            entry = {"rows": rows}
            if rows:
                entry["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
                entry["first"] = str(pd.read_csv(path, nrows=1)["Date"].iloc[0])
            manifest["files"][f"{kind}/{ticker}.csv"] = entry
            print(f"{kind:3s} {ticker:16s} rows={rows}")
    (PRICE_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True))
    missing = [k for k, v in manifest["files"].items() if not v["rows"]]
    print(f"done; {len(missing)} empty file(s): {missing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
