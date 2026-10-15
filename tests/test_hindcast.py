"""Offline tests for the hindcast (synthetic prices only; no network)."""
import builtins
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from config import RISK_CONFIG
from hindcast import data as hdata
from hindcast import stats
from hindcast.engine import FeatureCache, decision_dates, replay

CAL = pd.bdate_range("2017-06-01", "2026-10-09")


def _walk(seed, start=100.0, n=len(CAL), drift=0.0003, vol=0.015):
    rng = np.random.default_rng(seed)
    return start * np.exp(np.cumsum(rng.normal(drift, vol, n)))


def _frame(close, index):
    close = pd.Series(close, index=index)
    return pd.DataFrame({"Open": close, "High": close * 1.01, "Low": close * 0.99, "Close": close})


def _universe(n=6, late=None):
    prices = {f"S{i}": _frame(_walk(i), CAL) for i in range(n)}
    if late:
        prices["LATE"] = _frame(_walk(99, n=len(CAL[CAL >= late])), CAL[CAL >= late])
    sectors = {s: ("Banking" if i % 2 else "IT") for i, s in enumerate(sorted(prices))}
    bench = pd.Series(_walk(7, drift=0.0004, vol=0.01), index=CAL)
    return prices, sectors, bench


def test_corporate_action_table_fixes_unadjusted_bonus():
    idx = pd.bdate_range("2024-01-01", periods=60)
    close = np.full(60, 100.0)
    close[30:] = 50.0  # unadjusted 1:1 bonus on day 30
    df = _frame(close, idx)
    info = hdata.SeriesInfo("X.NS")
    ev = [{"symbol": "X.NS", "ex_date": str(idx[31].date()), "type": "bonus", "ratio": "0.5", "status": "sourced"}]
    out = hdata.apply_corporate_actions(df, "X.NS", ev, info)
    assert np.allclose(out["Close"], 50.0)
    assert "ADJ_FIXED" in info.tags
    # An already-adjusted series is left alone.
    info2 = hdata.SeriesInfo("X.NS")
    out2 = hdata.apply_corporate_actions(out, "X.NS", ev, info2)
    assert out2.equals(out) and "ADJ_FIXED" not in info2.tags


def test_unexplained_jump_is_logged_not_repaired():
    idx = pd.bdate_range("2024-01-01", periods=40)
    close = np.full(40, 100.0)
    close[20:] = 40.0
    info = hdata.SeriesInfo("Y.NS")
    out = hdata.apply_corporate_actions(_frame(close, idx), "Y.NS", [], info)
    assert out["Close"].iloc[0] == 100.0 and "CA_SUSPECT" in info.tags


def test_stitch_renamed_ticker():
    old = _frame(np.linspace(100, 110, 20), pd.bdate_range("2025-01-01", periods=20))
    new = _frame(np.linspace(110, 120, 10), pd.bdate_range(old.index[-1] + pd.offsets.BDay(1), periods=10))
    s = hdata.stitch(new, old, "2025-02-01")
    assert len(s) == 30 and s.index.is_monotonic_increasing


def test_decision_dates_are_month_ends():
    d = decision_dates(CAL, "2023-01-01", "2023-03-31")
    assert [x.strftime("%Y-%m-%d") for x in d] == ["2023-01-31", "2023-02-28", "2023-03-31"]


def test_no_lookahead_poisoned_future_changes_no_past_decision():
    prices, sectors, bench = _universe()
    dates = decision_dates(bench.index, "2021-01-01", "2022-12-31")
    cut = dates[11]
    base = replay(prices, sectors, bench, dates[:12], RISK_CONFIG, universe=list(prices))
    poisoned = {s: df.copy() for s, df in prices.items()}
    for df in poisoned.values():
        df.loc[df.index > cut, ["Open", "High", "Low", "Close"]] *= 10
    bad_bench = bench.copy()
    bad_bench[bad_bench.index > cut] *= 10
    again = replay(poisoned, sectors, bad_bench, dates[:12], RISK_CONFIG, universe=list(prices))
    cols = ["date", "symbol", "decision", "weight_pct"]
    pd.testing.assert_frame_equal(base.decisions[cols], again.decisions[cols])


def test_fills_happen_at_next_close():
    prices, sectors, bench = _universe()
    dates = decision_dates(bench.index, "2020-01-01", "2023-12-31")
    res = replay(prices, sectors, bench, dates, RISK_CONFIG, universe=list(prices))
    trades = res.trades[res.trades["action"] != "ADMIT"]
    assert not trades.empty
    cal = list(bench.index)
    dset = set(dates)
    for _, t in trades.iterrows():
        prev = cal[cal.index(t["date"]) - 1]
        assert prev in dset  # executed the session after a decision date
        assert t["price"] == pytest.approx(float(prices[t["symbol"]].loc[t["date"], "Close"]))


def test_existence_gate_and_entry():
    prices, sectors, bench = _universe(late="2021-06-01")
    sectors["LATE"] = "IT"
    dates = decision_dates(bench.index, "2021-01-01", "2023-06-30")
    res = replay(prices, sectors, bench, dates, RISK_CONFIG, universe=list(prices))
    late = res.decisions[res.decisions["symbol"] == "LATE"].set_index("date")
    assert late.loc[dates[0], "data_tag"] == "NOT_LISTED"
    assert "SHORT_HISTORY" in set(late["data_tag"])
    assert (late["data_tag"] == "ENTRY").sum() == 1
    first_ok = late[late["data_tag"] == "OK"].index.min()
    assert FeatureCache(prices).sessions("LATE", first_ok) >= 252


def test_scoring_bands_neutral_and_unresolved():
    cal = pd.bdate_range("2020-01-01", periods=600)
    bench = pd.Series(np.full(600, 100.0), index=cal)
    closes = pd.DataFrame({"UP": np.linspace(100, 200, 600), "FLAT": np.full(600, 100.0)}, index=cal)
    dec = pd.DataFrame({"date": [cal[10], cal[10], cal[10], cal[500]],
                        "symbol": ["UP", "UP", "FLAT", "UP"],
                        "decision": ["SELL", "ACCUMULATE", "SELL", "SELL"]})
    out = stats.score(stats.forward_returns(dec, closes, bench))
    assert out.loc[0, "correct_b5"] == 0.0      # sold a riser
    assert out.loc[1, "correct_b5"] == 1.0      # bought a riser
    assert np.isnan(out.loc[2, "correct_b5"])   # flat = neutral
    assert out.loc[3, "outcome"] == "UNRESOLVED"


def test_episode_collapse():
    dates = list(pd.bdate_range("2024-01-31", periods=5, freq="BME"))
    dec = pd.DataFrame({"date": dates * 1, "symbol": ["A"] * 5,
                        "decision": ["HOLD", "HOLD", "SELL", "SELL", "HOLD"]})
    out = stats.episodes(dec, dates)
    assert out["episode_id"].nunique() == 3
    assert out["episode_start"].tolist() == [True, False, True, False, True]


def test_purge_drops_overlapping_train_labels():
    cal = pd.bdate_range("2019-01-01", "2024-12-31")
    train = decision_dates(cal, "2019-01-01", "2022-09-30")
    kept = stats.purge_train(train, "2023-10-01", cal)
    pos = {d: i for i, d in enumerate(cal)}
    assert all(cal[pos[d] + 1 + 252] < pd.Timestamp("2023-10-01") for d in kept)
    assert len(kept) < len(train) or cal[pos[train[-1]] + 253] < pd.Timestamp("2023-10-01")


def test_grid_is_committed_and_frozen(tmp_path):
    from hindcast import run
    configs, sha = run.load_grid()
    assert configs[0]["id"] == "incumbent" and len(configs) <= 30 and len(sha) == 64
    for c in configs:
        for k in c["overrides"]:
            assert hasattr(RISK_CONFIG, k)
    with pytest.raises(SystemExit):
        run.load_grid(tmp_path / "missing.json")


def test_replay_never_opens_thesis_csv(monkeypatch):
    prices, sectors, bench = _universe()
    real_open = builtins.open

    def guarded(file, *a, **k):
        assert "thesis.csv" not in str(file), "hindcast must not read thesis.csv"
        return real_open(file, *a, **k)

    monkeypatch.setattr(builtins, "open", guarded)
    monkeypatch.setattr(pd, "read_csv", lambda *a, **k: (_ for _ in ()).throw(AssertionError("no CSV reads in replay")))
    dates = decision_dates(bench.index, "2021-01-01", "2021-12-31")
    replay(prices, sectors, bench, dates, RISK_CONFIG, universe=list(prices))


def test_stats_primitives():
    lo, hi = stats.wilson(7, 10)
    assert 0 < lo < 0.7 < hi < 1
    rng = np.random.default_rng(1)
    assert abs(stats.newey_west_t(rng.normal(0, 1, 500))) < 4
    assert stats.newey_west_t(rng.normal(1, 0.1, 100)) > 10
    lo, hi = stats.block_bootstrap_ci(rng.normal(0.5, 1, 200), n_boot=500)
    assert lo < 0.5 < hi
    m = pd.DataFrame(rng.normal(0, 0.01, (600, 5)))
    assert 0 <= stats.pbo_cscv(m) <= 1
    assert 0 <= stats.deflated_sharpe(pd.Series(rng.normal(0.001, 0.01, 500)), 10, 1e-4) <= 1
