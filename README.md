# Orchestrated Multi-Agent Portfolio Audit - 2026-11-19

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-19
* **Portfolio XIRR**: **-4.32%** (Current Traded Positions Value: ₹508,631)
* **Benchmark XIRR**: **7.93%** (Simulated Benchmark Value: ₹681,469)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| KOTAKBKETF |         30 |           30 | ₹1,964          | 40.45%  | Full                 |
| FEDBAN     |         48 |           48 | ₹17,496         | 33.41%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹18,165         | 31.68%  | Full                 |
| GAIL       |         61 |           61 | ₹11,718         | 20.10%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,566          | 18.27%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,358          | 15.81%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.60%  | Full                 |
| BHAELE     |         80 |           48 | ₹19,402         | 14.89%  | Partial (48/80 sh)   |
| NIPNIT     |         76 |           76 | ₹2,612          | 14.58%  | Full                 |
| ICINIF     |         86 |           86 | ₹24,619         | 13.74%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,405          | 10.35%  | Full                 |
| NHPC       |         55 |           55 | ₹4,197          | 9.77%   | Full                 |
| TATGLO     |         30 |           30 | ₹34,320         | 7.64%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,720          | 6.65%   | Full                 |
| NTPC       |         12 |           12 | ₹3,900          | 5.84%   | Full                 |
| HDF250     |         24 |           24 | ₹4,311          | 5.04%   | Full                 |
| HINPET     |         14 |           14 | ₹5,460          | 3.05%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,631          | 3.03%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,810         | 0.74%   | Full                 |
| MIR150     |        194 |          194 | ₹4,491          | -0.47%  | Full                 |
| ASHLEY     |        106 |           53 | ₹8,806          | -5.62%  | Partial (53/106 sh)  |
| ONGC       |         39 |           39 | ₹8,756          | -5.82%  | Full                 |
| RELIND     |         76 |           74 | ₹101,794        | -6.02%  | Partial (74/76 sh)   |
| GUJGA      |          7 |            7 | ₹2,808          | -7.57%  | Full                 |
| HDFBAN     |        130 |           75 | ₹61,635         | -10.34% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,765          | -13.70% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,350          | -16.02% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹31,268         | -20.33% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹27,532         | -27.50% | Full                 |
| ICIPSE     |        193 |          193 | ₹30,720         | -47.09% | Full                 |
| LIC        |         80 |           45 | ₹18,185         | -51.05% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 16.3%    | +11.66%        | N/A             | SELL        | Exit all 130 sh (~₹106,834)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 15.9%    | +18.72%        | N/A             | SELL        | Exit all 76 sh (~₹104,546)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.2%     | -22.20%        | N/A             | SELL        | Exit all 220 sh (~₹40,465)       | Thesis invalidated: Price ₹183.93 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.2%     | +42.89%        | N/A             | SELL        | Exit all 30 sh (~₹34,320)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| BHAELE     | Defense              | 4.9%     | +156.10%       | ₹330.97         | SELL        | Exit all 80 sh (~₹32,336)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| LIC        | Insurance            | 4.9%     | -55.00%        | N/A             | SELL        | Exit all 80 sh (~₹32,328)        | Thesis invalidated: Price ₹404.10 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 4.7%     | -36.65%        | N/A             | SELL        | Exit all 193 sh (~₹30,720)       | Thesis invalidated: Price ₹159.17 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| JSWENE     | Power                | 4.2%     | +1.24%         | N/A             | SELL        | Exit all 54 sh (~₹27,810)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.2%     | -20.62%        | N/A             | SELL        | Exit all 250 sh (~₹27,532)       | Thesis invalidated: Price ₹110.13 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| ICINIF     | Broad Market         | 3.7%     | +5.60%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹286.27 moving sideways between 50 DMA (₹265.38) and 200 DMA (₹270.58); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.4%     | +50.54%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.8%     | +63.87%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹18,165)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| ASHLEY     | Auto                 | 2.7%     | +67.86%        | ₹148.26         | SELL        | Exit all 106 sh (~₹17,612)       | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| FEDBAN     | Banking              | 2.7%     | +143.18%       | ₹259.30         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +143.18%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | +6.00%         | N/A             | SELL        | Exit all 46 sh (~₹15,895)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -2.32%         | N/A             | SELL        | Exit all 53 sh (~₹12,020)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.8%     | +23.50%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +23.50%, position weight 1.8%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| NTPGRE     | Power                | 1.7%     | -23.63%        | N/A             | SELL        | Exit all 138 sh (~₹11,382)       | Thesis invalidated: Price ₹82.48 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| ONGC       | Oil & Gas            | 1.3%     | -7.81%         | N/A             | SELL        | Exit all 39 sh (~₹8,756)         | Trend exit: month-end close ₹217.71 < 10-month average ₹245.69. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +17.96%        | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +4.84%         | N/A             | SELL        | Exit all 14 sh (~₹5,460)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +4.82%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +4.82%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | -0.17%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹23.15 moving sideways between 50 DMA (₹22.55) and 200 DMA (₹22.66); conviction (4/5) thesis INTACT above invalidation (₹20.41).                                                                                                     | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +2.00%         | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +30.61%        | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹76.30 < 200 DMA (₹76.85) with return +30.61%; thesis remains INTACT above invalidation (₹53.75).                                                                                                                                         | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +17.23%        | N/A             | SELL        | Exit all 12 sh (~₹3,900)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -35.84%        | N/A             | SELL        | Exit all 67 sh (~₹3,765)         | Thesis invalidated: Price ₹56.20 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +108.81%       | ₹133.52         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +108.81%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                               | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.4%     | +19.91%        | N/A             | SELL        | Exit all 8 sh (~₹2,720)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +6.21%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +6.21%, position weight 0.4%; conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                                 | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +91.04%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,358)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +9.92%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹65.48 moving sideways between 50 DMA (₹58.66) and 200 DMA (₹58.73); conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                     | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹290.61 vs 200-day average ₹272.64 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 21.0%
* **Banking**: 19.2%
* **Commodities**: 8.9%
* **Power**: 8.2%
* **IT**: 6.6%
* **Consumption**: 5.2%
* **Broad Market**: 5.1%
* **Defense**: 4.9%
* **Insurance**: 4.9%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.4%
* **Telecom**: 2.8%
* **Auto**: 2.7%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 28.4%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 29.2%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| Financials        | 28.4%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (16.3%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.2%      | 25.0% | OK        | ONGC (1.3%), GAIL (1.8%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 8.9%       | 25.0% | OK        | ICIGOL (4.2%), ICIPSE (4.7%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 16.3%           | 16.78%             | +0.43% via ICINIF, +0.09% via KOTAKBKETF |
| RELIND   | 15.9%           | 16.23%             | +0.32% via ICINIF                        |
| WIPRO    | 6.2%            | 6.16%              | Direct only                              |
| TATGLO   | 5.2%            | 5.22%              | Direct only                              |
| BHAELE   | 4.9%            | 4.92%              | Direct only                              |
| LIC      | 4.9%            | 4.92%              | Direct only                              |
| ICIPSE   | 4.7%            | 4.68%              | Direct only                              |
| JSWENE   | 4.2%            | 4.23%              | Direct only                              |
| ICIGOL   | 4.2%            | 4.19%              | Direct only                              |
| ICINIF   | 3.7%            | 3.75%              | Direct only                              |
| LGELEC   | 3.4%            | 3.40%              | Direct only                              |
| IDECEL   | 2.8%            | 2.77%              | Direct only                              |
| ASHLEY   | 2.7%            | 2.68%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.67%              | +0.01% via KOTAKBKETF                    |
| TATCAP   | 2.4%            | 2.42%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.1%** (Target: 50.0%, Gap: +44.9%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **94.9%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.7%     | ₹24,619 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,491  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,311  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 16.3%    | ₹106,834 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.9%    | ₹104,546 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,405   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,900   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.2%     | ₹40,465  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 4.9%     | ₹32,328  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.4%     | ₹22,311  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.7%     | ₹17,612  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹17,496  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹15,895  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.8%     | ₹11,718  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.3%     | ₹8,756   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,631   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,720   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,612   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,964   | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.2%     | ₹34,320  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹32,336  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 4.7%     | ₹30,720  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹27,810  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹12,020  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,382  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,460   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹4,197   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,765   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,566   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.2%     | ₹27,532  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.8%     | ₹18,165  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,358   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,964)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,358)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,612)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,720)   |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,566)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,765)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹4,197)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,311)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,491) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,631)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,460)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹51,786.93  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹51,786.93  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹6,816.02   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹138,400**, Tax savings potential: **₹19,331**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹821.80  | ₹1455.47   | ₹34,852             | LTCG      | ₹4,357                |
| RELIND   |       27 | ₹1375.60 | ₹2228.99   | ₹23,042             | LTCG      | ₹2,880                |
| LIC      |       45 | ₹404.10  | ₹895.05    | ₹22,093             | LTCG      | ₹2,762                |
| WIPRO    |      170 | ₹183.93  | ₹304.31    | ₹20,465             | LTCG/STCG | ₹2,708                |
| ICIPSE   |      193 | ₹159.17  | ₹250.36    | ₹17,599             | STCG      | ₹3,520                |
| ICIGOL   |      250 | ₹110.13  | ₹138.24    | ₹7,028              | STCG      | ₹1,406                |
| JSWENE   |       28 | ₹515.00  | ₹668.00    | ₹4,284              | LTCG      | ₹535                  |
| JIOFIN   |       28 | ₹226.80  | ₹344.38    | ₹3,292              | LTCG      | ₹412                  |
| ASHLEY   |       33 | ₹166.15  | ₹230.20    | ₹2,114              | LTCG      | ₹264                  |
| SJVLIM   |       67 | ₹56.20   | ₹86.95     | ₹2,060              | LTCG      | ₹258                  |

*Showing top 10 of 18 loss-harvest candidates.*


