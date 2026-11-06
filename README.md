# Orchestrated Multi-Agent Portfolio Audit - 2026-11-07

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-06
* **Portfolio XIRR**: **-4.59%** (Current Traded Positions Value: ₹506,277)
* **Benchmark XIRR**: **6.41%** (Simulated Benchmark Value: ₹655,355)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹19,335         | 37.80%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,780          | 35.02%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,248         | 30.79%  | Full                 |
| GAIL       |         61 |           61 | ₹11,345         | 17.50%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.93%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,226          | 15.77%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,328          | 15.61%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,965         | 14.25%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,433          | 11.97%  | Full                 |
| TATPOW     |          8 |            8 | ₹2,916          | 9.30%   | Full                 |
| DRREDD     |          6 |            6 | ₹8,196          | 8.96%   | Full                 |
| ICINIF     |         86 |           86 | ₹23,905         | 6.68%   | Full                 |
| TATGLO     |         30 |           30 | ₹32,331         | 6.40%   | Full                 |
| NTPC       |         12 |           12 | ₹3,764          | 4.64%   | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,799          | 2.68%   | Full                 |
| HINPET     |         14 |           14 | ₹5,321          | 1.65%   | Full                 |
| HDF250     |         24 |           24 | ₹4,251          | 1.62%   | Full                 |
| JSWENE     |         54 |           54 | ₹28,261         | 1.32%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,340          | -0.53%  | Full                 |
| ONGC       |         39 |           39 | ₹8,970          | -4.12%  | Full                 |
| ASHLEY     |        106 |           53 | ₹9,021          | -4.88%  | Partial (53/106 sh)  |
| MIR150     |        194 |          194 | ₹4,417          | -4.89%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.71%  | Full                 |
| RELIND     |         76 |           74 | ₹97,192         | -7.82%  | Partial (74/76 sh)   |
| HDFBAN     |        130 |           75 | ₹57,000         | -12.28% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,856          | -13.15% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,429          | -15.80% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹33,728         | -17.38% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹30,075         | -18.70% | Full                 |
| ICIPSE     |        193 |          193 | ₹35,811         | -35.78% | Full                 |
| LIC        |         80 |           45 | ₹18,360         | -51.76% | Partial (45/80 sh)   |

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
| RELIND     | Oil & Gas            | 15.3%    | +13.35%        | N/A             | SELL        | Exit all 76 sh (~₹99,818)        | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 15.1%    | +3.26%         | N/A             | SELL        | Exit all 130 sh (~₹98,800)       | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 6.7%     | -16.08%        | N/A             | SELL        | Exit all 220 sh (~₹43,648)       | Thesis invalidated: Price ₹198.40 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 5.5%     | -26.15%        | N/A             | SELL        | Exit all 193 sh (~₹35,811)       | Thesis invalidated: Price ₹185.55 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.0%     | -54.57%        | N/A             | SELL        | Exit all 80 sh (~₹32,640)        | Thesis invalidated: Price ₹408.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.0%     | +34.61%        | N/A             | SELL        | Exit all 30 sh (~₹32,331)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| BHAELE     | Defense              | 4.8%     | +150.33%       | ₹330.97         | SELL        | Exit all 80 sh (~₹31,608)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.6%     | -13.29%        | N/A             | SELL        | Exit all 250 sh (~₹30,075)       | Thesis invalidated: Price ₹120.30 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.3%     | +2.88%         | N/A             | SELL        | Exit all 54 sh (~₹28,261)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.7%     | +2.54%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹277.96 moving sideways between 50 DMA (₹262.92) and 200 DMA (₹270.53); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +56.01%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 3.0%     | +74.42%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹19,335)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| ASHLEY     | Auto                 | 2.8%     | +71.96%        | ₹148.26         | SELL        | Exit all 106 sh (~₹18,042)       | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| FEDBAN     | Banking              | 2.5%     | +125.83%       | ₹259.30         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +125.83%, position weight 2.5%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.5%     | +6.70%         | N/A             | SELL        | Exit all 46 sh (~₹16,001)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.9%     | -1.10%         | N/A             | SELL        | Exit all 53 sh (~₹12,170)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| NTPGRE     | Power                | 1.8%     | -22.51%        | N/A             | SELL        | Exit all 138 sh (~₹11,549)       | Thesis invalidated: Price ₹83.69 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +19.57%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +19.57%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -5.56%         | N/A             | SELL        | Exit all 39 sh (~₹8,970)         | Trend exit: month-end close ₹225.39 < 10-month average ₹254.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +15.02%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹1366.00 moving sideways between 50 DMA (₹1220.68) and 200 DMA (₹1243.70); conviction (5/5) thesis INTACT above invalidation (₹1009.47).                                                                                             | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +2.16%         | N/A             | SELL        | Exit all 14 sh (~₹5,321)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| NHPC       | Power                | 0.7%     | +37.97%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹80.60 moving sideways between 50 DMA (₹74.93) and 200 DMA (₹76.83); conviction (3/5) thesis INTACT above invalidation (₹53.75).                                                                                                     | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -1.81%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -1.77%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return -1.77%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +0.59%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹177.13 moving sideways between 50 DMA (₹179.67) and 200 DMA (₹171.10); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| SJVLIM     | Power                | 0.6%     | -34.30%        | N/A             | SELL        | Exit all 67 sh (~₹3,856)         | Thesis invalidated: Price ₹57.55 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| NTPC       | Power                | 0.6%     | +13.16%        | N/A             | SELL        | Exit all 12 sh (~₹3,764)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| GUJPPL     | Infrastructure       | 0.5%     | +88.90%        | ₹135.92         | HOLD        | Hold                             | Consolidation hold: Price ₹161.28 moving sideways between 50 DMA (₹163.81) and 200 DMA (₹156.32); conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                  | INTACT          |            3 |
| TATPOW     | Power                | 0.4%     | +28.57%        | N/A             | SELL        | Exit all 8 sh (~₹2,916)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +13.04%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹36.58 moving sideways between 50 DMA (₹33.42) and 200 DMA (₹33.83); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +88.59%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,328)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +0.64%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹59.95 moving sideways between 50 DMA (₹57.97) and 200 DMA (₹58.61); conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                     | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹279.36 vs 200-day average ₹272.66 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.3%
* **Banking**: 17.9%
* **Commodities**: 10.1%
* **Power**: 8.4%
* **IT**: 7.1%
* **Insurance**: 5.0%
* **Broad Market**: 5.0%
* **Consumption**: 5.0%
* **Defense**: 4.8%
* **Financial Services**: 4.3%
* **Consumer Electronics**: 3.5%
* **Telecom**: 3.0%
* **Auto**: 2.8%
* **Pharma**: 1.6%
* **Infrastructure**: 1.2%
* **Financials (combined)**: 27.2%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.7%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.8%), +7 more          |
| Financials        | 27.2%      | 25.0% | ⚠️ BREACH | FEDBAN (2.5%), HDFBAN (15.1%), KOTAKBKETF (0.3%), JIOFIN (1.9%), TATCAP (2.5%), +1 more |
| State-owned (PSU) | 19.2%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 10.1%      | 25.0% | OK        | ICIGOL (4.6%), ICIPSE (5.5%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 15.1%           | 15.63%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 15.3%           | 15.60%             | +0.31% via ICINIF                        |
| WIPRO    | 6.7%            | 6.68%              | Direct only                              |
| ICIPSE   | 5.5%            | 5.48%              | Direct only                              |
| LIC      | 5.0%            | 5.00%              | Direct only                              |
| TATGLO   | 5.0%            | 4.95%              | Direct only                              |
| BHAELE   | 4.8%            | 4.84%              | Direct only                              |
| ICIGOL   | 4.6%            | 4.61%              | Direct only                              |
| JSWENE   | 4.3%            | 4.33%              | Direct only                              |
| ICINIF   | 3.7%            | 3.66%              | Direct only                              |
| LGELEC   | 3.5%            | 3.54%              | Direct only                              |
| IDECEL   | 3.0%            | 2.96%              | Direct only                              |
| ASHLEY   | 2.8%            | 2.76%              | Direct only                              |
| FEDBAN   | 2.5%            | 2.50%              | +0.01% via KOTAKBKETF                    |
| TATCAP   | 2.5%            | 2.45%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.7%     | ₹23,905 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,417  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,251  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.3%    | ₹99,818 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 15.1%    | ₹98,800 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,196  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,764  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.7%     | ₹43,648 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.0%     | ₹32,640 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹23,120 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.8%     | ₹18,042 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.5%     | ₹16,248 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.5%     | ₹16,001 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹11,345 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,970  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,340  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,916  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,780  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,799  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 5.5%     | ₹35,811 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.0%     | ₹32,331 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹31,608 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.3%     | ₹28,261 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.9%     | ₹12,170 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.8%     | ₹11,549 | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,321  | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,433  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,856  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,226  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.6%     | ₹30,075 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 3.0%     | ₹19,335 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,328  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,799)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,328)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,780)  |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,916)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,226)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,856)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,251)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,340)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,417) |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,433)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,321)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹47,574.67  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹47,574.67  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹3,182.81   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹132,909**, Tax savings potential: **₹18,133**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹760.00  | ₹1455.47   | ₹38,251             | LTCG      | ₹4,781                |
| RELIND   |       42 | ₹1313.40 | ₹1906.06   | ₹24,892             | LTCG/STCG | ₹3,124                |
| LIC      |       45 | ₹408.00  | ₹895.05    | ₹21,917             | LTCG/STCG | ₹2,922                |
| WIPRO    |      170 | ₹198.40  | ₹304.31    | ₹18,005             | LTCG/STCG | ₹2,270                |
| ICIPSE   |      193 | ₹185.55  | ₹250.36    | ₹12,507             | STCG      | ₹2,501                |
| ICIGOL   |      250 | ₹120.30  | ₹138.24    | ₹4,485              | STCG      | ₹897                  |
| JSWENE   |       28 | ₹523.35  | ₹668.00    | ₹4,050              | LTCG      | ₹506                  |
| JIOFIN   |       28 | ₹229.62  | ₹344.38    | ₹3,213              | LTCG      | ₹402                  |
| ASHLEY   |       33 | ₹170.21  | ₹230.20    | ₹1,980              | LTCG      | ₹247                  |
| SJVLIM   |       67 | ₹57.55   | ₹86.95     | ₹1,970              | LTCG      | ₹246                  |

*Showing top 10 of 19 loss-harvest candidates.*


