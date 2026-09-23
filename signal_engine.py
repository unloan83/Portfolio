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
    explanation: str
    technical_trend: str
    is_overextended: bool
    fundamental_pass: bool
    fundamental_unknown: bool


def evaluate_signal(
    current_price: Optional[float],
    dma_50: Optional[float],
    dma_200: Optional[float],
    roe: Optional[float] = None,
    stock_sector: str = "unknown",
    sector_risk_exposure: float = 0.0,
    technical_trend_override: Optional[str] = None,
    config: RiskConfig = RISK_CONFIG,
) -> SignalEvaluationResult:
    """Evaluates combined technical and fundamental signals for a single symbol."""
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

    if technical_trend in ("NO_DATA", "FETCH_ERROR", "NO_TICKER"):
        signal = "⚪ NO DATA"
        explanation = (
            f"Could not evaluate ({technical_trend.replace('_', ' ').lower()}) "
            "— verify manually."
        )
    elif (
        sector_risk_exposure > config.max_sector_pct
        and technical_trend == "BULLISH"
    ):
        signal = "⚠️ SECTOR CAP"
        explanation = (
            f"{stock_sector} cluster at {sector_risk_exposure:.1f}% — "
            "would-be BUY blocked by concentration limit."
        )
    elif technical_trend == "BEARISH":
        signal = "🔴 STRG SELL"
        explanation = "Below 200 DMA structural breakdown."
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

    return SignalEvaluationResult(
        signal=signal,
        explanation=explanation,
        technical_trend=technical_trend,
        is_overextended=is_overextended,
        fundamental_pass=fundamental_pass,
        fundamental_unknown=fundamental_unknown,
    )
