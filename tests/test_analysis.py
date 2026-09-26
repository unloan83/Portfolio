from unittest.mock import MagicMock

import numpy as np
import pandas as pd

import analysis



class FakeTicker:
    def __init__(self, symbol: str):
        self.symbol = symbol
        if self.symbol == "ERR.NS":
            raise RuntimeError("API Timeout")
        self.info = {"returnOnEquity": 0.20}

    def history(self, period: str) -> pd.DataFrame:
        if self.symbol == "EMPTY.NS":
            return pd.DataFrame()
        close = pd.Series(range(100, 320), dtype=float)
        return pd.DataFrame({"Close": close})


def test_verified_corporate_action_ticker_mappings():
    assert analysis.TICKER_MAP["TATCAP"] == "TATACAP.NS"
    assert analysis.TICKER_MAP["LGELEC"] == "LGEINDIA.NS"
    assert analysis.TICKER_MAP["SEQSCI"] == "VIYASH.NS"
    assert analysis.TICKER_MAP["NIPNIT"] == "ITBEES.NS"


def test_no_data_and_sector_cap_are_explicit(tmp_path, monkeypatch):
    portfolio = pd.DataFrame(
        [
            {
                "Stock Symbol": "BULL",
                "Company Name": "Bullish Holding",
                "Qty": 10,
                "Average Cost Price": 100,
                "Current Market Price": 200,
            },
            {
                "Stock Symbol": "EMPTY",
                "Company Name": "Missing History",
                "Qty": 1,
                "Average Cost Price": 100,
                "Current Market Price": 100,
            },
            {
                "Stock Symbol": "ERRSTOCK",
                "Company Name": "Fetch Error Stock",
                "Qty": 1,
                "Average Cost Price": 100,
                "Current Market Price": 100,
            },
            {
                "Stock Symbol": "UNLIST",
                "Company Name": "Unlisted Ticker Stock",
                "Qty": 1,
                "Average Cost Price": 100,
                "Current Market Price": 100,
            },
        ]
    )
    portfolio.to_csv(tmp_path / "portfolio.csv", index=False)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setitem(analysis.TICKER_MAP, "BULL", "BULL.NS")
    monkeypatch.setitem(analysis.TICKER_MAP, "EMPTY", "EMPTY.NS")
    monkeypatch.setitem(analysis.TICKER_MAP, "ERRSTOCK", "ERR.NS")
    monkeypatch.setitem(analysis.TICKER_MAP, "UNLIST", "UNLISTED")
    monkeypatch.setitem(analysis.SECTOR_MAP, "BULL", "Test Sector")
    monkeypatch.setattr(analysis.yf, "Ticker", FakeTicker)

    mock_notifier = MagicMock()
    analysis.run_weekly_analysis(notify_fn=mock_notifier)

    mock_notifier.assert_called_once()
    sent_msg = mock_notifier.call_args[0][0]
    assert "BULL" in sent_msg
    assert "EMPTY" in sent_msg
    assert "ERRSTOCK" in sent_msg
    assert "UNLIST" in sent_msg

    tracking = pd.read_csv(tmp_path / "re-engineering.csv")

    # 1. Verify existing columns are unchanged in position/name (first 5 columns)
    expected_original_cols = [
        "Analysis_Date",
        "Stock_Symbol",
        "Price_At_Signal",
        "Model_Signal",
        "Trigger_Reason",
    ]
    assert list(tracking.columns[:5]) == expected_original_cols

    # Verify all 16 columns are in exact expected schema
    expected_full_cols = expected_original_cols + [
        "run_timestamp_ist",
        "current_price",
        "dma_50",
        "dma_200",
        "roe",
        "portfolio_weight_pct",
        "sector",
        "technical_trend",
        "Recommended_Action",
        "Thesis_Status",
        "Conviction",
    ]
    assert list(tracking.columns) == expected_full_cols

    # 2. Verify successful signal writes all new columns populated
    bull_row = tracking[tracking["Stock_Symbol"] == "BULL"].iloc[0]
    assert bull_row["Model_Signal"] == "⚠️ NO THESIS"
    assert "IST" in str(bull_row["run_timestamp_ist"])
    assert float(bull_row["current_price"]) == 319.0
    assert pd.notna(bull_row["dma_50"])
    assert pd.notna(bull_row["dma_200"])
    assert float(bull_row["roe"]) == 0.20
    assert float(bull_row["portfolio_weight_pct"]) > 0
    assert bull_row["sector"] == "Test Sector"
    assert bull_row["technical_trend"] == "BULLISH"

    # 3. Verify failed fetches write rows with nulls + failure state rather than being skipped
    assert len(tracking) == 4

    empty_row = tracking[tracking["Stock_Symbol"] == "EMPTY"].iloc[0]
    assert empty_row["Model_Signal"] == "⚪ NO DATA"
    assert empty_row["technical_trend"] == "NO_DATA"
    assert pd.isna(empty_row["current_price"])
    assert pd.isna(empty_row["Price_At_Signal"])
    assert pd.isna(empty_row["dma_50"])
    assert pd.isna(empty_row["dma_200"])
    assert pd.isna(empty_row["roe"])
    assert pd.notna(empty_row["portfolio_weight_pct"])

    err_row = tracking[tracking["Stock_Symbol"] == "ERRSTOCK"].iloc[0]
    assert err_row["Model_Signal"] == "⚪ NO DATA"
    assert err_row["technical_trend"] == "FETCH_ERROR"
    assert pd.isna(err_row["current_price"])

    unlist_row = tracking[tracking["Stock_Symbol"] == "UNLIST"].iloc[0]
    assert unlist_row["Model_Signal"] == "⚪ NO DATA"
    assert unlist_row["technical_trend"] == "NO_TICKER"
    assert pd.isna(unlist_row["current_price"])


def test_consecutive_run_suppresses_telegram_notification(tmp_path, monkeypatch):
    portfolio = pd.DataFrame(
        [
            {
                "Stock Symbol": "BULL",
                "Company Name": "Bullish Holding",
                "Qty": 10,
                "Average Cost Price": 100,
                "Current Market Price": 200,
            }
        ]
    )
    portfolio.to_csv(tmp_path / "portfolio.csv", index=False)
    thesis = pd.DataFrame(
        [
            {
                "Stock Symbol": "BULL",
                "Thesis": "Growth thesis intact",
                "Conviction": 5,
                "Invalidation_Price": 50,
                "Last_Updated": "2026-09-25",
            }
        ]
    )
    thesis.to_csv(tmp_path / "thesis.csv", index=False)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setitem(analysis.TICKER_MAP, "BULL", "BULL.NS")
    monkeypatch.setitem(analysis.SECTOR_MAP, "BULL", "Test Sector")
    monkeypatch.setattr(analysis.yf, "Ticker", FakeTicker)

    # First run should send notification
    mock_notifier1 = MagicMock()
    analysis.run_weekly_analysis(notify_fn=mock_notifier1)
    mock_notifier1.assert_called_once()

    # Second run without changes in incremental mode should suppress notification
    mock_notifier2 = MagicMock()
    analysis.run_weekly_analysis(notify_fn=mock_notifier2)
    mock_notifier2.assert_not_called()


