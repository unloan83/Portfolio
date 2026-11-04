# Orchestrated Multi-Agent Portfolio Audit - 2026-11-04

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-04
* **Portfolio XIRR**: **-5.16%** (Current Traded Positions Value: ₹499,858)
* **Benchmark XIRR**: **5.43%** (Simulated Benchmark Value: ₹639,970)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹18,825         | 35.65%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,090         | 30.45%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,704          | 26.59%  | Full                 |
| GAIL       |         61 |           61 | ₹11,359         | 17.71%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,300          | 16.39%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.98%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,285          | 15.14%  | Full                 |
| BHAELE     |         80 |           48 | ₹19,104         | 14.54%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,317          | 10.98%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,244          | 9.37%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,880          | 8.85%   | Full                 |
| TATGLO     |         30 |           30 | ₹32,040         | 6.21%   | Full                 |
| NTPC       |         12 |           12 | ₹3,863          | 5.58%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,594         | 0.48%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,354          | -0.36%  | Full                 |
| HINPET     |         14 |           14 | ₹5,129          | -0.38%  | Full                 |
| HDF250     |         24 |           24 | ₹4,208          | -1.18%  | Full                 |
| ICINIF     |         86 |           86 | ₹23,096         | -2.42%  | Full                 |
| ONGC       |         39 |           39 | ₹9,165          | -2.44%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.73%  | Full                 |
| RELIND     |         76 |           74 | ₹97,014         | -7.91%  | Partial (74/76 sh)   |
| ASHLEY     |        106 |           53 | ₹8,164          | -8.22%  | Partial (53/106 sh)  |
| MIR150     |        194 |          194 | ₹4,336          | -9.73%  | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,737          | -11.23% | Full                 |
| HDFBAN     |        130 |           75 | ₹55,253         | -13.03% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,755          | -13.96% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,224          | -16.99% | Partial (28/53 sh)   |
| ICIGOL     |        250 |          250 | ₹30,215         | -18.27% | Full                 |
| WIPRO      |        220 |          170 | ₹33,074         | -18.28% | Partial (170/220 sh) |
| ICIPSE     |        193 |          193 | ₹35,497         | -36.85% | Full                 |
| LIC        |         80 |           45 | ₹18,360         | -51.94% | Partial (45/80 sh)   |

#### Trade History Coverage Gaps

* **Missing Holdings (No trades recorded in `trades.csv`)**: `LGELEC`, `NTPGRE`, `TATCAP`
* **Partial Trade History (`trades.csv` shares < `portfolio.csv` shares)**:
  - `ASHLEY`: Portfolio has 106 sh, trades record 53 sh (unrecorded: 53 sh)
  - `HDFBAN`: Portfolio has 130 sh, trades record 75 sh (unrecorded: 55 sh)
  - `BHAELE`: Portfolio has 80 sh, trades record 48 sh (unrecorded: 32 sh)
  - `JIOFIN`: Portfolio has 53 sh, trades record 28 sh (unrecorded: 25 sh)
  - `WIPRO`: Portfolio has 220 sh, trades record 170 sh (unrecorded: 50 sh)
  - `LIC`: Portfolio has 80 sh, trades record 45 sh (unrecorded: 35 sh)
  - `RELIND`: Portfolio has 76 sh, trades record 74 sh (unrecorded: 2 sh)


### Asset Health Assessment
| Symbol     | Sector               | Weight   | Total Return   | Trailing Stop   | Decision    | Action                           | Reasoning                                                                                                                                                                                                                                                      | Thesis Status   |   Conviction |
|:-----------|:---------------------|:---------|:---------------|:----------------|:------------|:---------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|-------------:|
| RELIND     | Oil & Gas            | 15.5%    | +13.15%        | N/A             | SELL        | Exit all 76 sh (~₹99,636)        | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 14.9%    | +0.09%         | N/A             | SELL        | Exit all 130 sh (~₹95,771)       | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 6.7%     | -17.71%        | N/A             | SELL        | Exit all 220 sh (~₹42,801)       | Thesis invalidated: Price ₹194.55 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 5.5%     | -26.80%        | N/A             | SELL        | Exit all 193 sh (~₹35,497)       | Thesis invalidated: Price ₹183.92 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.1%     | -54.57%        | N/A             | SELL        | Exit all 80 sh (~₹32,640)        | Thesis invalidated: Price ₹408.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.0%     | +33.40%        | N/A             | SELL        | Exit all 30 sh (~₹32,040)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| BHAELE     | Defense              | 5.0%     | +152.17%       | ₹330.97         | SELL        | Exit all 80 sh (~₹31,840)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.7%     | -12.89%        | N/A             | SELL        | Exit all 250 sh (~₹30,215)       | Thesis invalidated: Price ₹120.86 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.3%     | +0.45%         | N/A             | SELL        | Exit all 54 sh (~₹27,594)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.6%     | -0.93%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.4%     | +48.43%        | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +69.82%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹18,825)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| ASHLEY     | Auto                 | 2.5%     | +55.62%        | ₹148.26         | SELL        | Exit all 106 sh (~₹16,327)       | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| FEDBAN     | Banking              | 2.5%     | +123.63%       | ₹259.30         | HOLD        | Hold                             | Consolidation hold: Price ₹335.20 moving sideways between 50 DMA (₹337.41) and 200 DMA (₹311.20); conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                 | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | +3.60%         | N/A             | SELL        | Exit all 46 sh (~₹15,536)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -4.27%         | N/A             | SELL        | Exit all 53 sh (~₹11,780)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| NTPGRE     | Power                | 1.8%     | -22.68%        | N/A             | SELL        | Exit all 138 sh (~₹11,524)       | Thesis invalidated: Price ₹83.51 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.8%     | +19.72%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +19.72%, position weight 1.8%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -3.50%         | N/A             | SELL        | Exit all 39 sh (~₹9,165)         | Trend exit: month-end close ₹225.39 < 10-month average ₹254.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +15.69%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹1374.00 moving sideways between 50 DMA (₹1217.16) and 200 DMA (₹1242.79); conviction (5/5) thesis INTACT above invalidation (₹1009.47).                                                                                             | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | -1.52%         | N/A             | SELL        | Exit all 14 sh (~₹5,129)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | -1.46%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return -1.46%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | -3.62%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |
| NHPC       | Power                | 0.7%     | +34.35%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹78.49 moving sideways between 50 DMA (₹74.85) and 200 DMA (₹76.82); conviction (3/5) thesis INTACT above invalidation (₹53.75).                                                                                                     | INTACT          |            3 |
| HDF250     | Broad Market         | 0.7%     | -0.43%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹175.33 moving sideways between 50 DMA (₹179.83) and 200 DMA (₹171.03); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| NTPC       | Power                | 0.6%     | +16.13%        | N/A             | SELL        | Exit all 12 sh (~₹3,863)         | Trend exit: month-end close ₹316.25 < 10-month average ₹353.10. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -36.01%        | N/A             | SELL        | Exit all 67 sh (~₹3,755)         | Thesis invalidated: Price ₹56.05 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +93.23%        | ₹135.92         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +93.23%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                                | INTACT          |            3 |
| TATPOW     | Power                | 0.4%     | +26.97%        | N/A             | SELL        | Exit all 8 sh (~₹2,880)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +9.95%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹35.58 moving sideways between 50 DMA (₹33.37) and 200 DMA (₹33.85); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +85.06%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,285)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -2.79%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹272.81 vs 200-day average ₹272.72 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.6%
* **Banking**: 17.7%
* **Commodities**: 10.2%
* **Power**: 8.4%
* **IT**: 7.1%
* **Insurance**: 5.1%
* **Consumption**: 5.0%
* **Defense**: 5.0%
* **Broad Market**: 4.9%
* **Financial Services**: 4.3%
* **Consumer Electronics**: 3.4%
* **Telecom**: 2.9%
* **Auto**: 2.5%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 27.0%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 29.0%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.8%), +7 more          |
| Financials        | 27.0%      | 25.0% | ⚠️ BREACH | FEDBAN (2.5%), HDFBAN (14.9%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.6%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.8%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 10.2%      | 25.0% | OK        | ICIGOL (4.7%), ICIPSE (5.5%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| RELIND   | 15.5%           | 15.81%             | +0.31% via ICINIF                        |
| HDFBAN   | 14.9%           | 15.40%             | +0.41% via ICINIF, +0.08% via KOTAKBKETF |
| WIPRO    | 6.7%            | 6.66%              | Direct only                              |
| ICIPSE   | 5.5%            | 5.52%              | Direct only                              |
| LIC      | 5.1%            | 5.08%              | Direct only                              |
| TATGLO   | 5.0%            | 4.99%              | Direct only                              |
| BHAELE   | 5.0%            | 4.96%              | Direct only                              |
| ICIGOL   | 4.7%            | 4.70%              | Direct only                              |
| JSWENE   | 4.3%            | 4.29%              | Direct only                              |
| ICINIF   | 3.6%            | 3.59%              | Direct only                              |
| LGELEC   | 3.4%            | 3.42%              | Direct only                              |
| IDECEL   | 2.9%            | 2.93%              | Direct only                              |
| ASHLEY   | 2.5%            | 2.54%              | Direct only                              |
| FEDBAN   | 2.5%            | 2.51%              | +0.01% via KOTAKBKETF                    |
| TATCAP   | 2.4%            | 2.42%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **4.9%** (Target: 50.0%, Gap: +45.1%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.1%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹23,096 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,336  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,208  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.5%    | ₹99,636 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 14.9%    | ₹95,771 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,244  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,863  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.7%     | ₹42,801 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.1%     | ₹32,640 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.4%     | ₹21,997 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹16,327 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.5%     | ₹16,090 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹15,536 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.8%     | ₹11,359 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹9,165  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,354  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,880  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,704  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,737  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 5.5%     | ₹35,497 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.0%     | ₹32,040 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 5.0%     | ₹31,840 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.3%     | ₹27,594 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,780 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.8%     | ₹11,524 | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,129  | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,317  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,755  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,300  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.7%     | ₹30,215 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹18,825 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,285  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,737)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,285)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,704)  |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,880)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,300)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,755)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,208)  |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,317)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,336) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,354)  |
| ENGIND     | Infrastructure | 0.8%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,129)  |

### Thesis Governance & Review Status
All portfolio theses are within their scheduled 3-month review window.

#### Exit or Re-underwrite (Currently Invalidated Holdings)
The following 9 holdings have breached their entry Invalidation Price. Per portfolio governance rules, Invalidation_Price must not be lowered to accommodate losses; the holdings require fundamental re-underwriting or orderly exit:

| Symbol   | Role     | CMP     | Invalidation Price   | Governance Action     |
|:---------|:---------|:--------|:---------------------|:----------------------|
| LIC      | Core     | ₹411.35 | ₹790.25              | Exit or re-underwrite |
| WIPRO    | Core     | ₹204.25 | ₹208.04              | Exit or re-underwrite |
| GUJGA    | Core     | ₹401.15 | ₹430.75              | Exit or re-underwrite |
| SJVLIM   | Core     | ₹75.16  | ₹80.58               | Exit or re-underwrite |
| ICIPSE   | Tactical | ₹260.35 | ₹231.16              | Exit or re-underwrite |
| ICIGOL   | Tactical | ₹133.12 | ₹131.80              | Exit or re-underwrite |
| JSWENE   | Core     | ₹595.05 | ₹468.00              | Exit or re-underwrite |
| NTPGRE   | Core     | ₹103.52 | ₹99.36               | Exit or re-underwrite |
| HINPET   | Core     | ₹393.85 | ₹342.25              | Exit or re-underwrite |

See `reports/thesis_proposals.md` for proposed invalidation floor increases on major winners.
### Tax Plan (FY 2026-27)

> [!NOTE]
> **Advisory Notice**: This tax plan is indicative and for planning purposes only. Tax parameters (STCG Rate: **20.0%**, LTCG Rate: **12.5%**, Section 112A LTCG Exemption: **₹125,000**) are configured in `config.py` (`stcg_rate`, `ltcg_rate`, `ltcg_exemption_limit`). Consult a chartered accountant for statutory tax filing.

#### Capital Gains Inventory (FIFO Matching)

| Metric                                | Amount      | Tax Rate        | Notes                                |
|:--------------------------------------|:------------|:----------------|:-------------------------------------|
| Realised STCG (FY 2026-27 so far)     | ₹0.00       | 20.0%           | Taxable on net short-term gains      |
| Realised LTCG (FY 2026-27 so far)     | ₹0.00       | 12.5%           | Subject to ₹125,000 annual exemption |
| Section 112A LTCG Exemption Remaining | ₹125,000.00 | 0.0%            | Limit: ₹125,000 per financial year   |
| Total Unrealised LTCG (> 365 days)    | ₹46,027.02  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹46,027.02  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹2,364.89   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹136,963**, Tax savings potential: **₹18,736**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹736.70  | ₹1267.91   | ₹39,840             | LTCG/STCG | ₹5,003                |
| RELIND   |       42 | ₹1311.00 | ₹1906.06   | ₹24,993             | LTCG/STCG | ₹3,140                |
| LIC      |       45 | ₹408.00  | ₹895.05    | ₹21,917             | LTCG/STCG | ₹2,922                |
| WIPRO    |      170 | ₹194.55  | ₹304.31    | ₹18,659             | LTCG/STCG | ₹2,386                |
| ICIPSE   |      193 | ₹183.92  | ₹250.36    | ₹12,822             | STCG      | ₹2,564                |
| JSWENE   |       28 | ₹511.00  | ₹668.00    | ₹4,396              | LTCG      | ₹549                  |
| ICIGOL   |      250 | ₹120.86  | ₹138.24    | ₹4,345              | STCG      | ₹869                  |
| JIOFIN   |       28 | ₹222.27  | ₹344.38    | ₹3,419              | LTCG      | ₹427                  |
| ASHLEY   |       35 | ₹154.03  | ₹226.29    | ₹2,529              | LTCG      | ₹316                  |
| SJVLIM   |       67 | ₹56.05   | ₹86.95     | ₹2,070              | LTCG      | ₹259                  |

*Showing top 10 of 19 loss-harvest candidates.*


