# Orchestrated Multi-Agent Portfolio Audit - 2026-11-06

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-06
* **Portfolio XIRR**: **-4.41%** (Current Traded Positions Value: ₹508,429)
* **Benchmark XIRR**: **7.24%** (Simulated Benchmark Value: ₹668,543)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹19,140         | 36.93%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,786          | 35.74%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,325         | 30.98%  | Full                 |
| GAIL       |         61 |           61 | ₹11,333         | 17.39%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,330          | 16.61%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 15.93%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,295          | 15.23%  | Full                 |
| BHAELE     |         80 |           48 | ₹19,008         | 14.33%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,514          | 12.67%  | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,837          | 12.02%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,238          | 9.29%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,820          | 8.06%   | Full                 |
| ICINIF     |         86 |           86 | ₹23,905         | 6.68%   | Full                 |
| TATGLO     |         30 |           30 | ₹32,589         | 6.57%   | Full                 |
| NTPC       |         12 |           12 | ₹3,881          | 5.74%   | Full                 |
| HINPET     |         14 |           14 | ₹5,420          | 2.69%   | Full                 |
| JSWENE     |         54 |           54 | ₹28,347         | 1.43%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,438          | 0.70%   | Full                 |
| HDF250     |         24 |           24 | ₹4,211          | -1.00%  | Full                 |
| ONGC       |         39 |           39 | ₹9,039          | -3.52%  | Full                 |
| ASHLEY     |        106 |           53 | ₹9,121          | -4.51%  | Partial (53/106 sh)  |
| MIR150     |        194 |          194 | ₹4,417          | -4.89%  | Full                 |
| RELIND     |         76 |           74 | ₹97,680         | -7.63%  | Partial (74/76 sh)   |
| GUJGA      |          7 |            7 | ₹2,808          | -7.71%  | Full                 |
| HDFBAN     |        130 |           75 | ₹59,119         | -11.42% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,829          | -13.36% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,474          | -15.56% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹33,660         | -17.47% | Partial (170/220 sh) |
| ICIGOL     |        250 |          250 | ₹30,075         | -18.70% | Full                 |
| ICIPSE     |        193 |          193 | ₹35,195         | -37.41% | Full                 |
| LIC        |         80 |           45 | ₹17,730         | -53.30% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 15.6%    | +7.10%         | N/A             | SELL        | Exit all 130 sh (~₹102,472)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 15.3%    | +13.92%        | N/A             | SELL        | Exit all 76 sh (~₹100,320)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 6.6%     | -16.25%        | N/A             | SELL        | Exit all 220 sh (~₹43,560)       | Thesis invalidated: Price ₹198.00 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 5.4%     | -27.42%        | N/A             | SELL        | Exit all 193 sh (~₹35,195)       | Thesis invalidated: Price ₹182.36 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| TATGLO     | Consumption          | 5.0%     | +35.68%        | N/A             | SELL        | Exit all 30 sh (~₹32,589)        | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| BHAELE     | Defense              | 4.8%     | +150.90%       | ₹330.97         | SELL        | Exit all 80 sh (~₹31,680)        | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| LIC        | Insurance            | 4.8%     | -56.13%        | N/A             | SELL        | Exit all 80 sh (~₹31,520)        | Thesis invalidated: Price ₹394.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 4.6%     | -13.29%        | N/A             | SELL        | Exit all 250 sh (~₹30,075)       | Thesis invalidated: Price ₹120.30 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.3%     | +3.19%         | N/A             | SELL        | Exit all 54 sh (~₹28,347)        | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.6%     | +2.54%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹277.96 moving sideways between 50 DMA (₹262.92) and 200 DMA (₹270.53); conviction (4/5) thesis INTACT above invalidation (₹238.55).                                                                                                 | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +53.87%        | ₹1285.20        | ACCUMULATE  | ACCUMULATE (next monthly review) | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +72.67%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹19,140)      | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| ASHLEY     | Auto                 | 2.8%     | +73.86%        | ₹148.26         | SELL        | Exit all 106 sh (~₹18,242)       | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.5%     | +9.83%         | N/A             | SELL        | Exit all 46 sh (~₹16,470)        | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| FEDBAN     | Banking              | 2.5%     | +126.90%       | ₹259.30         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +126.90%, position weight 2.5%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| JIOFIN     | Financial Services   | 1.9%     | -0.42%         | N/A             | SELL        | Exit all 53 sh (~₹12,254)        | Trend exit: month-end close ₹204.50 < 10-month average ₹237.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| NTPGRE     | Power                | 1.7%     | -23.49%        | N/A             | SELL        | Exit all 138 sh (~₹11,403)       | Thesis invalidated: Price ₹82.63 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +19.44%        | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +19.44%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -4.83%         | N/A             | SELL        | Exit all 39 sh (~₹9,039)         | Trend exit: month-end close ₹225.39 < 10-month average ₹254.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +15.61%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹1373.00 moving sideways between 50 DMA (₹1224.27) and 200 DMA (₹1244.67); conviction (5/5) thesis INTACT above invalidation (₹1009.47).                                                                                             | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | +4.07%         | N/A             | SELL        | Exit all 14 sh (~₹5,420)         | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.7%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting  | Unreliable price data: As-of (2026-09-26) price ₹314.08 differs from broker price ₹231.70 by +35.6% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| NHPC       | Power                | 0.7%     | +40.50%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹82.08 moving sideways between 50 DMA (₹75.04) and 200 DMA (₹76.84); conviction (3/5) thesis INTACT above invalidation (₹53.75).                                                                                                     | INTACT          |            3 |
| PETLNG     | Oil & Gas            | 0.7%     | +0.44%         | N/A             | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +0.44%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| MIR150     | Broad Market         | 0.7%     | -1.81%         | N/A             | REVIEW      | Review                           | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |
| HDF250     | Broad Market         | 0.6%     | -0.37%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹175.44 moving sideways between 50 DMA (₹179.48) and 200 DMA (₹171.16); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| NTPC       | Power                | 0.6%     | +16.67%        | N/A             | SELL        | Exit all 12 sh (~₹3,881)         | Trend exit: month-end close ₹313.25 < 10-month average ₹349.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -34.75%        | N/A             | SELL        | Exit all 67 sh (~₹3,829)         | Thesis invalidated: Price ₹57.15 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +95.00%        | ₹135.92         | HOLD        | Hold                             | Position hold: Technical trend BULLISH, total return +95.00%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                                | INTACT          |            3 |
| TATPOW     | Power                | 0.4%     | +24.32%        | N/A             | SELL        | Exit all 8 sh (~₹2,820)          | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting  | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +13.29%        | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹36.66 moving sideways between 50 DMA (₹33.48) and 200 DMA (₹33.80); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.3%     | +85.89%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,295)         | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | +2.79%         | N/A             | HOLD        | Hold                             | Consolidation hold: Price ₹61.23 moving sideways between 50 DMA (₹58.01) and 200 DMA (₹58.61); conviction (4/5) thesis INTACT above invalidation (₹52.42).                                                                                                     | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🟢 Market trend RISK-ON: Nifty ETF ₹284.22 vs 200-day average ₹272.62 (±2% band) — no market-wide action
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.3%
* **Banking**: 18.4%
* **Commodities**: 9.9%
* **Power**: 8.3%
* **IT**: 7.1%
* **Consumption**: 5.0%
* **Broad Market**: 5.0%
* **Defense**: 4.8%
* **Insurance**: 4.8%
* **Financial Services**: 4.4%
* **Consumer Electronics**: 3.5%
* **Telecom**: 2.9%
* **Auto**: 2.8%
* **Pharma**: 1.6%
* **Infrastructure**: 1.2%
* **Financials (combined)**: 27.6%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.7%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.7%), +7 more          |
| Financials        | 27.6%      | 25.0% | ⚠️ BREACH | FEDBAN (2.5%), HDFBAN (15.6%), KOTAKBKETF (0.3%), JIOFIN (1.9%), TATCAP (2.5%), +1 more |
| State-owned (PSU) | 19.0%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 9.9%       | 25.0% | OK        | ICIGOL (4.6%), ICIPSE (5.4%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 15.6%           | 16.11%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 15.3%           | 15.59%             | +0.31% via ICINIF                        |
| WIPRO    | 6.6%            | 6.64%              | Direct only                              |
| ICIPSE   | 5.4%            | 5.36%              | Direct only                              |
| TATGLO   | 5.0%            | 4.97%              | Direct only                              |
| BHAELE   | 4.8%            | 4.83%              | Direct only                              |
| LIC      | 4.8%            | 4.80%              | Direct only                              |
| ICIGOL   | 4.6%            | 4.58%              | Direct only                              |
| JSWENE   | 4.3%            | 4.32%              | Direct only                              |
| ICINIF   | 3.6%            | 3.64%              | Direct only                              |
| LGELEC   | 3.5%            | 3.47%              | Direct only                              |
| IDECEL   | 2.9%            | 2.92%              | Direct only                              |
| ASHLEY   | 2.8%            | 2.78%              | Direct only                              |
| TATCAP   | 2.5%            | 2.51%              | Direct only                              |
| FEDBAN   | 2.5%            | 2.49%              | +0.01% via KOTAKBKETF                    |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹23,905 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,417  |            4 |
| HDF250   | Index ETF (Core) | 0.6%     | ₹4,211  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value    | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:---------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 15.6%    | ₹102,472 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.3%    | ₹100,320 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,238   | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,881   | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.6%     | ₹43,560  | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 4.8%     | ₹31,520  | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹22,803  | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.8%     | ₹18,242  | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.5%     | ₹16,470  | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.5%     | ₹16,325  | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹11,333  | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹9,039   | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,438   | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,820   | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,786   | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,837   | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 5.4%     | ₹35,195  | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.0%     | ₹32,589  | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹31,680  | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.3%     | ₹28,347  | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.9%     | ₹12,254  | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.7%     | ₹11,403  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹5,420   | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.7%     | ₹4,866   | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,514   | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,829   | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,330   | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808   | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.6%     | ₹30,075  | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹19,140  | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.3%     | ₹2,295   | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,837)  |
| SEQSCI     | Pharma         | 0.3%     |            2 | Exit all 10 sh (~₹2,295)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,786)  |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,820)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,330)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,829)  |
| HDF250     | Broad Market   | 0.6%     |            4 | Exit all 24 sh (~₹4,211)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,417) |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,438)  |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,514)  |
| ENGIND     | Infrastructure | 0.7%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹5,420)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹48,319.71  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹48,319.71  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹3,859.39   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹132,178**, Tax savings potential: **₹18,089**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       55 | ₹788.25  | ₹1455.47   | ₹36,697             | LTCG      | ₹4,587                |
| RELIND   |       37 | ₹1320.00 | ₹1986.03   | ₹24,643             | LTCG/STCG | ₹3,088                |
| LIC      |       45 | ₹394.00  | ₹895.05    | ₹22,547             | LTCG/STCG | ₹3,006                |
| WIPRO    |      170 | ₹198.00  | ₹304.31    | ₹18,073             | LTCG/STCG | ₹2,282                |
| ICIPSE   |      193 | ₹182.36  | ₹250.36    | ₹13,123             | STCG      | ₹2,625                |
| ICIGOL   |      250 | ₹120.30  | ₹138.24    | ₹4,485              | STCG      | ₹897                  |
| JSWENE   |       28 | ₹524.95  | ₹668.00    | ₹4,005              | LTCG      | ₹501                  |
| JIOFIN   |       28 | ₹231.20  | ₹344.38    | ₹3,169              | LTCG      | ₹396                  |
| SJVLIM   |       67 | ₹57.15   | ₹86.95     | ₹1,997              | LTCG      | ₹250                  |
| ASHLEY   |       33 | ₹172.09  | ₹230.20    | ₹1,918              | LTCG      | ₹240                  |

*Showing top 10 of 18 loss-harvest candidates.*


