"""Unit tests for refresh_portfolio module."""
import pandas as pd
import pytest
from refresh_portfolio import (
    PARTIAL_HISTORY_SYMBOLS,
    calculate_trades_positions,
    refresh_portfolio,
    refresh_row,
)


def test_calculate_trades_positions():
    trades = pd.DataFrame([
        {"Date": "2024-01-01", "Stock Symbol": "TEST", "Action": "BUY", "Qty": 10, "Price": 100.0},
        {"Date": "2024-01-02", "Stock Symbol": "TEST", "Action": "BUY", "Qty": 10, "Price": 200.0},
        {"Date": "2024-01-03", "Stock Symbol": "TEST", "Action": "SELL", "Qty": 5, "Price": 250.0},
    ])
    
    positions = calculate_trades_positions(trades)
    assert "TEST" in positions
    assert positions["TEST"]["qty"] == 15.0
    assert abs(positions["TEST"]["avg_cost"] - 150.0) < 0.01


def test_partial_history_symbols_never_overwritten():
    """
    These 11 symbols have known-incomplete trades.csv history
    (missing pre-April-2021 trades / IPO-demerger allotments).
    They must be skipped by refresh logic regardless of what
    calc_qty comes out to — even if a future trade addition makes
    calc_qty >= existing_qty by coincidence.
    """
    for symbol in PARTIAL_HISTORY_SYMBOLS:
        original_qty = 999          # arbitrary "existing" value
        original_avg_cost = 123.45
        row = {
            "Stock Symbol": symbol,
            "Qty": original_qty,
            "Average Cost Price": original_avg_cost,
            "Current Market Price": 150.0,
        }
        # simulate calc_qty deliberately >= existing to try to trigger old bug
        result = refresh_row(row.copy(), calc_qty=original_qty + 500, calc_avg_cost=1.0)

        assert result["Qty"] == original_qty
        assert result["Average Cost Price"] == original_avg_cost


def test_refresh_portfolio_overwrite_stale_snapshot(tmp_path):
    port_file = tmp_path / "portfolio.csv"
    trades_file = tmp_path / "trades.csv"

    port_df = pd.DataFrame([
        {
            "Stock Symbol": "ETF_TEST",
            "Company Name": "Test ETF",
            "ISIN Code": "INE000A01010",
            "Qty": 10,
            "Average Cost Price": 100.0,
            "Current Market Price": 200.0,
            "% Change over prev close": "0.0",
            "Value At Cost": 1000.0,
            "Value At Market Price": 2000.0,
            "Realized Profit / Loss": 0.0,
            "Unrealized Profit/Loss": 1000.0,
            "Unrealized Profit/Loss %": "100.00",
        }
    ])
    port_df.to_csv(port_file, index=False)

    trades_df = pd.DataFrame([
        {"Date": "2024-01-01", "Stock Symbol": "ETF_TEST", "Action": "BUY", "Qty": 25, "Price": 150.0},
    ])
    trades_df.to_csv(trades_file, index=False)

    refreshed = refresh_portfolio(str(trades_file), str(port_file))
    
    assert refreshed.iloc[0]["Qty"] == 25
    assert refreshed.iloc[0]["Average Cost Price"] == 150.0
    assert refreshed.iloc[0]["Value At Cost"] == 3750.0


def test_unclassified_symbol_raises_error(tmp_path):
    port_file = tmp_path / "portfolio.csv"
    trades_file = tmp_path / "trades.csv"

    port_df = pd.DataFrame([
        {
            "Stock Symbol": "KNOWN",
            "Qty": 10,
            "Average Cost Price": 100.0,
            "Current Market Price": 200.0,
        }
    ])
    port_df.to_csv(port_file, index=False)

    trades_df = pd.DataFrame([
        {"Date": "2024-01-01", "Stock Symbol": "UNKNOWN_34TH", "Action": "BUY", "Qty": 10, "Price": 50.0},
    ])
    trades_df.to_csv(trades_file, index=False)

    with pytest.raises(ValueError, match="Unclassified symbol"):
        refresh_portfolio(str(trades_file), str(port_file))
