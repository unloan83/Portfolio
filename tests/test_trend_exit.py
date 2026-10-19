import numpy as np
import pandas as pd

from analysis import market_trend_state, month_end_trend, trend_flipped_up
from config import RISK_CONFIG
from hindcast.loss_control import sig_sma_months
from signal_engine import evaluate_signal


def _series(seed=3, n=700):
    rng = np.random.default_rng(seed)
    idx = pd.bdate_range("2020-01-01", periods=n)
    return pd.Series(100 * np.exp(np.cumsum(rng.normal(0, 0.015, n))), index=idx)


def test_month_end_trend_matches_backtested_rule():
    c = _series()
    tested = sig_sma_months(c, 10)  # 1 = invested
    month_ends = c.groupby(c.index.to_period("M")).tail(1).index
    for d in month_ends[10:]:
        live = month_end_trend(c.loc[:d], is_month_end=True, months=10)
        assert live["trend_below"] == (tested.loc[d] == 0.0)
        # mid-month runs keep the state set at the previous month-end
        mid = c.loc[:d].index[-1] + pd.offsets.BDay(8)
        if mid in c.index and mid.month != d.month:
            nxt = month_end_trend(c.loc[:mid], is_month_end=False, months=10)
            assert nxt["trend_below"] == live["trend_below"]


def test_month_end_trend_needs_enough_history():
    c = _series(n=150)
    assert month_end_trend(c, True, 10)["trend_below"] is None


def _eval(**kw):
    base = dict(current_price=100.0, dma_50=105.0, dma_200=110.0, roe=0.15, thesis_text="INTACT",
                conviction=4, invalidation_price=50.0, stock_weight=3.0)
    base.update(kw)
    return evaluate_signal(**base)


def test_trend_exit_sells_stocks_only():
    res = _eval(symbol="WIPRO", trend_below=True, trend_month_end_close=100.0, trend_sma_months=112.0)
    assert res.decision == "SELL" and res.trend_exit
    assert "Trend exit" in res.rationale and "₹112.00" in res.rationale
    etf = _eval(symbol="ICINIF", trend_below=True)
    assert etf.decision != "SELL" and not etf.trend_exit
    above = _eval(symbol="WIPRO", trend_below=False)
    assert above.decision != "SELL"


def test_trend_exit_outranks_position_cap_trim():
    res = _eval(symbol="RELIND", stock_weight=14.9, trend_below=True)
    assert res.decision == "SELL"


def test_invalidation_rationale_kept_when_both_fire():
    res = _eval(symbol="WIPRO", current_price=40.0, trend_below=True, role="tactical")
    assert res.decision == "SELL" and "invalidat" in res.rationale.lower()


def test_trend_exit_can_be_disabled(monkeypatch):
    from dataclasses import replace
    cfg = replace(RISK_CONFIG, trend_exit_enabled=False)
    assert _eval(symbol="WIPRO", trend_below=True, config=cfg).decision != "SELL"


def test_market_trend_state_hysteresis():
    idx = pd.bdate_range("2024-01-01", periods=260)
    px = np.r_[np.full(220, 100.0), np.full(20, 97.0), np.full(20, 103.0)]
    states = market_trend_state(pd.Series(px, index=idx), 200, 2.0)
    assert states.iloc[219] == "RISK-ON"
    assert states.iloc[225] == "RISK-OFF"
    assert states.iloc[-1] == "RISK-ON"


def test_reentry_fires_once_after_flip():
    idx = pd.bdate_range("2025-01-01", "2026-10-31")
    px = pd.Series(100.0, index=idx)
    px[(idx >= "2026-07-01") & (idx < "2026-10-01")] = 80.0   # below at Jul/Aug month-ends
    px[idx >= "2026-09-28"] = 130.0                            # back above at Sep month-end
    hit = trend_flipped_up(px.loc[:"2026-10-02"], 10, pd.Timestamp("2026-10-02"))
    assert hit is not None and hit["close"] == 130.0
    assert trend_flipped_up(px.loc[:"2026-10-20"], 10, pd.Timestamp("2026-10-20")) is None
