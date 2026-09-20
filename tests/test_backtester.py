import numpy as np
import pandas as pd

from backtest.backtester import run_backtest
from backtest.run_dma_backtest import DmaCrossoverStrategy


def test_dma_backtest_reports_requested_metrics():
    index = pd.date_range("2024-01-01", periods=280, freq="B")
    close = np.concatenate(
        [np.linspace(100, 200, 230), np.linspace(200, 60, 50)]
    )
    frame = pd.DataFrame(
        {
            "open": close,
            "high": close + 1,
            "low": close - 1,
            "close": close,
            "volume": 1000,
        },
        index=index,
    )

    result = run_backtest(
        DmaCrossoverStrategy(), {"TEST.NS": frame}, slippage_bps=5
    )
    summary = result.summary()

    assert summary["trades"] == 1
    assert "win_rate_pct" in summary
    assert "expectancy_pct" in summary
    assert "max_drawdown_pct" in summary
