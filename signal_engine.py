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
    thesis_is_set = (
        thesis_text is not None
        and str(thesis_text).strip() != ""
        and str(thesis_text).strip() not in ("NOT YET SET", "NOT SET")
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
    )

