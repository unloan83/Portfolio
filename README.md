# Orchestrated Multi-Agent Portfolio Audit - 2026-10-21

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-21
* **Portfolio XIRR**: **-7.30%** (Current Traded Positions Value: ₹477,559)
* **Benchmark XIRR**: **3.14%** (Simulated Benchmark Value: ₹605,430)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| NIPNIT     |         76 |           76 | ₹2,730          | 33.18%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,418         | 31.71%  | Full                 |
| IDECEL     |       1500 |         1500 | ₹17,595         | 30.83%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.35%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,252          | 16.16%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,102          | 13.12%  | Full                 |
| BHAELE     |         80 |           48 | ₹17,621         | 11.81%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹3,959          | 7.85%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,782          | 7.68%   | Full                 |
| GAIL       |         61 |           61 | ₹10,078         | 6.28%   | Full                 |
| TATGLO     |         30 |           30 | ₹28,962         | 4.07%   | Full                 |
| NTPC       |         12 |           12 | ₹3,617          | 3.27%   | Full                 |
| DRREDD     |          6 |            6 | ₹7,437          | 3.05%   | Full                 |
| JSWENE     |         54 |           54 | ₹25,372         | -2.48%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,130          | -3.29%  | Full                 |
| HINPET     |         14 |           14 | ₹4,789          | -4.16%  | Full                 |
| ONGC       |         39 |           39 | ₹8,797          | -5.82%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.89%  | Full                 |
| HDF250     |         24 |           24 | ₹4,106          | -8.55%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,655          | -10.45% | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹89,007         | -11.33% | Partial (74/76 sh)   |
| ICINIF     |         86 |           86 | ₹22,359         | -11.50% | Full                 |
| HDFBAN     |        130 |           75 | ₹52,500         | -14.37% | Partial (75/130 sh)  |
| ICIGOL     |        250 |          250 | ₹30,608         | -17.60% | Full                 |
| SJVLIM     |         67 |           67 | ₹3,290          | -17.99% | Full                 |
| JIOFIN     |         53 |           28 | ₹5,898          | -19.15% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹32,043         | -20.04% | Partial (170/220 sh) |
| MIR150     |        194 |          194 | ₹4,185          | -20.15% | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,709          | -20.27% | Full                 |
| ICIPSE     |        193 |          193 | ₹39,285         | -27.90% | Full                 |
| LIC        |         80 |           45 | ₹17,597         | -55.12% | Partial (45/80 sh)   |

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
| RELIND     | Oil & Gas            | 14.9%    | +3.81%         | N/A             | SELL        | Exit all 76 sh (~₹91,413)       | Trend exit: month-end close ₹1187.00 < 10-month average ₹1348.24. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| HDFBAN     | Banking              | 14.8%    | -4.89%         | N/A             | SELL        | Exit all 130 sh (~₹91,000)      | Trend exit: month-end close ₹708.70 < 10-month average ₹793.75. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| WIPRO      | IT                   | 6.8%     | -20.27%        | N/A             | SELL        | Exit all 220 sh (~₹41,468)      | Thesis invalidated: Price ₹188.49 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIPSE     | Commodities          | 6.4%     | -18.99%        | N/A             | SELL        | Exit all 193 sh (~₹39,285)      | Thesis invalidated: Price ₹203.55 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| LIC        | Insurance            | 5.1%     | -56.45%        | N/A             | SELL        | Exit all 80 sh (~₹31,284)       | Thesis invalidated: Price ₹391.05 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 5.0%     | -11.76%        | N/A             | SELL        | Exit all 250 sh (~₹30,608)      | Thesis invalidated: Price ₹122.43 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.8%     | +132.59%       | ₹330.97         | SELL        | Exit all 80 sh (~₹29,368)       | Trend exit: month-end close ₹388.30 < 10-month average ₹412.84. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| TATGLO     | Consumption          | 4.7%     | +20.58%        | N/A             | SELL        | Exit all 30 sh (~₹28,962)       | Trend exit: month-end close ₹949.50 < 10-month average ₹1090.32. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                   | INTACT          |            3 |
| JSWENE     | Power                | 4.1%     | -7.64%         | N/A             | SELL        | Exit all 54 sh (~₹25,372)       | Trend exit: month-end close ₹494.70 < 10-month average ₹520.03. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            3 |
| ICINIF     | Broad Market         | 3.6%     | -4.09%         | N/A             | REVIEW      | Review                          | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 29 sessions                                                                                                                                                                                  | INTACT          |            4 |
| LGELEC     | Consumer Electronics | 3.5%     | +45.09%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹1654.00 moving sideways between 50 DMA (₹1680.36) and 200 DMA (₹1561.29); conviction (4/5) thesis INTACT above invalidation (₹1003.20).                                                                                             | INTACT          |            4 |
| IDECEL     | Telecom              | 2.9%     | +58.73%        | ₹11.05          | HOLD        | Hold                            | Pullback hold: Price ₹11.73 < 200 DMA (₹12.30) with return +58.73%; thesis remains INTACT above invalidation (₹7.02).                                                                                                                                          | INTACT          |            2 |
| FEDBAN     | Banking              | 2.7%     | +128.20%       | ₹259.30         | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return +128.20%, position weight 2.7%; conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +45.92%        | N/A             | SELL        | Exit all 106 sh (~₹15,310)      | Trend exit: month-end close ₹154.19 < 10-month average ₹169.46. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.3%     | -4.06%         | N/A             | SELL        | Exit all 46 sh (~₹14,386)       | Trend exit: month-end close ₹327.95 < 10-month average ₹338.49. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NTPGRE     | Power                | 1.9%     | -22.42%        | N/A             | SELL        | Exit all 138 sh (~₹11,563)      | Thesis invalidated: Price ₹83.79 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.8%     | -9.28%         | N/A             | SELL        | Exit all 53 sh (~₹11,164)       | Trend exit: month-end close ₹216.88 < 10-month average ₹246.07. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INVALIDATED     |            3 |
| GAIL       | Oil & Gas            | 1.6%     | +6.22%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹165.22 moving sideways between 50 DMA (₹171.91) and 200 DMA (₹165.07); conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                 | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -7.37%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹225.80 < 10-month average ₹255.21. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| DRREDD     | Pharma               | 1.2%     | +4.37%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹1233.00 < 10-month average ₹1249.29. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                  | INTACT          |            5 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| HINPET     | Oil & Gas            | 0.8%     | -8.04%         | N/A             | SELL        | Exit all 14 sh (~₹4,789)        | Trend exit: month-end close ₹350.35 < 10-month average ₹380.95. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INVALIDATED     |            3 |
| MIR150     | Broad Market         | 0.7%     | -6.99%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹21.57 < 200 DMA (₹22.66) with return -6.99%; thesis remains INTACT above invalidation (₹20.41).                                                                                                                                          | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -6.53%         | N/A             | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return -6.53%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | -2.85%         | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹171.08 moving sideways between 50 DMA (₹182.72) and 200 DMA (₹170.87); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +23.23%        | N/A             | SELL        | Exit all 55 sh (~₹3,959)        | Trend exit: month-end close ₹72.81 < 10-month average ₹77.36. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                      | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +8.74%         | N/A             | SELL        | Hold (below minimum trade)      | Trend exit: month-end close ₹322.75 < 10-month average ₹353.83. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            5 |
| SJVLIM     | Power                | 0.5%     | -43.94%        | N/A             | SELL        | Exit all 67 sh (~₹3,290)        | Thesis invalidated: Price ₹49.10 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +90.45%        | ₹135.92         | HOLD        | Hold                            | Position hold: Technical trend BULLISH, total return +90.45%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                                | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.5%     | +22.66%        | N/A             | SELL        | Exit all 8 sh (~₹2,782)         | Trend exit: month-end close ₹359.00 < 10-month average ₹382.51. Sell and hold cash; re-entry is signalled when a month-end close is back above the average.                                                                                                    | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +11.00%        | N/A             | HOLD        | Hold                            | Consolidation hold: Price ₹35.92 moving sideways between 50 DMA (₹33.11) and 200 DMA (₹34.16); conviction (4/5) thesis INTACT above invalidation (₹28.48).                                                                                                     | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.3%     | +70.31%        | ₹208.60         | HOLD        | Hold                            | Pullback hold: Price ₹210.25 < 200 DMA (₹233.15) with return +70.31%; thesis remains INTACT above invalidation (₹117.28).                                                                                                                                      | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -4.40%         | N/A             | HOLD        | Hold                            | Pullback hold: Price ₹56.95 < 200 DMA (₹58.83) with return -4.40%; thesis remains INTACT above invalidation (₹52.42).                                                                                                                                          | INTACT          |            4 |

### Market Trend and Re-entry Watchlist
* 🔴 Market trend RISK-OFF: Nifty ETF ₹259.05 vs 200-day average ₹274.30 (±2% band) — warning only: stop new buying; per-stock trend exits do the selling
* Sold stocks watched for re-entry: none

### Sector Concentration Metrics
* **Oil & Gas**: 19.9%
* **Banking**: 17.8%
* **Commodities**: 11.4%
* **Power**: 8.2%
* **IT**: 7.2%
* **Insurance**: 5.1%
* **Broad Market**: 5.0%
* **Defense**: 4.8%
* **Consumption**: 4.7%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.5%
* **Telecom**: 2.9%
* **Auto**: 2.5%
* **Pharma**: 1.6%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 27.0%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.1%      | 25.0% | ⚠️ BREACH | TATPOW (0.5%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.5%), NTPGRE (1.9%), +7 more          |
| Financials        | 27.0%      | 25.0% | ⚠️ BREACH | FEDBAN (2.7%), HDFBAN (14.8%), KOTAKBKETF (0.3%), JIOFIN (1.8%), TATCAP (2.3%), +1 more |
| State-owned (PSU) | 19.3%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.6%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 11.4%      | 25.0% | OK        | ICIGOL (5.0%), ICIPSE (6.4%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 14.8%           | 15.33%             | +0.42% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 14.9%           | 15.21%             | +0.31% via ICINIF                        |
| WIPRO    | 6.8%            | 6.76%              | Direct only                              |
| ICIPSE   | 6.4%            | 6.40%              | Direct only                              |
| LIC      | 5.1%            | 5.10%              | Direct only                              |
| ICIGOL   | 5.0%            | 4.99%              | Direct only                              |
| BHAELE   | 4.8%            | 4.79%              | Direct only                              |
| TATGLO   | 4.7%            | 4.72%              | Direct only                              |
| JSWENE   | 4.1%            | 4.13%              | Direct only                              |
| ICINIF   | 3.6%            | 3.64%              | Direct only                              |
| LGELEC   | 3.5%            | 3.50%              | Direct only                              |
| IDECEL   | 2.9%            | 2.87%              | Direct only                              |
| FEDBAN   | 2.7%            | 2.68%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.49%              | Direct only                              |
| TATCAP   | 2.3%            | 2.34%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **5.0%** (Target: 50.0%, Gap: +45.0%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.0%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹22,359 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,185  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,106  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.9%    | ₹91,413 | Active         |
| HDFBAN     | Banking              | Single Stock  |            5 | 14.8%    | ₹91,000 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.2%     | ₹7,437  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,617  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.8%     | ₹41,468 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.1%     | ₹31,284 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.5%     | ₹21,502 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.7%     | ₹16,418 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,310 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.3%     | ₹14,386 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.6%     | ₹10,078 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,797  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,130  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.5%     | ₹2,782  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,730  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,709  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.4%     | ₹39,285 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.8%     | ₹29,368 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.7%     | ₹28,962 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.1%     | ₹25,372 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 1.9%     | ₹11,563 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.8%     | ₹11,164 | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,789  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹3,959  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.5%     | ₹3,290  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,252  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 5.0%     | ₹30,608 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 2.9%     | ₹17,595 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.3%     | ₹2,102  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,709)  |
| SEQSCI     | Pharma         | 0.3%     |            2 | Exit all 10 sh (~₹2,102)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,730)  |
| TATPOW     | Power          | 0.5%     |            4 | Exit all 8 sh (~₹2,782)   |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,252)  |
| SJVLIM     | Power          | 0.5%     |            3 | Exit all 67 sh (~₹3,290)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹3,959)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,106)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,130)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,185) |
| HINPET     | Oil & Gas      | 0.8%     |            3 | Exit all 14 sh (~₹4,789)  |
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
| Total Unrealised LTCG (> 365 days)    | ₹35,783.21  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest   | ₹35,783.21  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,369.10   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹148,022**, Tax savings potential: **₹20,588**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹700.00  | ₹1267.91   | ₹42,593             | LTCG/STCG | ₹5,402                |
| RELIND   |       72 | ₹1202.80 | ₹1639.79   | ₹31,463             | LTCG/STCG | ₹4,147                |
| LIC      |       45 | ₹391.05  | ₹895.05    | ₹22,680             | LTCG/STCG | ₹3,409                |
| WIPRO    |      170 | ₹188.49  | ₹304.31    | ₹19,690             | LTCG/STCG | ₹2,570                |
| ICIPSE   |      193 | ₹203.55  | ₹250.36    | ₹9,033              | STCG      | ₹1,807                |
| JSWENE   |       28 | ₹469.85  | ₹668.00    | ₹5,548              | LTCG      | ₹694                  |
| ICIGOL   |      250 | ₹122.43  | ₹138.24    | ₹3,952              | STCG      | ₹790                  |
| JIOFIN   |       28 | ₹210.64  | ₹344.38    | ₹3,745              | LTCG      | ₹468                  |
| ASHLEY   |       43 | ₹144.43  | ₹212.38    | ₹2,922              | LTCG      | ₹365                  |
| SJVLIM   |       67 | ₹49.10   | ₹86.95     | ₹2,536              | LTCG      | ₹317                  |

*Showing top 10 of 19 loss-harvest candidates.*


