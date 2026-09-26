import os
import re
from datetime import datetime
from zoneinfo import ZoneInfo
import pandas as pd
import yfinance as yf

from config import RISK_CONFIG
from signal_engine import evaluate_signal

# Fully vetted Exchange Tickers mapping
TICKER_MAP = {
    'ASHLEY': 'ASHOKLEY.NS', 'FEDBAN': 'FEDERALBNK.NS', 'HDFBAN': 'HDFCBANK.NS',
    'HDF250': 'HDFCSML250.NS', 'ICIGOL': 'GOLDIETF.NS', 'ICINIF': 'NIFTYIETF.NS',
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
    'IDECEL': 'Telecom'
}

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
                        "invalidation_price": t_row.get("Invalidation_Price"),
                    }
        except Exception as exc:
            print(f"[warn] Error reading thesis file {thesis_file}: {exc}")

    # --- LOAD HISTORICAL SIGNALS FOR EVENT-DRIVEN ALERTING ---
    last_signals = {}
    if os.path.exists(tracking_file):
        try:
            hist_df = pd.read_csv(tracking_file)
            if not hist_df.empty and "Stock_Symbol" in hist_df.columns and "Model_Signal" in hist_df.columns:
                last_signals = hist_df.groupby("Stock_Symbol")["Model_Signal"].last().to_dict()
        except Exception as exc:
            print(f"[warn] Error reading historical signals from {tracking_file}: {exc}")

    run_type = os.environ.get("RUN_TYPE", "incremental").strip().lower()
    is_full_review = (run_type == "full")

    # --- AGENT 1: RISK & ALLOCATION PRE-COMPUTATION ---
    df['Sector'] = df['Stock Symbol'].str.strip().map(SECTOR_MAP).fillna('Other ETFs/Misc')
    df['Current_Value'] = df['Qty'] * df['Current Market Price']
    total_portfolio_value = df['Current_Value'].sum()
    df['Weight_%'] = (df['Current_Value'] / total_portfolio_value) * 100
    
    sector_allocations = df.groupby('Sector')['Weight_%'].sum().to_dict()

    analysis_results = []
    tracking_rows = []
    telegram_lines = []
    now_ist = datetime.now(ZoneInfo("Asia/Kolkata"))
    date_str = now_ist.strftime("%Y-%m-%d")
    run_timestamp_ist = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    for _, row in df.iterrows():
        broker_symbol = str(row["Stock Symbol"]).strip()
        company_name = row["Company Name"]
        qty = row["Qty"]
        avg_cost = row["Average Cost Price"]
        csv_current_price = row["Current Market Price"]
        stock_weight = row["Weight_%"]
        stock_sector = row["Sector"]

        yf_ticker = TICKER_MAP.get(broker_symbol, f"{broker_symbol}.NS")
        current_price = None
        dma_50 = None
        dma_200 = None
        roe = None
        technical_trend_override = None

        if yf_ticker not in ('UNLISTED', 'TODO_VERIFY'):
            try:
                ticker_obj = yf.Ticker(yf_ticker)

                # Fundamental Agent
                info = ticker_obj.info or {}
                roe = info.get('returnOnEquity')

                # Momentum Agent
                data = ticker_obj.history(period="1y")
                clean_close = data["Close"].dropna() if not data.empty and "Close" in data.columns else pd.Series(dtype=float)
                if not clean_close.empty and len(clean_close) >= 200:
                    current_price = float(clean_close.iloc[-1])
                    dma_50 = float(clean_close.rolling(window=50).mean().iloc[-1])
                    dma_200 = float(clean_close.rolling(window=200).mean().iloc[-1])
                else:
                    technical_trend_override = "NO_DATA"
            except Exception as exc:
                technical_trend_override = "FETCH_ERROR"
                print(
                    f"[warn] {broker_symbol} ({yf_ticker}) "
                    f"{type(exc).__name__}: {exc}"
                )
        else:
            technical_trend_override = "NO_TICKER"

        # --- EXECUTIVE COORDINATOR ENGINE ---
        sector_risk_exposure = sector_allocations.get(stock_sector, 0)
        display_price = current_price if current_price is not None else csv_current_price
        total_return = ((display_price - avg_cost) / avg_cost) * 100
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
            config=RISK_CONFIG,
        )
        signal = eval_res.signal
        recommended_action = eval_res.recommended_action
        explanation = eval_res.explanation
        thesis_status = eval_res.thesis_status
        conviction_disp = str(int(eval_res.conviction)) if eval_res.conviction is not None else ""
        technical_trend = eval_res.technical_trend

        # Save to Main Display DataFrame
        analysis_results.append({
            "Symbol": broker_symbol,
            "Sector": stock_sector,
            "Weight": f"{stock_weight:.1f}%",
            "Total Return": f"{total_return:+.2f}%",
            "Signal": signal,
            "Recommended Action": recommended_action,
            "Reasoning": explanation,
            "Thesis Status": thesis_status,
            "Conviction": conviction_disp
        })

        # --- LOG TO HISTORY TRACKING ARRAY ---
        if technical_trend in ("NO_DATA", "FETCH_ERROR", "NO_TICKER"):
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
            "Conviction": conviction_disp
        })

        # --- EVENT-DRIVEN ALERT QUALIFICATION ---
        last_sig = last_signals.get(broker_symbol)
        signal_changed = (last_sig != signal)
        crossed_into_alert = (
            signal in ("⚠️ NO THESIS", "🔴 STRG SELL")
            and last_sig not in ("⚠️ NO THESIS", "🔴 STRG SELL")
        )

        if is_full_review or signal_changed or crossed_into_alert:
            telegram_lines.append(
                f"{signal} | {broker_symbol} ({stock_weight:.1f}%) | {return_emoji}{total_return:+.1f}% | Action: {recommended_action}"
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
    report_df = pd.DataFrame(analysis_results).sort_values(by="Weight", ascending=False)
    sector_summary_md = "\n### Sector Concentration Metrics\n"
    for sec, w in sorted(sector_allocations.items(), key=lambda x: x[1], reverse=True):
        sector_summary_md += f"* **{sec}**: {w:.1f}%\n"

    markdown_output = f"# Orchestrated Multi-Agent Portfolio Audit - {date_str}\n\n" \
                      f"### Asset Health Assessment\n{report_df.to_markdown(index=False)}\n" + sector_summary_md

    with open("README.md", "w") as f:
        f.write(markdown_output)

    # Dispatch Telegram Notification Only If Qualifying Changes Exist
    if telegram_lines:
        header = f"🛡️ *Multi-Agent Portfolio Matrix ({date_str})*"
        if is_full_review:
            header += " [FULL REVIEW]"
        summary_msg = f"{header}\n\n" + "\n".join(telegram_lines[:18])
        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a") as env_file:
                env_file.write("TELEGRAM_SUMMARY<<EOF\n")
                env_file.write(summary_msg + "\n")
                env_file.write("EOF\n")

        summary_msg_html = f"<b>{header}</b>\n\n" + "\n".join(telegram_lines[:18])
        if notify_fn is not None:
            notify_fn(summary_msg_html)
    else:
        print("[info] Incremental run with 0 qualifying signal changes. Telegram alert suppressed.")
        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a") as env_file:
                env_file.write("TELEGRAM_SUMMARY<<EOF\nEOF\n")

if __name__ == "__main__":
    run_weekly_analysis()


