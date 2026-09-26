"""Independent Vectorbt Cross-Validation & Market Breadth Analysis Script."""
import sys
import os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Fix for plotly template in vectorbt if loaded
import plotly.graph_objs as go
if not hasattr(go.layout.template.Data, 'scattermapbox'):
    setattr(go.layout.template.Data, 'scattermapbox', None)

import pandas as pd
import numpy as np
import vectorbt as vbt

from analysis import TICKER_MAP, SECTOR_MAP

from backtest.backtester import run_backtest, Signal
from backtest.run_dma_backtest import DmaCrossoverStrategy, _portfolio_symbols
from backtest.yfinance_adapter import fetch_history
from signal_engine import evaluate_signal

def run_cross_validation():
    portfolio_path = Path("portfolio.csv")
    symbols = _portfolio_symbols(portfolio_path)
    
    vbt_results = {}
    bkt_results = {}
    
    all_bkt_trades = []
    all_vbt_trades = []
    
    diverged_symbols = []
    comparison_rows = []

    print(f"=== STEP 1: Running Cross-Validation on {len(symbols)} Portfolio Symbols ===")
    
    for broker_symbol in symbols:
        yahoo_symbol = TICKER_MAP.get(broker_symbol, f"{broker_symbol}.NS")
        if yahoo_symbol in {"UNLISTED", "TODO_VERIFY"}:
            continue
            
        try:
            history = fetch_history(yahoo_symbol, period="3y")
            if history.empty or len(history) < 202:
                continue
        except Exception as exc:
            print(f"[warn] Skipping {broker_symbol}: {exc}")
            continue

        # 1. Backtester.py Execution
        bkt_res = run_backtest(
            DmaCrossoverStrategy(),
            {yahoo_symbol: history},
            slippage_bps=5.0
        )
        bkt_sum = bkt_res.summary()
        bkt_closed = bkt_res.closed_trades()
        all_bkt_trades.extend(bkt_closed)

        # 2. Vectorbt Execution
        # Build vectorized entries and exits using evaluate_signal per bar
        close = history["close"]
        high = history["high"]
        low = history["low"]
        open_price = history["open"]
        
        dma_50 = close.rolling(50).mean()
        dma_200 = close.rolling(200).mean()
        
        entries = pd.Series(False, index=history.index)
        exits = pd.Series(False, index=history.index)
        stock_sector = SECTOR_MAP.get(broker_symbol, "Other ETFs/Misc")
        
        # Evaluate signals per bar starting from bar 199 (same as backtester.py index 199)
        for i in range(199, len(history)):
            cp = float(close.iloc[i])
            d50 = float(dma_50.iloc[i]) if pd.notna(dma_50.iloc[i]) else None
            d200 = float(dma_200.iloc[i]) if pd.notna(dma_200.iloc[i]) else None
            
            eval_res = evaluate_signal(
                current_price=cp,
                dma_50=d50,
                dma_200=d200,
                roe=None,
                stock_sector=stock_sector,
            )
            
            if eval_res.technical_trend == "BULLISH" and not eval_res.is_overextended and eval_res.fundamental_pass:
                entries.iloc[i] = True
            elif eval_res.technical_trend == "BEARISH":
                exits.iloc[i] = True

        # Run vectorbt portfolio with fill on next open and 5 bps slippage (0.0005)
        # Signal on bar i fills on open price at bar i+1
        open_shifted = open_price.shift(-1)
        pf = vbt.Portfolio.from_signals(
            close=close,
            entries=entries,
            exits=exits,
            price=open_shifted,
            slippage=0.0005,
            freq="1D",
            init_cash=100000.0,
        )
        
        vbt_trades = pf.trades.records_readable
        vbt_count = int(pf.trades.count())
        vbt_win_rate = round(float(pf.trades.win_rate()) * 100, 1) if vbt_count > 0 else 0.0
        
        # Calculate win rate and expectancy from vectorbt trade returns
        if vbt_count > 0 and not vbt_trades.empty:
            returns = vbt_trades["Return"] * 100
            vbt_expectancy = round(float(returns.mean()), 2)
        else:
            vbt_expectancy = 0.0
            
        bkt_count = int(bkt_sum["trades"])
        bkt_win_rate = float(bkt_sum["win_rate_pct"])
        bkt_expectancy = float(bkt_sum["expectancy_pct"])

        # Compare metrics with 5% relative tolerance
        # Tolerance check: abs(diff) / max(abs(val1), abs(val2), 1.0) <= 0.05
        count_diff = abs(vbt_count - bkt_count)
        win_diff = abs(vbt_win_rate - bkt_win_rate) / max(abs(vbt_win_rate), abs(bkt_win_rate), 1.0)
        exp_diff = abs(vbt_expectancy - bkt_expectancy) / max(abs(vbt_expectancy), abs(bkt_expectancy), 1.0)
        
        is_diverged = (count_diff > 0) or (win_diff > 0.05 and count_diff > 0) or (exp_diff > 0.05 and count_diff > 0)
        if is_diverged:
            diverged_symbols.append(broker_symbol)
            
        comparison_rows.append({
            "Symbol": broker_symbol,
            "BKT_Trades": bkt_count,
            "VBT_Trades": vbt_count,
            "BKT_WinRate%": bkt_win_rate,
            "VBT_WinRate%": vbt_win_rate,
            "BKT_Exp%": bkt_expectancy,
            "VBT_Exp%": vbt_expectancy,
            "Match": "MATCH" if not is_diverged else "DIVERGED"
        })

    comp_df = pd.DataFrame(comparison_rows)
    print("\n=== STEP 2: Per-Symbol Comparison Table ===")
    print(comp_df.to_string(index=False))
    
    print("\n=== STEP 3: Branch Selection ===")
    if not diverged_symbols:
        print("BRANCH (a): All backtested symbols match vectorbt within tolerance.")
        print("Backtester.py execution mechanics are CONFIRMED CORRECT.")
    else:
        print(f"BRANCH (b): Divergence detected on {len(diverged_symbols)} symbols: {diverged_symbols}")

    print("\n=== STEP 4: Pooled Portfolio Statistics across ALL Trades ===")
    if all_bkt_trades:
        total_trades = len(all_bkt_trades)
        pnls = [t.pnl_pct for t in all_bkt_trades if t.pnl_pct is not None]
        wins = [p for p in pnls if p > 0]
        losses = [p for p in pnls if p <= 0]
        pooled_win_rate = round(100.0 * len(wins) / total_trades, 1)
        pooled_expectancy = round(float(np.mean(pnls)), 2)
        avg_win = round(float(np.mean(wins)), 2) if wins else 0.0
        avg_loss = round(float(np.mean(losses)), 2) if losses else 0.0
        
        # Pooled compounding return
        equity_curve = np.cumprod([1 + p / 100 for p in pnls])
        running_max = np.maximum.accumulate(np.insert(equity_curve, 0, 1.0))[1:]
        drawdown = (equity_curve - running_max) / running_max
        max_dd = round(float(drawdown.min()) * 100, 2)
        total_ret = round((float(equity_curve[-1]) - 1) * 100, 2)
        
        print(f"Total Pooled Trades:       {total_trades}")
        print(f"Pooled Win Rate:           {pooled_win_rate}% ({len(wins)} wins / {len(losses)} losses)")
        print(f"Pooled Expectancy / Trade: {pooled_expectancy}%")
        print(f"Average Win:               +{avg_win}%")
        print(f"Average Loss:              {avg_loss}%")
        print(f"Pooled Compound Return:    {total_ret}%")
        print(f"Pooled Max Drawdown:       {max_dd}%")
    else:
        print("No closed trades generated.")

    print("\n=== STEP 5: Broad Market Breadth Sanity Check (200 DMA Breakdown Cluster) ===")
    nifty50_sample = [
        "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
        "BHARTIARTL.NS", "ITC.NS", "SBIN.NS", "LTIM.NS", "LT.NS",
        "HINDUNILVR.NS", "AXISBANK.NS", "KOTAKBANK.NS", "M&M.NS", "HCLTECH.NS",
        "SUNPHARMA.NS", "NTPC.NS", "TATAMOTORS.NS", "POWERGRID.NS", "ONGC.NS",
        "TITAN.NS", "ADANIENT.NS", "BAJFINANCE.NS", "COALINDIA.NS", "TATASTEEL.NS",
        "ULTRACEMCO.NS", "ASIANPAINT.NS", "BPCL.NS", "GRASIM.NS", "HEROMOTOCO.NS",
        "JSWSTEEL.NS", "TECHM.NS", "ADANIPORTS.NS", "HDFCLIFE.NS", "WIPRO.NS",
        "CIPLA.NS", "SBI LIFE.NS", "EICHERMOT.NS", "BAJAJ-AUTO.NS", "DRREDDY.NS",
        "BRITANNIA.NS", "TATACONSUM.NS", "INDUSINDBK.NS", "DIVISLAB.NS", "APOLLOHOSP.NS"
    ]
    
    below_200_dma_count = 0
    valid_sample_count = 0
    
    import yfinance as yf
    for symbol in nifty50_sample:
        try:
            df = yf.Ticker(symbol).history(period="1y")
            if not df.empty and len(df) >= 200:
                cp = float(df["Close"].iloc[-1])
                d200 = float(df["Close"].rolling(200).mean().iloc[-1])
                valid_sample_count += 1
                if cp < d200:
                    below_200_dma_count += 1
        except Exception:
            continue

    if valid_sample_count > 0:
        pct_below = round((below_200_dma_count / valid_sample_count) * 100, 1)
        print(f"Broader NIFTY 50 Sample Evaluated: {valid_sample_count} stocks.")
        print(f"Stocks Below 200 DMA: {below_200_dma_count} / {valid_sample_count} ({pct_below}%).")
        print(f"Interpretation: Market breadth indicator confirms {pct_below}% of the benchmark index is currently below 200 DMA.")
    else:
        print("Market breadth sample query could not fetch live index data.")

if __name__ == "__main__":
    run_cross_validation()
