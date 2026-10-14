# Orchestrated Multi-Agent Portfolio Audit - 2026-10-14

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-14
* **Portfolio XIRR**: **-7.16%** (Current Traded Positions Value: ₹479,776)
* **Benchmark XIRR**: **3.08%** (Simulated Benchmark Value: ₹604,236)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹19,005         | 38.07%  | Full                 |
| FEDBAN     |         48 |           48 | ₹15,840         | 30.44%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,511          | 18.30%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.55%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,330          | 15.87%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,353         | 13.36%  | Partial (48/80 sh)   |
| NIPNIT     |         76 |           76 | ₹2,552          | 11.36%  | Full                 |
| NHPC       |         55 |           55 | ₹4,055          | 8.80%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,824          | 8.29%   | Full                 |
| GAIL       |         61 |           61 | ₹10,185         | 7.44%   | Full                 |
| HDF250     |         24 |           24 | ₹4,316          | 7.13%   | Full                 |
| NTPC       |         12 |           12 | ₹3,764          | 4.74%   | Full                 |
| TATGLO     |         30 |           30 | ₹29,637         | 4.58%   | Full                 |
| DRREDD     |          6 |            6 | ₹7,296          | 1.90%   | Full                 |
| JSWENE     |         54 |           54 | ₹26,476         | -0.99%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,101          | -3.71%  | Full                 |
| ONGC       |         39 |           39 | ₹8,794          | -5.94%  | Full                 |
| HINPET     |         14 |           14 | ₹4,635          | -5.99%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.97%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,685          | -10.39% | Partial (53/106 sh)  |
| MIR150     |        194 |          194 | ₹4,330          | -11.86% | Full                 |
| RELIND     |         76 |           74 | ₹86,920         | -12.35% | Partial (74/76 sh)   |
| SJVLIM     |         67 |           67 | ₹3,804          | -13.84% | Full                 |
| HDFBAN     |        130 |           75 | ₹53,303         | -14.08% | Partial (75/130 sh)  |
| ICIGOL     |        250 |          250 | ₹31,003         | -16.35% | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,727          | -17.33% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,132          | -17.91% | Partial (28/53 sh)   |
| ICINIF     |         86 |           86 | ₹21,847         | -18.26% | Full                 |
| ICIPSE     |        193 |          193 | ₹40,893         | -23.80% | Full                 |
| WIPRO      |        220 |          170 | ₹29,056         | -24.78% | Partial (170/220 sh) |
| LIC        |         80 |           45 | ₹17,730         | -55.46% | Partial (45/80 sh)   |

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
| Symbol     | Sector               | Weight   | Total Return   | Trailing Stop   | Decision    | Action                           | Reasoning                                                                                                                                                                                                   | Thesis Status   |   Conviction |
|:-----------|:---------------------|:---------|:---------------|:----------------|:------------|:---------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|-------------:|
| HDFBAN     | Banking              | 14.9%    | -3.44%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 49 sessions                                                                                                                               | INTACT          |            5 |
| RELIND     | Oil & Gas            | 14.4%    | +1.37%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 49 sessions                                                                                                                               | INTACT          |            5 |
| ICIPSE     | Commodities          | 6.6%     | -15.67%        | N/A             | SELL        | Exit all 193 sh (~₹40,893)       | Thesis invalidated: Price ₹211.88 <= invalidation price ₹231.16.                                                                                                                                            | INVALIDATED     |            3 |
| WIPRO      | IT                   | 6.1%     | -27.70%        | N/A             | SELL        | Exit all 220 sh (~₹37,602)       | Thesis invalidated: Price ₹170.92 <= invalidation price ₹208.04.                                                                                                                                            | INVALIDATED     |            4 |
| LIC        | Insurance            | 5.1%     | -56.13%        | N/A             | SELL        | Exit all 80 sh (~₹31,520)        | Thesis invalidated: Price ₹394.00 <= invalidation price ₹790.25.                                                                                                                                            | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 5.0%     | -10.62%        | N/A             | SELL        | Exit all 250 sh (~₹31,003)       | Thesis invalidated: Price ₹124.01 <= invalidation price ₹131.80.                                                                                                                                            | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.9%     | +142.25%       | ₹330.97         | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 23 sessions                                                                                                                               | INTACT          |            3 |
| TATGLO     | Consumption          | 4.8%     | +23.39%        | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 45 sessions                                                                                                                               | INTACT          |            3 |
| JSWENE     | Power                | 4.3%     | -3.62%         | N/A             | TRIM        | Hold (below minimum trade)       | Risk group cap breach: Risk factor group exposure (28.0%) exceeds limit (25.0%); trim holding (4.3% weight) for risk-factor control.                                                                        | INTACT          |            3 |
| LGELEC     | Consumer Electronics | 3.7%     | +52.72%        | ₹1277.50        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                             | INTACT          |            4 |
| ICINIF     | Broad Market         | 3.5%     | -6.29%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 24 sessions                                                                                                                               | INTACT          |            4 |
| IDECEL     | Telecom              | 3.1%     | +71.45%        | ₹11.05          | HOLD        | Hold                             | Consolidation hold: Price ₹12.67 moving sideways between 50 DMA (₹13.88) and 200 DMA (₹12.29); conviction (2/5) thesis INTACT above invalidation (₹7.02).                                                   | INTACT          |            2 |
| FEDBAN     | Banking              | 2.6%     | +120.16%       | ₹259.30         | HOLD        | Hold                             | Consolidation hold: Price ₹330.00 moving sideways between 50 DMA (₹341.39) and 200 DMA (₹305.55); conviction (4/5) thesis INTACT above invalidation (₹131.90).                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +46.49%        | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 22 sessions                                                                                                                               | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | -2.78%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹316.95 < 200 DMA (₹339.81) with return -2.78%; thesis remains INTACT above invalidation (₹286.88).                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 2.0%     | -15.07%        | N/A             | SELL        | Exit all 138 sh (~₹12,657)       | Thesis invalidated: Price ₹91.72 <= invalidation price ₹99.36.                                                                                                                                              | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.9%     | -5.68%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 42 sessions                                                                                                                               | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.6%     | +7.34%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹166.96 moving sideways between 50 DMA (₹172.51) and 200 DMA (₹165.03); conviction (4/5) thesis INTACT above invalidation (₹136.88).                                              | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -7.40%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 49 sessions                                                                                                                               | INTACT          |            4 |
| DRREDD     | Pharma               | 1.2%     | +2.39%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹1216.00 < 200 DMA (₹1239.09) with return +2.39%; thesis remains INTACT above invalidation (₹1009.47).                                                                                 | INTACT          |            5 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                 | INTACT          |            3 |
| HINPET     | Oil & Gas            | 0.7%     | -11.01%        | N/A             | SELL        | Exit all 14 sh (~₹4,635)         | Thesis invalidated: Price ₹331.05 <= invalidation price ₹342.25.                                                                                                                                            | INVALIDATED     |            3 |
| MIR150     | Broad Market         | 0.7%     | -3.75%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹22.32 < 200 DMA (₹22.68) with return -3.75%; thesis remains INTACT above invalidation (₹20.41).                                                                                       | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +2.12%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹179.82 moving sideways between 50 DMA (₹183.56) and 200 DMA (₹170.63); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                              | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -7.18%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return -7.18%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                             | INTACT          |            4 |
| NHPC       | Power                | 0.7%     | +26.19%        | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹73.72 < 200 DMA (₹77.16) with return +26.19%; thesis remains INTACT above invalidation (₹53.75).                                                                                      | INTACT          |            3 |
| SJVLIM     | Power                | 0.6%     | -35.19%        | N/A             | SELL        | Exit all 67 sh (~₹3,804)         | Thesis invalidated: Price ₹56.77 <= invalidation price ₹80.58.                                                                                                                                              | INVALIDATED     |            3 |
| NTPC       | Power                | 0.6%     | +13.16%        | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 48 sessions                                                                                                                               | INTACT          |            5 |
| GUJPPL     | Infrastructure       | 0.6%     | +105.59%       | ₹135.92         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +105.59%, position weight 0.6%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                            | INTACT          |            3 |
| TATPOW     | Power                | 0.5%     | +24.50%        | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹353.00 < 200 DMA (₹383.25) with return +24.50%; thesis remains INTACT above invalidation (₹249.52).                                                                                   | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | REVIEW      | Review                           | invalidation breached on broker price (1 of 3 closes). Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +3.77%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹33.58 < 200 DMA (₹34.36) with return +3.77%; thesis remains INTACT above invalidation (₹28.48).                                                                                       | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +88.72%        | ₹208.60         | HOLD        | Hold                             | Pullback hold: Price ₹232.98 < 200 DMA (₹233.00) with return +88.72%; thesis remains INTACT above invalidation (₹117.28).                                                                                   | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -3.36%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹57.57 < 200 DMA (₹58.90) with return -3.36%; thesis remains INTACT above invalidation (₹52.42).                                                                                       | INTACT          |            4 |

### Sector Concentration Metrics
* **Oil & Gas**: 19.4%
* **Banking**: 17.8%
* **Commodities**: 11.6%
* **Power**: 8.7%
* **IT**: 6.5%
* **Insurance**: 5.1%
* **Defense**: 4.9%
* **Broad Market**: 4.9%
* **Consumption**: 4.8%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.7%
* **Telecom**: 3.1%
* **Auto**: 2.5%
* **Pharma**: 1.6%
* **Infrastructure**: 1.4%
* **Financials (combined)**: 27.1%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.0%      | 25.0% | ⚠️ BREACH | TATPOW (0.5%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (2.0%), +7 more          |
| Financials        | 27.1%      | 25.0% | ⚠️ BREACH | FEDBAN (2.6%), HDFBAN (14.9%), KOTAKBKETF (0.3%), JIOFIN (1.9%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.7%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.6%), HINPET (0.7%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 11.6%      | 25.0% | OK        | ICIGOL (5.0%), ICIPSE (6.6%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 14.9%           | 15.42%             | +0.41% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 14.4%           | 14.73%             | +0.30% via ICINIF                        |
| ICIPSE   | 6.6%            | 6.61%              | Direct only                              |
| WIPRO    | 6.1%            | 6.08%              | Direct only                              |
| LIC      | 5.1%            | 5.09%              | Direct only                              |
| ICIGOL   | 5.0%            | 5.01%              | Direct only                              |
| BHAELE   | 4.9%            | 4.94%              | Direct only                              |
| TATGLO   | 4.8%            | 4.79%              | Direct only                              |
| JSWENE   | 4.3%            | 4.28%              | Direct only                              |
| LGELEC   | 3.7%            | 3.66%              | Direct only                              |
| ICINIF   | 3.5%            | 3.53%              | Direct only                              |
| IDECEL   | 3.1%            | 3.07%              | Direct only                              |
| FEDBAN   | 2.6%            | 2.57%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.48%              | Direct only                              |
| TATCAP   | 2.4%            | 2.36%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **4.9%** (Target: 50.0%, Gap: +45.1%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.1%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.5%     | ₹21,847 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,330  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,316  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 14.9%    | ₹92,391 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.4%    | ₹89,270 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.2%     | ₹7,296  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,764  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.1%     | ₹37,602 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.1%     | ₹31,520 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.7%     | ₹22,633 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.6%     | ₹15,840 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,370 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹14,580 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.6%     | ₹10,185 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,794  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,101  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.5%     | ₹2,824  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,552  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,727  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.6%     | ₹40,893 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹30,588 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.8%     | ₹29,637 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.3%     | ₹26,476 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 2.0%     | ₹12,657 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.9%     | ₹11,607 | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.7%     | ₹4,635  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,055  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,804  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.6%     | ₹3,511  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 5.0%     | ₹31,003 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 3.1%     | ₹19,005 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,330  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,727)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,330)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,552)  |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.5%     |            4 | Exit all 8 sh (~₹2,824)   |
| GUJPPL     | Infrastructure | 0.6%     |            3 | Exit all 20 sh (~₹3,511)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,804)  |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,055)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,101)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,316)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,330) |
| HINPET     | Oil & Gas      | 0.7%     |            3 | Exit all 14 sh (~₹4,635)  |
| ENGIND     | Infrastructure | 0.8%     |            3 | Exit all 21 sh (~₹4,866)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹39,105.70  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest  | ₹39,105.70  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,373.70   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹149,132**, Tax savings potential: **₹20,977**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹710.70  | ₹1267.91   | ₹41,790             | LTCG/STCG | ₹5,286                |
| RELIND   |       72 | ₹1174.60 | ₹1639.79   | ₹33,494             | LTCG/STCG | ₹4,453                |
| WIPRO    |      170 | ₹170.92  | ₹304.31    | ₹22,677             | LTCG/STCG | ₹3,101                |
| LIC      |       45 | ₹394.00  | ₹895.05    | ₹22,547             | LTCG/STCG | ₹3,579                |
| ICIPSE   |      193 | ₹211.88  | ₹250.36    | ₹7,426              | STCG      | ₹1,485                |
| JSWENE   |       28 | ₹490.30  | ₹668.00    | ₹4,976              | LTCG      | ₹622                  |
| ICIGOL   |      250 | ₹124.01  | ₹138.24    | ₹3,557              | STCG      | ₹711                  |
| JIOFIN   |       28 | ₹219.00  | ₹344.38    | ₹3,511              | LTCG      | ₹439                  |
| ASHLEY   |       43 | ₹145.00  | ₹212.38    | ₹2,897              | LTCG      | ₹362                  |
| SJVLIM   |       67 | ₹56.77   | ₹86.95     | ₹2,022              | LTCG      | ₹253                  |

*Showing top 10 of 21 loss-harvest candidates.*


