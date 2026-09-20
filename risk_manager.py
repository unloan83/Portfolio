"""ATR sizing and portfolio-level vetoes for read-only portfolio analysis."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Mapping, Optional, Protocol

from config import RISK_CONFIG, RiskConfig


logger = logging.getLogger("portfolio.risk")


class HoldingLike(Protocol):
    asset_type: str
    market_value: float


class PortfolioLike(Protocol):
    holdings: Mapping[str, HoldingLike]

    @property
    def total_equity(self) -> float: ...

    def exposure_by_sector(self) -> dict[str, float]: ...


@dataclass(frozen=True)
class SizingResult:
    approved: bool
    quantity: int
    reason: str
    stop_price: Optional[float] = None
    target_price: Optional[float] = None


class RiskManager:
    def __init__(self, portfolio: PortfolioLike, config: RiskConfig = RISK_CONFIG):
        self.portfolio = portfolio
        self.config = config
        self.day_start_equity: Optional[float] = None

    def start_of_day(self) -> None:
        self.day_start_equity = self.portfolio.total_equity
        logger.info("Day start equity snapshot: %.2f", self.day_start_equity)

    def kill_switch_triggered(self) -> bool:
        if self.day_start_equity is None or self.day_start_equity <= 0:
            return False
        drop_pct = (
            (self.day_start_equity - self.portfolio.total_equity)
            / self.day_start_equity
            * 100
        )
        if drop_pct >= self.config.daily_loss_kill_switch_pct:
            logger.warning(
                "KILL SWITCH: portfolio down %.2f%% today (limit %.2f%%); blocking new entries",
                drop_pct,
                self.config.daily_loss_kill_switch_pct,
            )
            return True
        return False

    def size_position(
        self,
        symbol: str,
        entry_price: float,
        atr_value: float,
        sector: str = "unknown",
    ) -> SizingResult:
        if self.kill_switch_triggered():
            return SizingResult(False, 0, "Daily loss kill-switch active — no new entries today.")

        if (
            len(self.portfolio.holdings) >= self.config.max_open_positions
            and symbol not in self.portfolio.holdings
        ):
            return SizingResult(
                False,
                0,
                f"Max open positions ({self.config.max_open_positions}) reached.",
            )

        equity = self.portfolio.total_equity
        if equity <= 0 or entry_price <= 0 or atr_value <= 0:
            return SizingResult(False, 0, "Invalid equity/price/ATR inputs.")

        stop_distance = atr_value * self.config.atr_stop_multiple
        stop_price = entry_price - stop_distance
        target_price = entry_price + atr_value * self.config.atr_target_multiple
        risk_amount = equity * (self.config.risk_per_trade_pct / 100)
        qty_by_risk = risk_amount / stop_distance
        qty_by_position_cap = (
            equity * (self.config.max_position_pct / 100) / entry_price
        )

        sector_exposure = self.portfolio.exposure_by_sector().get(sector, 0.0)
        remaining_sector_room_pct = max(
            0.0, self.config.max_sector_pct - sector_exposure
        )
        qty_by_sector_cap = (
            equity * remaining_sector_room_pct / 100 / entry_price
        )
        quantity = int(min(qty_by_risk, qty_by_position_cap, qty_by_sector_cap))

        if quantity <= 0:
            return SizingResult(
                False,
                0,
                f"Sizing collapsed to 0 (risk_qty={qty_by_risk:.1f}, "
                f"position_cap_qty={qty_by_position_cap:.1f}, "
                f"sector_cap_qty={qty_by_sector_cap:.1f}). Sector '{sector}' "
                f"is likely near its {self.config.max_sector_pct}% cap.",
            )

        reward_risk = (target_price - entry_price) / stop_distance
        return SizingResult(
            True,
            quantity,
            f"Sized {quantity} @ ~{entry_price:.2f}; stop {stop_price:.2f}; "
            f"target {target_price:.2f}; R:R {reward_risk:.1f}:1; "
            f"risking {self.config.risk_per_trade_pct}% of equity.",
            stop_price=stop_price,
            target_price=target_price,
        )
