# Orchestrated Multi-Agent Portfolio Audit - 2026-10-30

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-30
* **Portfolio XIRR**: **-7.42%** (Current Traded Positions Value: ₹475,391)
* **Benchmark XIRR**: **3.82%** (Simulated Benchmark Value: ₹615,732)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| NIPNIT     |         76 |           76 | ₹2,753          | 33.70%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,306         | 31.15%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹17,745         | 30.99%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.11%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,182          | 15.48%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,184          | 14.02%  | Full                 |
| BHAELE     |         80 |           48 | ₹17,755         | 11.98%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,276          | 10.67%  | Full                 |
| DRREDD     |          6 |            6 | ₹8,112          | 8.41%   | Full                 |
| GAIL       |         61 |           61 | ₹10,243         | 7.69%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,760          | 7.32%   | Full                 |
| TATGLO     |         30 |           30 | ₹30,777         | 5.35%   | Full                 |
| NTPC       |         12 |           12 | ₹3,795          | 4.96%   | Full                 |
| JSWENE     |         54 |           54 | ₹27,019         | -0.26%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,053          | -4.25%  | Full                 |
| HINPET     |         14 |           14 | ₹4,768          | -4.35%  | Full                 |
| ONGC       |         39 |           39 | ₹8,790          | -5.77%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.79%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,675          | -10.28% | Partial (53/106 sh)  |
| ICINIF     |         86 |           86 | ₹22,379         | -10.55% | Full                 |
| HDF250     |         24 |           24 | ₹4,049          | -11.62% | Full                 |
| RELIND     |         76 |           74 | ₹86,203         | -12.45% | Partial (74/76 sh)   |
| HDFBAN     |        130 |           75 | ₹51,960         | -14.53% | Partial (75/130 sh)  |
| SJVLIM     |         67 |           67 | ₹3,577          | -15.45% | Full                 |
| WIPRO      |        220 |          170 | ₹33,713         | -17.56% | Partial (170/220 sh) |
| KOTAKBKETF |         30 |           30 | ₹1,704          | -19.21% | Full                 |
| MIR150     |        194 |          194 | ₹4,173          | -19.51% | Full                 |
| JIOFIN     |         53 |           28 | ₹5,726          | -19.99% | Partial (28/53 sh)   |
| ICIGOL     |        250 |          250 | ₹29,843         | -20.15% | Full                 |
| ICIPSE     |        193 |          193 | ₹34,952         | -38.91% | Full                 |
| LIC        |         80 |           45 | ₹17,246         | -55.13% | Partial (45/80 sh)   |

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
| HDFBAN     | Banking              | 14.7%    | -5.87%         | N/A             | SELL        | Exit all 130 sh (~₹90,064)      | Trend exit: month-end close ₹708.70 < 10-month average ₹793.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| RELIND     | Oil & Gas            | 14.5%    | +0.54%         | N/A             | SELL        | Exit all 76 sh (~₹88,532)       | Trend exit: month-end close ₹1187.00 < 10-month average ₹1348.24. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| WIPRO      | IT                   | 7.1%     | -16.12%        | N/A             | SELL        | Exit all 220 sh (~₹43,628)      | Thesis invalidated: Price ₹198.31 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 5.7%     | -27.92%        | N/A             | SELL        | Exit all 193 sh (~₹34,952)      | Thesis invalidated: Price ₹181.10 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| TATGLO     | Consumption          | 5.0%     | +28.14%        | N/A             | SELL        | Exit all 30 sh (~₹30,777)       | Trend exit: month-end close ₹949.50 < 10-month average ₹1090.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                   | INTACT          |            3 |
| LIC        | Insurance            | 5.0%     | -57.32%        | N/A             | SELL        | Exit all 80 sh (~₹30,660)       | Thesis invalidated: Price ₹383.25 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 4.9%     | -13.96%        | N/A             | SELL        | Exit all 250 sh (~₹29,843)      | Thesis invalidated: Price ₹119.37 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.8%     | +134.37%       | ₹330.97         | SELL        | Exit all 80 sh (~₹29,592)       | Trend exit: month-end close ₹388.30 < 10-month average ₹412.84. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| JSWENE     | Power                | 4.4%     | -1.64%         | N/A             | SELL        | Exit all 54 sh (~₹27,019)       | Trend exit: month-end close ₹494.70 < 10-month average ₹520.03. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.7%     | -4.01%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 37 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +45.74%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1661.40 moving sideways between 50 DMA (₹1685.87) and 200 DMA (₹1567.10); conviction (4/5) thesis INTACT above invalidation (₹1003.20).                                                                                             | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +60.08%        | ₹11.05          | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 1 sessions                                                                                                                                                                                   | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +126.63%       | ₹259.30         | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return +126.63%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +46.31%        | N/A             | SELL        | Exit all 106 sh (~₹15,351)      | Trend exit: month-end close ₹154.19 < 10-month average ₹169.46. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | -1.87%         | N/A             | SELL        | Exit all 46 sh (~₹14,715)       | Trend exit: month-end close ₹327.95 < 10-month average ₹338.49. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.9%     | -23.67%        | N/A             | SELL        | Exit all 138 sh (~₹11,377)      | Thesis invalidated: Price ₹82.44 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -11.92%        | N/A             | SELL        | Exit all 53 sh (~₹10,838)       | Thesis invalidated: Price ₹204.50 <= invalidation price ₹213.61.                                                                                                                                                                                               | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +7.95%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹167.91 moving sideways between 50 DMA (₹170.87) and 200 DMA (₹165.09); conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                 | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -7.45%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹225.80 < 10-month average ₹255.21. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.3%     | +13.84%        | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹1233.00 < 10-month average ₹1249.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| HINPET     | Oil & Gas            | 0.8%     | -8.46%         | N/A             | SELL        | Exit all 14 sh (~₹4,768)        | Thesis invalidated: Price ₹340.55 <= invalidation price ₹342.25.                                                                                                                                                                                               | INVALIDATED     |            3 |
| NHPC       | Power                | 0.7%     | +33.07%        | N/A             | SELL        | Exit all 55 sh (~₹4,276)        | Trend exit: month-end close ₹72.81 < 10-month average ₹77.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -7.24%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 8 sessions                                                                                                                                                                                   | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -8.27%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹289.50 moving sideways between 50 DMA (₹289.74) and 200 DMA (₹280.83); conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                 | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -4.20%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 0 sessions                                                                                                                                                                                   | INTACT          |            4 |
| NTPC       | Power                | 0.6%     | +14.07%        | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹322.75 < 10-month average ₹353.83. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -39.05%        | N/A             | SELL        | Exit all 67 sh (~₹3,577)        | Thesis invalidated: Price ₹53.39 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +86.33%        | ₹135.92         | HOLD        | Hold                            | Consolidation hold: Price ₹159.09 moving sideways between 50 DMA (₹163.52) and 200 DMA (₹156.64); conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                  | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.5%     | +21.69%        | N/A             | SELL        | Exit all 8 sh (~₹2,760)         | Trend exit: month-end close ₹359.00 < 10-month average ₹382.51. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NIPNIT     | IT                   | 0.5%     | +11.96%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹36.23 moving sideways between 50 DMA (₹33.25) and 200 DMA (₹33.94); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +76.91%        | ₹208.60         | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 2 sessions                                                                                                                                                                                   | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -4.65%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 1 sessions                                                                                                                                                                                   | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹262.89 vs 200-day average ₹273.05 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 19.5%
* **Banking**: 17.7%
* **Commodities**: 10.6%
* **Power**: 8.6%
* **IT**: 7.6%
* **Consumption**: 5.0%
* **Insurance**: 5.0%
* **Broad Market**: 5.0%
* **Defense**: 4.8%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.5%
* **Telecom**: 2.9%
* **Auto**: 2.5%
* **Pharma**: 1.7%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 26.9%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.1%      | 25.0% | ⚠️ BREACH | TATPOW (0.5%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.6%), NTPGRE (1.9%), +7 more          |
| Financials        | 26.9%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (14.7%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.4%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 10.6%      | 25.0% | OK        | ICIGOL (4.9%), ICIPSE (5.7%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 14.7%           | 15.23%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 14.5%           | 14.79%             | +0.31% via ICINIF                        |
| WIPRO    | 7.1%            | 7.13%              | Direct only                              |
| ICIPSE   | 5.7%            | 5.72%              | Direct only                              |
| TATGLO   | 5.0%            | 5.03%              | Direct only                              |
| LIC      | 5.0%            | 5.01%              | Direct only                              |
| ICIGOL   | 4.9%            | 4.88%              | Direct only                              |
| BHAELE   | 4.8%            | 4.84%              | Direct only                              |
| JSWENE   | 4.4%            | 4.42%              | Direct only                              |
| ICINIF   | 3.7%            | 3.66%              | Direct only                              |
| LGELEC   | 3.5%            | 3.53%              | Direct only                              |
| IDECEL   | 2.9%            | 2.90%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.67%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.51%              | Direct only                              |
| TATCAP   | 2.4%            | 2.41%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.7%     | ₹22,379 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,173  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,049  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 14.7%    | ₹90,064 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.5%    | ₹88,532 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.3%     | ₹8,112  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,795  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 7.1%     | ₹43,628 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.0%     | ₹30,660 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹21,598 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹16,306 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,351 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹14,715 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹10,243 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,790  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,053  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.5%     | ₹2,760  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.5%     | ₹2,753  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,704  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 5.7%     | ₹34,952 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 5.0%     | ₹30,777 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹29,592 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.4%     | ₹27,019 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.9%     | ₹11,377 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹10,838 | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,768  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,276  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,577  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,182  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 4.9%     | ₹29,843 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹17,745 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,184  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,704)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,184)  |
| NIPNIT     | IT             | 0.5%     |            4 | Exit all 76 sh (~₹2,753)  |
| TATPOW     | Power          | 0.5%     |            4 | Exit all 8 sh (~₹2,760)   |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,182)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,577)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,049)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,053)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,173) |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,276)  |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,768)  |
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
| Total Unrealised LTCG (> 365 days)    | ₹39,643.90  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹39,643.90  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,481.55   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹154,163**, Tax savings potential: **₹21,353**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹692.80  | ₹1267.91   | ₹43,133             | LTCG/STCG | ₹5,481                |
| RELIND   |       74 | ₹1164.90 | ₹1627.08   | ₹34,201             | LTCG/STCG | ₹4,560                |
| LIC      |       45 | ₹383.25  | ₹895.05    | ₹23,031             | LTCG/STCG | ₹3,071                |
| WIPRO    |      170 | ₹198.31  | ₹304.31    | ₹18,020             | LTCG/STCG | ₹2,273                |
| ICIPSE   |      193 | ₹181.10  | ₹250.36    | ₹13,366             | STCG      | ₹2,673                |
| ICIGOL   |      250 | ₹119.37  | ₹138.24    | ₹4,717              | STCG      | ₹943                  |
| JSWENE   |       28 | ₹500.35  | ₹668.00    | ₹4,694              | LTCG      | ₹587                  |
| JIOFIN   |       28 | ₹204.50  | ₹344.38    | ₹3,917              | LTCG      | ₹490                  |
| ASHLEY   |       43 | ₹144.82  | ₹212.38    | ₹2,905              | LTCG      | ₹363                  |
| SJVLIM   |       67 | ₹53.39   | ₹86.95     | ₹2,249              | LTCG      | ₹281                  |

*Showing top 10 of 19 loss-harvest candidates.*


