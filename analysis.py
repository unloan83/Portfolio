import os
from datetime import datetime
import pandas as pd
import yfinance as yf


def run_weekly_analysis():
    # 1. Load Portfolio
    portfolio_file = "portfolio.csv"
    if not os.path.exists(portfolio_file):
        print("portfolio.csv not found!")
        return

    df = pd.read_csv(portfolio_file)

    # 2. Fetch Live Market Data
    tickers = df["Ticker"].tolist()
    # Download data for technical moving averages (50 & 200 DMA)
    data = yf.download(tickers, period="1y")["Close"]

    analysis_results = []

    # 3. Process Rules Engine
    for _, row in df.iterrows():
        ticker = row["Ticker"]
        avg_cost = row["Avg_Cost"]
        shares = row["Shares"]

        current_price = data[ticker].iloc[-1]
        dma_50 = data[ticker].rolling(window=50).mean().iloc[-1]
        dma_200 = data[ticker].rolling(window=200).mean().iloc[-1]

        # Calculate Returns
        total_return = ((current_price - avg_cost) / avg_cost) * 100

        # Simple Logic Rules Engine
        if current_price < dma_200:
            signal = "🔴 STRONG SELL (Below 200 DMA)"
        elif current_price > dma_50 and dma_50 > dma_200:
            signal = "🟢 BUY / ACCUMULATE (Golden Cross Trend)"
        else:
            signal = "🟡 HOLD"

        analysis_results.append(
            {
                "Ticker": ticker,
                "Current Price": f"₹{current_price:.2f}",
                "Total Return": f"{total_return:.2f}%",
                "Action Signal": signal,
            }
        )

    # 4. Generate Structured Markdown Report
    report_df = pd.DataFrame(analysis_results)
    date_str = datetime.now().strftime("%Y-%m-%d")

    markdown_output = f"""# Weekly Portfolio Analysis Report - {date_str}

## Executive Summary & Action Items
Below is the automated status of your portfolio based on weekly closure trends.

{report_df.to_markdown(index=False)}

---
*Report generated automatically via GitHub Actions.*
"""

    # Save to a reports archive directory
    os.makedirs("reports", exist_ok=True)
    with open(f"reports/report_{date_str}.md", "w") as f:
        f.write(markdown_output)

    # Also update a master README for quick viewing in GitHub
    with open("README.md", "w") as f:
        f.write(markdown_output)


if __name__ == "__main__":
    run_weekly_analysis()
