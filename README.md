# Orchestrated Multi-Agent Portfolio Audit - 2026-11-02

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-02
* **Portfolio XIRR**: **-6.70%** (Current Traded Positions Value: ₹482,828)
* **Benchmark XIRR**: **4.31%** (Simulated Benchmark Value: ₹623,010)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| NIPNIT     |         76 |           76 | ₹2,780          | 36.14%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹18,135         | 32.62%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,037         | 30.38%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.03%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,235          | 15.89%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,205          | 14.24%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,026         | 12.49%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,351          | 11.30%  | Full                 |
| GAIL       |         61 |           61 | ₹10,622         | 11.13%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,140          | 8.59%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,822          | 8.12%   | Full                 |
| NTPC       |         12 |           12 | ₹3,912          | 6.04%   | Full                 |
| TATGLO     |         30 |           30 | ₹30,816         | 5.37%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,378         | 0.20%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,182          | -2.56%  | Full                 |
| HINPET     |         14 |           14 | ₹4,908          | -2.78%  | Full                 |
| ONGC       |         39 |           39 | ₹8,924          | -4.56%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.75%  | Full                 |
| HDF250     |         24 |           24 | ₹4,105          | -7.84%  | Full                 |
| ICINIF     |         86 |           86 | ₹22,468         | -9.37%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,850          | -9.52%  | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹92,056         | -9.90%  | Partial (74/76 sh)   |
| SJVLIM     |         67 |           67 | ₹3,840          | -13.32% | Full                 |
| HDFBAN     |        130 |           75 | ₹52,050         | -14.45% | Partial (75/130 sh)  |
| MIR150     |        194 |          194 | ₹4,225          | -16.20% | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,711          | -17.16% | Full                 |
| WIPRO      |        220 |          170 | ₹33,425         | -17.86% | Partial (170/220 sh) |
| JIOFIN     |         53 |           28 | ₹5,933          | -18.70% | Partial (28/53 sh)   |
| ICIGOL     |        250 |          250 | ₹29,233         | -22.39% | Full                 |
| ICIPSE     |        193 |          193 | ₹34,265         | -40.35% | Full                 |
| LIC        |         80 |           45 | ₹17,518         | -54.19% | Partial (45/80 sh)   |

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
| RELIND     | Oil & Gas            | 15.2%    | +7.36%         | N/A             | SELL        | Exit all 76 sh (~₹94,544)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 14.5%    | -5.71%         | N/A             | SELL        | Exit all 130 sh (~₹90,220)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 7.0%     | -16.83%        | N/A             | SELL        | Exit all 220 sh (~₹43,256)      | Thesis invalidated: Price ₹196.62 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 5.5%     | -29.34%        | N/A             | SELL        | Exit all 193 sh (~₹34,265)      | Thesis invalidated: Price ₹177.54 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.0%     | -56.65%        | N/A             | SELL        | Exit all 80 sh (~₹31,144)       | Thesis invalidated: Price ₹389.30 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 5.0%     | +28.30%        | N/A             | SELL        | Exit all 30 sh (~₹30,816)       | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| BHAELE     | Defense              | 4.8%     | +137.95%       | ₹330.97         | SELL        | Exit all 80 sh (~₹30,044)       | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.7%     | -15.72%        | N/A             | SELL        | Exit all 250 sh (~₹29,233)      | Thesis invalidated: Price ₹116.93 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.4%     | -0.33%         | N/A             | SELL        | Exit all 54 sh (~₹27,378)       | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.6%     | -3.62%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 38 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +46.23%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1667.00 moving sideways between 50 DMA (₹1686.31) and 200 DMA (₹1568.29); conviction (4/5) thesis INTACT above invalidation (₹1003.20).                                                                                             | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +63.60%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹18,135)     | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| FEDBAN     | Banking              | 2.6%     | +122.90%       | ₹259.30         | HOLD        | Hold                            | Consolidation hold: Price ₹334.10 moving sideways between 50 DMA (₹338.29) and 200 DMA (₹310.37); conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                 | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +49.65%        | N/A             | SELL        | Exit all 106 sh (~₹15,701)      | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | -0.54%         | N/A             | SELL        | Exit all 46 sh (~₹14,916)       | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.9%     | -22.35%        | N/A             | SELL        | Exit all 138 sh (~₹11,573)      | Thesis invalidated: Price ₹83.86 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -8.73%         | N/A             | SELL        | Exit all 53 sh (~₹11,231)       | Thesis invalidated: Price ₹211.90 <= invalidation price ₹213.61.                                                                                                                                                                                               | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +11.94%        | N/A             | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return +11.94%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -6.04%         | N/A             | SELL        | Exit all 39 sh (~₹8,924)        | Trend exit: month-end close ₹225.39 < 10-month average ₹254.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +14.24%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1356.70 moving sideways between 50 DMA (₹1209.71) and 200 DMA (₹1241.21); conviction (5/5) thesis INTACT above invalidation (₹1009.47).                                                                                             | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | -5.77%         | N/A             | SELL        | Exit all 14 sh (~₹4,908)        | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| NHPC       | Power                | 0.7%     | +35.42%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹79.11 moving sideways between 50 DMA (₹74.75) and 200 DMA (₹76.84); conviction (3/5) thesis INTACT above invalidation (₹53.75).                                                                                                     | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -6.08%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 9 sessions                                                                                                                                                                                   | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -5.35%         | N/A             | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return -5.35%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -2.86%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |
| NTPC       | Power                | 0.6%     | +17.59%        | N/A             | SELL        | Exit all 12 sh (~₹3,912)        | Trend exit: month-end close ₹316.25 < 10-month average ₹353.10. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -34.57%        | N/A             | SELL        | Exit all 67 sh (~₹3,840)        | Thesis invalidated: Price ₹57.31 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +89.47%        | ₹135.92         | HOLD        | Hold                            | Consolidation hold: Price ₹161.77 moving sideways between 50 DMA (₹163.55) and 200 DMA (₹156.54); conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                  | INTACT          |            3 |
| TATPOW     | Power                | 0.5%     | +24.43%        | N/A             | SELL        | Exit all 8 sh (~₹2,822)         | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +13.04%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹36.58 moving sideways between 50 DMA (₹33.31) and 200 DMA (₹33.91); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +78.63%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,205)        | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -4.26%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹265.71 vs 200-day average ₹272.91 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.3%
* **Banking**: 17.4%
* **Commodities**: 10.2%
* **Power**: 8.7%
* **IT**: 7.4%
* **Insurance**: 5.0%
* **Consumption**: 5.0%
* **Broad Market**: 5.0%
* **Defense**: 4.8%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.5%
* **Telecom**: 2.9%
* **Auto**: 2.5%
* **Pharma**: 1.7%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 26.6%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 29.0%      | 25.0% | ⚠️ BREACH | TATPOW (0.5%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.9%), +7 more          |
| Financials        | 26.6%      | 25.0% | ⚠️ BREACH | FEDBAN (2.6%), HDFBAN (14.5%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.5%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 10.2%      | 25.0% | OK        | ICIGOL (4.7%), ICIPSE (5.5%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| RELIND   | 15.2%           | 15.55%             | +0.31% via ICINIF                        |
| HDFBAN   | 14.5%           | 15.04%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| WIPRO    | 7.0%            | 6.97%              | Direct only                              |
| ICIPSE   | 5.5%            | 5.52%              | Direct only                              |
| LIC      | 5.0%            | 5.02%              | Direct only                              |
| TATGLO   | 5.0%            | 4.97%              | Direct only                              |
| BHAELE   | 4.8%            | 4.84%              | Direct only                              |
| ICIGOL   | 4.7%            | 4.71%              | Direct only                              |
| JSWENE   | 4.4%            | 4.41%              | Direct only                              |
| ICINIF   | 3.6%            | 3.62%              | Direct only                              |
| LGELEC   | 3.5%            | 3.49%              | Direct only                              |
| IDECEL   | 2.9%            | 2.92%              | Direct only                              |
| FEDBAN   | 2.6%            | 2.59%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.53%              | Direct only                              |
| TATCAP   | 2.4%            | 2.40%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹22,468 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,225  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,105  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.2%    | ₹94,544 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 14.5%    | ₹90,220 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,140  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,912  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 7.0%     | ₹43,256 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.0%     | ₹31,144 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹21,671 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.6%     | ₹16,037 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,701 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹14,916 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹10,622 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,924  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,182  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.5%     | ₹2,822  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,780  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,711  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 5.5%     | ₹34,265 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.0%     | ₹30,816 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹30,044 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.4%     | ₹27,378 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.9%     | ₹11,573 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,231 | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,908  | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,351  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,840  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,235  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.7%     | ₹29,233 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹18,135 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,205  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,711)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,205)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,780)  |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.5%     |            4 | Exit all 8 sh (~₹2,822)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,235)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,840)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,105)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,182)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,225) |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,351)  |
| ENGIND     | Infrastructure | 0.8%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,908)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹41,165.26  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹41,165.26  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,775.42   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹148,541**, Tax savings potential: **₹20,590**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹694.00  | ₹1267.91   | ₹43,043             | LTCG/STCG | ₹5,468                |
| RELIND   |       62 | ₹1244.00 | ₹1707.69   | ₹28,749             | LTCG/STCG | ₹3,730                |
| LIC      |       45 | ₹389.30  | ₹895.05    | ₹22,759             | LTCG/STCG | ₹3,035                |
| WIPRO    |      170 | ₹196.62  | ₹304.31    | ₹18,308             | LTCG/STCG | ₹2,324                |
| ICIPSE   |      193 | ₹177.54  | ₹250.36    | ₹14,053             | STCG      | ₹2,811                |
| ICIGOL   |      250 | ₹116.93  | ₹138.24    | ₹5,327              | STCG      | ₹1,065                |
| JSWENE   |       28 | ₹507.00  | ₹668.00    | ₹4,508              | LTCG      | ₹563                  |
| JIOFIN   |       28 | ₹211.90  | ₹344.38    | ₹3,710              | LTCG      | ₹464                  |
| ASHLEY   |       41 | ₹148.12  | ₹215.55    | ₹2,765              | LTCG      | ₹346                  |
| SJVLIM   |       67 | ₹57.31   | ₹86.95     | ₹1,986              | LTCG      | ₹248                  |

*Showing top 10 of 19 loss-harvest candidates.*


