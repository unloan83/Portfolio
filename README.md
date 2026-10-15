# Orchestrated Multi-Agent Portfolio Audit - 2026-10-15

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-15
* **Portfolio XIRR**: **-6.81%** (Current Traded Positions Value: ₹483,366)
* **Benchmark XIRR**: **3.79%** (Simulated Benchmark Value: ₹614,243)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹18,780         | 36.92%  | Full                 |
| FEDBAN     |         48 |           48 | ₹16,080         | 31.03%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,362          | 17.11%  | Full                 |
| ENGIND     |         21 |           21 | ₹4,866          | 16.52%  | Full                 |
| NIPNIT     |         76 |           76 | ₹2,593          | 16.49%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,259          | 15.05%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,259         | 13.16%  | Partial (48/80 sh)   |
| GAIL       |         61 |           61 | ₹10,330         | 8.84%   | Full                 |
| NHPC       |         55 |           55 | ₹3,998          | 8.27%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,798          | 7.94%   | Full                 |
| NTPC       |         12 |           12 | ₹3,776          | 4.85%   | Full                 |
| TATGLO     |         30 |           30 | ₹29,744         | 4.66%   | Full                 |
| DRREDD     |          6 |            6 | ₹7,313          | 2.04%   | Full                 |
| HDF250     |         24 |           24 | ₹4,234          | 0.58%   | Full                 |
| JSWENE     |         54 |           54 | ₹25,863         | -1.82%  | Full                 |
| HINPET     |         14 |           14 | ₹4,879          | -3.19%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,133          | -3.28%  | Full                 |
| ONGC       |         39 |           39 | ₹8,761          | -6.24%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.96%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,854          | -9.67%  | Partial (53/106 sh)  |
| RELIND     |         76 |           74 | ₹89,910         | -11.01% | Partial (74/76 sh)   |
| MIR150     |        194 |          194 | ₹4,307          | -13.30% | Full                 |
| HDFBAN     |        130 |           75 | ₹54,514         | -13.53% | Partial (75/130 sh)  |
| ICINIF     |         86 |           86 | ₹22,212         | -13.81% | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,739          | -13.87% | Full                 |
| SJVLIM     |         67 |           67 | ₹3,711          | -14.56% | Full                 |
| ICIGOL     |        250 |          250 | ₹31,030         | -16.16% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,132          | -17.89% | Partial (28/53 sh)   |
| WIPRO      |        220 |          170 | ₹29,589         | -23.88% | Partial (170/220 sh) |
| ICIPSE     |        193 |          193 | ₹39,802         | -26.99% | Full                 |
| LIC        |         80 |           45 | ₹17,730         | -55.36% | Partial (45/80 sh)   |

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
| Symbol     | Sector               | Weight   | Total Return   | Trailing Stop   | Decision    | Action                              | Reasoning                                                                                                                                                                                                                                                      | Thesis Status   |   Conviction |
|:-----------|:---------------------|:---------|:---------------|:----------------|:------------|:------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|-------------:|
| HDFBAN     | Banking              | 15.2%    | -1.24%         | N/A             | TRIM        | Trim 62 sh (~₹45,065) → 7.9% weight | Position cap breach: Weight 15.2% exceeds max position limit (8.0%); trim required.; also under REVIEW: 200-DMA breakdown                                                                                                                                      | INTACT          |            5 |
| RELIND     | Oil & Gas            | 14.8%    | +4.86%         | N/A             | TRIM        | Trim 35 sh (~₹42,525) → 8.0% weight | Position cap breach: Weight 14.8% exceeds max position limit (8.0%); trim required.; also under REVIEW: 200-DMA breakdown                                                                                                                                      | INTACT          |            5 |
| ICIPSE     | Commodities          | 6.4%     | -17.92%        | N/A             | SELL        | Exit all 193 sh (~₹39,802)          | Thesis invalidated: Price ₹206.23 <= invalidation price ₹231.16.                                                                                                                                                                                               | INVALIDATED     |            3 |
| WIPRO      | IT                   | 6.1%     | -26.38%        | N/A             | SELL        | Exit all 220 sh (~₹38,291)          | Thesis invalidated: Price ₹174.05 <= invalidation price ₹208.04.                                                                                                                                                                                               | INVALIDATED     |            4 |
| LIC        | Insurance            | 5.1%     | -56.13%        | N/A             | SELL        | Exit all 80 sh (~₹31,520)           | Thesis invalidated: Price ₹394.00 <= invalidation price ₹790.25.                                                                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 5.0%     | -10.54%        | N/A             | SELL        | Exit all 250 sh (~₹31,030)          | Thesis invalidated: Price ₹124.12 <= invalidation price ₹131.80.                                                                                                                                                                                               | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.9%     | +141.02%       | ₹330.97         | REVIEW      | Review                              | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 24 sessions                                                                                                                                                                                  | INTACT          |            3 |
| TATGLO     | Consumption          | 4.8%     | +23.84%        | N/A             | REVIEW      | Review                              | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 46 sessions                                                                                                                                                                                  | INTACT          |            3 |
| JSWENE     | Power                | 4.1%     | -5.85%         | N/A             | TRIM        | Hold (below minimum trade)          | Risk group cap breach: Risk factor group exposure (28.2%) exceeds limit (25.0%); trim holding (4.1% weight) for risk-factor control.                                                                                                                           | INTACT          |            3 |
| LGELEC     | Consumer Electronics | 3.6%     | +51.94%        | ₹1277.50        | ACCUMULATE  | ACCUMULATE (next monthly review)    | Accumulation channel intact; scheduled for next monthly review.                                                                                                                                                                                                | INTACT          |            4 |
| ICINIF     | Broad Market         | 3.6%     | -4.72%         | N/A             | REVIEW      | Review                              | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 25 sessions                                                                                                                                                                                  | INTACT          |            4 |
| IDECEL     | Telecom              | 3.0%     | +69.42%        | ₹11.05          | HOLD        | Hold                                | Consolidation hold: Price ₹12.52 moving sideways between 50 DMA (₹13.88) and 200 DMA (₹12.29); conviction (2/5) thesis INTACT above invalidation (₹7.02).                                                                                                      | INTACT          |            2 |
| FEDBAN     | Banking              | 2.6%     | +123.50%       | ₹259.30         | HOLD        | Hold                                | Consolidation hold: Price ₹335.00 moving sideways between 50 DMA (₹340.87) and 200 DMA (₹305.90); conviction (4/5) thesis INTACT above invalidation (₹131.90).                                                                                                 | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +49.71%        | N/A             | REVIEW      | Review                              | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 23 sessions                                                                                                                                                                                  | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | -1.43%         | N/A             | HOLD        | Hold                                | Pullback hold: Price ₹321.35 < 200 DMA (₹339.70) with return -1.43%; thesis remains INTACT above invalidation (₹286.88).                                                                                                                                       | INTACT          |            4 |
| NTPGRE     | Power                | 2.0%     | -16.06%        | N/A             | SELL        | Exit all 138 sh (~₹12,511)          | Thesis invalidated: Price ₹90.66 <= invalidation price ₹99.36.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.9%     | -5.67%         | N/A             | REVIEW      | Review                              | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 43 sessions                                                                                                                                                                                  | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +8.87%         | N/A             | HOLD        | Hold                                | Consolidation hold: Price ₹169.35 moving sideways between 50 DMA (₹172.41) and 200 DMA (₹165.04); conviction (4/5) thesis INTACT above invalidation (₹136.88).                                                                                                 | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -7.76%         | N/A             | REVIEW      | Review                              | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 49 sessions                                                                                                                                                                                  | INTACT          |            4 |
| DRREDD     | Pharma               | 1.2%     | +2.63%         | N/A             | HOLD        | Hold                                | Pullback hold: Price ₹1218.80 < 200 DMA (₹1238.81) with return +2.63%; thesis remains INTACT above invalidation (₹1009.47).                                                                                                                                    | INTACT          |            5 |
| HINPET     | Oil & Gas            | 0.8%     | -6.32%         | N/A             | REVIEW      | Review                              | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 49 sessions                                                                                                                                                                                  | INTACT          |            3 |
| ENGIND     | Infrastructure       | 0.8%     | +29.80%        | N/A             | VERIFY DATA | Verify price data before acting     | Unreliable price data: As-of (2026-09-26) price ₹315.65 differs from broker price ₹231.70 by +36.2% (limit ±25%); check ticker or corporate action.; evaluation incomplete.                                                                                    | INTACT          |            3 |
| MIR150     | Broad Market         | 0.7%     | -4.27%         | N/A             | HOLD        | Hold                                | Pullback hold: Price ₹22.20 < 200 DMA (₹22.67) with return -4.27%; thesis remains INTACT above invalidation (₹20.41).                                                                                                                                          | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +0.18%         | N/A             | HOLD        | Hold                                | Consolidation hold: Price ₹176.40 moving sideways between 50 DMA (₹183.42) and 200 DMA (₹170.70); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                                                                 | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -6.46%         | N/A             | HOLD        | Hold                                | Position hold: Technical trend BULLISH, total return -6.46%, position weight 0.7%; conviction (4/5) thesis INTACT above invalidation (₹277.73).                                                                                                                | INTACT          |            4 |
| NHPC       | Power                | 0.6%     | +24.44%        | N/A             | HOLD        | Hold                                | Pullback hold: Price ₹72.70 < 200 DMA (₹77.14) with return +24.44%; thesis remains INTACT above invalidation (₹53.75).                                                                                                                                         | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +13.50%        | N/A             | REVIEW      | Review                              | 200-DMA breakdown hysteresis review: price > 3% below 200-DMA for 49 sessions                                                                                                                                                                                  | INTACT          |            5 |
| SJVLIM     | Power                | 0.6%     | -36.76%        | N/A             | SELL        | Exit all 67 sh (~₹3,711)            | Thesis invalidated: Price ₹55.39 <= invalidation price ₹80.58.                                                                                                                                                                                                 | INVALIDATED     |            3 |
| GUJPPL     | Infrastructure       | 0.5%     | +96.87%        | ₹135.92         | HOLD        | Hold                                | Position hold: Technical trend BULLISH, total return +96.87%, position weight 0.5%; conviction (3/5) thesis INTACT above invalidation (₹78.55).                                                                                                                | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | N/A             | VERIFY DATA | Verify price data before acting     | invalidation breached on broker price (₹401.15 <= ₹430.75); live price unreliable — verify before acting. Unreliable price data: As-of (2026-09-26) price ₹236.02 differs from broker price ₹401.15 by -41.2% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.4%     | +23.37%        | N/A             | HOLD        | Hold                                | Pullback hold: Price ₹349.80 < 200 DMA (₹383.10) with return +23.37%; thesis remains INTACT above invalidation (₹249.52).                                                                                                                                      | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +5.44%         | N/A             | HOLD        | Hold                                | Pullback hold: Price ₹34.12 < 200 DMA (₹34.31) with return +5.44%; thesis remains INTACT above invalidation (₹28.48).                                                                                                                                          | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +83.01%        | ₹208.60         | HOLD        | Hold                                | Pullback hold: Price ₹225.93 < 200 DMA (₹233.04) with return +83.01%; thesis remains INTACT above invalidation (₹117.28).                                                                                                                                      | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -2.69%         | N/A             | HOLD        | Hold                                | Pullback hold: Price ₹57.97 < 200 DMA (₹58.88) with return -2.69%; thesis remains INTACT above invalidation (₹52.42).                                                                                                                                          | INTACT          |            4 |

### Sector Concentration Metrics
* **Oil & Gas**: 19.8%
* **Banking**: 18.0%
* **Commodities**: 11.4%
* **Power**: 8.4%
* **IT**: 6.6%
* **Insurance**: 5.1%
* **Broad Market**: 4.9%
* **Defense**: 4.9%
* **Consumption**: 4.8%
* **Financial Services**: 4.2%
* **Consumer Electronics**: 3.6%
* **Telecom**: 3.0%
* **Auto**: 2.5%
* **Pharma**: 1.5%
* **Infrastructure**: 1.3%
* **Financials (combined)**: 27.3%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 28.2%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.6%), SJVLIM (0.6%), NTPGRE (2.0%), +7 more          |
| Financials        | 27.3%      | 25.0% | ⚠️ BREACH | FEDBAN (2.6%), HDFBAN (15.2%), KOTAKBKETF (0.3%), JIOFIN (1.9%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 19.5%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.7%), HINPET (0.8%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 11.4%      | 25.0% | OK        | ICIGOL (5.0%), ICIPSE (6.4%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 15.2%           | 15.64%             | +0.41% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 14.8%           | 15.11%             | +0.30% via ICINIF                        |
| ICIPSE   | 6.4%            | 6.38%              | Direct only                              |
| WIPRO    | 6.1%            | 6.14%              | Direct only                              |
| LIC      | 5.1%            | 5.05%              | Direct only                              |
| ICIGOL   | 5.0%            | 4.98%              | Direct only                              |
| BHAELE   | 4.9%            | 4.88%              | Direct only                              |
| TATGLO   | 4.8%            | 4.77%              | Direct only                              |
| JSWENE   | 4.1%            | 4.15%              | Direct only                              |
| LGELEC   | 3.6%            | 3.61%              | Direct only                              |
| ICINIF   | 3.6%            | 3.56%              | Direct only                              |
| IDECEL   | 3.0%            | 3.01%              | Direct only                              |
| FEDBAN   | 2.6%            | 2.59%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.52%              | Direct only                              |
| TATCAP   | 2.4%            | 2.37%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **4.9%** (Target: 50.0%, Gap: +45.1%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.1%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹22,212 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,307  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,234  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 15.2%    | ₹94,490 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.8%    | ₹92,340 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.2%     | ₹7,313  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,776  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.1%     | ₹38,291 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.1%     | ₹31,520 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.6%     | ₹22,517 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.6%     | ₹16,080 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,707 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹14,782 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹10,330 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,761  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,133  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,798  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,593  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,739  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.4%     | ₹39,802 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹30,432 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.8%     | ₹29,744 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.1%     | ₹25,863 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 2.0%     | ₹12,511 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.9%     | ₹11,608 | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.8%     | ₹4,879  | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 0.8%     | ₹4,866  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.6%     | ₹3,998  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.6%     | ₹3,711  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.5%     | ₹3,362  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 5.0%     | ₹31,030 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 3.0%     | ₹18,780 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,259  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,739)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,259)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,593)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,798)   |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.5%     |            3 | Exit all 20 sh (~₹3,362)  |
| SJVLIM     | Power          | 0.6%     |            3 | Exit all 67 sh (~₹3,711)  |
| NHPC       | Power          | 0.6%     |            3 | Exit all 55 sh (~₹3,998)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,133)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,234)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,307) |
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
| Total Unrealised LTCG (> 365 days)    | ₹38,800.75  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest  | ₹38,800.75  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,458.82   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹145,322**, Tax savings potential: **₹20,430**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹726.85  | ₹1267.91   | ₹40,579             | LTCG/STCG | ₹5,110                |
| RELIND   |       67 | ₹1215.00 | ₹1671.95   | ₹30,616             | LTCG/STCG | ₹4,018                |
| LIC      |       45 | ₹394.00  | ₹895.05    | ₹22,547             | LTCG/STCG | ₹3,579                |
| WIPRO    |      170 | ₹174.05  | ₹304.31    | ₹22,144             | LTCG/STCG | ₹3,007                |
| ICIPSE   |      193 | ₹206.23  | ₹250.36    | ₹8,516              | STCG      | ₹1,703                |
| JSWENE   |       28 | ₹478.95  | ₹668.00    | ₹5,293              | LTCG      | ₹662                  |
| ICIGOL   |      250 | ₹124.12  | ₹138.24    | ₹3,530              | STCG      | ₹706                  |
| JIOFIN   |       28 | ₹219.01  | ₹344.38    | ₹3,510              | LTCG      | ₹439                  |
| ASHLEY   |       41 | ₹148.18  | ₹215.55    | ₹2,762              | LTCG      | ₹345                  |
| SJVLIM   |       67 | ₹55.39   | ₹86.95     | ₹2,115              | LTCG      | ₹264                  |

*Showing top 10 of 21 loss-harvest candidates.*


