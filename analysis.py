import math
import os
import re
import html
from dataclasses import dataclass
from datetime import datetime
from typing import Mapping, Optional
from zoneinfo import ZoneInfo
import pandas as pd
import yfinance as yf

from config import RISK_CONFIG, RISK_GROUPS, RiskConfig
from indicators import atr as compute_atr
from risk_manager import RiskManager, trim_quantity
from signal_engine import DATA_FAILURE_TRENDS, evaluate_signal
import lookthrough

# Fully vetted Exchange Tickers mapping
TICKER_MAP = {
    'ASHLEY': 'ASHOKLEY.NS', 'FEDBAN': 'FEDERALBNK.NS', 'HDFBAN': 'HDFCBANK.NS',
    'HDF250': 'HDFCSML250.NS', 'ICIGOL': 'GOLDIETF.NS', 'ICINIF': '537007.BO',
    'ICIPSE': 'SILVERIETF.NS', 'NIPNIT': 'ITBEES.NS', 'MIR150': 'MIDCAPETF.NS', 'KOTAKBKETF': 'BANKNIFTY1.NS',
    'BHAELE': 'BEL.NS', 'TATGLO': 'TATACONSUM.NS', 'JIOFIN': 'JIOFIN.NS',
    'WIPRO': 'WIPRO.NS', 'ENGIND': 'ENGINERSIN.NS', 'LIC': 'LICI.NS',
    'DRREDD': 'DRREDDY.NS', 'SEQSCI': 'VIYASH.NS', 'JSWENE': 'JSWENERGY.NS',
    'NHPC': 'NHPC.NS', 'NTPC': 'NTPC.NS', 'NTPGRE': 'NTPCGREEN.NS',
    'SJVLIM': 'SJVN.NS', 'TATPOW': 'TATAPOWER.NS', 'GAIL': 'GAIL.NS',
    'GUJGA': 'GUJENERGY.NS', 'HINPET': 'HINDPETRO.NS', 'ONGC': 'ONGC.NS',
    'PETLNG': 'PETRONET.NS', 'RELIND': 'RELIANCE.NS', 'GUJPPL': 'GPPL.NS',
    'IDECEL': 'IDEA.NS', 'TATCAP': 'TATACAP.NS', 'LGELEC': 'LGEINDIA.NS'
}

# Explicit sector definitions to track concentration rules
SECTOR_MAP = {
    'ASHLEY': 'Auto', 'TATGLO': 'Consumption', 'LGELEC': 'Consumer Electronics',
    'FEDBAN': 'Banking', 'HDFBAN': 'Banking', 'KOTAKBKETF': 'Banking', 'JIOFIN': 'Financial Services', 'TATCAP': 'Financial Services',
    'WIPRO': 'IT', 'NIPNIT': 'IT',
    'BHAELE': 'Defense', 'ENGIND': 'Infrastructure', 'GUJPPL': 'Infrastructure',
    'LIC': 'Insurance', 'DRREDD': 'Pharma', 'SEQSCI': 'Pharma',
    'JSWENE': 'Power', 'NHPC': 'Power', 'NTPC': 'Power', 'NTPGRE': 'Power', 'SJVLIM': 'Power', 'TATPOW': 'Power',
    'GAIL': 'Oil & Gas', 'GUJGA': 'Oil & Gas', 'HINPET': 'Oil & Gas', 'ONGC': 'Oil & Gas', 'PETLNG': 'Oil & Gas', 'RELIND': 'Oil & Gas',
    'IDECEL': 'Telecom',
    'ICIGOL': 'Commodities', 'ICIPSE': 'Commodities',
    'ICINIF': 'Broad Market', 'HDF250': 'Broad Market', 'MIR150': 'Broad Market',
}

FINANCIALS_SECTORS = ("Banking", "Financial Services", "Insurance")

# NSE price bands cap a single session's move far below 2.5x, so a bigger
# day-over-day jump in Yahoo history is an unadjusted split/bonus/consolidation.
SPLIT_JUMP_RATIO = 2.5


def adjust_unadjusted_splits(history: pd.DataFrame) -> pd.DataFrame:
    """Rescale bars before any implausible one-day jump onto the latest basis."""
    if history.empty or "Close" not in history.columns:
        return history
    adjusted = history.copy()
    price_cols = [c for c in ("Open", "High", "Low", "Close") if c in adjusted.columns]
    close = adjusted["Close"]
    ratios = close / close.shift(1)
    jumps = ratios[(ratios > SPLIT_JUMP_RATIO) | (ratios < 1 / SPLIT_JUMP_RATIO)].dropna()
    for jump_label, ratio in jumps.items():
        position = adjusted.index.get_loc(jump_label)
        adjusted.iloc[:position, [adjusted.columns.get_loc(c) for c in price_cols]] *= ratio
    return adjusted


def fetch_market_data(yf_ticker: str) -> dict:
    """Price, 50/200 DMA, 14-day ATR, 52-week High and ROE for one ticker; failures are tagged."""
    result = {"price": None, "dma_50": None, "dma_200": None, "atr": None, "roe": None, "high_52w": None, "trend_override": None}
    if yf_ticker in ('UNLISTED', 'TODO_VERIFY'):
        result["trend_override"] = "NO_TICKER"
        return result
    try:
        ticker_obj = yf.Ticker(yf_ticker)

        # Fundamental Agent
        info = ticker_obj.info or {}
        result["roe"] = info.get('returnOnEquity')

        # Momentum Agent
        data = ticker_obj.history(period="1y")
        if data.empty or "Close" not in data.columns:
            result["trend_override"] = "NO_DATA"
            return result
        data = adjust_unadjusted_splits(data[data["Close"].notna()])
        clean_close = data["Close"]
        if len(clean_close) < 200:
            result["trend_override"] = "NO_DATA"
            return result
        result["price"] = float(clean_close.iloc[-1])
        result["dma_50"] = float(clean_close.rolling(window=50).mean().iloc[-1])
        result["dma_200"] = float(clean_close.rolling(window=200).mean().iloc[-1])
        if "High" in data.columns and not data["High"].dropna().empty:
            result["high_52w"] = float(data["High"].max())
        else:
            result["high_52w"] = float(clean_close.max())
        if {"High", "Low"}.issubset(data.columns):
            atr_series = compute_atr(data.rename(columns={"High": "high", "Low": "low", "Close": "close"}))
            if not atr_series.empty and pd.notna(atr_series.iloc[-1]):
                result["atr"] = float(atr_series.iloc[-1])
    except Exception as exc:
        result["trend_override"] = "FETCH_ERROR"
        print(f"[warn] ({yf_ticker}) {type(exc).__name__}: {exc}")
    return result


def price_data_issue(
    live_price: Optional[float],
    dma_200: Optional[float],
    broker_price: Optional[float],
    config: RiskConfig = RISK_CONFIG,
) -> Optional[str]:
    """Why the fetched price can't be trusted, or None if it passes the checks."""
    if live_price is None or live_price <= 0:
        return None
    if broker_price is not None and pd.notna(broker_price) and broker_price > 0:
        gap_pct = (live_price / broker_price - 1) * 100
        if abs(gap_pct) > config.price_mismatch_pct:
            return (
                f"Live price ₹{live_price:.2f} differs from broker price ₹{broker_price:.2f} "
                f"by {gap_pct:+.1f}% (limit ±{config.price_mismatch_pct:.0f}%); check ticker or corporate action."
            )
    if dma_200 is not None and dma_200 > 0:
        ratio = live_price / dma_200
        limit = config.max_price_to_dma_ratio
        if ratio > limit or ratio < 1 / limit:
            return (
                f"Price ₹{live_price:.2f} is {ratio:.2f}x its 200 DMA ₹{dma_200:.2f}; "
                "price history looks broken (ticker or unadjusted corporate action)."
            )
    return None


@dataclass
class _Holding:
    asset_type: str
    market_value: float


@dataclass
class _PortfolioView:
    """Read-only portfolio snapshot satisfying risk_manager.PortfolioLike."""
    holdings: Mapping[str, _Holding]
    sector_weights: Mapping[str, float]
    equity: float

    @property
    def total_equity(self) -> float:
        return self.equity

    def exposure_by_sector(self) -> dict[str, float]:
        return dict(self.sector_weights)


def size_action(
    eval_res,
    qty: float,
    price: float,
    total_value: float,
    stock_weight: float,
    sector: str,
    sector_weight: float,
    atr_value: Optional[float],
    risk_manager: RiskManager,
    symbol: str,
    config: RiskConfig = RISK_CONFIG,
) -> str:
    """Turn the decision's action into share counts the user can execute."""
    action = eval_res.recommended_action
    decision = eval_res.decision

    if decision == "TRIM":
        shares = trim_quantity(qty, price, total_value, config.max_position_pct)
        if sector_weight > config.max_sector_pct:
            target_weight = max(0.0, stock_weight - (sector_weight - config.max_sector_pct))
            shares = max(shares, trim_quantity(qty, price, total_value, target_weight))
        if eval_res.is_overextended:
            shares = max(shares, math.ceil(qty * config.overextension_trim_fraction))
        if getattr(eval_res, "trailing_stop_hit", False):
            shares = max(shares, math.ceil(qty * 0.5))
        shares = int(min(shares, qty))
        if shares <= 0:
            return action
        new_weight = (qty - shares) * price / total_value * 100
        return f"Trim {shares} sh (~₹{shares * price:,.0f}) → {new_weight:.1f}% weight"

    if decision == "SELL":
        return f"Exit all {int(qty)} sh (~₹{qty * price:,.0f})"

    if decision in ("ACCUMULATE", "BUY"):
        if atr_value is None or atr_value <= 0:
            return f"{action} — size manually (ATR unavailable)"
        sizing = risk_manager.size_position(
            symbol, price, atr_value, sector, current_position_value=qty * price
        )
        if not sizing.approved:
            return f"{action} — no size: {sizing.reason}"
        shares = sizing.quantity
        if action == "Add on weakness (small)":
            shares = max(1, shares // 2)
        return (
            f"{action}: buy {shares} sh (~₹{shares * price:,.0f}), "
            f"stop ₹{sizing.stop_price:.2f}, target ₹{sizing.target_price:.2f}"
        )

    return action


def send_telegram_notification(summary_msg: str) -> bool:
    """
    Sends a summary notification to Telegram using bot token and chat ID
    from environment variables or local credentials env files.
    Redacts all secrets in logs.
    """
    import json
    import urllib.request
    
    token = os.environ.get("TELEGRAM_BOT_TOKEN") or os.environ.get("TELEGRAM_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID") or os.environ.get("TELEGRAM_TO") or os.environ.get("CHAT_ID")

    # If missing in env, search known local credential file locations
    if token:
        token = token.strip()
        if token.startswith("bot"):
            token = token[3:]
    if chat_id:
        chat_id = str(chat_id).strip()

    if not token or not chat_id:
        env_paths = [
            "/home/user/projects/retained_credentials_and_data/Telegram_Credentials.env",
            os.path.join(os.path.dirname(__file__), "..", "retained_credentials_and_data", "Telegram_Credentials.env"),
            os.path.join(os.path.dirname(__file__), "Telegram_Credentials.env"),
            os.path.join(os.path.dirname(__file__), ".env"),
        ]
        for path in env_paths:
            if os.path.exists(path):
                try:
                    with open(path, "r") as f:
                        for line in f:
                            line = line.strip()
                            if line and not line.startswith("#") and "=" in line:
                                k, v = line.split("=", 1)
                                k, v = k.strip(), v.strip().strip("'\"")
                                if k in ("TELEGRAM_BOT_TOKEN", "TELEGRAM_TOKEN") and not token:
                                    token = v
                                elif k in ("TELEGRAM_CHAT_ID", "TELEGRAM_TO", "CHAT_ID") and not chat_id:
                                    chat_id = v
                except Exception as exc:
                    print(f"[warn] Error reading credential file {path}: {type(exc).__name__}")

    if not token or not chat_id:
        print("[info] Telegram credentials not configured. Skipping outbound message.")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": summary_msg,
        "parse_mode": "HTML",
    }
    
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as response:
            print("[info] Telegram notification dispatched successfully.")
            return True
    except Exception as exc:
        print(f"[warn] Telegram dispatch failed: {type(exc).__name__}: {exc}")
        return False


def run_weekly_analysis(notify_fn=send_telegram_notification):
    portfolio_file = "portfolio.csv"
    tracking_file = "re-engineering.csv"
    thesis_file = "thesis.csv"

    if not os.path.exists(portfolio_file):
        return

    df = pd.read_csv(portfolio_file)
    df.columns = df.columns.str.strip()

    # --- LOAD THESIS DATA ---
    thesis_dict = {}
    if os.path.exists(thesis_file):
        try:
            thesis_df = pd.read_csv(thesis_file)
            thesis_df.columns = thesis_df.columns.str.strip()
            for _, t_row in thesis_df.iterrows():
                sym = str(t_row.get("Stock Symbol", "")).strip()
                if sym:
                    thesis_dict[sym] = {
                        "thesis": str(t_row.get("Thesis", "NOT YET SET")).strip(),
                        "conviction": t_row.get("Conviction"),
                        # Invalidation_Price is anchored to Avg_Cost at entry and does not adjust for unrealized gains — it is a thesis-broken trigger, not a trailing profit-protection stop.
                        "invalidation_price": t_row.get("Invalidation_Price"),
                    }
        except Exception as exc:
            print(f"[warn] Error reading thesis file {thesis_file}: {exc}")

    # --- LOAD HISTORICAL DECISIONS FOR EVENT-DRIVEN ALERTING ---
    last_decisions = {}
    if os.path.exists(tracking_file):
        try:
            hist_df = pd.read_csv(tracking_file)
            if not hist_df.empty and "Stock_Symbol" in hist_df.columns:
                if "Decision" in hist_df.columns:
                    last_decisions = hist_df.groupby("Stock_Symbol")["Decision"].last().dropna().to_dict()
                elif "Model_Signal" in hist_df.columns:
                    raw_sigs = hist_df.groupby("Stock_Symbol")["Model_Signal"].last().to_dict()
                    for sym, sig in raw_sigs.items():
                        if pd.notna(sig):
                            s_str = str(sig).strip()
                            if "NO THESIS" in s_str:
                                last_decisions[sym] = "NO THESIS"
                            elif "NO DATA" in s_str:
                                last_decisions[sym] = "NO DATA"
                            elif "STRG SELL" in s_str:
                                last_decisions[sym] = "SELL"
                            elif "ACCUMULATE" in s_str:
                                last_decisions[sym] = "ACCUMULATE"
                            elif "TRIM" in s_str:
                                last_decisions[sym] = "TRIM"
                            else:
                                last_decisions[sym] = "HOLD"
        except Exception as exc:
            print(f"[warn] Error reading historical signals from {tracking_file}: {exc}")

    run_type = os.environ.get("RUN_TYPE", "incremental").strip().lower()
    is_full_review = (run_type == "full")

    # --- AGENT 1: MARKET DATA + PRICE SANITY CHECKS ---
    df['Stock Symbol'] = df['Stock Symbol'].astype(str).str.strip()
    market = {}
    for _, row in df.iterrows():
        broker_symbol = row["Stock Symbol"]
        md = fetch_market_data(TICKER_MAP.get(broker_symbol, f"{broker_symbol}.NS"))
        md["issue"] = None
        if md["trend_override"] is None:
            md["issue"] = price_data_issue(md["price"], md["dma_200"], row["Current Market Price"])
            if md["issue"]:
                print(f"[warn] {broker_symbol}: {md['issue']}")
        market[broker_symbol] = md

    # --- AGENT 2: RISK & ALLOCATION PRE-COMPUTATION ---
    # Weights use the same price the decision uses: the live price when it is
    # trustworthy, otherwise the broker price from portfolio.csv.
    def _valuation_price(row):
        md = market[row["Stock Symbol"]]
        if md["trend_override"] is None and md["issue"] is None and md["price"] is not None:
            return md["price"]
        return row["Current Market Price"]

    df['Sector'] = df['Stock Symbol'].map(SECTOR_MAP).fillna('Other ETFs/Misc')
    df['Valuation_Price'] = df.apply(_valuation_price, axis=1)
    df['Current_Value'] = df['Qty'] * df['Valuation_Price']
    total_portfolio_value = df['Current_Value'].sum()
    df['Weight_%'] = (df['Current_Value'] / total_portfolio_value) * 100

    sector_allocations = df.groupby('Sector')['Weight_%'].sum().to_dict()
    financials_total = sum(sector_allocations.get(s, 0.0) for s in FINANCIALS_SECTORS)
    risk_group_exposures = lookthrough.calculate_risk_group_exposures(df, RISK_GROUPS)
    risk_manager = RiskManager(
        _PortfolioView(
            holdings={
                r["Stock Symbol"]: _Holding("equity", r["Current_Value"]) for _, r in df.iterrows()
            },
            sector_weights=sector_allocations,
            equity=total_portfolio_value,
        ),
        RISK_CONFIG,
    )

    analysis_results = []
    tracking_rows = []
    telegram_lines = []
    now_ist = datetime.now(ZoneInfo("Asia/Kolkata"))
    date_str = now_ist.strftime("%Y-%m-%d")
    run_timestamp_ist = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    for _, row in df.iterrows():
        broker_symbol = row["Stock Symbol"]
        qty = row["Qty"]
        avg_cost = row["Average Cost Price"]
        csv_current_price = row["Current Market Price"]
        valuation_price = row["Valuation_Price"]
        stock_weight = row["Weight_%"]
        stock_sector = row["Sector"]

        md = market[broker_symbol]
        current_price = md["price"]
        dma_50 = md["dma_50"]
        dma_200 = md["dma_200"]
        roe = md["roe"]
        technical_trend_override = md["trend_override"]

        # --- EXECUTIVE COORDINATOR ENGINE ---
        if stock_sector in FINANCIALS_SECTORS:
            sector_risk_exposure = financials_total
        else:
            sector_risk_exposure = sector_allocations.get(stock_sector, 0)

        sym_rgs = [g for g, mems in RISK_GROUPS.items() if broker_symbol in mems]
        stock_rg_exposure = max([risk_group_exposures[g]["exposure_pct"] for g in sym_rgs], default=0.0)
        total_return = ((valuation_price - avg_cost) / avg_cost) * 100
        return_emoji = "📈" if total_return >= 0 else "📉"

        t_info = thesis_dict.get(broker_symbol, {})
        raw_thesis = t_info.get("thesis")
        t_text = str(raw_thesis).strip() if (raw_thesis is not None and pd.notna(raw_thesis) and str(raw_thesis).strip()) else "NOT YET SET"
        t_conv = t_info.get("conviction")
        t_inv = t_info.get("invalidation_price")

        conviction_val = None
        if t_conv is not None and not pd.isna(t_conv) and str(t_conv).strip() != "":
            s_conv = str(t_conv).strip()
            try:
                conviction_val = float(s_conv)
            except ValueError:
                match = re.search(r"(\d+(?:\.\d+)?)", s_conv)
                if match:
                    try:
                        conviction_val = float(match.group(1))
                    except ValueError:
                        conviction_val = None

        inv_price_val = None
        if t_inv is not None and not pd.isna(t_inv) and str(t_inv).strip() != "":
            try:
                inv_price_val = float(t_inv)
            except ValueError:
                inv_price_val = None

        eval_res = evaluate_signal(
            current_price=current_price,
            dma_50=dma_50,
            dma_200=dma_200,
            roe=roe,
            stock_sector=stock_sector,
            sector_risk_exposure=sector_risk_exposure,
            technical_trend_override=technical_trend_override,
            total_return=total_return,
            thesis_text=t_text,
            conviction=conviction_val,
            invalidation_price=inv_price_val,
            stock_weight=stock_weight,
            config=RISK_CONFIG,
            fallback_price=csv_current_price,
            data_issue=md["issue"],
            high_52w=md.get("high_52w"),
            atr=md.get("atr"),
            risk_group_exposure=stock_rg_exposure,
        )
        signal = eval_res.signal
        recommended_action = size_action(
            eval_res,
            qty=qty,
            price=valuation_price,
            total_value=total_portfolio_value,
            stock_weight=stock_weight,
            sector=stock_sector,
            sector_weight=sector_risk_exposure,
            atr_value=md["atr"],
            risk_manager=risk_manager,
            symbol=broker_symbol,
        )
        explanation = eval_res.explanation
        thesis_status = eval_res.thesis_status
        conviction_disp = str(int(eval_res.conviction)) if eval_res.conviction is not None else ""
        technical_trend = eval_res.technical_trend
        decision = eval_res.decision
        horizon_short_term = eval_res.horizon_short_term
        horizon_long_term = eval_res.horizon_long_term
        rationale = eval_res.rationale
        data_status = eval_res.data_status

        # Save to Main Display DataFrame
        ts_val = eval_res.trailing_stop
        ts_str = f"₹{ts_val:.2f}" if ts_val is not None else "N/A"
        analysis_results.append({
            "_weight": stock_weight,
            "Symbol": broker_symbol,
            "Sector": stock_sector,
            "Weight": f"{stock_weight:.1f}%",
            "Total Return": f"{total_return:+.2f}%",
            "Trailing Stop": ts_str,
            "Decision": decision,
            "Action": recommended_action,
            "Reasoning": rationale,
            "Thesis Status": thesis_status,
            "Conviction": conviction_disp
        })

        # --- LOG TO HISTORY TRACKING ARRAY ---
        if technical_trend in DATA_FAILURE_TRENDS:
            log_price = None
            log_dma_50 = None
            log_dma_200 = None
            log_roe = None
        else:
            log_price = round(current_price, 2) if current_price is not None else None
            log_dma_50 = round(dma_50, 2) if dma_50 is not None else None
            log_dma_200 = round(dma_200, 2) if dma_200 is not None else None
            log_roe = round(roe, 4) if roe is not None else None

        tracking_rows.append({
            "Analysis_Date": date_str,
            "Stock_Symbol": broker_symbol,
            "Price_At_Signal": log_price,
            "Model_Signal": signal,
            "Trigger_Reason": explanation,
            "run_timestamp_ist": run_timestamp_ist,
            "current_price": log_price,
            "dma_50": log_dma_50,
            "dma_200": log_dma_200,
            "roe": log_roe,
            "portfolio_weight_pct": round(stock_weight, 2),
            "sector": stock_sector,
            "technical_trend": technical_trend,
            "Recommended_Action": recommended_action,
            "Thesis_Status": thesis_status,
            "Conviction": conviction_disp,
            "Decision": decision,
            "Horizon_Short_Term": horizon_short_term,
            "Horizon_Long_Term": horizon_long_term,
            "Rationale": rationale,
            "Data_Status": data_status,
        })

        # --- EVENT-DRIVEN ALERT QUALIFICATION (KEYED ON DECISION) ---
        last_dec = last_decisions.get(broker_symbol)
        decision_changed = (last_dec != decision)
        crossed_into_alert = (
            decision in ("SELL", "TRIM")
            and last_dec not in ("SELL", "TRIM")
        )

        if is_full_review or decision_changed or crossed_into_alert:
            emoji_map = {
                "ACCUMULATE": "🟢",
                "BUY": "🟢",
                "HOLD": "🟡",
                "TRIM": "✂️",
                "SELL": "🔴",
                "NO THESIS": "⚠️",
                "NO DATA": "⚪",
                "VERIFY DATA": "⚪",
            }
            dec_emoji = emoji_map.get(decision, "📊")
            safe_dec = html.escape(str(decision))
            safe_sym = html.escape(str(broker_symbol))
            safe_short = html.escape(str(horizon_short_term))
            safe_long = html.escape(str(horizon_long_term))
            safe_rat = html.escape(str(rationale))
            safe_act = html.escape(str(recommended_action))
            telegram_lines.append(
                f"{dec_emoji} <b>{safe_dec}</b> | <b>{safe_sym}</b> ({stock_weight:.1f}%) | {return_emoji}{total_return:+.1f}%\n"
                f"• Action: {safe_act}\n"
                f"• Short: {safe_short}\n"
                f"• Long: {safe_long}\n"
                f"• Rationale: {safe_rat}"
            )

    # --- COMPILING THE HISTORICAL TIME SERIES RECORD ---
    new_log_df = pd.DataFrame(tracking_rows)
    if os.path.exists(tracking_file):
        existing_df = pd.read_csv(tracking_file)
        if list(existing_df.columns) != list(new_log_df.columns):
            existing_df = existing_df.reindex(columns=new_log_df.columns)
            combined_df = pd.concat([existing_df, new_log_df], ignore_index=True)
            combined_df.to_csv(tracking_file, index=False)
        else:
            new_log_df.to_csv(tracking_file, mode='a', index=False, header=False)
    else:
        new_log_df.to_csv(tracking_file, mode='w', index=False, header=True)

    # Output rendering logs
    report_df = (
        pd.DataFrame(analysis_results)
        .sort_values(by="_weight", ascending=False)
        .drop(columns="_weight")
    )
    sector_summary_md = "\n### Sector Concentration Metrics\n"
    for sec, w in sorted(sector_allocations.items(), key=lambda x: x[1], reverse=True):
        sector_summary_md += f"* **{sec}**: {w:.1f}%\n"
    sector_summary_md += f"* **Financials (combined)**: {financials_total:.1f}%\n"

    # Consolidation section: holdings <1% weight with conviction <5
    consolidation_candidates = []
    for _, row in df.iterrows():
        sym = row["Stock Symbol"]
        w = row["Weight_%"]
        qty = row["Qty"]
        px = row["Valuation_Price"]
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
        if w < 1.0 and (conv_val is None or conv_val < 5.0):
            conv_disp = str(int(conv_val)) if conv_val is not None else "N/A"
            consolidation_candidates.append({
                "_weight": w,
                "Symbol": sym,
                "Sector": row["Sector"],
                "Weight": f"{w:.1f}%",
                "Conviction": conv_disp,
                "Shares to Exit": f"Exit all {int(qty)} sh (~₹{qty * px:,.0f})",
            })

    consolidation_md = "\n### Portfolio Consolidation\n"
    consolidation_md += (
        f"Portfolio holds {len(df)} positions versus target maximum of "
        f"{RISK_CONFIG.max_open_positions} (`config.max_open_positions`). "
        f"The following {len(consolidation_candidates)} holdings are under 1.0% portfolio weight "
        "with conviction below 5 and are candidates for consolidation/exit:\n\n"
    )
    if consolidation_candidates:
        consol_df = (
            pd.DataFrame(consolidation_candidates)
            .sort_values(by="_weight", ascending=True)
            .drop(columns="_weight")
        )
        consolidation_md += consol_df.to_markdown(index=False) + "\n"
    else:
        consolidation_md += "No holdings currently qualify as consolidation candidates.\n"

    # --- PERFORMANCE SECTION (XIRR vs BENCHMARK) ---
    perf_md = ""
    if os.path.exists("trades.csv"):
        try:
            import performance
            trades_df = pd.read_csv("trades.csv")
            perf_res = performance.calculate_portfolio_and_benchmark_xirr(
                trades_df=trades_df,
                portfolio_df=df,
                current_prices={row["Stock Symbol"]: row["Valuation_Price"] for _, row in df.iterrows()},
            )
            perf_md = performance.format_performance_markdown(perf_res) + "\n"
        except Exception as exc:
            print(f"[warn] Performance computation failed: {exc}")

    # --- ETF LOOK-THROUGH & RISK FACTOR GROUPS ---
    try:
        effective_df = lookthrough.calculate_effective_weights(df)
        lookthrough_md = lookthrough.format_lookthrough_and_risk_groups_markdown(effective_df, risk_group_exposures)
    except Exception as exc:
        print(f"[warn] Look-through computation failed: {exc}")
        lookthrough_md = ""

    markdown_output = (
        f"# Orchestrated Multi-Agent Portfolio Audit - {date_str}\n\n"
        + perf_md
        + f"### Asset Health Assessment\n{report_df.to_markdown(index=False)}\n"
        + sector_summary_md
        + lookthrough_md
        + consolidation_md
    )



    with open("README.md", "w") as f:
        f.write(markdown_output)

    # Dispatch Telegram Notification Only If Qualifying Changes Exist
    if telegram_lines:
        header_title = f"🛡️ Multi-Agent Portfolio Matrix ({date_str})"
        if is_full_review:
            header_title += " [FULL REVIEW]"
        
        chunks = []
        current_chunk = [f"<b>{header_title}</b>\n"]
        current_len = len(current_chunk[0])
        
        for line in telegram_lines:
            if current_len + len(line) + 2 > 3800:
                chunks.append("\n".join(current_chunk))
                current_chunk = [f"<b>{header_title} (Cont.)</b>\n", line]
                current_len = len(current_chunk[0]) + len(line) + 1
            else:
                current_chunk.append(line)
                current_len += len(line) + 1
        if current_chunk:
            chunks.append("\n".join(current_chunk))

        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a") as env_file:
                env_file.write("TELEGRAM_SUMMARY<<EOF\n")
                env_file.write(chunks[0] + "\n")
                env_file.write("EOF\n")

        if notify_fn is not None:
            for chunk in chunks:
                notify_fn(chunk)
    else:
        print("[info] Incremental run with 0 qualifying signal changes. Telegram alert suppressed.")
        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a") as env_file:
                env_file.write("TELEGRAM_SUMMARY<<EOF\nEOF\n")

if __name__ == "__main__":
    run_weekly_analysis()


