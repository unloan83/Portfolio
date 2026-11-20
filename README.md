# Orchestrated Multi-Agent Portfolio Audit - 2026-11-20

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-20
* **Portfolio XIRR**: **-4.27%** (Current Traded Positions Value: ₹509,204)
* **Benchmark XIRR**: **8.37%** (Simulated Benchmark Value: ₹689,116)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| KOTAKBKETF |         30 |           30 | ₹2,019          | 54.28%  | Full                 |
| FEDBAN     |         48 |           48 | ₹17,928         | 34.38%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹18,225         | 31.89%  | Full                 |
| GAIL       |         61 |           61 | ₹11,678         | 19.71%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,648          | 18.02%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,511          | 17.84%  | Full                 |
| ICINIF     |         86 |           86 | ₹24,864         | 16.31%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.58%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,334          | 15.53%  | Full                 |
| BHAELE     |         80 |           48 | ₹19,296         | 14.68%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,214          | 9.91%   | Full                 |
| DRREDD     |          6 |            6 | ₹8,341          | 9.85%   | Full                 |
| TATGLO     |         30 |           30 | ₹34,677         | 7.87%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,718          | 6.61%   | Full                 |
| NTPC       |         12 |           12 | ₹3,858          | 5.44%   | Full                 |
| HDF250     |         24 |           24 | ₹4,299          | 4.28%   | Full                 |
| HINPET     |         14 |           14 | ₹5,549          | 3.94%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,608          | 2.74%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,724         | 0.64%   | Full                 |
| MIR150     |        194 |          194 | ₹4,507          | 0.39%   | Full                 |
| RELIND     |         76 |           74 | ₹101,935        | -5.97%  | Partial (74/76 sh)   |
| ONGC       |         39 |           39 | ₹8,715          | -6.15%  | Full                 |
| ASHLEY     |        106 |           53 | ₹8,658          | -6.17%  | Partial (53/106 sh)  |
| GUJGA      |          7 |            7 | ₹2,808          | -7.55%  | Full                 |
| HDFBAN     |        130 |           75 | ₹63,450         | -9.65%  | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,737          | -13.91% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,299          | -16.29% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹31,569         | -19.89% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹26,275         | -32.04% | Full                 |
| ICIPSE     |        193 |          193 | ₹29,415         | -50.09% | Full                 |
| LIC        |         80 |           45 | ₹18,482         | -50.25% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 16.7%    | +14.94%        | N/A             | SELL        | Exit all 130 sh (~₹109,980)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 15.9%    | +18.88%        | N/A             | SELL        | Exit all 76 sh (~₹104,690)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.2%     | -21.45%        | N/A             | SELL        | Exit all 220 sh (~₹40,854)       | Thesis invalidated: Price ₹185.70 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.3%     | +44.38%        | N/A             | SELL        | Exit all 30 sh (~₹34,677)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| LIC        | Insurance            | 5.0%     | -54.27%        | N/A             | SELL        | Exit all 80 sh (~₹32,856)        | Thesis invalidated: Price ₹410.70 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| BHAELE     | Defense              | 4.9%     | +154.70%       | ₹330.97         | SELL        | Exit all 80 sh (~₹32,160)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIPSE     | Commodities          | 4.5%     | -39.34%        | N/A             | SELL        | Exit all 193 sh (~₹29,415)       | Thesis invalidated: Price ₹152.41 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| JSWENE     | Power                | 4.2%     | +0.92%         | N/A             | SELL        | Exit all 54 sh (~₹27,724)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.0%     | -24.25%        | N/A             | SELL        | Exit all 250 sh (~₹26,275)       | Thesis invalidated: Price ₹105.10 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| ICINIF     | Broad Market         | 3.8%     | +6.65%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹289.12 moving sideways between 50 DMA (₹265.85) and 200 DMA (₹270.58); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.4%     | +52.69%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.8%     | +64.41%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹18,225)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +149.18%       | ₹262.01         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +149.18%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.6%     | +65.03%        | ₹147.37         | SELL        | Exit all 106 sh (~₹17,315)       | Trend exit: month-end close ₹143.95 < 10-month average ₹165.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | +5.90%         | N/A             | SELL        | Exit all 46 sh (~₹15,882)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -3.11%         | N/A             | SELL        | Exit all 53 sh (~₹11,923)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.8%     | +23.07%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +23.07%, position weight 1.8%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| NTPGRE     | Power                | 1.7%     | -22.90%        | N/A             | SELL        | Exit all 138 sh (~₹11,491)       | Thesis invalidated: Price ₹83.27 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| ONGC       | Oil & Gas            | 1.3%     | -8.24%         | N/A             | SELL        | Exit all 39 sh (~₹8,715)         | Trend exit: month-end close ₹217.71 < 10-month average ₹245.69. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +17.06%        | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +6.54%         | N/A             | SELL        | Exit all 14 sh (~₹5,549)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +4.29%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +4.29%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | +0.17%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹23.23 moving sideways between 50 DMA (₹22.55) and 200 DMA (₹22.67); conviction (4/5) thesis INTACT above invalidation (₹20.41).                                                                                                     | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +1.72%         | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +31.14%        | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹76.61 < 200 DMA (₹76.84) with return +31.14%; thesis remains INTACT above invalidation (₹53.75).                                                                                                                                         | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +15.97%        | N/A             | SELL        | Exit all 12 sh (~₹3,858)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -36.32%        | N/A             | SELL        | Exit all 67 sh (~₹3,737)         | Thesis invalidated: Price ₹55.78 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +105.59%       | ₹133.52         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +105.59%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                               | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.4%     | +19.81%        | N/A             | SELL        | Exit all 8 sh (~₹2,718)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +7.66%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +7.66%, position weight 0.4%; conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                                 | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +89.03%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,334)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +12.98%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +12.98%, position weight 0.3%; conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                                | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹294.22 vs 200-day average ₹272.68 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.9%
* **Banking**: 19.7%
* **Commodities**: 8.4%
* **Power**: 8.2%
* **IT**: 6.6%
* **Consumption**: 5.3%
* **Broad Market**: 5.1%
* **Insurance**: 5.0%
* **Defense**: 4.9%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.4%
* **Telecom**: 2.8%
* **Auto**: 2.6%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 28.9%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 29.1%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| Financials        | 28.9%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (16.7%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.2%      | 25.0% | OK        | ONGC (1.3%), GAIL (1.8%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 8.4%       | 25.0% | OK        | ICIGOL (4.0%), ICIPSE (4.5%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 16.7%           | 17.20%             | +0.43% via ICINIF, +0.09% via KOTAKBKETF |
| RELIND   | 15.9%           | 16.20%             | +0.32% via ICINIF                        |
| WIPRO    | 6.2%            | 6.20%              | Direct only                              |
| TATGLO   | 5.3%            | 5.26%              | Direct only                              |
| LIC      | 5.0%            | 4.98%              | Direct only                              |
| BHAELE   | 4.9%            | 4.88%              | Direct only                              |
| ICIPSE   | 4.5%            | 4.46%              | Direct only                              |
| JSWENE   | 4.2%            | 4.21%              | Direct only                              |
| ICIGOL   | 4.0%            | 3.99%              | Direct only                              |
| ICINIF   | 3.8%            | 3.77%              | Direct only                              |
| LGELEC   | 3.4%            | 3.43%              | Direct only                              |
| IDECEL   | 2.8%            | 2.76%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.73%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.6%            | 2.63%              | Direct only                              |
| TATCAP   | 2.4%            | 2.41%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.1%** (Target: 50.0%, Gap: +44.9%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **94.9%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.8%     | ₹24,864 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,507  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,299  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 16.7%    | ₹109,980 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.9%    | ₹104,690 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,341   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,858   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.2%     | ₹40,854  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.0%     | ₹32,856  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.4%     | ₹22,629  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹17,928  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.6%     | ₹17,315  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹15,882  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.8%     | ₹11,678  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.3%     | ₹8,715   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,608   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,718   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,648   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹2,019   | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.3%     | ₹34,677  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹32,160  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 4.5%     | ₹29,415  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹27,724  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,923  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,491  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,549   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹4,214   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,737   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,511   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.0%     | ₹26,275  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.8%     | ₹18,225  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,334   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹2,019)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,334)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,648)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,718)   |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,511)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,737)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹4,214)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,299)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,507) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,608)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,549)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹52,340.28  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹52,340.28  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹7,651.10   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹139,216**, Tax savings potential: **₹19,610**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹846.00  | ₹1455.47   | ₹33,521             | LTCG      | ₹4,190                |
| RELIND   |       27 | ₹1377.50 | ₹2228.99   | ₹22,990             | LTCG      | ₹2,874                |
| LIC      |       45 | ₹410.70  | ₹895.05    | ₹21,796             | LTCG      | ₹2,724                |
| WIPRO    |      170 | ₹185.70  | ₹304.31    | ₹20,164             | LTCG/STCG | ₹2,654                |
| ICIPSE   |      193 | ₹152.41  | ₹250.36    | ₹18,903             | STCG      | ₹3,781                |
| ICIGOL   |      250 | ₹105.10  | ₹138.24    | ₹8,285              | STCG      | ₹1,657                |
| JSWENE   |       28 | ₹513.40  | ₹668.00    | ₹4,329              | LTCG      | ₹541                  |
| JIOFIN   |       28 | ₹224.97  | ₹344.38    | ₹3,344              | LTCG      | ₹418                  |
| ASHLEY   |       33 | ₹163.35  | ₹230.20    | ₹2,206              | LTCG      | ₹276                  |
| SJVLIM   |       67 | ₹55.78   | ₹86.95     | ₹2,088              | LTCG      | ₹261                  |

*Showing top 10 of 18 loss-harvest candidates.*


