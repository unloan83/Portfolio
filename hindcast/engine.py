"""Point-in-time replay of the live engine plus follow-model / do-nothing shadow books.

Every decision at date t sees only bars <= t; trades execute at the close of the
next trading day. No tax, fees or slippage are modelled.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Optional

import numpy as np
import pandas as pd

from analysis import FINANCIALS_SECTORS, compute_market_features
from config import RISK_GROUPS, RiskConfig
from signal_engine import evaluate_signal

MIN_SESSIONS = 252          # 200-DMA needs 200, 52-week high needs 252
FEATURE_TAIL = 460          # bars passed to compute_market_features (>= 252 + 200)
MIN_TRADE_FRACTION = 0.0005  # ignore adds/trims below 0.05% of NAV


@dataclass(frozen=True)
class NeutralInputs:
    """thesis.csv was written in 2026, so the replay never reads it."""
    thesis_text: str = "INTACT"
    conviction: float = 4.0
    roe: float = 0.15
    invalidation_mode: str = "none"  # none | cost_x0.85 | low_52w


@dataclass
class ReplayResult:
    decisions: pd.DataFrame
    nav: pd.DataFrame
    trades: pd.DataFrame


def decision_dates(calendar: pd.DatetimeIndex, start: str, end: str) -> list[pd.Timestamp]:
    """Last trading day of each month in [start, end]."""
    cal = calendar[(calendar >= pd.Timestamp(start)) & (calendar <= pd.Timestamp(end))]
    if len(cal) == 0:
        return []
    s = pd.Series(cal, index=cal)
    return list(s.groupby([cal.year, cal.month]).max().sort_values())


def aligned_closes(prices: dict[str, pd.DataFrame], calendar: pd.DatetimeIndex) -> pd.DataFrame:
    """Close per calendar day, forward-filled only after a symbol's first bar."""
    cols = {}
    for sym, df in prices.items():
        s = df["Close"].reindex(calendar.union(df.index)).sort_index().ffill()
        s = s.reindex(calendar)
        s[s.index < df.index[0]] = np.nan
        cols[sym] = s
    return pd.DataFrame(cols, index=calendar)


class FeatureCache:
    def __init__(self, prices: dict[str, pd.DataFrame]):
        self.prices = prices
        self._cache: dict[tuple, dict] = {}

    def sessions(self, sym: str, t: pd.Timestamp) -> int:
        df = self.prices.get(sym)
        return 0 if df is None else int(df.index.searchsorted(t, side="right"))

    def get(self, sym: str, t: pd.Timestamp, config: RiskConfig) -> dict:
        key = (sym, t, config.dma_200_breach_pct)
        if key not in self._cache:
            df = self.prices[sym]
            n = df.index.searchsorted(t, side="right")
            self._cache[key] = compute_market_features(df.iloc[max(0, n - FEATURE_TAIL):n], config)
        return self._cache[key]


def _sector_exposure(sym: str, sectors: dict[str, str], weights: dict[str, float]) -> float:
    sec = sectors.get(sym, "Other ETFs/Misc")
    if sec in FINANCIALS_SECTORS:
        return sum(w for s, w in weights.items() if sectors.get(s) in FINANCIALS_SECTORS)
    return sum(w for s, w in weights.items() if sectors.get(s, "Other ETFs/Misc") == sec)


def _group_exposure(sym: str, weights: dict[str, float]) -> float:
    groups = [mems for mems in RISK_GROUPS.values() if sym in mems]
    return max((sum(weights.get(m, 0.0) for m in mems) for mems in groups), default=0.0)


def _group_excess(weights: dict[str, float], sectors: dict[str, str], config: RiskConfig) -> dict[str, float]:
    """Each holding's pro-rata share (in % of NAV) of every breached sector/Financials/risk group."""
    buckets: list[list[str]] = []
    by_sector: dict[str, list[str]] = {}
    for s in weights:
        by_sector.setdefault(sectors.get(s, "Other ETFs/Misc"), []).append(s)
    buckets.extend(by_sector.values())
    buckets.append([s for s in weights if sectors.get(s) in FINANCIALS_SECTORS])
    out = {s: 0.0 for s in weights}
    for members in buckets:
        total = sum(weights[m] for m in members)
        if total > config.max_sector_pct:
            for m in members:
                out[m] = max(out[m], (total - config.max_sector_pct) * weights[m] / total)
    for mems in RISK_GROUPS.values():
        held = [m for m in mems if m in weights]
        total = sum(weights[m] for m in held)
        if total > config.max_risk_group_pct:
            for m in held:
                out[m] = max(out[m], (total - config.max_risk_group_pct) * weights[m] / total)
    return out


class Book:
    """Notional book in rupee value; cash optionally tracks the benchmark."""

    def __init__(self):
        self.shares: dict[str, float] = {}
        self.cost: dict[str, float] = {}
        self.cash = 0.0

    def nav(self, px: pd.Series) -> float:
        return self.cash + sum(q * px[s] for s, q in self.shares.items())

    def buy(self, sym: str, value: float, price: float) -> float:
        if value <= 0 or price <= 0:
            return 0.0
        q = value / price
        old_q = self.shares.get(sym, 0.0)
        self.cost[sym] = (old_q * self.cost.get(sym, price) + q * price) / (old_q + q)
        self.shares[sym] = old_q + q
        self.cash -= value
        return value

    def sell(self, sym: str, q: float, price: float) -> float:
        q = min(q, self.shares.get(sym, 0.0))
        if q <= 0:
            return 0.0
        self.shares[sym] -= q
        if self.shares[sym] <= 1e-12:
            del self.shares[sym]
            self.cost.pop(sym, None)
        self.cash += q * price
        return q * price

    def admit(self, sym: str, px: pd.Series) -> float:
        """Give a newly eligible symbol an equal share: cash first, then pro-rata sells."""
        nav = self.nav(px)
        target = nav / (len(self.shares) + 1)
        need = max(0.0, target - max(self.cash, 0.0))
        held = nav - self.cash
        traded = 0.0
        if need > 0 and held > 0:
            frac = min(1.0, need / held)
            for s in list(self.shares):
                traded += self.sell(s, self.shares[s] * frac, px[s])
        traded += self.buy(sym, min(target, self.cash), px[sym])
        return traded


def replay(
    prices: dict[str, pd.DataFrame],
    sectors: dict[str, str],
    bench: pd.Series,
    dates: list[pd.Timestamp],
    config: RiskConfig,
    neutral: NeutralInputs = NeutralInputs(),
    cash_mode: str = "zero",
    features: Optional[FeatureCache] = None,
    tickers: Optional[dict[str, str]] = None,
    universe: Optional[list[str]] = None,
    until: Optional[pd.Timestamp] = None,
) -> ReplayResult:
    """Replay monthly decisions over `dates` and simulate the three books.

    universe lists every symbol that must appear in the decision log even if its
    price series is missing (logged as NO DATA / MISSING).
    """
    if not dates:
        raise ValueError("no decision dates")
    features = features or FeatureCache(prices)
    tickers = tickers or {}
    universe = sorted(set(universe or prices.keys()))
    calendar = bench.index
    P = aligned_closes(prices, calendar)
    days = calendar[calendar >= dates[0]]
    if until is not None:
        days = days[days <= pd.Timestamp(until)]
    dset = set(dates)

    A, B = Book(), Book()
    bench_units = 0.0
    eligible_seen: set[str] = set()
    in_review: dict[str, bool] = {}
    pending: list[tuple] = []
    rec_rows, trade_rows, nav_rows = [], [], []

    for i, day in enumerate(days):
        px = P.loc[day]
        prev = days[i - 1] if i > 0 else None
        if cash_mode == "bench" and prev is not None and A.cash > 0:
            A.cash *= float(bench.loc[day] / bench.loc[prev])

        # 1) execute yesterday's decisions at today's close
        for book_name, action, sym, amount in pending:
            book = A if book_name == "A" else B
            price = float(px[sym])
            if action == "ADMIT":
                traded = book.admit(sym, px)
            elif action == "SELL_ALL":
                traded = book.sell(sym, book.shares.get(sym, 0.0), price)
            elif action == "SELL_VALUE":
                traded = book.sell(sym, amount / price, price)
            else:  # BUY_VALUE
                traded = book.buy(sym, min(amount, book.cash), price)
            if traded > 0:
                trade_rows.append({"date": day, "book": book_name, "action": action, "symbol": sym,
                                   "price": price, "value": traded})
        pending = []

        # 2) day-0 initial equal-weight book
        if i == 0:
            first = [s for s in prices if features.sessions(s, day) >= MIN_SESSIONS and pd.notna(px.get(s))]
            if not first:
                raise ValueError(f"no eligible symbols on {day.date()}")
            for book in (A, B):
                book.cash = 100.0
                for s in sorted(first):
                    book.buy(s, 100.0 / len(first), float(px[s]))
            bench_units = 100.0 / float(bench.loc[day])
            eligible_seen.update(first)

        nav_rows.append({"date": day, "A": A.nav(px), "B": B.nav(px), "C": bench_units * float(bench.loc[day])})

        # 3) decisions at a month-end close, executed tomorrow
        if day not in dset or i + 1 >= len(days):
            continue
        nav_a = A.nav(px)
        weights = {s: q * float(px[s]) / nav_a * 100 for s, q in A.shares.items()}
        excess = _group_excess(weights, sectors, config)
        eligible_now = [s for s in universe if s in prices and features.sessions(s, day) >= MIN_SESSIONS and pd.notna(px.get(s))]
        n_elig = max(1, len(eligible_now))
        for sym in universe:
            row = {"date": day, "symbol": sym, "ticker": tickers.get(sym, "")}
            if sym not in prices:
                rec_rows.append({**row, "data_tag": "MISSING", "decision": "NO DATA"})
                continue
            n_sess = features.sessions(sym, day)
            if n_sess == 0 or pd.isna(px.get(sym)):
                rec_rows.append({**row, "data_tag": "NOT_LISTED", "decision": "NO DATA"})
                continue
            if n_sess < MIN_SESSIONS:
                rec_rows.append({**row, "data_tag": "SHORT_HISTORY", "decision": "NO DATA"})
                continue
            if sym not in eligible_seen:
                eligible_seen.add(sym)
                pending += [("A", "ADMIT", sym, 0.0), ("B", "ADMIT", sym, 0.0)]
                rec_rows.append({**row, "data_tag": "ENTRY", "decision": "ENTRY"})
                continue

            f = features.get(sym, day, config)
            held = sym in A.shares
            price = f["price"]
            cost = A.cost.get(sym)
            total_return = (price / cost - 1.0) * 100 if held and cost else None
            if neutral.invalidation_mode == "cost_x0.85":
                inv = cost * 0.85 if held and cost else None
            elif neutral.invalidation_mode == "low_52w":
                inv = f.get("low_52w")
            else:
                inv = None
            w = weights.get(sym, 0.0)
            res = evaluate_signal(
                current_price=price, dma_50=f["dma_50"], dma_200=f["dma_200"], roe=neutral.roe,
                stock_sector=sectors.get(sym, "Other ETFs/Misc"),
                sector_risk_exposure=_sector_exposure(sym, sectors, weights),
                total_return=total_return, thesis_text=neutral.thesis_text, conviction=neutral.conviction,
                invalidation_price=inv, stock_weight=w, config=config,
                high_52w=f["high_52w"], atr=f["atr"], risk_group_exposure=_group_exposure(sym, weights),
                symbol=sym, role="core", is_month_end=True, is_friday_close=f["is_friday_close"],
                price_history=f["history"] if inv is not None else None,
                sessions_below_200dma=f["sessions_below_200dma"], sma_10_month=f["sma_10_month"],
                in_dma_review=in_review.get(sym, False), dma_200_rising=f["dma_200_rising"],
                dma_200_20_ago=f["dma_200_20_ago"], vol_adj_return_6m=f["vol_adj_return_6m"],
                vol_adj_return_12m=f["vol_adj_return_12m"],
            )
            in_review[sym] = res.dma_review_active
            value = weights.get(sym, 0.0) / 100 * nav_a
            if res.decision == "SELL" and held:
                pending.append(("A", "SELL_ALL", sym, 0.0))
            elif res.decision == "TRIM" and held:
                trim = max(
                    value - config.max_position_pct / 100 * nav_a,
                    value * config.trailing_trim_fraction if res.trailing_stop_hit else 0.0,
                    excess.get(sym, 0.0) / 100 * nav_a,
                )
                trim = min(trim, value)
                if trim > MIN_TRADE_FRACTION * nav_a:
                    pending.append(("A", "SELL_VALUE", sym, trim))
            elif res.decision in ("ACCUMULATE", "BUY"):
                target = min(config.max_position_pct, 100.0 / n_elig) / 100 * nav_a
                add = max(0.0, target - value) / 3.0  # monthly tranche: a third of the gap
                if add > MIN_TRADE_FRACTION * nav_a:
                    pending.append(("A", "BUY_VALUE", sym, add))
            rec_rows.append({
                **row, "data_tag": "OK", "decision": res.decision, "signal": res.signal,
                "rationale": res.rationale, "price": price, "weight_pct": w,
                "total_return_pct": total_return, "invalidation_price": inv,
                "dma_50": f["dma_50"], "dma_200": f["dma_200"], "high_52w": f["high_52w"], "atr": f["atr"],
                "sessions_below_200dma": f["sessions_below_200dma"], "dma_review_active": res.dma_review_active,
                "trailing_stop_hit": res.trailing_stop_hit,
            })
        # BUY_VALUE orders are funded from cash; run sells first so proceeds are available.
        order = {"ADMIT": 0, "SELL_ALL": 1, "SELL_VALUE": 2, "BUY_VALUE": 3}
        pending.sort(key=lambda p: (order[p[1]], p[0], p[2]))

    nav = pd.DataFrame(nav_rows).set_index("date")
    return ReplayResult(pd.DataFrame(rec_rows), nav, pd.DataFrame(trade_rows))


def with_overrides(config: RiskConfig, overrides: dict) -> RiskConfig:
    return replace(config, **overrides) if overrides else config
