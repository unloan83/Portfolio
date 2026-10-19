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
    # Bearish breakdown: 20 sessions > 3% below 200 DMA enters REVIEW with hysteresis
    res = evaluate_signal(
        current_price=90.0,
        dma_50=95.0,
        dma_200=100.0,
        roe=0.15,
        stock_sector="Banking",
        sector_risk_exposure=10.0,
        sessions_below_200dma=20,
    )
    assert res.signal == "🟡 REVIEW"
    assert res.technical_trend == "BEARISH"
    assert "200-DMA breakdown hysteresis review" in res.explanation
    assert res.decision == "REVIEW"
    assert res.recommended_action == "Review"


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
    assert "EXTENDED: don't add" in res.explanation


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
    # Core role with 1 close below level gives REVIEW
    res = evaluate_signal(
        current_price=80.0,
        dma_50=95.0,
        dma_200=100.0,
        thesis_text="Strong retail growth",
        conviction=2.0,
        invalidation_price=85.0,
        role="core",
    )
    assert res.signal == "🟡 REVIEW"
    assert res.thesis_status == "INVALIDATED"
    assert "invalidation breached" in res.explanation
    assert res.decision == "REVIEW"
    assert res.recommended_action == "Review"

    # Tactical role keeps immediate hard stop (SELL)
    res_tac = evaluate_signal(
        current_price=80.0,
        dma_50=95.0,
        dma_200=100.0,
        thesis_text="Tactical gold",
        conviction=2.0,
        invalidation_price=85.0,
        role="tactical",
    )
    assert res_tac.signal == "🔴 STRG SELL"
    assert res_tac.decision == "SELL"
    assert res_tac.recommended_action == "Exit"


def test_signal_bearish_pullback_strong_return():
    # Pullback below 200-DMA: no longer "Add on weakness (small)", defaults to HOLD
    res = evaluate_signal(
        current_price=90.0,
        dma_50=95.0,
        dma_200=100.0,
        total_return=30.0,
        thesis_text="Long term compounder",
        conviction=5.0,
        roe=0.15,
    )
    assert res.signal == "🟡 HOLD / PULLBACK"
    assert "Pullback below 200-DMA" in res.explanation
    assert res.decision == "HOLD"
    assert res.recommended_action == "Hold"


def test_signal_bearish_negative_return():
    # BEARISH with negative return no longer auto-sells; it gives HOLD (or REVIEW if 20 sessions below)
    res = evaluate_signal(
        current_price=90.0,
        dma_50=95.0,
        dma_200=100.0,
        total_return=-10.0,
        thesis_text="Long term compounder",
        conviction=3.0,
        roe=0.15,
    )
    assert res.signal == "🟡 HOLD / PULLBACK"
    assert res.decision == "HOLD"
    assert res.recommended_action == "Hold"


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

    # Tactical role -> Exit immediately on breach
    res_tac = evaluate_signal(
        current_price=75.0,
        dma_50=95.0,
        dma_200=100.0,
        thesis_text="Turnaround play",
        conviction=2.0,
        invalidation_price=80.0,
        role="tactical",
    )
    assert res_tac.thesis_status == "INVALIDATED"
    assert res_tac.signal == "🔴 STRG SELL"
    assert res_tac.recommended_action == "Exit"

    # Core role with 1 close below -> REVIEW
    res_core = evaluate_signal(
        current_price=75.0,
        dma_50=95.0,
        dma_200=100.0,
        thesis_text="Turnaround play",
        conviction=2.0,
        invalidation_price=80.0,
        role="core",
    )
    assert res_core.thesis_status == "INVALIDATED"
    assert res_core.signal == "🟡 REVIEW"
    assert res_core.recommended_action == "Review"


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
        role="core",
    )
    assert res.signal == "⚪ NO DATA"
    assert res.thesis_status == "INVALIDATED"
    # Broker price never moves, so closes cannot confirm: ask for a data check.
    assert res.decision == "NO DATA"
    assert res.recommended_action == "Verify price manually"
    assert "invalidation breached on broker price" in res.rationale

    # Tactical role escalates to SELL on broker price
    res_tac = evaluate_signal(
        current_price=None,
        dma_50=None,
        dma_200=None,
        technical_trend_override="NO_DATA",
        thesis_text="Tactical gold",
        conviction=4.0,
        invalidation_price=240.0,
        fallback_price=230.0,
        role="tactical",
    )
    assert res_tac.decision == "SELL"
    assert res_tac.recommended_action == "Exit"


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
        "REVIEW": {"Review"},
        "ACCUMULATE": {"Accumulate", "ACCUMULATE (next monthly review)"},
        "HOLD": {"Hold"},
    }[res.decision]
    assert res.recommended_action in expected


# ==============================================================================
# PART 5 DEDICATED TESTS: Trailing Stop, Invalidation, Review Hysteresis, Accumulate
# ==============================================================================

def test_trailing_stop_rules():
    # 1. Loser below trailing stop level -> no TRIM
    res_loser = evaluate_signal(
        current_price=60.0,
        dma_50=90.0,
        dma_200=100.0,
        total_return=-20.0,  # losing position
        thesis_text="Intact thesis",
        conviction=4.0,
        invalidation_price=40.0,
        high_52w=100.0,
        atr=5.0,
        is_month_end=True,
    )
    assert not res_loser.trailing_stop_hit
    assert res_loser.decision != "TRIM"

    # 2. +10% gain -> not armed (needs total_return >= 50%)
    res_10pct = evaluate_signal(
        current_price=110.0,
        dma_50=105.0,
        dma_200=100.0,
        total_return=10.0,  # below 50%
        thesis_text="Intact thesis",
        conviction=4.0,
        invalidation_price=80.0,
        high_52w=200.0,
        atr=10.0,
        is_month_end=True,
    )
    assert not res_10pct.trailing_stop_hit
    assert res_10pct.decision != "TRIM"

    # 3. +140% winner 35% below its high at month-end -> TRIM 1/3
    # high = 200, 35% drawdown = 130. max(30%, 3*ATR=15) = 30% drawdown limit = 140.
    # price 130 is <= 140, total_return 140% >= 50%, is_month_end=True
    res_winner_month_end = evaluate_signal(
        current_price=130.0,
        dma_50=120.0,
        dma_200=100.0,
        total_return=140.0,
        thesis_text="Growth thesis",
        conviction=4.0,
        invalidation_price=50.0,
        high_52w=200.0,
        atr=5.0,
        is_month_end=True,
    )
    assert res_winner_month_end.trailing_stop_hit
    assert res_winner_month_end.decision == "TRIM"
    assert res_winner_month_end.rationale == "trailing stop hit"

    # 4. Same +140% winner mid-month -> no TRIM
    res_winner_mid_month = evaluate_signal(
        current_price=130.0,
        dma_50=120.0,
        dma_200=100.0,
        total_return=140.0,
        thesis_text="Growth thesis",
        conviction=4.0,
        invalidation_price=50.0,
        high_52w=200.0,
        atr=5.0,
        is_month_end=False,  # mid-month
    )
    assert not res_winner_mid_month.trailing_stop_hit
    assert res_winner_mid_month.decision != "TRIM"

    # 5. Broad index ETF is never trailing-trimmed (e.g. ICINIF, HDF250, MIR150)
    for etf_sym in ("ICINIF", "HDF250", "MIR150"):
        res_etf = evaluate_signal(
            current_price=130.0,
            dma_50=120.0,
            dma_200=100.0,
            total_return=140.0,
            thesis_text="Index ETF",
            conviction=4.0,
            invalidation_price=50.0,
            high_52w=200.0,
            atr=5.0,
            is_month_end=True,
            symbol=etf_sym,
        )
        assert not res_etf.trailing_stop_hit
        assert res_etf.decision != "TRIM"


def test_invalidation_rules():
    import pandas as pd
    # 1 close below invalidation price -> REVIEW
    hist_1 = pd.Series([105.0, 102.0, 99.0])  # invalidation at 100, 1 close below
    res_1 = evaluate_signal(
        current_price=99.0,
        dma_50=105.0,
        dma_200=100.0,
        thesis_text="Core holding",
        conviction=4.0,
        invalidation_price=100.0,
        price_history=hist_1,
        role="core",
        is_friday_close=False,
    )
    assert res_1.decision == "REVIEW"
    assert "invalidation breached" in res_1.rationale

    # 2 closes below invalidation price -> REVIEW
    hist_2 = pd.Series([105.0, 99.0, 98.0])  # 2 closes below
    res_2 = evaluate_signal(
        current_price=98.0,
        dma_50=105.0,
        dma_200=100.0,
        thesis_text="Core holding",
        conviction=4.0,
        invalidation_price=100.0,
        price_history=hist_2,
        role="core",
        is_friday_close=False,
    )
    assert res_2.decision == "REVIEW"
    assert "invalidation breached" in res_2.rationale

    # 3 closes below invalidation price -> SELL
    hist_3 = pd.Series([99.0, 98.0, 97.0])  # 3 consecutive closes below
    res_3 = evaluate_signal(
        current_price=97.0,
        dma_50=105.0,
        dma_200=100.0,
        thesis_text="Core holding",
        conviction=4.0,
        invalidation_price=100.0,
        price_history=hist_3,
        role="core",
        is_friday_close=False,
    )
    assert res_3.decision == "SELL"
    assert res_3.thesis_status == "INVALIDATED"

    # Single close >= 10% below invalidation price -> SELL
    hist_10pct = pd.Series([105.0, 102.0, 89.0])  # 89 <= 100 * 0.9 = 90
    res_10pct = evaluate_signal(
        current_price=89.0,
        dma_50=105.0,
        dma_200=100.0,
        thesis_text="Core holding",
        conviction=4.0,
        invalidation_price=100.0,
        price_history=hist_10pct,
        role="core",
        is_friday_close=False,
    )
    assert res_10pct.decision == "SELL"
    assert res_10pct.thesis_status == "INVALIDATED"

    # Friday close below invalidation price -> SELL
    res_fri = evaluate_signal(
        current_price=99.0,
        dma_50=105.0,
        dma_200=100.0,
        thesis_text="Core holding",
        conviction=4.0,
        invalidation_price=100.0,
        price_history=hist_1,
        role="core",
        is_friday_close=True,  # Friday close
    )
    assert res_fri.decision == "SELL"
    assert res_fri.thesis_status == "INVALIDATED"

    # Tactical role -> immediate SELL on first close below
    res_tactical = evaluate_signal(
        current_price=99.0,
        dma_50=105.0,
        dma_200=100.0,
        thesis_text="Tactical holding",
        conviction=2.0,
        invalidation_price=100.0,
        price_history=hist_1,
        role="tactical",
        is_friday_close=False,
    )
    assert res_tactical.decision == "SELL"
    assert res_tactical.thesis_status == "INVALIDATED"


def test_review_hysteresis():
    # Entry: close is > 3% below 200-DMA for >= 20 sessions -> enters REVIEW
    res_entry = evaluate_signal(
        current_price=95.0,  # 5% below 200 DMA 100
        dma_50=98.0,
        dma_200=100.0,
        thesis_text="Intact thesis",
        conviction=4.0,
        invalidation_price=70.0,
        sessions_below_200dma=20,
        in_dma_review=False,
    )
    assert res_entry.decision == "REVIEW"
    assert "200-DMA breakdown hysteresis review" in res_entry.explanation

    # Stays in REVIEW while below 200-DMA + 2%
    res_still_in = evaluate_signal(
        current_price=101.0,  # 1% above 200 DMA, but exit requires > 200 DMA + 2% (102.0)
        dma_50=100.0,
        dma_200=100.0,
        thesis_text="Intact thesis",
        conviction=4.0,
        invalidation_price=70.0,
        sessions_below_200dma=0,
        in_dma_review=True,
    )
    assert res_still_in.decision == "REVIEW"

    # Exit REVIEW: close is > 200-DMA + 2% (e.g. 103 > 102) -> exits REVIEW and never SELL
    res_exit = evaluate_signal(
        current_price=103.0,  # > 102.0
        dma_50=101.0,
        dma_200=100.0,
        thesis_text="Intact thesis",
        conviction=4.0,
        invalidation_price=70.0,
        sessions_below_200dma=0,
        in_dma_review=True,
        stock_weight=2.0,
        is_month_end=False,
    )
    assert res_exit.decision != "REVIEW"
    assert res_exit.decision != "SELL"


def test_accumulate_and_extended_rules():
    # Overextension (> 1.25 * 50-DMA) sets is_overextended, gives "EXTENDED: don't add", and blocks ACCUMULATE
    res_extended = evaluate_signal(
        current_price=130.0,  # 130 > 1.25 * 100 = 125
        dma_50=100.0,
        dma_200=90.0,
        thesis_text="Intact thesis",
        conviction=5.0,
        invalidation_price=70.0,
        high_52w=135.0,
        dma_200_rising=True,
        vol_adj_return_6m=1.5,
        vol_adj_return_12m=1.2,
        is_month_end=True,
        stock_weight=2.0,
        sector_risk_exposure=15.0,
    )
    assert res_extended.is_overextended
    assert "EXTENDED: don't add" in res_extended.sizing_note
    assert res_extended.decision == "HOLD"  # blocks ACCUMULATE

    # Fully qualified ACCUMULATE at month-end
    res_accum = evaluate_signal(
        current_price=110.0,
        dma_50=105.0,
        dma_200=100.0,
        thesis_text="Intact thesis",
        conviction=5.0,
        invalidation_price=70.0,
        high_52w=120.0,  # within 20% of 52w high (110 >= 96)
        dma_200_rising=True,
        vol_adj_return_6m=1.2,
        vol_adj_return_12m=1.1,
        is_month_end=True,
        stock_weight=3.0,
        sector_risk_exposure=15.0,
    )
    assert res_accum.decision == "ACCUMULATE"
    assert res_accum.recommended_action == "Accumulate"

    # Same qualified holding mid-month -> shows "ACCUMULATE (next monthly review)"
    res_mid_month = evaluate_signal(
        current_price=110.0,
        dma_50=105.0,
        dma_200=100.0,
        thesis_text="Intact thesis",
        conviction=5.0,
        invalidation_price=70.0,
        high_52w=120.0,
        dma_200_rising=True,
        vol_adj_return_6m=1.2,
        vol_adj_return_12m=1.1,
        is_month_end=False,
        stock_weight=3.0,
        sector_risk_exposure=15.0,
    )
    assert res_mid_month.decision == "ACCUMULATE"
    assert res_mid_month.recommended_action == "ACCUMULATE (next monthly review)"


# --- Precedence, fallback and ETF REVIEW rules -----------------------------

def _below_200dma_kwargs(**over):
    """A core stock > 3% below its 200-DMA for 49 sessions with an intact thesis."""
    kw = dict(
        current_price=700.0, dma_50=730.0, dma_200=745.0,
        total_return=-3.0, thesis_text="Core bank", conviction=5.0,
        invalidation_price=600.0, sessions_below_200dma=49,
        symbol="HDFBAN", role="core",
    )
    kw.update(over)
    return kw


def test_position_cap_trim_wins_over_dma_review():
    res = evaluate_signal(**_below_200dma_kwargs(stock_weight=14.9))
    assert res.dma_review_active
    assert res.decision == "TRIM"
    assert "Position cap breach" in res.rationale
    assert "REVIEW" in res.rationale


def test_dma_review_without_cap_breach_stays_review():
    res = evaluate_signal(**_below_200dma_kwargs(stock_weight=4.0))
    assert res.decision == "REVIEW"


def test_bad_data_invalidation_breach_asks_for_verification_not_review():
    res = evaluate_signal(
        current_price=236.0, dma_50=240.0, dma_200=300.0,
        thesis_text="City gas", conviction=3.0, invalidation_price=430.75,
        fallback_price=401.15, data_issue="As-of price differs from broker price.",
        stock_weight=0.5, role="core",
    )
    assert res.decision == "VERIFY DATA"
    assert "live price unreliable" in res.rationale
    assert "1 of" not in res.rationale


def test_index_etf_ignores_20_session_rule_but_uses_10_month_rule():
    kw = dict(current_price=254.0, dma_50=262.0, dma_200=268.0, total_return=-5.0,
              thesis_text="Index core", conviction=4.0, invalidation_price=200.0,
              sessions_below_200dma=24, symbol="ICINIF", sma_10_month=266.0)
    assert evaluate_signal(**kw, is_month_end=False).decision != "REVIEW"
    assert evaluate_signal(**kw, is_month_end=True).decision == "REVIEW"
    # A single stock with the same numbers enters REVIEW on the session rule.
    kw["symbol"] = "ONGC"
    assert evaluate_signal(**kw, is_month_end=False).decision == "REVIEW"


# --- Decision snapshot: one row per rule path; fails if any path changes -----

_SNAPSHOT = [
    # (name, kwargs, expected decision)
    ("tactical stop", dict(current_price=124.0, dma_50=130.0, dma_200=132.0, total_return=-10.0,
                           invalidation_price=131.8, role="tactical", conviction=2.0), "SELL"),
    ("core 1 close below", dict(current_price=207.0, dma_50=215.0, dma_200=220.0, total_return=-12.0,
                                invalidation_price=208.04, consecutive_closes_below=1, conviction=4.0), "REVIEW"),
    ("core 3 closes below", dict(current_price=207.0, dma_50=215.0, dma_200=220.0, total_return=-12.0,
                                 invalidation_price=208.04, consecutive_closes_below=3, conviction=4.0), "SELL"),
    ("core 10% gap", dict(current_price=180.0, dma_50=215.0, dma_200=220.0, total_return=-20.0,
                          invalidation_price=208.04, consecutive_closes_below=1, conviction=4.0), "SELL"),
    ("cap breach in review", dict(current_price=700.0, dma_50=730.0, dma_200=745.0, total_return=-3.0,
                                  invalidation_price=600.0, sessions_below_200dma=49, stock_weight=14.9,
                                  conviction=5.0), "TRIM"),
    ("trend review", dict(current_price=700.0, dma_50=730.0, dma_200=745.0, total_return=-3.0,
                          invalidation_price=600.0, sessions_below_200dma=49, stock_weight=4.0,
                          conviction=5.0), "REVIEW"),
    ("trailing stop month-end", dict(current_price=160.0, dma_50=200.0, dma_200=170.0, total_return=60.0,
                                     invalidation_price=80.0, high_52w=255.0, atr=10.0, is_month_end=True,
                                     stock_weight=3.0, conviction=4.0), "TRIM"),
    ("trailing stop mid-month", dict(current_price=160.0, dma_50=200.0, dma_200=170.0, total_return=60.0,
                                     invalidation_price=80.0, high_52w=255.0, atr=10.0, is_month_end=False,
                                     stock_weight=3.0, conviction=4.0), "HOLD"),
    ("loser never trailing-trimmed", dict(current_price=160.0, dma_50=200.0, dma_200=170.0, total_return=-5.0,
                                          invalidation_price=80.0, high_52w=255.0, atr=10.0, is_month_end=True,
                                          stock_weight=3.0, conviction=4.0), "HOLD"),
    ("accumulate", dict(current_price=1741.0, dma_50=1650.0, dma_200=1550.0, total_return=50.0,
                        invalidation_price=1003.2, high_52w=1800.0, stock_weight=3.7, conviction=4.0,
                        dma_200_rising=True, vol_adj_return_6m=0.8, vol_adj_return_12m=0.9), "ACCUMULATE"),
    ("extended blocks accumulate", dict(current_price=2200.0, dma_50=1650.0, dma_200=1550.0, total_return=90.0,
                                        invalidation_price=1003.2, high_52w=2200.0, stock_weight=3.7, conviction=4.0,
                                        dma_200_rising=True, vol_adj_return_6m=0.8, vol_adj_return_12m=0.9), "HOLD"),
    ("broker fallback breach", dict(current_price=None, dma_50=None, dma_200=None, technical_trend_override="NO_DATA",
                                    invalidation_price=430.75, fallback_price=401.15, conviction=3.0), "NO DATA"),
    ("no thesis", dict(current_price=110.0, dma_50=105.0, dma_200=100.0, thesis_text="NOT YET SET"), "NO THESIS"),
]


@pytest.mark.parametrize("name,kwargs,expected", _SNAPSHOT, ids=[s[0] for s in _SNAPSHOT])
def test_decision_snapshot(name, kwargs, expected):
    kwargs = dict(kwargs)
    kwargs.setdefault("thesis_text", "Thesis")
    assert evaluate_signal(**kwargs).decision == expected
