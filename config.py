"""Central configuration for portfolio analysis and risk controls.

Risk thresholds are environment-overridable so the report, sizing engine,
and tests all use the same values. No credentials or live-trading settings
belong in this read-only analysis repository.
"""
from dataclasses import dataclass
import os

from dotenv import load_dotenv


load_dotenv()


def _float(name: str, default: float) -> float:
    value = os.getenv(name)
    return float(value) if value else default


def _int(name: str, default: int) -> int:
    value = os.getenv(name)
    return int(value) if value else default


@dataclass(frozen=True)
class RiskConfig:
    """Single source of truth for portfolio-analysis risk thresholds."""

    risk_per_trade_pct: float = _float("RISK_PER_TRADE_PCT", 0.5)
    max_position_pct: float = _float("MAX_POSITION_PCT", 8.0)
    max_sector_pct: float = _float("MAX_SECTOR_PCT", 25.0)
    max_open_positions: int = _int("MAX_OPEN_POSITIONS", 15)
    daily_loss_kill_switch_pct: float = _float("DAILY_LOSS_KILL_SWITCH_PCT", 3.0)
    atr_stop_multiple: float = _float("ATR_STOP_MULTIPLE", 2.0)
    atr_target_multiple: float = _float("ATR_TARGET_MULTIPLE", 4.0)
    minimum_roe: float = _float("MINIMUM_ROE", 0.10)
    overextension_multiple: float = _float("OVEREXTENSION_MULTIPLE", 1.25)
    # Fraction of an overextended position to trim (no cap is breached, so
    # there is no natural target weight to trim down to).
    overextension_trim_fraction: float = _float("OVEREXTENSION_TRIM_FRACTION", 0.25)
    # Live (Yahoo) price vs broker price in portfolio.csv: a larger gap means
    # one of the two is wrong (bad ticker, unadjusted corporate action, stale
    # CSV), so the row is flagged instead of acted on.
    price_mismatch_pct: float = _float("PRICE_MISMATCH_PCT", 25.0)
    # Price / 200 DMA outside [1/x, x] cannot happen through normal trading and
    # indicates a broken price history.
    max_price_to_dma_ratio: float = _float("MAX_PRICE_TO_DMA_RATIO", 2.5)
    # Trailing stop distance from 52-week high in multiples of ATR (default 3x ATR).
    trailing_stop_atr_multiple: float = _float("TRAILING_STOP_ATR_MULTIPLE", 3.0)
    # Maximum risk factor group cap (default 25%)
    max_risk_group_pct: float = _float("MAX_RISK_GROUP_PCT", 25.0)
    # Core/Satellite structure targets
    target_core_pct: float = _float("TARGET_CORE_PCT", 50.0)
    target_satellite_count: int = _int("TARGET_SATELLITE_COUNT", 15)


RISK_CONFIG = RiskConfig()

# Predefined Risk Factor Groups mapping symbols to thematic/structural risk buckets
RISK_GROUPS: dict[str, list[str]] = {
    "Energy & Power": [
        "TATPOW", "NTPC", "NHPC", "SJVLIM", "NTPGRE", "JSWENE",
        "ONGC", "GAIL", "HINPET", "PETLNG", "RELIND", "GUJGA"
    ],
    "State-owned (PSU)": [
        "ONGC", "GAIL", "HINPET", "PETLNG", "NTPC", "NHPC",
        "SJVLIM", "NTPGRE", "LIC", "BHAELE", "ENGIND", "GUJGA"
    ],
    "Financials": [
        "FEDBAN", "HDFBAN", "KOTAKBKETF", "JIOFIN", "TATCAP", "LIC"
    ],
    "Precious metals": [
        "ICIGOL", "ICIPSE"
    ],
}


