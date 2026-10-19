"""Outcome scoring and overlap-aware statistics for the hindcast."""
from __future__ import annotations

import math
from itertools import combinations
from typing import Optional

import numpy as np
import pandas as pd
from scipy.stats import norm

HORIZON = 252
NW_LAG = 11
BLOCK = 12
N_BOOT = 10_000
SEED = 42

# Expected direction of each decision vs the benchmark.
DIRECTION = {"SELL": -1, "TRIM": -1, "REVIEW": -1, "ACCUMULATE": 1, "BUY": 1}
SIGNED_SCORE = {"SELL": -2, "TRIM": -1, "REVIEW": -1, "HOLD": 0, "ACCUMULATE": 1, "BUY": 1}
CLASS_OF = {"SELL": "SELL", "TRIM": "TRIM", "REVIEW": "REVIEW", "ACCUMULATE": "ACCUMULATE", "BUY": "ACCUMULATE", "HOLD": "HOLD"}


def forward_returns(dec: pd.DataFrame, closes: pd.DataFrame, bench: pd.Series, horizon: int = HORIZON) -> pd.DataFrame:
    """R from close(t+1) to close(t+1+horizon); windows past the data are UNRESOLVED, never truncated."""
    out = dec.copy()
    cal = bench.index
    pos = {d: i for i, d in enumerate(cal)}
    r_s, r_b, status = [], [], []
    for d, sym in zip(out["date"], out["symbol"]):
        i = pos.get(d)
        if i is None or i + 1 + horizon >= len(cal) or sym not in closes.columns:
            r_s.append(np.nan), r_b.append(np.nan), status.append("UNRESOLVED")
            continue
        a, b = cal[i + 1], cal[i + 1 + horizon]
        p0, p1 = closes.at[a, sym], closes.at[b, sym]
        if pd.isna(p0) or pd.isna(p1) or p0 <= 0:
            r_s.append(np.nan), r_b.append(np.nan), status.append("UNRESOLVED")
            continue
        r_s.append(p1 / p0 - 1.0)
        r_b.append(float(bench.iloc[i + 1 + horizon] / bench.iloc[i + 1] - 1.0))
        status.append("RESOLVED")
    out["R_stock"], out["R_bench"], out["outcome"] = r_s, r_b, status
    out["XR"] = (1 + out["R_stock"]) / (1 + out["R_bench"]) - 1
    out["XR_diff"] = out["R_stock"] - out["R_bench"]
    return out


def score(dec: pd.DataFrame, bands=(0.0, 0.02, 0.05)) -> pd.DataFrame:
    """correct_bX in {1, 0, NaN}: NaN = neutral (inside the band), not a directional class, or unresolved."""
    out = dec.copy()
    direction = out["decision"].map(DIRECTION)
    for b in bands:
        col = f"correct_b{int(round(b * 100))}"
        signed = out["XR"] * direction
        val = np.where(signed > b, 1.0, np.where(signed < -b, 0.0, np.nan))
        val = np.where(direction.isna() | out["XR"].isna(), np.nan, val)
        out[col] = val
    return out


def episodes(dec: pd.DataFrame, dates: list) -> pd.DataFrame:
    """Runs of the same decision for a symbol on consecutive decision dates share an episode_id."""
    out = dec.sort_values(["symbol", "date"]).copy()
    order = {d: i for i, d in enumerate(sorted(dates))}
    ids, start = [], []
    last = {}
    counter = 0
    for sym, d, decision in zip(out["symbol"], out["date"], out["decision"]):
        prev = last.get(sym)
        if prev and prev[1] == decision and order.get(d, -9) == order.get(prev[0], -99) + 1:
            ids.append(prev[2]), start.append(False)
            last[sym] = (d, decision, prev[2])
        else:
            counter += 1
            ids.append(counter), start.append(True)
            last[sym] = (d, decision, counter)
    out["episode_id"], out["episode_start"] = ids, start
    return out.sort_values(["date", "symbol"]).reset_index(drop=True)


def newey_west_t(x, lag: int = NW_LAG) -> float:
    x = np.asarray(pd.Series(x).dropna(), dtype=float)
    n = len(x)
    if n < 3:
        return float("nan")
    e = x - x.mean()
    s = e @ e / n
    for k in range(1, min(lag, n - 1) + 1):
        s += 2 * (1 - k / (lag + 1)) * (e[k:] @ e[:-k]) / n
    se = math.sqrt(s / n) if s > 0 else float("nan")
    return float(x.mean() / se) if se and se == se else float("nan")


def block_bootstrap_ci(x, block: int = BLOCK, n_boot: int = N_BOOT, seed: int = SEED, alpha: float = 0.05):
    x = np.asarray(pd.Series(x).dropna(), dtype=float)
    n = len(x)
    if n < 2:
        return (float("nan"), float("nan"))
    block = max(1, min(block, n))
    rng = np.random.default_rng(seed)
    n_blocks = math.ceil(n / block)
    starts = rng.integers(0, n - block + 1, size=(n_boot, n_blocks))
    idx = (starts[:, :, None] + np.arange(block)[None, None, :]).reshape(n_boot, -1)[:, :n]
    means = x[idx].mean(axis=1)
    return (float(np.quantile(means, alpha / 2)), float(np.quantile(means, 1 - alpha / 2)))


def wilson(k: float, n: float, z: float = 1.96):
    if n <= 0:
        return (float("nan"), float("nan"))
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (max(0.0, c - h), min(1.0, c + h))


def per_date_signed(dec: pd.DataFrame, cls: str) -> pd.Series:
    """Per decision date: mean XR of the class, signed so that 'right' is positive."""
    rows = dec[(dec["decision"].map(CLASS_OF) == cls) & dec["XR"].notna()]
    if rows.empty:
        return pd.Series(dtype=float)
    sign = -1.0 if cls in ("SELL", "TRIM", "REVIEW") else 1.0
    return rows.groupby("date")["XR"].mean().sort_index() * sign


def information_coefficient(dec: pd.DataFrame) -> pd.Series:
    rows = dec[dec["decision"].isin(SIGNED_SCORE) & dec["XR"].notna()].copy()
    rows["score"] = rows["decision"].map(SIGNED_SCORE)
    out = {}
    for d, g in rows.groupby("date"):
        if g["score"].nunique() > 1 and len(g) >= 5:
            out[d] = g["score"].rank().corr(g["XR"].rank())
    return pd.Series(out, dtype=float).sort_index()


def class_table(dec: pd.DataFrame, band_col: str = "correct_b5") -> pd.DataFrame:
    rows = []
    for cls in ("SELL", "TRIM", "REVIEW", "ACCUMULATE", "HOLD"):
        sub = dec[dec["decision"].map(CLASS_OF) == cls]
        res = sub[sub["XR"].notna()]
        ep = res[res["episode_start"]] if "episode_start" in res else res
        series = per_date_signed(dec, cls) if cls != "HOLD" else pd.Series(dtype=float)
        n_dates = int(series.size)
        row = {"class": cls, "decisions": len(sub), "resolved": len(res), "episodes": len(ep),
               "avg_XR": float(res["XR"].mean()) if len(res) else float("nan"),
               "median_XR": float(res["XR"].median()) if len(res) else float("nan")}
        if cls == "HOLD":
            row["share_abs_XR_le_10pct"] = float((res["XR"].abs() <= 0.10).mean()) if len(res) else float("nan")
            row["verdict"] = "BASELINE"
            rows.append(row)
            continue
        k = float(np.nansum(ep[band_col])) if len(ep) else 0.0
        n = float(ep[band_col].notna().sum()) if len(ep) else 0.0
        neff = n_dates / 12.0
        row.update({
            "hit_rate": k / n if n else float("nan"),
            "hit_ci_naive": wilson(k, n),
            "n_eff_years": neff,
            "hit_ci_eff": wilson(k * neff / n, neff) if n and neff >= 1 else (float("nan"), float("nan")),
            "neutral_share": float(ep[band_col].isna().mean()) if len(ep) else float("nan"),
            "signed_mean": float(series.mean()) if n_dates else float("nan"),
            "nw_t": newey_west_t(series),
            "boot_ci": block_bootstrap_ci(series),
        })
        row["verdict"] = verdict(row, dec, cls)
        rows.append(row)
    return pd.DataFrame(rows)


def verdict(row: dict, dec: pd.DataFrame, cls: str) -> str:
    mean, t, (lo, hi) = row["signed_mean"], row["nw_t"], row["boot_ci"]
    if not (mean == mean):
        return "INSUFFICIENT EVIDENCE"
    regimes_ok = True
    if "bench_above_200dma" in dec.columns:
        for flag in (True, False):
            s = per_date_signed(dec[dec["bench_above_200dma"] == flag], cls)
            if len(s) and np.sign(s.mean()) != np.sign(mean):
                regimes_ok = False
    if mean > 0 and (t > 3.0 or lo > 0) and row["episodes"] >= 10 and regimes_ok:
        return "SKILL"
    if mean < 0 and hi < 0:
        return "OUT OF LINE"
    return "INSUFFICIENT EVIDENCE"


def nav_metrics(nav: pd.Series) -> dict:
    nav = nav.dropna()
    if len(nav) < 2:
        return {}
    rets = nav.pct_change().dropna()
    years = (nav.index[-1] - nav.index[0]).days / 365.25
    dd = nav / nav.cummax() - 1
    trough = dd.idxmin()
    peak = nav.loc[:trough].idxmax()
    recovered = nav.loc[trough:][nav.loc[trough:] >= nav.loc[peak]]
    end = recovered.index[0] if len(recovered) else nav.index[-1]
    return {
        "CAGR": (nav.iloc[-1] / nav.iloc[0]) ** (1 / years) - 1 if years > 0 else float("nan"),
        "vol": float(rets.std() * math.sqrt(252)),
        "max_dd": float(dd.min()),
        "dd_days": int((end - peak).days),
    }


def active_returns(nav: pd.DataFrame, a: str = "A", b: str = "B") -> pd.Series:
    r = nav[[a, b]].pct_change().dropna()
    return r[a] - r[b]


def deflated_sharpe(returns: pd.Series, n_trials: int, sr_variance: float) -> float:
    """Bailey & Lopez de Prado (2014) DSR on per-period returns."""
    r = pd.Series(returns).dropna()
    T = len(r)
    if T < 10 or r.std() == 0:
        return float("nan")
    sr = r.mean() / r.std()
    g = 0.5772156649
    n = max(2, n_trials)
    sr0 = math.sqrt(max(sr_variance, 0.0)) * ((1 - g) * norm.ppf(1 - 1 / n) + g * norm.ppf(1 - 1 / (n * math.e)))
    skew, kurt = float(r.skew()), float(r.kurt()) + 3.0
    den = math.sqrt(max(1e-12, 1 - skew * sr + (kurt - 1) / 4 * sr * sr))
    return float(norm.cdf((sr - sr0) * math.sqrt(T - 1) / den))


def pbo_cscv(matrix: pd.DataFrame, s: int = 6) -> float:
    """Probability of backtest overfitting via CSCV on a (time x config) return matrix."""
    m = matrix.dropna()
    if m.shape[1] < 2 or len(m) < s * 5:
        return float("nan")
    blocks = np.array_split(np.arange(len(m)), s)
    lam = []
    for is_idx in combinations(range(s), s // 2):
        is_rows = np.concatenate([blocks[i] for i in is_idx])
        oos_rows = np.concatenate([blocks[i] for i in range(s) if i not in is_idx])
        sr_is = m.iloc[is_rows].mean() / m.iloc[is_rows].std().replace(0, np.nan)
        sr_oos = m.iloc[oos_rows].mean() / m.iloc[oos_rows].std().replace(0, np.nan)
        best = sr_is.idxmax()
        rank = sr_oos.rank().loc[best]
        w = rank / (len(sr_oos) + 1)
        lam.append(math.log(w / (1 - w)))
    return float(np.mean(np.array(lam) <= 0))


def purge_train(train_dates: list, test_start, calendar: pd.DatetimeIndex, horizon: int = HORIZON) -> list:
    """Drop train decision dates whose label window reaches into the test window."""
    pos = {d: i for i, d in enumerate(calendar)}
    keep = []
    for d in train_dates:
        i = pos[d]
        end = calendar[min(len(calendar) - 1, i + 1 + horizon)]
        if end < pd.Timestamp(test_start):
            keep.append(d)
    return keep
