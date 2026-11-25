# Orchestrated Multi-Agent Portfolio Audit - 2026-11-25

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-25
* **Portfolio XIRR**: **-4.67%** (Current Traded Positions Value: ₹504,086)
* **Benchmark XIRR**: **8.36%** (Simulated Benchmark Value: ₹689,614)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| KOTAKBKETF |         30 |           30 | ₹1,982          | 41.93%  | Full                 |
| FEDBAN     |         48 |           48 | ₹17,098         | 32.28%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹17,535         | 28.52%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,717          | 24.20%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,485          | 17.59%  | Full                 |
| GAIL       |         61 |           61 | ₹11,438         | 17.47%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.45%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,289          | 14.98%  | Full                 |
| BHAELE     |         80 |           48 | ₹19,406         | 14.82%  | Partial (48/80 sh)   |
| ICINIF     |         86 |           86 | ₹24,764         | 14.70%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,388          | 10.12%  | Full                 |
| NHPC       |         55 |           55 | ₹4,161          | 9.39%   | Full                 |
| TATGLO     |         30 |           30 | ₹35,574         | 8.40%   | Full                 |
| NTPC       |         12 |           12 | ₹3,816          | 5.03%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,584          | 4.79%   | Full                 |
| HINPET     |         14 |           14 | ₹5,474          | 3.16%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,578          | 2.36%   | Full                 |
| HDF250     |         24 |           24 | ₹4,254          | 1.57%   | Full                 |
| MIR150     |        194 |          194 | ₹4,487          | -0.65%  | Full                 |
| JSWENE     |         54 |           54 | ₹26,233         | -1.27%  | Full                 |
| RELIND     |         76 |           74 | ₹101,669        | -6.03%  | Partial (74/76 sh)   |
| ONGC       |         39 |           39 | ₹8,658          | -6.57%  | Full                 |
| ASHLEY     |        106 |           53 | ₹8,374          | -7.23%  | Partial (53/106 sh)  |
| GUJGA      |          7 |            7 | ₹2,808          | -7.50%  | Full                 |
| HDFBAN     |        130 |           75 | ₹63,465         | -9.61%  | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,715          | -14.02% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,240          | -16.53% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹32,139         | -19.00% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹25,882         | -32.95% | Full                 |
| LIC        |         80 |           45 | ₹18,376         | -50.08% | Partial (45/80 sh)   |
| ICIPSE     |        193 |          193 | ₹27,634         | -53.60% | Full                 |

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
| HDFBAN     | Banking              | 16.8%    | +14.97%        | N/A             | SELL        | Exit all 130 sh (~₹110,006)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 15.9%    | +18.57%        | N/A             | SELL        | Exit all 76 sh (~₹104,416)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.3%     | -20.03%        | N/A             | SELL        | Exit all 220 sh (~₹41,591)       | Thesis invalidated: Price ₹189.05 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.4%     | +48.11%        | N/A             | SELL        | Exit all 30 sh (~₹35,574)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| LIC        | Insurance            | 5.0%     | -54.53%        | N/A             | SELL        | Exit all 80 sh (~₹32,668)        | Thesis invalidated: Price ₹408.35 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| BHAELE     | Defense              | 4.9%     | +156.16%       | ₹330.97         | SELL        | Exit all 80 sh (~₹32,344)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIPSE     | Commodities          | 4.2%     | -43.02%        | N/A             | SELL        | Exit all 193 sh (~₹27,634)       | Thesis invalidated: Price ₹143.18 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| JSWENE     | Power                | 4.0%     | -4.50%         | N/A             | SELL        | Exit all 54 sh (~₹26,233)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.0%     | -25.38%        | N/A             | SELL        | Exit all 250 sh (~₹25,882)       | Thesis invalidated: Price ₹103.53 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| ICINIF     | Broad Market         | 3.8%     | +6.22%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹287.95 moving sideways between 50 DMA (₹267.31) and 200 DMA (₹270.58); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.6%     | +59.51%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.7%     | +58.19%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹17,535)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| FEDBAN     | Banking              | 2.6%     | +137.64%       | ₹263.34         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +137.64%, position weight 2.6%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.6%     | +59.63%        | ₹147.37         | SELL        | Exit all 106 sh (~₹16,748)       | Trend exit: month-end close ₹143.95 < 10-month average ₹165.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.5%     | +7.85%         | N/A             | SELL        | Exit all 46 sh (~₹16,174)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -4.02%         | N/A             | SELL        | Exit all 53 sh (~₹11,811)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +20.54%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +20.54%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| NTPGRE     | Power                | 1.7%     | -24.35%        | N/A             | SELL        | Exit all 138 sh (~₹11,275)       | Thesis invalidated: Price ₹81.70 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| ONGC       | Oil & Gas            | 1.3%     | -8.84%         | N/A             | SELL        | Exit all 39 sh (~₹8,658)         | Trend exit: month-end close ₹217.71 < 10-month average ₹245.69. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +17.72%        | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +5.10%         | N/A             | SELL        | Exit all 14 sh (~₹5,474)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +3.61%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +3.61%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | -0.26%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹23.13 moving sideways between 50 DMA (₹22.53) and 200 DMA (₹22.68); conviction (4/5) thesis INTACT above invalidation (₹20.41).                                                                                                     | INTACT          |            4 |
| HDF250     | Broad Market         | 0.6%     | +0.65%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹177.24 moving sideways between 50 DMA (₹177.90) and 200 DMA (₹172.26); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +29.49%        | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹75.65 < 200 DMA (₹76.83) with return +29.49%; thesis remains INTACT above invalidation (₹53.75).                                                                                                                                         | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +14.71%        | N/A             | SELL        | Exit all 12 sh (~₹3,816)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -36.69%        | N/A             | SELL        | Exit all 67 sh (~₹3,715)         | Thesis invalidated: Price ₹55.45 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +104.08%       | ₹133.52         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +104.08%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                               | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +10.48%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +10.48%, position weight 0.4%; conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                                | INTACT          |            4 |
| TATPOW     | Power                | 0.4%     | +13.92%        | N/A             | SELL        | Exit all 8 sh (~₹2,584)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.3%     | +85.40%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,289)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +10.88%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +10.88%, position weight 0.3%; conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                                | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹294.07 vs 200-day average ₹272.73 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 21.0%
* **Banking**: 19.7%
* **Commodities**: 8.2%
* **Power**: 7.9%
* **IT**: 6.8%
* **Consumption**: 5.4%
* **Broad Market**: 5.1%
* **Insurance**: 5.0%
* **Defense**: 4.9%
* **Financial Services**: 4.3%
* **Consumer Electronics**: 3.6%
* **Telecom**: 2.7%
* **Auto**: 2.6%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 29.0%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Financials        | 29.0%      | 25.0% | ⚠️ BREACH | FEDBAN (2.6%), HDFBAN (16.8%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.5%), +1 more |
| Energy & Power    | 28.9%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| State-owned (PSU) | 19.2%      | 25.0% | OK        | ONGC (1.3%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 8.2%       | 25.0% | OK        | ICIGOL (4.0%), ICIPSE (4.2%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 16.8%           | 17.31%             | +0.43% via ICINIF, +0.09% via KOTAKBKETF |
| RELIND   | 15.9%           | 16.26%             | +0.32% via ICINIF                        |
| WIPRO    | 6.3%            | 6.35%              | Direct only                              |
| TATGLO   | 5.4%            | 5.43%              | Direct only                              |
| LIC      | 5.0%            | 4.99%              | Direct only                              |
| BHAELE   | 4.9%            | 4.94%              | Direct only                              |
| ICIPSE   | 4.2%            | 4.22%              | Direct only                              |
| JSWENE   | 4.0%            | 4.00%              | Direct only                              |
| ICIGOL   | 4.0%            | 3.95%              | Direct only                              |
| ICINIF   | 3.8%            | 3.78%              | Direct only                              |
| LGELEC   | 3.6%            | 3.61%              | Direct only                              |
| IDECEL   | 2.7%            | 2.68%              | Direct only                              |
| FEDBAN   | 2.6%            | 2.62%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.6%            | 2.56%              | Direct only                              |
| TATCAP   | 2.5%            | 2.47%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.1%** (Target: 50.0%, Gap: +44.9%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **94.9%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.8%     | ₹24,764 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,487  |            4 |
| HDF250   | Index ETF (Core) | 0.6%     | ₹4,254  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 16.8%    | ₹110,006 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.9%    | ₹104,416 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,388   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,816   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.3%     | ₹41,591  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.0%     | ₹32,668  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.6%     | ₹23,639  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.6%     | ₹17,098  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.6%     | ₹16,748  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.5%     | ₹16,174  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹11,438  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.3%     | ₹8,658   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,578   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,717   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,584   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,982   | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.4%     | ₹35,574  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹32,344  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 4.2%     | ₹27,634  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.0%     | ₹26,233  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,811  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,275  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,474   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹4,161   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,715   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,485   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.0%     | ₹25,882  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.7%     | ₹17,535  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.3%     | ₹2,289   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,982)  |
| SEQSCI     | Pharma         | 0.3%     |            2 | Exit all 10 sh (~₹2,289)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,584)   |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,717)  |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,485)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,715)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹4,161)  |
| HDF250     | Broad Market   | 0.6%     |            4 | Exit all 24 sh (~₹4,254)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,487) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,578)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,474)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹50,544.78  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹50,544.78  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹7,306.90   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹142,194**, Tax savings potential: **₹20,121**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹846.20  | ₹1455.47   | ₹33,510             | LTCG      | ₹4,189                |
| RELIND   |       27 | ₹1373.90 | ₹2228.99   | ₹23,087             | LTCG      | ₹2,886                |
| LIC      |       45 | ₹408.35  | ₹895.05    | ₹21,901             | LTCG      | ₹2,738                |
| ICIPSE   |      193 | ₹143.18  | ₹250.36    | ₹20,685             | STCG      | ₹4,137                |
| WIPRO    |      170 | ₹189.05  | ₹304.31    | ₹19,594             | LTCG/STCG | ₹2,553                |
| ICIGOL   |      250 | ₹103.53  | ₹138.24    | ₹8,678              | STCG      | ₹1,736                |
| JSWENE   |       28 | ₹485.80  | ₹668.00    | ₹5,102              | LTCG      | ₹638                  |
| JIOFIN   |       28 | ₹222.85  | ₹344.38    | ₹3,403              | LTCG      | ₹425                  |
| ASHLEY   |       35 | ₹158.00  | ₹226.29    | ₹2,390              | LTCG      | ₹299                  |
| SJVLIM   |       67 | ₹55.45   | ₹86.95     | ₹2,110              | LTCG      | ₹264                  |

*Showing top 10 of 17 loss-harvest candidates.*


