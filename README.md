# Orchestrated Multi-Agent Portfolio Audit - 2026-10-13

### Portfolio Performance vs Benchmark

* **First Recorded Trade**: 2021-04-16
* **Valuation Date**: 2026-10-13
* **Portfolio XIRR**: **-7.09%** (Current Traded Positions Value: ₹480,578)
* **Benchmark XIRR**: **3.27%** (Simulated Benchmark Value: ₹606,887)
* *Benchmark: Nifty 50 (^NSEI; Nifty 50 TRI is not available on Yahoo Finance)*

#### Holding-Level XIRR (From Trade Cash Flows)

| Symbol     |   Held Qty |   Traded Qty | Current Value   | XIRR    | History              |
|:-----------|-----------:|-------------:|:----------------|:--------|:---------------------|
| IDECEL     |       1500 |         1500 | ₹19,200         | 39.08%  | Full                 |
| ENGIND     |         21 |           21 | ₹6,060          | 32.07%  | Full                 |
| FEDBAN     |         48 |           48 | ₹15,816         | 30.40%  | Full                 |
| GUJPPL     |         20 |           20 | ₹3,433          | 17.70%  | Full                 |
| SEQSCI     |         10 |           10 | ₹2,350          | 16.11%  | Full                 |
| BHAELE     |         80 |           48 | ₹18,240         | 13.15%  | Partial (48/80 sh)   |
| NHPC       |         55 |           55 | ₹4,042          | 8.69%   | Full                 |
| GAIL       |         61 |           61 | ₹10,266         | 8.27%   | Full                 |
| TATPOW     |          8 |            8 | ₹2,760          | 7.44%   | Full                 |
| HDF250     |         24 |           24 | ₹4,318          | 7.39%   | Full                 |
| NIPNIT     |         76 |           76 | ₹2,513          | 6.47%   | Full                 |
| NTPC       |         12 |           12 | ₹3,732          | 4.43%   | Full                 |
| TATGLO     |         30 |           30 | ₹28,800         | 3.97%   | Full                 |
| DRREDD     |          6 |            6 | ₹7,440          | 3.12%   | Full                 |
| JSWENE     |         54 |           54 | ₹24,867         | -3.21%  | Full                 |
| PETLNG     |         14 |           14 | ₹4,060          | -4.27%  | Full                 |
| SJVLIM     |         67 |           67 | ₹5,036          | -4.97%  | Full                 |
| HINPET     |         14 |           14 | ₹4,606          | -6.33%  | Full                 |
| ONGC       |         39 |           39 | ₹8,683          | -6.98%  | Full                 |
| GUJGA      |          7 |            7 | ₹2,808          | -7.98%  | Full                 |
| ASHLEY     |        106 |           53 | ₹7,811          | -9.87%  | Partial (53/106 sh)  |
| MIR150     |        194 |          194 | ₹4,328          | -12.09% | Full                 |
| RELIND     |         76 |           74 | ₹86,336         | -12.63% | Partial (74/76 sh)   |
| HDFBAN     |        130 |           75 | ₹53,550         | -13.98% | Partial (75/130 sh)  |
| ICIGOL     |        250 |          250 | ₹31,358         | -14.83% | Full                 |
| ICINIF     |         86 |           86 | ₹22,036         | -16.16% | Full                 |
| KOTAKBKETF |         30 |           30 | ₹1,729          | -17.09% | Full                 |
| JIOFIN     |         53 |           28 | ₹6,098          | -18.13% | Partial (28/53 sh)   |
| ICIPSE     |        193 |          193 | ₹41,840         | -20.99% | Full                 |
| WIPRO      |        220 |          170 | ₹28,730         | -25.35% | Partial (170/220 sh) |
| LIC        |         80 |           45 | ₹17,732         | -55.55% | Partial (45/80 sh)   |

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
| Symbol     | Sector               | Weight   | Total Return   | Trailing Stop   | Decision   | Action                                                           | Reasoning                                                                                                                                                                                                      | Thesis Status   |   Conviction |
|:-----------|:---------------------|:---------|:---------------|:----------------|:-----------|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|-------------:|
| HDFBAN     | Banking              | 15.0%    | -2.99%         | ₹959.47         | TRIM       | Trim 65 sh (~₹46,410) → 7.5% weight                              | trailing stop hit                                                                                                                                                                                              | INTACT          |            5 |
| RELIND     | Oil & Gas            | 14.3%    | +0.69%         | ₹1538.62        | TRIM       | Trim 38 sh (~₹44,335) → 7.1% weight                              | trailing stop hit                                                                                                                                                                                              | INTACT          |            5 |
| ICIPSE     | Commodities          | 6.7%     | -13.72%        | ₹360.51         | SELL       | Exit all 193 sh (~₹41,840)                                       | Thesis invalidated: Price ₹216.79 <= invalidation price ₹231.16.                                                                                                                                               | INVALIDATED     |            3 |
| WIPRO      | IT                   | 6.0%     | -28.51%        | ₹251.04         | SELL       | Exit all 220 sh (~₹37,180)                                       | Thesis invalidated: Price ₹169.00 <= invalidation price ₹208.04.                                                                                                                                               | INVALIDATED     |            4 |
| LIC        | Insurance            | 5.1%     | -56.12%        | ₹790.25         | SELL       | Exit all 80 sh (~₹31,524)                                        | Thesis invalidated: Price ₹394.05 <= invalidation price ₹790.25.                                                                                                                                               | INVALIDATED     |            4 |
| ICIGOL     | Commodities          | 5.1%     | -9.59%         | ₹152.49         | SELL       | Exit all 250 sh (~₹31,358)                                       | Thesis invalidated: Price ₹125.43 <= invalidation price ₹131.80.                                                                                                                                               | INVALIDATED     |            2 |
| BHAELE     | Defense              | 4.9%     | +140.77%       | ₹448.25         | TRIM       | Trim 40 sh (~₹15,200) → 2.4% weight                              | trailing stop hit                                                                                                                                                                                              | INTACT          |            3 |
| TATGLO     | Consumption          | 4.6%     | +19.91%        | ₹1215.95        | TRIM       | Trim 15 sh (~₹14,400) → 2.3% weight                              | trailing stop hit                                                                                                                                                                                              | INTACT          |            3 |
| JSWENE     | Power                | 4.0%     | -9.48%         | ₹577.57         | SELL       | Exit all 54 sh (~₹24,867)                                        | Thesis invalidated: Price ₹460.50 <= invalidation price ₹468.00.                                                                                                                                               | INVALIDATED     |            3 |
| LGELEC     | Consumer Electronics | 3.7%     | +54.21%        | ₹1679.61        | ACCUMULATE | Accumulate: buy 15 sh (~₹26,370), stop ₹1661.07, target ₹1951.86 | Structural accumulation: Price ₹1758.00 > 50 DMA (₹1661.59) > 200 DMA (₹1556.31); weight 3.7% < 8.0% max cap with conviction (4/5).                                                                            | INTACT          |            4 |
| ICINIF     | Broad Market         | 3.6%     | -5.48%         | ₹285.31         | TRIM       | Trim 43 sh (~₹11,018) → 1.8% weight                              | trailing stop hit                                                                                                                                                                                              | INTACT          |            4 |
| IDECEL     | Telecom              | 3.1%     | +73.21%        | ₹14.37          | TRIM       | Trim 750 sh (~₹9,600) → 1.5% weight                              | trailing stop hit                                                                                                                                                                                              | INTACT          |            2 |
| FEDBAN     | Banking              | 2.5%     | +119.83%       | ₹346.66         | TRIM       | Trim 41 sh (~₹13,510) → 0.4% weight                              | trailing stop hit                                                                                                                                                                                              | INTACT          |            4 |
| ASHLEY     | Auto                 | 2.5%     | +48.89%        | ₹199.60         | TRIM       | Trim 53 sh (~₹7,811) → 1.3% weight                               | trailing stop hit                                                                                                                                                                                              | INTACT          |            4 |
| TATCAP     | Financial Services   | 2.4%     | +0.51%         | ₹363.35         | TRIM       | Trim 41 sh (~₹13,434) → 0.3% weight                              | trailing stop hit                                                                                                                                                                                              | INTACT          |            4 |
| NTPGRE     | Power                | 2.1%     | -14.04%        | ₹112.88         | SELL       | Exit all 138 sh (~₹12,812)                                       | Thesis invalidated: Price ₹92.84 <= invalidation price ₹99.36.                                                                                                                                                 | INVALIDATED     |            3 |
| JIOFIN     | Financial Services   | 1.9%     | -6.19%         | ₹301.48         | SELL       | Exit all 53 sh (~₹11,543)                                        | Structural breakdown: Price ₹217.80 < 200 DMA (₹246.68) with return -6.19%; conviction (3/5) < 4 or thesis INTACT insufficient to hold breakdown.                                                              | INTACT          |            3 |
| GAIL       | Oil & Gas            | 1.7%     | +8.20%         | ₹171.54         | TRIM       | Trim 31 sh (~₹5,217) → 0.8% weight                               | trailing stop hit                                                                                                                                                                                              | INTACT          |            4 |
| ONGC       | Oil & Gas            | 1.4%     | -8.57%         | ₹293.31         | TRIM       | Trim 20 sh (~₹4,453) → 0.7% weight                               | trailing stop hit                                                                                                                                                                                              | INTACT          |            4 |
| DRREDD     | Pharma               | 1.2%     | +4.41%         | ₹1322.18        | TRIM       | Trim 3 sh (~₹3,720) → 0.6% weight                                | trailing stop hit                                                                                                                                                                                              | INTACT          |            5 |
| ENGIND     | Infrastructure       | 1.0%     | +61.64%        | ₹281.96         | HOLD       | Hold                                                             | Position hold: Technical trend BULLISH, total return +61.64%, position weight 1.0%; conviction (3/5) thesis INTACT above invalidation (₹164.23).                                                               | INTACT          |            3 |
| SJVLIM     | Power                | 0.8%     | -14.19%        | ₹84.78          | SELL       | Exit all 67 sh (~₹5,036)                                         | Thesis invalidated: Broker price ₹75.16 <= invalidation price ₹80.58. Unreliable price data: Live price ₹56.07 differs from broker price ₹75.16 by -25.4% (limit ±25%); check ticker or corporate action..     | INVALIDATED     |            3 |
| HINPET     | Oil & Gas            | 0.7%     | -11.56%        | ₹456.47         | SELL       | Exit all 14 sh (~₹4,606)                                         | Thesis invalidated: Price ₹329.00 <= invalidation price ₹342.25.                                                                                                                                               | INVALIDATED     |            3 |
| MIR150     | Broad Market         | 0.7%     | -3.79%         | ₹23.05          | TRIM       | Trim 97 sh (~₹2,164) → 0.3% weight                               | trailing stop hit                                                                                                                                                                                              | INTACT          |            4 |
| HDF250     | Broad Market         | 0.7%     | +2.18%         | ₹179.35         | HOLD       | Hold                                                             | Consolidation hold: Price ₹179.92 moving sideways between 50 DMA (₹183.60) and 200 DMA (₹170.55); conviction (4/5) thesis INTACT above invalidation (₹154.96).                                                 | INTACT          |            4 |
| PETLNG     | Oil & Gas            | 0.7%     | -8.11%         | ₹303.99         | TRIM       | Trim 7 sh (~₹2,030) → 0.3% weight                                | trailing stop hit                                                                                                                                                                                              | INTACT          |            4 |
| NHPC       | Power                | 0.7%     | +25.80%        | ₹82.13          | TRIM       | Trim 28 sh (~₹2,058) → 0.3% weight                               | trailing stop hit                                                                                                                                                                                              | INTACT          |            3 |
| NTPC       | Power                | 0.6%     | +12.18%        | ₹392.64         | TRIM       | Trim 6 sh (~₹1,866) → 0.3% weight                                | trailing stop hit                                                                                                                                                                                              | INTACT          |            5 |
| GUJPPL     | Infrastructure       | 0.6%     | +101.04%       | ₹178.76         | TRIM       | Trim 10 sh (~₹1,716) → 0.3% weight                               | trailing stop hit                                                                                                                                                                                              | INTACT          |            3 |
| GUJGA      | Oil & Gas            | 0.5%     | -14.32%        | ₹430.75         | SELL       | Exit all 7 sh (~₹2,808)                                          | Thesis invalidated: Broker price ₹401.15 <= invalidation price ₹430.75. Unreliable price data: Live price ₹221.80 differs from broker price ₹401.15 by -44.7% (limit ±25%); check ticker or corporate action.. | INVALIDATED     |            3 |
| TATPOW     | Power                | 0.4%     | +21.68%        | ₹438.59         | TRIM       | Trim 4 sh (~₹1,380) → 0.2% weight                                | trailing stop hit                                                                                                                                                                                              | INTACT          |            4 |
| NIPNIT     | IT                   | 0.4%     | +2.16%         | ₹41.42          | TRIM       | Trim 38 sh (~₹1,256) → 0.2% weight                               | trailing stop hit                                                                                                                                                                                              | INTACT          |            4 |
| SEQSCI     | Pharma               | 0.4%     | +90.38%        | ₹272.36         | TRIM       | Trim 5 sh (~₹1,175) → 0.2% weight                                | trailing stop hit                                                                                                                                                                                              | INTACT          |            2 |
| KOTAKBKETF | Banking              | 0.3%     | -3.26%         | ₹61.36          | TRIM       | Trim 30 sh (~₹1,729) → 0.0% weight                               | trailing stop hit                                                                                                                                                                                              | INTACT          |            4 |

### Sector Concentration Metrics
* **Oil & Gas**: 19.2%
* **Banking**: 17.8%
* **Commodities**: 11.8%
* **Power**: 8.6%
* **IT**: 6.4%
* **Insurance**: 5.1%
* **Broad Market**: 4.9%
* **Defense**: 4.9%
* **Consumption**: 4.6%
* **Financial Services**: 4.3%
* **Consumer Electronics**: 3.7%
* **Telecom**: 3.1%
* **Auto**: 2.5%
* **Pharma**: 1.6%
* **Infrastructure**: 1.5%
* **Financials (combined)**: 27.2%
### Risk Factor Groups Concentration

Portfolio exposure across macro risk buckets (Risk Cap: **25.0%**):

| Risk Group        | Exposure   | Cap   | Status    | Top Constituents                                                                        |
|:------------------|:-----------|:------|:----------|:----------------------------------------------------------------------------------------|
| Energy & Power    | 27.8%      | 25.0% | ⚠️ BREACH | TATPOW (0.4%), NTPC (0.6%), NHPC (0.7%), SJVLIM (0.8%), NTPGRE (2.1%), +7 more          |
| Financials        | 27.2%      | 25.0% | ⚠️ BREACH | FEDBAN (2.5%), HDFBAN (15.0%), KOTAKBKETF (0.3%), JIOFIN (1.9%), TATCAP (2.4%), +1 more |
| State-owned (PSU) | 20.0%      | 25.0% | OK        | ONGC (1.4%), GAIL (1.7%), HINPET (0.7%), PETLNG (0.7%), NTPC (0.6%), +7 more            |
| Precious metals   | 11.8%      | 25.0% | OK        | ICIGOL (5.1%), ICIPSE (6.7%)                                                            |

### ETF Look-Through Effective Exposure

Combined direct stock holdings plus indirect exposure via Nifty 50 (`ICINIF`) and Nifty Bank (`KOTAKBKETF`) index ETFs:

| Symbol   | Direct Weight   | Effective Weight   | Indirect Source                          |
|:---------|:----------------|:-------------------|:-----------------------------------------|
| HDFBAN   | 15.0%           | 15.45%             | +0.41% via ICINIF, +0.08% via KOTAKBKETF |
| RELIND   | 14.3%           | 14.59%             | +0.30% via ICINIF                        |
| ICIPSE   | 6.7%            | 6.74%              | Direct only                              |
| WIPRO    | 6.0%            | 5.99%              | Direct only                              |
| LIC      | 5.1%            | 5.08%              | Direct only                              |
| ICIGOL   | 5.1%            | 5.05%              | Direct only                              |
| BHAELE   | 4.9%            | 4.90%              | Direct only                              |
| TATGLO   | 4.6%            | 4.64%              | Direct only                              |
| JSWENE   | 4.0%            | 4.01%              | Direct only                              |
| LGELEC   | 3.7%            | 3.68%              | Direct only                              |
| ICINIF   | 3.6%            | 3.55%              | Direct only                              |
| IDECEL   | 3.1%            | 3.09%              | Direct only                              |
| FEDBAN   | 2.5%            | 2.56%              | +0.01% via KOTAKBKETF                    |
| ASHLEY   | 2.5%            | 2.52%              | Direct only                              |
| TATCAP   | 2.4%            | 2.43%              | Direct only                              |

*Showing top 15 of 47 holdings by effective weight.*

### Core / Satellite Portfolio Structure

* **Core Allocation (Index ETFs)**: **4.9%** (Target: 50.0%, Gap: +45.1%) across 3 index ETFs
* **Satellite Allocation (Stocks & Thematic ETFs)**: **95.1%** across **31 holdings** (Target: ≤15, Excess: +16)

#### Core Holdings (Passive Index Foundation)

| Symbol   | Category         | Weight   | Value   |   Conviction |
|:---------|:-----------------|:---------|:--------|-------------:|
| ICINIF   | Index ETF (Core) | 3.6%     | ₹22,036 |            4 |
| MIR150   | Index ETF (Core) | 0.7%     | ₹4,328  |            4 |
| HDF250   | Index ETF (Core) | 0.7%     | ₹4,318  |            4 |

#### Satellite Holdings (Ranked by Conviction & Weight)

| Symbol     | Sector               | Type          |   Conviction | Weight   | Value   | Status         |
|:-----------|:---------------------|:--------------|-------------:|:---------|:--------|:---------------|
| HDFBAN     | Banking              | Single Stock  |            5 | 15.0%    | ₹92,820 | Active         |
| RELIND     | Oil & Gas            | Single Stock  |            5 | 14.3%    | ₹88,669 | Active         |
| DRREDD     | Pharma               | Single Stock  |            5 | 1.2%     | ₹7,440  | Active         |
| NTPC       | Power                | Single Stock  |            5 | 0.6%     | ₹3,732  | Active         |
| WIPRO      | IT                   | Single Stock  |            4 | 6.0%     | ₹37,180 | Active         |
| LIC        | Insurance            | Single Stock  |            4 | 5.1%     | ₹31,524 | Active         |
| LGELEC     | Consumer Electronics | Single Stock  |            4 | 3.7%     | ₹22,854 | Active         |
| FEDBAN     | Banking              | Single Stock  |            4 | 2.5%     | ₹15,816 | Active         |
| ASHLEY     | Auto                 | Single Stock  |            4 | 2.5%     | ₹15,621 | Active         |
| TATCAP     | Financial Services   | Single Stock  |            4 | 2.4%     | ₹15,072 | Active         |
| GAIL       | Oil & Gas            | Single Stock  |            4 | 1.7%     | ₹10,266 | Active         |
| ONGC       | Oil & Gas            | Single Stock  |            4 | 1.4%     | ₹8,683  | Active         |
| PETLNG     | Oil & Gas            | Single Stock  |            4 | 0.7%     | ₹4,060  | ⚠️ Consolidate |
| TATPOW     | Power                | Single Stock  |            4 | 0.4%     | ₹2,760  | ⚠️ Consolidate |
| NIPNIT     | IT                   | Thematic ETF  |            4 | 0.4%     | ₹2,513  | ⚠️ Consolidate |
| KOTAKBKETF | Banking              | Thematic ETF  |            4 | 0.3%     | ₹1,729  | ⚠️ Consolidate |
| ICIPSE     | Commodities          | Commodity ETF |            3 | 6.7%     | ₹41,840 | ⚠️ Consolidate |
| BHAELE     | Defense              | Single Stock  |            3 | 4.9%     | ₹30,400 | ⚠️ Consolidate |
| TATGLO     | Consumption          | Single Stock  |            3 | 4.6%     | ₹28,800 | ⚠️ Consolidate |
| JSWENE     | Power                | Single Stock  |            3 | 4.0%     | ₹24,867 | ⚠️ Consolidate |
| NTPGRE     | Power                | Single Stock  |            3 | 2.1%     | ₹12,812 | ⚠️ Consolidate |
| JIOFIN     | Financial Services   | Single Stock  |            3 | 1.9%     | ₹11,543 | ⚠️ Consolidate |
| ENGIND     | Infrastructure       | Single Stock  |            3 | 1.0%     | ₹6,060  | ⚠️ Consolidate |
| SJVLIM     | Power                | Single Stock  |            3 | 0.8%     | ₹5,036  | ⚠️ Consolidate |
| HINPET     | Oil & Gas            | Single Stock  |            3 | 0.7%     | ₹4,606  | ⚠️ Consolidate |
| NHPC       | Power                | Single Stock  |            3 | 0.7%     | ₹4,042  | ⚠️ Consolidate |
| GUJPPL     | Infrastructure       | Single Stock  |            3 | 0.6%     | ₹3,433  | ⚠️ Consolidate |
| GUJGA      | Oil & Gas            | Single Stock  |            3 | 0.5%     | ₹2,808  | ⚠️ Consolidate |
| ICIGOL     | Commodities          | Commodity ETF |            2 | 5.1%     | ₹31,358 | ⚠️ Consolidate |
| IDECEL     | Telecom              | Single Stock  |            2 | 3.1%     | ₹19,200 | ⚠️ Consolidate |
| SEQSCI     | Pharma               | Single Stock  |            2 | 0.4%     | ₹2,350  | ⚠️ Consolidate |


### Portfolio Consolidation
Portfolio holds 34 positions versus target maximum of 15 (`config.max_open_positions`). The following 13 holdings are under 1.0% portfolio weight with conviction below 5 and are candidates for consolidation/exit:

| Symbol     | Sector         | Weight   |   Conviction | Shares to Exit            |
|:-----------|:---------------|:---------|-------------:|:--------------------------|
| KOTAKBKETF | Banking        | 0.3%     |            4 | Exit all 30 sh (~₹1,729)  |
| SEQSCI     | Pharma         | 0.4%     |            2 | Exit all 10 sh (~₹2,350)  |
| NIPNIT     | IT             | 0.4%     |            4 | Exit all 76 sh (~₹2,513)  |
| TATPOW     | Power          | 0.4%     |            4 | Exit all 8 sh (~₹2,760)   |
| GUJGA      | Oil & Gas      | 0.5%     |            3 | Exit all 7 sh (~₹2,808)   |
| GUJPPL     | Infrastructure | 0.6%     |            3 | Exit all 20 sh (~₹3,433)  |
| NHPC       | Power          | 0.7%     |            3 | Exit all 55 sh (~₹4,042)  |
| PETLNG     | Oil & Gas      | 0.7%     |            4 | Exit all 14 sh (~₹4,060)  |
| HDF250     | Broad Market   | 0.7%     |            4 | Exit all 24 sh (~₹4,318)  |
| MIR150     | Broad Market   | 0.7%     |            4 | Exit all 194 sh (~₹4,328) |
| HINPET     | Oil & Gas      | 0.7%     |            3 | Exit all 14 sh (~₹4,606)  |
| SJVLIM     | Power          | 0.8%     |            3 | Exit all 67 sh (~₹5,036)  |
| ENGIND     | Infrastructure | 1.0%     |            3 | Exit all 21 sh (~₹6,060)  |
### Tax Plan (FY 2026-27)

> [!NOTE]
> **Advisory Notice**: This tax plan is indicative and for planning purposes only. Tax parameters (STCG Rate: **20.0%**, LTCG Rate: **12.5%**, Section 112A LTCG Exemption: **₹125,000**) are configured in `config.py` (`stcg_rate`, `ltcg_rate`, `ltcg_exemption_limit`). Consult a chartered accountant for statutory tax filing.

#### Capital Gains Inventory (FIFO Matching)

| Metric                                | Amount      | Tax Rate        | Notes                                |
|:--------------------------------------|:------------|:----------------|:-------------------------------------|
| Realised STCG (FY 2026-27 so far)     | ₹0.00       | 20.0%           | Taxable on net short-term gains      |
| Realised LTCG (FY 2026-27 so far)     | ₹0.00       | 12.5%           | Subject to ₹125,000 annual exemption |
| Section 112A LTCG Exemption Remaining | ₹125,000.00 | 0.0%            | Limit: ₹125,000 per financial year   |
| Total Unrealised LTCG (> 365 days)    | ₹38,706.98  | 12.5%           | Open long-term profit inventory      |
| ⚡ Eligible Tax-Free LTCG to Harvest  | ₹38,706.98  | 0.0% (Zero Tax) | Can be booked tax-free before FY end |
| Total Unrealised STCG (≤ 365 days)    | ₹1,399.22   | 20.0%           | Short-term unrealised gains          |

#### Loss-Harvest Candidates (Offset Value)

The following positions carry unrealised capital losses that can be booked to offset taxable STCG/LTCG (Total potential offset: **₹147,957**, Tax savings potential: **₹20,752**):

| Symbol   |   Shares | CMP      | Avg Cost   | Loss Offset Value   | Term      | Potential Tax Saved   |
|:---------|---------:|:---------|:-----------|:--------------------|:----------|:----------------------|
| HDFBAN   |       75 | ₹714.00  | ₹1267.91   | ₹41,543             | LTCG/STCG | ₹5,250                |
| RELIND   |       74 | ₹1166.70 | ₹1627.08   | ₹34,068             | LTCG/STCG | ₹4,540                |
| WIPRO    |      170 | ₹169.00  | ₹304.31    | ₹23,003             | LTCG/STCG | ₹3,159                |
| LIC      |       45 | ₹394.05  | ₹895.05    | ₹22,545             | LTCG/STCG | ₹3,578                |
| ICIPSE   |      193 | ₹216.79  | ₹250.36    | ₹6,478              | STCG      | ₹1,296                |
| JSWENE   |       28 | ₹460.50  | ₹668.00    | ₹5,810              | LTCG      | ₹726                  |
| JIOFIN   |       28 | ₹217.80  | ₹344.38    | ₹3,544              | LTCG      | ₹443                  |
| ICIGOL   |      250 | ₹125.43  | ₹138.24    | ₹3,202              | STCG      | ₹640                  |
| ASHLEY   |       41 | ₹147.37  | ₹215.55    | ₹2,795              | LTCG      | ₹349                  |
| ICINIF   |       86 | ₹256.23  | ₹271.08    | ₹1,277              | STCG      | ₹255                  |

*Showing top 10 of 20 loss-harvest candidates.*


