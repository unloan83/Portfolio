# Orchestrated Multi-Agent Portfolio Audit - 2026-10-28

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-28
* **Portfolio XIRR**: **-7.73%** (Current Traded Positions Value: ₹472,343)
* **Benchmark XIRR**: **3.17%** (Simulated Benchmark Value: ₹606,270)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| FEDBAN     |         48 |           48 | ₹16,608         | 31.97%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹17,790         | 31.32%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,661          | 22.82%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.17%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,203          | 15.68%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,270          | 15.04%  | Full                 |
| BHAELE     |         80 |           48 | ₹17,441         | 11.37%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,094          | 9.05%   | Full                 |
| DRREDD     |          6 |            6 | ₹8,012          | 7.65%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,680          | 6.25%   | Full                 |
| GAIL       |         61 |           61 | ₹10,052         | 5.92%   | Full                 |
| TATGLO     |         30 |           30 | ₹30,006         | 4.81%   | Full                 |
| NTPC       |         12 |           12 | ₹3,645          | 3.52%   | Full                 |
| JSWENE     |         54 |           54 | ₹26,082         | -1.50%  | Full                 |
| HINPET     |         14 |           14 | ₹4,860          | -3.33%  | Full                 |
| PETLNG     |         14 |           14 | ₹3,989          | -5.12%  | Full                 |
| ONGC       |         39 |           39 | ₹8,771          | -5.97%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.81%  | Full                 |
| HDF250     |         24 |           24 | ₹4,106          | -8.06%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,677          | -10.29% | Partial (53/106 sh)  |
| ICINIF     |         86 |           86 | ₹22,219         | -12.46% | Full                 |
| RELIND     |         76 |           74 | ₹85,692         | -12.71% | Partial (74/76 sh)   |
| HDFBAN     |        130 |           75 | ₹51,397         | -14.80% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,413          | -16.83% | Full                 |
| MIR150     |        194 |          194 | ₹4,208          | -17.80% | Full                 |
| ICIGOL     |        250 |          250 | ₹30,378         | -18.08% | Full                 |
| JIOFIN     |         53 |           28 | ₹5,744          | -19.92% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹31,365         | -20.80% | Partial (170/220 sh) |
| KOTAKBKETF |         30 |           30 | ₹1,691          | -22.41% | Full                 |
| ICIPSE     |        193 |          193 | ₹37,000         | -33.60% | Full                 |
| LIC        |         80 |           45 | ₹17,615         | -54.41% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 14.7%    | -6.89%         | N/A             | SELL        | Exit all 130 sh (~₹89,089)       | Trend exit: month-end close ₹708.70 < 10-month average ₹793.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 14.5%    | -0.06%         | N/A             | SELL        | Exit all 76 sh (~₹88,008)        | Trend exit: month-end close ₹1187.00 < 10-month average ₹1348.24. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.7%     | -21.96%        | N/A             | SELL        | Exit all 220 sh (~₹40,590)       | Thesis invalidated: Price ₹184.50 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 6.1%     | -23.70%        | N/A             | SELL        | Exit all 193 sh (~₹37,000)       | Thesis invalidated: Price ₹191.71 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.2%     | -56.41%        | N/A             | SELL        | Exit all 80 sh (~₹31,316)        | Thesis invalidated: Price ₹391.45 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 5.0%     | -12.42%        | N/A             | SELL        | Exit all 250 sh (~₹30,378)       | Thesis invalidated: Price ₹121.51 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| TATGLO     | Consumption          | 4.9%     | +24.93%        | N/A             | SELL        | Exit all 30 sh (~₹30,006)        | Trend exit: month-end close ₹949.50 < 10-month average ₹1090.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                   | INTACT          |            3 |
| BHAELE     | Defense              | 4.8%     | +130.22%       | ₹330.97         | SELL        | Exit all 80 sh (~₹29,068)        | Trend exit: month-end close ₹388.30 < 10-month average ₹412.84. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| JSWENE     | Power                | 4.3%     | -5.05%         | N/A             | SELL        | Exit all 54 sh (~₹26,082)        | Trend exit: month-end close ₹494.70 < 10-month average ₹520.03. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.7%     | -4.69%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 35 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.6%     | +48.30%        | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +60.49%        | ₹11.05          | HOLD        | Hold                             | Pullback hold: Price ₹11.86 < 200 DMA (₹12.30) with return +60.49%; thesis remains INTACT above invalidation (₹7.02).                                                                                                                                          | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +130.84%       | ₹259.30         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +130.84%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +46.34%        | N/A             | SELL        | Exit all 106 sh (~₹15,354)       | Trend exit: month-end close ₹154.19 < 10-month average ₹169.46. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.3%     | -5.12%         | N/A             | SELL        | Exit all 46 sh (~₹14,228)        | Trend exit: month-end close ₹327.95 < 10-month average ₹338.49. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.9%     | -22.94%        | N/A             | SELL        | Exit all 138 sh (~₹11,484)       | Thesis invalidated: Price ₹83.22 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -11.64%        | N/A             | SELL        | Exit all 53 sh (~₹10,873)        | Thesis invalidated: Price ₹205.15 <= invalidation price ₹213.61.                                                                                                                                                                                               | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +5.93%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹164.78 < 200 DMA (₹165.06) with return +5.93%; thesis remains INTACT above invalidation (₹136.88).                                                                                                                                       | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -7.65%         | N/A             | SELL        | Hold (below minimum trade)       | Trend exit: month-end close ₹225.80 < 10-month average ₹255.21. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +12.44%        | N/A             | SELL        | Hold (below minimum trade)       | Trend exit: month-end close ₹1233.00 < 10-month average ₹1249.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| HINPET     | Oil & Gas            | 0.8%     | -6.68%         | N/A             | SELL        | Exit all 14 sh (~₹4,860)         | Trend exit: month-end close ₹350.35 < 10-month average ₹380.95. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -6.47%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹21.69 < 200 DMA (₹22.63) with return -6.47%; thesis remains INTACT above invalidation (₹20.41).                                                                                                                                          | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -2.83%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹171.10 moving sideways between 50 DMA (₹181.13) and 200 DMA (₹170.91); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| NHPC       | Power                | 0.7%     | +27.42%        | N/A             | SELL        | Exit all 55 sh (~₹4,094)         | Trend exit: month-end close ₹72.81 < 10-month average ₹77.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | -9.73%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹284.90 moving sideways between 50 DMA (₹289.53) and 200 DMA (₹280.86); conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                 | INTACT          |            4 |
| NTPC       | Power                | 0.6%     | +9.57%         | N/A             | SELL        | Hold (below minimum trade)       | Trend exit: month-end close ₹322.75 < 10-month average ₹353.83. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -41.84%        | N/A             | SELL        | Exit all 67 sh (~₹3,413)         | Thesis invalidated: Price ₹50.94 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +87.58%        | ₹135.92         | HOLD        | Hold                             | Consolidation hold: Price ₹160.16 moving sideways between 50 DMA (₹163.30) and 200 DMA (₹156.86); conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                  | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.4%     | +18.15%        | N/A             | SELL        | Exit all 8 sh (~₹2,680)          | Trend exit: month-end close ₹359.00 < 10-month average ₹382.51. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +8.19%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹35.01 moving sideways between 50 DMA (₹33.17) and 200 DMA (₹34.00); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +83.88%        | ₹208.60         | HOLD        | Hold                             | Pullback hold: Price ₹227.00 < 200 DMA (₹233.27) with return +83.88%; thesis remains INTACT above invalidation (₹117.28).                                                                                                                                      | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -5.37%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹56.37 < 200 DMA (₹58.71) with return -5.37%; thesis remains INTACT above invalidation (₹52.42).                                                                                                                                          | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹259.59 vs 200-day average ₹273.38 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 19.5%
* **Banking**: 17.7%
* **Commodities**: 11.1%
* **Power**: 8.5%
* **IT**: 7.1%
* **Insurance**: 5.2%
* **Broad Market**: 5.0%
* **Consumption**: 4.9%
* **Defense**: 4.8%
* **Financial Services**: 4.1%
* **Consumer Electronics**: 3.6%
* **Telecom**: 2.9%
* **Auto**: 2.5%
* **Pharma**: 1.7%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 27.0%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.0%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.9%), +7 more          |
| Financials        | 27.0%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (14.7%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.3%), +1 more |
| State-owned (PSU) | 19.5%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 11.1%      | 25.0% | OK        | ICIGOL (5.0%), ICIPSE (6.1%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 14.7%           | 15.17%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 14.5%           | 14.80%             | +0.31% via ICINIF                        |
| WIPRO    | 6.7%            | 6.68%              | Direct only                              |
| ICIPSE   | 6.1%            | 6.09%              | Direct only                              |
| LIC      | 5.2%            | 5.16%              | Direct only                              |
| ICIGOL   | 5.0%            | 5.00%              | Direct only                              |
| TATGLO   | 4.9%            | 4.94%              | Direct only                              |
| BHAELE   | 4.8%            | 4.79%              | Direct only                              |
| JSWENE   | 4.3%            | 4.29%              | Direct only                              |
| ICINIF   | 3.7%            | 3.66%              | Direct only                              |
| LGELEC   | 3.6%            | 3.62%              | Direct only                              |
| IDECEL   | 2.9%            | 2.93%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.74%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.53%              | Direct only                              |
| TATCAP   | 2.3%            | 2.34%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.7%     | ₹22,219 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,208  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,106  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 14.7%    | ₹89,089 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.5%    | ₹88,008 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,012  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,645  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.7%     | ₹40,590 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.2%     | ₹31,316 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.6%     | ₹21,978 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹16,608 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,354 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.3%     | ₹14,228 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹10,052 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,771  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹3,989  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,680  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,661  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,691  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.1%     | ₹37,000 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.9%     | ₹30,006 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹29,068 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.3%     | ₹26,082 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.9%     | ₹11,484 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹10,873 | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,860  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,094  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,413  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,203  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 5.0%     | ₹30,378 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹17,790 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,270  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,691)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,270)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,661)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,680)   |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,203)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,413)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹3,989)  |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,094)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,106)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,208) |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,860)  |
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
| Total Unrealised LTCG (> 365 days)    | ₹38,040.32  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹38,040.32  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,282.58   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹155,408**, Tax savings potential: **₹21,662**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹685.30  | ₹1267.91   | ₹43,696             | LTCG/STCG | ₹5,562                |
| RELIND   |       74 | ₹1158.00 | ₹1627.08   | ₹34,712             | LTCG/STCG | ₹4,637                |
| LIC      |       45 | ₹391.45  | ₹895.05    | ₹22,662             | LTCG/STCG | ₹3,215                |
| WIPRO    |      170 | ₹184.50  | ₹304.31    | ₹20,368             | LTCG/STCG | ₹2,690                |
| ICIPSE   |      193 | ₹191.71  | ₹250.36    | ₹11,319             | STCG      | ₹2,264                |
| JSWENE   |       28 | ₹483.00  | ₹668.00    | ₹5,180              | LTCG      | ₹647                  |
| ICIGOL   |      250 | ₹121.51  | ₹138.24    | ₹4,182              | STCG      | ₹836                  |
| JIOFIN   |       28 | ₹205.15  | ₹344.38    | ₹3,899              | LTCG      | ₹487                  |
| ASHLEY   |       43 | ₹144.85  | ₹212.38    | ₹2,904              | LTCG      | ₹363                  |
| SJVLIM   |       67 | ₹50.94   | ₹86.95     | ₹2,413              | LTCG      | ₹302                  |

*Showing top 10 of 20 loss-harvest candidates.*


