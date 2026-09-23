"""Run the report's 50/200-DMA state rule over three years per symbol."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from analysis import SECTOR_MAP, TICKER_MAP  # noqa: E402
from backtest.backtester import Signal, run_backtest  # noqa: E402
from backtest.yfinance_adapter import fetch_history  # noqa: E402
from signal_engine import evaluate_signal  # noqa: E402


class DmaCrossoverStrategy:
    """Match the weekly report's bullish-entry and bearish-exit states."""

    def generate_signals(
        self,
        price_data: dict[str, pd.DataFrame],
        held_symbols: set[str],
    ) -> list[Signal]:
        signals: list[Signal] = []
        for symbol, frame in price_data.items():
            if len(frame) < 200:
                continue
            close = frame["close"]
            current_price = float(close.iloc[-1])
            dma_50 = float(close.rolling(50).mean().iloc[-1])
            dma_200 = float(close.rolling(200).mean().iloc[-1])
            stock_sector = SECTOR_MAP.get(symbol, "Other ETFs/Misc")
            eval_res = evaluate_signal(
                current_price=current_price,
                dma_50=dma_50,
                dma_200=dma_200,
                roe=None,
                stock_sector=stock_sector,
            )
            if eval_res.technical_trend == "BEARISH" and symbol in held_symbols:
                signals.append(
                    Signal(symbol, "exit_long", eval_res.explanation)
                )
            elif (
                eval_res.technical_trend == "BULLISH"
                and not eval_res.is_overextended
                and eval_res.fundamental_pass
                and symbol not in held_symbols
            ):
                signals.append(
                    Signal(symbol, "enter_long", eval_res.explanation)
                )
        return signals




def _portfolio_symbols(portfolio_path: Path) -> list[str]:
    portfolio = pd.read_csv(portfolio_path)
    portfolio.columns = portfolio.columns.str.strip()
    return portfolio["Stock Symbol"].astype(str).str.strip().drop_duplicates().tolist()


def run(symbols: list[str], period: str, slippage_bps: float) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for broker_symbol in symbols:
        yahoo_symbol = TICKER_MAP.get(broker_symbol, f"{broker_symbol}.NS")
        if yahoo_symbol in {"UNLISTED", "TODO_VERIFY"}:
            print(
                f"[warn] {broker_symbol} ({yahoo_symbol}) ValueError: "
                "ticker is not verified",
                file=sys.stderr,
            )
            continue
        try:
            history = fetch_history(yahoo_symbol, period=period)
            result = run_backtest(
                DmaCrossoverStrategy(),
                {yahoo_symbol: history},
                slippage_bps=slippage_bps,
            )
            summary = result.summary()
        except Exception as exc:
            print(
                f"[warn] {broker_symbol} ({yahoo_symbol}) "
                f"{type(exc).__name__}: {exc}",
                file=sys.stderr,
            )
            continue
        rows.append(
            {
                "Symbol": broker_symbol,
                "Yahoo Ticker": yahoo_symbol,
                "Trades": summary["trades"],
                "Win Rate %": summary["win_rate_pct"],
                "Expectancy %": summary["expectancy_pct"],
                "Max Drawdown %": summary["max_drawdown_pct"],
            }
        )
    return pd.DataFrame(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--period", default="3y")
    parser.add_argument("--slippage-bps", type=float, default=5.0)
    parser.add_argument(
        "--symbols",
        help="Comma-separated broker symbols; defaults to portfolio.csv",
    )
    arguments = parser.parse_args()
    symbols = (
        [symbol.strip() for symbol in arguments.symbols.split(",") if symbol.strip()]
        if arguments.symbols
        else _portfolio_symbols(REPOSITORY_ROOT / "portfolio.csv")
    )
    report = run(symbols, arguments.period, arguments.slippage_bps)
    if report.empty:
        print("No backtest results were produced.", file=sys.stderr)
        return 1
    print(report.to_markdown(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
