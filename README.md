# Orchestrated Multi-Agent Portfolio Audit - 2026-10-19

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-19
* **Portfolio XIRR**: **-6.70%** (Current Traded Positions Value: ₹484,203)
* **Benchmark XIRR**: **3.90%** (Simulated Benchmark Value: ₹616,170)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹18,945         | 37.40%  | Full                 |
| FEDBAN     |         48 |           48 | ₹15,658         | 29.81%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,691          | 28.56%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,363          | 17.08%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.41%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,214          | 14.48%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,122         | 12.84%  | Partial (48/80 sh)   |
| TATPOW     |          8 |            8 | ₹2,820          | 8.20%   | Full                 |
| GAIL       |         61 |           61 | ₹10,271         | 8.18%   | Full                 |
| NHPC       |         55 |           55 | ₹3,912          | 7.41%   | Full                 |
| NTPC       |         12 |           12 | ₹3,767          | 4.74%   | Full                 |
| TATGLO     |         30 |           30 | ₹29,050         | 4.14%   | Full                 |
| DRREDD     |          6 |            6 | ₹7,436          | 3.05%   | Full                 |
| HDF250     |         24 |           24 | ₹4,248          | 1.64%   | Full                 |
| JSWENE     |         54 |           54 | ₹26,074         | -1.53%  | Full                 |
| HINPET     |         14 |           14 | ₹4,866          | -3.32%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,109          | -3.58%  | Full                 |
| ONGC       |         39 |           39 | ₹8,771          | -6.09%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.91%  | Full                 |
| ICINIF     |         86 |           86 | ₹22,545         | -9.47%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,867          | -9.57%  | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹90,472         | -10.72% | Partial (74/76 sh)   |
| MIR150     |        194 |          194 | ₹4,309          | -12.75% | Full                 |
| HDFBAN     |        130 |           75 | ₹53,509         | -13.94% | Partial (75/130 sh)  |
| KOTAKBKETF |         30 |           30 | ₹1,733          | -14.76% | Full                 |
| ICIGOL     |        250 |          250 | ₹31,110         | -15.56% | Full                 |
| SJVLIM     |         67 |           67 | ₹3,450          | -16.65% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,061          | -18.23% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹31,433         | -20.96% | Partial (170/220 sh) |
| ICIPSE     |        193 |          193 | ₹39,986         | -26.04% | Full                 |
| LIC        |         80 |           45 | ₹17,737         | -54.96% | Partial (45/80 sh)   |

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
| RELIND     | Oil & Gas            | 14.9%    | +5.52%         | N/A             | SELL        | Exit all 76 sh (~₹92,918)        | Trend exit: month-end close ₹1187.00 < 10-month average ₹1348.24. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 14.9%    | -3.07%         | N/A             | SELL        | Exit all 130 sh (~₹92,749)       | Trend exit: month-end close ₹708.70 < 10-month average ₹793.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 6.5%     | -21.79%        | N/A             | SELL        | Exit all 220 sh (~₹40,678)       | Thesis invalidated: Price ₹184.90 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 6.4%     | -17.54%        | N/A             | SELL        | Exit all 193 sh (~₹39,986)       | Thesis invalidated: Price ₹207.18 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.1%     | -56.11%        | N/A             | SELL        | Exit all 80 sh (~₹31,532)        | Thesis invalidated: Price ₹394.15 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 5.0%     | -10.31%        | N/A             | SELL        | Exit all 250 sh (~₹31,110)       | Thesis invalidated: Price ₹124.44 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.8%     | +139.21%       | ₹330.97         | SELL        | Exit all 80 sh (~₹30,204)        | Trend exit: month-end close ₹388.30 < 10-month average ₹412.84. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| TATGLO     | Consumption          | 4.7%     | +20.95%        | N/A             | SELL        | Exit all 30 sh (~₹29,050)        | Trend exit: month-end close ₹949.50 < 10-month average ₹1090.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                   | INTACT          |            3 |
| JSWENE     | Power                | 4.2%     | -5.08%         | N/A             | SELL        | Exit all 54 sh (~₹26,074)        | Trend exit: month-end close ₹494.70 < 10-month average ₹520.03. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.6%     | -3.29%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 28 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.6%     | +49.74%        | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 3.0%     | +70.91%        | ₹11.05          | HOLD        | Hold                             | Consolidation hold: Price ₹12.63 moving sideways between 50 DMA (₹13.87) and 200 DMA (₹12.30); conviction (2/5) thesis INTACT above invalidation (₹7.02).                                                                                                      | INTACT          |            2 |
| ASHLEY     | Auto                 | 2.5%     | +49.97%        | N/A             | SELL        | Exit all 106 sh (~₹15,735)       | Trend exit: month-end close ₹154.19 < 10-month average ₹169.46. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| FEDBAN     | Banking              | 2.5%     | +117.63%       | ₹259.30         | HOLD        | Hold                             | Consolidation hold: Price ₹326.20 moving sideways between 50 DMA (₹340.00) and 200 DMA (₹306.61); conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                 | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.3%     | -2.48%         | N/A             | SELL        | Exit all 46 sh (~₹14,623)        | Trend exit: month-end close ₹327.95 < 10-month average ₹338.49. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 2.0%     | -17.33%        | N/A             | SELL        | Exit all 138 sh (~₹12,321)       | Thesis invalidated: Price ₹89.28 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -6.77%         | N/A             | SELL        | Exit all 53 sh (~₹11,472)        | Trend exit: month-end close ₹216.88 < 10-month average ₹246.07. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.6%     | +8.25%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹168.38 moving sideways between 50 DMA (₹172.09) and 200 DMA (₹165.07); conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                 | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -7.65%         | N/A             | SELL        | Hold (below minimum trade)       | Trend exit: month-end close ₹225.80 < 10-month average ₹255.21. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.2%     | +4.36%         | N/A             | SELL        | Hold (below minimum trade)       | Trend exit: month-end close ₹1233.00 < 10-month average ₹1249.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| HINPET     | Oil & Gas            | 0.8%     | -6.58%         | N/A             | SELL        | Exit all 14 sh (~₹4,866)         | Trend exit: month-end close ₹350.35 < 10-month average ₹380.95. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -4.23%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹22.21 < 200 DMA (₹22.67) with return -4.23%; thesis remains INTACT above invalidation (₹20.41).                                                                                                                                          | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +0.52%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹177.00 moving sideways between 50 DMA (₹183.04) and 200 DMA (₹170.86); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -7.00%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return -7.00%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +21.74%        | N/A             | SELL        | Exit all 55 sh (~₹3,912)         | Trend exit: month-end close ₹72.81 < 10-month average ₹77.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +13.23%        | N/A             | SELL        | Hold (below minimum trade)       | Trend exit: month-end close ₹322.75 < 10-month average ₹353.83. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -41.21%        | N/A             | SELL        | Exit all 67 sh (~₹3,450)         | Thesis invalidated: Price ₹51.49 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +96.97%        | ₹135.92         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +96.97%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                                | INTACT          |            3 |
| TATPOW     | Power                | 0.5%     | +24.32%        | N/A             | SELL        | Exit all 8 sh (~₹2,820)          | Trend exit: month-end close ₹359.00 < 10-month average ₹382.51. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +9.43%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹35.41 moving sideways between 50 DMA (₹33.10) and 200 DMA (₹34.19); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +79.38%        | ₹208.60         | HOLD        | Hold                             | Pullback hold: Price ₹221.45 < 200 DMA (₹233.14) with return +79.38%; thesis remains INTACT above invalidation (₹117.28).                                                                                                                                      | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -3.04%         | N/A             | HOLD        | Hold                             | Pullback hold: Price ₹57.76 < 200 DMA (₹58.84) with return -3.04%; thesis remains INTACT above invalidation (₹52.42).                                                                                                                                          | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹262.96 vs 200-day average ₹274.48 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 19.8%
* **Banking**: 17.7%
* **Commodities**: 11.4%
* **Power**: 8.4%
* **IT**: 7.0%
* **Insurance**: 5.1%
* **Broad Market**: 5.0%
* **Defense**: 4.8%
* **Consumption**: 4.7%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.6%
* **Telecom**: 3.0%
* **Auto**: 2.5%
* **Pharma**: 1.5%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 26.9%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.2%      | 25.0% | ⚠️ BREACH | TATPOW (0.5%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (2.0%), +7 more          |
| Financials        | 26.9%      | 25.0% | ⚠️ BREACH | FEDBAN (2.5%), HDFBAN (14.9%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.3%), +1 more |
| State-owned (PSU) | 19.4%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.6%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 11.4%      | 25.0% | OK        | ICIGOL (5.0%), ICIPSE (6.4%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 14.9%           | 15.37%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 14.9%           | 15.21%             | +0.31% via ICINIF                        |
| WIPRO    | 6.5%            | 6.52%              | Direct only                              |
| ICIPSE   | 6.4%            | 6.41%              | Direct only                              |
| LIC      | 5.1%            | 5.06%              | Direct only                              |
| ICIGOL   | 5.0%            | 4.99%              | Direct only                              |
| BHAELE   | 4.8%            | 4.84%              | Direct only                              |
| TATGLO   | 4.7%            | 4.66%              | Direct only                              |
| JSWENE   | 4.2%            | 4.18%              | Direct only                              |
| ICINIF   | 3.6%            | 3.62%              | Direct only                              |
| LGELEC   | 3.6%            | 3.56%              | Direct only                              |
| IDECEL   | 3.0%            | 3.04%              | Direct only                              |
| ASHLEY   | 2.5%            | 2.52%              | Direct only                              |
| FEDBAN   | 2.5%            | 2.52%              | +0.01% via KOTAKBKETF                    |
| TATCAP   | 2.3%            | 2.35%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹22,545 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,309  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,248  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.9%    | ₹92,918 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 14.9%    | ₹92,749 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.2%     | ₹7,436  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,767  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.5%     | ₹40,678 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.1%     | ₹31,532 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.6%     | ₹22,191 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,735 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.5%     | ₹15,658 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.3%     | ₹14,623 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.6%     | ₹10,271 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,771  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,109  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.5%     | ₹2,820  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,691  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,733  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.4%     | ₹39,986 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹30,204 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.7%     | ₹29,050 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.2%     | ₹26,074 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 2.0%     | ₹12,321 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,472 | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹3,912  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,450  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,363  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 5.0%     | ₹31,110 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 3.0%     | ₹18,945 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,214  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,733)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,214)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,691)  |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.5%     |            4 | Exit all 8 sh (~₹2,820)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,363)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,450)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹3,912)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,109)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,248)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,309) |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,866)  |
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
| Total Unrealised LTCG (> 365 days)    | ₹37,845.75  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹37,845.75  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,516.68   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹143,588**, Tax savings potential: **₹19,885**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹713.45  | ₹1267.91   | ₹41,584             | LTCG/STCG | ₹5,256                |
| RELIND   |       67 | ₹1222.60 | ₹1671.95   | ₹30,107             | LTCG/STCG | ₹3,940                |
| LIC      |       45 | ₹394.15  | ₹895.05    | ₹22,541             | LTCG/STCG | ₹3,388                |
| WIPRO    |      170 | ₹184.90  | ₹304.31    | ₹20,300             | LTCG/STCG | ₹2,678                |
| ICIPSE   |      193 | ₹207.18  | ₹250.36    | ₹8,333              | STCG      | ₹1,667                |
| JSWENE   |       28 | ₹482.85  | ₹668.00    | ₹5,184              | LTCG      | ₹648                  |
| JIOFIN   |       28 | ₹216.46  | ₹344.38    | ₹3,582              | LTCG      | ₹448                  |
| ICIGOL   |      250 | ₹124.44  | ₹138.24    | ₹3,450              | STCG      | ₹690                  |
| ASHLEY   |       41 | ₹148.44  | ₹215.55    | ₹2,752              | LTCG      | ₹344                  |
| SJVLIM   |       67 | ₹51.49   | ₹86.95     | ₹2,376              | LTCG      | ₹297                  |

*Showing top 10 of 19 loss-harvest candidates.*


