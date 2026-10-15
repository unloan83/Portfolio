"""Shared Signal Engine module for portfolio analysis and backtesting.

Provides a unified single source of truth for technical and fundamental
signal evaluations.

QUANT VALIDATION (Redbull core discipline):

Hypotheses:
H1 trailing stop: a >= 30% fall from the 52w high after a >= 50% gain predicts 12-month underperformance vs NIFTYBEES.
H2 invalidation: 3 closes below the level predict underperformance better than 1 close.
H3 200-DMA REVIEW: > 3% below the 200-DMA for 20 sessions flags higher risk, but not reliably enough to SELL.
H4 accumulate gate: a rising 200-DMA + positive 6/12-month vol-adjusted momentum predicts outperformance.
H5 cap precedence: trimming above 8% reduces drawdown without materially lowering return.

Failure Modes:
- V-shaped recoveries (REVIEW/SELL at lows): False breakdown signals during sharp temporary dips trigger REVIEW or SELL actions near cycle troughs, locking in underperformance right before violent rebounds.
- Momentum crashes (accumulate gate buys tops, e.g. Sep 2024): Accumulate filters require strong 6/12-month momentum and rising 200-DMA, which can trigger buy signals at cyclical peaks immediately before sharp reversals.
- Stale broker price driving decisions: Divergence between static broker snapshot prices and active live market quotes can distort portfolio weights, trigger spurious invalidation breaches, or misallocate trims.
- Corporate-action gaps faking breakdowns: Unadjusted price series following splits, bonuses, or demergers create artificial overnight drops that mimic thesis invalidation or 200-DMA breakdowns.

Tax and Transaction Cost Disclaimer:
All signals, rule evaluations, and model returns exclude tax and transaction costs, representing an upper bound on net performance.
"""
from dataclasses import dataclass
from typing import Optional

from config import RISK_CONFIG, RiskConfig


import pandas as pd

# Technical states in which no trend could be computed. BAD_DATA means a price
# history was fetched but failed a sanity check, so it must not drive a trade.
DATA_FAILURE_TRENDS = ("NO_DATA", "FETCH_ERROR", "NO_TICKER", "BAD_DATA")

# One action per decision, so the report never shows e.g. SELL next to "Hold".
# analysis.py appends share counts to TRIM / ACCUMULATE / BUY.
DECISION_ACTIONS = {
    "SELL": "Exit",
    "TRIM": "Trim",
    "REVIEW": "Review",
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
    trailing_stop: Optional[float] = None
    trailing_stop_hit: bool = False
    # True while the 200-DMA / 10-month-SMA hysteresis REVIEW is active; callers
    # feed it back as in_dma_review on the next evaluation.
    dma_review_active: bool = False


"""
DECISION TREE:
1. NO DATA / FETCH ERROR / NO TICKER / BAD DATA -> Signal: "⚪ NO DATA"
2. NO THESIS (thesis missing or "NOT YET SET") -> Signal: "⚠️ NO THESIS", Reason: "Thesis not set for symbol."
3. THESIS INVALIDATED (current_price <= Invalidation_Price):
   - Role tactical (ICIGOL, ICIPSE): immediate hard stop -> Decision: "SELL", Action: "Exit"
   - Role core:
     - Escalate to SELL if: 3 consecutive daily closes below level, Friday close below level, or single close >= 10% below level -> Decision: "SELL", Action: "Exit"
     - Otherwise -> Decision: "REVIEW", Action: "Review", Reason: "invalidation breached, N of 3 closes"
   - Fallback price (no technical data): VERIFY DATA / NO DATA with the breach in the rationale
     (the broker price never moves, so closes cannot confirm); tactical -> SELL.
   PRECEDENCE: SELL > position-cap TRIM (> max_position_pct) / trailing-stop TRIM > REVIEW
   > sector/risk-group TRIM > ACCUMULATE > HOLD.
4. 200-DMA BREAKDOWN HYSTERESIS REVIEW:
   - Enter when close > 3% below 200-DMA for >= 20 sessions OR month-end close < 10-month SMA -> Decision: "REVIEW", Action: "Review"
   - Exit when close > 200-DMA + 2%
   - Broad index ETFs use only the month-end 10-month SMA entry rule.
   - Never escalates to SELL.
5. THESIS INTACT & NO REVIEW:
   - Trailing Stop hit (armed when total_return >= 50%; fires on month-end close at least max(30%, 3*ATR) below 52w high; index ETFs exempt; never on losers) -> Decision: "TRIM" (trim 1/3), Rationale: "trailing stop hit"
   - Position cap breach (> 8%) or Sector/Risk Group cap breach (> 25% for major holding) -> Decision: "TRIM"
   - ACCUMULATE: requires ALL of: thesis INTACT, 200-DMA rising (> 20 sessions ago), positive volatility-adjusted 6- and 12-month returns, price within 20% of 52w high, not EXTENDED, room under position/sector/risk-group caps.
     - Evaluated on last run of each month -> Decision: "ACCUMULATE", Action: "Accumulate"
     - Other runs -> Decision: "ACCUMULATE", Action: "ACCUMULATE (next monthly review)"
   - Overextended (> 1.25x 50-DMA) -> Signal: "🟡 HOLD / PEAK", Reason: "EXTENDED: don't add" (blocks ACCUMULATE, not a TRIM)
   - Other -> Signal: "🟡 HOLD", Decision: "HOLD", Action: "Hold"

RECOMMENDED ACTION:
Derived from the decision via DECISION_ACTIONS. ACCUMULATE evaluated only at
month-end; other runs show "ACCUMULATE (next monthly review)". Trailing stop
trim sells 1/3 of position.
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
    high_52w: Optional[float] = None,
    atr: Optional[float] = None,
    risk_group_exposure: float = 0.0,
    symbol: Optional[str] = None,
    role: str = "core",
    is_month_end: bool = False,
    is_friday_close: bool = False,
    consecutive_closes_below: int = 1,
    price_history: Optional[pd.Series] = None,
    sessions_below_200dma: int = 0,
    sma_10_month: Optional[float] = None,
    in_dma_review: bool = False,
    dma_200_rising: Optional[bool] = None,
    dma_200_20_ago: Optional[float] = None,
    vol_adj_return_6m: Optional[float] = None,
    vol_adj_return_12m: Optional[float] = None,
) -> SignalEvaluationResult:
    """Evaluates combined technical, thesis, and fundamental signals for a single symbol."""
    fundamental_pass = roe is None or roe >= config.minimum_roe
    fundamental_unknown = roe is None

    # Derive price history properties if provided
    if price_history is not None and len(price_history) > 0:
        if current_price is None:
            current_price = float(price_history.iloc[-1])
        if hasattr(price_history.index, "dayofweek"):
            is_friday_close = bool(price_history.index[-1].dayofweek == 4)
        if invalidation_price is not None:
            c_below = 0
            for val in reversed(price_history.values):
                if val <= invalidation_price:
                    c_below += 1
                else:
                    break
            consecutive_closes_below = c_below

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
        else:
            technical_trend = "NEUTRAL"

    # Overextension flag: > overextension_multiple above 50-DMA
    is_overextended = False
    if current_price is not None and dma_50 is not None and dma_50 > 0:
        if current_price > (dma_50 * config.overextension_multiple):
            is_overextended = True

    # Evaluate Thesis Status
    thesis_str = str(thesis_text).strip().upper() if thesis_text is not None else ""
    thesis_is_set = (
        thesis_str != ""
        and thesis_str not in ("NOT YET SET", "NOT SET", "NAN", "NONE", "NULL", "UNDEFINED")
    )
    has_technical_data = technical_trend not in DATA_FAILURE_TRENDS
    eval_price = current_price if has_technical_data else fallback_price

    invalidation_breached = False
    invalidation_escalated_to_sell = False
    invalidation_is_review = False

    if thesis_is_set and invalidation_price is not None and eval_price is not None:
        if eval_price <= invalidation_price:
            invalidation_breached = True
            is_tactical = (str(role).strip().lower() == "tactical")
            if is_tactical:
                invalidation_escalated_to_sell = True
            elif not has_technical_data:
                # The broker-price fallback path gives REVIEW, not SELL
                invalidation_is_review = True
            else:
                # Core holding check for escalation to SELL:
                # 1. 3 consecutive daily closes below level
                # 2. a Friday close below level
                # 3. single close >= invalidation_gap_pct (10%) below level
                is_3_closes = (consecutive_closes_below >= config.invalidation_confirm_closes)
                is_friday = is_friday_close
                gap_threshold = invalidation_price * (1.0 - config.invalidation_gap_pct / 100.0)
                is_severe_gap = (eval_price <= gap_threshold)
                if is_3_closes or is_friday or is_severe_gap:
                    invalidation_escalated_to_sell = True
                else:
                    invalidation_is_review = True

    if not thesis_is_set:
        thesis_status = "NOT SET"
    elif invalidation_breached:
        thesis_status = "INVALIDATED"
    else:
        thesis_status = "INTACT"

    # Trailing stop:
    # - Arm only when total_return >= trailing_min_gain_pct (50%) and total_return > 0
    # - Exempt broad index ETFs entirely (ICINIF, HDF250, MIR150)
    # - Distance: max(trailing_drawdown_pct = 30%, trailing_atr_multiple * ATR14) below 52-week high
    # - Separate from invalidation price: no max() with invalidation
    trailing_stop = None
    trailing_stop_hit = False
    is_index_etf = (symbol is not None and symbol in config.broad_index_etfs)

    if (
        not is_index_etf
        and total_return is not None
        and total_return >= config.trailing_min_gain_pct
        and total_return > 0
        and high_52w is not None
        and high_52w > 0
    ):
        dd_dist = high_52w * (config.trailing_drawdown_pct / 100.0)
        atr_dist = (config.trailing_atr_multiple * atr) if (atr is not None and atr > 0) else 0.0
        stop_dist = max(dd_dist, atr_dist)
        trailing_stop = high_52w - stop_dist

        # Fire only on LAST trading day of month (month-end close) on winners
        if (
            thesis_status == "INTACT"
            and eval_price is not None
            and is_month_end
            and eval_price <= trailing_stop
        ):
            trailing_stop_hit = True

    # 200-DMA Review with Hysteresis:
    # - Enter when close > 3% below 200-DMA for >= 20 sessions OR month-end close < 10-month SMA
    # - Exit when close > 200-DMA + 2%
    # - Never escalates to SELL
    dma_review_active = False
    if has_technical_data and current_price is not None and dma_200 is not None and dma_200 > 0:
        if in_dma_review:
            exit_level = dma_200 * (1.0 + config.dma_200_exit_pct / 100.0)
            if current_price > exit_level:
                dma_review_active = False
            else:
                dma_review_active = True
        else:
            breach_level = dma_200 * (1.0 - config.dma_200_breach_pct / 100.0)
            # Broad index ETFs only use the month-end 10-month SMA rule: a
            # 20-session single-stock trend rule is too noisy for an index.
            entered_by_sessions = (
                not is_index_etf
                and sessions_below_200dma >= config.dma_200_breach_sessions
                and current_price < breach_level
            )
            entered_by_10m = (is_month_end and sma_10_month is not None and current_price < sma_10_month)
            dma_review_active = (entered_by_sessions or entered_by_10m)

    # ACCUMULATE evaluation:
    # Require ALL of:
    # 1. thesis INTACT
    # 2. 200-DMA rising (higher than 20 sessions ago)
    # 3. positive volatility-adjusted 6- and 12-month returns
    # 4. price within 20% of 52-week high
    # 5. not EXTENDED
    # 6. room under position and sector caps
    conviction_val = None
    if conviction is not None:
        try:
            conviction_val = float(conviction)
        except (ValueError, TypeError):
            conviction_val = None

    if dma_200_rising is None:
        if dma_200 is not None and dma_200_20_ago is not None:
            is_dma_200_rising = (dma_200 > dma_200_20_ago)
        else:
            is_dma_200_rising = True
    else:
        is_dma_200_rising = dma_200_rising

    pos_vol_returns = True
    if vol_adj_return_6m is not None and vol_adj_return_12m is not None:
        pos_vol_returns = (vol_adj_return_6m > 0 and vol_adj_return_12m > 0)

    within_high = True
    if high_52w is not None and high_52w > 0 and current_price is not None:
        within_high = (current_price >= high_52w * (1.0 - config.accumulate_high_52w_pct / 100.0))

    accumulate_qualified = (
        thesis_status == "INTACT"
        and conviction_val is not None
        and conviction_val >= 4.0
        and stock_weight < config.max_position_pct
        and sector_risk_exposure <= config.max_sector_pct
        and risk_group_exposure <= config.max_risk_group_pct
        and not is_overextended
        and within_high
        and is_dma_200_rising
        and pos_vol_returns
        and technical_trend == "BULLISH"
    )

    # Determine Signal and Explanation
    if not has_technical_data:
        signal = "⚪ NO DATA"
        explanation = (
            f"Could not evaluate ({technical_trend.replace('_', ' ').lower()}) — verify manually."
        )
        if data_issue:
            explanation += f" {data_issue}"
    elif thesis_status == "NOT SET":
        signal = "⚠️ NO THESIS"
        explanation = "Thesis not set for symbol."
    elif invalidation_escalated_to_sell:
        signal = "🔴 STRG SELL"
        explanation = "thesis invalidated"
    elif invalidation_is_review:
        signal = "🟡 REVIEW"
        explanation = f"invalidation breached, {consecutive_closes_below} of {config.invalidation_confirm_closes} closes"
    elif dma_review_active:
        signal = "🟡 REVIEW"
        explanation = f"200-DMA breakdown hysteresis review ({sessions_below_200dma} sessions > 3% below 200-DMA)"
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
        overextension_pct = config.overextension_multiple - 1.0
        explanation = f"Overextended >{overextension_pct:.0%} above 50 DMA — EXTENDED: don't add"
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
    elif technical_trend == "BEARISH":
        signal = "🟡 HOLD / PULLBACK"
        explanation = "Pullback below 200-DMA within thesis."
    else:
        signal = "🟡 HOLD"
        explanation = "Sideways consolidation pattern."

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
    # Precedence: SELL > position-cap / trailing-stop TRIM > REVIEW > sector/group TRIM
    # > ACCUMULATE > HOLD. A cap breach or a fired profit stop is a concrete action
    # that exists whatever the trend, so it must not be hidden behind a REVIEW.
    position_cap_breach = stock_weight > config.max_position_pct
    if not has_technical_data:
        # Without trustworthy live data the broker price never moves, so a
        # core invalidation breach cannot "confirm" over closes: ask for a
        # data check instead of sitting in REVIEW forever.
        if invalidation_escalated_to_sell:
            decision = "SELL"
        elif position_cap_breach:
            decision = "TRIM"
        elif data_status == "BAD DATA":
            decision = "VERIFY DATA"
        else:
            decision = "NO DATA"
    elif data_status == "NO THESIS":
        decision = "NO THESIS"
    elif invalidation_escalated_to_sell:
        decision = "SELL"
    elif position_cap_breach or trailing_stop_hit:
        decision = "TRIM"
    elif invalidation_is_review or dma_review_active:
        decision = "REVIEW"
    elif (
        (sector_risk_exposure > config.max_sector_pct and stock_weight >= (config.max_position_pct / 2))
        or (risk_group_exposure > config.max_risk_group_pct and stock_weight >= (config.max_position_pct / 2))
    ):
        decision = "TRIM"
    elif accumulate_qualified:
        if stock_weight == 0.0:
            decision = "BUY"
        else:
            decision = "ACCUMULATE"
    else:
        decision = "HOLD"

    # Recommended action derived via DECISION_ACTIONS
    recommended_action = DECISION_ACTIONS.get(decision, "Hold")
    if decision in ("ACCUMULATE", "BUY"):
        if not is_month_end:
            recommended_action = "ACCUMULATE (next monthly review)"
        else:
            recommended_action = "Accumulate" if decision == "ACCUMULATE" else "Buy"

    # 2. Horizon and Rationale Construction
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
        elif invalidation_is_review:
            horizon_long_term = f"UNVERIFIED — Broker price {fb_str} breached invalidation level {inv_str}"
            rationale = (
                f"invalidation breached on broker price ({fb_str} <= {inv_str}); live price unreliable "
                f"— verify before acting. {missing}."
            )
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

        if decision == "SELL":
            horizon_long_term = f"INVALIDATED — Price {cp_str} breached invalidation level {inv_str}"
            rationale = f"Thesis invalidated: Price {cp_str} <= invalidation price {inv_str}."
        elif decision == "REVIEW":
            if invalidation_is_review:
                horizon_long_term = f"REVIEW — Invalidation level {inv_str} breached ({consecutive_closes_below} of {config.invalidation_confirm_closes} closes)"
                rationale = f"invalidation breached, {consecutive_closes_below} of {config.invalidation_confirm_closes} closes"
            elif dma_review_active:
                horizon_long_term = f"REVIEW — 200-DMA breakdown hysteresis active ({sessions_below_200dma} sessions > 3% below 200-DMA)"
                rationale = f"200-DMA breakdown hysteresis review: price > 3% below 200-DMA for {sessions_below_200dma} sessions"
            else:
                horizon_long_term = "REVIEW — Thesis and technical review required"
                rationale = "Review required"
        elif decision == "TRIM":
            horizon_long_term = f"INTACT — High conviction ({conv_str}) thesis intact; risk limits require position/sector trimming"
            if position_cap_breach:
                rationale = f"Position cap breach: Weight {stock_weight:.1f}% exceeds max position limit ({config.max_position_pct:.1f}%); trim required."
                if invalidation_is_review:
                    rationale += f"; also under REVIEW: invalidation breached, {consecutive_closes_below} of {config.invalidation_confirm_closes} closes"
                elif dma_review_active:
                    rationale += "; also under REVIEW: 200-DMA breakdown"
            elif trailing_stop_hit:
                ts_str = f"₹{trailing_stop:.2f}" if trailing_stop is not None else "N/A"
                horizon_long_term = f"TRIM — Trailing stop hit ({ts_str}); profit protection"
                rationale = "trailing stop hit"
                if invalidation_is_review or dma_review_active:
                    rationale += "; also under REVIEW"
            elif sector_risk_exposure > config.max_sector_pct:
                rationale = f"Sector cap breach: {stock_sector} sector exposure ({sector_risk_exposure:.1f}%) exceeds sector limit ({config.max_sector_pct:.1f}%); trim holding ({stock_weight:.1f}% weight) for concentration risk control."
            elif risk_group_exposure > config.max_risk_group_pct:
                rationale = f"Risk group cap breach: Risk factor group exposure ({risk_group_exposure:.1f}%) exceeds limit ({config.max_risk_group_pct:.1f}%); trim holding ({stock_weight:.1f}% weight) for risk-factor control."
            else:
                rationale = f"Risk trim trigger: Position weight ({stock_weight:.1f}%) or sector risk ({sector_risk_exposure:.1f}%); trim for capital protection."
        elif decision in ("ACCUMULATE", "BUY"):
            horizon_long_term = f"INTACT — High conviction ({conv_str}) thesis intact; price {cp_str} above invalidation ({inv_str})"
            if is_month_end:
                rationale = f"Structural accumulation: Price {cp_str} > 50 DMA ({d50_str}) > 200 DMA ({d200_str}); weight {stock_weight:.1f}% < {config.max_position_pct:.1f}% max cap with conviction ({conv_str})."
            else:
                rationale = f"Accumulation channel intact; scheduled for next monthly review."
        else:  # HOLD
            if is_overextended:
                horizon_long_term = f"INTACT — High conviction ({conv_str}) thesis intact; overextension lock active"
                rationale = f"EXTENDED: don't add. Price {cp_str} > 50 DMA ({d50_str}) by >{(config.overextension_multiple - 1.0):.0%}."
            elif technical_trend == "BEARISH":
                horizon_long_term = f"INTACT — Conviction ({conv_str}) thesis intact above invalidation ({inv_str}); pullback monitored"
                rationale = f"Pullback hold: Price {cp_str} < 200 DMA ({d200_str}) with return {ret_str}; thesis remains INTACT above invalidation ({inv_str})."
            elif technical_trend == "NEUTRAL":
                horizon_long_term = f"INTACT — Thesis intact ({conv_str}); price {cp_str} above invalidation ({inv_str})"
                rationale = f"Consolidation hold: Price {cp_str} moving sideways between 50 DMA ({d50_str}) and 200 DMA ({d200_str}); conviction ({conv_str}) thesis INTACT above invalidation ({inv_str})."
            else:
                horizon_long_term = f"INTACT — Thesis intact ({conv_str}); price {cp_str} above invalidation ({inv_str})"
                rationale = f"Position hold: Technical trend {technical_trend}, total return {ret_str}, position weight {stock_weight:.1f}%; conviction ({conv_str}) thesis INTACT above invalidation ({inv_str})."

    if is_overextended:
        sizing_note = "EXTENDED: don't add"
    elif recommended_action == "ACCUMULATE (next monthly review)":
        conv_str = f"{int(conviction_val)}/5" if conviction_val is not None else "N/A"
        sizing_note = f"ACCUMULATE (next monthly review) — Conviction {conv_str} qualifies for monthly accumulation review."
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
        trailing_stop=trailing_stop,
        trailing_stop_hit=trailing_stop_hit,
        dma_review_active=dma_review_active,
    )


