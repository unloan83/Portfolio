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
                "Current Market Price": 310,
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

    # Verify all 21 columns are in exact expected schema
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
        "Decision",
        "Horizon_Short_Term",
        "Horizon_Long_Term",
        "Rationale",
        "Data_Status",
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
                "Current Market Price": 310,
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




def test_gujarat_gas_ticker():
    # GUJGASLTD is delisted (404); official post-merger ticker is GUJENERGY.NS
    assert analysis.TICKER_MAP["GUJGA"] == "GUJENERGY.NS"


def test_icinif_ticker_mapping():
    # NIFTYIETF.NS has <200 bars; 537007.BO provides full 1y history
    assert analysis.TICKER_MAP["ICINIF"] == "537007.BO"


def test_adjust_unadjusted_splits_rescales_history():
    close = pd.Series([500.0] * 150 + [50.0] * 100)  # 1:10 split not adjusted
    frame = pd.DataFrame({"Close": close, "High": close * 1.01, "Low": close * 0.99})
    adjusted = analysis.adjust_unadjusted_splits(frame)
    assert np.allclose(adjusted["Close"], 50.0)
    assert np.isclose(adjusted["High"].iloc[0], 50.5)
    # Ordinary moves are left alone.
    normal = pd.DataFrame({"Close": pd.Series([100.0, 110.0, 95.0])})
    assert analysis.adjust_unadjusted_splits(normal).equals(normal)


def test_price_data_issue_checks():
    assert analysis.price_data_issue(237.58, 334.18, 401.15) is not None  # wrong ticker
    assert analysis.price_data_issue(56.78, 203.97, 58.65) is not None  # broken history
    assert analysis.price_data_issue(395.2, 420.0, 411.35) is None
    assert analysis.price_data_issue(None, None, 100.0) is None


class TrendTicker:
    """Steady uptrend with High/Low so ATR is available."""

    def __init__(self, symbol: str):
        self.symbol = symbol
        self.info = {"returnOnEquity": 0.20}

    def history(self, period: str) -> pd.DataFrame:
        close = pd.Series(np.linspace(100, 200, 250))
        return pd.DataFrame({"Close": close, "High": close + 2, "Low": close - 2})


def test_report_gives_sized_actions(tmp_path, monkeypatch):
    portfolio = pd.DataFrame(
        [
            {"Stock Symbol": "BIG", "Company Name": "Big", "Qty": 300, "Average Cost Price": 150, "Current Market Price": 200},
            {"Stock Symbol": "SMALL", "Company Name": "Small", "Qty": 10, "Average Cost Price": 150, "Current Market Price": 200},
            {"Stock Symbol": "REST", "Company Name": "Rest", "Qty": 1000, "Average Cost Price": 150, "Current Market Price": 200},
        ]
    )
    portfolio.to_csv(tmp_path / "portfolio.csv", index=False)
    pd.DataFrame(
        [
            {"Stock Symbol": s, "Thesis": "Thesis", "Conviction": "4/5", "Invalidation_Price": 50, "Last_Updated": "2026-10-01"}
            for s in ("BIG", "SMALL", "REST")
        ]
    ).to_csv(tmp_path / "thesis.csv", index=False)
    monkeypatch.chdir(tmp_path)
    for i, sym in enumerate(("BIG", "SMALL", "REST")):
        monkeypatch.setitem(analysis.TICKER_MAP, sym, f"{sym}.NS")
        monkeypatch.setitem(analysis.SECTOR_MAP, sym, f"Sector{i}")
    monkeypatch.setattr(analysis.yf, "Ticker", TrendTicker)

    analysis.run_weekly_analysis(notify_fn=MagicMock())

    tracking = pd.read_csv(tmp_path / "re-engineering.csv").set_index("Stock_Symbol")
    # BIG = 300 of 1310 shares = 22.9% > 8% cap -> trim 196 sh, just under the 8% cap.
    assert tracking.loc["BIG", "Decision"] == "TRIM"
    assert tracking.loc["BIG", "Recommended_Action"].startswith("Trim 196 sh")
    assert "7.9% weight" in tracking.loc["BIG", "Recommended_Action"]
    # SMALL is a bullish 0.8% holding -> ATR-sized buy with stop and target.
    assert tracking.loc["SMALL", "Decision"] == "ACCUMULATE"
    assert "buy" in tracking.loc["SMALL", "Recommended_Action"]
    assert "stop ₹" in tracking.loc["SMALL", "Recommended_Action"]

    readme = (tmp_path / "README.md").read_text()
    assert "| Action" in readme
    assert "STRG SELL" not in readme and "| Signal" not in readme
    # Sorted by numeric weight, largest first.
    assert readme.index("| REST") < readme.index("| BIG") < readme.index("| SMALL")
