# Orchestrated Multi-Agent Portfolio Audit - 2026-11-16

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-16
* **Portfolio XIRR**: **-4.31%** (Current Traded Positions Value: ₹508,929)
* **Benchmark XIRR**: **7.59%** (Simulated Benchmark Value: ₹675,507)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹18,795         | 34.68%  | Full                 |
| FEDBAN     |         48 |           48 | ₹17,376         | 33.23%  | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,911          | 28.25%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,694          | 23.32%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,525          | 18.00%  | Full                 |
| GAIL       |         61 |           61 | ₹11,407         | 17.59%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,364          | 15.90%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.68%  | Full                 |
| BHAELE     |         80 |           48 | ₹19,267         | 14.68%  | Partial (48/80 sh)   |
| ICINIF     |         86 |           86 | ₹24,518         | 12.90%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,267          | 9.36%   | Full                 |
| NHPC       |         55 |           55 | ₹4,128          | 9.18%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,764          | 7.25%   | Full                 |
| TATGLO     |         30 |           30 | ₹33,525         | 7.15%   | Full                 |
| NTPC       |         12 |           12 | ₹3,855          | 5.44%   | Full                 |
| HDF250     |         24 |           24 | ₹4,297          | 4.30%   | Full                 |
| HINPET     |         14 |           14 | ₹5,417          | 2.62%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,564          | 2.23%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,716         | 0.63%   | Full                 |
| MIR150     |        194 |          194 | ₹4,470          | -1.67%  | Full                 |
| ONGC       |         39 |           39 | ₹8,853          | -5.03%  | Full                 |
| ASHLEY     |        106 |           53 | ₹8,877          | -5.37%  | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹99,515         | -6.87%  | Partial (74/76 sh)   |
| GUJGA      |          7 |            7 | ₹2,808          | -7.60%  | Full                 |
| HDFBAN     |        130 |           75 | ₹61,238         | -10.51% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,791          | -13.54% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,328          | -16.20% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹32,902         | -18.22% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹28,507         | -24.08% | Full                 |
| ICIPSE     |        193 |          193 | ₹32,385         | -43.38% | Full                 |
| LIC        |         80 |           45 | ₹18,000         | -51.76% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 16.1%    | +10.94%        | N/A             | SELL        | Exit all 130 sh (~₹106,145)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 15.5%    | +16.06%        | N/A             | SELL        | Exit all 76 sh (~₹102,205)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.5%     | -18.13%        | N/A             | SELL        | Exit all 220 sh (~₹42,579)       | Thesis invalidated: Price ₹193.54 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.1%     | +39.58%        | N/A             | SELL        | Exit all 30 sh (~₹33,525)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| ICIPSE     | Commodities          | 4.9%     | -33.22%        | N/A             | SELL        | Exit all 193 sh (~₹32,385)       | Thesis invalidated: Price ₹167.80 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| BHAELE     | Defense              | 4.9%     | +154.32%       | ₹330.97         | SELL        | Exit all 80 sh (~₹32,112)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| LIC        | Insurance            | 4.9%     | -55.46%        | N/A             | SELL        | Exit all 80 sh (~₹32,000)        | Thesis invalidated: Price ₹400.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 4.3%     | -17.81%        | N/A             | SELL        | Exit all 250 sh (~₹28,507)       | Thesis invalidated: Price ₹114.03 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.2%     | +0.89%         | N/A             | SELL        | Exit all 54 sh (~₹27,716)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.7%     | +5.17%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹285.09 moving sideways between 50 DMA (₹264.32) and 200 DMA (₹270.55); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.4%     | +51.13%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +69.55%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹18,795)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| ASHLEY     | Auto                 | 2.7%     | +69.22%        | ₹148.26         | SELL        | Exit all 106 sh (~₹17,754)       | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| FEDBAN     | Banking              | 2.6%     | +141.51%       | ₹259.30         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +141.51%, position weight 2.6%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.5%     | +7.81%         | N/A             | SELL        | Exit all 46 sh (~₹16,167)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -2.66%         | N/A             | SELL        | Exit all 53 sh (~₹11,978)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +20.22%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +20.22%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| NTPGRE     | Power                | 1.7%     | -23.77%        | N/A             | SELL        | Exit all 138 sh (~₹11,362)       | Thesis invalidated: Price ₹82.33 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| ONGC       | Oil & Gas            | 1.3%     | -6.79%         | N/A             | SELL        | Exit all 39 sh (~₹8,853)         | Trend exit: month-end close ₹217.71 < 10-month average ₹245.69. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +16.02%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹1377.90 moving sideways between 50 DMA (₹1245.16) and 200 DMA (₹1250.13); conviction (5/5) thesis INTACT above invalidation (₹1009.47).                                                                                             | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +4.02%         | N/A             | SELL        | Exit all 14 sh (~₹5,417)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +3.30%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +3.30%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | -0.65%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹23.04 moving sideways between 50 DMA (₹22.59) and 200 DMA (₹22.64); conviction (4/5) thesis INTACT above invalidation (₹20.41).                                                                                                     | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +1.68%         | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +28.47%        | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹75.05 < 200 DMA (₹76.83) with return +28.47%; thesis remains INTACT above invalidation (₹53.75).                                                                                                                                         | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +15.88%        | N/A             | SELL        | Exit all 12 sh (~₹3,855)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -35.40%        | N/A             | SELL        | Exit all 67 sh (~₹3,791)         | Thesis invalidated: Price ₹56.58 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +106.42%       | ₹133.52         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +106.42%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                               | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.4%     | +21.85%        | N/A             | SELL        | Exit all 8 sh (~₹2,764)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +9.55%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹35.45 moving sideways between 50 DMA (₹33.62) and 200 DMA (₹33.64); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +91.48%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,364)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +6.95%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹63.71 moving sideways between 50 DMA (₹58.34) and 200 DMA (₹58.66); conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                     | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹287.61 vs 200-day average ₹272.58 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.6%
* **Banking**: 19.1%
* **Commodities**: 9.3%
* **Power**: 8.2%
* **IT**: 6.9%
* **Consumption**: 5.1%
* **Broad Market**: 5.1%
* **Defense**: 4.9%
* **Insurance**: 4.9%
* **Financial Services**: 4.3%
* **Consumer Electronics**: 3.4%
* **Telecom**: 2.9%
* **Auto**: 2.7%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 28.2%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.7%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| Financials        | 28.2%      | 25.0% | ⚠️ BREACH | FEDBAN (2.6%), HDFBAN (16.1%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.5%), +1 more |
| State-owned (PSU) | 19.0%      | 25.0% | OK        | ONGC (1.3%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 9.3%       | 25.0% | OK        | ICIGOL (4.3%), ICIPSE (4.9%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 16.1%           | 16.66%             | +0.43% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 15.5%           | 15.86%             | +0.32% via ICINIF                        |
| WIPRO    | 6.5%            | 6.48%              | Direct only                              |
| TATGLO   | 5.1%            | 5.10%              | Direct only                              |
| ICIPSE   | 4.9%            | 4.93%              | Direct only                              |
| BHAELE   | 4.9%            | 4.88%              | Direct only                              |
| LIC      | 4.9%            | 4.87%              | Direct only                              |
| ICIGOL   | 4.3%            | 4.34%              | Direct only                              |
| JSWENE   | 4.2%            | 4.22%              | Direct only                              |
| ICINIF   | 3.7%            | 3.73%              | Direct only                              |
| LGELEC   | 3.4%            | 3.41%              | Direct only                              |
| IDECEL   | 2.9%            | 2.86%              | Direct only                              |
| ASHLEY   | 2.7%            | 2.70%              | Direct only                              |
| FEDBAN   | 2.6%            | 2.65%              | +0.01% via KOTAKBKETF                    |
| TATCAP   | 2.5%            | 2.46%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.1%** (Target: 50.0%, Gap: +44.9%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **94.9%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.7%     | ₹24,518 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,470  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,297  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 16.1%    | ₹106,145 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.5%    | ₹102,205 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,267   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,855   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.5%     | ₹42,579  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 4.9%     | ₹32,000  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.4%     | ₹22,398  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.7%     | ₹17,754  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.6%     | ₹17,376  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.5%     | ₹16,167  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹11,407  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.3%     | ₹8,853   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,564   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,764   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,694   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,911   | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.1%     | ₹33,525  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 4.9%     | ₹32,385  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹32,112  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹27,716  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,978  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,362  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,417   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹4,128   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,791   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,525   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.3%     | ₹28,507  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹18,795  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,364   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,911)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,364)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,694)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,764)   |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,525)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,791)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹4,128)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,297)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,470) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,564)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,417)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹50,274.28  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹50,274.28  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹5,642.46   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹135,416**, Tax savings potential: **₹18,670**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹816.50  | ₹1455.47   | ₹35,144             | LTCG      | ₹4,393                |
| RELIND   |       27 | ₹1344.80 | ₹2228.99   | ₹23,873             | LTCG      | ₹2,984                |
| LIC      |       45 | ₹400.00  | ₹895.05    | ₹22,277             | LTCG      | ₹2,785                |
| WIPRO    |      170 | ₹193.54  | ₹304.31    | ₹18,831             | LTCG/STCG | ₹2,417                |
| ICIPSE   |      193 | ₹167.80  | ₹250.36    | ₹15,933             | STCG      | ₹3,187                |
| ICIGOL   |      250 | ₹114.03  | ₹138.24    | ₹6,053              | STCG      | ₹1,211                |
| JSWENE   |       28 | ₹513.25  | ₹668.00    | ₹4,333              | LTCG      | ₹542                  |
| JIOFIN   |       28 | ₹226.00  | ₹344.38    | ₹3,315              | LTCG      | ₹414                  |
| ASHLEY   |       33 | ₹167.49  | ₹230.20    | ₹2,069              | LTCG      | ₹259                  |
| SJVLIM   |       67 | ₹56.58   | ₹86.95     | ₹2,035              | LTCG      | ₹254                  |

*Showing top 10 of 17 loss-harvest candidates.*


