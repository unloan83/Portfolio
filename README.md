# Orchestrated Multi-Agent Portfolio Audit - 2026-10-20

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-20
* **Portfolio XIRR**: **-6.92%** (Current Traded Positions Value: ₹481,699)
* **Benchmark XIRR**: **3.56%** (Simulated Benchmark Value: ₹611,347)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹18,420         | 34.84%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,745         | 32.57%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,655          | 23.57%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,322          | 16.73%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.38%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,211          | 14.44%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,106         | 12.80%  | Partial (48/80 sh)   |
| TATPOW     |          8 |            8 | ₹2,818          | 8.16%   | Full                 |
| GAIL       |         61 |           61 | ₹10,205         | 7.53%   | Full                 |
| NHPC       |         55 |           55 | ₹3,888          | 7.18%   | Full                 |
| NTPC       |         12 |           12 | ₹3,708          | 4.16%   | Full                 |
| TATGLO     |         30 |           30 | ₹28,995         | 4.10%   | Full                 |
| DRREDD     |          6 |            6 | ₹7,455          | 3.20%   | Full                 |
| JSWENE     |         54 |           54 | ₹26,039         | -1.57%  | Full                 |
| HDF250     |         24 |           24 | ₹4,201          | -1.84%  | Full                 |
| HINPET     |         14 |           14 | ₹4,879          | -3.16%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,111          | -3.54%  | Full                 |
| ONGC       |         39 |           39 | ₹8,775          | -6.04%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.90%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,829          | -9.72%  | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹88,948         | -11.37% | Partial (74/76 sh)   |
| ICINIF     |         86 |           86 | ₹22,359         | -11.58% | Full                 |
| HDFBAN     |        130 |           75 | ₹53,400         | -13.98% | Partial (75/130 sh)  |
| KOTAKBKETF |         30 |           30 | ₹1,733          | -14.49% | Full                 |
| MIR150     |        194 |          194 | ₹4,266          | -15.33% | Full                 |
| ICIGOL     |        250 |          250 | ₹31,052         | -15.74% | Full                 |
| SJVLIM     |         67 |           67 | ₹3,424          | -16.85% | Full                 |
| JIOFIN     |         53 |           28 | ₹5,992          | -18.61% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹30,964         | -21.62% | Partial (170/220 sh) |
| ICIPSE     |        193 |          193 | ₹39,824         | -26.42% | Full                 |
| LIC        |         80 |           45 | ₹17,701         | -54.96% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 14.9%    | -3.26%         | N/A             | SELL        | Exit all 130 sh (~₹92,560)       | Trend exit: month-end close ₹708.70 < 10-month average ₹793.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 14.7%    | +3.74%         | N/A             | SELL        | Exit all 76 sh (~₹91,352)        | Trend exit: month-end close ₹1187.00 < 10-month average ₹1348.24. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.5%     | -22.96%        | N/A             | SELL        | Exit all 220 sh (~₹40,071)       | Thesis invalidated: Price ₹182.14 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 6.4%     | -17.88%        | N/A             | SELL        | Exit all 193 sh (~₹39,824)       | Thesis invalidated: Price ₹206.34 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.1%     | -56.20%        | N/A             | SELL        | Exit all 80 sh (~₹31,468)        | Thesis invalidated: Price ₹393.35 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 5.0%     | -10.47%        | N/A             | SELL        | Exit all 250 sh (~₹31,052)       | Thesis invalidated: Price ₹124.21 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.9%     | +138.99%       | ₹330.97         | SELL        | Exit all 80 sh (~₹30,176)        | Trend exit: month-end close ₹388.30 < 10-month average ₹412.84. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| TATGLO     | Consumption          | 4.7%     | +20.72%        | N/A             | SELL        | Exit all 30 sh (~₹28,995)        | Trend exit: month-end close ₹949.50 < 10-month average ₹1090.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                   | INTACT          |            3 |
| JSWENE     | Power                | 4.2%     | -5.21%         | N/A             | SELL        | Exit all 54 sh (~₹26,039)        | Trend exit: month-end close ₹494.70 < 10-month average ₹520.03. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.6%     | -4.09%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 29 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.6%     | +49.58%        | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 3.0%     | +66.17%        | ₹11.05          | HOLD        | Hold                             | Pullback hold: Price ₹12.28 < 200 DMA (₹12.30) with return +66.17%; thesis remains INTACT above invalidation (₹7.02).                                                                                                                                          | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +132.74%       | ₹259.30         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +132.74%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +49.24%        | N/A             | SELL        | Exit all 106 sh (~₹15,658)       | Trend exit: month-end close ₹154.19 < 10-month average ₹169.46. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.3%     | -3.60%         | N/A             | SELL        | Exit all 46 sh (~₹14,456)        | Trend exit: month-end close ₹327.95 < 10-month average ₹338.49. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 2.0%     | -18.81%        | N/A             | SELL        | Exit all 138 sh (~₹12,100)       | Thesis invalidated: Price ₹87.68 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -7.83%         | N/A             | SELL        | Exit all 53 sh (~₹11,342)        | Trend exit: month-end close ₹216.88 < 10-month average ₹246.07. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.6%     | +7.55%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹167.30 moving sideways between 50 DMA (₹172.07) and 200 DMA (₹165.06); conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                 | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -7.61%         | N/A             | SELL        | Hold (below minimum trade)       | Trend exit: month-end close ₹225.80 < 10-month average ₹255.21. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.2%     | +4.62%         | N/A             | SELL        | Hold (below minimum trade)       | Trend exit: month-end close ₹1233.00 < 10-month average ₹1249.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | -6.32%         | N/A             | SELL        | Exit all 14 sh (~₹4,879)         | Trend exit: month-end close ₹350.35 < 10-month average ₹380.95. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -5.17%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹21.99 < 200 DMA (₹22.67) with return -5.17%; thesis remains INTACT above invalidation (₹20.41).                                                                                                                                          | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -0.60%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹175.04 moving sideways between 50 DMA (₹183.00) and 200 DMA (₹170.85); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -6.96%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return -6.96%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +21.02%        | N/A             | SELL        | Exit all 55 sh (~₹3,888)         | Trend exit: month-end close ₹72.81 < 10-month average ₹77.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +11.46%        | N/A             | SELL        | Hold (below minimum trade)       | Trend exit: month-end close ₹322.75 < 10-month average ₹353.83. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -41.65%        | N/A             | SELL        | Exit all 67 sh (~₹3,424)         | Thesis invalidated: Price ₹51.11 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +94.52%        | ₹135.92         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +94.52%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                                | INTACT          |            3 |
| TATPOW     | Power                | 0.5%     | +24.23%        | N/A             | SELL        | Exit all 8 sh (~₹2,818)          | Trend exit: month-end close ₹359.00 < 10-month average ₹382.51. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +7.94%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹34.93 moving sideways between 50 DMA (₹33.09) and 200 DMA (₹34.19); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +79.11%        | ₹208.60         | HOLD        | Hold                             | Pullback hold: Price ₹221.11 < 200 DMA (₹233.14) with return +79.11%; thesis remains INTACT above invalidation (₹117.28).                                                                                                                                      | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -3.02%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹57.77 < 200 DMA (₹58.84) with return -3.02%; thesis remains INTACT above invalidation (₹52.42).                                                                                                                                          | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹261.20 vs 200-day average ₹274.47 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 19.7%
* **Banking**: 17.9%
* **Commodities**: 11.4%
* **Power**: 8.4%
* **IT**: 6.9%
* **Insurance**: 5.1%
* **Broad Market**: 5.0%
* **Defense**: 4.9%
* **Consumption**: 4.7%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.6%
* **Telecom**: 3.0%
* **Auto**: 2.5%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 27.1%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.1%      | 25.0% | ⚠️ BREACH | TATPOW (0.5%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (2.0%), +7 more          |
| Financials        | 27.1%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (14.9%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.3%), +1 more |
| State-owned (PSU) | 19.4%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.6%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 11.4%      | 25.0% | OK        | ICIGOL (5.0%), ICIPSE (6.4%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 14.9%           | 15.42%             | +0.41% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 14.7%           | 15.04%             | +0.31% via ICINIF                        |
| WIPRO    | 6.5%            | 6.46%              | Direct only                              |
| ICIPSE   | 6.4%            | 6.42%              | Direct only                              |
| LIC      | 5.1%            | 5.07%              | Direct only                              |
| ICIGOL   | 5.0%            | 5.01%              | Direct only                              |
| BHAELE   | 4.9%            | 4.87%              | Direct only                              |
| TATGLO   | 4.7%            | 4.68%              | Direct only                              |
| JSWENE   | 4.2%            | 4.20%              | Direct only                              |
| ICINIF   | 3.6%            | 3.61%              | Direct only                              |
| LGELEC   | 3.6%            | 3.57%              | Direct only                              |
| IDECEL   | 3.0%            | 2.97%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.71%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.53%              | Direct only                              |
| TATCAP   | 2.3%            | 2.33%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹22,359 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,266  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,201  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 14.9%    | ₹92,560 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.7%    | ₹91,352 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.2%     | ₹7,455  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,708  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.5%     | ₹40,071 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.1%     | ₹31,468 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.6%     | ₹22,168 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹16,745 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,658 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.3%     | ₹14,456 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.6%     | ₹10,205 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,775  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,111  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.5%     | ₹2,818  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,655  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,733  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.4%     | ₹39,824 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹30,176 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.7%     | ₹28,995 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹26,039 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 2.0%     | ₹12,100 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,342 | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,879  | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹3,888  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,424  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,322  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 5.0%     | ₹31,052 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 3.0%     | ₹18,420 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,211  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,733)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,211)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,655)  |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.5%     |            4 | Exit all 8 sh (~₹2,818)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,322)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,424)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹3,888)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,111)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,201)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,266) |
| ENGIND     | Infrastructure | 0.8%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,879)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹38,087.58  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹38,087.58  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,414.64   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹146,232**, Tax savings potential: **₹20,318**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹712.00  | ₹1267.91   | ₹41,693             | LTCG/STCG | ₹5,272                |
| RELIND   |       72 | ₹1202.00 | ₹1639.79   | ₹31,521             | LTCG/STCG | ₹4,155                |
| LIC      |       45 | ₹393.35  | ₹895.05    | ₹22,576             | LTCG/STCG | ₹3,393                |
| WIPRO    |      170 | ₹182.14  | ₹304.31    | ₹20,769             | LTCG/STCG | ₹2,762                |
| ICIPSE   |      193 | ₹206.34  | ₹250.36    | ₹8,495              | STCG      | ₹1,699                |
| JSWENE   |       28 | ₹482.20  | ₹668.00    | ₹5,202              | LTCG      | ₹650                  |
| JIOFIN   |       28 | ₹214.00  | ₹344.38    | ₹3,651              | LTCG      | ₹456                  |
| ICIGOL   |      250 | ₹124.21  | ₹138.24    | ₹3,508              | STCG      | ₹702                  |
| ASHLEY   |       41 | ₹147.72  | ₹215.55    | ₹2,781              | LTCG      | ₹348                  |
| SJVLIM   |       67 | ₹51.11   | ₹86.95     | ₹2,401              | LTCG      | ₹300                  |

*Showing top 10 of 20 loss-harvest candidates.*


