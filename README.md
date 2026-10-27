# Orchestrated Multi-Agent Portfolio Audit - 2026-10-27

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-27
* **Portfolio XIRR**: **-7.66%** (Current Traded Positions Value: ₹473,162)
* **Benchmark XIRR**: **3.26%** (Simulated Benchmark Value: ₹607,479)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹17,985         | 32.31%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,553         | 31.86%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,716          | 29.83%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.19%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,208          | 15.73%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,149          | 13.63%  | Full                 |
| BHAELE     |         80 |           48 | ₹17,695         | 11.89%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹3,998          | 8.17%   | Full                 |
| GAIL       |         61 |           61 | ₹10,226         | 7.59%   | Full                 |
| DRREDD     |          6 |            6 | ₹7,898          | 6.75%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,713          | 6.70%   | Full                 |
| TATGLO     |         30 |           30 | ₹29,761         | 4.64%   | Full                 |
| NTPC       |         12 |           12 | ₹3,645          | 3.52%   | Full                 |
| JSWENE     |         54 |           54 | ₹25,267         | -2.61%  | Full                 |
| HINPET     |         14 |           14 | ₹4,838          | -3.58%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,070          | -4.04%  | Full                 |
| ONGC       |         39 |           39 | ₹8,870          | -5.10%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.82%  | Full                 |
| HDF250     |         24 |           24 | ₹4,079          | -9.92%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,520          | -10.97% | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹88,267         | -11.58% | Partial (74/76 sh)   |
| ICINIF     |         86 |           86 | ₹22,012         | -14.81% | Full                 |
| HDFBAN     |        130 |           75 | ₹51,112         | -14.95% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,382          | -17.10% | Full                 |
| JIOFIN     |         53 |           28 | ₹5,803          | -19.59% | Partial (28/53 sh)   |
| ICIGOL     |        250 |          250 | ₹29,965         | -19.87% | Full                 |
| WIPRO      |        220 |          170 | ₹32,018         | -19.91% | Partial (170/220 sh) |
| MIR150     |        194 |          194 | ₹4,159          | -20.71% | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,688          | -23.23% | Full                 |
| ICIPSE     |        193 |          193 | ₹36,500         | -35.09% | Full                 |
| LIC        |         80 |           45 | ₹17,388         | -55.06% | Partial (45/80 sh)   |

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
| RELIND     | Oil & Gas            | 14.9%    | +2.94%         | N/A             | SELL        | Exit all 76 sh (~₹90,653)       | Trend exit: month-end close ₹1187.00 < 10-month average ₹1348.24. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 14.6%    | -7.41%         | N/A             | SELL        | Exit all 130 sh (~₹88,595)      | Trend exit: month-end close ₹708.70 < 10-month average ₹793.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 6.8%     | -20.33%        | N/A             | SELL        | Exit all 220 sh (~₹41,435)      | Thesis invalidated: Price ₹188.34 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 6.0%     | -24.73%        | N/A             | SELL        | Exit all 193 sh (~₹36,500)      | Thesis invalidated: Price ₹189.12 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.1%     | -56.97%        | N/A             | SELL        | Exit all 80 sh (~₹30,912)       | Thesis invalidated: Price ₹386.40 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 4.9%     | -13.61%        | N/A             | SELL        | Exit all 250 sh (~₹29,965)      | Thesis invalidated: Price ₹119.86 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| TATGLO     | Consumption          | 4.9%     | +23.91%        | N/A             | SELL        | Exit all 30 sh (~₹29,761)       | Trend exit: month-end close ₹949.50 < 10-month average ₹1090.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                   | INTACT          |            3 |
| BHAELE     | Defense              | 4.9%     | +133.57%       | ₹330.97         | SELL        | Exit all 80 sh (~₹29,492)       | Trend exit: month-end close ₹388.30 < 10-month average ₹412.84. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| JSWENE     | Power                | 4.2%     | -8.02%         | N/A             | SELL        | Exit all 54 sh (~₹25,267)       | Thesis invalidated: Price ₹467.90 <= invalidation price ₹468.00.                                                                                                                                                                                               | INVALIDATED     |            3 |
| ICINIF     | Broad Market         | 3.6%     | -5.58%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 33 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.6%     | +47.45%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1680.90 moving sideways between 50 DMA (₹1686.19) and 200 DMA (₹1564.05); conviction (4/5) thesis INTACT above invalidation (₹1003.20).                                                                                             | INTACT          |            4 |
| IDECEL     | Telecom              | 3.0%     | +62.25%        | ₹11.05          | HOLD        | Hold                            | Pullback hold: Price ₹11.99 < 200 DMA (₹12.30) with return +62.25%; thesis remains INTACT above invalidation (₹7.02).                                                                                                                                          | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +130.07%       | ₹259.30         | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return +130.07%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +43.34%        | N/A             | SELL        | Exit all 106 sh (~₹15,039)      | Trend exit: month-end close ₹154.19 < 10-month average ₹169.46. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.3%     | -8.04%         | N/A             | SELL        | Exit all 46 sh (~₹13,791)       | Trend exit: month-end close ₹327.95 < 10-month average ₹338.49. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.9%     | -23.13%        | N/A             | SELL        | Exit all 138 sh (~₹11,457)      | Thesis invalidated: Price ₹83.02 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -10.74%        | N/A             | SELL        | Exit all 53 sh (~₹10,984)       | Thesis invalidated: Price ₹207.25 <= invalidation price ₹213.61.                                                                                                                                                                                               | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +7.77%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹167.64 moving sideways between 50 DMA (₹171.33) and 200 DMA (₹165.08); conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                 | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.5%     | -6.61%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹225.80 < 10-month average ₹255.21. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +10.84%        | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹1233.00 < 10-month average ₹1249.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| HINPET     | Oil & Gas            | 0.8%     | -7.10%         | N/A             | SELL        | Exit all 14 sh (~₹4,838)        | Trend exit: month-end close ₹350.35 < 10-month average ₹380.95. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -7.55%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹21.44 < 200 DMA (₹22.64) with return -7.55%; thesis remains INTACT above invalidation (₹20.41).                                                                                                                                          | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -3.48%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹169.96 < 200 DMA (₹170.90) with return -3.48%; thesis remains INTACT above invalidation (₹154.96).                                                                                                                                       | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -7.87%         | N/A             | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return -7.87%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| NHPC       | Power                | 0.7%     | +24.44%        | N/A             | SELL        | Exit all 55 sh (~₹3,998)        | Trend exit: month-end close ₹72.81 < 10-month average ₹77.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +9.57%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹322.75 < 10-month average ₹353.83. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -42.37%        | N/A             | SELL        | Exit all 67 sh (~₹3,382)        | Thesis invalidated: Price ₹50.48 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +87.89%        | ₹135.92         | HOLD        | Hold                            | Consolidation hold: Price ₹160.42 moving sideways between 50 DMA (₹163.18) and 200 DMA (₹156.95); conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                  | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +10.44%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹35.74 moving sideways between 50 DMA (₹33.14) and 200 DMA (₹34.07); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| TATPOW     | Power                | 0.4%     | +19.61%        | N/A             | SELL        | Exit all 8 sh (~₹2,713)         | Trend exit: month-end close ₹359.00 < 10-month average ₹382.51. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +74.09%        | ₹208.60         | HOLD        | Hold                            | Pullback hold: Price ₹214.91 < 200 DMA (₹233.17) with return +74.09%; thesis remains INTACT above invalidation (₹117.28).                                                                                                                                      | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -5.52%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹56.28 < 200 DMA (₹58.76) with return -5.52%; thesis remains INTACT above invalidation (₹52.42).                                                                                                                                          | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹259.31 vs 200-day average ₹273.76 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.0%
* **Banking**: 17.6%
* **Commodities**: 10.9%
* **Power**: 8.3%
* **IT**: 7.3%
* **Insurance**: 5.1%
* **Broad Market**: 5.0%
* **Consumption**: 4.9%
* **Defense**: 4.9%
* **Financial Services**: 4.1%
* **Consumer Electronics**: 3.6%
* **Telecom**: 3.0%
* **Auto**: 2.5%
* **Pharma**: 1.7%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 26.7%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.3%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.9%), +7 more          |
| Financials        | 26.7%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (14.6%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.3%), +1 more |
| State-owned (PSU) | 19.5%      | 25.0% | OK        | ONGC (1.5%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 10.9%      | 25.0% | OK        | ICIGOL (4.9%), ICIPSE (6.0%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| RELIND   | 14.9%           | 15.23%             | +0.31% via ICINIF                        |
| HDFBAN   | 14.6%           | 15.08%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| WIPRO    | 6.8%            | 6.82%              | Direct only                              |
| ICIPSE   | 6.0%            | 6.01%              | Direct only                              |
| LIC      | 5.1%            | 5.09%              | Direct only                              |
| ICIGOL   | 4.9%            | 4.93%              | Direct only                              |
| TATGLO   | 4.9%            | 4.90%              | Direct only                              |
| BHAELE   | 4.9%            | 4.85%              | Direct only                              |
| JSWENE   | 4.2%            | 4.16%              | Direct only                              |
| ICINIF   | 3.6%            | 3.62%              | Direct only                              |
| LGELEC   | 3.6%            | 3.60%              | Direct only                              |
| IDECEL   | 3.0%            | 2.96%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.73%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.48%              | Direct only                              |
| TATCAP   | 2.3%            | 2.27%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹22,012 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,159  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,079  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.9%    | ₹90,653 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 14.6%    | ₹88,595 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹7,898  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,645  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.8%     | ₹41,435 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.1%     | ₹30,912 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.6%     | ₹21,852 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹16,553 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,039 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.3%     | ₹13,791 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹10,226 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.5%     | ₹8,870  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,070  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,716  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,713  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,688  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.0%     | ₹36,500 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.9%     | ₹29,761 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹29,492 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹25,267 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.9%     | ₹11,457 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹10,984 | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,838  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹3,998  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,382  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,208  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.9%     | ₹29,965 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 3.0%     | ₹17,985 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,149  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,688)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,149)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,713)   |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,716)  |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,208)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,382)  |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹3,998)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,070)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,079)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,159) |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,838)  |
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
| Total Unrealised LTCG (> 365 days)    | ₹37,556.48  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹37,556.48  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,443.26   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹154,266**, Tax savings potential: **₹21,514**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹681.50  | ₹1267.91   | ₹43,980             | LTCG/STCG | ₹5,603                |
| RELIND   |       72 | ₹1192.80 | ₹1639.79   | ₹32,183             | LTCG/STCG | ₹4,255                |
| LIC      |       45 | ₹386.40  | ₹895.05    | ₹22,889             | LTCG/STCG | ₹3,247                |
| WIPRO    |      170 | ₹188.34  | ₹304.31    | ₹19,715             | LTCG/STCG | ₹2,574                |
| ICIPSE   |      193 | ₹189.12  | ₹250.36    | ₹11,818             | STCG      | ₹2,364                |
| JSWENE   |       28 | ₹467.90  | ₹668.00    | ₹5,603              | LTCG      | ₹700                  |
| ICIGOL   |      250 | ₹119.86  | ₹138.24    | ₹4,595              | STCG      | ₹919                  |
| JIOFIN   |       28 | ₹207.25  | ₹344.38    | ₹3,840              | LTCG      | ₹480                  |
| ASHLEY   |       43 | ₹141.88  | ₹212.38    | ₹3,031              | LTCG      | ₹379                  |
| SJVLIM   |       67 | ₹50.48   | ₹86.95     | ₹2,443              | LTCG      | ₹305                  |

*Showing top 10 of 19 loss-harvest candidates.*


