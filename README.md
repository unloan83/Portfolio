# Orchestrated Multi-Agent Portfolio Audit - 2026-11-03

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-03
* **Portfolio XIRR**: **-5.81%** (Current Traded Positions Value: ₹492,592)
* **Benchmark XIRR**: **5.17%** (Simulated Benchmark Value: ₹635,971)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹18,390         | 33.73%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,741          | 31.19%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,020         | 30.30%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,267          | 16.13%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.01%  | Full                 |
| GAIL       |         61 |           61 | ₹11,087         | 15.32%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,194          | 14.11%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,245         | 12.90%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,367          | 11.43%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,210          | 9.12%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,852          | 8.50%   | Full                 |
| TATGLO     |         30 |           30 | ₹32,190         | 6.31%   | Full                 |
| NTPC       |         12 |           12 | ₹3,859          | 5.54%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,140         | -0.10%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,242          | -1.78%  | Full                 |
| HINPET     |         14 |           14 | ₹4,935          | -2.48%  | Full                 |
| ONGC       |         39 |           39 | ₹9,055          | -3.41%  | Full                 |
| HDF250     |         24 |           24 | ₹4,128          | -6.34%  | Full                 |
| ICINIF     |         86 |           86 | ₹22,732         | -6.45%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.74%  | Full                 |
| RELIND     |         76 |           74 | ₹96,785         | -8.00%  | Partial (74/76 sh)   |
| ASHLEY     |        106 |           53 | ₹8,095          | -8.50%  | Partial (53/106 sh)  |
| HDFBAN     |        130 |           75 | ₹54,412         | -13.40% | Partial (75/130 sh)  |
| MIR150     |        194 |          194 | ₹4,266          | -13.81% | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,725          | -13.94% | Full                 |
| SJVLIM     |         67 |           67 | ₹3,736          | -14.12% | Full                 |
| WIPRO      |        220 |          170 | ₹33,660         | -17.54% | Partial (170/220 sh) |
| JIOFIN     |         53 |           28 | ₹6,000          | -18.30% | Partial (28/53 sh)   |
| ICIGOL     |        250 |          250 | ₹29,205         | -22.42% | Full                 |
| ICIPSE     |        193 |          193 | ₹33,582         | -42.00% | Full                 |
| LIC        |         80 |           45 | ₹17,798         | -53.41% | Partial (45/80 sh)   |

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
| RELIND     | Oil & Gas            | 15.7%    | +12.88%        | N/A             | SELL        | Exit all 76 sh (~₹99,400)        | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 14.9%    | -1.43%         | N/A             | SELL        | Exit all 130 sh (~₹94,315)       | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 6.9%     | -16.25%        | N/A             | SELL        | Exit all 220 sh (~₹43,560)       | Thesis invalidated: Price ₹198.00 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 5.3%     | -30.75%        | N/A             | SELL        | Exit all 193 sh (~₹33,582)       | Thesis invalidated: Price ₹174.00 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| TATGLO     | Consumption          | 5.1%     | +34.02%        | N/A             | SELL        | Exit all 30 sh (~₹32,190)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| LIC        | Insurance            | 5.0%     | -55.96%        | N/A             | SELL        | Exit all 80 sh (~₹31,640)        | Thesis invalidated: Price ₹395.50 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| BHAELE     | Defense              | 4.8%     | +140.83%       | ₹330.97         | SELL        | Exit all 80 sh (~₹30,408)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.6%     | -15.80%        | N/A             | SELL        | Exit all 250 sh (~₹29,205)       | Thesis invalidated: Price ₹116.82 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.3%     | -1.20%         | N/A             | SELL        | Exit all 54 sh (~₹27,140)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.6%     | -2.49%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +48.27%        | N/A             | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +65.90%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹18,390)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| ASHLEY     | Auto                 | 2.6%     | +54.31%        | ₹148.26         | SELL        | Exit all 106 sh (~₹16,190)       | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| FEDBAN     | Banking              | 2.5%     | +122.66%       | ₹259.30         | HOLD        | Hold                             | Consolidation hold: Price ₹333.75 moving sideways between 50 DMA (₹337.93) and 200 DMA (₹310.78); conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                 | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | +2.39%         | N/A             | SELL        | Exit all 46 sh (~₹15,355)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.8%     | -23.73%        | N/A             | SELL        | Exit all 138 sh (~₹11,367)       | Thesis invalidated: Price ₹82.37 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -7.71%         | N/A             | SELL        | Exit all 53 sh (~₹11,356)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.8%     | +16.84%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +16.84%, position weight 1.8%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -4.66%         | N/A             | SELL        | Exit all 39 sh (~₹9,055)         | Trend exit: month-end close ₹225.39 < 10-month average ₹254.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +15.21%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹1368.30 moving sideways between 50 DMA (₹1213.18) and 200 DMA (₹1241.96); conviction (5/5) thesis INTACT above invalidation (₹1009.47).                                                                                             | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | -5.24%         | N/A             | SELL        | Exit all 14 sh (~₹4,935)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| NHPC       | Power                | 0.7%     | +35.91%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹79.40 moving sideways between 50 DMA (₹74.81) and 200 DMA (₹76.83); conviction (3/5) thesis INTACT above invalidation (₹53.75).                                                                                                     | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -5.17%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -3.99%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return -3.99%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -2.32%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |
| NTPC       | Power                | 0.6%     | +15.99%        | N/A             | SELL        | Exit all 12 sh (~₹3,859)         | Trend exit: month-end close ₹316.25 < 10-month average ₹353.10. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -36.34%        | N/A             | SELL        | Exit all 67 sh (~₹3,736)         | Thesis invalidated: Price ₹55.76 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +91.30%        | ₹135.92         | HOLD        | Hold                             | Consolidation hold: Price ₹163.33 moving sideways between 50 DMA (₹163.63) and 200 DMA (₹156.46); conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                  | INTACT          |            3 |
| TATPOW     | Power                | 0.5%     | +25.75%        | N/A             | SELL        | Exit all 8 sh (~₹2,852)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +11.46%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹36.07 moving sideways between 50 DMA (₹33.34) and 200 DMA (₹33.88); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.3%     | +77.76%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,194)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -3.46%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹270.12 vs 200-day average ₹272.81 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.8%
* **Banking**: 17.7%
* **Commodities**: 9.9%
* **Power**: 8.4%
* **IT**: 7.3%
* **Consumption**: 5.1%
* **Insurance**: 5.0%
* **Broad Market**: 4.9%
* **Defense**: 4.8%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.5%
* **Telecom**: 2.9%
* **Auto**: 2.6%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 26.9%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 29.2%      | 25.0% | ⚠️ BREACH | TATPOW (0.5%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.8%), +7 more          |
| Financials        | 26.9%      | 25.0% | ⚠️ BREACH | FEDBAN (2.5%), HDFBAN (14.9%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.3%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.8%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 9.9%       | 25.0% | OK        | ICIGOL (4.6%), ICIPSE (5.3%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| RELIND   | 15.7%           | 16.00%             | +0.31% via ICINIF                        |
| HDFBAN   | 14.9%           | 15.39%             | +0.41% via ICINIF, +0.08% via KOTAKBKETF |
| WIPRO    | 6.9%            | 6.88%              | Direct only                              |
| ICIPSE   | 5.3%            | 5.30%              | Direct only                              |
| TATGLO   | 5.1%            | 5.08%              | Direct only                              |
| LIC      | 5.0%            | 5.00%              | Direct only                              |
| BHAELE   | 4.8%            | 4.80%              | Direct only                              |
| ICIGOL   | 4.6%            | 4.61%              | Direct only                              |
| JSWENE   | 4.3%            | 4.29%              | Direct only                              |
| ICINIF   | 3.6%            | 3.59%              | Direct only                              |
| LGELEC   | 3.5%            | 3.47%              | Direct only                              |
| IDECEL   | 2.9%            | 2.90%              | Direct only                              |
| ASHLEY   | 2.6%            | 2.56%              | Direct only                              |
| FEDBAN   | 2.5%            | 2.54%              | +0.01% via KOTAKBKETF                    |
| TATCAP   | 2.4%            | 2.43%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **4.9%** (Target: 50.0%, Gap: +45.1%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.1%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹22,732 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,266  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,128  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.7%    | ₹99,400 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 14.9%    | ₹94,315 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,210  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,859  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.9%     | ₹43,560 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.0%     | ₹31,640 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹21,974 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.6%     | ₹16,190 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.5%     | ₹16,020 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹15,355 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.8%     | ₹11,087 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹9,055  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,242  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.5%     | ₹2,852  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,741  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,725  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 5.3%     | ₹33,582 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.1%     | ₹32,190 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹30,408 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.3%     | ₹27,140 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.8%     | ₹11,367 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,356 | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,935  | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,367  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,736  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,267  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.6%     | ₹29,205 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹18,390 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.3%     | ₹2,194  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,725)  |
| SEQSCI     | Pharma         | 0.3%     |            2 | Exit all 10 sh (~₹2,194)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,741)  |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.5%     |            4 | Exit all 8 sh (~₹2,852)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,267)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,736)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,128)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,242)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,266) |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,367)  |
| ENGIND     | Infrastructure | 0.8%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,935)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹44,193.43  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹44,193.43  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹2,098.28   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹142,128**, Tax savings potential: **₹19,632**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹725.50  | ₹1267.91   | ₹40,680             | LTCG/STCG | ₹5,125                |
| RELIND   |       47 | ₹1307.90 | ₹1842.64   | ₹25,133             | LTCG/STCG | ₹3,161                |
| LIC      |       45 | ₹395.50  | ₹895.05    | ₹22,480             | LTCG/STCG | ₹2,997                |
| WIPRO    |      170 | ₹198.00  | ₹304.31    | ₹18,073             | LTCG/STCG | ₹2,282                |
| ICIPSE   |      193 | ₹174.00  | ₹250.36    | ₹14,737             | STCG      | ₹2,947                |
| ICIGOL   |      250 | ₹116.82  | ₹138.24    | ₹5,355              | STCG      | ₹1,071                |
| JSWENE   |       28 | ₹502.60  | ₹668.00    | ₹4,631              | LTCG      | ₹579                  |
| JIOFIN   |       28 | ₹214.27  | ₹344.38    | ₹3,643              | LTCG      | ₹455                  |
| ASHLEY   |       39 | ₹152.74  | ₹218.80    | ₹2,576              | LTCG      | ₹322                  |
| SJVLIM   |       67 | ₹55.76   | ₹86.95     | ₹2,090              | LTCG      | ₹261                  |

*Showing top 10 of 19 loss-harvest candidates.*


