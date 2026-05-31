import os
from datetime import datetime
import pandas as pd
import yfinance as yf

# Maps broker codes from portfolio.csv to standard Yahoo Finance symbols
TICKER_MAP = {
    'ASHLEY': 'ASHOKLEY.NS',
    'FEDBAN': 'FEDERALBNK.NS',
    'HDFBAN': 'HDFCBANK.NS',
    'HDF250': 'HDFCSML250.NS',
    
    # --- FIXED ETF TICKERS ---
    'ICIGOL': 'ICICIGOLD.NS',
    'ICINIF': 'ICICINFITY.NS',   # Note the specific Yahoo typo tracking: NFITY instead of NIFTY
    'ICIPSE': 'ICICISLVRE.NS',   # Silver ETF trading key
    'NIPNIT': 'NETFIT.NS',       # Nippon India Nifty IT ETF
    'MIR150': 'MNDF150ETF.NS',   # Mirae Asset Nifty Midcap 150 ETF
    
    # --- FIXED STOCK TICKERS ---
    'BHAELE': 'BEL.NS',
    'TATGLO': 'TATACONSUM.NS',
    'JIOFIN': 'JIOFIN.NS',
    'WIPRO': 'WIPRO.NS',
    'ENGIND': 'ENGINERSIN.NS',
    'LIC': 'LICI.NS',
    'DRREDD': 'DRREDDY.NS',
    'SEQSCI': 'SEQUENT.NS',      # Sequent Scientific Ltd
    'JSWENE': 'JSWENERGY.NS',
    'NHPC': 'NHPC.NS',
    'NTPC': 'NTPC.NS',
    'NTPGRE': 'NTPCGREEN.NS',
    'SJVLIM': 'SJVN.NS',
    'TATPOW': 'TATAPOWER.NS',
    'GAIL': 'GAIL.NS',
    'GUJGA': 'GUJGASLTD.NS',
    'HINPET': 'HINDPETRO.NS',
    'ONGC': 'ONGC.NS',
    'PETLNG': 'PETRONET.NS',
    'RELIND': 'RELIANCE.NS',
    'GUJPPL': 'GPPL.NS',
    'IDECEL': 'IDEA.NS',
    
    # --- UNLISTED / PRIVATE HOLDINGS ---
    # These remain unlisted. The script fallback engine uses your CSV market prices
    'TATCAP': 'UNLISTED',
    'LGELEC': 'UNLISTED'
}
def run_weekly_analysis():
    portfolio_file = "portfolio.csv"
    if not os.path.exists(portfolio_file):
        print("portfolio.csv not found!")
        return

    # Read CSV and clean trailing whitespaces in column names
    df = pd.read_csv(portfolio_file)
    df.columns = df.columns.str.strip()

    analysis_results = []

    for _, row in df.iterrows():
        broker_symbol = str(row["Stock Symbol"]).strip()
        company_name = row["Company Name"]
        qty = row["Qty"]
        avg_cost = row["Average Cost Price"]
        csv_current_price = row["Current Market Price"]

        # Convert broker symbol to Yahoo Finance ticker
        yf_ticker = TICKER_MAP.get(broker_symbol, f"{broker_symbol}.NS")

        current_price = csv_current_price
        signal = "🟡 HOLD (No Live Trend Data)"
        
        try:
            # Pull daily market data for 50/200 DMA metrics
            ticker_obj = yf.Ticker(yf_ticker)
            data = ticker_obj.history(period="1y")
            
            if not data.empty and len(data) >= 200:
                current_price = data["Close"].iloc[-1]
                dma_50 = data["Close"].rolling(window=50).mean().iloc[-1]
                dma_200 = data["Close"].rolling(window=200).mean().iloc[-1]

                if current_price < dma_200:
                    signal = "🔴 STRONG SELL (Below 200 DMA)"
                elif current_price > dma_50 and dma_50 > dma_200:
                    signal = "🟢 BUY / ACCUMULATE (Golden Cross)"
                else:
                    signal = "🟡 HOLD"
            elif not data.empty:
                current_price = data["Close"].iloc[-1]
                signal = "🟡 HOLD (Insufficient history for DMA metrics)"
        except Exception as e:
            print(f"Using CSV defaults for {broker_symbol} due to fetch variance: {e}")

        # Calculate performance returns
        total_return = ((current_price - avg_cost) / avg_cost) * 100

        analysis_results.append({
            "Symbol": broker_symbol,
            "Company Name": company_name,
            "Qty": qty,
            "Avg Cost": f"₹{avg_cost:,.2f}",
            "Current Price": f"₹{current_price:,.2f}",
            "Total Return": f"{total_return:+.2f}%",
            "Action Signal": signal
        })

    # Generate Markdown File Outputs
    report_df = pd.DataFrame(analysis_results)
    date_str = datetime.now().strftime("%Y-%m-%d")

    markdown_output = f"""# Weekly Portfolio Analysis Report - {date_str}

## Executive Summary & Action Items
Below is the automated status of your portfolio based on weekly closure trends.

{report_df.to_markdown(index=False)}

---
*Report generated automatically via GitHub Actions.*
"""

    os.makedirs("reports", exist_ok=True)
    with open(f"reports/report_{date_str}.md", "w") as f:
        f.write(markdown_output)

    with open("README.md", "w") as f:
        f.write(markdown_output)

if __name__ == "__main__":
    run_weekly_analysis()
