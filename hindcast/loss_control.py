"""Stock-market-only loss-control test: do simple, pre-specified rules cut drawdowns, and at what cost?

Usage: python -m hindcast.loss_control   (offline; uses the data/prices cache)

Rules are taken from published work, not fitted here:
  B. 10-month SMA (Faber 2007): invested when the month-end close is above the
     average of the last 10 month-end closes, otherwise in cash.
  C. 200-day SMA with a 2% band: exit below 0.98 x SMA, re-enter above 1.02 x SMA.
  D. Volatility target (Moreira & Muir 2017): exposure = min(1, 15% / 60-day
     realised vol), changed only when it moves by more than 0.10.
Signals use the close of day t; trades fill at the close of t+1, so they earn
returns from t+2 (no look-ahead). Switches cost 0.10% per unit traded. Cash earns
CASH_RATE (liquid-fund proxy); a 0% cash run is reported as a sensitivity.

Writes reports/loss_control_test.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from hindcast.run import load_universe  # noqa: E402

COST = 0.001
CASH_RATE = 0.055
DAYS = 252
ETF_HINTS = ("ETF", "BEES", "BANKNIFTY", "537007", "HDFCSML250")
WINDOWS = {"COVID crash (Jan-Jun 2020)": ("2020-01-01", "2020-06-30"),
           "2024-25 correction (Sep 2024-Mar 2025)": ("2024-09-01", "2025-03-31")}
OUT = ROOT / "reports" / "loss_control_test.md"


# ---------- signals (all use data up to and including day t only) ----------

def sig_buy_hold(c: pd.Series) -> pd.Series:
    return pd.Series(1.0, index=c.index)


def sig_sma_months(c: pd.Series, months: int = 10) -> pd.Series:
    me = c.groupby(c.index.to_period("M")).tail(1)
    on = (me > me.rolling(months).mean()).astype(float).where(me.rolling(months).count() == months)
    return on.reindex(c.index).ffill().fillna(1.0)  # before enough history: invested (same as buy-hold)


def sig_sma_band(c: pd.Series, days: int = 200, band: float = 0.02) -> pd.Series:
    sma = c.rolling(days).mean()
    state, out = 1.0, []
    for px, m in zip(c.values, sma.values):
        if not np.isnan(m):
            if state == 1.0 and px < m * (1 - band):
                state = 0.0
            elif state == 0.0 and px > m * (1 + band):
                state = 1.0
        out.append(state)
    return pd.Series(out, index=c.index)


def sig_vol_target(c: pd.Series, target: float = 0.15, lookback: int = 60, step: float = 0.10) -> pd.Series:
    vol = c.pct_change().rolling(lookback).std() * np.sqrt(DAYS)
    raw = (target / vol).clip(upper=1.0)
    w, out = 1.0, []
    for x in raw.values:
        if not np.isnan(x) and abs(x - w) > step:
            w = float(x)
        out.append(w)
    return pd.Series(out, index=c.index)


RULES = {
    "A. Buy and hold": sig_buy_hold,
    "B. 10-month SMA": sig_sma_months,
    "C. 200-day SMA, 2% band": sig_sma_band,
    "D. Vol target 15%": sig_vol_target,
}


# ---------- simulation ----------

def run(asset_ret: pd.Series, signal: pd.Series, cash_rate: float = CASH_RATE) -> pd.Series:
    """Daily strategy returns. Signal at close t -> trade at close t+1 -> earns from t+2."""
    w = signal.shift(2).fillna(signal.iloc[0])
    turnover = w.diff().abs().fillna(0.0)
    cash = (1 + cash_rate) ** (1 / DAYS) - 1
    return w * asset_ret + (1 - w) * cash - turnover * COST


def metrics(r: pd.Series, w: pd.Series | None = None) -> dict:
    eq = (1 + r).cumprod()
    years = len(r) / DAYS
    dd = eq / eq.cummax() - 1
    roll = eq.pct_change(DAYS).dropna()
    out = {"CAGR": eq.iloc[-1] ** (1 / years) - 1, "Max fall": dd.min(),
           "Worst 12m": roll.min() if len(roll) else np.nan,
           "Vol": r.std() * np.sqrt(DAYS)}
    out["Return/fall"] = out["CAGR"] / abs(out["Max fall"]) if out["Max fall"] < 0 else np.nan
    if w is not None:
        out["Invested"] = w.mean()
        out["Switches/yr"] = (w.diff().abs() > 0.05).sum() / years
    return out


def window_fall(r: pd.Series, start: str, end: str) -> float:
    seg = r.loc[start:end]
    eq = (1 + seg).cumprod()
    return float((eq / eq.cummax() - 1).min()) if len(seg) else np.nan


def block_bootstrap(r_rule: pd.Series, r_base: pd.Series, n: int = 2000, block: int = 63, seed: int = 7) -> dict:
    """Paired moving-block resampling: P(rule has the smaller max fall) and P(rule has higher CAGR)."""
    rng = np.random.default_rng(seed)
    a, b = r_rule.values, r_base.values
    T = len(a)
    starts_max = T - block
    smaller_fall = higher_cagr = 0
    for _ in range(n):
        idx = np.concatenate([np.arange(s, s + block) for s in rng.integers(0, starts_max, T // block + 1)])[:T]
        ea, eb = np.cumprod(1 + a[idx]), np.cumprod(1 + b[idx])
        fa = (ea / np.maximum.accumulate(ea) - 1).min()
        fb = (eb / np.maximum.accumulate(eb) - 1).min()
        smaller_fall += fa > fb
        higher_cagr += ea[-1] > eb[-1]
    return {"P(smaller fall)": smaller_fall / n, "P(higher return)": higher_cagr / n}


# ---------- assets ----------

def stock_basket(prices: dict, tickers: dict, index: pd.DatetimeIndex) -> tuple[pd.DataFrame, list[str]]:
    names = [s for s, t in tickers.items() if s in prices and not any(h in t.upper() for h in ETF_HINTS)
             and "GOLD" not in t.upper() and "SILVER" not in t.upper()]
    closes = pd.DataFrame({s: prices[s]["Close"] for s in names}).reindex(index).ffill(limit=5)
    return closes, names


def basket_returns(closes: pd.DataFrame, weights_on: pd.DataFrame | None, cash_rate: float = CASH_RATE) -> tuple[pd.Series, pd.Series]:
    """Equal weight across stocks with data, rebalanced daily (approx. monthly in practice).
    weights_on: per-stock 0/1 signal at close t; executed with the same t+2 lag as `run`."""
    rets = closes.pct_change()
    avail = closes.notna() & closes.shift(1).notna()
    n = avail.sum(axis=1).replace(0, np.nan)
    base_w = avail.div(n, axis=0).fillna(0.0)
    if weights_on is not None:
        on = weights_on.shift(2).reindex(base_w.index).fillna(1.0)
        w = base_w * on
    else:
        w = base_w
    invested = w.sum(axis=1)
    turnover = w.diff().abs().sum(axis=1).fillna(0.0)
    cash = (1 + cash_rate) ** (1 / DAYS) - 1
    r = (w * rets.fillna(0.0)).sum(axis=1) + (1 - invested) * cash - turnover * COST
    return r, invested


# ---------- report ----------

def pct(x: float) -> str:
    return "" if pd.isna(x) else f"{x * 100:.1f}%"


def table(rows: dict[str, dict], cols: list[str]) -> str:
    lines = ["| Rule | " + " | ".join(cols) + " |", "|---" * (len(cols) + 1) + "|"]
    for name, m in rows.items():
        cells = []
        for c in cols:
            v = m.get(c, np.nan)
            if c in ("Switches/yr", "Return/fall"):
                cells.append("" if pd.isna(v) else f"{v:.2f}")
            elif c.startswith("P("):
                cells.append(f"{v:.0%}")
            else:
                cells.append(pct(v))
        lines.append(f"| {name} | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def main() -> int:
    _, prices, tickers, _, bench, _ = load_universe()
    bench = bench.dropna()
    idx = bench.index
    r_idx = bench.pct_change().fillna(0.0)
    start = idx[0] + pd.Timedelta(days=320)  # all rules have their warm-up history from here
    sl = slice(start, idx[-1])

    md = [f"# Stock-market-only loss control test",
          f"",
          f"Data: NIFTYBEES {start.date()} to {idx[-1].date()} ({(idx[-1] - start).days / 365.25:.1f} years), "
          f"next-close execution, 0.10% per switch, cash at {CASH_RATE:.1%}/yr. Generated by `python -m hindcast.loss_control`.",
          ""]

    # 1. Index
    rows, rets, sigs = {}, {}, {}
    for name, fn in RULES.items():
        s = fn(bench)
        r = run(r_idx, s).loc[sl]
        rets[name], sigs[name] = r, s.shift(2).loc[sl]
        rows[name] = metrics(r, sigs[name])
        for wname, (a, b) in WINDOWS.items():
            rows[name][wname] = window_fall(r, a, b)
    base = rets["A. Buy and hold"]
    for name in list(RULES)[1:]:
        rows[name].update(block_bootstrap(rets[name], base))
    cols = ["CAGR", "Max fall", "Worst 12m", "Vol", "Return/fall", "Invested", "Switches/yr", *WINDOWS]
    md += ["## 1. Nifty 50 (NIFTYBEES)", "", table(rows, cols), "",
           "Bootstrap (2,000 paired 3-month-block resamples of the same period):", "",
           table({k: v for k, v in rows.items() if k != "A. Buy and hold"}, ["P(smaller fall)", "P(higher return)"]), ""]

    zero = {name: metrics(run(r_idx, fn(bench), 0.0).loc[sl]) for name, fn in RULES.items()}
    md += ["Sensitivity, cash earning 0%:", "", table(zero, ["CAGR", "Max fall"]), ""]

    # 2. Parameter neighbourhood
    nb = {}
    for m in range(6, 13):
        nb[f"{m}-month SMA"] = metrics(run(r_idx, sig_sma_months(bench, m)).loc[sl])
    for d in (100, 150, 200, 250):
        nb[f"{d}-day SMA, 2% band"] = metrics(run(r_idx, sig_sma_band(bench, d)).loc[sl])
    for t in (0.10, 0.12, 0.15, 0.18):
        nb[f"Vol target {t:.0%}"] = metrics(run(r_idx, sig_vol_target(bench, t)).loc[sl])
    bh = rows["A. Buy and hold"]
    better_fall = sum(v["Max fall"] > bh["Max fall"] for v in nb.values())
    better_cagr = sum(v["CAGR"] > bh["CAGR"] for v in nb.values())
    md += ["## 2. Nearby settings (does the result depend on the exact number?)", "",
           table(nb, ["CAGR", "Max fall", "Return/fall"]), "",
           f"{better_fall}/{len(nb)} settings had a smaller max fall than buy-and-hold; "
           f"{better_cagr}/{len(nb)} had a higher CAGR.", ""]

    # 3. Your stocks
    closes, names = stock_basket(prices, tickers, idx)
    r_bh, inv_bh = basket_returns(closes, None)
    per_stock = pd.DataFrame({s: sig_sma_months(closes[s].dropna()).reindex(idx) for s in names})
    r_ps, inv_ps = basket_returns(closes, per_stock)
    r_ix, inv_ix = basket_returns(closes, pd.DataFrame({s: sig_sma_months(bench) for s in names}))
    vt = sig_vol_target((1 + r_bh).cumprod())
    r_vt = vt.shift(2).fillna(1.0) * r_bh + (1 - vt.shift(2).fillna(1.0)) * ((1 + CASH_RATE) ** (1 / DAYS) - 1) \
        - vt.shift(2).diff().abs().fillna(0.0) * COST
    srows = {"A. Hold all stocks (equal weight)": metrics(r_bh.loc[sl], inv_bh.loc[sl]),
             "B1. Per-stock 10-month SMA": metrics(r_ps.loc[sl], inv_ps.loc[sl]),
             "B2. Nifty 10-month SMA on whole basket": metrics(r_ix.loc[sl], inv_ix.loc[sl]),
             "D. Vol target 15% on basket": metrics(r_vt.loc[sl], vt.shift(2).loc[sl])}
    for name, r in zip(srows, (r_bh, r_ps, r_ix, r_vt)):
        for wname, (a, b) in WINDOWS.items():
            srows[name][wname] = window_fall(r.loc[sl], a, b)
    for name, r in zip(list(srows)[1:], (r_ps, r_ix, r_vt)):
        srows[name].update(block_bootstrap(r.loc[sl], r_bh.loc[sl]))
    md += [f"## 3. Your {len(names)} current stocks (equal weight, each from its listing date)", "",
           "Survivorship warning: these are stocks you hold today, picked with hindsight, so absolute returns "
           "are biased upward. Compare the rules with each other, not with the index.", "",
           table(srows, ["CAGR", "Max fall", "Worst 12m", "Return/fall", "Invested", *WINDOWS]), "",
           table({k: v for k, v in srows.items() if not k.startswith("A.")}, ["P(smaller fall)", "P(higher return)"]), ""]

    OUT.write_text("\n".join(md) + "\n")
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
