"""Offline hindcast: verify the live engine's monthly decisions 1 year later, then tune.

Usage: python -m hindcast.run   (needs the cache from `python -m hindcast.fetch`)

Outputs (deterministic for a given commit + cache):
  reports/hindcast_decisions.csv, reports/hindcast_trials.csv,
  reports/hindcast_summary.md, reports/hindcast_param_proposal.diff (only if accepted)
"""
from __future__ import annotations

import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from analysis import SECTOR_MAP, TICKER_MAP  # noqa: E402
from config import RISK_CONFIG  # noqa: E402
from hindcast import stats  # noqa: E402
from hindcast.data import BENCHMARK_TICKER, PRICE_DIR, load_adjusted, load_corporate_actions, load_symbol  # noqa: E402
from hindcast.engine import FeatureCache, NeutralInputs, aligned_closes, decision_dates, replay, with_overrides  # noqa: E402

PRIMARY = ("2022-10-01", "2025-10-31")
TRAIN = ("2019-01-01", "2022-09-30")
TEST = ("2023-10-01", "2025-10-31")
DRAWDOWN_WINDOW = ("2024-10-01", "2025-03-31")
GRID_FILE = ROOT / "data" / "hindcast" / "grid.json"
REPORTS = ROOT / "reports"
ACCEPT = {"dsr": 0.95, "pbo": 0.30}


def load_grid(path: Path = GRID_FILE) -> tuple[list[dict], str]:
    if not path.exists():
        raise SystemExit(f"{path} is missing: the tuning grid must be committed before any tuning run.")
    raw = path.read_bytes()
    configs = json.loads(raw)["configs"]
    if not configs or configs[0]["id"] != "incumbent" or configs[0]["overrides"]:
        raise SystemExit("grid.json must start with the incumbent (no overrides).")
    return configs, hashlib.sha256(raw).hexdigest()


def git_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "unknown"


def load_universe(price_dir: Path = PRICE_DIR):
    symbols = sorted(pd.read_csv(ROOT / "portfolio.csv")["Stock Symbol"].astype(str).str.strip())
    events = load_corporate_actions()
    prices, tickers, data_log = {}, {}, []
    for sym in symbols:
        ticker = TICKER_MAP.get(sym, f"{sym}.NS")
        df, info = load_symbol(sym, ticker, events, price_dir)
        tickers[sym] = info.ticker
        if df is not None:
            prices[sym] = df
        data_log.append({"symbol": sym, "ticker": info.ticker, "rows": 0 if df is None else len(df),
                         "first": "" if df is None else str(df.index[0].date()),
                         "tags": ",".join(sorted(set(info.tags))) or "OK", "notes": " | ".join(info.log)})
    bench_df = load_adjusted(BENCHMARK_TICKER, price_dir)
    if bench_df is None:
        raise SystemExit(f"Benchmark {BENCHMARK_TICKER} missing from {price_dir}; run `python -m hindcast.fetch` first.")
    sectors = {s: SECTOR_MAP.get(s, "Other ETFs/Misc") for s in symbols}
    return symbols, prices, tickers, sectors, bench_df["Close"], pd.DataFrame(data_log)


def regime_labels(bench: pd.Series) -> pd.DataFrame:
    dma = bench.rolling(200).mean()
    dd = bench / bench.cummax() - 1
    return pd.DataFrame({"bench_above_200dma": bench > dma, "bench_drawdown_gt_10pct": dd < -0.10})


def evaluate(res, closes, bench, regimes, dates, label):
    dec = res.decisions.copy()
    dec = stats.forward_returns(dec, closes, bench)
    dec = stats.score(dec)
    dec = stats.episodes(dec, dates)
    dec = dec.join(regimes, on="date")
    dec.insert(0, "run", label)
    return dec


def regime_table(dec: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for cls in ("SELL", "TRIM", "REVIEW", "ACCUMULATE"):
        for name, mask in (("bench above 200DMA", dec["bench_above_200dma"] == True),  # noqa: E712
                           ("bench below 200DMA", dec["bench_above_200dma"] == False),  # noqa: E712
                           ("bench drawdown > 10%", dec["bench_drawdown_gt_10pct"] == True)):  # noqa: E712
            s = stats.per_date_signed(dec[mask], cls)
            rows.append({"class": cls, "regime": name, "dates": len(s),
                         "signed_mean_XR": float(s.mean()) if len(s) else float("nan")})
    return pd.DataFrame(rows)


def turnover(res, years: float) -> float:
    if res.trades.empty:
        return 0.0
    a = res.trades[(res.trades["book"] == "A") & (res.trades["action"] != "ADMIT")]
    avg_nav = res.nav["A"].mean()
    return float(a["value"].sum() / avg_nav / years) if years > 0 and avg_nav > 0 else float("nan")


def book_summary(res) -> pd.DataFrame:
    years = (res.nav.index[-1] - res.nav.index[0]).days / 365.25
    rows = []
    for col, name in (("A", "FOLLOW-MODEL"), ("B", "DO-NOTHING"), ("C", "NIFTYBEES")):
        m = stats.nav_metrics(res.nav[col])
        m["book"] = name
        if col == "A":
            m["turnover_per_year"] = turnover(res, years)
            m["trades"] = int(((res.trades["book"] == "A") & (res.trades["action"] != "ADMIT")).sum()) if not res.trades.empty else 0
        rows.append(m)
    act = stats.active_returns(res.nav)
    lo, hi = stats.block_bootstrap_ci(act, block=63, n_boot=2000)
    return pd.DataFrame(rows), {"active_ann": float(act.mean() * 252), "active_ci_ann": (lo * 252, hi * 252)}


def train_hit_rate(dec: pd.DataFrame) -> float:
    ep = dec[dec["episode_start"] & dec["correct_b5"].notna()]
    return float(ep["correct_b5"].mean()) if len(ep) else float("nan")


def proposal_diff(overrides: dict) -> str:
    text = (ROOT / "config.py").read_text()
    new = text
    for field, value in overrides.items():
        pat = re.compile(rf"(\s{field}: \w+ = _(?:float|int)\(\"[A-Z0-9_]+\", )([^)]+)(\))")
        if not pat.search(new):
            raise ValueError(f"cannot locate default for {field} in config.py")
        new = pat.sub(lambda m: f"{m.group(1)}{value}{m.group(3)}", new, count=1)
    return "".join(difflib.unified_diff(text.splitlines(True), new.splitlines(True), "a/config.py", "b/config.py"))


def _int(x) -> str:
    return "" if x is None or (isinstance(x, float) and x != x) else str(int(x))


def fmt(x, pct=False, nd=2):
    if x is None or (isinstance(x, float) and x != x):
        return "n/a"
    if isinstance(x, tuple):
        return "[" + ", ".join(fmt(v, pct, nd) for v in x) + "]"
    return f"{x * 100:.{nd}f}%" if pct else f"{x:.{nd}f}"


def main(argv=None) -> int:
    configs, grid_sha = load_grid()
    symbols, prices, tickers, sectors, bench, data_log = load_universe(PRICE_DIR)
    calendar = bench.index
    closes = aligned_closes(prices, calendar)
    regimes = regime_labels(bench)
    feats = FeatureCache(prices)
    manifest = PRICE_DIR / "manifest.json"
    data_sha = hashlib.sha256(manifest.read_bytes()).hexdigest()[:16] if manifest.exists() else "no-manifest"
    common = dict(prices=prices, sectors=sectors, bench=bench, features=feats, tickers=tickers, universe=symbols)

    # ---- 1) Verify the incumbent over the primary window ----
    p_dates = decision_dates(calendar, *PRIMARY)
    primary = replay(dates=p_dates, config=RISK_CONFIG, **common)
    p_dec = evaluate(primary, closes, bench, regimes, p_dates, "primary:incumbent")
    p_table = stats.class_table(p_dec)
    p_ic = stats.information_coefficient(p_dec)
    p_books, p_active = book_summary(primary)

    # Sensitivities on neutralised inputs (decision changes vs primary, and A-B).
    sens_rows = []
    base = p_dec.set_index(["date", "symbol"])["decision"]
    for label, neutral in (("conviction=3", NeutralInputs(conviction=3.0)),
                           ("invalidation=cost x0.85", NeutralInputs(invalidation_mode="cost_x0.85")),
                           ("invalidation=52w low", NeutralInputs(invalidation_mode="low_52w"))):
        r = replay(dates=p_dates, config=RISK_CONFIG, neutral=neutral, **common)
        alt = r.decisions.set_index(["date", "symbol"])["decision"]
        changed = int((alt.reindex(base.index) != base).sum())
        sens_rows.append({"variant": label, "decisions_changed": changed,
                          "active_ann": float(stats.active_returns(r.nav).mean() * 252)})
    sens = pd.DataFrame(sens_rows)

    # ---- 2) Tuning: TRAIN picks, TEST confirms once ----
    train_dates = stats.purge_train(decision_dates(calendar, *TRAIN), TEST[0], calendar)
    test_dates = decision_dates(calendar, *TEST)
    trials, train_active = [], {}
    for cfg in configs:
        c = with_overrides(RISK_CONFIG, cfg["overrides"])
        r = replay(dates=train_dates, config=c, until=pd.Timestamp(TRAIN[1]), **common)
        d = evaluate(r, closes, bench, regimes, train_dates, f"train:{cfg['id']}")
        act = stats.active_returns(r.nav)
        train_active[cfg["id"]] = act
        trials.append({"config_id": cfg["id"], "overrides": json.dumps(cfg["overrides"], sort_keys=True),
                       "train_active_ann": float(act.mean() * 252), "train_sharpe_per_day": float(act.mean() / act.std()) if act.std() else float("nan"),
                       "train_hit_b5": train_hit_rate(d), "grid_sha256": grid_sha})
    trials_df = pd.DataFrame(trials)
    ranked = trials_df.sort_values(["train_active_ann", "train_hit_b5"], ascending=False, kind="mergesort")
    chosen_id = ranked.iloc[0]["config_id"]
    chosen = next(c for c in configs if c["id"] == chosen_id)

    test_runs = {}
    for cid in dict.fromkeys(["incumbent", chosen_id]):
        cfg = next(c for c in configs if c["id"] == cid)
        r = replay(dates=test_dates, config=with_overrides(RISK_CONFIG, cfg["overrides"]), **common)
        test_runs[cid] = (r, evaluate(r, closes, bench, regimes, test_dates, f"test:{cid}"))

    inc_r, inc_dec = test_runs["incumbent"]
    ch_r, ch_dec = test_runs[chosen_id]
    inc_act, ch_act = stats.active_returns(inc_r.nav), stats.active_returns(ch_r.nav)
    sr_var = float(np.nanvar(trials_df["train_sharpe_per_day"]))
    dsr = stats.deflated_sharpe(ch_act, len(configs), sr_var)
    pbo = stats.pbo_cscv(pd.DataFrame(train_active))
    test_books, _ = book_summary(ch_r)
    cagr = dict(zip(test_books["book"], test_books["CAGR"]))
    above = regimes["bench_above_200dma"].reindex(ch_act.index).fillna(False)
    diff = ch_act - inc_act.reindex(ch_act.index).fillna(0.0)
    regime_ok = bool(diff[above].mean() > 0 and diff[~above].mean() > 0)
    checks = {
        "chosen differs from incumbent": chosen_id != "incumbent",
        "TEST: tuned beats incumbent (A-B)": float(ch_act.mean()) > float(inc_act.mean()),
        "TEST: follow-model >= do-nothing": cagr.get("FOLLOW-MODEL", -1) >= cagr.get("DO-NOTHING", 0),
        "TEST: follow-model >= NIFTYBEES": cagr.get("FOLLOW-MODEL", -1) >= cagr.get("NIFTYBEES", 0),
        f"DSR > {ACCEPT['dsr']}": dsr == dsr and dsr > ACCEPT["dsr"],
        f"PBO < {ACCEPT['pbo']}": pbo == pbo and pbo < ACCEPT["pbo"],
        "improvement holds above and below the benchmark 200-DMA": regime_ok,
    }
    accepted = all(checks.values())
    diff_path = REPORTS / "hindcast_param_proposal.diff"
    if accepted:
        diff_path.write_text(proposal_diff(chosen["overrides"]))
    elif diff_path.exists():
        diff_path.unlink()

    # Robustness of each tuned parameter: share of its grid neighbours with the same sign of TRAIN benefit.
    robust_rows = []
    inc_train = trials_df.set_index("config_id").loc["incumbent", "train_active_ann"]
    params = {}
    for cfg in configs[1:]:
        for k in cfg["overrides"]:
            params.setdefault(k, []).append(cfg["id"])
    for k, ids in params.items():
        signs = [np.sign(trials_df.set_index("config_id").loc[i, "train_active_ann"]) for i in ids]
        base_sign = np.sign(inc_train)
        share = float(np.mean([s == base_sign for s in signs])) if signs else float("nan")
        robust_rows.append({"parameter": k, "neighbours": ", ".join(ids), "same_sign_share": share,
                            "robust": share >= 0.7})
    robust = pd.DataFrame(robust_rows)

    # ---- 3) Outputs ----
    REPORTS.mkdir(exist_ok=True)
    all_dec = pd.concat([p_dec, inc_dec, ch_dec] if chosen_id != "incumbent" else [p_dec, inc_dec], ignore_index=True)
    all_dec["date"] = all_dec["date"].dt.strftime("%Y-%m-%d")
    all_dec.round(6).to_csv(REPORTS / "hindcast_decisions.csv", index=False)
    trials_df.round(6).to_csv(REPORTS / "hindcast_trials.csv", index=False)

    dw = p_dec[(p_dec["date"] >= DRAWDOWN_WINDOW[0]) & (p_dec["date"] <= DRAWDOWN_WINDOW[1])
               & p_dec["decision"].isin(["SELL", "TRIM", "REVIEW"])]
    lines = [
        "# Hindcast summary", "",
        f"Engine commit `{git_commit()}` · price manifest sha256 `{data_sha}` · grid sha256 `{grid_sha[:16]}` · "
        f"benchmark {BENCHMARK_TICKER} (adjusted close) · bootstrap seed {stats.SEED}", "",
        "## 1. Verdict per decision type (primary window, incumbent parameters)", "",
        f"Decision dates {PRIMARY[0]} to {PRIMARY[1]} ({len(p_dates)} month-ends). Outcome = 252-session excess return vs "
        "NIFTYBEES from the next close. Hit rate at a ±5% neutral band, one count per episode.", "",
        "| Class | Decisions | Episodes | Hit rate | 95% CI (naive) | 95% CI (effective N) | Avg XR | NW t | Bootstrap CI | Verdict |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for _, r in p_table.iterrows():
        if r["class"] == "HOLD":
            lines.append(f"| HOLD | {r['decisions']} | {r['episodes']} | – | – | – | {fmt(r['avg_XR'], True)} | – | – | baseline (|XR|≤10%: {fmt(r['share_abs_XR_le_10pct'], True)}) |")
        else:
            lines.append(f"| {r['class']} | {r['decisions']} | {r['episodes']} | {fmt(r['hit_rate'], True)} | {fmt(r['hit_ci_naive'], True)} | "
                         f"{fmt(r['hit_ci_eff'], True)} | {fmt(r['avg_XR'], True)} | {fmt(r['nw_t'])} | {fmt(r['boot_ci'], True)} | **{r['verdict']}** |")
    lines += ["", f"Information coefficient (signed decision score vs XR, per date): mean {fmt(float(p_ic.mean()) if len(p_ic) else float('nan'))}, "
              f"NW t {fmt(stats.newey_west_t(p_ic))}, dates {len(p_ic)}.", "",
              "## 2. Acting on the recommendations", "",
              "| Window | Book | CAGR | Vol | Max DD | DD days | Turnover/yr | Trades |", "|---|---|---|---|---|---|---|---|"]
    for wname, books in (("primary (incumbent)", p_books), (f"TEST ({'tuned: ' + chosen_id if chosen_id != 'incumbent' else 'incumbent'})", test_books)):
        for _, b in books.iterrows():
            lines.append(f"| {wname} | {b['book']} | {fmt(b['CAGR'], True)} | {fmt(b['vol'], True)} | {fmt(b['max_dd'], True)} | "
                         f"{b['dd_days']} | {fmt(b.get('turnover_per_year'))} | {_int(b.get('trades'))} |")
    inc_books, _ = book_summary(inc_r)
    for _, b in inc_books.iterrows():
        if b["book"] == "FOLLOW-MODEL" and chosen_id != "incumbent":
            lines.append(f"| TEST (incumbent) | FOLLOW-MODEL | {fmt(b['CAGR'], True)} | {fmt(b['vol'], True)} | {fmt(b['max_dd'], True)} | "
                         f"{b['dd_days']} | {fmt(b.get('turnover_per_year'))} | {_int(b.get('trades'))} |")
    lines += ["", f"Primary FOLLOW-MODEL minus DO-NOTHING: {fmt(p_active['active_ann'], True)} a year, "
              f"bootstrap 95% CI {fmt(p_active['active_ci_ann'], True)}.", "",
              "## 3. Tuning result", "",
              f"TRAIN {TRAIN[0]}–{TRAIN[1]} ({len(train_dates)} decision dates after purging labels that overlap TEST); "
              f"TEST {TEST[0]}–{TEST[1]} ({len(test_dates)} dates), looked at once. Grid: {len(configs)} configs from `data/hindcast/grid.json`.", "",
              f"Best on TRAIN: **{chosen_id}** {json.dumps(chosen['overrides'])}. DSR {fmt(dsr)}, PBO {fmt(pbo)}.", "",
              "| Acceptance check | Pass |", "|---|---|"]
    lines += [f"| {k} | {'yes' if v else 'no'} |" for k, v in checks.items()]
    if accepted:
        lines += ["", "**Recommendation: adopt the tuned parameters** — see `reports/hindcast_param_proposal.diff` (not applied)."]
    else:
        out_of_line = [r["class"] for _, r in p_table.iterrows() if r["verdict"] == "OUT OF LINE"]
        lines += ["", "**Recommendation: keep current parameters.**",
                  f"Rule types to make advisory-only (verdict OUT OF LINE): {', '.join(out_of_line) or 'none'}.",
                  f"Next-best TRAIN config: {ranked.iloc[1]['config_id'] if len(ranked) > 1 else 'n/a'}."]
    lines += ["", "Parameter robustness (share of grid neighbours with the same sign of TRAIN benefit; ≥70% = robust):", "",
              robust.to_markdown(index=False) if len(robust) else "(no tuned parameters)", "",
              "## 4. Coverage and data log", "",
              data_log[["symbol", "ticker", "rows", "first", "tags", "notes"]].to_markdown(index=False), "",
              "Decision coverage (primary): " + ", ".join(f"{k}={v}" for k, v in p_dec["data_tag"].value_counts().sort_index().items()), "",
              "## 5. Sensitivities and regimes", "",
              sens.to_markdown(index=False), "", regime_table(p_dec).to_markdown(index=False), "",
              f"SELL/TRIM/REVIEW issued {DRAWDOWN_WINDOW[0]} to {DRAWDOWN_WINDOW[1]}: {len(dw)} decisions, "
              f"resolved avg XR {fmt(float(dw['XR'].mean()) if dw['XR'].notna().any() else float('nan'), True)}.", "",
              "## 6. Caveats", "",
              "- No tax or transaction costs: every return is an upper bound.",
              "- Universe = today's 34 holdings, as if held throughout (survivorship-biased: SELL looks worse, ACCUMULATE better). "
              "FOLLOW-MODEL vs DO-NOTHING uses the same names, so the bias largely cancels there.",
              "- thesis.csv is never read (written in 2026): thesis INTACT, conviction 4, ROE 0.15, no invalidation price in the primary run.",
              "- Overlapping 1-year windows: the primary window holds about 3 non-overlapping years, TEST about 2; one market path.",
              "- Decisions are monthly; daily confirmation rules (3 closes) are only approximated at month-ends.", ""]
    (REPORTS / "hindcast_summary.md").write_text("\n".join(lines))
    print("\n".join(lines[:40]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
