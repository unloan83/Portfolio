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


RISK_CONFIG = RiskConfig()
