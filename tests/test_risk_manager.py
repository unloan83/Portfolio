from dataclasses import dataclass, field

from risk_manager import RiskManager


@dataclass
class Holding:
    symbol: str
    quantity: float
    price: float
    sector: str
    asset_type: str = "equity"

    @property
    def market_value(self) -> float:
        return self.quantity * self.price


@dataclass
class Portfolio:
    cash: float
    holdings: dict[str, Holding] = field(default_factory=dict)

    @property
    def total_equity(self) -> float:
        return self.cash + sum(holding.market_value for holding in self.holdings.values())

    def exposure_by_sector(self) -> dict[str, float]:
        return {
            sector: sum(
                holding.market_value
                for holding in self.holdings.values()
                if holding.sector == sector
            )
            / self.total_equity
            * 100
            for sector in {holding.sector for holding in self.holdings.values()}
        }


def test_sizing_respects_risk_per_trade():
    manager = RiskManager(Portfolio(cash=1_000_000))
    manager.start_of_day()
    result = manager.size_position("TESTSTK", 100.0, 2.0, "tech")
    assert result.approved
    assert result.quantity <= 1250


def test_sizing_respects_max_position_cap():
    manager = RiskManager(Portfolio(cash=100_000))
    manager.start_of_day()
    result = manager.size_position("TESTSTK", 100.0, 0.1, "tech")
    assert result.approved
    assert result.quantity * 100.0 <= 8_000


def test_kill_switch_blocks_new_entries():
    portfolio = Portfolio(cash=100_000)
    manager = RiskManager(portfolio)
    manager.start_of_day()
    portfolio.cash = 96_000
    result = manager.size_position("TESTSTK", 100.0, 2.0, "tech")
    assert not result.approved
    assert "kill-switch" in result.reason.lower()


def test_sector_cap_blocks_when_no_room_remains():
    holding = Holding("EXIST", quantity=250, price=100.0, sector="tech")
    portfolio = Portfolio(cash=75_000, holdings={holding.symbol: holding})
    manager = RiskManager(portfolio)
    manager.start_of_day()
    result = manager.size_position("NEWSTK", 100.0, 1.0, "tech")
    assert not result.approved
    assert "sector" in result.reason.lower()
