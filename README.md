# Orchestrated Multi-Agent Portfolio Audit - 2026-11-17

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-17
* **Portfolio XIRR**: **-4.29%** (Current Traded Positions Value: ₹509,076)
* **Benchmark XIRR**: **7.74%** (Simulated Benchmark Value: ₹678,079)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| KOTAKBKETF |         30 |           30 | ₹1,943          | 35.89%  | Full                 |
| FEDBAN     |         48 |           48 | ₹17,558         | 33.62%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹18,450         | 33.08%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,676          | 21.27%  | Full                 |
| GAIL       |         61 |           61 | ₹11,407         | 17.55%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,462          | 17.51%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,374          | 16.00%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.65%  | Full                 |
| BHAELE     |         80 |           48 | ₹19,178         | 14.51%  | Partial (48/80 sh)   |
| ICINIF     |         86 |           86 | ₹24,636         | 14.11%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,328          | 9.80%   | Full                 |
| NHPC       |         55 |           55 | ₹4,114          | 9.05%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,756          | 7.14%   | Full                 |
| TATGLO     |         30 |           30 | ₹33,372         | 7.04%   | Full                 |
| NTPC       |         12 |           12 | ₹3,862          | 5.49%   | Full                 |
| HDF250     |         24 |           24 | ₹4,291          | 3.93%   | Full                 |
| HINPET     |         14 |           14 | ₹5,454          | 2.99%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,593          | 2.58%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,805         | 0.74%   | Full                 |
| MIR150     |        194 |          194 | ₹4,499          | -0.04%  | Full                 |
| ONGC       |         39 |           39 | ₹8,717          | -6.17%  | Full                 |
| RELIND     |         76 |           74 | ₹101,158        | -6.27%  | Partial (74/76 sh)   |
| ASHLEY     |        106 |           53 | ₹8,506          | -6.77%  | Partial (53/106 sh)  |
| GUJGA      |          7 |            7 | ₹2,808          | -7.59%  | Full                 |
| HDFBAN     |        130 |           75 | ₹61,121         | -10.55% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,744          | -13.89% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,411          | -15.72% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹32,281         | -19.01% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹28,485         | -24.09% | Full                 |
| ICIPSE     |        193 |          193 | ₹32,324         | -43.40% | Full                 |
| LIC        |         80 |           45 | ₹17,897         | -51.92% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 16.1%    | +10.73%        | N/A             | SELL        | Exit all 130 sh (~₹105,944)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 15.8%    | +17.98%        | N/A             | SELL        | Exit all 76 sh (~₹103,892)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.4%     | -19.68%        | N/A             | SELL        | Exit all 220 sh (~₹41,776)       | Thesis invalidated: Price ₹189.89 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.1%     | +38.94%        | N/A             | SELL        | Exit all 30 sh (~₹33,372)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| ICIPSE     | Commodities          | 4.9%     | -33.34%        | N/A             | SELL        | Exit all 193 sh (~₹32,324)       | Thesis invalidated: Price ₹167.48 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| BHAELE     | Defense              | 4.9%     | +153.15%       | ₹330.97         | SELL        | Exit all 80 sh (~₹31,964)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| LIC        | Insurance            | 4.8%     | -55.71%        | N/A             | SELL        | Exit all 80 sh (~₹31,816)        | Thesis invalidated: Price ₹397.70 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 4.3%     | -17.88%        | N/A             | SELL        | Exit all 250 sh (~₹28,485)       | Thesis invalidated: Price ₹113.94 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.2%     | +1.22%         | N/A             | SELL        | Exit all 54 sh (~₹27,805)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.8%     | +5.67%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹286.46 moving sideways between 50 DMA (₹264.61) and 200 DMA (₹270.55); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.4%     | +50.99%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.8%     | +66.44%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹18,450)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +144.05%       | ₹259.30         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +144.05%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.6%     | +62.15%        | ₹148.26         | SELL        | Exit all 106 sh (~₹17,013)       | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | +5.64%         | N/A             | SELL        | Exit all 46 sh (~₹15,842)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -1.39%         | N/A             | SELL        | Exit all 53 sh (~₹12,135)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| NTPGRE     | Power                | 1.7%     | -23.16%        | N/A             | SELL        | Exit all 138 sh (~₹11,453)       | Thesis invalidated: Price ₹82.99 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +20.22%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +20.22%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.3%     | -8.22%         | N/A             | SELL        | Exit all 39 sh (~₹8,717)         | Trend exit: month-end close ₹217.71 < 10-month average ₹245.69. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +16.87%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹1388.00 moving sideways between 50 DMA (₹1249.79) and 200 DMA (₹1251.02); conviction (5/5) thesis INTACT above invalidation (₹1009.47).                                                                                             | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +4.71%         | N/A             | SELL        | Exit all 14 sh (~₹5,454)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +3.96%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +3.96%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | +0.00%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹23.19 moving sideways between 50 DMA (₹22.58) and 200 DMA (₹22.64); conviction (4/5) thesis INTACT above invalidation (₹20.41).                                                                                                     | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +1.54%         | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +28.04%        | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹74.80 < 200 DMA (₹76.83) with return +28.04%; thesis remains INTACT above invalidation (₹53.75).                                                                                                                                         | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +16.08%        | N/A             | SELL        | Exit all 12 sh (~₹3,862)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -36.20%        | N/A             | SELL        | Exit all 67 sh (~₹3,744)         | Thesis invalidated: Price ₹55.88 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +102.75%       | ₹133.52         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +102.75%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                               | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.4%     | +21.50%        | N/A             | SELL        | Exit all 8 sh (~₹2,756)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +8.81%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +8.81%, position weight 0.4%; conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                                 | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +92.30%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,374)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +8.73%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹64.77 moving sideways between 50 DMA (₹58.45) and 200 DMA (₹58.68); conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                     | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹289.60 vs 200-day average ₹272.60 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.8%
* **Banking**: 19.1%
* **Commodities**: 9.3%
* **Power**: 8.2%
* **IT**: 6.8%
* **Broad Market**: 5.1%
* **Consumption**: 5.1%
* **Defense**: 4.9%
* **Insurance**: 4.8%
* **Financial Services**: 4.3%
* **Consumer Electronics**: 3.4%
* **Telecom**: 2.8%
* **Auto**: 2.6%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 28.2%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 29.0%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| Financials        | 28.2%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (16.1%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.0%      | 25.0% | OK        | ONGC (1.3%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 9.3%       | 25.0% | OK        | ICIGOL (4.3%), ICIPSE (4.9%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 16.1%           | 16.65%             | +0.43% via ICINIF, +0.09% via KOTAKBKETF |
| RELIND   | 15.8%           | 16.14%             | +0.32% via ICINIF                        |
| WIPRO    | 6.4%            | 6.36%              | Direct only                              |
| TATGLO   | 5.1%            | 5.08%              | Direct only                              |
| ICIPSE   | 4.9%            | 4.92%              | Direct only                              |
| BHAELE   | 4.9%            | 4.87%              | Direct only                              |
| LIC      | 4.8%            | 4.84%              | Direct only                              |
| ICIGOL   | 4.3%            | 4.34%              | Direct only                              |
| JSWENE   | 4.2%            | 4.23%              | Direct only                              |
| ICINIF   | 3.8%            | 3.75%              | Direct only                              |
| LGELEC   | 3.4%            | 3.41%              | Direct only                              |
| IDECEL   | 2.8%            | 2.81%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.68%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.6%            | 2.59%              | Direct only                              |
| TATCAP   | 2.4%            | 2.41%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.1%** (Target: 50.0%, Gap: +44.9%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **94.9%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.8%     | ₹24,636 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,499  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,291  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 16.1%    | ₹105,944 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.8%    | ₹103,892 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,328   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,862   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.4%     | ₹41,776  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 4.8%     | ₹31,816  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.4%     | ₹22,377  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹17,558  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.6%     | ₹17,013  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹15,842  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹11,407  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.3%     | ₹8,717   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,593   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,756   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,676   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,943   | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.1%     | ₹33,372  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 4.9%     | ₹32,324  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹31,964  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹27,805  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹12,135  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,453  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,454   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹4,114   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,744   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,462   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.3%     | ₹28,485  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.8%     | ₹18,450  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,374   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,943)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,374)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,676)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,756)   |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,462)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,744)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹4,114)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,291)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,499) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,593)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,454)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹50,302.83  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹50,302.83  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹6,305.42   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹135,960**, Tax savings potential: **₹18,782**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹814.95  | ₹1455.47   | ₹35,229             | LTCG      | ₹4,404                |
| RELIND   |       27 | ₹1367.00 | ₹2228.99   | ₹23,274             | LTCG      | ₹2,909                |
| LIC      |       45 | ₹397.70  | ₹895.05    | ₹22,381             | LTCG      | ₹2,798                |
| WIPRO    |      170 | ₹189.89  | ₹304.31    | ₹19,452             | LTCG/STCG | ₹2,527                |
| ICIPSE   |      193 | ₹167.48  | ₹250.36    | ₹15,995             | STCG      | ₹3,199                |
| ICIGOL   |      250 | ₹113.94  | ₹138.24    | ₹6,075              | STCG      | ₹1,215                |
| JSWENE   |       28 | ₹514.90  | ₹668.00    | ₹4,287              | LTCG      | ₹536                  |
| JIOFIN   |       28 | ₹228.96  | ₹344.38    | ₹3,232              | LTCG      | ₹404                  |
| ASHLEY   |       35 | ₹160.50  | ₹226.29    | ₹2,303              | LTCG      | ₹288                  |
| SJVLIM   |       67 | ₹55.88   | ₹86.95     | ₹2,082              | LTCG      | ₹260                  |

*Showing top 10 of 17 loss-harvest candidates.*


