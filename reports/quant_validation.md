# Quantitative Validation Report: Redbull Core Discipline

**Date**: 2026-10-15  
**Discipline**: Redbull Core Systematic Governance  
**Scope**: Model Hypotheses, Failure Mode Audits, Lookahead Bias Truncation Verification, and Sensitivity Robustness Framework  

---

## 1. Core Model Hypotheses

The revised portfolio management framework rests on five testable hypotheses formulated to balance drawdown mitigation against friction and false whipsaws:

- **H1 (Trailing Stop)**: A $\ge 30\%$ fall from the 52w high after a $\ge 50\%$ gain predicts 12-month underperformance vs NIFTYBEES.  
  *Operational Mechanics*: Armed only for winners ($\text{total\_return} \ge 50\%$); evaluated exclusively on month-end closes; trims $1/3$ to derisk while preserving core exposure. Index ETFs are exempt.
- **H2 (Invalidation Confirmation)**: 3 closes below the level predict underperformance better than 1 close.  
  *Operational Mechanics*: Transient intraday or single-day closes often reflect market noise or liquidity spikes. Requiring 3 consecutive daily closes (or a Friday weekly close, or a severe $\ge 10\%$ drop) filters transient panic while confirming persistent structural thesis breakdowns.
- **H3 (200-DMA REVIEW)**: $> 3\%$ below the 200-DMA for 20 sessions flags higher risk, but not reliably enough to SELL.  
  *Operational Mechanics*: Prevents mechanical selling of quality holdings at cyclical bottoms. Enters a monitored `REVIEW` state under hysteresis (requires recovery $> 2\%$ above 200-DMA to clear), reserving `SELL` triggers strictly for thesis invalidations.
- **H4 (Accumulate Gate)**: A rising 200-DMA + positive 6/12-month vol-adjusted momentum predicts outperformance.  
  *Operational Mechanics*: Restricts capital additions to confirmed uptrends ($\text{200-DMA} > \text{200-DMA}_{t-20}$), positive risk-adjusted returns over 6 and 12 months, and proximity to 52w highs ($\le 20\%$), preventing "averaging down" on deteriorating assets. Evaluated only at month-end.
- **H5 (Cap Precedence)**: Trimming above 8% reduces drawdown without materially lowering return.  
  *Operational Mechanics*: Enforces idiosyncratic risk boundaries ($8\%$ stock cap, $25\%$ sector cap) before evaluating additions, reducing portfolio vulnerability to single-asset blowups.

---

## 2. Failure Mode Catalog & Mitigations

Systematic quantitative overlays introduce specific failure modes that must be actively audited and governed:

| Failure Mode | Mechanism | Historical / Pathological Manifestation | Systematic Mitigation in Place |
|:---|:---|:---|:---|
| **V-Shaped Recoveries** | Violent market sell-offs trigger breakdown signals (`REVIEW` or `SELL`) near cyclical bottoms, causing exits right before rapid rebounds. | Post-pandemic liquidity troughs (March 2020) or election day swings (June 2024). | 3-close invalidation confirmation prevents panic exits on day 1; 200-DMA breaches trigger `REVIEW`, never automatic `SELL`. |
| **Momentum Crashes** | Accumulate gates buy extended leaders at late-cycle tops right as trend exhaustion occurs. | September 2024 momentum peaks followed by sharp multi-month corrections across broader market mid/small caps. | Overextension multiple filter ($> 1.25\times$ 50-DMA) strictly blocks additions; additions gated to month-end reviews; vol-adjusted denominator penalizes erratic price spikes. |
| **Stale Broker Prices** | Disconnect between broker account snapshot prices and live exchange quotes misrepresents actual weightings and triggers false actions. | Off-market transactions, unrefreshed broker exports, or frozen illiquid holdings. | Dual verification check (`price_data_issue`) comparing the as-of close against broker price within $\pm 25\%$ (`price_mismatch_pct`); data failures route to `NO DATA` / `VERIFY DATA` and freeze trades. |
| **Corporate-Action Gaps** | Splits, bonus shares, or demergers create overnight nominal price drops that mimic structural thesis breaches or moving-average collapses. | Demergers (e.g. Jio Financial from Reliance) or stock splits (e.g. 10:1 splits). | `adjust_unadjusted_splits` only rescales one-day jumps beyond $2.5\times$ / $0.4\times$, so ordinary 1:1 and 1:2 bonuses (0.5x / 0.67x) are **not** caught; the hindcast corporate-actions table (`data/corporate_actions.csv`) is the real fix. `price_data_issue` ratio bounds ($> 2.5\times$ or $< 0.4\times$ 200-DMA, `max_price_to_dma_ratio`) tag broken histories for manual audit. |

---

## 3. No-Lookahead Truncation Verification

To ensure backtest integrity and live inference alignment, all feature pipelines must guarantee zero lookahead bias.

### Invariance Definition
For any arbitrary temporal cutoff $t < T$, feature computation executed on truncated historical data $D_{[:t]}$ must produce outputs strictly identical to the feature values evaluated at time $t$ on the complete historical series $D_{[:T]}$:
$$\mathcal{F}(D_{[:t]}) \equiv \mathcal{F}(D_{[:T]})\Big|_t$$

### Feature Audit Matrix

| Feature | Lookback Specification | Truncation Invariance Result |
|:---|:---|:---|
| **Consecutive-Close Counts** (`sessions_below_200dma`) | Backwards count from $t$ of closes $< 0.97 \times \text{200-DMA}_t$. | **PASSED**: Strictly identical to full series backward scan; zero leakage. |
| **Thesis Invalidation Closes** (`consecutive_closes_below`) | Backwards count from $t$ of closes $\le \text{Invalidation\_Price}$. | **PASSED**: Pure point-in-time calculation; identical across all $t$. |
| **Month-End Detection** (`is_month_end`) | Calendar offset evaluation: $\text{Date}_t + \text{1 BDay}$ enters new month. | **PASSED**: Relies solely on calendar arithmetic at $t$; future dates excluded. |
| **200-DMA Rising Check** (`dma_200_rising`) | $\text{SMA}_{200}(t) > \text{SMA}_{200}(t-20)$. | **PASSED**: Rolling averages at $t$ and $t-20$ depend solely on $D_{[t-220:t]}$. |
| **6-Month Momentum** (`vol_adj_return_6m`) | $R_{6m} / (\sigma_{6m} \times \sqrt{252})$ over trailing 126 sessions. | **PASSED**: Sliced window $D_{[t-126:t]}$ exactly matches full rolling window. |
| **12-Month Momentum** (`vol_adj_return_12m`) | $R_{12m} / (\sigma_{12m} \times \sqrt{252})$ over trailing 252 sessions. | **PASSED**: Sliced window $D_{[t-252:t]}$ exactly matches full rolling window. |
| **52-Week High / Low** (`high_52w`, `low_52w`) | $\max(High_{[t-252:t]})$ and $\min(Low_{[t-252:t]})$. | **PASSED**: Trailing 252-day extremum is strictly historical. |

### Leakage Trap (Stress Test)
Unit tests in `tests/test_analysis.py` (`test_no_lookahead_feature_truncation`) systematically inject corrupted future data into $D_{[t:T]}$ (multiplying future prices by $10\times$ and introducing artificial extremes). In all iterations across randomized $t \in [260, 480]$, the features and final model signal decisions remained $100\%$ unchanged.

---

## 4. Parameter Sensitivity Audit (Hindcast Cache)

### Cache Availability Check
- **Target Cache Path**: `data/prices/`
- **Status**: **NOT PRESENT** in workspace repository.
- **Audit Decision**: Per task instructions ("*only on the hindcast cache, if data/prices/ exists; else skip and say so*"), hindcast parameter sensitivity is **skipped**.

### Sensitivity Protocol Specification (Awaiting Price Cache Ingestion)
When the historical price cache is populated, the parameter perturbation matrix is defined as follows:

| Parameter | Baseline Default | Perturbation Range | Robustness Threshold |
|:---|:---|:---|:---|
| **Trailing Drawdown** | $30\%$ | $\{20\%, 30\%, 40\%\}$ | $\ge 70\%$ neighbouring sign stability |
| **Minimum Gain Threshold** | $50\%$ | $\{25\%, 50\%, 75\%\}$ | $\ge 70\%$ neighbouring sign stability |
| **Confirmation Closes** | $3$ closes | $\{2, 3, 5\}$ | $\ge 70\%$ neighbouring sign stability |
| **REVIEW Sessions** | $20$ sessions | $\{10, 20, 40\}$ | $\ge 70\%$ neighbouring sign stability |
| **REVIEW Band** | $3\%$ | $\{2\%, 3\%, 5\%\}$ | $\ge 70\%$ neighbouring sign stability |

*Governing Rule*: Parameters failing the $\ge 70\%$ sign-of-benefit robustness criterion across neighbouring settings will be flagged as **advisory-only** rather than hard execution rules. Defaults remain fixed pending empirical test data.

---

## 5. Tax and Transaction Cost Disclaimer

> [!IMPORTANT]
> **Upper Bound Notice**: All quantitative signals, simulated returns, and optimization metrics generated by this model **exclude taxation (capital gains tax, STT) and transaction costs (slippage, brokerage, exchange fees)**. Consequently, all reported performance figures and model improvements represent an **upper bound** on real-world net investor returns.
