# Orchestrated Multi-Agent Portfolio Audit - 2026-10-26

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-26
* **Portfolio XIRR**: **-7.83%** (Current Traded Positions Value: ₹471,526)
* **Benchmark XIRR**: **3.28%** (Simulated Benchmark Value: ₹607,722)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| NIPNIT     |         76 |           76 | ₹2,735          | 32.48%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹17,925         | 32.09%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,531         | 31.84%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.22%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,163          | 15.37%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,079          | 12.79%  | Full                 |
| BHAELE     |         80 |           48 | ₹17,424         | 11.36%  | Partial (48/80 sh)   |
| GAIL       |         61 |           61 | ₹10,265         | 7.98%   | Full                 |
| NHPC       |         55 |           55 | ₹3,881          | 7.07%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,708          | 6.64%   | Full                 |
| DRREDD     |          6 |            6 | ₹7,865          | 6.50%   | Full                 |
| TATGLO     |         30 |           30 | ₹28,095         | 3.41%   | Full                 |
| NTPC       |         12 |           12 | ₹3,600          | 3.08%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,084          | -3.86%  | Full                 |
| HINPET     |         14 |           14 | ₹4,808          | -3.92%  | Full                 |
| JSWENE     |         54 |           54 | ₹24,281         | -3.99%  | Full                 |
| ONGC       |         39 |           39 | ₹8,909          | -4.76%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.83%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,521          | -10.98% | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹88,933         | -11.30% | Partial (74/76 sh)   |
| HDF250     |         24 |           24 | ₹4,013          | -14.29% | Full                 |
| HDFBAN     |        130 |           75 | ₹51,604         | -14.73% | Partial (75/130 sh)  |
| ICINIF     |         86 |           86 | ₹22,012         | -14.92% | Full                 |
| SJVLIM     |         67 |           67 | ₹3,283          | -17.97% | Full                 |
| ICIGOL     |        250 |          250 | ₹30,095         | -19.41% | Full                 |
| WIPRO      |        220 |          170 | ₹32,164         | -19.73% | Partial (170/220 sh) |
| JIOFIN     |         53 |           28 | ₹5,746          | -19.95% | Partial (28/53 sh)   |
| KOTAKBKETF |         30 |           30 | ₹1,696          | -21.94% | Full                 |
| MIR150     |        194 |          194 | ₹4,122          | -22.94% | Full                 |
| ICIPSE     |        193 |          193 | ₹37,166         | -33.37% | Full                 |
| LIC        |         80 |           45 | ₹17,143         | -55.76% | Partial (45/80 sh)   |

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
| RELIND     | Oil & Gas            | 15.1%    | +3.72%         | N/A             | SELL        | Exit all 76 sh (~₹91,337)       | Trend exit: month-end close ₹1187.00 < 10-month average ₹1348.24. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 14.8%    | -6.52%         | N/A             | SELL        | Exit all 130 sh (~₹89,446)      | Trend exit: month-end close ₹708.70 < 10-month average ₹793.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 6.9%     | -19.97%        | N/A             | SELL        | Exit all 220 sh (~₹41,624)      | Thesis invalidated: Price ₹189.20 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 6.1%     | -23.36%        | N/A             | SELL        | Exit all 193 sh (~₹37,166)      | Thesis invalidated: Price ₹192.57 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.0%     | -57.58%        | N/A             | SELL        | Exit all 80 sh (~₹30,476)       | Thesis invalidated: Price ₹380.95 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 5.0%     | -13.23%        | N/A             | SELL        | Exit all 250 sh (~₹30,095)      | Thesis invalidated: Price ₹120.38 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.8%     | +129.99%       | ₹330.97         | SELL        | Exit all 80 sh (~₹29,040)       | Trend exit: month-end close ₹388.30 < 10-month average ₹412.84. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| TATGLO     | Consumption          | 4.6%     | +16.97%        | N/A             | SELL        | Exit all 30 sh (~₹28,095)       | Trend exit: month-end close ₹949.50 < 10-month average ₹1090.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                   | INTACT          |            3 |
| JSWENE     | Power                | 4.0%     | -11.61%        | N/A             | SELL        | Exit all 54 sh (~₹24,281)       | Thesis invalidated: Price ₹449.65 <= invalidation price ₹468.00.                                                                                                                                                                                               | INVALIDATED     |            3 |
| ICINIF     | Broad Market         | 3.6%     | -5.58%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 33 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +42.23%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1621.40 moving sideways between 50 DMA (₹1684.14) and 200 DMA (₹1563.07); conviction (4/5) thesis INTACT above invalidation (₹1003.20).                                                                                             | INTACT          |            4 |
| IDECEL     | Telecom              | 3.0%     | +61.71%        | ₹11.05          | HOLD        | Hold                            | Pullback hold: Price ₹11.95 < 200 DMA (₹12.30) with return +61.71%; thesis remains INTACT above invalidation (₹7.02).                                                                                                                                          | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +129.77%       | ₹259.30         | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return +129.77%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +43.36%        | N/A             | SELL        | Exit all 106 sh (~₹15,041)      | Trend exit: month-end close ₹154.19 < 10-month average ₹169.46. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.3%     | -8.11%         | N/A             | SELL        | Exit all 46 sh (~₹13,779)       | Trend exit: month-end close ₹327.95 < 10-month average ₹338.49. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.9%     | -24.31%        | N/A             | SELL        | Exit all 138 sh (~₹11,280)      | Thesis invalidated: Price ₹81.74 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -11.61%        | N/A             | SELL        | Exit all 53 sh (~₹10,877)       | Thesis invalidated: Price ₹205.23 <= invalidation price ₹213.61.                                                                                                                                                                                               | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +8.18%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹168.28 moving sideways between 50 DMA (₹171.48) and 200 DMA (₹165.09); conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                 | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.5%     | -6.20%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹225.80 < 10-month average ₹255.21. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +10.38%        | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹1233.00 < 10-month average ₹1249.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| HINPET     | Oil & Gas            | 0.8%     | -7.68%         | N/A             | SELL        | Exit all 14 sh (~₹4,808)        | Trend exit: month-end close ₹350.35 < 10-month average ₹380.95. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -8.37%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹21.25 < 200 DMA (₹22.64) with return -8.37%; thesis remains INTACT above invalidation (₹20.41).                                                                                                                                          | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -7.56%         | N/A             | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return -7.56%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -5.05%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹167.20 < 200 DMA (₹170.88) with return -5.05%; thesis remains INTACT above invalidation (₹154.96).                                                                                                                                       | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +20.78%        | N/A             | SELL        | Exit all 55 sh (~₹3,881)        | Trend exit: month-end close ₹72.81 < 10-month average ₹77.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +8.21%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹322.75 < 10-month average ₹353.83. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.5%     | -44.06%        | N/A             | SELL        | Exit all 67 sh (~₹3,283)        | Thesis invalidated: Price ₹49.00 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +85.25%        | ₹135.92         | HOLD        | Hold                            | Consolidation hold: Price ₹158.17 moving sideways between 50 DMA (₹162.92) and 200 DMA (₹157.04); conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                  | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.5%     | +11.22%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹35.99 moving sideways between 50 DMA (₹33.15) and 200 DMA (₹34.07); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| TATPOW     | Power                | 0.4%     | +19.38%        | N/A             | SELL        | Exit all 8 sh (~₹2,708)         | Trend exit: month-end close ₹359.00 < 10-month average ₹382.51. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.3%     | +68.38%        | ₹208.60         | HOLD        | Hold                            | Pullback hold: Price ₹207.87 < 200 DMA (₹233.15) with return +68.38%; thesis remains INTACT above invalidation (₹117.28).                                                                                                                                      | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -5.12%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹56.52 < 200 DMA (₹58.76) with return -5.12%; thesis remains INTACT above invalidation (₹52.42).                                                                                                                                          | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹259.40 vs 200-day average ₹273.76 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.2%
* **Banking**: 17.8%
* **Commodities**: 11.1%
* **Power**: 8.1%
* **IT**: 7.3%
* **Insurance**: 5.0%
* **Broad Market**: 5.0%
* **Defense**: 4.8%
* **Consumption**: 4.6%
* **Financial Services**: 4.1%
* **Consumer Electronics**: 3.5%
* **Telecom**: 3.0%
* **Auto**: 2.5%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 26.9%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.3%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.5%), NTPGRE (1.9%), +7 more          |
| Financials        | 26.9%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (14.8%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.3%), +1 more |
| State-owned (PSU) | 19.4%      | 25.0% | OK        | ONGC (1.5%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 11.1%      | 25.0% | OK        | ICIGOL (5.0%), ICIPSE (6.1%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| RELIND   | 15.1%           | 15.41%             | +0.31% via ICINIF                        |
| HDFBAN   | 14.8%           | 15.28%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| WIPRO    | 6.9%            | 6.88%              | Direct only                              |
| ICIPSE   | 6.1%            | 6.14%              | Direct only                              |
| LIC      | 5.0%            | 5.04%              | Direct only                              |
| ICIGOL   | 5.0%            | 4.97%              | Direct only                              |
| BHAELE   | 4.8%            | 4.80%              | Direct only                              |
| TATGLO   | 4.6%            | 4.64%              | Direct only                              |
| JSWENE   | 4.0%            | 4.01%              | Direct only                              |
| ICINIF   | 3.6%            | 3.64%              | Direct only                              |
| LGELEC   | 3.5%            | 3.48%              | Direct only                              |
| IDECEL   | 3.0%            | 2.96%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.74%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.49%              | Direct only                              |
| TATCAP   | 2.3%            | 2.28%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹22,012 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,122  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,013  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.1%    | ₹91,337 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 14.8%    | ₹89,446 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹7,865  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,600  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.9%     | ₹41,624 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.0%     | ₹30,476 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹21,078 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹16,531 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,041 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.3%     | ₹13,779 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹10,265 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.5%     | ₹8,909  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,084  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.5%     | ₹2,735  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,708  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,696  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.1%     | ₹37,166 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹29,040 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.6%     | ₹28,095 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.0%     | ₹24,281 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.9%     | ₹11,280 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹10,877 | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,808  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹3,881  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.5%     | ₹3,283  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,163  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 5.0%     | ₹30,095 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 3.0%     | ₹17,925 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.3%     | ₹2,079  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,696)  |
| SEQSCI     | Pharma         | 0.3%     |            2 | Exit all 10 sh (~₹2,079)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,708)   |
| NIPNIT     | IT             | 0.5%     |            4 | Exit all 76 sh (~₹2,735)  |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,163)  |
| SJVLIM     | Power          | 0.5%     |            3 | Exit all 67 sh (~₹3,283)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹3,881)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,013)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,084)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,122) |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,808)  |
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
| Total Unrealised LTCG (> 365 days)    | ₹34,763.82  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹34,763.82  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,471.57   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹153,138**, Tax savings potential: **₹21,287**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹688.05  | ₹1267.91   | ₹43,489             | LTCG/STCG | ₹5,532                |
| RELIND   |       72 | ₹1201.80 | ₹1639.79   | ₹31,535             | LTCG/STCG | ₹4,157                |
| LIC      |       45 | ₹380.95  | ₹895.05    | ₹23,134             | LTCG/STCG | ₹3,282                |
| WIPRO    |      170 | ₹189.20  | ₹304.31    | ₹19,569             | LTCG/STCG | ₹2,548                |
| ICIPSE   |      193 | ₹192.57  | ₹250.36    | ₹11,153             | STCG      | ₹2,231                |
| JSWENE   |       28 | ₹449.65  | ₹668.00    | ₹6,114              | LTCG      | ₹764                  |
| ICIGOL   |      250 | ₹120.38  | ₹138.24    | ₹4,465              | STCG      | ₹893                  |
| JIOFIN   |       28 | ₹205.23  | ₹344.38    | ₹3,896              | LTCG      | ₹487                  |
| ASHLEY   |       43 | ₹141.90  | ₹212.38    | ₹3,031              | LTCG      | ₹379                  |
| SJVLIM   |       67 | ₹49.00   | ₹86.95     | ₹2,543              | LTCG      | ₹318                  |

*Showing top 10 of 19 loss-harvest candidates.*


