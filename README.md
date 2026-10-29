# Orchestrated Multi-Agent Portfolio Audit - 2026-10-29

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-29
* **Portfolio XIRR**: **-7.32%** (Current Traded Positions Value: ₹476,541)
* **Benchmark XIRR**: **3.61%** (Simulated Benchmark Value: ₹612,624)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹18,180         | 33.09%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,692         | 32.15%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,695          | 26.75%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.14%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,251          | 16.06%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,246          | 14.75%  | Full                 |
| BHAELE     |         80 |           48 | ₹17,760         | 12.00%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,246          | 10.41%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,070          | 8.09%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,756          | 7.27%   | Full                 |
| GAIL       |         61 |           61 | ₹10,075         | 6.13%   | Full                 |
| TATGLO     |         30 |           30 | ₹30,630         | 5.25%   | Full                 |
| NTPC       |         12 |           12 | ₹3,726          | 4.30%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,540         | 0.41%   | Full                 |
| HINPET     |         14 |           14 | ₹4,792          | -4.08%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,048          | -4.32%  | Full                 |
| ONGC       |         39 |           39 | ₹8,806          | -5.64%  | Full                 |
| HDF250     |         24 |           24 | ₹4,141          | -5.72%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.80%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,685          | -10.25% | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹86,388         | -12.38% | Partial (74/76 sh)   |
| ICINIF     |         86 |           86 | ₹22,158         | -13.03% | Full                 |
| HDFBAN     |        130 |           75 | ₹51,247         | -14.86% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,511          | -16.00% | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,717          | -16.61% | Full                 |
| MIR150     |        194 |          194 | ₹4,218          | -17.12% | Full                 |
| ICIGOL     |        250 |          250 | ₹30,118         | -19.09% | Full                 |
| WIPRO      |        220 |          170 | ₹32,317         | -19.44% | Partial (170/220 sh) |
| JIOFIN     |         53 |           28 | ₹5,796          | -19.59% | Partial (28/53 sh)   |
| ICIPSE     |        193 |          193 | ₹36,240         | -35.57% | Full                 |
| LIC        |         80 |           45 | ₹17,820         | -53.81% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 14.5%    | -7.16%         | N/A             | SELL        | Exit all 130 sh (~₹88,829)      | Trend exit: month-end close ₹708.70 < 10-month average ₹793.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 14.5%    | +0.75%         | N/A             | SELL        | Exit all 76 sh (~₹88,722)       | Trend exit: month-end close ₹1187.00 < 10-month average ₹1348.24. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.8%     | -19.59%        | N/A             | SELL        | Exit all 220 sh (~₹41,822)      | Thesis invalidated: Price ₹190.10 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 5.9%     | -25.27%        | N/A             | SELL        | Exit all 193 sh (~₹36,240)      | Thesis invalidated: Price ₹187.77 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.2%     | -55.90%        | N/A             | SELL        | Exit all 80 sh (~₹31,680)       | Thesis invalidated: Price ₹396.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.0%     | +27.53%        | N/A             | SELL        | Exit all 30 sh (~₹30,630)       | Trend exit: month-end close ₹949.50 < 10-month average ₹1090.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                   | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.9%     | -13.17%        | N/A             | SELL        | Exit all 250 sh (~₹30,118)      | Thesis invalidated: Price ₹120.47 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.8%     | +134.43%       | ₹330.97         | SELL        | Exit all 80 sh (~₹29,600)       | Trend exit: month-end close ₹388.30 < 10-month average ₹412.84. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| JSWENE     | Power                | 4.5%     | +0.26%         | N/A             | SELL        | Exit all 54 sh (~₹27,540)       | Trend exit: month-end close ₹494.70 < 10-month average ₹520.03. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.6%     | -4.95%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 36 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.6%     | +47.51%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1681.60 moving sideways between 50 DMA (₹1685.63) and 200 DMA (₹1566.08); conviction (4/5) thesis INTACT above invalidation (₹1003.20).                                                                                             | INTACT          |            4 |
| IDECEL     | Telecom              | 3.0%     | +64.01%        | ₹11.05          | HOLD        | Hold                            | Pullback hold: Price ₹12.12 < 200 DMA (₹12.31) with return +64.01%; thesis remains INTACT above invalidation (₹7.02).                                                                                                                                          | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +132.00%       | ₹259.30         | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return +132.00%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +46.49%        | N/A             | SELL        | Exit all 106 sh (~₹15,370)      | Trend exit: month-end close ₹154.19 < 10-month average ₹169.46. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | +0.11%         | N/A             | SELL        | Exit all 46 sh (~₹15,012)       | Trend exit: month-end close ₹327.95 < 10-month average ₹338.49. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.9%     | -22.29%        | N/A             | SELL        | Exit all 138 sh (~₹11,582)      | Thesis invalidated: Price ₹83.93 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -10.85%        | N/A             | SELL        | Exit all 53 sh (~₹10,971)       | Thesis invalidated: Price ₹207.00 <= invalidation price ₹213.61.                                                                                                                                                                                               | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.6%     | +6.18%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹165.17 moving sideways between 50 DMA (₹170.97) and 200 DMA (₹165.07); conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                 | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -7.28%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹225.80 < 10-month average ₹255.21. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +13.25%        | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹1233.00 < 10-month average ₹1249.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| HINPET     | Oil & Gas            | 0.8%     | -7.99%         | N/A             | SELL        | Exit all 14 sh (~₹4,792)        | Trend exit: month-end close ₹350.35 < 10-month average ₹380.95. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| NHPC       | Power                | 0.7%     | +32.15%        | N/A             | SELL        | Exit all 55 sh (~₹4,246)        | Trend exit: month-end close ₹72.81 < 10-month average ₹77.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -6.25%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹21.74 < 200 DMA (₹22.62) with return -6.25%; thesis remains INTACT above invalidation (₹20.41).                                                                                                                                          | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -2.01%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹172.55 moving sideways between 50 DMA (₹180.88) and 200 DMA (₹170.93); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -8.38%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹289.15 moving sideways between 50 DMA (₹289.68) and 200 DMA (₹280.84); conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                 | INTACT          |            4 |
| NTPC       | Power                | 0.6%     | +12.00%        | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹322.75 < 10-month average ₹353.83. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -40.18%        | N/A             | SELL        | Exit all 67 sh (~₹3,511)        | Thesis invalidated: Price ₹52.40 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +90.37%        | ₹135.92         | HOLD        | Hold                            | Consolidation hold: Price ₹162.54 moving sideways between 50 DMA (₹163.45) and 200 DMA (₹156.76); conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                  | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.4%     | +21.52%        | N/A             | SELL        | Exit all 8 sh (~₹2,756)         | Trend exit: month-end close ₹359.00 < 10-month average ₹382.51. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +9.58%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹35.46 moving sideways between 50 DMA (₹33.20) and 200 DMA (₹33.97); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +81.90%        | ₹208.60         | HOLD        | Hold                            | Pullback hold: Price ₹224.55 < 200 DMA (₹233.36) with return +81.90%; thesis remains INTACT above invalidation (₹117.28).                                                                                                                                      | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -3.93%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹57.23 < 200 DMA (₹58.69) with return -3.93%; thesis remains INTACT above invalidation (₹52.42).                                                                                                                                          | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹261.88 vs 200-day average ₹273.21 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 19.5%
* **Banking**: 17.5%
* **Commodities**: 10.8%
* **Power**: 8.7%
* **IT**: 7.3%
* **Insurance**: 5.2%
* **Consumption**: 5.0%
* **Broad Market**: 5.0%
* **Defense**: 4.8%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.6%
* **Telecom**: 3.0%
* **Auto**: 2.5%
* **Pharma**: 1.7%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 26.9%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.2%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.9%), +7 more          |
| Financials        | 26.9%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (14.5%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.5%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.6%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 10.8%      | 25.0% | OK        | ICIGOL (4.9%), ICIPSE (5.9%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 14.5%           | 14.99%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 14.5%           | 14.78%             | +0.31% via ICINIF                        |
| WIPRO    | 6.8%            | 6.82%              | Direct only                              |
| ICIPSE   | 5.9%            | 5.91%              | Direct only                              |
| LIC      | 5.2%            | 5.17%              | Direct only                              |
| TATGLO   | 5.0%            | 5.00%              | Direct only                              |
| ICIGOL   | 4.9%            | 4.91%              | Direct only                              |
| BHAELE   | 4.8%            | 4.83%              | Direct only                              |
| JSWENE   | 4.5%            | 4.49%              | Direct only                              |
| ICINIF   | 3.6%            | 3.61%              | Direct only                              |
| LGELEC   | 3.6%            | 3.57%              | Direct only                              |
| IDECEL   | 3.0%            | 2.97%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.73%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.51%              | Direct only                              |
| TATCAP   | 2.4%            | 2.45%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹22,158 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,218  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,141  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 14.5%    | ₹88,829 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.5%    | ₹88,722 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,070  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,726  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.8%     | ₹41,822 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.2%     | ₹31,680 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.6%     | ₹21,861 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹16,692 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,370 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹15,012 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.6%     | ₹10,075 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,806  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,048  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,756  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,695  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,717  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 5.9%     | ₹36,240 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.0%     | ₹30,630 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹29,600 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.5%     | ₹27,540 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.9%     | ₹11,582 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹10,971 | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,792  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,246  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,511  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,251  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.9%     | ₹30,118 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 3.0%     | ₹18,180 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,246  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,717)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,246)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,695)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,756)   |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,251)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,511)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,048)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,141)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,218) |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,246)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,792)  |
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
| Total Unrealised LTCG (> 365 days)    | ₹40,550.86  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹40,550.86  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,344.50   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹153,782**, Tax savings potential: **₹21,466**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹683.30  | ₹1267.91   | ₹43,846             | LTCG/STCG | ₹5,584                |
| RELIND   |       74 | ₹1167.40 | ₹1627.08   | ₹34,016             | LTCG/STCG | ₹4,532                |
| LIC      |       45 | ₹396.00  | ₹895.05    | ₹22,457             | LTCG/STCG | ₹3,186                |
| WIPRO    |      170 | ₹190.10  | ₹304.31    | ₹19,416             | LTCG/STCG | ₹2,521                |
| ICIPSE   |      193 | ₹187.77  | ₹250.36    | ₹12,079             | STCG      | ₹2,416                |
| ICIGOL   |      250 | ₹120.47  | ₹138.24    | ₹4,442              | STCG      | ₹888                  |
| JSWENE   |       28 | ₹510.00  | ₹668.00    | ₹4,424              | LTCG      | ₹553                  |
| JIOFIN   |       28 | ₹207.00  | ₹344.38    | ₹3,847              | LTCG      | ₹481                  |
| ASHLEY   |       43 | ₹145.00  | ₹212.38    | ₹2,897              | LTCG      | ₹362                  |
| SJVLIM   |       67 | ₹52.40   | ₹86.95     | ₹2,315              | LTCG      | ₹289                  |

*Showing top 10 of 19 loss-harvest candidates.*


