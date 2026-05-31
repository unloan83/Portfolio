import os
from datetime import datetime
import pandas as pd
import yfinance as yf

# Fully vetted Exchange Tickers mapping
TICKER_MAP = {
    'ASHLEY': 'ASHOKLEY.NS', 'FEDBAN': 'FEDERALBNK.NS', 'HDFBAN': 'HDFCBANK.NS',
    'HDF250': 'HDFCSML250.NS', 'ICIGOL': 'GOLDBEES.NS', 'ICINIF': 'ICICINIFTY.NS',   
    'ICIPSE': 'SILVERBEES.NS', 'NIPNIT': 'NIFTYIETF.NS', 'MIR150': 'MOMENTUM.NS',     
    'BHAELE': 'BEL.NS', 'TATGLO': 'TATACONSUM.NS', 'JIOFIN': 'JIOFIN.NS',
    'WIPRO': 'WIPRO.NS', 'ENGIND': 'ENGINERSIN.NS', 'LIC': 'LICI.NS',
    'DRREDD': 'DRREDDY.NS', 'SEQSCI': 'STAR.NS', 'JSWENE': 'JSWENERGY.NS',
    'NHPC': 'NHPC.NS', 'NTPC': 'NTPC.NS', 'NTPGRE': 'NTPCGREEN.NS',
    'SJVLIM': 'SJVN.NS', 'TATPOW': 'TATAPOWER.NS', 'GAIL': 'GAIL.NS',
    'GUJGA': 'GUJGASLTD.NS', 'HINPET': 'HINDPETRO.NS', 'ONGC': 'ONGC.NS',
    'PETLNG': 'PETRONET.NS', 'RELIND': 'RELIANCE.NS', 'GUJPPL': 'GPPL.NS',
    'IDECEL': 'IDEA.NS', 'TATCAP': 'UNLISTED', 'LGELEC': 'UNLISTED'
}

# Explicit sector definitions to track concentration rules
SECTOR_MAP = {
    'ASHLEY': 'Auto', 'TATGLO': 'Consumption', 'LGELEC': 'Consumer Electronics',
    'FEDBAN': 'Banking', 'HDFBAN': 'Banking', 'JIOFIN': 'Financial Services', 'TATCAP': 'Financial Services',
    'WIPRO': 'IT', 'NIPNIT': 'IT',
    'BHAELE': 'Defense', 'ENGIND': 'Infrastructure', 'GUJPPL': 'Infrastructure',
    'LIC': 'Insurance', 'DRREDD': 'Pharma', 'SEQSCI': 'Pharma',
    'JSWENE': 'Power', 'NHPC': 'Power', 'NTPC': 'Power', 'NTPGRE': 'Power', 'SJVLIM': 'Power', 'TATPOW': 'Power',
    'GAIL': 'Oil & Gas', 'GUJGA': 'Oil & Gas', 'HINPET': 'Oil & Gas', 'ONGC': 'Oil & Gas', 'PETLNG': 'Oil & Gas', 'RELIND': 'Oil & Gas',
    'IDECEL': 'Telecom'
}

def run_weekly_analysis():
    portfolio_file = "portfolio.csv"
    tracking_file = "re-engineering.csv"
    if not os.path.exists(portfolio_file):
        return

    df = pd.read_csv(portfolio_file)
    df.columns = df.columns.str.strip()

    # --- AGENT 1: RISK & ALLOCATION PRE-COMPUTATION ---
    df['Sector'] = df['Stock Symbol'].str.strip().map(SECTOR_MAP).fillna('Other ETFs/Misc')
    df['Current_Value'] = df['Qty'] * df['Current Market Price']
    total_portfolio_value = df['Current_Value'].sum()
    df['Weight_%'] = (df['Current_Value'] / total_portfolio_value) * 100
    
    sector_allocations = df.groupby('Sector')['Weight_%'].sum().to_dict()

    analysis_results = []
    tracking_rows = []
    telegram_lines = []
    date_str = datetime.now().strftime("%Y-%m-%d")

    for _, row in df.iterrows():
        broker_symbol = str(row["Stock Symbol"]).strip()
        company_name = row["Company Name"]
        qty = row["Qty"]
        avg_cost = row["Average Cost Price"]
        csv_current_price = row["Current Market Price"]
        stock_weight = row["Weight_%"]
        stock_sector = row["Sector"]

        yf_ticker = TICKER_MAP.get(broker_symbol, f"{broker_symbol}.NS")
        current_price = csv_current_price
        
        fundamental_pass = True
        technical_trend = "NEUTRAL"
        is_overextended = False
        
        if yf_ticker != 'UNLISTED':
            try:
                ticker_obj = yf.Ticker(yf_ticker)
                
                # Fundamental Agent
                info = ticker_obj.info
                roe = info.get('returnOnEquity', 0.15)
                if roe is not None and roe < 0.10: 
                    fundamental_pass = False 
                
                # Momentum Agent
                data = ticker_obj.history(period="1y")
                if not data.empty and len(data) >= 200:
                    current_price = data["Close"].iloc[-1]
                    dma_50 = data["Close"].rolling(window=50).mean().iloc[-1]
                    dma_200 = data["Close"].rolling(window=200).mean().iloc[-1]

                    if current_price < dma_200:
                        technical_trend = "BEARISH"
                    elif current_price > dma_50 and dma_50 > dma_200:
                        technical_trend = "BULLISH"
                        if current_price > (dma_50 * 1.25):
                            is_overextended = True
            except Exception:
                pass

        # --- EXECUTIVE COORDINATOR ENGINE ---
        sector_risk_exposure = sector_allocations.get(stock_sector, 0)
        total_return = ((current_price - avg_cost) / avg_cost) * 100
        return_emoji = "📈" if total_return >= 0 else "📉"

        if technical_trend == "BEARISH":
            signal = "🔴 STRG SELL"
            explanation = "Below 200 DMA structural breakdown."
        elif is_overextended:
            signal = "🟡 HOLD / PEAK"
            explanation = "Overextended >25% above 50 DMA."
        elif not fundamental_pass:
            signal = "🟡 HOLD / RISK"
            explanation = "Weak operational efficiency ROE < 10%."
        elif sector_risk_exposure > 25.0:
            signal = "⚠️ SECTOR CAP"
            explanation = f"{stock_sector} cluster concentration danger ({sector_risk_exposure:.1f}%)."
        elif technical_trend == "BULLISH":
            signal = "🟢 ACCUMULATE"
            explanation = "Healthy structural accumulation channel."
        else:
            signal = "🟡 HOLD"
            explanation = "Sideways consolidation pattern."

        # Save to Main Display DataFrame
        analysis_results.append({
            "Symbol": broker_symbol,
            "Sector": stock_sector,
            "Weight": f"{stock_weight:.1f}%",
            "Total Return": f"{total_return:+.2f}%",
            "Action Signal": signal,
            "Reasoning Matrix": explanation
        })

        # --- LOG TO HISTORY TRACKING ARRAY ---
        tracking_rows.append({
            "Analysis_Date": date_str,
            "Stock_Symbol": broker_symbol,
            "Price_At_Signal": round(current_price, 2),
            "Model_Signal": signal,
            "Trigger_Reason": explanation
        })

        telegram_lines.append(f"{signal} | {broker_symbol} ({stock_weight:.1f}%) | {return_emoji}{total_return:+.1f}%")

    # --- COMPILING THE HISTORICAL TIME SERIES RECORD ---
    new_log_df = pd.DataFrame(tracking_rows)
    if os.path.exists(tracking_file):
        # Append without writing headers if file already exists
        new_log_df.to_csv(tracking_file, mode='a', index=False, header=False)
    else:
        # Create fresh file with schema headers
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

    summary_msg = f"🛡️ *Multi-Agent Portfolio Matrix ({date_str})*\n\n" + "\n".join(telegram_lines[:18])
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as env_file:
            env_file.write("TELEGRAM_SUMMARY<<EOF\n")
            env_file.write(summary_msg + "\n")
            env_file.write("EOF\n")

if __name__ == "__main__":
    run_weekly_analysis()
