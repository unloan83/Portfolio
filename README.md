# Orchestrated Multi-Agent Portfolio Audit - 2026-11-14

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-13
* **Portfolio XIRR**: **-3.99%** (Current Traded Positions Value: ₹512,936)
* **Benchmark XIRR**: **7.63%** (Simulated Benchmark Value: ₹675,728)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹19,455         | 37.81%  | Full                 |
| FEDBAN     |         48 |           48 | ₹17,400         | 33.38%  | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,914          | 30.03%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,718          | 26.36%  | Full                 |
| GAIL       |         61 |           61 | ₹11,463         | 18.21%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,522          | 17.63%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,351          | 16.70%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.75%  | Full                 |
| BHAELE     |         80 |           48 | ₹19,430         | 15.02%  | Partial (48/80 sh)   |
| ICINIF     |         86 |           86 | ₹24,639         | 14.55%  | Full                 |
| NHPC       |         55 |           55 | ₹4,224          | 10.07%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,320          | 9.80%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,856          | 8.47%   | Full                 |
| HDF250     |         24 |           24 | ₹4,348          | 7.62%   | Full                 |
| TATGLO     |         30 |           30 | ₹32,559         | 6.52%   | Full                 |
| NTPC       |         12 |           12 | ₹3,876          | 5.65%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,690          | 3.76%   | Full                 |
| HINPET     |         14 |           14 | ₹5,468          | 3.16%   | Full                 |
| JSWENE     |         54 |           54 | ₹28,061         | 1.06%   | Full                 |
| MIR150     |        194 |          194 | ₹4,493          | -0.37%  | Full                 |
| ASHLEY     |        106 |           53 | ₹9,219          | -4.11%  | Partial (53/106 sh)  |
| ONGC       |         39 |           39 | ₹8,756          | -5.90%  | Full                 |
| RELIND     |         76 |           74 | ₹99,138         | -7.03%  | Partial (74/76 sh)   |
| GUJGA      |          7 |            7 | ₹2,808          | -7.63%  | Full                 |
| HDFBAN     |        130 |           75 | ₹60,922         | -10.65% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,922          | -12.57% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,474          | -15.44% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹33,354         | -17.70% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹29,003         | -22.42% | Full                 |
| ICIPSE     |        193 |          193 | ₹34,508         | -38.37% | Full                 |
| LIC        |         80 |           45 | ₹18,180         | -51.58% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 15.9%    | +10.37%        | N/A             | SELL        | Exit all 130 sh (~₹105,599)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 15.4%    | +15.62%        | N/A             | SELL        | Exit all 76 sh (~₹101,817)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.5%     | -17.01%        | N/A             | SELL        | Exit all 220 sh (~₹43,164)       | Thesis invalidated: Price ₹196.20 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 5.2%     | -28.84%        | N/A             | SELL        | Exit all 193 sh (~₹34,508)       | Thesis invalidated: Price ₹178.80 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| TATGLO     | Consumption          | 4.9%     | +35.56%        | N/A             | SELL        | Exit all 30 sh (~₹32,559)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| BHAELE     | Defense              | 4.9%     | +156.48%       | ₹330.97         | SELL        | Exit all 80 sh (~₹32,384)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| LIC        | Insurance            | 4.9%     | -55.01%        | N/A             | SELL        | Exit all 80 sh (~₹32,320)        | Thesis invalidated: Price ₹404.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 4.4%     | -16.38%        | N/A             | SELL        | Exit all 250 sh (~₹29,003)       | Thesis invalidated: Price ₹116.01 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.2%     | +2.15%         | N/A             | SELL        | Exit all 54 sh (~₹28,061)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.7%     | +5.69%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹286.50 moving sideways between 50 DMA (₹264.04) and 200 DMA (₹270.55); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.4%     | +51.65%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +75.51%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹19,455)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| ASHLEY     | Auto                 | 2.8%     | +75.74%        | ₹148.26         | SELL        | Exit all 106 sh (~₹18,439)       | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| FEDBAN     | Banking              | 2.6%     | +141.84%       | ₹259.30         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +141.84%, position weight 2.6%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.5%     | +9.40%         | N/A             | SELL        | Exit all 46 sh (~₹16,406)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.8%     | -0.42%         | N/A             | SELL        | Exit all 53 sh (~₹12,254)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| NTPGRE     | Power                | 1.7%     | -22.63%        | N/A             | SELL        | Exit all 138 sh (~₹11,531)       | Thesis invalidated: Price ₹83.56 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +20.80%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +20.80%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.3%     | -7.81%         | N/A             | SELL        | Exit all 39 sh (~₹8,756)         | Trend exit: month-end close ₹217.71 < 10-month average ₹245.69. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +16.76%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹1386.60 moving sideways between 50 DMA (₹1236.51) and 200 DMA (₹1247.88); conviction (5/5) thesis INTACT above invalidation (₹1009.47).                                                                                             | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +5.00%         | N/A             | SELL        | Exit all 14 sh (~₹5,468)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +6.15%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +6.15%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | -0.13%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹23.16 moving sideways between 50 DMA (₹22.60) and 200 DMA (₹22.63); conviction (4/5) thesis INTACT above invalidation (₹20.41).                                                                                                     | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +2.88%         | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +31.46%        | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹76.80 < 200 DMA (₹76.83) with return +31.46%; thesis remains INTACT above invalidation (₹53.75).                                                                                                                                         | INTACT          |            3 |
| SJVLIM     | Power                | 0.6%     | -33.18%        | N/A             | SELL        | Exit all 67 sh (~₹3,922)         | Thesis invalidated: Price ₹58.53 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| NTPC       | Power                | 0.6%     | +16.51%        | N/A             | SELL        | Exit all 12 sh (~₹3,876)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| GUJPPL     | Infrastructure       | 0.5%     | +96.25%        | ₹133.52         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +96.25%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                                | INTACT          |            3 |
| TATPOW     | Power                | 0.4%     | +25.91%        | N/A             | SELL        | Exit all 8 sh (~₹2,856)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +10.51%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹35.76 moving sideways between 50 DMA (₹33.59) and 200 DMA (₹33.70); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +104.32%       | ₹208.60         | SELL        | Exit all 10 sh (~₹2,522)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +7.12%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹63.81 moving sideways between 50 DMA (₹58.18) and 200 DMA (₹58.63); conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                     | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹288.22 vs 200-day average ₹272.57 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.4%
* **Banking**: 18.9%
* **Commodities**: 9.6%
* **Power**: 8.2%
* **IT**: 6.9%
* **Broad Market**: 5.1%
* **Consumption**: 4.9%
* **Defense**: 4.9%
* **Insurance**: 4.9%
* **Financial Services**: 4.3%
* **Consumer Electronics**: 3.4%
* **Telecom**: 2.9%
* **Auto**: 2.8%
* **Pharma**: 1.6%
* **Infrastructure**: 1.2%
* **Financials (combined)**: 28.1%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.6%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| Financials        | 28.1%      | 25.0% | ⚠️ BREACH | FEDBAN (2.6%), HDFBAN (15.9%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.5%), +1 more |
| State-owned (PSU) | 19.1%      | 25.0% | OK        | ONGC (1.3%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 9.6%       | 25.0% | OK        | ICIGOL (4.4%), ICIPSE (5.2%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 15.9%           | 16.45%             | +0.43% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 15.4%           | 15.68%             | +0.32% via ICINIF                        |
| WIPRO    | 6.5%            | 6.51%              | Direct only                              |
| ICIPSE   | 5.2%            | 5.21%              | Direct only                              |
| TATGLO   | 4.9%            | 4.91%              | Direct only                              |
| BHAELE   | 4.9%            | 4.89%              | Direct only                              |
| LIC      | 4.9%            | 4.88%              | Direct only                              |
| ICIGOL   | 4.4%            | 4.38%              | Direct only                              |
| JSWENE   | 4.2%            | 4.23%              | Direct only                              |
| ICINIF   | 3.7%            | 3.72%              | Direct only                              |
| LGELEC   | 3.4%            | 3.39%              | Direct only                              |
| IDECEL   | 2.9%            | 2.94%              | Direct only                              |
| ASHLEY   | 2.8%            | 2.78%              | Direct only                              |
| FEDBAN   | 2.6%            | 2.63%              | +0.01% via KOTAKBKETF                    |
| TATCAP   | 2.5%            | 2.48%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.1%** (Target: 50.0%, Gap: +44.9%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **94.9%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.7%     | ₹24,639 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,493  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,348  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 15.9%    | ₹105,599 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.4%    | ₹101,817 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,320   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,876   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.5%     | ₹43,164  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 4.9%     | ₹32,320  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.4%     | ₹22,474  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.8%     | ₹18,439  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.6%     | ₹17,400  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.5%     | ₹16,406  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹11,463  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.3%     | ₹8,756   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,690   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,856   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,718   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,914   | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 5.2%     | ₹34,508  | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.9%     | ₹32,559  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹32,384  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹28,061  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹12,254  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,531  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,468   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹4,224   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,922   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,351   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.4%     | ₹29,003  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹19,455  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,522   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,914)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,522)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,718)  |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,856)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,351)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,922)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹4,224)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,348)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,493) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,690)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,468)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹50,724.18  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹50,724.18  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹5,655.74   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹131,872**, Tax savings potential: **₹18,009**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹812.30  | ₹1455.47   | ₹35,375             | LTCG      | ₹4,422                |
| RELIND   |       27 | ₹1339.70 | ₹2228.99   | ₹24,011             | LTCG      | ₹3,001                |
| LIC      |       45 | ₹404.00  | ₹895.05    | ₹22,097             | LTCG      | ₹2,762                |
| WIPRO    |      170 | ₹196.20  | ₹304.31    | ₹18,379             | LTCG/STCG | ₹2,336                |
| ICIPSE   |      193 | ₹178.80  | ₹250.36    | ₹13,810             | STCG      | ₹2,762                |
| ICIGOL   |      250 | ₹116.01  | ₹138.24    | ₹5,557              | STCG      | ₹1,111                |
| JSWENE   |       28 | ₹519.65  | ₹668.00    | ₹4,154              | LTCG      | ₹519                  |
| JIOFIN   |       28 | ₹231.20  | ₹344.38    | ₹3,169              | LTCG      | ₹396                  |
| SJVLIM   |       67 | ₹58.53   | ₹86.95     | ₹1,904              | LTCG      | ₹238                  |
| ASHLEY   |       33 | ₹173.95  | ₹230.20    | ₹1,856              | LTCG      | ₹232                  |

*Showing top 10 of 17 loss-harvest candidates.*


