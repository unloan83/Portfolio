"""Monthly scorecard: did following the model's SELL / re-entry signals beat holding everything?

Two books start on config.scorecard_start with the quantities in
data/scorecard_baseline.csv:
  * Hold: keeps every baseline holding.
  * Follow: sells a holding at the close of the session after the model's first
    SELL for it (same next-session execution as hindcast/loss_control.py), keeps
    the proceeds in cash at scorecard_cash_rate, and buys back at the close after
    the first run where the decision is no longer SELL or a RE-ENTRY is logged.
Signals come from re-engineering.csv; prices are daily closes. Costs and tax are
not included. This scores the rule, not your actual trades or cash.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Callable, Optional

import pandas as pd

from config import RISK_CONFIG, RiskConfig

BASELINE_FILE = "data/scorecard_baseline.csv"
REPORT_FILE = "reports/scorecard.md"


@dataclass
class Switch:
    symbol: str
    signal_date: pd.Timestamp
    kind: str  # "EXIT" or "RE-ENTRY"
    exec_date: Optional[pd.Timestamp] = None
    exec_price: Optional[float] = None


@dataclass
class ScorecardResult:
    daily: pd.DataFrame
    switches: list[Switch] = field(default_factory=list)


def signal_switches(tracking: pd.DataFrame, start: str) -> list[Switch]:
    """EXIT on the first SELL run; RE-ENTRY on the first later run that is not SELL."""
    df = tracking.copy()
    df["Analysis_Date"] = pd.to_datetime(df["Analysis_Date"], errors="coerce")
    df = df[(df["Analysis_Date"] >= pd.Timestamp(start)) & df["Decision"].notna()]
    order = "run_timestamp_ist" if "run_timestamp_ist" in df.columns else "Analysis_Date"
    df = df.sort_values([order, "Analysis_Date"], kind="stable")
    out: list[Switch] = []
    for sym, rows in df.groupby("Stock_Symbol", sort=True):
        invested = True
        for _, r in rows.iterrows():
            dec = str(r["Decision"]).strip().upper()
            if invested and dec == "SELL":
                out.append(Switch(sym, r["Analysis_Date"], "EXIT"))
                invested = False
            elif not invested and dec != "SELL":
                out.append(Switch(sym, r["Analysis_Date"], "RE-ENTRY"))
                invested = True
    return out


def simulate(closes: pd.DataFrame, qty: pd.Series, switches: list[Switch], start: str,
             cash_rate: float) -> ScorecardResult:
    """Daily values of the Hold and Follow books. A switch fills at the first close after its signal date."""
    closes = closes.loc[closes.index >= pd.Timestamp(start)].ffill()
    syms = [s for s in qty.index if s in closes.columns]
    daily_cash = (1 + cash_rate) ** (1 / 252) - 1
    by_sym: dict[str, list[Switch]] = {}
    for sw in switches:
        by_sym.setdefault(sw.symbol, []).append(sw)

    hold = pd.Series(0.0, index=closes.index)
    follow = pd.Series(0.0, index=closes.index)
    for sym in syms:
        px = closes[sym]
        hold = hold.add(qty[sym] * px, fill_value=0.0)
        units, cash = float(qty[sym]), 0.0
        pending = sorted(by_sym.get(sym, []), key=lambda s: s.signal_date)
        vals = []
        for day, price in px.items():
            cash *= 1 + daily_cash
            while pending and pending[0].signal_date < day and pd.notna(price):
                sw = pending.pop(0)
                sw.exec_date, sw.exec_price = day, float(price)
                if sw.kind == "EXIT" and units > 0:
                    cash, units = units * price, 0.0
                elif sw.kind == "RE-ENTRY" and units == 0:
                    units, cash = cash / price, 0.0
            vals.append(units * price + cash if pd.notna(price) else float("nan"))
        follow = follow.add(pd.Series(vals, index=px.index), fill_value=0.0)
    daily = pd.DataFrame({"Hold": hold, "Follow": follow})
    return ScorecardResult(daily=daily, switches=[s for s in switches if s.symbol in syms])


def _max_fall(v: pd.Series) -> float:
    v = v.dropna()
    return float((v / v.cummax() - 1).min()) if len(v) else float("nan")


def render(res: ScorecardResult, closes: pd.DataFrame, start: str) -> tuple[str, str]:
    """(markdown report, short Telegram HTML card)."""
    d = res.daily.dropna()
    if d.empty:
        return "# Model scorecard\n\nNo price data yet.\n", ""
    first, last = d.iloc[0], d.iloc[-1]
    ret = {k: last[k] / first[k] - 1 for k in d.columns}
    fall = {k: _max_fall(d[k]) for k in d.columns}
    month_end = d.groupby(d.index.to_period("M")).tail(1)
    md = [f"# Model scorecard (since {start})", "",
          "Follow = act on every model SELL / re-entry at the next close; Hold = keep every holding "
          "from the baseline. Cash earns the liquid-fund proxy; costs and tax not included.", "",
          "| Book | Value now | Return | Worst fall |", "|---|---|---|---|"]
    for k in ("Follow", "Hold"):
        md.append(f"| {k} | ₹{last[k]:,.0f} | {ret[k]:+.1%} | {fall[k]:.1%} |")
    md += ["", f"Difference (Follow − Hold): ₹{last['Follow'] - last['Hold']:+,.0f}", "",
           "## Month-end values", "", "| Month | Follow | Hold |", "|---|---|---|"]
    for day, row in month_end.iterrows():
        md.append(f"| {day:%b %Y} | ₹{row['Follow']:,.0f} | ₹{row['Hold']:,.0f} |")
    md += ["", "## Signals and what happened since", "",
           "| Symbol | Signal | Signal date | Filled | Fill price | Price now | Move since |", "|---|---|---|---|---|---|---|"]
    for sw in sorted(res.switches, key=lambda s: (s.signal_date, s.symbol)):
        now = closes[sw.symbol].dropna().iloc[-1] if sw.symbol in closes else float("nan")
        if sw.exec_price:
            move = now / sw.exec_price - 1
            md.append(f"| {sw.symbol} | {sw.kind} | {sw.signal_date:%d %b %Y} | {sw.exec_date:%d %b %Y} | "
                      f"₹{sw.exec_price:,.2f} | ₹{now:,.2f} | {move:+.1%} |")
        else:
            md.append(f"| {sw.symbol} | {sw.kind} | {sw.signal_date:%d %b %Y} | pending | | ₹{now:,.2f} | |")
    md += ["", "For an EXIT, a negative move means the fall was avoided; for a RE-ENTRY, a positive move is gain captured."]

    diff = last["Follow"] - last["Hold"]
    verdict = "ahead of" if diff > 0 else "behind"
    card = (f"📊 <b>Monthly scorecard</b> (since {start})\n"
            f"• Follow model: ₹{last['Follow']:,.0f} ({ret['Follow']:+.1%}, worst fall {fall['Follow']:.1%})\n"
            f"• Hold all: ₹{last['Hold']:,.0f} ({ret['Hold']:+.1%}, worst fall {fall['Hold']:.1%})\n"
            f"• Following the model is ₹{abs(diff):,.0f} {verdict} holding. Details: reports/scorecard.md")
    return "\n".join(md) + "\n", card


def fetch_closes(tickers: dict[str, str], start: str) -> pd.DataFrame:
    import yfinance as yf
    begin = (pd.Timestamp(start) - pd.Timedelta(days=7)).strftime("%Y-%m-%d")
    cols = {}
    for sym, tk in tickers.items():
        try:
            h = yf.Ticker(tk).history(start=begin)["Close"].dropna()
            if len(h):
                h.index = pd.DatetimeIndex(h.index).tz_localize(None).normalize()
                cols[sym] = h
        except Exception as exc:
            print(f"[warn] scorecard price fetch failed for {sym}: {exc}")
    return pd.DataFrame(cols).sort_index()


def due_this_month(today: pd.Timestamp, report_file: str = REPORT_FILE) -> bool:
    """True when the scorecard has not been produced for today's month yet."""
    marker = f"<!-- month: {today:%Y-%m} -->"
    if not os.path.exists(report_file):
        return True
    with open(report_file) as fh:
        return marker not in fh.read()


def run_scorecard(tracking_file: str, ticker_map: dict[str, str],
                  fetch: Callable[[dict[str, str], str], pd.DataFrame] = fetch_closes,
                  config: RiskConfig = RISK_CONFIG, today: Optional[pd.Timestamp] = None) -> str:
    """Writes reports/scorecard.md and returns the Telegram card ('' if it cannot run)."""
    if not (os.path.exists(BASELINE_FILE) and os.path.exists(tracking_file)):
        return ""
    base = pd.read_csv(BASELINE_FILE)
    qty = base.set_index("Symbol")["Qty"].astype(float)
    tracking = pd.read_csv(tracking_file)
    start = config.scorecard_start
    tickers = {s: ticker_map.get(s, f"{s}.NS") for s in qty.index}
    closes = fetch(tickers, start)
    if closes.empty:
        return ""
    res = simulate(closes, qty, signal_switches(tracking, start), start, config.scorecard_cash_rate)
    md, card = render(res, closes.loc[closes.index >= pd.Timestamp(start)], start)
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    today = pd.Timestamp.today() if today is None else today
    with open(REPORT_FILE, "w") as fh:
        fh.write(f"<!-- month: {today:%Y-%m} -->\n" + md)
    return card
