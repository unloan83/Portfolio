"""Unit tests for ingest_trades script."""
import pandas as pd
import pytest
from ingest_trades import load_upstox_exports, reconcile


def test_load_upstox_exports(tmp_path):
    export_csv = tmp_path / "tradebook_FY24.csv"
    df = pd.DataFrame(
        [
            {
                "Trade Date": "2024-05-10",
                "Symbol": "BHAELE",
                "Trade Type": "buy",
                "Quantity": 80,
                "Price": 157.83,
            }
        ]
    )
    df.to_csv(export_csv, index=False)

    loaded = load_upstox_exports([str(export_csv)])
    assert len(loaded) == 1
    assert loaded.iloc[0]["Stock Symbol"] == "BHAELE"
    assert loaded.iloc[0]["Action"] == "BUY"
    assert loaded.iloc[0]["Date"] == "2024-05-10"


def test_reconcile_match_and_mismatch(tmp_path):
    portfolio_csv = tmp_path / "portfolio.csv"
    port_df = pd.DataFrame(
        [
            {"Stock Symbol": "MATCH", "Qty": 50},
            {"Stock Symbol": "MISMATCH", "Qty": 100},
            {"Stock Symbol": "MISSING", "Qty": 10},
        ]
    )
    port_df.to_csv(portfolio_csv, index=False)

    trades = pd.DataFrame(
        [
            {"Date": "2024-01-01", "Stock Symbol": "MATCH", "Action": "BUY", "Qty": 50, "Price": 100, "Notes": "import"},
            {"Date": "2024-01-01", "Stock Symbol": "MISMATCH", "Action": "BUY", "Qty": 80, "Price": 100, "Notes": "import"},
        ]
    )

    trades_out, report = reconcile(trades, str(portfolio_csv))
    
    match_status = report[report["Stock Symbol"] == "MATCH"].iloc[0]["Status"]
    assert match_status == "OK"

    mismatch_status = report[report["Stock Symbol"] == "MISMATCH"].iloc[0]["Status"]
    assert mismatch_status in ("MISMATCH", "PARTIAL HISTORY")

    missing_status = report[report["Stock Symbol"] == "MISSING"].iloc[0]["Status"]
    assert missing_status in ("NO TRADE HISTORY FOUND", "PARTIAL HISTORY")
