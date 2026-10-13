from datetime import datetime
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


def test_sector_map_etfs_and_financials():
    assert analysis.SECTOR_MAP["ICIGOL"] == "Commodities"
    assert analysis.SECTOR_MAP["ICIPSE"] == "Commodities"
    assert analysis.SECTOR_MAP["ICINIF"] == "Broad Market"
    assert analysis.SECTOR_MAP["HDF250"] == "Broad Market"
    assert analysis.SECTOR_MAP["MIR150"] == "Broad Market"
    assert analysis.SECTOR_MAP["NIPNIT"] == "IT"
    assert analysis.SECTOR_MAP["KOTAKBKETF"] == "Banking"
    assert "Banking" in analysis.FINANCIALS_SECTORS
    assert "Financial Services" in analysis.FINANCIALS_SECTORS
    assert "Insurance" in analysis.FINANCIALS_SECTORS


class MockPullbackTicker:
    """Ticker that rose to 250, then pulled back to 210 with ATR ~10."""

    def __init__(self, symbol: str):
        self.symbol = symbol
        self.info = {"returnOnEquity": 0.20}

    def history(self, period: str) -> pd.DataFrame:
        prices = list(np.linspace(100, 250, 230)) + list(np.linspace(250, 210, 20))
        close = pd.Series(prices)
        return pd.DataFrame({"Close": close, "High": close + 5, "Low": close - 5})


def test_trailing_stop_rule_trims_half_winner(tmp_path, monkeypatch):
    # WINNER holding: 80 shares @ cost 100, current price ~210, 52w high 255, ATR 10
    # Invalidation price 80.
    # 52w high - 3*ATR = 255 - 30 = 225.
    # Price 210 is below trailing stop 225, but well above invalidation 80.
    portfolio = pd.DataFrame(
        [
            {"Stock Symbol": "WINNER", "Company Name": "Winner Co", "Qty": 80, "Average Cost Price": 100, "Current Market Price": 210},
            {"Stock Symbol": "BASE", "Company Name": "Base Co", "Qty": 1000, "Average Cost Price": 100, "Current Market Price": 210},
        ]
    )
    portfolio.to_csv(tmp_path / "portfolio.csv", index=False)
    pd.DataFrame(
        [
            {"Stock Symbol": "WINNER", "Thesis": "Growth thesis", "Conviction": "4/5", "Invalidation_Price": 80, "Last_Updated": "2026-10-01"},
            {"Stock Symbol": "BASE", "Thesis": "Base thesis", "Conviction": "5/5", "Invalidation_Price": 50, "Last_Updated": "2026-10-01"},
        ]
    ).to_csv(tmp_path / "thesis.csv", index=False)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setitem(analysis.TICKER_MAP, "WINNER", "WINNER.NS")
    monkeypatch.setitem(analysis.TICKER_MAP, "BASE", "BASE.NS")
    monkeypatch.setitem(analysis.SECTOR_MAP, "WINNER", "Auto")
    monkeypatch.setitem(analysis.SECTOR_MAP, "BASE", "Defense")
    monkeypatch.setattr(analysis.yf, "Ticker", MockPullbackTicker)

    analysis.run_weekly_analysis(notify_fn=MagicMock())

    tracking = pd.read_csv(tmp_path / "re-engineering.csv").set_index("Stock_Symbol")
    winner_row = tracking.loc["WINNER"]
    assert winner_row["Decision"] == "TRIM"
    assert winner_row["Rationale"] == "trailing stop hit"
    # Sells half of 80 shares = 40 shares
    assert winner_row["Recommended_Action"].startswith("Trim 40 sh")

    readme = (tmp_path / "README.md").read_text()
    assert "| Trailing Stop" in readme
    assert "trailing stop hit" in readme


def test_thesis_invalidation_wins_over_trailing_stop():
    from config import RiskConfig
    from signal_engine import evaluate_signal

    # Invalidation price 100. 52w high 150, ATR 10 -> trailing stop = 120.
    # If price drops to 90 (below both 120 and 100), thesis invalidation wins (SELL, not TRIM).
    res = evaluate_signal(
        current_price=90.0,
        dma_50=120.0,
        dma_200=110.0,
        roe=0.15,
        invalidation_price=100.0,
        high_52w=150.0,
        atr=10.0,
        stock_weight=3.0,
        config=RiskConfig(),
    )
    assert res.decision == "SELL"
    assert res.thesis_status == "INVALIDATED"


def test_consolidation_section_in_report(tmp_path, monkeypatch):
    # Total portfolio equity = 100k.
    # CANDIDATE: Qty 5 @ 100 = 500 (0.5% weight < 1%), conviction 3 (< 5) -> Candidate!
    # HIGH_CONV: Qty 5 @ 100 = 500 (0.5% weight < 1%), conviction 5 (>= 5) -> NOT Candidate!
    # LARGE_POS: Qty 50 @ 100 = 5000 (5.0% weight > 1%), conviction 3 -> NOT Candidate!
    # REST: Qty 940 @ 100 = 94,000 (94% weight) -> NOT Candidate.
    portfolio = pd.DataFrame(
        [
            {"Stock Symbol": "CANDIDATE", "Company Name": "Small Low Conv", "Qty": 5, "Average Cost Price": 100, "Current Market Price": 100},
            {"Stock Symbol": "HIGH_CONV", "Company Name": "Small High Conv", "Qty": 5, "Average Cost Price": 100, "Current Market Price": 100},
            {"Stock Symbol": "LARGE_POS", "Company Name": "Large Low Conv", "Qty": 50, "Average Cost Price": 100, "Current Market Price": 100},
            {"Stock Symbol": "REST", "Company Name": "Rest", "Qty": 940, "Average Cost Price": 100, "Current Market Price": 100},
        ]
    )
    portfolio.to_csv(tmp_path / "portfolio.csv", index=False)
    pd.DataFrame(
        [
            {"Stock Symbol": "CANDIDATE", "Thesis": "Thesis", "Conviction": "3/5", "Invalidation_Price": 50, "Last_Updated": "2026-10-01"},
            {"Stock Symbol": "HIGH_CONV", "Thesis": "Thesis", "Conviction": "5/5", "Invalidation_Price": 50, "Last_Updated": "2026-10-01"},
            {"Stock Symbol": "LARGE_POS", "Thesis": "Thesis", "Conviction": "3/5", "Invalidation_Price": 50, "Last_Updated": "2026-10-01"},
            {"Stock Symbol": "REST", "Thesis": "Thesis", "Conviction": "4/5", "Invalidation_Price": 50, "Last_Updated": "2026-10-01"},
        ]
    ).to_csv(tmp_path / "thesis.csv", index=False)
    monkeypatch.chdir(tmp_path)
    for sym in ("CANDIDATE", "HIGH_CONV", "LARGE_POS", "REST"):
        monkeypatch.setitem(analysis.TICKER_MAP, sym, f"{sym}.NS")
        monkeypatch.setitem(analysis.SECTOR_MAP, sym, "TestSector")
    monkeypatch.setattr(analysis.yf, "Ticker", TrendTicker)

    analysis.run_weekly_analysis(notify_fn=MagicMock())

    readme = (tmp_path / "README.md").read_text()
    assert "### Portfolio Consolidation" in readme
    assert "CANDIDATE" in readme
    assert "Exit all 5 sh" in readme
    consolidation_section = readme.split("### Portfolio Consolidation")[1]
    assert "CANDIDATE" in consolidation_section
    assert "HIGH_CONV" not in consolidation_section
    assert "LARGE_POS" not in consolidation_section


def test_combined_financials_sector_cap(tmp_path, monkeypatch):
    # Banking (15%) + Financial Services (6%) + Insurance (5%) = 26% > 25% cap.
    portfolio = pd.DataFrame(
        [
            {"Stock Symbol": "BANK1", "Company Name": "Bank 1", "Qty": 150, "Average Cost Price": 100, "Current Market Price": 100},
            {"Stock Symbol": "FIN1", "Company Name": "Fin 1", "Qty": 60, "Average Cost Price": 100, "Current Market Price": 100},
            {"Stock Symbol": "INS1", "Company Name": "Ins 1", "Qty": 50, "Average Cost Price": 100, "Current Market Price": 100},
            {"Stock Symbol": "OTHER", "Company Name": "Other", "Qty": 740, "Average Cost Price": 100, "Current Market Price": 100},
        ]
    )
    portfolio.to_csv(tmp_path / "portfolio.csv", index=False)
    pd.DataFrame(
        [
            {"Stock Symbol": s, "Thesis": "Thesis", "Conviction": "4/5", "Invalidation_Price": 50, "Last_Updated": "2026-10-01"}
            for s in ("BANK1", "FIN1", "INS1", "OTHER")
        ]
    ).to_csv(tmp_path / "thesis.csv", index=False)
    monkeypatch.chdir(tmp_path)
    for s in ("BANK1", "FIN1", "INS1", "OTHER"):
        monkeypatch.setitem(analysis.TICKER_MAP, s, f"{s}.NS")
    monkeypatch.setitem(analysis.SECTOR_MAP, "BANK1", "Banking")
    monkeypatch.setitem(analysis.SECTOR_MAP, "FIN1", "Financial Services")
    monkeypatch.setitem(analysis.SECTOR_MAP, "INS1", "Insurance")
    monkeypatch.setitem(analysis.SECTOR_MAP, "OTHER", "Power")
    monkeypatch.setattr(analysis.yf, "Ticker", TrendTicker)

    analysis.run_weekly_analysis(notify_fn=MagicMock())

    readme = (tmp_path / "README.md").read_text()
    assert "* **Financials (combined)**:" in readme
    assert "* **Banking**:" in readme
    assert "* **Financial Services**:" in readme
    assert "* **Insurance**:" in readme


def test_xirr_math():
    import performance

    # 10% annual gain
    r1 = performance.xirr([-100.0, 110.0], ["2025-01-01", "2026-01-01"])
    assert r1 is not None
    assert abs(r1 - 0.10) < 0.001

    # -10% annual loss
    r2 = performance.xirr([-100.0, 90.0], ["2025-01-01", "2026-01-01"])
    assert r2 is not None
    assert abs(r2 - (-0.10)) < 0.001

    # Edge cases
    assert performance.xirr([-100.0, -50.0], ["2025-01-01", "2026-01-01"]) is None
    assert performance.xirr([100.0, 50.0], ["2025-01-01", "2026-01-01"]) is None
    assert performance.xirr([], []) is None


def test_performance_calculation_and_gaps():
    import performance

    trades = pd.DataFrame([
        {"Date": "2024-01-01", "Stock Symbol": "STOCK_A", "Action": "BUY", "Qty": 10, "Price": 100},
        {"Date": "2024-06-01", "Stock Symbol": "STOCK_A", "Action": "BUY", "Qty": 10, "Price": 120},
        {"Date": "2024-01-01", "Stock Symbol": "STOCK_B", "Action": "BUY", "Qty": 5, "Price": 200},
    ])
    portfolio = pd.DataFrame([
        {"Stock Symbol": "STOCK_A", "Qty": 20, "Current Market Price": 150},  # full (20/20)
        {"Stock Symbol": "STOCK_B", "Qty": 10, "Current Market Price": 220},  # partial (5/10)
        {"Stock Symbol": "STOCK_C", "Qty": 5, "Current Market Price": 50},    # missing completely
    ])
    bench_df = pd.DataFrame({
        "Close": [1000.0, 1100.0, 1200.0]
    }, index=pd.to_datetime(["2024-01-01", "2024-06-01", "2025-01-01"]))

    res = performance.calculate_portfolio_and_benchmark_xirr(
        trades_df=trades,
        portfolio_df=portfolio,
        current_prices={"STOCK_A": 150.0, "STOCK_B": 220.0, "STOCK_C": 50.0},
        benchmark_history=bench_df,
        valuation_date=datetime(2025, 1, 1),
    )

    assert res["portfolio_xirr"] is not None
    assert res["benchmark_xirr"] is not None
    assert res["missing_completely"] == ["STOCK_C"]
    assert len(res["partial_history"]) == 1
    assert res["partial_history"][0]["Stock Symbol"] == "STOCK_B"
    assert res["partial_history"][0]["Difference"] == 5.0

    md = performance.format_performance_markdown(res)
    assert "### Portfolio Performance vs Benchmark" in md
    assert "STOCK_C" in md
    assert "STOCK_B" in md
    assert "^NSEI" in md


def test_performance_section_in_readme(tmp_path, monkeypatch):
    trades = pd.DataFrame([
        {"Date": "2024-01-01", "Stock Symbol": "BASE", "Action": "BUY", "Qty": 100, "Price": 100},
    ])
    trades.to_csv(tmp_path / "trades.csv", index=False)
    portfolio = pd.DataFrame([
        {"Stock Symbol": "BASE", "Company Name": "Base Co", "Qty": 100, "Average Cost Price": 100, "Current Market Price": 120},
    ])
    portfolio.to_csv(tmp_path / "portfolio.csv", index=False)
    pd.DataFrame([
        {"Stock Symbol": "BASE", "Thesis": "Base thesis", "Conviction": "4/5", "Invalidation_Price": 50, "Last_Updated": "2026-10-01"}
    ]).to_csv(tmp_path / "thesis.csv", index=False)

    monkeypatch.chdir(tmp_path)
    monkeypatch.setitem(analysis.TICKER_MAP, "BASE", "BASE.NS")
    monkeypatch.setitem(analysis.SECTOR_MAP, "BASE", "Defense")
    monkeypatch.setattr(analysis.yf, "Ticker", TrendTicker)

    analysis.run_weekly_analysis(notify_fn=MagicMock())

    readme = (tmp_path / "README.md").read_text()
    assert "### Portfolio Performance vs Benchmark" in readme
    assert "### Asset Health Assessment" in readme
    # Ensure Performance section appears at the top (before Asset Health Assessment)
    perf_idx = readme.index("### Portfolio Performance vs Benchmark")
    health_idx = readme.index("### Asset Health Assessment")
    assert perf_idx < health_idx


def test_risk_groups_config():
    from config import RISK_CONFIG, RISK_GROUPS

    assert RISK_CONFIG.max_risk_group_pct == 25.0
    assert "Energy & Power" in RISK_GROUPS
    assert "State-owned (PSU)" in RISK_GROUPS
    assert "Financials" in RISK_GROUPS
    assert "Precious metals" in RISK_GROUPS

    psu_expected = [
        "ONGC", "GAIL", "HINPET", "PETLNG", "NTPC", "NHPC",
        "SJVLIM", "NTPGRE", "LIC", "BHAELE", "ENGIND", "GUJGA"
    ]
    for p in psu_expected:
        assert p in RISK_GROUPS["State-owned (PSU)"]

    assert "ICIGOL" in RISK_GROUPS["Precious metals"]
    assert "ICIPSE" in RISK_GROUPS["Precious metals"]


def test_risk_group_cap_triggers_trim():
    from config import RiskConfig
    from signal_engine import evaluate_signal

    # Stock has 4.5% weight (>= max_pos/2 = 4.0%), risk group exposure is 28% (> 25% cap)
    res = evaluate_signal(
        current_price=100.0,
        dma_50=95.0,
        dma_200=90.0,
        roe=0.15,
        invalidation_price=80.0,
        stock_weight=4.5,
        sector_risk_exposure=15.0,
        risk_group_exposure=28.0,
        config=RiskConfig(max_risk_group_pct=25.0),
    )
    assert res.decision == "TRIM"
    assert "Risk group cap breach" in res.rationale


def test_lookthrough_effective_weights():
    import lookthrough

    port = pd.DataFrame([
        {"Stock Symbol": "HDFBAN", "Weight_%": 15.0},
        {"Stock Symbol": "ICINIF", "Weight_%": 4.0},
        {"Stock Symbol": "KOTAKBKETF", "Weight_%": 2.0},
    ])
    mock_etf = {
        "etfs": {
            "ICINIF": {
                "top_10": [{"symbol": "HDFBAN", "weight_pct": 10.0}]  # 4.0% * 10% = 0.4%
            },
            "KOTAKBKETF": {
                "top_10": [{"symbol": "HDFBAN", "weight_pct": 25.0}]  # 2.0% * 25% = 0.5%
            }
        }
    }
    eff = lookthrough.calculate_effective_weights(port, mock_etf).set_index("Symbol")
    # HDFBAN effective weight = 15.0 + 0.4 + 0.5 = 15.9%
    assert abs(eff.loc["HDFBAN", "Effective_Weight"] - 15.9) < 0.01


def test_lookthrough_and_risk_groups_in_readme(tmp_path, monkeypatch):
    portfolio = pd.DataFrame([
        {"Stock Symbol": "ONGC", "Company Name": "ONGC", "Qty": 100, "Average Cost Price": 100, "Current Market Price": 100},
        {"Stock Symbol": "BASE", "Company Name": "Base", "Qty": 900, "Average Cost Price": 100, "Current Market Price": 100},
    ])
    portfolio.to_csv(tmp_path / "portfolio.csv", index=False)
    pd.DataFrame([
        {"Stock Symbol": s, "Thesis": "Thesis", "Conviction": "4/5", "Invalidation_Price": 50, "Last_Updated": "2026-10-01"}
        for s in ("ONGC", "BASE")
    ]).to_csv(tmp_path / "thesis.csv", index=False)

    monkeypatch.chdir(tmp_path)
    monkeypatch.setitem(analysis.TICKER_MAP, "ONGC", "ONGC.NS")
    monkeypatch.setitem(analysis.TICKER_MAP, "BASE", "BASE.NS")
    monkeypatch.setitem(analysis.SECTOR_MAP, "ONGC", "Oil & Gas")
    monkeypatch.setitem(analysis.SECTOR_MAP, "BASE", "Defense")
    monkeypatch.setattr(analysis.yf, "Ticker", TrendTicker)

    analysis.run_weekly_analysis(notify_fn=MagicMock())

    readme = (tmp_path / "README.md").read_text()
    assert "### Risk Factor Groups Concentration" in readme
    assert "### ETF Look-Through Effective Exposure" in readme



