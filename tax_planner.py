"""
tax_planner.py

Calculates capital gains and tax harvesting strategy for the current financial year
using FIFO lot tracking on trade history from trades.csv.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from config import RISK_CONFIG, RiskConfig


def get_financial_year(date: datetime) -> Tuple[datetime, datetime, str]:
    """Returns (start_date, end_date, label) for the Indian financial year containing date."""
    year = date.year
    if date.month >= 4:
        start = datetime(year, 4, 1)
        end = datetime(year + 1, 3, 31, 23, 59, 59)
        label = f"FY {year}-{str(year + 1)[-2:]}"
    else:
        start = datetime(year - 1, 4, 1)
        end = datetime(year, 3, 31, 23, 59, 59)
        label = f"FY {year - 1}-{str(year)[-2:]}"
    return start, end, label


def calculate_tax_plan(
    trades_df: pd.DataFrame,
    portfolio_df: pd.DataFrame,
    current_prices: Optional[Dict[str, float]] = None,
    valuation_date: Optional[datetime] = None,
    config: RiskConfig = RISK_CONFIG,
) -> Dict[str, Any]:
    """
    Computes realised and unrealised capital gains (STCG/LTCG) using FIFO lots,
    evaluates unrealised LTCG eligible under Section 112A exemption, and
    identifies loss-harvest candidates with tax offset values.
    """
    if valuation_date is None:
        valuation_date = datetime.now()
    val_date = pd.to_datetime(valuation_date).tz_localize(None).normalize()
    fy_start, fy_end, fy_label = get_financial_year(val_date.to_pydatetime())

    # Map current prices
    prices: Dict[str, float] = {}
    if current_prices:
        prices.update(current_prices)
    for _, row in portfolio_df.iterrows():
        sym = str(row["Stock Symbol"]).strip()
        if sym not in prices and "Current Market Price" in row and pd.notna(row["Current Market Price"]):
            prices[sym] = float(row["Current Market Price"])

    # Prepare trades
    trades = trades_df.copy()
    valid_trades = trades[
        pd.to_datetime(trades["Date"], errors="coerce").notna()
        & pd.to_numeric(trades["Qty"], errors="coerce").notna()
        & pd.to_numeric(trades["Price"], errors="coerce").notna()
    ].copy()
    valid_trades["Date"] = pd.to_datetime(valid_trades["Date"]).dt.tz_localize(None).dt.normalize()
    valid_trades["Qty"] = valid_trades["Qty"].astype(float)
    valid_trades["Price"] = valid_trades["Price"].astype(float)
    valid_trades["Action"] = valid_trades["Action"].astype(str).str.strip().str.upper()
    valid_trades = valid_trades.sort_values("Date")

    open_lots: Dict[str, List[Dict[str, Any]]] = {}
    realised_fy_stcg = 0.0
    realised_fy_ltcg = 0.0
    realised_fy_trades: List[Dict[str, Any]] = []

    for _, r in valid_trades.iterrows():
        sym = str(r["Stock Symbol"]).strip()
        act = r["Action"]
        q = r["Qty"]
        p = r["Price"]
        d = r["Date"]

        open_lots.setdefault(sym, [])

        if act == "BUY":
            open_lots[sym].append({"date": d, "qty": q, "price": p})
        elif act == "SELL":
            rem_qty = q
            while rem_qty > 0 and open_lots[sym]:
                first_lot = open_lots[sym][0]
                matched_qty = min(rem_qty, first_lot["qty"])
                holding_days = (d - first_lot["date"]).days
                gain = (p - first_lot["price"]) * matched_qty

                # If the sale fell within the current financial year:
                if fy_start <= d <= fy_end:
                    if holding_days > 365:
                        realised_fy_ltcg += gain
                        term = "LTCG"
                    else:
                        realised_fy_stcg += gain
                        term = "STCG"
                    realised_fy_trades.append({
                        "Symbol": sym,
                        "Date": d.strftime("%Y-%m-%d"),
                        "Qty": matched_qty,
                        "Buy Price": first_lot["price"],
                        "Sell Price": p,
                        "Gain": gain,
                        "Term": term,
                        "Holding Days": holding_days,
                    })

                first_lot["qty"] -= matched_qty
                rem_qty -= matched_qty
                if first_lot["qty"] <= 1e-6:
                    open_lots[sym].pop(0)

    # Process open lots at valuation date
    unrealised_ltcg = 0.0
    unrealised_stcg = 0.0
    loss_harvest_lots: List[Dict[str, Any]] = []

    for sym, lots in open_lots.items():
        cur_p = prices.get(sym, 0.0)
        for lot in lots:
            l_qty = lot["qty"]
            if l_qty <= 1e-6:
                continue
            l_price = lot["price"]
            l_date = lot["date"]
            holding_days = (val_date - l_date).days
            gain = (cur_p - l_price) * l_qty

            if holding_days > 365:
                if gain > 0:
                    unrealised_ltcg += gain
                else:
                    loss_harvest_lots.append({
                        "Symbol": sym,
                        "Qty": l_qty,
                        "Buy Date": l_date.strftime("%Y-%m-%d"),
                        "Buy Price": l_price,
                        "Current Price": cur_p,
                        "Loss": -gain,
                        "Term": "LTCG",
                        "Holding Days": holding_days,
                        "Tax Rate": config.ltcg_rate,
                        "Tax Savings": -gain * config.ltcg_rate,
                    })
            else:
                if gain > 0:
                    unrealised_stcg += gain
                else:
                    loss_harvest_lots.append({
                        "Symbol": sym,
                        "Qty": l_qty,
                        "Buy Date": l_date.strftime("%Y-%m-%d"),
                        "Buy Price": l_price,
                        "Current Price": cur_p,
                        "Loss": -gain,
                        "Term": "STCG",
                        "Holding Days": holding_days,
                        "Tax Rate": config.stcg_rate,
                        "Tax Savings": -gain * config.stcg_rate,
                    })

    # LTCG Exemption computation (Section 112A: ₹1.25 Lakh per FY)
    exemption_limit = config.ltcg_exemption_limit
    remaining_exemption = max(0.0, exemption_limit - max(0.0, realised_fy_ltcg))
    harvestable_tax_free_ltcg = min(unrealised_ltcg, remaining_exemption)

    # Aggregate loss harvest candidates by symbol
    loss_by_symbol: Dict[str, Dict[str, Any]] = {}
    for item in loss_harvest_lots:
        sym = item["Symbol"]
        loss_by_symbol.setdefault(sym, {
            "Symbol": sym,
            "Total Loss": 0.0,
            "Total Shares": 0.0,
            "Current Price": item["Current Price"],
            "Avg Buy Price": 0.0,
            "Terms": set(),
            "Total Tax Savings": 0.0,
            "_cost_sum": 0.0,
        })
        loss_by_symbol[sym]["Total Loss"] += item["Loss"]
        loss_by_symbol[sym]["Total Shares"] += item["Qty"]
        loss_by_symbol[sym]["_cost_sum"] += item["Buy Price"] * item["Qty"]
        loss_by_symbol[sym]["Terms"].add(item["Term"])
        loss_by_symbol[sym]["Total Tax Savings"] += item["Tax Savings"]

    aggregated_candidates = []
    for sym, c in loss_by_symbol.items():
        avg_buy = c["_cost_sum"] / c["Total Shares"] if c["Total Shares"] > 0 else 0.0
        terms_str = "/".join(sorted(list(c["Terms"])))
        aggregated_candidates.append({
            "Symbol": sym,
            "Shares": int(c["Total Shares"]),
            "Current Price": c["Current Price"],
            "Avg Buy Price": avg_buy,
            "Unrealised Loss": c["Total Loss"],
            "Term": terms_str,
            "Tax Offset Savings": c["Total Tax Savings"],
        })

    aggregated_candidates.sort(key=lambda x: x["Unrealised Loss"], reverse=True)

    return {
        "financial_year": fy_label,
        "fy_start": fy_start.strftime("%Y-%m-%d"),
        "fy_end": fy_end.strftime("%Y-%m-%d"),
        "realised_stcg": realised_fy_stcg,
        "realised_ltcg": realised_fy_ltcg,
        "unrealised_stcg": unrealised_stcg,
        "unrealised_ltcg": unrealised_ltcg,
        "exemption_limit": exemption_limit,
        "remaining_exemption": remaining_exemption,
        "harvestable_tax_free_ltcg": harvestable_tax_free_ltcg,
        "loss_harvest_candidates": aggregated_candidates,
        "total_loss_harvest_offset": sum(c["Unrealised Loss"] for c in aggregated_candidates),
        "total_tax_savings_potential": sum(c["Tax Offset Savings"] for c in aggregated_candidates),
        "stcg_rate": config.stcg_rate,
        "ltcg_rate": config.ltcg_rate,
    }


def format_tax_plan_markdown(plan: Dict[str, Any], config: RiskConfig = RISK_CONFIG) -> str:
    """Formats the tax plan section for README.md."""
    fy = plan["financial_year"]
    stcg_rate_disp = f"{plan['stcg_rate']:.1%}"
    ltcg_rate_disp = f"{plan['ltcg_rate']:.1%}"
    exemption_disp = f"₹{plan['exemption_limit']:,.0f}"

    md = f"### Tax Plan ({fy})\n\n"
    md += "> [!NOTE]\n"
    md += f"> **Advisory Notice**: This tax plan is indicative and for planning purposes only. Tax parameters "
    md += f"(STCG Rate: **{stcg_rate_disp}**, LTCG Rate: **{ltcg_rate_disp}**, Section 112A LTCG Exemption: **{exemption_disp}**) "
    md += "are configured in `config.py` (`stcg_rate`, `ltcg_rate`, `ltcg_exemption_limit`). Consult a chartered accountant for statutory tax filing.\n\n"

    # Capital Gains Summary Table
    r_stcg = plan["realised_stcg"]
    r_ltcg = plan["realised_ltcg"]
    u_ltcg = plan["unrealised_ltcg"]
    u_stcg = plan["unrealised_stcg"]
    rem_ex = plan["remaining_exemption"]
    harv_ltcg = plan["harvestable_tax_free_ltcg"]

    summary_rows = [
        {"Metric": f"Realised STCG ({fy} so far)", "Amount": f"₹{r_stcg:,.2f}", "Tax Rate": stcg_rate_disp, "Notes": "Taxable on net short-term gains"},
        {"Metric": f"Realised LTCG ({fy} so far)", "Amount": f"₹{r_ltcg:,.2f}", "Tax Rate": ltcg_rate_disp, "Notes": f"Subject to {exemption_disp} annual exemption"},
        {"Metric": "Section 112A LTCG Exemption Remaining", "Amount": f"₹{rem_ex:,.2f}", "Tax Rate": "0.0%", "Notes": f"Limit: {exemption_disp} per financial year"},
        {"Metric": "Total Unrealised LTCG (> 365 days)", "Amount": f"₹{u_ltcg:,.2f}", "Tax Rate": ltcg_rate_disp, "Notes": "Open long-term profit inventory"},
        {"Metric": "⚡ Eligible Tax-Free LTCG to Harvest", "Amount": f"₹{harv_ltcg:,.2f}", "Tax Rate": "0.0% (Zero Tax)", "Notes": "Can be booked tax-free before FY end"},
        {"Metric": "Total Unrealised STCG (≤ 365 days)", "Amount": f"₹{u_stcg:,.2f}", "Tax Rate": stcg_rate_disp, "Notes": "Short-term unrealised gains"},
    ]
    md += "#### Capital Gains Inventory (FIFO Matching)\n\n"
    md += pd.DataFrame(summary_rows).to_markdown(index=False) + "\n\n"

    # Loss Harvesting Candidates
    cands = plan.get("loss_harvest_candidates", [])
    if cands:
        md += "#### Loss-Harvest Candidates (Offset Value)\n\n"
        md += f"The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹{plan['total_loss_harvest_offset']:,.0f}**, Tax savings potential: **₹{plan['total_tax_savings_potential']:,.0f}**):\n\n"
        cand_rows = []
        for c in cands[:10]:
            cand_rows.append({
                "Symbol": c["Symbol"],
                "Shares": c["Shares"],
                "CMP": f"₹{c['Current Price']:.2f}",
                "Avg Cost": f"₹{c['Avg Buy Price']:.2f}",
                "Loss Offset Value": f"₹{c['Unrealised Loss']:,.0f}",
                "Term": c["Term"],
                "Potential Tax Saved": f"₹{c['Tax Offset Savings']:,.0f}",
            })
        md += pd.DataFrame(cand_rows).to_markdown(index=False) + "\n"
        if len(cands) > 10:
            md += f"\n*Showing top 10 of {len(cands)} loss-harvest candidates.*\n"
        md += "\n"

    return md
