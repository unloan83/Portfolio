"""Unit tests for signal_engine module."""
import pytest
from config import RISK_CONFIG
from signal_engine import SignalEvaluationResult, evaluate_signal


def test_signal_accumulate():
    # Healthy uptrend: price > dma_50 > dma_200, not overextended, ROE >= minimum_roe
    res = evaluate_signal(
        current_price=110.0,
        dma_50=105.0,
        dma_200=100.0,
        roe=0.15,
        stock_sector="Banking",
        sector_risk_exposure=10.0,
    )
    assert res.signal == "🟢 ACCUMULATE"
    assert res.technical_trend == "BULLISH"
    assert not res.is_overextended
    assert res.fundamental_pass
    assert not res.fundamental_unknown
    assert "Healthy structural accumulation" in res.explanation


def test_signal_strg_sell():
    # Bearish breakdown: price < dma_200
    res = evaluate_signal(
        current_price=90.0,
        dma_50=95.0,
        dma_200=100.0,
        roe=0.15,
        stock_sector="Banking",
        sector_risk_exposure=10.0,
    )
    assert res.signal == "🔴 STRG SELL"
    assert res.technical_trend == "BEARISH"
    assert "Below 200 DMA structural breakdown" in res.explanation


def test_signal_sector_cap():
    # Bullish trend but sector exposure exceeds max_sector_pct (25%)
    res = evaluate_signal(
        current_price=110.0,
        dma_50=105.0,
        dma_200=100.0,
        roe=0.15,
        stock_sector="Banking",
        sector_risk_exposure=30.0,
    )
    assert res.signal == "⚠️ SECTOR CAP"
    assert res.technical_trend == "BULLISH"
    assert "concentration limit" in res.explanation


def test_signal_hold_peak_overextended():
    # Bullish trend but overextended (> 1.25 * dma_50 = 131.25)
    res = evaluate_signal(
        current_price=135.0,
        dma_50=105.0,
        dma_200=100.0,
        roe=0.15,
        stock_sector="Banking",
        sector_risk_exposure=10.0,
    )
    assert res.signal == "🟡 HOLD / PEAK"
    assert res.technical_trend == "BULLISH"
    assert res.is_overextended
    assert "Overextended" in res.explanation


def test_signal_roe_unknown():
    # Bullish trend but ROE is None
    res = evaluate_signal(
        current_price=110.0,
        dma_50=105.0,
        dma_200=100.0,
        roe=None,
        stock_sector="Banking",
        sector_risk_exposure=10.0,
    )
    assert res.signal == "🟡 HOLD / REVIEW"
    assert res.technical_trend == "BULLISH"
    assert res.fundamental_unknown
    assert "ROE unavailable" in res.explanation


def test_signal_hold_risk_low_roe():
    # Bullish trend but ROE < 0.10
    res = evaluate_signal(
        current_price=110.0,
        dma_50=105.0,
        dma_200=100.0,
        roe=0.05,
        stock_sector="Banking",
        sector_risk_exposure=10.0,
    )
    assert res.signal == "🟡 HOLD / RISK"
    assert not res.fundamental_pass
    assert "Weak operational efficiency" in res.explanation


def test_signal_no_thesis():
    res = evaluate_signal(
        current_price=110.0,
        dma_50=105.0,
        dma_200=100.0,
        roe=0.15,
        thesis_text="NOT YET SET",
    )
    assert res.signal == "⚠️ NO THESIS"
    assert res.thesis_status == "NOT SET"
    assert res.decision == "NO THESIS"
    assert res.recommended_action == "Set thesis in thesis.csv"


def test_signal_thesis_invalidated():
    res = evaluate_signal(
        current_price=80.0,
        dma_50=95.0,
        dma_200=100.0,
        thesis_text="Strong retail growth",
        conviction=2.0,
        invalidation_price=85.0,
    )
    assert res.signal == "🔴 STRG SELL"
    assert res.thesis_status == "INVALIDATED"
    assert res.explanation == "thesis invalidated"
    assert res.recommended_action == "Exit"


def test_signal_bearish_pullback_strong_return():
    res = evaluate_signal(
        current_price=90.0,
        dma_50=95.0,
        dma_200=100.0,
        total_return=30.0,
        thesis_text="Long term compounder",
        conviction=5.0,
    )
    assert res.signal == "🟡 HOLD / TRIM WATCH"
    assert res.explanation == "pullback within thesis, not a breakdown"
    assert res.recommended_action == "Add on weakness (small)"


def test_signal_bearish_negative_return():
    res = evaluate_signal(
        current_price=90.0,
        dma_50=95.0,
        dma_200=100.0,
        total_return=-10.0,
        thesis_text="Long term compounder",
        conviction=3.0,
    )
    assert res.signal == "🔴 STRG SELL"
    assert res.explanation == "breakdown + thesis stress"
    # SELL decision must never be paired with a "Hold" action.
    assert res.decision == "SELL"
    assert res.recommended_action == "Exit"


def test_signal_thesis_nan_and_unset_handling():
    import numpy as np
    for unset_val in ["NOT YET SET", "not set", "nan", "None", "NULL", "undefined", np.nan]:
        res = evaluate_signal(
            current_price=110.0,
            dma_50=105.0,
            dma_200=100.0,
            roe=0.15,
            thesis_text=unset_val,
        )
        assert res.signal == "⚠️ NO THESIS"
        assert res.thesis_status == "NOT SET"


def test_signal_thesis_intact_and_invalidated_matrix():
    # Intact thesis with high conviction
    res_intact = evaluate_signal(
        current_price=110.0,
        dma_50=105.0,
        dma_200=100.0,
        roe=0.15,
        thesis_text="Solid compounder",
        conviction=5.0,
        invalidation_price=80.0,
    )
    assert res_intact.thesis_status == "INTACT"
    assert res_intact.signal == "🟢 ACCUMULATE"

    # Invalidated thesis with low conviction -> Exit
    res_inv = evaluate_signal(
        current_price=75.0,
        dma_50=95.0,
        dma_200=100.0,
        thesis_text="Turnaround play",
        conviction=2.0,
        invalidation_price=80.0,
    )
    assert res_inv.thesis_status == "INVALIDATED"
    assert res_inv.signal == "🔴 STRG SELL"
    assert res_inv.recommended_action == "Exit"




def test_no_data_uses_broker_price_for_thesis_invalidation():
    res = evaluate_signal(
        current_price=None,
        dma_50=None,
        dma_200=None,
        technical_trend_override="NO_DATA",
        thesis_text="Index exposure",
        conviction=4.0,
        invalidation_price=240.0,
        fallback_price=230.0,
    )
    assert res.signal == "⚪ NO DATA"
    assert res.thesis_status == "INVALIDATED"
    assert res.decision == "SELL"
    assert res.recommended_action == "Exit"
    assert "Broker price ₹230.00" in res.rationale


def test_no_data_without_breach_stays_no_data():
    res = evaluate_signal(
        current_price=None,
        dma_50=None,
        dma_200=None,
        technical_trend_override="NO_DATA",
        thesis_text="Index exposure",
        conviction=4.0,
        invalidation_price=200.0,
        fallback_price=266.0,
    )
    assert res.decision == "NO DATA"
    assert res.recommended_action == "Verify price manually"


def test_no_data_still_trims_position_cap_breach():
    res = evaluate_signal(
        current_price=None,
        dma_50=None,
        dma_200=None,
        technical_trend_override="FETCH_ERROR",
        thesis_text="Core holding",
        conviction=5.0,
        invalidation_price=100.0,
        fallback_price=500.0,
        stock_weight=12.0,
    )
    assert res.decision == "TRIM"
    assert res.recommended_action == "Trim"


def test_data_issue_blocks_trade_on_suspect_price():
    # Live price looks like a breakdown, but it failed the sanity check.
    res = evaluate_signal(
        current_price=237.0,
        dma_50=300.0,
        dma_200=334.0,
        total_return=-49.0,
        thesis_text="City gas franchise",
        conviction=3.0,
        invalidation_price=200.0,
        fallback_price=401.0,
        data_issue="Live price differs from broker price.",
    )
    assert res.technical_trend == "BAD_DATA"
    assert res.data_status == "BAD DATA"
    assert res.thesis_status == "INTACT"  # judged on the broker price
    assert res.decision == "VERIFY DATA"
    assert res.recommended_action == "Verify price data before acting"


@pytest.mark.parametrize(
    "kwargs",
    [
        dict(current_price=80.0, dma_50=95.0, dma_200=100.0, total_return=-20.0, conviction=4.0, invalidation_price=85.0),
        dict(current_price=90.0, dma_50=95.0, dma_200=100.0, total_return=-5.0, conviction=3.0, invalidation_price=50.0),
        dict(current_price=110.0, dma_50=105.0, dma_200=100.0, total_return=10.0, conviction=5.0, invalidation_price=50.0, stock_weight=14.0),
        dict(current_price=90.0, dma_50=95.0, dma_200=100.0, total_return=40.0, conviction=4.0, invalidation_price=50.0, stock_weight=2.0),
        dict(current_price=110.0, dma_50=105.0, dma_200=100.0, roe=0.2, total_return=10.0, conviction=4.0, invalidation_price=50.0, stock_weight=2.0),
    ],
)
def test_recommended_action_always_matches_decision(kwargs):
    res = evaluate_signal(thesis_text="Thesis", **kwargs)
    expected = {
        "SELL": {"Exit"},
        "TRIM": {"Trim"},
        "ACCUMULATE": {"Accumulate", "Add on weakness (small)"},
        "HOLD": {"Hold"},
    }[res.decision]
    assert res.recommended_action in expected
