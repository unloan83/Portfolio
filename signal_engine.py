"""Shared Signal Engine module for portfolio analysis and backtesting.

Provides a unified single source of truth for technical and fundamental
signal evaluations.
"""
from dataclasses import dataclass
from typing import Optional

from config import RISK_CONFIG, RiskConfig


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
1. NO DATA / FETCH ERROR / NO TICKER -> Signal: "⚪ NO DATA"
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

RECOMMENDED ACTION MATRIX:
- Conviction 4-5 + thesis intact + BEARISH pullback = "Add on weakness (small)"
- Conviction 1-2 + thesis invalidated = "Exit"
- All other cases = "Hold"
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
    config: RiskConfig = RISK_CONFIG,
) -> SignalEvaluationResult:
    """Evaluates combined technical, thesis, and fundamental signals for a single symbol."""
    fundamental_pass = roe is None or roe >= config.minimum_roe
    fundamental_unknown = roe is None

    is_overextended = False

    if technical_trend_override is not None:
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
    eval_price = current_price if current_price is not None else None

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
    if technical_trend in ("NO_DATA", "FETCH_ERROR", "NO_TICKER"):
        signal = "⚪ NO DATA"
        explanation = (
            f"Could not evaluate ({technical_trend.replace('_', ' ').lower()}) "
            "— verify manually."
        )
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

    # Derive Recommended Action
    conviction_val = None
    if conviction is not None:
        try:
            conviction_val = float(conviction)
        except (ValueError, TypeError):
            conviction_val = None

    if conviction_val in (4.0, 5.0) and thesis_status == "INTACT" and technical_trend == "BEARISH" and (total_return is not None and total_return > 25.0):
        recommended_action = "Add on weakness (small)"
    elif conviction_val in (1.0, 2.0) and thesis_status == "INVALIDATED":
        recommended_action = "Exit"
    else:
        recommended_action = "Hold"

    # --- DERIVE DECISION ENGINE ADDITIVE FIELDS ---
    if technical_trend in ("NO_DATA", "FETCH_ERROR", "NO_TICKER"):
        data_status = "NO DATA"
    elif thesis_status == "NOT SET":
        data_status = "NO THESIS"
    else:
        data_status = "OK"

    decision = signal.split(" ", 1)[-1] if " " in signal else signal

    if data_status == "NO DATA":
        horizon_short_term = "NO DATA — Fresh price history unavailable"
        horizon_long_term = "UNVERIFIED — Technical layer missing"
        rationale = explanation
    elif data_status == "NO THESIS":
        horizon_short_term = f"{technical_trend} — Price evaluation complete"
        horizon_long_term = "NO THESIS — Thesis not set for symbol"
        rationale = explanation
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
            rationale = f"Price {cp_str} breached invalidation level {inv_str}; thesis invalidated."
        elif total_return is not None and total_return < 0.0 and technical_trend == "BEARISH":
            horizon_long_term = f"STRESSED — Thesis intact above invalidation ({inv_str}), but return ({ret_str}) negative with 200 DMA breakdown"
            rationale = f"Price {cp_str} breached 200 DMA ({d200_str}) with return {ret_str}; thesis intact above invalidation ({inv_str})."
        elif total_return is not None and total_return > 25.0 and technical_trend == "BEARISH":
            horizon_long_term = f"INTACT — Thesis intact ({conv_str}); price {cp_str} above invalidation ({inv_str}) with return {ret_str}"
            rationale = f"Pullback within long-term thesis (return {ret_str} > 25%); price {cp_str} remains above invalidation {inv_str}."
        else:
            horizon_long_term = f"INTACT — Thesis intact ({conv_str}); price {cp_str} above invalidation ({inv_str})"
            rationale = f"{explanation} Price {cp_str} vs 200 DMA ({d200_str}), total return {ret_str}."

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

