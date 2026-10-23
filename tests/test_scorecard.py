import numpy as np
import pandas as pd

import scorecard
from analysis import compute_market_features


def _tracking(rows):
    return pd.DataFrame(rows, columns=["Analysis_Date", "Stock_Symbol", "Decision", "run_timestamp_ist"])


def test_switches_exit_then_reentry():
    t = _tracking([
        ("2026-10-19", "AAA", "SELL", "2026-10-19 09:20"),
        ("2026-10-20", "AAA", "SELL", "2026-10-20 09:20"),
        ("2026-11-02", "AAA", "HOLD", "2026-11-02 09:20"),
        ("2026-10-19", "BBB", "HOLD", "2026-10-19 09:20"),
        ("2026-10-01", "CCC", "SELL", "2026-10-01 09:20"),  # before start: ignored
    ])
    sw = scorecard.signal_switches(t, "2026-10-19")
    assert [(s.symbol, s.kind) for s in sw] == [("AAA", "EXIT"), ("AAA", "RE-ENTRY")]


def test_simulate_fills_next_close_and_keeps_cash():
    idx = pd.bdate_range("2026-10-19", periods=6)
    closes = pd.DataFrame({"AAA": [100, 90, 80, 70, 60, 50.0], "BBB": [10.0] * 6}, index=idx)
    qty = pd.Series({"AAA": 10.0, "BBB": 100.0})
    sw = [scorecard.Switch("AAA", idx[0], "EXIT")]
    res = scorecard.simulate(closes, qty, sw, "2026-10-19", cash_rate=0.0)
    assert sw[0].exec_date == idx[1] and sw[0].exec_price == 90.0  # signal day 0 -> fill at day-1 close
    assert res.daily["Hold"].iloc[-1] == 10 * 50 + 1000
    assert res.daily["Follow"].iloc[-1] == 10 * 90 + 1000


def test_reentry_buys_back_with_cash():
    idx = pd.bdate_range("2026-10-19", periods=5)
    closes = pd.DataFrame({"AAA": [100, 50, 50, 25, 100.0]}, index=idx)
    sw = [scorecard.Switch("AAA", idx[0], "EXIT"), scorecard.Switch("AAA", idx[2], "RE-ENTRY")]
    res = scorecard.simulate(closes, pd.Series({"AAA": 1.0}), sw, "2026-10-19", 0.0)
    # sold at 50, bought back at 25 -> 2 units -> 200 at the end
    assert res.daily["Follow"].iloc[-1] == 200.0


def test_run_scorecard_writes_report_once_per_month(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "data").mkdir()
    pd.DataFrame({"Symbol": ["AAA"], "Qty": [10]}).to_csv("data/scorecard_baseline.csv", index=False)
    _tracking([("2026-10-19", "AAA", "SELL", "x")]).to_csv("track.csv", index=False)
    idx = pd.bdate_range("2026-10-19", periods=10)
    fetch = lambda tickers, start: pd.DataFrame({"AAA": np.linspace(100, 80, 10)}, index=idx)
    today = pd.Timestamp("2026-11-02")
    assert scorecard.due_this_month(today)
    card = scorecard.run_scorecard("track.csv", {}, fetch=fetch, today=today)
    assert "Monthly scorecard" in card and "ahead of" in card
    assert not scorecard.due_this_month(today)
    assert scorecard.due_this_month(pd.Timestamp("2026-12-01"))


def test_live_trend_ignores_intraday_month_end():
    idx = pd.bdate_range("2025-06-02", "2026-10-30")
    px = pd.Series(100.0, index=idx)
    px.iloc[-1] = 10.0  # 30 Oct intraday crash must not count as the October month-end close
    f = compute_market_features(pd.DataFrame({"Close": px}))
    assert f["trend_month_end_close"] == 100.0 and f["trend_below"] is False
