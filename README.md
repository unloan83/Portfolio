# Orchestrated Multi-Agent Portfolio Audit - 2026-11-10

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-10
* **Portfolio XIRR**: **-4.14%** (Current Traded Positions Value: ₹511,336)
* **Benchmark XIRR**: **7.23%** (Simulated Benchmark Value: ₹668,925)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹19,005         | 36.03%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,517         | 31.34%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,737          | 29.06%  | Full                 |
| GAIL       |         61 |           61 | ₹11,468         | 18.39%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,412          | 17.20%  | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,860          | 17.17%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,375          | 16.09%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.83%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,938         | 14.15%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,421          | 11.82%  | Full                 |
| ICINIF     |         86 |           86 | ₹24,361         | 11.66%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,310          | 9.78%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,880          | 8.80%   | Full                 |
| TATGLO     |         30 |           30 | ₹32,517         | 6.51%   | Full                 |
| NTPC       |         12 |           12 | ₹3,945          | 6.30%   | Full                 |
| HINPET     |         14 |           14 | ₹5,400          | 2.47%   | Full                 |
| JSWENE     |         54 |           54 | ₹28,250         | 1.30%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,486          | 1.29%   | Full                 |
| HDF250     |         24 |           24 | ₹4,240          | 0.88%   | Full                 |
| ONGC       |         39 |           39 | ₹9,106          | -2.91%  | Full                 |
| MIR150     |        194 |          194 | ₹4,433          | -3.86%  | Full                 |
| ASHLEY     |        106 |           53 | ₹9,268          | -3.95%  | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹98,006         | -7.48%  | Partial (74/76 sh)   |
| GUJGA      |          7 |            7 | ₹2,808          | -7.66%  | Full                 |
| HDFBAN     |        130 |           75 | ₹59,861         | -11.09% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,867          | -13.02% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,440          | -15.68% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹33,830         | -17.16% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹30,295         | -17.56% | Full                 |
| ICIPSE     |        193 |          193 | ₹35,477         | -36.20% | Full                 |
| LIC        |         80 |           45 | ₹17,955         | -52.39% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 15.7%    | +8.44%         | N/A             | SELL        | Exit all 130 sh (~₹103,760)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 15.2%    | +14.30%        | N/A             | SELL        | Exit all 76 sh (~₹100,654)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.6%     | -15.82%        | N/A             | SELL        | Exit all 220 sh (~₹43,780)       | Thesis invalidated: Price ₹199.00 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 5.4%     | -26.84%        | N/A             | SELL        | Exit all 193 sh (~₹35,477)       | Thesis invalidated: Price ₹183.82 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| TATGLO     | Consumption          | 4.9%     | +35.38%        | N/A             | SELL        | Exit all 30 sh (~₹32,517)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| LIC        | Insurance            | 4.8%     | -55.57%        | N/A             | SELL        | Exit all 80 sh (~₹31,920)        | Thesis invalidated: Price ₹399.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| BHAELE     | Defense              | 4.8%     | +149.98%       | ₹330.97         | SELL        | Exit all 80 sh (~₹31,564)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.6%     | -12.66%        | N/A             | SELL        | Exit all 250 sh (~₹30,295)       | Thesis invalidated: Price ₹121.18 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.3%     | +2.84%         | N/A             | SELL        | Exit all 54 sh (~₹28,250)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.7%     | +4.50%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹283.27 moving sideways between 50 DMA (₹263.28) and 200 DMA (₹270.51); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +57.35%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +71.45%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹19,005)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| ASHLEY     | Auto                 | 2.8%     | +76.66%        | ₹148.26         | SELL        | Exit all 106 sh (~₹18,535)       | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| FEDBAN     | Banking              | 2.5%     | +129.57%       | ₹259.30         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +129.57%, position weight 2.5%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.5%     | +8.30%         | N/A             | SELL        | Exit all 46 sh (~₹16,240)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -0.94%         | N/A             | SELL        | Exit all 53 sh (~₹12,190)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +20.86%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +20.86%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| NTPGRE     | Power                | 1.7%     | -23.62%        | N/A             | SELL        | Exit all 138 sh (~₹11,384)       | Thesis invalidated: Price ₹82.49 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| ONGC       | Oil & Gas            | 1.4%     | -4.12%         | N/A             | SELL        | Exit all 39 sh (~₹9,106)         | Trend exit: month-end close ₹225.39 < 10-month average ₹254.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +16.62%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹1385.00 moving sideways between 50 DMA (₹1228.33) and 200 DMA (₹1245.70); conviction (5/5) thesis INTACT above invalidation (₹1009.47).                                                                                             | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +3.69%         | N/A             | SELL        | Exit all 14 sh (~₹5,400)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +1.54%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +1.54%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | -1.47%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |
| NHPC       | Power                | 0.7%     | +37.61%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹80.39 moving sideways between 50 DMA (₹75.13) and 200 DMA (₹76.84); conviction (3/5) thesis INTACT above invalidation (₹53.75).                                                                                                     | INTACT          |            3 |
| HDF250     | Broad Market         | 0.6%     | +0.33%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹176.67 moving sideways between 50 DMA (₹179.28) and 200 DMA (₹171.23); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| NTPC       | Power                | 0.6%     | +18.58%        | N/A             | SELL        | Exit all 12 sh (~₹3,945)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -34.10%        | N/A             | SELL        | Exit all 67 sh (~₹3,867)         | Thesis invalidated: Price ₹57.72 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +99.79%        | ₹135.92         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +99.79%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                                | INTACT          |            3 |
| TATPOW     | Power                | 0.4%     | +26.97%        | N/A             | SELL        | Exit all 8 sh (~₹2,880)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +11.28%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹36.01 moving sideways between 50 DMA (₹33.52) and 200 DMA (₹33.77); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +92.39%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,375)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +4.10%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹62.01 moving sideways between 50 DMA (₹58.05) and 200 DMA (₹58.62); conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                     | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹285.01 vs 200-day average ₹272.60 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.3%
* **Banking**: 18.5%
* **Commodities**: 10.0%
* **Power**: 8.3%
* **IT**: 7.0%
* **Broad Market**: 5.0%
* **Consumption**: 4.9%
* **Insurance**: 4.8%
* **Defense**: 4.8%
* **Financial Services**: 4.3%
* **Consumer Electronics**: 3.5%
* **Telecom**: 2.9%
* **Auto**: 2.8%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 27.6%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.6%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| Financials        | 27.6%      | 25.0% | ⚠️ BREACH | FEDBAN (2.5%), HDFBAN (15.7%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.5%), +1 more |
| State-owned (PSU) | 19.0%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 10.0%      | 25.0% | OK        | ICIGOL (4.6%), ICIPSE (5.4%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 15.7%           | 16.22%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 15.2%           | 15.56%             | +0.31% via ICINIF                        |
| WIPRO    | 6.6%            | 6.63%              | Direct only                              |
| ICIPSE   | 5.4%            | 5.37%              | Direct only                              |
| TATGLO   | 4.9%            | 4.92%              | Direct only                              |
| LIC      | 4.8%            | 4.83%              | Direct only                              |
| BHAELE   | 4.8%            | 4.78%              | Direct only                              |
| ICIGOL   | 4.6%            | 4.59%              | Direct only                              |
| JSWENE   | 4.3%            | 4.28%              | Direct only                              |
| ICINIF   | 3.7%            | 3.69%              | Direct only                              |
| LGELEC   | 3.5%            | 3.53%              | Direct only                              |
| IDECEL   | 2.9%            | 2.88%              | Direct only                              |
| ASHLEY   | 2.8%            | 2.81%              | Direct only                              |
| FEDBAN   | 2.5%            | 2.51%              | +0.01% via KOTAKBKETF                    |
| TATCAP   | 2.5%            | 2.46%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.7%     | ₹24,361 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,433  |            4 |
| HDF250   | Index ETF (Core) | 0.6%     | ₹4,240  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 15.7%    | ₹103,760 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.2%    | ₹100,654 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,310   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,945   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.6%     | ₹43,780  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 4.8%     | ₹31,920  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹23,319  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.8%     | ₹18,535  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.5%     | ₹16,517  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.5%     | ₹16,240  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹11,468  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹9,106   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,486   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,880   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,737   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,860   | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 5.4%     | ₹35,477  | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.9%     | ₹32,517  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹31,564  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.3%     | ₹28,250  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹12,190  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,384  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,400   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,421   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,867   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,412   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.6%     | ₹30,295  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹19,005  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,375   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,860)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,375)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,737)  |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,880)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,412)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,867)  |
| HDF250     | Broad Market   | 0.6%     |            4 | Exit all 24 sh (~₹4,240)  |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,421)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,433) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,486)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,400)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹48,658.04  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹48,658.04  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹4,674.99   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹130,426**, Tax savings potential: **₹17,628**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹798.15  | ₹1455.47   | ₹36,153             | LTCG      | ₹4,519                |
| RELIND   |       32 | ₹1324.40 | ₹2089.85   | ₹24,494             | LTCG/STCG | ₹3,067                |
| LIC      |       45 | ₹399.00  | ₹895.05    | ₹22,322             | LTCG      | ₹2,790                |
| WIPRO    |      170 | ₹199.00  | ₹304.31    | ₹17,903             | LTCG/STCG | ₹2,252                |
| ICIPSE   |      193 | ₹183.82  | ₹250.36    | ₹12,841             | STCG      | ₹2,568                |
| ICIGOL   |      250 | ₹121.18  | ₹138.24    | ₹4,265              | STCG      | ₹853                  |
| JSWENE   |       28 | ₹523.15  | ₹668.00    | ₹4,056              | LTCG      | ₹507                  |
| JIOFIN   |       28 | ₹230.00  | ₹344.38    | ₹3,203              | LTCG      | ₹400                  |
| SJVLIM   |       67 | ₹57.72   | ₹86.95     | ₹1,958              | LTCG      | ₹245                  |
| ASHLEY   |       33 | ₹174.86  | ₹230.20    | ₹1,826              | LTCG      | ₹228                  |

*Showing top 10 of 17 loss-harvest candidates.*


