# Orchestrated Multi-Agent Portfolio Audit - 2026-11-11

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-11
* **Portfolio XIRR**: **-3.88%** (Current Traded Positions Value: ₹514,398)
* **Benchmark XIRR**: **7.57%** (Simulated Benchmark Value: ₹674,544)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹19,320         | 37.36%  | Full                 |
| FEDBAN     |         48 |           48 | ₹17,357         | 33.34%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,718          | 26.75%  | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,883          | 22.66%  | Full                 |
| GAIL       |         61 |           61 | ₹11,584         | 19.35%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,546          | 17.91%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,397          | 17.08%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.80%  | Full                 |
| BHAELE     |         80 |           48 | ₹19,152         | 14.54%  | Partial (48/80 sh)   |
| ICINIF     |         86 |           86 | ₹24,361         | 11.58%  | Full                 |
| NHPC       |         55 |           55 | ₹4,285          | 10.62%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,262          | 9.39%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,880          | 8.79%   | Full                 |
| TATGLO     |         30 |           30 | ₹32,790         | 6.68%   | Full                 |
| NTPC       |         12 |           12 | ₹3,924          | 6.10%   | Full                 |
| HINPET     |         14 |           14 | ₹5,602          | 4.54%   | Full                 |
| HDF250     |         24 |           24 | ₹4,296          | 4.43%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,617          | 2.89%   | Full                 |
| JSWENE     |         54 |           54 | ₹28,053         | 1.06%   | Full                 |
| MIR150     |        194 |          194 | ₹4,478          | -1.28%  | Full                 |
| ONGC       |         39 |           39 | ₹9,157          | -2.47%  | Full                 |
| ASHLEY     |        106 |           53 | ₹9,217          | -4.13%  | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹98,820         | -7.17%  | Partial (74/76 sh)   |
| GUJGA      |          7 |            7 | ₹2,808          | -7.65%  | Full                 |
| HDFBAN     |        130 |           75 | ₹60,495         | -10.83% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,991          | -12.08% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,457          | -15.57% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹33,658         | -17.36% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹29,858         | -19.23% | Full                 |
| ICIPSE     |        193 |          193 | ₹35,568         | -35.85% | Full                 |
| LIC        |         80 |           45 | ₹18,000         | -52.20% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 15.8%    | +9.59%         | N/A             | SELL        | Exit all 130 sh (~₹104,858)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 15.3%    | +15.25%        | N/A             | SELL        | Exit all 76 sh (~₹101,490)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.6%     | -16.25%        | N/A             | SELL        | Exit all 220 sh (~₹43,558)       | Thesis invalidated: Price ₹197.99 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 5.4%     | -26.65%        | N/A             | SELL        | Exit all 193 sh (~₹35,568)       | Thesis invalidated: Price ₹184.29 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| TATGLO     | Consumption          | 4.9%     | +36.52%        | N/A             | SELL        | Exit all 30 sh (~₹32,790)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| LIC        | Insurance            | 4.8%     | -55.46%        | N/A             | SELL        | Exit all 80 sh (~₹32,000)        | Thesis invalidated: Price ₹400.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| BHAELE     | Defense              | 4.8%     | +152.80%       | ₹330.97         | SELL        | Exit all 80 sh (~₹31,920)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.5%     | -13.92%        | N/A             | SELL        | Exit all 250 sh (~₹29,858)       | Thesis invalidated: Price ₹119.43 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.2%     | +2.12%         | N/A             | SELL        | Exit all 54 sh (~₹28,053)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.7%     | +4.50%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹283.27 moving sideways between 50 DMA (₹263.47) and 200 DMA (₹270.52); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.4%     | +52.68%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +74.29%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹19,320)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| ASHLEY     | Auto                 | 2.8%     | +75.69%        | ₹148.26         | SELL        | Exit all 106 sh (~₹18,433)       | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| FEDBAN     | Banking              | 2.6%     | +141.24%       | ₹259.30         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +141.24%, position weight 2.6%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.5%     | +9.25%         | N/A             | SELL        | Exit all 46 sh (~₹16,383)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -0.68%         | N/A             | SELL        | Exit all 53 sh (~₹12,222)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +22.08%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +22.08%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| NTPGRE     | Power                | 1.7%     | -22.69%        | N/A             | SELL        | Exit all 138 sh (~₹11,523)       | Thesis invalidated: Price ₹83.50 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| ONGC       | Oil & Gas            | 1.4%     | -3.58%         | N/A             | SELL        | Exit all 39 sh (~₹9,157)         | Trend exit: month-end close ₹225.39 < 10-month average ₹254.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.2%     | +15.95%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹1377.00 moving sideways between 50 DMA (₹1232.33) and 200 DMA (₹1246.75); conviction (5/5) thesis INTACT above invalidation (₹1009.47).                                                                                             | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +7.56%         | N/A             | SELL        | Exit all 14 sh (~₹5,602)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +4.50%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +4.50%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | -0.47%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return -0.47%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹20.41).                                                                                                                 | INTACT          |            4 |
| HDF250     | Broad Market         | 0.6%     | +1.66%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹179.02 moving sideways between 50 DMA (₹179.15) and 200 DMA (₹171.30); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +33.34%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹77.90 moving sideways between 50 DMA (₹75.15) and 200 DMA (₹76.84); conviction (3/5) thesis INTACT above invalidation (₹53.75).                                                                                                     | INTACT          |            3 |
| SJVLIM     | Power                | 0.6%     | -32.00%        | N/A             | SELL        | Exit all 67 sh (~₹3,991)         | Thesis invalidated: Price ₹59.56 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| NTPC       | Power                | 0.6%     | +17.95%        | N/A             | SELL        | Exit all 12 sh (~₹3,924)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| GUJPPL     | Infrastructure       | 0.5%     | +98.91%        | ₹135.92         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +98.91%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                                | INTACT          |            3 |
| TATPOW     | Power                | 0.4%     | +26.97%        | N/A             | SELL        | Exit all 8 sh (~₹2,880)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +10.51%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹35.76 moving sideways between 50 DMA (₹33.56) and 200 DMA (₹33.74); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +106.27%       | ₹208.60         | SELL        | Exit all 10 sh (~₹2,546)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +5.37%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹62.77 moving sideways between 50 DMA (₹58.11) and 200 DMA (₹58.62); conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                     | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹286.54 vs 200-day average ₹272.57 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.4%
* **Banking**: 18.7%
* **Commodities**: 9.9%
* **Power**: 8.2%
* **IT**: 7.0%
* **Broad Market**: 5.0%
* **Consumption**: 4.9%
* **Insurance**: 4.8%
* **Defense**: 4.8%
* **Financial Services**: 4.3%
* **Consumer Electronics**: 3.4%
* **Telecom**: 2.9%
* **Auto**: 2.8%
* **Pharma**: 1.6%
* **Infrastructure**: 1.2%
* **Financials (combined)**: 27.8%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.6%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| Financials        | 27.8%      | 25.0% | ⚠️ BREACH | FEDBAN (2.6%), HDFBAN (15.8%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.5%), +1 more |
| State-owned (PSU) | 19.0%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 9.9%       | 25.0% | OK        | ICIGOL (4.5%), ICIPSE (5.4%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 15.8%           | 16.31%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 15.3%           | 15.61%             | +0.31% via ICINIF                        |
| WIPRO    | 6.6%            | 6.56%              | Direct only                              |
| ICIPSE   | 5.4%            | 5.36%              | Direct only                              |
| TATGLO   | 4.9%            | 4.94%              | Direct only                              |
| LIC      | 4.8%            | 4.82%              | Direct only                              |
| BHAELE   | 4.8%            | 4.81%              | Direct only                              |
| ICIGOL   | 4.5%            | 4.50%              | Direct only                              |
| JSWENE   | 4.2%            | 4.23%              | Direct only                              |
| ICINIF   | 3.7%            | 3.67%              | Direct only                              |
| LGELEC   | 3.4%            | 3.41%              | Direct only                              |
| IDECEL   | 2.9%            | 2.91%              | Direct only                              |
| ASHLEY   | 2.8%            | 2.78%              | Direct only                              |
| FEDBAN   | 2.6%            | 2.62%              | +0.01% via KOTAKBKETF                    |
| TATCAP   | 2.5%            | 2.47%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.7%     | ₹24,361 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,478  |            4 |
| HDF250   | Index ETF (Core) | 0.6%     | ₹4,296  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 15.8%    | ₹104,858 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.3%    | ₹101,490 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.2%     | ₹8,262   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,924   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.6%     | ₹43,558  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 4.8%     | ₹32,000  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.4%     | ₹22,628  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.8%     | ₹18,433  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.6%     | ₹17,357  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.5%     | ₹16,383  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹11,584  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹9,157   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,617   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,880   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,718   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,883   | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 5.4%     | ₹35,568  | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.9%     | ₹32,790  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹31,920  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹28,053  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹12,222  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,523  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,602   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹4,285   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,991   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,397   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.5%     | ₹29,858  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹19,320  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,546   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,883)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,546)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,718)  |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,880)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,397)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,991)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹4,285)  |
| HDF250     | Broad Market   | 0.6%     |            4 | Exit all 24 sh (~₹4,296)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,478) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,617)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,602)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹50,639.39  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹50,639.39  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹5,193.90   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹129,864**, Tax savings potential: **₹17,583**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹806.60  | ₹1455.47   | ₹35,688             | LTCG      | ₹4,461                |
| RELIND   |       32 | ₹1335.40 | ₹2089.85   | ₹24,142             | LTCG/STCG | ₹3,019                |
| LIC      |       45 | ₹400.00  | ₹895.05    | ₹22,277             | LTCG      | ₹2,785                |
| WIPRO    |      170 | ₹197.99  | ₹304.31    | ₹18,075             | LTCG/STCG | ₹2,282                |
| ICIPSE   |      193 | ₹184.29  | ₹250.36    | ₹12,751             | STCG      | ₹2,550                |
| ICIGOL   |      250 | ₹119.43  | ₹138.24    | ₹4,702              | STCG      | ₹940                  |
| JSWENE   |       28 | ₹519.50  | ₹668.00    | ₹4,158              | LTCG      | ₹520                  |
| JIOFIN   |       28 | ₹230.60  | ₹344.38    | ₹3,186              | LTCG      | ₹398                  |
| ASHLEY   |       33 | ₹173.90  | ₹230.20    | ₹1,858              | LTCG      | ₹232                  |
| SJVLIM   |       67 | ₹59.56   | ₹86.95     | ₹1,835              | LTCG      | ₹229                  |

*Showing top 10 of 17 loss-harvest candidates.*


