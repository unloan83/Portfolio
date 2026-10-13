"""Shared Signal Engine module for portfolio analysis and backtesting.

Provides a unified single source of truth for technical and fundamental
signal evaluations.
"""
from dataclasses import dataclass
from typing import Optional

from config import RISK_CONFIG, RiskConfig


# Technical states in which no trend could be computed. BAD_DATA means a price
# history was fetched but failed a sanity check, so it must not drive a trade.
DATA_FAILURE_TRENDS = ("NO_DATA", "FETCH_ERROR", "NO_TICKER", "BAD_DATA")

# One action per decision, so the report never shows e.g. SELL next to "Hold".
# analysis.py appends share counts to TRIM / ACCUMULATE / BUY.
DECISION_ACTIONS = {
    "SELL": "Exit",
    "TRIM": "Trim",
    "ACCUMULATE": "Accumulate",
    "BUY": "Buy",
    "HOLD": "Hold",
    "NO THESIS": "Set thesis in thesis.csv",
    "NO DATA": "Verify price manually",
    "VERIFY DATA": "Verify price data before acting",
}


@dataclass(frozen=True)
class SignalEvaluationResult:
    signal: str
    recommended_action: str
    explanation: str
    thesis_status: str
    conviction: Optional[float]
    technical_trend: str
    is_overextended: bool
    fundamental_pass: bool
    fundamental_unknown: bool
    decision: str = ""
    horizon_short_term: str = ""
    horizon_long_term: str = ""
    rationale: str = ""
    sizing_note: str = ""
    data_status: str = "OK"


"""
DECISION TREE:
1. NO DATA / FETCH ERROR / NO TICKER / BAD DATA -> Signal: "⚪ NO DATA"
2. NO THESIS (thesis missing or "NOT YET SET") -> Signal: "⚠️ NO THESIS", Reason: "Thesis not set for symbol."
3. THESIS INVALIDATED (current_price <= Invalidation_Price) -> Signal: "🔴 STRG SELL", Reason: "thesis invalidated"
4. THESIS INTACT:
   - BEARISH technical + total_return > 25% -> Signal: "🟡 HOLD / TRIM WATCH", Reason: "pullback within thesis, not a breakdown"
   - BEARISH technical + total_return < 0% -> Signal: "🔴 STRG SELL", Reason: "breakdown + thesis stress"
   - BEARISH technical (other) -> Signal: "🔴 STRG SELL", Reason: "Below 200 DMA structural breakdown."
   - BULLISH + Sector Exposure > Max -> Signal: "⚠️ SECTOR CAP", Reason: "Sector cluster ... limit."
   - Overextended -> Signal: "🟡 HOLD / PEAK", Reason: "Overextended ..."
   - ROE < Minimum -> Signal: "🟡 HOLD / RISK", Reason: "Weak operational efficiency ..."
   - ROE Unknown -> Signal: "🟡 HOLD / REVIEW", Reason: "ROE unavailable ..."
   - BULLISH -> Signal: "🟢 ACCUMULATE", Reason: "Healthy structural accumulation channel."
   - Neutral / Other -> Signal: "🟡 HOLD", Reason: "Sideways consolidation pattern."

RECOMMENDED ACTION:
Derived from the decision via DECISION_ACTIONS. ACCUMULATE on a BEARISH
pullback (return > 25%) reads "Add on weakness (small)".

DECISION WITHOUT USABLE TECHNICAL DATA:
The broker price (fallback_price) still drives the thesis-invalidation and
position-cap checks, giving SELL or TRIM; otherwise NO DATA (nothing fetched)
or VERIFY DATA (fetched data failed a sanity check, see data_issue).
"""


def evaluate_signal(
    current_price: Optional[float],
    dma_50: Optional[float],
    dma_200: Optional[float],
    roe: Optional[float] = None,
    stock_sector: str = "unknown",
    sector_risk_exposure: float = 0.0,
    technical_trend_override: Optional[str] = None,
    total_return: Optional[float] = None,
    thesis_text: Optional[str] = "INTACT",
    conviction: Optional[float] = None,
    invalidation_price: Optional[float] = None,
    stock_weight: float = 0.0,
    config: RiskConfig = RISK_CONFIG,
    fallback_price: Optional[float] = None,
    data_issue: Optional[str] = None,
) -> SignalEvaluationResult:
    """Evaluates combined technical, thesis, and fundamental signals for a single symbol."""
    fundamental_pass = roe is None or roe >= config.minimum_roe
    fundamental_unknown = roe is None

    is_overextended = False

    if data_issue:
        technical_trend = "BAD_DATA"
    elif technical_trend_override is not None:
        technical_trend = technical_trend_override
    elif current_price is None or dma_50 is None or dma_200 is None:
        technical_trend = "NO_DATA"
    else:
        if current_price < dma_200:
            technical_trend = "BEARISH"
        elif current_price > dma_50 and dma_50 > dma_200:
            technical_trend = "BULLISH"
            if current_price > (dma_50 * config.overextension_multiple):
                is_overextended = True
        else:
            technical_trend = "NEUTRAL"

    # Evaluate Thesis Status
    thesis_str = str(thesis_text).strip().upper() if thesis_text is not None else ""
    thesis_is_set = (
        thesis_str != ""
        and thesis_str not in ("NOT YET SET", "NOT SET", "NAN", "NONE", "NULL", "UNDEFINED")
    )
    has_technical_data = technical_trend not in DATA_FAILURE_TRENDS
    eval_price = current_price if has_technical_data else fallback_price

    thesis_invalidated = False
    if thesis_is_set and invalidation_price is not None and eval_price is not None:
        if eval_price <= invalidation_price:
            thesis_invalidated = True

    if not thesis_is_set:
        thesis_status = "NOT SET"
    elif thesis_invalidated:
        thesis_status = "INVALIDATED"
    else:
        thesis_status = "INTACT"

    # Determine Signal and Explanation based on Decision Tree
    if not has_technical_data:
        signal = "⚪ NO DATA"
        explanation = (
            f"Could not evaluate ({technical_trend.replace('_', ' ').lower()}) "
            "— verify manually."
        )
        if data_issue:
            explanation += f" {data_issue}"
    elif thesis_status == "NOT SET":
        signal = "⚠️ NO THESIS"
        explanation = "Thesis not set for symbol."
    elif thesis_status == "INVALIDATED":
        signal = "🔴 STRG SELL"
        explanation = "thesis invalidated"
    elif technical_trend == "BEARISH":
        if total_return is not None and total_return > 25.0:
            signal = "🟡 HOLD / TRIM WATCH"
            explanation = "pullback within thesis, not a breakdown"
        elif total_return is not None and total_return < 0.0:
            signal = "🔴 STRG SELL"
            explanation = "breakdown + thesis stress"
        else:
            signal = "🔴 STRG SELL"
            explanation = "Below 200 DMA structural breakdown."
    elif (
        sector_risk_exposure > config.max_sector_pct
        and technical_trend == "BULLISH"
    ):
        signal = "⚠️ SECTOR CAP"
        explanation = (
            f"{stock_sector} cluster at {sector_risk_exposure:.1f}% — "
            "would-be BUY blocked by concentration limit."
        )
    elif is_overextended:
        signal = "🟡 HOLD / PEAK"
        overextension_pct = config.overextension_multiple - 1
        explanation = f"Overextended >{overextension_pct:.0%} above 50 DMA."
    elif fundamental_unknown:
        signal = "🟡 HOLD / REVIEW"
        explanation = "ROE unavailable — verify fundamentals manually."
    elif not fundamental_pass:
        signal = "🟡 HOLD / RISK"
        explanation = (
            "Weak operational efficiency ROE "
            f"< {config.minimum_roe:.0%}."
        )
    elif technical_trend == "BULLISH":
        signal = "🟢 ACCUMULATE"
        explanation = "Healthy structural accumulation channel."
    else:
        signal = "🟡 HOLD"
        explanation = "Sideways consolidation pattern."

    conviction_val = None
    if conviction is not None:
        try:
            conviction_val = float(conviction)
        except (ValueError, TypeError):
            conviction_val = None

    # --- DERIVE DECISION ENGINE ADDITIVE FIELDS ---
    if technical_trend == "BAD_DATA":
        data_status = "BAD DATA"
    elif not has_technical_data:
        data_status = "NO DATA"
    elif thesis_status == "NOT SET":
        data_status = "NO THESIS"
    else:
        data_status = "OK"

    # 1. Decision Derivation Tree (Strict, Non-Contradictory)
    if not has_technical_data:
        if thesis_status == "INVALIDATED":
            decision = "SELL"
        elif stock_weight > config.max_position_pct:
            decision = "TRIM"
        elif data_status == "BAD DATA":
            decision = "VERIFY DATA"
        else:
            decision = "NO DATA"
    elif data_status == "NO THESIS":
        decision = "NO THESIS"
    elif thesis_status == "INVALIDATED":
        decision = "SELL"
    elif (
        technical_trend == "BEARISH"
        and total_return is not None
        and total_return < 0.0
        and (thesis_status != "INTACT" or conviction_val is None or conviction_val < 4.0)
    ):
        # Reserve SELL for: thesis invalidated OR (BEARISH + negative return + conviction < 4 / thesis not intact)
        decision = "SELL"
    elif is_overextended or stock_weight > config.max_position_pct or (sector_risk_exposure > config.max_sector_pct and stock_weight >= (config.max_position_pct / 2)):
        # TRIM if overextended, position weight exceeds max cap (8%), or sector exposure > 25% for a major holding
        decision = "TRIM"
    elif (
        thesis_status == "INTACT"
        and conviction_val is not None
        and conviction_val >= 4.0
        and stock_weight < config.max_position_pct
        and sector_risk_exposure <= config.max_sector_pct
        and (
            technical_trend == "BULLISH"
            or (technical_trend == "BEARISH" and total_return is not None and total_return > 25.0)
        )
    ):
        if stock_weight == 0.0:
            decision = "BUY"
        else:
            decision = "ACCUMULATE"
    else:
        # Default HOLD (including BEARISH pullback with negative return when thesis is INTACT and conviction >= 4)
        decision = "HOLD"

    # 2. Horizon and Rationale Construction (Harmonized with Decision & Dynamic Variables)
    if not has_technical_data:
        trend_str = technical_trend.replace('_', ' ').lower()
        fb_str = f"₹{fallback_price:.2f}" if fallback_price is not None else "N/A"
        inv_str = f"₹{invalidation_price:.2f}" if invalidation_price is not None else "N/A"
        if data_issue:
            horizon_short_term = f"BAD DATA — {data_issue}"
            missing = f"Unreliable price data: {data_issue}"
        else:
            horizon_short_term = "NO DATA — Fresh price history unavailable"
            missing = f"Missing data: Technical price history unavailable ({trend_str})"
        if decision == "SELL":
            horizon_long_term = f"INVALIDATED — Broker price {fb_str} breached invalidation level {inv_str}"
            rationale = f"Thesis invalidated: Broker price {fb_str} <= invalidation price {inv_str}. {missing}."
        elif decision == "TRIM":
            horizon_long_term = "UNVERIFIED — Technical layer missing; risk limits require position trimming"
            rationale = f"Position cap breach: Weight {stock_weight:.1f}% exceeds max position limit ({config.max_position_pct:.1f}%); trim required. {missing}."
        else:
            horizon_long_term = "UNVERIFIED — Technical layer missing"
            rationale = f"{missing}; evaluation incomplete."
    elif data_status == "NO THESIS":
        cp_str = f"₹{current_price:.2f}" if current_price is not None else "N/A"
        horizon_short_term = f"{technical_trend} — Price {cp_str} evaluation complete"
        horizon_long_term = "NO THESIS — Thesis not set for symbol"
        rationale = "Missing thesis: Long-term investment thesis and invalidation price not defined in thesis.csv."
    else:
        cp_str = f"₹{current_price:.2f}" if current_price is not None else "N/A"
        d50_str = f"₹{dma_50:.2f}" if dma_50 is not None else "N/A"
        d200_str = f"₹{dma_200:.2f}" if dma_200 is not None else "N/A"
        ret_str = f"{total_return:+.2f}%" if total_return is not None else "N/A"
        inv_str = f"₹{invalidation_price:.2f}" if invalidation_price is not None else "N/A"
        conv_str = f"{int(conviction_val)}/5" if conviction_val is not None else "N/A"

        horizon_short_term = f"{technical_trend} — Price {cp_str} vs 50 DMA ({d50_str}) and 200 DMA ({d200_str})"

        if thesis_status == "INVALIDATED":
            horizon_long_term = f"INVALIDATED — Price {cp_str} breached invalidation level {inv_str}"
            rationale = f"Thesis invalidated: Price {cp_str} <= invalidation price {inv_str}."
        elif decision == "SELL":
            horizon_long_term = f"BROKEN — 200 DMA breakdown with negative return ({ret_str}) and conviction ({conv_str}) < 4"
            rationale = f"Structural breakdown: Price {cp_str} < 200 DMA ({d200_str}) with return {ret_str}; conviction ({conv_str}) < 4 or thesis {thesis_status} insufficient to hold breakdown."
        elif decision == "TRIM":
            horizon_long_term = f"INTACT — High conviction ({conv_str}) thesis intact; risk limits require position/sector trimming"
            if is_overextended:
                overextension_pct = config.overextension_multiple - 1.0
                rationale = f"Overextended: Price {cp_str} > 50 DMA ({d50_str}) by >{overextension_pct:.0%}; position trimmed for peak profit lock."
            elif stock_weight > config.max_position_pct:
                rationale = f"Position cap breach: Weight {stock_weight:.1f}% exceeds max position limit ({config.max_position_pct:.1f}%); trim required."
            elif sector_risk_exposure > config.max_sector_pct:
                rationale = f"Sector cap breach: {stock_sector} sector exposure ({sector_risk_exposure:.1f}%) exceeds sector limit ({config.max_sector_pct:.1f}%); trim holding ({stock_weight:.1f}% weight) for concentration risk control."
            else:
                rationale = f"Risk trim trigger: Position weight ({stock_weight:.1f}%), sector risk ({sector_risk_exposure:.1f}%), or overextension active; trim for capital protection."
        elif decision in ("ACCUMULATE", "BUY"):
            if total_return is not None and total_return > 25.0 and technical_trend == "BEARISH":
                horizon_long_term = f"INTACT — High conviction ({conv_str}) thesis intact; buyable pullback (return {ret_str} > 25%)"
                rationale = f"Pullback accumulation: Total return {ret_str} > 25% with conviction ({conv_str}) and intact thesis above invalidation {inv_str}; price {cp_str} below 200 DMA ({d200_str}) offers dip-buy channel."
            else:
                horizon_long_term = f"INTACT — High conviction ({conv_str}) thesis intact; price {cp_str} above invalidation ({inv_str})"
                rationale = f"Structural accumulation: Price {cp_str} > 50 DMA ({d50_str}) > 200 DMA ({d200_str}); weight {stock_weight:.1f}% < {config.max_position_pct:.1f}% max cap with conviction ({conv_str})."
        else:  # HOLD
            if technical_trend == "BEARISH" and total_return is not None and total_return < 0.0:
                horizon_long_term = f"INTACT — High conviction ({conv_str}) thesis intact above invalidation ({inv_str}); drawdown monitored"
                rationale = f"High-conviction pullback hold: Price {cp_str} < 200 DMA ({d200_str}) with return {ret_str}, but high conviction ({conv_str}) thesis remains INTACT above invalidation ({inv_str})."
            elif technical_trend == "NEUTRAL":
                horizon_long_term = f"INTACT — Thesis intact ({conv_str}); price {cp_str} above invalidation ({inv_str})"
                rationale = f"Consolidation hold: Price {cp_str} moving sideways between 50 DMA ({d50_str}) and 200 DMA ({d200_str}); conviction ({conv_str}) thesis INTACT above invalidation ({inv_str})."
            else:
                horizon_long_term = f"INTACT — Thesis intact ({conv_str}); price {cp_str} above invalidation ({inv_str})"
                rationale = f"Position hold: Technical trend {technical_trend}, total return {ret_str}, position weight {stock_weight:.1f}%; conviction ({conv_str}) thesis INTACT above invalidation ({inv_str})."

    recommended_action = DECISION_ACTIONS.get(decision, "Hold")
    if decision in ("ACCUMULATE", "BUY") and technical_trend == "BEARISH":
        recommended_action = "Add on weakness (small)"

    if recommended_action == "Add on weakness (small)":
        conv_str = f"{int(conviction_val)}/5" if conviction_val is not None else "N/A"
        sizing_note = f"Add on weakness (small) — Conviction {conv_str} with intact thesis allows small tactical accumulation on deep dips."
    elif signal == "🟢 ACCUMULATE":
        conv_str = f"{int(conviction_val)}/5" if conviction_val is not None else "N/A"
        sizing_note = f"Accumulate — Conviction {conv_str} with healthy structural accumulation channel."
    else:
        sizing_note = "N/A"

    return SignalEvaluationResult(
        signal=signal,
        recommended_action=recommended_action,
        explanation=explanation,
        thesis_status=thesis_status,
        conviction=conviction_val,
        technical_trend=technical_trend,
        is_overextended=is_overextended,
        fundamental_pass=fundamental_pass,
        fundamental_unknown=fundamental_unknown,
        decision=decision,
        horizon_short_term=horizon_short_term,
        horizon_long_term=horizon_long_term,
        rationale=rationale,
        sizing_note=sizing_note,
        data_status=data_status,
    )

