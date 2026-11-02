# Orchestrated Multi-Agent Portfolio Audit - 2026-11-02

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-11-02
* **Portfolio XIRR**: **-6.21%** (Current Traded Positions Value: ₹488,252)
* **Benchmark XIRR**: **4.52%** (Simulated Benchmark Value: ₹626,087)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹18,375         | 33.73%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,741          | 31.34%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,200         | 30.79%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.03%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,250          | 16.01%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,203          | 14.22%  | Full                 |
| GAIL       |         61 |           61 | ₹10,797         | 12.73%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,072         | 12.58%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,333          | 11.14%  | Full                 |
| TATPOW     |          8 |            8 | ₹2,847          | 8.44%   | Full                 |
| DRREDD     |          6 |            6 | ₹8,052          | 7.90%   | Full                 |
| NTPC       |         12 |           12 | ₹3,876          | 5.71%   | Full                 |
| TATGLO     |         30 |           30 | ₹30,867         | 5.41%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,297         | 0.10%   | Full                 |
| PETLNG     |         14 |           14 | ₹4,213          | -2.15%  | Full                 |
| ONGC       |         39 |           39 | ₹9,158          | -2.51%  | Full                 |
| HINPET     |         14 |           14 | ₹4,872          | -3.18%  | Full                 |
| HDF250     |         24 |           24 | ₹4,110          | -7.52%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.75%  | Full                 |
| RELIND     |         76 |           74 | ₹96,200         | -8.24%  | Partial (74/76 sh)   |
| ASHLEY     |        106 |           53 | ₹7,908          | -9.28%  | Partial (53/106 sh)  |
| ICINIF     |         86 |           86 | ₹22,468         | -9.37%  | Full                 |
| SJVLIM     |         67 |           67 | ₹3,786          | -13.75% | Full                 |
| HDFBAN     |        130 |           75 | ₹52,500         | -14.25% | Partial (75/130 sh)  |
| MIR150     |        194 |          194 | ₹4,227          | -16.09% | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,709          | -17.60% | Full                 |
| WIPRO      |        220 |          170 | ₹33,388         | -17.91% | Partial (170/220 sh) |
| JIOFIN     |         53 |           28 | ₹5,971          | -18.48% | Partial (28/53 sh)   |
| ICIGOL     |        250 |          250 | ₹29,155         | -22.70% | Full                 |
| ICIPSE     |        193 |          193 | ₹34,499         | -39.73% | Full                 |
| LIC        |         80 |           45 | ₹17,505         | -54.22% | Partial (45/80 sh)   |

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
| RELIND     | Oil & Gas            | 15.8%    | +12.20%        | N/A             | SELL        | Exit all 76 sh (~₹98,800)       | Trend exit: month-end close ₹1164.90 < 10-month average ₹1308.41. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 14.5%    | -4.89%         | N/A             | SELL        | Exit all 130 sh (~₹91,000)      | Trend exit: month-end close ₹692.80 < 10-month average ₹765.53. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 6.9%     | -16.92%        | N/A             | SELL        | Exit all 220 sh (~₹43,208)      | Thesis invalidated: Price ₹196.40 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 5.5%     | -28.86%        | N/A             | SELL        | Exit all 193 sh (~₹34,499)      | Thesis invalidated: Price ₹178.75 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.0%     | -56.68%        | N/A             | SELL        | Exit all 80 sh (~₹31,120)       | Thesis invalidated: Price ₹389.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| TATGLO     | Consumption          | 4.9%     | +28.51%        | N/A             | SELL        | Exit all 30 sh (~₹30,867)       | Trend exit: month-end close ₹1025.90 < 10-month average ₹1074.71. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            3 |
| BHAELE     | Defense              | 4.8%     | +138.55%       | ₹330.97         | SELL        | Exit all 80 sh (~₹30,120)       | Trend exit: month-end close ₹369.90 < 10-month average ₹410.09. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICIGOL     | Commodities          | 4.7%     | -15.94%        | N/A             | SELL        | Exit all 250 sh (~₹29,155)      | Thesis invalidated: Price ₹116.62 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| JSWENE     | Power                | 4.4%     | -0.63%         | N/A             | SELL        | Exit all 54 sh (~₹27,297)       | Trend exit: month-end close ₹500.35 < 10-month average ₹521.99. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.6%     | -3.62%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 38 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +47.54%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1682.00 moving sideways between 50 DMA (₹1686.61) and 200 DMA (₹1568.36); conviction (4/5) thesis INTACT above invalidation (₹1003.20).                                                                                             | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +65.76%        | ₹11.05          | SELL        | Exit all 1500 sh (~₹18,375)     | Trend exit: month-end close ₹11.83 < 10-month average ₹12.11. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            2 |
| FEDBAN     | Banking              | 2.6%     | +125.17%       | ₹259.30         | HOLD        | Hold                            | Consolidation hold: Price ₹337.50 moving sideways between 50 DMA (₹338.36) and 200 DMA (₹310.38); conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                 | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +50.74%        | ₹148.26         | SELL        | Exit all 106 sh (~₹15,815)      | Trend exit: month-end close ₹144.82 < 10-month average ₹166.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | -0.21%         | N/A             | SELL        | Exit all 46 sh (~₹14,964)       | Trend exit: month-end close ₹319.90 < 10-month average ₹336.35. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.8%     | -22.76%        | N/A             | SELL        | Exit all 138 sh (~₹11,512)      | Thesis invalidated: Price ₹83.42 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -8.15%         | N/A             | SELL        | Exit all 53 sh (~₹11,302)       | Thesis invalidated: Price ₹213.25 <= invalidation price ₹213.61.                                                                                                                                                                                               | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +13.79%        | N/A             | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return +13.79%, position weight 1.7%; conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                               | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.5%     | -3.57%         | N/A             | SELL        | Exit all 39 sh (~₹9,158)        | Trend exit: month-end close ₹225.39 < 10-month average ₹254.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +13.00%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1342.00 moving sideways between 50 DMA (₹1209.41) and 200 DMA (₹1241.13); conviction (5/5) thesis INTACT above invalidation (₹1009.47).                                                                                             | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | -6.45%         | N/A             | SELL        | Exit all 14 sh (~₹4,872)        | Trend exit: month-end close ₹340.55 < 10-month average ₹367.55. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| NHPC       | Power                | 0.7%     | +34.85%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹78.78 moving sideways between 50 DMA (₹74.75) and 200 DMA (₹76.84); conviction (3/5) thesis INTACT above invalidation (₹53.75).                                                                                                     | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -6.04%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 9 sessions                                                                                                                                                                                   | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -4.64%         | N/A             | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return -4.64%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -2.74%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |
| NTPC       | Power                | 0.6%     | +16.51%        | N/A             | SELL        | Exit all 12 sh (~₹3,876)        | Trend exit: month-end close ₹316.25 < 10-month average ₹353.10. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -35.49%        | N/A             | SELL        | Exit all 67 sh (~₹3,786)        | Thesis invalidated: Price ₹56.50 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +90.30%        | ₹135.92         | HOLD        | Hold                            | Consolidation hold: Price ₹162.48 moving sideways between 50 DMA (₹163.56) and 200 DMA (₹156.55); conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                  | INTACT          |            3 |
| TATPOW     | Power                | 0.5%     | +25.52%        | N/A             | SELL        | Exit all 8 sh (~₹2,847)         | Trend exit: month-end close ₹345.05 < 10-month average ₹379.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| GUJGA      | Oil & Gas            | 0.4%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| NIPNIT     | IT                   | 0.4%     | +11.43%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹36.06 moving sideways between 50 DMA (₹33.30) and 200 DMA (₹33.91); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +78.46%        | ₹208.60         | SELL        | Exit all 10 sh (~₹2,203)        | Trend exit: month-end close ₹218.39 < 10-month average ₹231.17. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -4.38%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹265.90 vs 200-day average ₹272.91 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 20.9%
* **Banking**: 17.4%
* **Commodities**: 10.2%
* **Power**: 8.6%
* **IT**: 7.3%
* **Insurance**: 5.0%
* **Consumption**: 4.9%
* **Broad Market**: 4.9%
* **Defense**: 4.8%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.5%
* **Telecom**: 2.9%
* **Auto**: 2.5%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 26.5%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 29.4%      | 25.0% | ⚠️ BREACH | TATPOW (0.5%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.8%), +7 more          |
| Financials        | 26.5%      | 25.0% | ⚠️ BREACH | FEDBAN (2.6%), HDFBAN (14.5%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.4%      | 25.0% | OK        | ONGC (1.5%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 10.2%      | 25.0% | OK        | ICIGOL (4.7%), ICIPSE (5.5%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| RELIND   | 15.8%           | 16.08%             | +0.30% via ICINIF                        |
| HDFBAN   | 14.5%           | 15.02%             | +0.41% via ICINIF, +0.08% via KOTAKBKETF |
| WIPRO    | 6.9%            | 6.90%              | Direct only                              |
| ICIPSE   | 5.5%            | 5.51%              | Direct only                              |
| LIC      | 5.0%            | 4.97%              | Direct only                              |
| TATGLO   | 4.9%            | 4.93%              | Direct only                              |
| BHAELE   | 4.8%            | 4.81%              | Direct only                              |
| ICIGOL   | 4.7%            | 4.65%              | Direct only                              |
| JSWENE   | 4.4%            | 4.36%              | Direct only                              |
| ICINIF   | 3.6%            | 3.59%              | Direct only                              |
| LGELEC   | 3.5%            | 3.49%              | Direct only                              |
| IDECEL   | 2.9%            | 2.93%              | Direct only                              |
| FEDBAN   | 2.6%            | 2.59%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.52%              | Direct only                              |
| TATCAP   | 2.4%            | 2.39%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **4.9%** (Target: 50.0%, Gap: +45.1%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.1%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹22,468 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,227  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,110  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 15.8%    | ₹98,800 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 14.5%    | ₹91,000 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,052  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,876  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.9%     | ₹43,208 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.0%     | ₹31,120 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹21,866 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.6%     | ₹16,200 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,815 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹14,964 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹10,797 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.5%     | ₹9,158  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,213  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.5%     | ₹2,847  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,741  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,709  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 5.5%     | ₹34,499 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.9%     | ₹30,867 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹30,120 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.4%     | ₹27,297 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.8%     | ₹11,512 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,302 | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,872  | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,333  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,786  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,250  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.4%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.7%     | ₹29,155 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹18,375 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,203  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,709)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,203)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,741)  |
| GUJGA      | Oil & Gas      | 0.4%     |            3 | Exit all 7 sh (~₹2,808)   |
| TATPOW     | Power          | 0.5%     |            4 | Exit all 8 sh (~₹2,847)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,250)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,786)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,110)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,213)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,227) |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,333)  |
| ENGIND     | Infrastructure | 0.8%     |            3 | Exit all 21 sh (~₹4,866)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,872)  |

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
| Total Unrealised LTCG (> 365 days)    | ₹42,473.13  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹42,473.13  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,866.53   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹144,516**, Tax savings potential: **₹19,953**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹700.00  | ₹1267.91   | ₹42,593             | LTCG/STCG | ₹5,402                |
| RELIND   |       47 | ₹1300.00 | ₹1842.64   | ₹25,504             | LTCG/STCG | ₹3,220                |
| LIC      |       45 | ₹389.00  | ₹895.05    | ₹22,772             | LTCG/STCG | ₹3,036                |
| WIPRO    |      170 | ₹196.40  | ₹304.31    | ₹18,345             | LTCG/STCG | ₹2,330                |
| ICIPSE   |      193 | ₹178.75  | ₹250.36    | ₹13,820             | STCG      | ₹2,764                |
| ICIGOL   |      250 | ₹116.62  | ₹138.24    | ₹5,405              | STCG      | ₹1,081                |
| JSWENE   |       28 | ₹505.50  | ₹668.00    | ₹4,550              | LTCG      | ₹569                  |
| JIOFIN   |       28 | ₹213.25  | ₹344.38    | ₹3,672              | LTCG      | ₹459                  |
| ASHLEY   |       41 | ₹149.20  | ₹215.55    | ₹2,720              | LTCG      | ₹340                  |
| SJVLIM   |       67 | ₹56.50   | ₹86.95     | ₹2,040              | LTCG      | ₹255                  |

*Showing top 10 of 19 loss-harvest candidates.*


