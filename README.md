# Orchestrated Multi-Agent Portfolio Audit - 2026-11-24

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-24
* **Portfolio XIRR**: **-4.90%** (Current Traded Positions Value: ₹501,492)
* **Benchmark XIRR**: **7.62%** (Simulated Benchmark Value: ₹677,071)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| KOTAKBKETF |         30 |           30 | ₹1,951          | 35.09%  | Full                 |
| FEDBAN     |         48 |           48 | ₹17,270         | 32.72%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹17,865         | 30.05%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,696          | 22.32%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,498          | 17.70%  | Full                 |
| GAIL       |         61 |           61 | ₹11,322         | 16.53%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,349          | 15.66%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.48%  | Full                 |
| ICINIF     |         86 |           86 | ₹24,764         | 14.80%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,998         | 14.08%  | Partial (48/80 sh)   |
| DRREDD     |          6 |            6 | ₹8,281          | 9.34%   | Full                 |
| NHPC       |         55 |           55 | ₹4,145          | 9.26%   | Full                 |
| TATGLO     |         30 |           30 | ₹33,990         | 7.41%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,624          | 5.34%   | Full                 |
| NTPC       |         12 |           12 | ₹3,785          | 4.75%   | Full                 |
| HINPET     |         14 |           14 | ₹5,390          | 2.32%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,565          | 2.21%   | Full                 |
| HDF250     |         24 |           24 | ₹4,257          | 1.79%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,138         | -0.10%  | Full                 |
| MIR150     |        194 |          194 | ₹4,481          | -0.96%  | Full                 |
| ONGC       |         39 |           39 | ₹8,691          | -6.30%  | Full                 |
| RELIND     |         76 |           74 | ₹99,974         | -6.65%  | Partial (74/76 sh)   |
| ASHLEY     |        106 |           53 | ₹8,411          | -7.10%  | Partial (53/106 sh)  |
| GUJGA      |          7 |            7 | ₹2,808          | -7.51%  | Full                 |
| HDFBAN     |        130 |           75 | ₹61,335         | -10.42% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,682          | -14.29% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,152          | -17.04% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹31,839         | -19.42% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹26,673         | -30.20% | Full                 |
| ICIPSE     |        193 |          193 | ₹29,363         | -49.68% | Full                 |
| LIC        |         80 |           45 | ₹18,328         | -50.27% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 16.4%    | +11.11%        | N/A             | SELL        | Exit all 130 sh (~₹106,314)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 15.8%    | +16.60%        | N/A             | SELL        | Exit all 76 sh (~₹102,676)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.3%     | -20.78%        | N/A             | SELL        | Exit all 220 sh (~₹41,204)       | Thesis invalidated: Price ₹187.29 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.2%     | +41.52%        | N/A             | SELL        | Exit all 30 sh (~₹33,990)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| LIC        | Insurance            | 5.0%     | -54.64%        | N/A             | SELL        | Exit all 80 sh (~₹32,584)        | Thesis invalidated: Price ₹407.30 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| BHAELE     | Defense              | 4.9%     | +150.78%       | ₹330.97         | SELL        | Exit all 80 sh (~₹31,664)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIPSE     | Commodities          | 4.5%     | -39.45%        | N/A             | SELL        | Exit all 193 sh (~₹29,363)       | Thesis invalidated: Price ₹152.14 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| JSWENE     | Power                | 4.2%     | -1.21%         | N/A             | SELL        | Exit all 54 sh (~₹27,138)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.1%     | -23.10%        | N/A             | SELL        | Exit all 250 sh (~₹26,673)       | Thesis invalidated: Price ₹106.69 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| ICINIF     | Broad Market         | 3.8%     | +6.22%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹287.95 moving sideways between 50 DMA (₹266.82) and 200 DMA (₹270.59); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.6%     | +55.92%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.8%     | +61.16%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹17,865)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +140.04%       | ₹263.34         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +140.04%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.6%     | +60.34%        | ₹147.37         | SELL        | Exit all 106 sh (~₹16,822)       | Trend exit: month-end close ₹143.95 < 10-month average ₹165.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | +5.23%         | N/A             | SELL        | Exit all 46 sh (~₹15,780)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -5.38%         | N/A             | SELL        | Exit all 53 sh (~₹11,644)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| NTPGRE     | Power                | 1.7%     | -23.80%        | N/A             | SELL        | Exit all 138 sh (~₹11,357)       | Thesis invalidated: Price ₹82.30 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +19.32%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +19.32%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.3%     | -8.49%         | N/A             | SELL        | Exit all 39 sh (~₹8,691)         | Trend exit: month-end close ₹217.71 < 10-month average ₹245.69. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +16.21%        | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +3.49%         | N/A             | SELL        | Exit all 14 sh (~₹5,390)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +3.31%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +3.31%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | -0.39%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹23.10 moving sideways between 50 DMA (₹22.54) and 200 DMA (₹22.67); conviction (4/5) thesis INTACT above invalidation (₹20.41).                                                                                                     | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +0.74%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹177.39 moving sideways between 50 DMA (₹178.07) and 200 DMA (₹172.16); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +29.00%        | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹75.36 < 200 DMA (₹76.83) with return +29.00%; thesis remains INTACT above invalidation (₹53.75).                                                                                                                                         | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +13.79%        | N/A             | SELL        | Exit all 12 sh (~₹3,785)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -37.25%        | N/A             | SELL        | Exit all 67 sh (~₹3,682)         | Thesis invalidated: Price ₹54.96 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +104.83%       | ₹133.52         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +104.83%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                               | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +9.64%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +9.64%, position weight 0.4%; conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                                 | INTACT          |            4 |
| TATPOW     | Power                | 0.4%     | +15.68%        | N/A             | SELL        | Exit all 8 sh (~₹2,624)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +90.31%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,349)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +9.18%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +9.18%, position weight 0.3%; conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                                 | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹289.43 vs 200-day average ₹272.69 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.9%
* **Banking**: 19.3%
* **Commodities**: 8.6%
* **Power**: 8.1%
* **IT**: 6.8%
* **Consumption**: 5.2%
* **Broad Market**: 5.2%
* **Insurance**: 5.0%
* **Defense**: 4.9%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.6%
* **Telecom**: 2.8%
* **Auto**: 2.6%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 28.6%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 29.0%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| Financials        | 28.6%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (16.4%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.2%      | 25.0% | OK        | ONGC (1.3%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 8.6%       | 25.0% | OK        | ICIGOL (4.1%), ICIPSE (4.5%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 16.4%           | 16.89%             | +0.44% via ICINIF, +0.09% via KOTAKBKETF |
| RELIND   | 15.8%           | 16.13%             | +0.32% via ICINIF                        |
| WIPRO    | 6.3%            | 6.34%              | Direct only                              |
| TATGLO   | 5.2%            | 5.23%              | Direct only                              |
| LIC      | 5.0%            | 5.02%              | Direct only                              |
| BHAELE   | 4.9%            | 4.87%              | Direct only                              |
| ICIPSE   | 4.5%            | 4.52%              | Direct only                              |
| JSWENE   | 4.2%            | 4.18%              | Direct only                              |
| ICIGOL   | 4.1%            | 4.11%              | Direct only                              |
| ICINIF   | 3.8%            | 3.81%              | Direct only                              |
| LGELEC   | 3.6%            | 3.56%              | Direct only                              |
| IDECEL   | 2.8%            | 2.75%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.67%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.6%            | 2.59%              | Direct only                              |
| TATCAP   | 2.4%            | 2.43%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.2%** (Target: 50.0%, Gap: +44.8%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **94.8%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.8%     | ₹24,764 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,481  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,257  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 16.4%    | ₹106,314 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.8%    | ₹102,676 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,281   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,785   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.3%     | ₹41,204  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.0%     | ₹32,584  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.6%     | ₹23,108  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹17,270  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.6%     | ₹16,822  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹15,780  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹11,322  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.3%     | ₹8,691   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,565   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,696   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,624   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,951   | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.2%     | ₹33,990  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹31,664  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 4.5%     | ₹29,363  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹27,138  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,644  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,357  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,390   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹4,145   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,682   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,498   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.1%     | ₹26,673  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.8%     | ₹17,865  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,349   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,951)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,349)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,624)   |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,696)  |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,498)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,682)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹4,145)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,257)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,481) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,565)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,390)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹48,864.83  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹48,864.83  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹6,039.09   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹141,840**, Tax savings potential: **₹19,902**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹817.80  | ₹1455.47   | ₹35,072             | LTCG      | ₹4,384                |
| RELIND   |       27 | ₹1351.00 | ₹2228.99   | ₹23,706             | LTCG      | ₹2,963                |
| LIC      |       45 | ₹407.30  | ₹895.05    | ₹21,949             | LTCG      | ₹2,744                |
| WIPRO    |      170 | ₹187.29  | ₹304.31    | ₹19,894             | LTCG/STCG | ₹2,606                |
| ICIPSE   |      193 | ₹152.14  | ₹250.36    | ₹18,956             | STCG      | ₹3,791                |
| ICIGOL   |      250 | ₹106.69  | ₹138.24    | ₹7,887              | STCG      | ₹1,577                |
| JSWENE   |       28 | ₹502.55  | ₹668.00    | ₹4,633              | LTCG      | ₹579                  |
| JIOFIN   |       28 | ₹219.70  | ₹344.38    | ₹3,491              | LTCG      | ₹436                  |
| ASHLEY   |       35 | ₹158.70  | ₹226.29    | ₹2,366              | LTCG      | ₹296                  |
| SJVLIM   |       67 | ₹54.96   | ₹86.95     | ₹2,143              | LTCG      | ₹268                  |

*Showing top 10 of 17 loss-harvest candidates.*


