# Orchestrated Multi-Agent Portfolio Audit - 2026-11-26

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-26
* **Portfolio XIRR**: **-4.23%** (Current Traded Positions Value: ₹509,285)
* **Benchmark XIRR**: **8.45%** (Simulated Benchmark Value: ₹691,356)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| KOTAKBKETF |         30 |           30 | ₹1,984          | 42.05%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,814          | 33.72%  | Full                 |
| FEDBAN     |         48 |           48 | ₹17,129         | 32.33%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹17,400         | 27.87%  | Full                 |
| ICINIF     |         86 |           86 | ₹25,158         | 18.75%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,566          | 18.18%  | Full                 |
| GAIL       |         61 |           61 | ₹11,468         | 17.68%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.43%  | Full                 |
| BHAELE     |         80 |           48 | ₹19,416         | 14.82%  | Partial (48/80 sh)   |
| SEQSCI     |         10 |           10 | ₹2,274          | 14.81%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,352          | 9.84%   | Full                 |
| NHPC       |         55 |           55 | ₹4,175          | 9.51%   | Full                 |
| TATGLO     |         30 |           30 | ₹34,920         | 7.99%   | Full                 |
| NTPC       |         12 |           12 | ₹3,843          | 5.28%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,588          | 4.84%   | Full                 |
| HDF250     |         24 |           24 | ₹4,297          | 4.03%   | Full                 |
| HINPET     |         14 |           14 | ₹5,399          | 2.40%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,570          | 2.27%   | Full                 |
| MIR150     |        194 |          194 | ₹4,499          | -0.04%  | Full                 |
| JSWENE     |         54 |           54 | ₹26,198         | -1.31%  | Full                 |
| RELIND     |         76 |           74 | ₹103,319        | -5.45%  | Partial (74/76 sh)   |
| ONGC       |         39 |           39 | ₹8,692          | -6.27%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.49%  | Full                 |
| ASHLEY     |        106 |           53 | ₹8,276          | -7.61%  | Partial (53/106 sh)  |
| HDFBAN     |        130 |           75 | ₹64,650         | -9.17%  | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,688          | -14.22% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,356          | -15.87% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹33,412         | -17.34% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹26,202         | -31.70% | Full                 |
| LIC        |         80 |           45 | ₹18,450         | -49.81% | Partial (45/80 sh)   |
| ICIPSE     |        193 |          193 | ₹28,518         | -51.41% | Full                 |

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
| HDFBAN     | Banking              | 17.0%    | +17.12%        | N/A             | SELL        | Exit all 130 sh (~₹112,060)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 16.1%    | +20.50%        | N/A             | SELL        | Exit all 76 sh (~₹106,111)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.5%     | -16.86%        | N/A             | SELL        | Exit all 220 sh (~₹43,239)       | Thesis invalidated: Price ₹196.54 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.3%     | +45.39%        | N/A             | SELL        | Exit all 30 sh (~₹34,920)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| LIC        | Insurance            | 5.0%     | -54.34%        | N/A             | SELL        | Exit all 80 sh (~₹32,800)        | Thesis invalidated: Price ₹410.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| BHAELE     | Defense              | 4.9%     | +156.29%       | ₹330.97         | SELL        | Exit all 80 sh (~₹32,360)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIPSE     | Commodities          | 4.3%     | -41.19%        | N/A             | SELL        | Exit all 193 sh (~₹28,518)       | Thesis invalidated: Price ₹147.76 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| ICIGOL     | Commodities          | 4.0%     | -24.46%        | N/A             | SELL        | Exit all 250 sh (~₹26,202)       | Thesis invalidated: Price ₹104.81 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.0%     | -4.63%         | N/A             | SELL        | Exit all 54 sh (~₹26,198)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.8%     | +7.91%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹292.53 moving sideways between 50 DMA (₹267.89) and 200 DMA (₹270.58); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +54.22%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.6%     | +56.97%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹17,400)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| FEDBAN     | Banking              | 2.6%     | +138.07%       | ₹263.34         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +138.07%, position weight 2.6%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +57.76%        | ₹147.37         | SELL        | Exit all 106 sh (~₹16,552)       | Trend exit: month-end close ₹143.95 < 10-month average ₹165.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | +7.45%         | N/A             | SELL        | Exit all 46 sh (~₹16,114)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -2.23%         | N/A             | SELL        | Exit all 53 sh (~₹12,031)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +20.86%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +20.86%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| NTPGRE     | Power                | 1.7%     | -23.70%        | N/A             | SELL        | Exit all 138 sh (~₹11,371)       | Thesis invalidated: Price ₹82.40 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| ONGC       | Oil & Gas            | 1.3%     | -8.48%         | N/A             | SELL        | Exit all 39 sh (~₹8,692)         | Trend exit: month-end close ₹217.71 < 10-month average ₹245.69. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +17.21%        | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +3.67%         | N/A             | SELL        | Exit all 14 sh (~₹5,399)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +3.44%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +3.44%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | +0.00%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹23.19 moving sideways between 50 DMA (₹22.52) and 200 DMA (₹22.69); conviction (4/5) thesis INTACT above invalidation (₹20.41).                                                                                                     | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +1.68%         | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +29.92%        | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹75.90 < 200 DMA (₹76.83) with return +29.92%; thesis remains INTACT above invalidation (₹53.75).                                                                                                                                         | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +15.52%        | N/A             | SELL        | Exit all 12 sh (~₹3,843)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -37.16%        | N/A             | SELL        | Exit all 67 sh (~₹3,688)         | Thesis invalidated: Price ₹55.04 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +108.81%       | ₹133.52         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +108.81%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                               | INTACT          |            3 |
| NIPNIT     | IT                   | 0.4%     | +14.40%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +14.40%, position weight 0.4%; conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                                | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.4%     | +14.09%        | N/A             | SELL        | Exit all 8 sh (~₹2,588)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.3%     | +84.24%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,274)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +11.01%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +11.01%, position weight 0.3%; conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                                | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹295.33 vs 200-day average ₹272.79 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 21.0%
* **Banking**: 19.8%
* **Commodities**: 8.3%
* **Power**: 7.8%
* **IT**: 7.0%
* **Consumption**: 5.3%
* **Broad Market**: 5.1%
* **Insurance**: 5.0%
* **Defense**: 4.9%
* **Financial Services**: 4.3%
* **Consumer Electronics**: 3.5%
* **Telecom**: 2.6%
* **Auto**: 2.5%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 29.1%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Financials        | 29.1%      | 25.0% | ⚠️ BREACH | FEDBAN (2.6%), HDFBAN (17.0%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| Energy & Power    | 28.9%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| State-owned (PSU) | 19.1%      | 25.0% | OK        | ONGC (1.3%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 8.3%       | 25.0% | OK        | ICIGOL (4.0%), ICIPSE (4.3%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 17.0%           | 17.48%             | +0.44% via ICINIF, +0.09% via KOTAKBKETF |
| RELIND   | 16.1%           | 16.38%             | +0.32% via ICINIF                        |
| WIPRO    | 6.5%            | 6.54%              | Direct only                              |
| TATGLO   | 5.3%            | 5.28%              | Direct only                              |
| LIC      | 5.0%            | 4.96%              | Direct only                              |
| BHAELE   | 4.9%            | 4.90%              | Direct only                              |
| ICIPSE   | 4.3%            | 4.31%              | Direct only                              |
| ICIGOL   | 4.0%            | 3.96%              | Direct only                              |
| JSWENE   | 4.0%            | 3.96%              | Direct only                              |
| ICINIF   | 3.8%            | 3.81%              | Direct only                              |
| LGELEC   | 3.5%            | 3.46%              | Direct only                              |
| IDECEL   | 2.6%            | 2.63%              | Direct only                              |
| FEDBAN   | 2.6%            | 2.60%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.50%              | Direct only                              |
| TATCAP   | 2.4%            | 2.44%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.1%** (Target: 50.0%, Gap: +44.9%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **94.9%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.8%     | ₹25,158 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,499  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,297  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 17.0%    | ₹112,060 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 16.1%    | ₹106,111 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,352   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,843   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.5%     | ₹43,239  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.0%     | ₹32,800  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹22,855  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.6%     | ₹17,129  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹16,552  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹16,114  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹11,468  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.3%     | ₹8,692   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,570   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,814   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,588   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,984   | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.3%     | ₹34,920  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹32,360  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 4.3%     | ₹28,518  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.0%     | ₹26,198  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹12,031  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,371  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,399   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹4,175   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,688   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,566   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.0%     | ₹26,202  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.6%     | ₹17,400  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.3%     | ₹2,274   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,984)  |
| SEQSCI     | Pharma         | 0.3%     |            2 | Exit all 10 sh (~₹2,274)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,588)   |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,814)  |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,566)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,688)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹4,175)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,297)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,499) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,570)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,399)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹50,261.03  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹50,261.03  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹8,720.16   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹138,124**, Tax savings potential: **₹19,451**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹862.00  | ₹1455.47   | ₹32,641             | LTCG      | ₹4,080                |
| RELIND   |       27 | ₹1396.20 | ₹2228.99   | ₹22,485             | LTCG      | ₹2,811                |
| LIC      |       45 | ₹410.00  | ₹895.05    | ₹21,827             | LTCG      | ₹2,728                |
| ICIPSE   |      193 | ₹147.76  | ₹250.36    | ₹19,801             | STCG      | ₹3,960                |
| WIPRO    |      170 | ₹196.54  | ₹304.31    | ₹18,321             | LTCG/STCG | ₹2,326                |
| ICIGOL   |      250 | ₹104.81  | ₹138.24    | ₹8,358              | STCG      | ₹1,672                |
| JSWENE   |       28 | ₹485.15  | ₹668.00    | ₹5,120              | LTCG      | ₹640                  |
| JIOFIN   |       28 | ₹227.00  | ₹344.38    | ₹3,287              | LTCG      | ₹411                  |
| ASHLEY   |       35 | ₹156.15  | ₹226.29    | ₹2,455              | LTCG      | ₹307                  |
| SJVLIM   |       67 | ₹55.04   | ₹86.95     | ₹2,138              | LTCG      | ₹267                  |

*Showing top 10 of 17 loss-harvest candidates.*


