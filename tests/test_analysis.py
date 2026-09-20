import pandas as pd

import analysis


class FakeTicker:
    def __init__(self, symbol: str):
        self.symbol = symbol
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
        ]
    )
    portfolio.to_csv(tmp_path / "portfolio.csv", index=False)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setitem(analysis.TICKER_MAP, "BULL", "BULL.NS")
    monkeypatch.setitem(analysis.TICKER_MAP, "EMPTY", "EMPTY.NS")
    monkeypatch.setitem(analysis.SECTOR_MAP, "BULL", "Test Sector")
    monkeypatch.setattr(analysis.yf, "Ticker", FakeTicker)

    analysis.run_weekly_analysis()

    tracking = pd.read_csv(tmp_path / "re-engineering.csv")
    signals = dict(zip(tracking["Stock_Symbol"], tracking["Model_Signal"]))
    assert signals["BULL"] == "⚠️ SECTOR CAP"
    assert signals["EMPTY"] == "⚪ NO DATA"
