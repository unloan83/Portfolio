import os
from datetime import datetime
import pandas as pd
import yfinance as yf

# Exact Yahoo Finance symbols matching tradeable Indian Market Exchange Tickers
TICKER_MAP = {
    'ASHLEY': 'ASHOKLEY.NS',
    'FEDBAN': 'FEDERALBNK.NS',
    'HDFBAN': 'HDFCBANK.NS',
    'HDF250': 'HDFCSML250.NS',
    'ICIGOL': 'GOLDBEES.NS',     
    'ICINIF': 'ICICINIFTY.NS',   
    'ICIPSE': 'SILVERBEES.NS',   
    'NIPNIT': 'NIFTYIETF.NS',    
    'MIR150': 'MOMENTUM.NS',     
    'BHAELE': 'BEL.NS',
    'TATGLO': 'TATACONSUM.NS',
    'JIOFIN': 'JIOFIN.NS',
    'WIPRO': 'WIPRO.NS',
    'ENGIND': 'ENGINERSIN.NS',
    'LIC': 'LICI.NS',
    'DRREDD': 'DRREDDY.NS',
    'SEQSCI': 'STAR.NS',         
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
    'TATCAP': 'UNLISTED',
    'LGELEC': 'UNLISTED'
}

def run_weekly_analysis():
    portfolio_file = "portfolio.csv"
    if not os.path.exists(portfolio_file):
        print("portfolio.csv not found!")
        return

    df = pd.read_csv(portfolio_file)
    df.columns = df.columns.str.strip()

    analysis_results = []
    telegram_lines = [] # To store compact lines for mobile view

    for _, row in df.iterrows():
        broker_symbol = str(row["Stock Symbol"]).strip()
        company_name = row["Company Name"]
        qty = row["Qty"]
        avg_cost = row["Average Cost Price"]
        csv_current_price = row["Current Market Price"]

        current_price = csv_current_price
        signal = "🟡 HOLD (Static)"
        
        yf_ticker = TICKER_MAP.get(broker_symbol, f"{broker_symbol}.NS")

        if yf_ticker != 'UNLISTED':
            try:
                ticker_obj = yf.Ticker(yf_ticker)
                data = ticker_obj.history(period="1y")
                
                if not data.empty and len(data) >= 200:
                    current_price = data["Close"].iloc[-1]
                    dma_50 = data["Close"].rolling(window=50).mean().iloc[-1]
                    dma_200 = data["Close"].rolling(window=200).mean().iloc[-1]

                    if current_price < dma_200:
                        signal = "🔴 STRG SELL"
                    elif current_price > dma_50 and dma_50 > dma_200:
                        signal = "🟢 BUY"
                    else:
                        signal = "🟡 HOLD"
                elif not data.empty:
                    current_price = data["Close"].iloc[-1]
                    signal = "🟡 HOLD (New)"
            except Exception as e:
                pass

        total_return = ((current_price - avg_cost) / avg_cost) * 100
        
        # Determine emoji for returns
        return_emoji = "📈" if total_return >= 0 else "📉"

        analysis_results.append({
            "Symbol": broker_symbol,
            "Company Name": company_name,
            "Qty": qty,
            "Avg Cost": f"₹{avg_cost:,.2f}",
            "Current Price": f"₹{current_price:,.2f}",
            "Total Return": f"{total_return:+.2f}%",
            "Action Signal": signal
        })

        # Create a hyper-compact layout for the Telegram message
        telegram_lines.append(f"{signal} | {broker_symbol} | Ret: {return_emoji}{total_return:+.1f}%")

    # Generate Markdown Files for GitHub Website
    report_df = pd.DataFrame(analysis_results)
    date_str = datetime.now().strftime("%Y-%m-%d")

    markdown_output = f"# Weekly Portfolio Analysis Report - {date_str}\n\n{report_df.to_markdown(index=False)}"

    os.makedirs("reports", exist_ok=True)
    with open(f"reports/report_{date_str}.md", "w") as f:
        f.write(markdown_output)

    with open("README.md", "w") as f:
        f.write(markdown_output)

    # --- NEW CAPABILITY FOR TELEGRAM OUTBOUND ---
    # Combine lines into a single message body
    summary_msg = f"📊 *Portfolio Snapshot ({date_str})*\n" + "\n".join(telegram_lines)
    
    # Save properly to GitHub Actions execution environment file if running in CI
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as env_file:
            # Use multi-line string syntax for GitHub Actions outputs
            env_file.write("TELEGRAM_SUMMARY<<EOF\n")
            env_file.write(summary_msg + "\n")
            env_file.write("EOF\n")

if __name__ == "__main__":
    run_weekly_analysis()
