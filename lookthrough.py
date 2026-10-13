"""
lookthrough.py

Computes ETF look-through constituent exposure and risk factor group concentration.
"""

import json
import os
from typing import Any, Dict, List, Optional
import pandas as pd
from config import RISK_CONFIG, RISK_GROUPS


DEFAULT_ETF_JSON = os.path.join(os.path.dirname(__file__), "data", "etf_constituents_2026_10.json")


def load_etf_constituents(json_path: str = DEFAULT_ETF_JSON) -> Dict[str, Any]:
    """Loads dated ETF constituent data from JSON."""
    if not os.path.exists(json_path):
        return {}
    with open(json_path, "r") as f:
        return json.load(f)


def calculate_effective_weights(
    portfolio_df: pd.DataFrame,
    etf_data: Optional[Dict[str, Any]] = None,
) -> pd.DataFrame:
    """
    Computes effective weight for each stock: direct weight + indirect weight via ETFs.
    """
    if etf_data is None:
        etf_data = load_etf_constituents()

    df = portfolio_df.copy()
    etfs = etf_data.get("etfs", {})

    # Map direct weights
    direct_weights = dict(zip(df["Stock Symbol"], df["Weight_%"]))

    # Calculate indirect weights
    indirect_weights: Dict[str, Dict[str, float]] = {}
    for etf_sym, etf_info in etfs.items():
        etf_weight = direct_weights.get(etf_sym, 0.0)
        if etf_weight <= 0:
            continue
        top_10 = etf_info.get("top_10", [])
        for item in top_10:
            c_sym = item["symbol"]
            c_wt = item["weight_pct"]
            ind_val = etf_weight * (c_wt / 100.0)
            indirect_weights.setdefault(c_sym, {})[etf_sym] = ind_val

    rows = []
    all_syms = sorted(list(set(df["Stock Symbol"]).union(indirect_weights.keys())))
    for sym in all_syms:
        direct = direct_weights.get(sym, 0.0)
        etf_contributions = indirect_weights.get(sym, {})
        indirect_total = sum(etf_contributions.values())
        effective = direct + indirect_total

        if direct > 0 or indirect_total > 0:
            detail_str = ""
            if etf_contributions:
                detail_str = ", ".join(f"+{v:.2f}% via {k}" for k, v in etf_contributions.items())
            rows.append({
                "Symbol": sym,
                "Direct_Weight": direct,
                "Indirect_Weight": indirect_total,
                "Effective_Weight": effective,
                "ETF_Contributions": detail_str,
            })

    res_df = pd.DataFrame(rows).sort_values(by="Effective_Weight", ascending=False)
    return res_df


def calculate_risk_group_exposures(
    portfolio_df: pd.DataFrame,
    risk_groups: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Dict[str, Any]]:
    """
    Calculates total portfolio weight exposure per risk factor group.
    """
    if risk_groups is None:
        risk_groups = RISK_GROUPS

    df = portfolio_df.copy()
    direct_weights = dict(zip(df["Stock Symbol"], df["Weight_%"]))

    results: Dict[str, Dict[str, Any]] = {}
    for group_name, members in risk_groups.items():
        group_symbols = [s for s in members if s in direct_weights]
        total_exposure = sum(direct_weights.get(s, 0.0) for s in group_symbols)
        cap = RISK_CONFIG.max_risk_group_pct
        breached = total_exposure > cap
        results[group_name] = {
            "exposure_pct": total_exposure,
            "cap_pct": cap,
            "breached": breached,
            "members_held": group_symbols,
            "member_breakdown": {s: direct_weights[s] for s in group_symbols},
        }

    return results


def format_lookthrough_and_risk_groups_markdown(
    effective_df: pd.DataFrame,
    risk_group_results: Dict[str, Dict[str, Any]],
) -> str:
    """Formats look-through weights and risk factor groups into markdown."""
    md = "### Risk Factor Groups Concentration\n\n"
    md += f"Portfolio exposure across macro risk buckets (Risk Cap: **{RISK_CONFIG.max_risk_group_pct:.1f}%**):\n\n"

    group_rows = []
    for gname, gdata in sorted(risk_group_results.items(), key=lambda x: -x[1]["exposure_pct"]):
        status = "⚠️ BREACH" if gdata["breached"] else "OK"
        held_list = ", ".join(f"{s} ({gdata['member_breakdown'][s]:.1f}%)" for s in gdata["members_held"][:5])
        if len(gdata["members_held"]) > 5:
            held_list += f", +{len(gdata['members_held']) - 5} more"
        group_rows.append({
            "Risk Group": gname,
            "Exposure": f"{gdata['exposure_pct']:.1f}%",
            "Cap": f"{gdata['cap_pct']:.1f}%",
            "Status": status,
            "Top Constituents": held_list if held_list else "None",
        })
    md += pd.DataFrame(group_rows).to_markdown(index=False) + "\n\n"

    md += "### ETF Look-Through Effective Exposure\n\n"
    md += "Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:\n\n"

    # Only show stocks with direct or indirect holdings
    disp_rows = []
    for _, r in effective_df.iterrows():
        sym = r["Symbol"]
        dir_wt = r["Direct_Weight"]
        eff_wt = r["Effective_Weight"]
        detail = r["ETF_Contributions"]
        disp_rows.append({
            "Symbol": sym,
            "Direct Weight": f"{dir_wt:.1f}%" if dir_wt > 0 else "0.0%",
            "Effective Weight": f"{eff_wt:.2f}%",
            "Indirect Source": detail if detail else "Direct only",
        })

    md += pd.DataFrame(disp_rows[:15]).to_markdown(index=False) + "\n"
    if len(disp_rows) > 15:
        md += f"\n*Showing top 15 of {len(disp_rows)} holdings by effective weight.*\n"
    md += "\n"

    return md
