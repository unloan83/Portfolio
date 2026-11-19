# Orchestrated Multi-Agent Portfolio Audit - 2026-11-20

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-19
* **Portfolio XIRR**: **-4.60%** (Current Traded Positions Value: ₹505,344)
* **Benchmark XIRR**: **7.46%** (Simulated Benchmark Value: ₹673,820)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| FEDBAN     |         48 |           48 | ₹17,297         | 32.94%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹18,150         | 31.62%  | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,929          | 31.52%  | Full                 |
| GAIL       |         61 |           61 | ₹11,590         | 19.02%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,646          | 17.99%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,494          | 17.73%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,356          | 15.78%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.60%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,998         | 14.14%  | Partial (48/80 sh)   |
| ICINIF     |         86 |           86 | ₹24,619         | 13.74%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,389          | 10.23%  | Full                 |
| NHPC       |         55 |           55 | ₹4,095          | 8.86%   | Full                 |
| TATGLO     |         30 |           30 | ₹33,927         | 7.39%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,704          | 6.43%   | Full                 |
| NTPC       |         12 |           12 | ₹3,845          | 5.33%   | Full                 |
| HINPET     |         14 |           14 | ₹5,410          | 2.54%   | Full                 |
| HDF250     |         24 |           24 | ₹4,265          | 2.29%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,557          | 2.13%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,640         | 0.53%   | Full                 |
| MIR150     |        194 |          194 | ₹4,491          | -0.47%  | Full                 |
| ONGC       |         39 |           39 | ₹8,775          | -5.66%  | Full                 |
| RELIND     |         76 |           74 | ₹100,862        | -6.36%  | Partial (74/76 sh)   |
| ASHLEY     |        106 |           53 | ₹8,610          | -6.36%  | Partial (53/106 sh)  |
| GUJGA      |          7 |            7 | ₹2,808          | -7.57%  | Full                 |
| HDFBAN     |        130 |           75 | ₹60,611         | -10.73% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,661          | -14.52% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,286          | -16.38% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹31,474         | -20.04% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹27,532         | -27.50% | Full                 |
| ICIPSE     |        193 |          193 | ₹31,455         | -45.29% | Full                 |
| LIC        |         80 |           45 | ₹18,000         | -51.50% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 16.1%    | +9.80%         | N/A             | SELL        | Exit all 130 sh (~₹105,060)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 15.9%    | +17.63%        | N/A             | SELL        | Exit all 76 sh (~₹103,588)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.3%     | -21.69%        | N/A             | SELL        | Exit all 220 sh (~₹40,731)       | Thesis invalidated: Price ₹185.14 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.2%     | +41.25%        | N/A             | SELL        | Exit all 30 sh (~₹33,927)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| LIC        | Insurance            | 4.9%     | -55.46%        | N/A             | SELL        | Exit all 80 sh (~₹32,000)        | Thesis invalidated: Price ₹400.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| BHAELE     | Defense              | 4.9%     | +150.78%       | ₹330.97         | SELL        | Exit all 80 sh (~₹31,664)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIPSE     | Commodities          | 4.8%     | -35.13%        | N/A             | SELL        | Exit all 193 sh (~₹31,455)       | Thesis invalidated: Price ₹162.98 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| JSWENE     | Power                | 4.2%     | +0.62%         | N/A             | SELL        | Exit all 54 sh (~₹27,640)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.2%     | -20.62%        | N/A             | SELL        | Exit all 250 sh (~₹27,532)       | Thesis invalidated: Price ₹110.13 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| ICINIF     | Broad Market         | 3.8%     | +5.60%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹286.27 moving sideways between 50 DMA (₹265.38) and 200 DMA (₹270.58); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.4%     | +47.34%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹1679.70 moving sideways between 50 DMA (₹1700.42) and 200 DMA (₹1587.39); conviction (4/5) thesis INTACT above invalidation (₹1003.20).                                                                                             | INTACT          |            4 |
| IDECEL     | Telecom              | 2.8%     | +63.73%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹18,150)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +140.41%       | ₹259.30         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +140.41%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.6%     | +64.12%        | ₹148.26         | SELL        | Exit all 106 sh (~₹17,220)       | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | +4.36%         | N/A             | SELL        | Exit all 46 sh (~₹15,649)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -3.31%         | N/A             | SELL        | Exit all 53 sh (~₹11,898)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.8%     | +22.15%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +22.15%, position weight 1.8%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| NTPGRE     | Power                | 1.7%     | -23.72%        | N/A             | SELL        | Exit all 138 sh (~₹11,368)       | Thesis invalidated: Price ₹82.38 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| ONGC       | Oil & Gas            | 1.3%     | -7.61%         | N/A             | SELL        | Exit all 39 sh (~₹8,775)         | Trend exit: month-end close ₹217.71 < 10-month average ₹245.69. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +17.73%        | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +3.88%         | N/A             | SELL        | Exit all 14 sh (~₹5,410)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +3.14%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +3.14%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | -0.17%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹23.15 moving sideways between 50 DMA (₹22.55) and 200 DMA (₹22.66); conviction (4/5) thesis INTACT above invalidation (₹20.41).                                                                                                     | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +0.91%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹177.70 moving sideways between 50 DMA (₹178.55) and 200 DMA (₹171.81); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +27.46%        | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹74.46 < 200 DMA (₹76.83) with return +27.46%; thesis remains INTACT above invalidation (₹53.75).                                                                                                                                         | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +15.57%        | N/A             | SELL        | Exit all 12 sh (~₹3,845)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -37.62%        | N/A             | SELL        | Exit all 67 sh (~₹3,661)         | Thesis invalidated: Price ₹54.64 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +104.64%       | ₹133.52         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +104.64%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                               | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.4%     | +19.21%        | N/A             | SELL        | Exit all 8 sh (~₹2,704)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +7.60%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +7.60%, position weight 0.4%; conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                                 | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +90.85%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,356)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +7.92%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹64.29 moving sideways between 50 DMA (₹58.54) and 200 DMA (₹58.71); conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                     | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹287.89 vs 200-day average ₹272.62 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 21.0%
* **Banking**: 19.1%
* **Commodities**: 9.1%
* **Power**: 8.2%
* **IT**: 6.7%
* **Consumption**: 5.2%
* **Broad Market**: 5.1%
* **Insurance**: 4.9%
* **Defense**: 4.9%
* **Financial Services**: 4.2%
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
| Energy & Power    | 29.2%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| Financials        | 28.2%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (16.1%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.1%      | 25.0% | OK        | ONGC (1.3%), GAIL (1.8%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 9.1%       | 25.0% | OK        | ICIGOL (4.2%), ICIPSE (4.8%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 16.1%           | 16.65%             | +0.43% via ICINIF, +0.09% via KOTAKBKETF |
| RELIND   | 15.9%           | 16.22%             | +0.32% via ICINIF                        |
| WIPRO    | 6.3%            | 6.25%              | Direct only                              |
| TATGLO   | 5.2%            | 5.21%              | Direct only                              |
| LIC      | 4.9%            | 4.91%              | Direct only                              |
| BHAELE   | 4.9%            | 4.86%              | Direct only                              |
| ICIPSE   | 4.8%            | 4.83%              | Direct only                              |
| JSWENE   | 4.2%            | 4.24%              | Direct only                              |
| ICIGOL   | 4.2%            | 4.23%              | Direct only                              |
| ICINIF   | 3.8%            | 3.78%              | Direct only                              |
| LGELEC   | 3.4%            | 3.35%              | Direct only                              |
| IDECEL   | 2.8%            | 2.79%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.66%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.6%            | 2.64%              | Direct only                              |
| TATCAP   | 2.4%            | 2.40%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.1%** (Target: 50.0%, Gap: +44.9%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **94.9%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.8%     | ₹24,619 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,491  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,265  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 16.1%    | ₹105,060 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.9%    | ₹103,588 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,389   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,845   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.3%     | ₹40,731  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 4.9%     | ₹32,000  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.4%     | ₹21,836  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹17,297  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.6%     | ₹17,220  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹15,649  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.8%     | ₹11,590  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.3%     | ₹8,775   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,557   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,704   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,646   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,929   | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.2%     | ₹33,927  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹31,664  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 4.8%     | ₹31,455  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹27,640  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,898  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,368  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,410   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹4,095   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,661   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,494   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.2%     | ₹27,532  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.8%     | ₹18,150  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,356   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,929)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,356)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,646)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,704)   |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,494)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,661)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹4,095)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,265)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,491) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,557)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,410)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹49,963.53  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹49,963.53  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹6,113.17   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹139,161**, Tax savings potential: **₹19,360**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹808.15  | ₹1455.47   | ₹35,603             | LTCG      | ₹4,450                |
| RELIND   |       27 | ₹1363.00 | ₹2228.99   | ₹23,382             | LTCG      | ₹2,923                |
| LIC      |       45 | ₹400.00  | ₹895.05    | ₹22,277             | LTCG      | ₹2,785                |
| WIPRO    |      170 | ₹185.14  | ₹304.31    | ₹20,259             | LTCG/STCG | ₹2,671                |
| ICIPSE   |      193 | ₹162.98  | ₹250.36    | ₹16,863             | STCG      | ₹3,373                |
| ICIGOL   |      250 | ₹110.13  | ₹138.24    | ₹7,028              | STCG      | ₹1,406                |
| JSWENE   |       28 | ₹511.85  | ₹668.00    | ₹4,372              | LTCG      | ₹547                  |
| JIOFIN   |       28 | ₹224.50  | ₹344.38    | ₹3,357              | LTCG      | ₹420                  |
| ASHLEY   |       33 | ₹162.45  | ₹230.20    | ₹2,236              | LTCG      | ₹279                  |
| SJVLIM   |       67 | ₹54.64   | ₹86.95     | ₹2,165              | LTCG      | ₹271                  |

*Showing top 10 of 18 loss-harvest candidates.*


