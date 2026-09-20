"""Small walk-forward backtester with next-bar fills and bounded friction."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class Signal:
    symbol: str
    action: str
    reason: str = ""


class Strategy(Protocol):
    def generate_signals(
        self,
        price_data: dict[str, pd.DataFrame],
        held_symbols: set[str],
    ) -> list[Signal]: ...


@dataclass
class Trade:
    symbol: str
    entry_date: pd.Timestamp
    entry_price: float
    exit_date: pd.Timestamp | None = None
    exit_price: float | None = None
    quantity: float = 1.0
    reason_in: str = ""
    reason_out: str = ""

    @property
    def pnl(self) -> float | None:
        if self.exit_price is None:
            return None
        return (self.exit_price - self.entry_price) * self.quantity

    @property
    def pnl_pct(self) -> float | None:
        if self.exit_price is None:
            return None
        return (self.exit_price / self.entry_price - 1) * 100


@dataclass
class BacktestResult:
    trades: list[Trade] = field(default_factory=list)

    def closed_trades(self) -> list[Trade]:
        return [trade for trade in self.trades if trade.exit_price is not None]

    def summary(self) -> dict[str, float | int]:
        closed = self.closed_trades()
        if not closed:
            return {
                "trades": 0,
                "win_rate_pct": 0.0,
                "expectancy_pct": 0.0,
                "max_drawdown_pct": 0.0,
            }

        pnls = [trade.pnl_pct for trade in closed]
        wins = [pnl for pnl in pnls if pnl > 0]
        losses = [pnl for pnl in pnls if pnl <= 0]
        equity_curve = np.cumprod([1 + pnl / 100 for pnl in pnls])
        running_max = np.maximum.accumulate(np.insert(equity_curve, 0, 1.0))[1:]
        drawdown = (equity_curve - running_max) / running_max
        return {
            "trades": len(closed),
            "win_rate_pct": round(100 * len(wins) / len(closed), 1),
            "avg_win_pct": round(float(np.mean(wins)), 2) if wins else 0.0,
            "avg_loss_pct": round(float(np.mean(losses)), 2) if losses else 0.0,
            "payoff_ratio": (
                round(abs(float(np.mean(wins) / np.mean(losses))), 2)
                if wins and losses and np.mean(losses) != 0
                else float("nan")
            ),
            "expectancy_pct": round(float(np.mean(pnls)), 2),
            "max_drawdown_pct": (
                round(float(drawdown.min()) * 100, 2) if len(drawdown) else 0.0
            ),
            "total_return_pct": round((float(equity_curve[-1]) - 1) * 100, 2),
        }


def run_backtest(
    strategy: Strategy,
    price_data: dict[str, pd.DataFrame],
    slippage_bps: float = 5.0,
) -> BacktestResult:
    """Run signals on bar close and fill them at the next bar's open."""
    if not price_data:
        return BacktestResult()
    if slippage_bps < 0:
        raise ValueError("slippage_bps must be non-negative")

    common_index: pd.Index | None = None
    for frame in price_data.values():
        common_index = (
            frame.index
            if common_index is None
            else common_index.intersection(frame.index)
        )
    if common_index is None or len(common_index) < 202:
        return BacktestResult()
    common_index = common_index.sort_values()

    result = BacktestResult()
    open_trades: dict[str, Trade] = {}
    for index_position in range(199, len(common_index) - 1):
        date = common_index[index_position]
        next_date = common_index[index_position + 1]
        window_data = {
            symbol: frame.loc[:date]
            for symbol, frame in price_data.items()
            if date in frame.index
        }
        signals = strategy.generate_signals(
            window_data, held_symbols=set(open_trades)
        )

        for signal in signals:
            frame = price_data[signal.symbol]
            if next_date not in frame.index:
                continue
            fill_price = float(frame.loc[next_date, "open"])
            slippage = fill_price * slippage_bps / 10_000
            if signal.action == "enter_long" and signal.symbol not in open_trades:
                open_trades[signal.symbol] = Trade(
                    symbol=signal.symbol,
                    entry_date=next_date,
                    entry_price=fill_price + slippage,
                    reason_in=signal.reason,
                )
            elif signal.action == "exit_long" and signal.symbol in open_trades:
                trade = open_trades.pop(signal.symbol)
                trade.exit_date = next_date
                trade.exit_price = fill_price - slippage
                trade.reason_out = signal.reason
                result.trades.append(trade)

    last_date = common_index[-1]
    for symbol, trade in open_trades.items():
        final_close = float(price_data[symbol].loc[last_date, "close"])
        trade.exit_date = last_date
        trade.exit_price = final_close * (1 - slippage_bps / 10_000)
        trade.reason_out = "backtest_end_force_close"
        result.trades.append(trade)
    return result
