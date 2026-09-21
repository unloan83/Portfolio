import os
import pandas as pd
import pytest

from signal_scorer import score_signals


def make_fake_history_loader(history_dict):
    def loader(symbol):
        return history_dict.get(symbol, pd.DataFrame())

    return loader


def test_row_old_enough_gets_scored_once(tmp_path):
    dates = pd.date_range(end="2026-09-01", periods=25, freq="B")
    signal_date = dates[0].strftime("%Y-%m-%d")

    tracking_df = pd.DataFrame(
        [
            {
                "Analysis_Date": signal_date,
                "Stock_Symbol": "TEST",
                "Price_At_Signal": 100.0,
                "Model_Signal": "🟢 ACCUMULATE",
                "Trigger_Reason": "Test signal",
                "run_timestamp_ist": f"{signal_date} 09:20:00 IST",
                "current_price": 100.0,
                "dma_50": 95.0,
                "dma_200": 90.0,
                "roe": 0.15,
                "portfolio_weight_pct": 5.0,
                "sector": "Testing",
                "technical_trend": "BULLISH",
            }
        ]
    )
    tracking_file = tmp_path / "re-engineering.csv"
    output_file = tmp_path / "reports" / "signal_scores.csv"
    tracking_df.to_csv(tracking_file, index=False)

    history_data = pd.DataFrame(
        {"Close": [100.0 + i * 2.0 for i in range(25)]}, index=dates
    )

    loader = make_fake_history_loader({"TEST": history_data})

    res_df = score_signals(
        tracking_file=str(tracking_file),
        output_file=str(output_file),
        ticker_history_loader=loader,
    )

    assert len(res_df) == 1
    row = res_df.iloc[0]
    assert row["symbol"] == "TEST"
    assert row["price_at_signal"] == 100.0
    assert row["price_5d_after"] == 110.0  # 100 + 5*2
    assert row["return_5d_pct"] == 10.0  # (110 - 100)/100 * 100
    assert row["price_10d_after"] == 120.0  # 100 + 10*2
    assert row["return_10d_pct"] == 20.0
    assert row["price_20d_after"] == 140.0  # 100 + 20*2
    assert row["return_20d_pct"] == 40.0


def test_row_too_recent_is_skipped(tmp_path):
    dates = pd.date_range(end="2026-09-21", periods=2, freq="B")
    signal_date = dates[-1].strftime("%Y-%m-%d")

    tracking_df = pd.DataFrame(
        [
            {
                "Analysis_Date": signal_date,
                "Stock_Symbol": "RECENT",
                "Price_At_Signal": 100.0,
                "Model_Signal": "🟢 ACCUMULATE",
                "Trigger_Reason": "Recent signal",
                "run_timestamp_ist": f"{signal_date} 09:20:00 IST",
                "current_price": 100.0,
                "dma_50": 95.0,
                "dma_200": 90.0,
                "roe": 0.15,
                "portfolio_weight_pct": 5.0,
                "sector": "Testing",
                "technical_trend": "BULLISH",
            }
        ]
    )
    tracking_file = tmp_path / "re-engineering.csv"
    output_file = tmp_path / "reports" / "signal_scores.csv"
    tracking_df.to_csv(tracking_file, index=False)

    history_data = pd.DataFrame({"Close": [100.0, 101.0]}, index=dates)
    loader = make_fake_history_loader({"RECENT": history_data})

    res_df = score_signals(
        tracking_file=str(tracking_file),
        output_file=str(output_file),
        ticker_history_loader=loader,
    )

    assert len(res_df) == 0


def test_row_already_scored_is_not_rescored(tmp_path):
    dates = pd.date_range(end="2026-09-01", periods=25, freq="B")
    signal_date = dates[0].strftime("%Y-%m-%d")

    tracking_df = pd.DataFrame(
        [
            {
                "Analysis_Date": signal_date,
                "Stock_Symbol": "SCORED",
                "Price_At_Signal": 100.0,
                "Model_Signal": "🟢 ACCUMULATE",
                "Trigger_Reason": "Scored signal",
                "run_timestamp_ist": f"{signal_date} 09:20:00 IST",
                "current_price": 100.0,
                "dma_50": 95.0,
                "dma_200": 90.0,
                "roe": 0.15,
                "portfolio_weight_pct": 5.0,
                "sector": "Testing",
                "technical_trend": "BULLISH",
            }
        ]
    )
    tracking_file = tmp_path / "re-engineering.csv"
    output_file = tmp_path / "reports" / "signal_scores.csv"
    os.makedirs(output_file.parent, exist_ok=True)
    tracking_df.to_csv(tracking_file, index=False)

    existing_df = pd.DataFrame(
        [
            {
                "symbol": "SCORED",
                "original_run_timestamp": f"{signal_date} 09:20:00 IST",
                "signal": "🟢 ACCUMULATE",
                "price_at_signal": 100.0,
                "price_5d_after": 105.0,
                "return_5d_pct": 5.0,
                "price_10d_after": 110.0,
                "return_10d_pct": 10.0,
                "price_20d_after": 120.0,
                "return_20d_pct": 20.0,
                "scored_at": "2026-09-01 10:00:00 IST",
            }
        ]
    )
    existing_df.to_csv(output_file, index=False)

    history_data = pd.DataFrame({"Close": [100.0 + i for i in range(25)]}, index=dates)
    loader = make_fake_history_loader({"SCORED": history_data})

    res_df = score_signals(
        tracking_file=str(tracking_file),
        output_file=str(output_file),
        ticker_history_loader=loader,
    )

    assert len(res_df) == 1
    assert res_df.iloc[0]["scored_at"] == "2026-09-01 10:00:00 IST"


def test_no_data_row_is_never_scored(tmp_path):
    dates = pd.date_range(end="2026-09-01", periods=25, freq="B")
    signal_date = dates[0].strftime("%Y-%m-%d")

    tracking_df = pd.DataFrame(
        [
            {
                "Analysis_Date": signal_date,
                "Stock_Symbol": "NODATA_STOCK",
                "Price_At_Signal": None,
                "Model_Signal": "⚪ NO DATA",
                "Trigger_Reason": "Could not evaluate",
                "run_timestamp_ist": f"{signal_date} 09:20:00 IST",
                "current_price": None,
                "dma_50": None,
                "dma_200": None,
                "roe": None,
                "portfolio_weight_pct": 2.0,
                "sector": "Testing",
                "technical_trend": "NO_DATA",
            },
            {
                "Analysis_Date": signal_date,
                "Stock_Symbol": "ERR_STOCK",
                "Price_At_Signal": None,
                "Model_Signal": "⚪ NO DATA",
                "Trigger_Reason": "Could not evaluate",
                "run_timestamp_ist": f"{signal_date} 09:20:00 IST",
                "current_price": None,
                "dma_50": None,
                "dma_200": None,
                "roe": None,
                "portfolio_weight_pct": 2.0,
                "sector": "Testing",
                "technical_trend": "FETCH_ERROR",
            },
        ]
    )
    tracking_file = tmp_path / "re-engineering.csv"
    output_file = tmp_path / "reports" / "signal_scores.csv"
    tracking_df.to_csv(tracking_file, index=False)

    history_data = pd.DataFrame({"Close": [100.0 + i for i in range(25)]}, index=dates)
    loader = make_fake_history_loader(
        {
            "NODATA_STOCK": history_data,
            "ERR_STOCK": history_data,
        }
    )

    res_df = score_signals(
        tracking_file=str(tracking_file),
        output_file=str(output_file),
        ticker_history_loader=loader,
    )

    assert len(res_df) == 0
