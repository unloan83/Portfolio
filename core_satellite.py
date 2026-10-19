"""
core_satellite.py

Classifies portfolio into Core (Index ETFs) and Satellite (Stocks & Thematic ETFs).
Analyzes allocation vs targets and ranks satellite positions by conviction and weight.
"""

import re
from typing import Any, Dict, List, Optional
import pandas as pd
from config import RISK_CONFIG, RiskConfig

CORE_SYMBOLS = {"ICINIF", "HDF250", "MIR150"}


def classify_holding(symbol: str) -> str:
    """Classifies a holding as Core (index ETF) or Satellite (stock/thematic ETF)."""
    if symbol in CORE_SYMBOLS:
        return "Core"
    return "Satellite"


def get_holding_type(symbol: str, sector: str) -> str:
    """Returns human-readable category for holding."""
    if symbol in CORE_SYMBOLS:
        return "Index ETF (Core)"
    if symbol in ("ICIGOL", "ICIPSE"):
        return "Commodity ETF"
    if symbol in ("KOTAKBKETF", "NIPNIT"):
        return "Thematic ETF"
    return "Single Stock"


def calculate_core_satellite_view(
    portfolio_df: pd.DataFrame,
    thesis_dict: Optional[Dict[str, Any]] = None,
    config: RiskConfig = RISK_CONFIG,
) -> Dict[str, Any]:
    """Computes Core/Satellite breakdown, ranks satellite holdings, and flags consolidation candidates."""
    if thesis_dict is None:
        thesis_dict = {}

    df = portfolio_df.copy()

    core_rows: List[Dict[str, Any]] = []
    satellite_rows: List[Dict[str, Any]] = []

    for _, row in df.iterrows():
        sym = str(row["Stock Symbol"]).strip()
        w = float(row.get("Weight_%", 0.0))
        qty = float(row.get("Qty", 0.0))
        px = float(row.get("Valuation_Price", row.get("Current Market Price", 0.0)))
        sec = str(row.get("Sector", "Other"))
        h_type = get_holding_type(sym, sec)
        cls = classify_holding(sym)

        t_info = thesis_dict.get(sym, {})
        conv = t_info.get("conviction")
        conv_val = None
        if conv is not None and not pd.isna(conv) and str(conv).strip() != "":
            s_conv = str(conv).strip()
            try:
                conv_val = float(s_conv)
            except ValueError:
                match = re.search(r"(\d+(?:\.\d+)?)", s_conv)
                if match:
                    try:
                        conv_val = float(match.group(1))
                    except ValueError:
                        conv_val = None

        item = {
            "Symbol": sym,
            "Sector": sec,
            "Type": h_type,
            "Weight": w,
            "Qty": qty,
            "Price": px,
            "Value": qty * px,
            "Conviction": conv_val,
            "Conviction_Disp": str(int(conv_val)) if conv_val is not None else "N/A",
        }

        if cls == "Core":
            core_rows.append(item)
        else:
            # Consolidation flag: low conviction (< 4) or tiny weight (< 1.0%) with conviction < 5
            is_consolidate = (conv_val is None or conv_val < 4.0) or (w < 1.0 and conv_val < 5.0)
            item["Consolidate"] = is_consolidate
            item["Status"] = "⚠️ Consolidate" if is_consolidate else "Active"
            satellite_rows.append(item)

    core_weight = sum(r["Weight"] for r in core_rows)
    satellite_weight = sum(r["Weight"] for r in satellite_rows)

    # Rank satellite holdings by Conviction (descending, None last), then Weight (descending)
    satellite_sorted = sorted(
        satellite_rows,
        key=lambda x: (x["Conviction"] is not None, x["Conviction"] or -1, x["Weight"]),
        reverse=True,
    )

    return {
        "core_weight": core_weight,
        "satellite_weight": satellite_weight,
        "core_count": len(core_rows),
        "satellite_count": len(satellite_rows),
        "target_core_pct": config.target_core_pct,
        "target_satellite_count": config.target_satellite_count,
        "core_holdings": sorted(core_rows, key=lambda x: x["Weight"], reverse=True),
        "satellite_holdings": satellite_sorted,
    }


def format_core_satellite_markdown(view_data: Dict[str, Any]) -> str:
    """Formats Core/Satellite portfolio review for README.md."""
    c_wt = view_data["core_weight"]
    t_c_wt = view_data["target_core_pct"]
    s_wt = view_data["satellite_weight"]
    s_cnt = view_data["satellite_count"]
    t_s_cnt = view_data["target_satellite_count"]
    c_cnt = view_data["core_count"]

    core_gap = t_c_wt - c_wt
    sat_gap = s_cnt - t_s_cnt

    md = "### Core / Satellite Portfolio Structure\n\n"
    md += f"* **Core Allocation (Index ETFs)**: **{c_wt:.1f}%** (Target: {t_c_wt:.1f}%, Gap: {core_gap:+.1f}%) across {c_cnt} index ETFs\n"
    md += f"* **Satellite Allocation (Stocks & Thematic ETFs)**: **{s_wt:.1f}%** across **{s_cnt} holdings** (Target: ≤{t_s_cnt}, Excess: +{sat_gap})\n\n"

    # Core holdings summary
    if view_data["core_holdings"]:
        md += "#### Core Holdings (Passive Index Foundation)\n\n"
        c_disp = []
        for c in view_data["core_holdings"]:
            c_disp.append({
                "Symbol": c["Symbol"],
                "Category": c["Type"],
                "Weight": f"{c['Weight']:.1f}%",
                "Value": f"₹{c['Value']:,.0f}",
                "Conviction": c["Conviction_Disp"],
            })
        md += pd.DataFrame(c_disp).to_markdown(index=False) + "\n\n"

    # Satellite rankings table
    sat = view_data["satellite_holdings"]
    if sat:
        md += "#### Satellite Holdings (Ranked by Conviction & Weight)\n\n"
        s_disp = []
        for r in sat:
            s_disp.append({
                "Symbol": r["Symbol"],
                "Sector": r["Sector"],
                "Type": r["Type"],
                "Conviction": r["Conviction_Disp"],
                "Weight": f"{r['Weight']:.1f}%",
                "Value": f"₹{r['Value']:,.0f}",
                "Status": r["Status"],
            })
        md += pd.DataFrame(s_disp).to_markdown(index=False) + "\n\n"

    return md
