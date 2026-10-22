# Orchestrated Multi-Agent Portfolio Audit - 2026-10-22

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-22
* **Portfolio XIRR**: **-7.64%** (Current Traded Positions Value: ₹473,934)
* **Benchmark XIRR**: **3.05%** (Simulated Benchmark Value: ₹604,298)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| FEDBAN     |         48 |           48 | ₹16,718         | 32.44%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹17,310         | 29.40%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,702          | 29.21%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.33%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,208          | 15.78%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,099          | 13.07%  | Full                 |
| BHAELE     |         80 |           48 | ₹17,472         | 11.50%  | Partial (48/80 sh)   |
| TATPOW     |          8 |            8 | ₹2,810          | 8.04%   | Full                 |
| NHPC       |         55 |           55 | ₹3,967          | 7.91%   | Full                 |
| GAIL       |         61 |           61 | ₹10,165         | 7.10%   | Full                 |
| TATGLO     |         30 |           30 | ₹28,611         | 3.81%   | Full                 |
| NTPC       |         12 |           12 | ₹3,607          | 3.17%   | Full                 |
| DRREDD     |          6 |            6 | ₹7,402          | 2.76%   | Full                 |
| JSWENE     |         54 |           54 | ₹25,061         | -2.91%  | Full                 |
| HINPET     |         14 |           14 | ₹4,799          | -4.05%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,072          | -4.05%  | Full                 |
| ONGC       |         39 |           39 | ₹8,783          | -5.94%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.88%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,737          | -10.09% | Partial (53/106 sh)  |
| HDF250     |         24 |           24 | ₹4,075          | -10.56% | Full                 |
| ICINIF     |         86 |           86 | ₹22,359         | -11.41% | Full                 |
| RELIND     |         76 |           74 | ₹87,971         | -11.77% | Partial (74/76 sh)   |
| HDFBAN     |        130 |           75 | ₹51,975         | -14.60% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,247          | -18.34% | Full                 |
| ICIGOL     |        250 |          250 | ₹30,397         | -18.42% | Full                 |
| JIOFIN     |         53 |           28 | ₹5,886          | -19.20% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹32,293         | -19.66% | Partial (170/220 sh) |
| KOTAKBKETF |         30 |           30 | ₹1,708          | -20.24% | Full                 |
| MIR150     |        194 |          194 | ₹4,171          | -20.80% | Full                 |
| ICIPSE     |        193 |          193 | ₹38,278         | -30.69% | Full                 |
| LIC        |         80 |           45 | ₹17,375         | -55.57% | Partial (45/80 sh)   |

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
| RELIND     | Oil & Gas            | 14.8%    | +2.60%         | N/A             | SELL        | Exit all 76 sh (~₹90,349)       | Trend exit: month-end close ₹1187.00 < 10-month average ₹1348.24. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 14.8%    | -5.84%         | N/A             | SELL        | Exit all 130 sh (~₹90,090)      | Trend exit: month-end close ₹708.70 < 10-month average ₹793.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 6.9%     | -19.65%        | N/A             | SELL        | Exit all 220 sh (~₹41,791)      | Thesis invalidated: Price ₹189.96 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 6.3%     | -21.07%        | N/A             | SELL        | Exit all 193 sh (~₹38,278)      | Thesis invalidated: Price ₹198.33 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.1%     | -57.00%        | N/A             | SELL        | Exit all 80 sh (~₹30,888)       | Thesis invalidated: Price ₹386.10 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 5.0%     | -12.36%        | N/A             | SELL        | Exit all 250 sh (~₹30,397)      | Thesis invalidated: Price ₹121.59 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.8%     | +130.63%       | ₹330.97         | SELL        | Exit all 80 sh (~₹29,120)       | Trend exit: month-end close ₹388.30 < 10-month average ₹412.84. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| TATGLO     | Consumption          | 4.7%     | +19.12%        | N/A             | SELL        | Exit all 30 sh (~₹28,611)       | Trend exit: month-end close ₹949.50 < 10-month average ₹1090.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                   | INTACT          |            3 |
| JSWENE     | Power                | 4.1%     | -8.77%         | N/A             | SELL        | Exit all 54 sh (~₹25,061)       | Trend exit: month-end close ₹494.70 < 10-month average ₹520.03. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INVALIDATED     |            3 |
| ICINIF     | Broad Market         | 3.7%     | -4.09%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 30 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +44.68%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1649.30 moving sideways between 50 DMA (₹1682.37) and 200 DMA (₹1561.93); conviction (4/5) thesis INTACT above invalidation (₹1003.20).                                                                                             | INTACT          |            4 |
| IDECEL     | Telecom              | 2.8%     | +56.16%        | ₹11.05          | HOLD        | Hold                            | Pullback hold: Price ₹11.54 < 200 DMA (₹12.30) with return +56.16%; thesis remains INTACT above invalidation (₹7.02).                                                                                                                                          | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +132.37%       | ₹259.30         | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return +132.37%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +47.49%        | N/A             | SELL        | Exit all 106 sh (~₹15,475)      | Trend exit: month-end close ₹154.19 < 10-month average ₹169.46. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.3%     | -5.14%         | N/A             | SELL        | Exit all 46 sh (~₹14,226)       | Trend exit: month-end close ₹327.95 < 10-month average ₹338.49. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.9%     | -21.68%        | N/A             | SELL        | Exit all 138 sh (~₹11,673)      | Thesis invalidated: Price ₹84.59 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -9.47%         | N/A             | SELL        | Exit all 53 sh (~₹11,141)       | Trend exit: month-end close ₹216.88 < 10-month average ₹246.07. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +7.13%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹166.64 moving sideways between 50 DMA (₹171.85) and 200 DMA (₹165.08); conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                 | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -7.53%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹225.80 < 10-month average ₹255.21. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.2%     | +3.88%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹1233.00 < 10-month average ₹1249.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| HINPET     | Oil & Gas            | 0.8%     | -7.85%         | N/A             | SELL        | Exit all 14 sh (~₹4,799)        | Trend exit: month-end close ₹350.35 < 10-month average ₹380.95. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -7.29%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹21.50 < 200 DMA (₹22.66) with return -7.29%; thesis remains INTACT above invalidation (₹20.41).                                                                                                                                          | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -3.57%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹169.81 < 200 DMA (₹170.86) with return -3.57%; thesis remains INTACT above invalidation (₹154.96).                                                                                                                                       | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -7.84%         | N/A             | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return -7.84%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| NHPC       | Power                | 0.7%     | +23.47%        | N/A             | SELL        | Exit all 55 sh (~₹3,967)        | Trend exit: month-end close ₹72.81 < 10-month average ₹77.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +8.43%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹322.75 < 10-month average ₹353.83. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.5%     | -44.66%        | N/A             | SELL        | Exit all 67 sh (~₹3,247)        | Thesis invalidated: Price ₹48.47 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +87.87%        | ₹135.92         | HOLD        | Hold                            | Consolidation hold: Price ₹160.40 moving sideways between 50 DMA (₹162.39) and 200 DMA (₹157.22); conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                  | INTACT          |            3 |
| TATPOW     | Power                | 0.5%     | +23.88%        | N/A             | SELL        | Exit all 8 sh (~₹2,810)         | Trend exit: month-end close ₹359.00 < 10-month average ₹382.51. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +9.86%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹35.55 moving sideways between 50 DMA (₹33.10) and 200 DMA (₹34.16); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.3%     | +70.02%        | ₹208.60         | HOLD        | Hold                            | Pullback hold: Price ₹209.89 < 200 DMA (₹233.18) with return +70.02%; thesis remains INTACT above invalidation (₹117.28).                                                                                                                                      | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -4.45%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹56.92 < 200 DMA (₹58.83) with return -4.45%; thesis remains INTACT above invalidation (₹52.42).                                                                                                                                          | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹258.53 vs 200-day average ₹274.29 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 19.9%
* **Banking**: 17.8%
* **Commodities**: 11.3%
* **Power**: 8.3%
* **IT**: 7.3%
* **Insurance**: 5.1%
* **Broad Market**: 5.0%
* **Defense**: 4.8%
* **Consumption**: 4.7%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.5%
* **Telecom**: 2.8%
* **Auto**: 2.5%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 27.0%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.1%      | 25.0% | ⚠️ BREACH | TATPOW (0.5%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.5%), NTPGRE (1.9%), +7 more          |
| Financials        | 27.0%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (14.8%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.3%), +1 more |
| State-owned (PSU) | 19.4%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 11.3%      | 25.0% | OK        | ICIGOL (5.0%), ICIPSE (6.3%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 14.8%           | 15.29%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 14.8%           | 15.14%             | +0.31% via ICINIF                        |
| WIPRO    | 6.9%            | 6.86%              | Direct only                              |
| ICIPSE   | 6.3%            | 6.28%              | Direct only                              |
| LIC      | 5.1%            | 5.07%              | Direct only                              |
| ICIGOL   | 5.0%            | 4.99%              | Direct only                              |
| BHAELE   | 4.8%            | 4.78%              | Direct only                              |
| TATGLO   | 4.7%            | 4.69%              | Direct only                              |
| JSWENE   | 4.1%            | 4.11%              | Direct only                              |
| ICINIF   | 3.7%            | 3.67%              | Direct only                              |
| LGELEC   | 3.5%            | 3.52%              | Direct only                              |
| IDECEL   | 2.8%            | 2.84%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.75%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.54%              | Direct only                              |
| TATCAP   | 2.3%            | 2.33%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.7%     | ₹22,359 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,171  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,075  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.8%    | ₹90,349 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 14.8%    | ₹90,090 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.2%     | ₹7,402  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,607  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.9%     | ₹41,791 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.1%     | ₹30,888 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹21,441 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹16,718 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,475 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.3%     | ₹14,226 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹10,165 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,783  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,072  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.5%     | ₹2,810  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,702  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,708  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.3%     | ₹38,278 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹29,120 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.7%     | ₹28,611 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.1%     | ₹25,061 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.9%     | ₹11,673 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,141 | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,799  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹3,967  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.5%     | ₹3,247  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,208  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 5.0%     | ₹30,397 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.8%     | ₹17,310 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.3%     | ₹2,099  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,708)  |
| SEQSCI     | Pharma         | 0.3%     |            2 | Exit all 10 sh (~₹2,099)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,702)  |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.5%     |            4 | Exit all 8 sh (~₹2,810)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,208)  |
| SJVLIM     | Power          | 0.5%     |            3 | Exit all 67 sh (~₹3,247)  |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹3,967)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,072)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,075)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,171) |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,799)  |
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
| Total Unrealised LTCG (> 365 days)    | ₹35,071.73  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹35,071.73  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,387.62   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹150,954**, Tax savings potential: **₹21,079**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹693.00  | ₹1267.91   | ₹43,118             | LTCG/STCG | ₹5,478                |
| RELIND   |       72 | ₹1188.80 | ₹1639.79   | ₹32,471             | LTCG/STCG | ₹4,299                |
| LIC      |       45 | ₹386.10  | ₹895.05    | ₹22,903             | LTCG/STCG | ₹3,442                |
| WIPRO    |      170 | ₹189.96  | ₹304.31    | ₹19,440             | LTCG/STCG | ₹2,525                |
| ICIPSE   |      193 | ₹198.33  | ₹250.36    | ₹10,041             | STCG      | ₹2,008                |
| JSWENE   |       28 | ₹464.10  | ₹668.00    | ₹5,709              | LTCG      | ₹714                  |
| ICIGOL   |      250 | ₹121.59  | ₹138.24    | ₹4,163              | STCG      | ₹833                  |
| JIOFIN   |       28 | ₹210.20  | ₹344.38    | ₹3,757              | LTCG      | ₹470                  |
| ASHLEY   |       43 | ₹145.99  | ₹212.38    | ₹2,855              | LTCG      | ₹357                  |
| SJVLIM   |       67 | ₹48.47   | ₹86.95     | ₹2,578              | LTCG      | ₹322                  |

*Showing top 10 of 19 loss-harvest candidates.*


