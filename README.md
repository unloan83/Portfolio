# Orchestrated Multi-Agent Portfolio Audit - 2026-10-23

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-23
* **Portfolio XIRR**: **-8.04%** (Current Traded Positions Value: ₹469,628)
* **Benchmark XIRR**: **3.00%** (Simulated Benchmark Value: ₹603,630)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| FEDBAN     |         48 |           48 | ₹16,363         | 31.51%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,707          | 29.65%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹17,040         | 28.03%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.30%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,141          | 15.22%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,042          | 12.35%  | Full                 |
| BHAELE     |         80 |           48 | ₹17,376         | 11.29%  | Partial (48/80 sh)   |
| TATPOW     |          8 |            8 | ₹2,785          | 7.70%   | Full                 |
| NHPC       |         55 |           55 | ₹3,841          | 6.71%   | Full                 |
| GAIL       |         61 |           61 | ₹10,002         | 5.51%   | Full                 |
| TATGLO     |         30 |           30 | ₹28,917         | 4.03%   | Full                 |
| NTPC       |         12 |           12 | ₹3,576          | 2.85%   | Full                 |
| DRREDD     |          6 |            6 | ₹7,377          | 2.54%   | Full                 |
| JSWENE     |         54 |           54 | ₹24,222         | -4.08%  | Full                 |
| HINPET     |         14 |           14 | ₹4,736          | -4.75%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,008          | -4.89%  | Full                 |
| ONGC       |         39 |           39 | ₹8,872          | -5.12%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.87%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,682          | -10.32% | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹88,060         | -11.72% | Partial (74/76 sh)   |
| ICINIF     |         86 |           86 | ₹22,148         | -13.73% | Full                 |
| HDFBAN     |        130 |           75 | ₹51,960         | -14.60% | Partial (75/130 sh)  |
| HDF250     |         24 |           24 | ₹3,955          | -18.31% | Full                 |
| SJVLIM     |         67 |           67 | ₹3,176          | -18.95% | Full                 |
| WIPRO      |        220 |          170 | ₹32,273         | -19.66% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹30,000         | -20.03% | Full                 |
| JIOFIN     |         53 |           28 | ₹5,741          | -20.05% | Partial (28/53 sh)   |
| KOTAKBKETF |         30 |           30 | ₹1,688          | -24.52% | Full                 |
| MIR150     |        194 |          194 | ₹4,080          | -25.86% | Full                 |
| ICIPSE     |        193 |          193 | ₹37,019         | -34.13% | Full                 |
| LIC        |         80 |           45 | ₹17,168         | -55.99% | Partial (45/80 sh)   |

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
| Symbol     | Sector               | Weight   | Total Return   | Trailing Stop   | Decision    | Action                          | Reasoning                                                                                                                                                                                                                                                      | Thesis Status   |   Conviction |
|:-----------|:---------------------|:---------|:---------------|:----------------|:------------|:--------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|-------------:|
| RELIND     | Oil & Gas            | 15.0%    | +2.70%         | N/A             | SELL        | Exit all 76 sh (~₹90,440)       | Trend exit: month-end close ₹1187.00 < 10-month average ₹1348.24. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 14.9%    | -5.87%         | N/A             | SELL        | Exit all 130 sh (~₹90,064)      | Trend exit: month-end close ₹708.70 < 10-month average ₹793.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 6.9%     | -19.70%        | N/A             | SELL        | Exit all 220 sh (~₹41,765)      | Thesis invalidated: Price ₹189.84 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 6.1%     | -23.66%        | N/A             | SELL        | Exit all 193 sh (~₹37,019)      | Thesis invalidated: Price ₹191.81 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.1%     | -57.52%        | N/A             | SELL        | Exit all 80 sh (~₹30,520)       | Thesis invalidated: Price ₹381.50 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 5.0%     | -13.51%        | N/A             | SELL        | Exit all 250 sh (~₹30,000)      | Thesis invalidated: Price ₹120.00 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.8%     | +129.36%       | ₹330.97         | SELL        | Exit all 80 sh (~₹28,960)       | Trend exit: month-end close ₹388.30 < 10-month average ₹412.84. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| TATGLO     | Consumption          | 4.8%     | +20.39%        | N/A             | SELL        | Exit all 30 sh (~₹28,917)       | Trend exit: month-end close ₹949.50 < 10-month average ₹1090.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                   | INTACT          |            3 |
| JSWENE     | Power                | 4.0%     | -11.82%        | N/A             | SELL        | Exit all 54 sh (~₹24,222)       | Thesis invalidated: Price ₹448.55 <= invalidation price ₹468.00.                                                                                                                                                                                               | INVALIDATED     |            3 |
| ICINIF     | Broad Market         | 3.7%     | -5.00%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 32 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +41.29%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1610.70 moving sideways between 50 DMA (₹1683.29) and 200 DMA (₹1562.38); conviction (4/5) thesis INTACT above invalidation (₹1003.20).                                                                                             | INTACT          |            4 |
| IDECEL     | Telecom              | 2.8%     | +53.72%        | ₹11.05          | HOLD        | Hold                            | Pullback hold: Price ₹11.36 < 200 DMA (₹12.30) with return +53.72%; thesis remains INTACT above invalidation (₹7.02).                                                                                                                                          | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +127.43%       | ₹259.30         | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return +127.43%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +46.44%        | N/A             | SELL        | Exit all 106 sh (~₹15,365)      | Trend exit: month-end close ₹154.19 < 10-month average ₹169.46. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.3%     | -5.90%         | N/A             | SELL        | Exit all 46 sh (~₹14,110)       | Trend exit: month-end close ₹327.95 < 10-month average ₹338.49. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.9%     | -24.81%        | N/A             | SELL        | Exit all 138 sh (~₹11,207)      | Thesis invalidated: Price ₹81.21 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -11.69%        | N/A             | SELL        | Exit all 53 sh (~₹10,867)       | Thesis invalidated: Price ₹205.03 <= invalidation price ₹213.61.                                                                                                                                                                                               | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +5.41%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹163.96 < 200 DMA (₹165.08) with return +5.41%; thesis remains INTACT above invalidation (₹136.88).                                                                                                                                       | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.5%     | -6.58%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹225.80 < 10-month average ₹255.21. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.2%     | +3.53%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹1233.00 < 10-month average ₹1249.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| HINPET     | Oil & Gas            | 0.8%     | -9.06%         | N/A             | SELL        | Exit all 14 sh (~₹4,736)        | Thesis invalidated: Price ₹338.30 <= invalidation price ₹342.25.                                                                                                                                                                                               | INVALIDATED     |            3 |
| MIR150     | Broad Market         | 0.7%     | -9.31%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹21.03 < 200 DMA (₹22.65) with return -9.31%; thesis remains INTACT above invalidation (₹20.41).                                                                                                                                          | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -9.28%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹286.30 moving sideways between 50 DMA (₹288.91) and 200 DMA (₹280.78); conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                 | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -6.41%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹164.81 < 200 DMA (₹170.89) with return -6.41%; thesis remains INTACT above invalidation (₹154.96).                                                                                                                                       | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +19.55%        | N/A             | SELL        | Exit all 55 sh (~₹3,841)        | Trend exit: month-end close ₹72.81 < 10-month average ₹77.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +7.49%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹322.75 < 10-month average ₹353.83. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.5%     | -45.88%        | N/A             | SELL        | Exit all 67 sh (~₹3,176)        | Thesis invalidated: Price ₹47.40 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +83.97%        | ₹135.92         | HOLD        | Hold                            | Pullback hold: Price ₹157.07 < 200 DMA (₹157.13) with return +83.97%; thesis remains INTACT above invalidation (₹78.55).                                                                                                                                       | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.5%     | +22.77%        | N/A             | SELL        | Exit all 8 sh (~₹2,785)         | Trend exit: month-end close ₹359.00 < 10-month average ₹382.51. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +10.07%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹35.62 moving sideways between 50 DMA (₹33.12) and 200 DMA (₹34.10); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.3%     | +65.39%        | ₹208.60         | HOLD        | Hold                            | Pullback hold: Price ₹204.18 < 200 DMA (₹233.15) with return +65.39%; thesis remains INTACT above invalidation (₹117.28).                                                                                                                                      | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -5.57%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹56.25 < 200 DMA (₹58.79) with return -5.57%; thesis remains INTACT above invalidation (₹52.42).                                                                                                                                          | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹257.22 vs 200-day average ₹273.94 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.0%
* **Banking**: 17.9%
* **Commodities**: 11.1%
* **Power**: 8.1%
* **IT**: 7.4%
* **Insurance**: 5.1%
* **Broad Market**: 5.0%
* **Defense**: 4.8%
* **Consumption**: 4.8%
* **Financial Services**: 4.1%
* **Consumer Electronics**: 3.5%
* **Telecom**: 2.8%
* **Auto**: 2.5%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 27.1%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.1%      | 25.0% | ⚠️ BREACH | TATPOW (0.5%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.5%), NTPGRE (1.9%), +7 more          |
| Financials        | 27.1%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (14.9%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.3%), +1 more |
| State-owned (PSU) | 19.3%      | 25.0% | OK        | ONGC (1.5%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 11.1%      | 25.0% | OK        | ICIGOL (5.0%), ICIPSE (6.1%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 14.9%           | 15.42%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 15.0%           | 15.30%             | +0.31% via ICINIF                        |
| WIPRO    | 6.9%            | 6.92%              | Direct only                              |
| ICIPSE   | 6.1%            | 6.13%              | Direct only                              |
| LIC      | 5.1%            | 5.06%              | Direct only                              |
| ICIGOL   | 5.0%            | 4.97%              | Direct only                              |
| BHAELE   | 4.8%            | 4.80%              | Direct only                              |
| TATGLO   | 4.8%            | 4.79%              | Direct only                              |
| JSWENE   | 4.0%            | 4.01%              | Direct only                              |
| ICINIF   | 3.7%            | 3.67%              | Direct only                              |
| LGELEC   | 3.5%            | 3.47%              | Direct only                              |
| IDECEL   | 2.8%            | 2.82%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.72%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.55%              | Direct only                              |
| TATCAP   | 2.3%            | 2.34%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.7%     | ₹22,148 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,080  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹3,955  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.0%    | ₹90,440 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 14.9%    | ₹90,064 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.2%     | ₹7,377  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,576  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.9%     | ₹41,765 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.1%     | ₹30,520 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹20,939 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹16,363 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,365 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.3%     | ₹14,110 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹10,002 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.5%     | ₹8,872  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,008  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.5%     | ₹2,785  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,707  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,688  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.1%     | ₹37,019 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹28,960 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.8%     | ₹28,917 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.0%     | ₹24,222 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.9%     | ₹11,207 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹10,867 | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,736  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹3,841  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.5%     | ₹3,176  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,141  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 5.0%     | ₹30,000 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.8%     | ₹17,040 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.3%     | ₹2,042  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,688)  |
| SEQSCI     | Pharma         | 0.3%     |            2 | Exit all 10 sh (~₹2,042)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,707)  |
| TATPOW     | Power          | 0.5%     |            4 | Exit all 8 sh (~₹2,785)   |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,141)  |
| SJVLIM     | Power          | 0.5%     |            3 | Exit all 67 sh (~₹3,176)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹3,841)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹3,955)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,008)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,080) |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,736)  |
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
| Total Unrealised LTCG (> 365 days)    | ₹33,860.70  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹33,860.70  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,264.94   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹153,926**, Tax savings potential: **₹21,606**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹692.80  | ₹1267.91   | ₹43,133             | LTCG/STCG | ₹5,481                |
| RELIND   |       72 | ₹1190.00 | ₹1639.79   | ₹32,385             | LTCG/STCG | ₹4,286                |
| LIC      |       45 | ₹381.50  | ₹895.05    | ₹23,110             | LTCG/STCG | ₹3,473                |
| WIPRO    |      170 | ₹189.84  | ₹304.31    | ₹19,460             | LTCG/STCG | ₹2,529                |
| ICIPSE   |      193 | ₹191.81  | ₹250.36    | ₹11,299             | STCG      | ₹2,260                |
| JSWENE   |       28 | ₹448.55  | ₹668.00    | ₹6,145              | LTCG      | ₹768                  |
| ICIGOL   |      250 | ₹120.00  | ₹138.24    | ₹4,560              | STCG      | ₹912                  |
| JIOFIN   |       28 | ₹205.03  | ₹344.38    | ₹3,902              | LTCG      | ₹488                  |
| ASHLEY   |       43 | ₹144.95  | ₹212.38    | ₹2,899              | LTCG      | ₹362                  |
| SJVLIM   |       67 | ₹47.40   | ₹86.95     | ₹2,650              | LTCG      | ₹331                  |

*Showing top 10 of 19 loss-harvest candidates.*


