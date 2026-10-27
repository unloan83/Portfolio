# Orchestrated Multi-Agent Portfolio Audit - 2026-10-27

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-27
* **Portfolio XIRR**: **-7.59%** (Current Traded Positions Value: ₹473,864)
* **Benchmark XIRR**: **3.27%** (Simulated Benchmark Value: ₹607,630)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹18,165         | 33.15%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,397         | 31.47%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,710          | 29.07%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.19%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,205          | 15.70%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,149          | 13.63%  | Full                 |
| BHAELE     |         80 |           48 | ₹17,662         | 11.83%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,026          | 8.43%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,713          | 6.70%   | Full                 |
| GAIL       |         61 |           61 | ₹10,106         | 6.46%   | Full                 |
| DRREDD     |          6 |            6 | ₹7,860          | 6.45%   | Full                 |
| TATGLO     |         30 |           30 | ₹30,000         | 4.81%   | Full                 |
| NTPC       |         12 |           12 | ₹3,622          | 3.29%   | Full                 |
| HINPET     |         14 |           14 | ₹4,956          | -2.28%  | Full                 |
| JSWENE     |         54 |           54 | ₹25,361         | -2.48%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,144          | -3.07%  | Full                 |
| ONGC       |         39 |           39 | ₹8,964          | -4.26%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.82%  | Full                 |
| HDF250     |         24 |           24 | ₹4,098          | -8.69%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,526          | -10.95% | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹88,519         | -11.47% | Partial (74/76 sh)   |
| ICINIF     |         86 |           86 | ₹22,202         | -12.74% | Full                 |
| HDFBAN     |        130 |           75 | ₹51,015         | -14.99% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,400          | -16.95% | Full                 |
| JIOFIN     |         53 |           28 | ₹5,803          | -19.59% | Partial (28/53 sh)   |
| ICIGOL     |        250 |          250 | ₹29,960         | -19.89% | Full                 |
| WIPRO      |        220 |          170 | ₹31,790         | -20.23% | Partial (170/220 sh) |
| MIR150     |        194 |          194 | ₹4,161          | -20.60% | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,688          | -23.23% | Full                 |
| ICIPSE     |        193 |          193 | ₹36,543         | -34.97% | Full                 |
| LIC        |         80 |           45 | ₹17,447         | -54.92% | Partial (45/80 sh)   |

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
| RELIND     | Oil & Gas            | 14.9%    | +3.24%         | N/A             | SELL        | Exit all 76 sh (~₹90,911)       | Trend exit: month-end close ₹1187.00 < 10-month average ₹1348.24. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 14.5%    | -7.58%         | N/A             | SELL        | Exit all 130 sh (~₹88,426)      | Trend exit: month-end close ₹708.70 < 10-month average ₹793.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 6.8%     | -20.90%        | N/A             | SELL        | Exit all 220 sh (~₹41,140)      | Thesis invalidated: Price ₹187.00 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 6.0%     | -24.64%        | N/A             | SELL        | Exit all 193 sh (~₹36,543)      | Thesis invalidated: Price ₹189.34 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.1%     | -56.83%        | N/A             | SELL        | Exit all 80 sh (~₹31,016)       | Thesis invalidated: Price ₹387.70 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 4.9%     | +24.90%        | N/A             | SELL        | Exit all 30 sh (~₹30,000)       | Trend exit: month-end close ₹949.50 < 10-month average ₹1090.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                   | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.9%     | -13.62%        | N/A             | SELL        | Exit all 250 sh (~₹29,960)      | Thesis invalidated: Price ₹119.84 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.8%     | +133.13%       | ₹330.97         | SELL        | Exit all 80 sh (~₹29,436)       | Trend exit: month-end close ₹388.30 < 10-month average ₹412.84. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| JSWENE     | Power                | 4.2%     | -7.68%         | N/A             | SELL        | Exit all 54 sh (~₹25,361)       | Trend exit: month-end close ₹494.70 < 10-month average ₹520.03. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.7%     | -4.77%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 34 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.6%     | +47.18%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1677.80 moving sideways between 50 DMA (₹1686.13) and 200 DMA (₹1564.04); conviction (4/5) thesis INTACT above invalidation (₹1003.20).                                                                                             | INTACT          |            4 |
| IDECEL     | Telecom              | 3.0%     | +63.87%        | ₹11.05          | HOLD        | Hold                            | Pullback hold: Price ₹12.11 < 200 DMA (₹12.30) with return +63.87%; thesis remains INTACT above invalidation (₹7.02).                                                                                                                                          | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +127.90%       | ₹259.30         | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return +127.90%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +43.46%        | N/A             | SELL        | Exit all 106 sh (~₹15,052)      | Trend exit: month-end close ₹154.19 < 10-month average ₹169.46. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.3%     | -7.84%         | N/A             | SELL        | Exit all 46 sh (~₹13,821)       | Trend exit: month-end close ₹327.95 < 10-month average ₹338.49. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.9%     | -23.03%        | N/A             | SELL        | Exit all 138 sh (~₹11,472)      | Thesis invalidated: Price ₹83.13 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -10.74%        | N/A             | SELL        | Exit all 53 sh (~₹10,984)       | Thesis invalidated: Price ₹207.24 <= invalidation price ₹213.61.                                                                                                                                                                                               | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +6.51%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹165.68 moving sideways between 50 DMA (₹171.29) and 200 DMA (₹165.07); conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                 | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.5%     | -5.62%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹225.80 < 10-month average ₹255.21. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +10.31%        | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹1233.00 < 10-month average ₹1249.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | -4.84%         | N/A             | SELL        | Exit all 14 sh (~₹4,956)        | Trend exit: month-end close ₹350.35 < 10-month average ₹380.95. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -7.50%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹21.45 < 200 DMA (₹22.64) with return -7.50%; thesis remains INTACT above invalidation (₹20.41).                                                                                                                                          | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -6.21%         | N/A             | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return -6.21%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -3.04%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹170.74 < 200 DMA (₹170.90) with return -3.04%; thesis remains INTACT above invalidation (₹154.96).                                                                                                                                       | INTACT          |            4 |
| NHPC       | Power                | 0.7%     | +25.30%        | N/A             | SELL        | Exit all 55 sh (~₹4,026)        | Trend exit: month-end close ₹72.81 < 10-month average ₹77.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +8.86%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹322.75 < 10-month average ₹353.83. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -42.06%        | N/A             | SELL        | Exit all 67 sh (~₹3,400)        | Thesis invalidated: Price ₹50.75 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +87.68%        | ₹135.92         | HOLD        | Hold                            | Consolidation hold: Price ₹160.24 moving sideways between 50 DMA (₹163.18) and 200 DMA (₹156.95); conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                  | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.4%     | +19.60%        | N/A             | SELL        | Exit all 8 sh (~₹2,713)         | Trend exit: month-end close ₹359.00 < 10-month average ₹382.51. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +10.20%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹35.66 moving sideways between 50 DMA (₹33.17) and 200 DMA (₹34.03); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +74.05%        | ₹208.60         | HOLD        | Hold                            | Pullback hold: Price ₹214.87 < 200 DMA (₹233.17) with return +74.05%; thesis remains INTACT above invalidation (₹117.28).                                                                                                                                      | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -5.52%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹56.28 < 200 DMA (₹58.74) with return -5.52%; thesis remains INTACT above invalidation (₹52.42).                                                                                                                                          | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹259.49 vs 200-day average ₹273.57 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.0%
* **Banking**: 17.5%
* **Commodities**: 10.9%
* **Power**: 8.3%
* **IT**: 7.2%
* **Insurance**: 5.1%
* **Broad Market**: 5.0%
* **Consumption**: 4.9%
* **Defense**: 4.8%
* **Financial Services**: 4.1%
* **Consumer Electronics**: 3.6%
* **Telecom**: 3.0%
* **Auto**: 2.5%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 26.7%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.4%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.9%), +7 more          |
| Financials        | 26.7%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (14.5%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.3%), +1 more |
| State-owned (PSU) | 19.5%      | 25.0% | OK        | ONGC (1.5%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 10.9%      | 25.0% | OK        | ICIGOL (4.9%), ICIPSE (6.0%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| RELIND   | 14.9%           | 15.26%             | +0.31% via ICINIF                        |
| HDFBAN   | 14.5%           | 15.04%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| WIPRO    | 6.8%            | 6.76%              | Direct only                              |
| ICIPSE   | 6.0%            | 6.01%              | Direct only                              |
| LIC      | 5.1%            | 5.10%              | Direct only                              |
| TATGLO   | 4.9%            | 4.93%              | Direct only                              |
| ICIGOL   | 4.9%            | 4.93%              | Direct only                              |
| BHAELE   | 4.8%            | 4.84%              | Direct only                              |
| JSWENE   | 4.2%            | 4.17%              | Direct only                              |
| ICINIF   | 3.7%            | 3.65%              | Direct only                              |
| LGELEC   | 3.6%            | 3.59%              | Direct only                              |
| IDECEL   | 3.0%            | 2.99%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.70%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.47%              | Direct only                              |
| TATCAP   | 2.3%            | 2.27%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.7%     | ₹22,202 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,161  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,098  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.9%    | ₹90,911 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 14.5%    | ₹88,426 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹7,860  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,622  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.8%     | ₹41,140 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.1%     | ₹31,016 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.6%     | ₹21,811 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹16,397 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,052 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.3%     | ₹13,821 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹10,106 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.5%     | ₹8,964  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,144  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,713  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,710  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,688  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.0%     | ₹36,543 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.9%     | ₹30,000 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹29,436 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹25,361 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.9%     | ₹11,472 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹10,984 | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,956  | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,026  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,400  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,205  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.9%     | ₹29,960 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 3.0%     | ₹18,165 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,149  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,688)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,149)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,710)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,713)   |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,205)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,400)  |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,026)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,098)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,144)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,161) |
| ENGIND     | Infrastructure | 0.8%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,956)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹37,849.78  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹37,849.78  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,365.02   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹153,779**, Tax savings potential: **₹21,437**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹680.20  | ₹1267.91   | ₹44,078             | LTCG/STCG | ₹5,618                |
| RELIND   |       72 | ₹1196.20 | ₹1639.79   | ₹31,939             | LTCG/STCG | ₹4,218                |
| LIC      |       45 | ₹387.70  | ₹895.05    | ₹22,831             | LTCG/STCG | ₹3,239                |
| WIPRO    |      170 | ₹187.00  | ₹304.31    | ₹19,943             | LTCG/STCG | ₹2,615                |
| ICIPSE   |      193 | ₹189.34  | ₹250.36    | ₹11,776             | STCG      | ₹2,355                |
| JSWENE   |       28 | ₹469.65  | ₹668.00    | ₹5,554              | LTCG      | ₹694                  |
| ICIGOL   |      250 | ₹119.84  | ₹138.24    | ₹4,600              | STCG      | ₹920                  |
| JIOFIN   |       28 | ₹207.24  | ₹344.38    | ₹3,840              | LTCG      | ₹480                  |
| ASHLEY   |       43 | ₹142.00  | ₹212.38    | ₹3,026              | LTCG      | ₹378                  |
| SJVLIM   |       67 | ₹50.75   | ₹86.95     | ₹2,425              | LTCG      | ₹303                  |

*Showing top 10 of 19 loss-harvest candidates.*


