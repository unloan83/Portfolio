# Measured probabilities from the repo's own price data (NIFTYBEES + 27 stocks, Jun 2017 – Oct 2026)

**Read this first: what these numbers are and are not.**
- Everything below is computed on **one ~9.4-year market path** (2017-06-01 → 2026-10-15, 2,313 NIFTYBEES sessions). It includes one crash (COVID 2020, −36%), a strong 2020–21 recovery, and a 2026 drawdown that has not recovered yet. A different 9 years could give quite different frequencies. The confidence intervals cover sampling noise *within this path*. They do not cover the risk that the next decade behaves differently.
- Data: `data/prices/adj/*.csv`, loaded with `hindcast/data.py::load_adjusted` (drops the NIFTYBEES 2019-12-19/20 bad prints at ~13 vs ~129). For single stocks, `apply_corporate_actions` was also applied with `data/corporate_actions.csv`. It back-adjusted only the RELIANCE 2023-07-21 demerger (×0.969) and the GUJENERGY 2026-07-02 demerger (×0.917). Every split and bonus was already adjusted. IDEA has three unexplained one-day moves (×1.36 on 2019-11-19, ×1.40 on 2020-02-19, ×0.65 on 2020-03-18). These look like real Vodafone-Idea volatility, and they were left in.
- NIFTYBEES is a price series of the ETF, so its returns are net of the ETF's expense ratio. There are no taxes or trading costs. Cash earns 0% unless a line says otherwise.
- Script (deterministic, seed 7, 2,000 bootstrap draws): `/tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/probs.py`. Full output: `/tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt`. Neither file is in the repo, and the scratchpad may not persist.
- **How overlapping windows are handled.** Daily-start rolling windows overlap heavily: a 3-year window shares about 99.9% of its days with the next one. Three types of interval are reported:
  - (a) **Wilson interval with effective n** = the number of non-overlapping windows the sample spans: 9.2 for 1y, 3.1 for 3y, 1.8 for 5y.
  - (b) **Moving-block bootstrap (MBB)** of the indicator series, with block length equal to the horizon. When every observation is identical (100%), this method collapses to a zero-width interval and is not informative.
  - (c) **Path-resampling CI**: a stationary bootstrap of daily log returns (mean block 63 days) builds 500 synthetic 9.4-year paths, and the statistic is recomputed on each. This asks how much the frequency could differ on a "similar" path. It understates crash clustering longer than a quarter.
  - For monthly conditional probabilities, an MBB over month pairs was used (block = 6 months). For the 200-DMA conditional outcomes, an MBB over days was used (block = 63 days).
- **Universe mismatch with the brief.** The brief mentions 30 stocks and a 34-name basket. The repo actually contains **27 individual stocks**; the other 9 files are ETFs or index proxies (NIFTYBEES, MIDCAPETF, HDFCSML250, GOLDIETF, SILVERIETF, ITBEES, BANKNIFTY1, NIFTYIETF, 537007.BO). 22 of the stocks have full history from 2017. The basket analysis therefore uses those 22 names, plus a variant with all 27 included as they list. **The stock universe is survivor- and selection-biased.** These are names in the user's current portfolio, chosen today and partly *because* of what they did. They are not a random draw of Indian stocks.

## 1. Nifty base rates: rolling 1/3/5-year windows, up days/months/years

### Takeaway
On this path, 1-year Nifty holding periods were positive about 86% of the time (realistic CI about 55–97%) and beat 6.5% p.a. about 64% of the time. **Every** 3-year and 5-year window was positive. However, only about 3 and about 2 independent 3y/5y windows exist, so "100%" carries a lower 95% bound of only about 30–50%. Days were up 54% of the time, months 59%, and all 8 full calendar years 2018–2025 were up.

### Cited Findings
- **Overall:** NIFTYBEES CAGR was 11.0% over 9.37 years (2017-06-01 → 2026-10-15). Annualised daily volatility was 14.9%. — [repo: data/prices/adj/NIFTYBEES.NS.csv via probs.py]
- **1-year windows** (2,061 daily starts, from 2017-06-01 to 2025-10-06):
  - P(return > 0) = **85.7%**. Wilson@n_eff 9.2: 53–97%. MBB(L=252): 78–97%. Path-resampling: 55–96%.
  - P(> 6.5% p.a.) = **64.1%**. Wilson: 34–86%. MBB: 52–84%. Path-resampling: 39–86%.
  - Worst −27.3% (start 2019-03-19, ending in the COVID crash). p10 −2.2%, median **10.4%**, p90 30.6%, best +83.7% (start 2020-03-23). — [repo: probs.py output]
- **3-year windows** (1,557 starts, 2017-06-01 → 2023-09-18):
  - P(ann. > 0) = **100%**. Wilson@n_eff 3.1: 44–100%. Path-resampling: 51–100%. The MBB is degenerate here.
  - P(> 6.5% p.a.) = **95.2%**. Wilson: 40–100%. Path-resampling: 21–100%.
  - Worst +4.4% p.a. (start 2017-06-02). p10 9.0%, median **14.7%**, p90 20.1%, best 31.6% p.a. (start 2020-03-23). — [repo: probs.py output]
- **5-year windows** (1,053 starts, 2017-06-01 → 2021-09-07):
  - P(> 0) = **100%**. P(> 6.5% p.a.) = **99.8%**. Wilson@n_eff 1.8: 32–100%. Path-resampling: 45–100% for >0 and 2–100% for >6.5%.
  - Worst +6.2% p.a. (start 2021-09-03). p10 10.8%, median **14.3%**, p90 18.9%, best 26.1% p.a. — [repo: probs.py output]
- **Up days:** 54.3% of 2,312 daily returns (Wilson 52–56%). Lag-1 autocorrelation of daily returns is 0.007, so days are close to independent and the plain Wilson interval is appropriate. — [repo: probs.py output]
- **Up months:** 58.9% of 112 calendar months (Wilson 50–68%). — [repo: probs.py output]
- **Calendar-year returns (%):**

  | 2017* | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026* |
  |---|---|---|---|---|---|---|---|---|---|
  | 10.4 | 4.8 | 13.6 | 15.4 | 26.0 | 5.5 | 21.0 | 10.4 | 11.7 | −11.4 |

  \*Partial years: 2017 from June, 2026 YTD to 15 Oct. Full years up: **8/8** (Wilson 68–100%). — [repo: probs.py output]

### Inferences
- The median 3y/5y windows (about 14–15% p.a.) are above the full-period CAGR of 11.0%. Windows starting in 2020–21 benefited from the post-COVID rebound, and the weak 2026 YTD only falls inside the 1y windows. Starting-point luck dominates these medians.
- "100% of 3/5-year windows were positive" is a statement about one path with about 2–3 independent observations. Treat the honest lower bound as about 30–50%, not about 99%.
- About 1 in 7 one-year holding periods lost money even in this fairly benign decade. About 1 in 3 failed to beat 6.5% (roughly a fixed-deposit or debt-fund hurdle, before tax).

### Gaps
- Only one path. Pre-2017 Nifty history (for example 2008, or the 2010–2013 flat period) is not in the repo, and that is where the 3y/5y loss probabilities would come from.
- NIFTYBEES dividend treatment depends on Yahoo's adjusted series. It was not checked against TRI.

## 2. Is volatility predictable? Is direction?

### Takeaway
Volatility clusters strongly. This month's realised vol explains about 37% of the variance of next month's log-vol (corr 0.57–0.61). Given an above-median-vol month, the next month is also above median about 68–75% of the time, against 50% unconditionally. Return direction does not persist in any usable way: monthly return autocorrelation is −0.04 (CI −0.20 to +0.16, R² 0.002), and P(up | prior month up) = 63% against an unconditional 58%.

### Cited Findings
- **Calendar-month realised vol (annualised), month t vs t+1:** Pearson **0.57** (MBB 95% CI 0.37–0.71). Log-vol correlation 0.61, Spearman 0.58, n = 111 pairs. — [repo: probs.py output]
- **Non-overlapping 21-session blocks:** vol corr(t, t+1) **0.53** (CI 0.30–0.70), n = 109. Rolling 21-day vol vs the next 21-day vol (daily steps): 0.53. — [repo: probs.py output]
- **High-vol persistence:**
  - P(next month vol > median | this month > median) = **67.9%** (n = 56, MBB 49–83%). P(high next | low now) = 32.7%. This uses the full-sample median, which carries a mild look-ahead.
  - With a no-look-ahead **expanding median** (state and outcome both judged against the median known at t): P(high next | high now) = **74.5%** (n = 55), against P(high next | low now) = 28.9%.
  - Top-quartile vol: P(next month top-quartile | this month top-quartile) = **60.7%** (n = 28, MBB 38–77%), against 25% unconditional. — [repo: probs.py output]
- **Direction persistence:** P(next month up | this month up) = **63.1%** (n = 65, MBB 54–75%). P(up | down) = 52.2%. Unconditional 58.0%. Monthly return autocorrelation −0.04 (CI −0.20 to 0.16). 21-day block return autocorrelation −0.06. — [repo: probs.py output]
- **R² comparison:** log-vol(t+1) on log-vol(t) R² = **0.37**. return(t+1) on return(t) R² = **0.002**. — [repo: probs.py output]
- **Vol as a return predictor:** the correlation of 21-day block vol with the next block's return is +0.19. High-vol blocks were followed by *better* returns on this path, mostly the post-March-2020 rebound. — [repo: probs.py output]

### Inferences
- Vol-targeting and position-sizing rules that use recent vol work on a measurable signal: risk tomorrow looks like risk today. Rules that use the last month's *direction* are close to a coin flip. The +5pp edge in P(up|up) sits inside its CI and is contradicted by the slightly negative autocorrelation.
- The +0.19 vol→next-return correlation is driven by one crash-and-rebound. Do not treat it as a rule.

### Gaps
- No intraday or implied-vol (India VIX) data in the repo, so implied-vs-realised comparisons are not possible.

## 3. Trend state: price above vs below the 200-day moving average

### Takeaway
On this path, being **below** the 200-DMA was followed by **better**, not worse, forward returns: mean next-63-day return +7.3% against +2.0% when above, and P(up) 85% against 62%. The difference is statistically clear on this sample (MBB diff CI −41 to −14pp). The probability of a ≥5% drawdown in the next 63 days was about the same in both states (60% below vs 56% above, CI on the difference −26 to +18pp). A 200-DMA in/out switch cut max drawdown from −36% to −17%, but CAGR fell from 11.0% to 6.9% (8.3% with 6% cash yield), across 73 switches.

### Cited Findings
- **Sample:** 2018-03-20 → 2026-07-15. The state is known at t's close and outcomes come strictly after t. Above 200-DMA on 1,599 days (78%), below on 452. 35 separate entries into the below state (heavy whipsaw). — [repo: probs.py output]
- **Next 21 days:**

  | State | Mean | Median | P(>0) | MBB CI for P(>0) | p10 | p90 |
  |---|---|---|---|---|---|---|
  | Above | 0.7% | 1.0% | 62.5% | 52–71% | −4.1% | 5.6% |
  | Below | 2.6% | 2.9% | 73.2% | 59–86% | −3.0% | 8.6% |

  CI on the P(>0) difference: −25 to +5pp, so it is not significant at 21 days. — [repo: probs.py output]
- **Next 63 days:**

  | State | Mean | Median | P(>0) | MBB CI for P(>0) | p10 | p90 |
  |---|---|---|---|---|---|---|
  | Above | 2.0% | 2.8% | 62.0% | 47–74% | −7.4% | 11.5% |
  | Below | 7.3% | 7.5% | 85.4% | 79–97% | −1.7% | 17.3% |

  CI on the P(>0) difference (above − below): −41 to −14pp. CI on the mean difference: −10 to −2pp. — [repo: probs.py output]
- **Max drawdown inside the next 63 days** (peak-to-trough within the window):

  | Drawdown | P(\| above) | MBB CI | P(\| below) | MBB CI | CI on difference |
  |---|---|---|---|---|---|
  | ≥5% | **56.3%** | 42–73% | **60.2%** | 42–79% | −26 to +18pp |
  | ≥10% | **18.7%** | 9–31% | **7.7%** | 1–19% | 0 to +22pp |

  Median 63-day max drawdown: −5.5% when above, −5.7% when below. — [repo: probs.py output]
- **Switching rule** (in Nifty if above the 200-DMA at the previous close, else cash; no costs):
  - CAGR **6.9%**, MDD **−16.7%**, against buy-and-hold 11.0% / −36.3%.
  - With cash at 6% p.a.: 8.3% / −15.0%.
  - 73 position changes. — [repo: probs.py output]
- **Best days fall in the below state:** 15 of the 20 best days occurred when Nifty was below its 200-DMA. — [repo: probs.py output]

### Inferences
- On this path, below-200-DMA states were mostly V-shaped dips (2018, 2019, 2020, 2022, 2025) that mean-reverted. That is why exiting below the line cost return. The drawdown-cutting benefit came mostly from sidestepping the second half of the COVID crash.
- Above-200-DMA states did not reduce the chance of a 5% drawdown. A ≥5% drawdown within any quarter happened more often than not in *both* states, about 56–60%. That is a base rate to expect, not a signal.
- Trend-following evidence from longer, multi-market samples may differ. This path has no prolonged bear market (like 2008), which is where 200-DMA rules usually earn their keep.

### Gaps
- Only about 35 below-state spells, highly clustered, so the effective sample is small. Costs and taxes on 73 switches (STCG on Indian equity) would cut the switch CAGR further, and they were not modelled.

## 4. Drawdown base rates

### Takeaway
In 9.4 years there were **6 Nifty drawdowns of ≥10%**, about one every 1.6 years. The last one (−14.8%, from the 2026-01-02 peak) is still unrecovered at −12.1% as of 2026-10-15. There was **one drawdown of ≥20%** (COVID, −36.3%). Completed ≥10% drawdowns took **157–391 calendar days** from peak to a new high. Nifty sat ≥10% below its prior peak on 12% of days, and ≥5% below on 38.5% of days.

### Cited Findings
Six ≥10% episodes (close-to-close, NIFTYBEES; td = trading days, cal = calendar days). — [repo: probs.py output]

| Peak | Trough | Depth | td peak→trough | td trough→recovery | cal peak→recovery | Recovered |
|---|---|---|---|---|---|---|
| 2018-08-28 | 2018-10-26 | −14.1% | 39 | 105 | 217 | 2019-04-02 |
| 2019-06-03 | 2019-09-19 | −10.5% | 73 | 32 | 157 | 2019-11-07 |
| 2020-01-17 | 2020-03-23 | **−36.3%** | 44 | 158 | 297 | 2020-11-09 |
| 2021-10-18 | 2022-06-17 | −16.1% | 166 | 99 | 389 | 2022-11-11 |
| 2024-09-27 | 2025-03-04 | −15.2% | 108 | 157 | 391 | 2025-10-23 |
| 2026-01-02 | 2026-03-30 | −14.8% | 58 | — | — | not yet (−12.1% on 2026-10-15) |

- **Time spent in drawdown:** 12.1% of sessions were ≥10% below the running peak. 38.5% were ≥5% below. — [repo: probs.py output]

### Inferences
- The base rate of a ≥10% fall in any given year on this path is high, roughly 6 in 9.4 years. Planning should assume one most years-and-a-half. Recoveries took 5–13 months, even after the 36% crash.
- The fast COVID recovery (under 10 months) is not typical of deep bear markets historically. With n = 1, the ≥20% recovery time should not be extrapolated.

### Gaps
- n = 1 for ≥20% drawdowns, so no probability can be estimated from this repo.

## 5. Single stocks vs the index (survivor-biased current-holdings universe)

### Takeaway
Over each stock's full available history, **12 of 27 (44%, Wilson 28–63%) beat NIFTYBEES**. Among the 22 names with full history, 10 of 22 (45%) did, with median excess CAGR −0.8pp. Over rolling 3-year windows, a stock beat Nifty in 56% of stock-windows, but the outcomes are extremely dispersed: the 3y excess CAGR runs from −20pp (p10) to +38pp (p90). 17.7% of single-stock 3y windows lost money in absolute terms, against 0% for Nifty. The median full-history stock suffered a −64% max drawdown, against Nifty's −36%.

### Cited Findings
- **Universe:** the 27 individual stocks in `data/prices/adj`. **Survivor-biased:** these are current holdings or watch names that still trade, chosen with hindsight. — [repo: data/prices/adj]
- **Full-history beat rate:**
  - All 27: **12/27 = 44.4%** beat (Wilson 28–63%). Median excess CAGR −1.3pp, IQR −3.8 to +5.1pp.
  - 22 full-history names: 10/22 = 45.5% beat. Median excess −0.8pp.
  - 24 names with ≥3y history: 10/24 = 41.7%. — [repo: probs.py output]
- **Full-history excess CAGR vs NIFTYBEES (pp), selected names:**
  - Best: BEL +14.8, JSWENERGY +14.2, TATACONSUM +12.5, TATAPOWER +7.6, RELIANCE +5.9.
  - Worst: IDEA −24.4, NTPCGREEN −12.5 (1.9y), JIOFIN −10.5 (3.2y), LICI −10.5 (4.4y), GPPL −4.8, HDFCBANK −3.6. — [repo: probs.py output]
- **Rolling 3-year windows** (34,701 stock-windows, 24 stocks):
  - P(stock beat Nifty) = **55.9%** pooled. 53.2% equal-weighted by stock (resampling stocks gives a CI of 45–62%).
  - Share of stocks beating Nifty at any one start date ranged from 27% to 83%. — [repo: probs.py output]
- **Per-stock share of 3y windows beating Nifty:**
  - Low: JIOFIN 0%, HDFCBANK 16%, IDEA 19%, PETRONET 31%.
  - High: JSWENERGY / TATAPOWER 85%, BEL 84%, TATACONSUM 78%. — [repo: probs.py output]
- **Dispersion of 3y excess CAGR:** p10 −19.8pp, p25 −10.4pp, median +3.3pp, p75 +19.0pp, p90 +38.1pp. P(excess < −10pp) = 25.7%. P(excess > +10pp) = 38.8%. — [repo: probs.py output]
- **Losses:** P(stock 3y CAGR < 0) = **17.7%**, against 0.0% for Nifty 3y windows. — [repo: probs.py output]
- **Drawdowns:** median full-history-stock MDD **−63.9%**; worst −95.8% (IDEA); mildest −33.0% (DRREDDY). 95.5% of full-history stocks (21/22) had a deeper MDD than Nifty's −36.3%. — [repo: probs.py output]

### Inferences
- The pooled 3y beat rate (56%) is *above* 50% only because this hindsight-selected list is tilted toward PSU, power and defence names that re-rated in 2021–24. Even so, fewer than half of the names beat the index over their full history, and the median name trailed slightly.
- With a truly random, survivor-free universe, beat rates would be expected to be lower. Published SPIVA-type studies are not in scope here.
- The decision-relevant fact is the spread: choosing one stock instead of the index changes a 3-year outcome by ±20–40pp in the tails. It roughly doubles the expected worst drawdown (−64% against −36%).

### Gaps
- No delisted or failed names, so true survivorship-free beat rates cannot be computed from the repo.
- The universe is not random (it is the user's portfolio), so the beat rates are not base rates for "a stock".

## 6. Diversification: equal-weight basket vs NIFTYBEES vs median stock

### Takeaway
An equal-weight, monthly-rebalanced basket of the 22 full-history stocks returned **16.1% CAGR** with a **−45.4% max drawdown** (vol 19.4%). NIFTYBEES returned 11.0% with −36.3% (vol 14.9%). The median single stock returned 10.2% with −63.9% (vol 34%). Diversifying across the names roughly halved volatility and cut the drawdown by about 18pp relative to the median stock. Because the basket is concentrated in high-beta PSU, energy and utility names, it still drew down further than the index.

### Cited Findings
- **Head-to-head:**

  | Portfolio | CAGR | MDD | Vol |
  |---|---|---|---|
  | EW basket, 22 full-history stocks | **16.1%** | **−45.4%** | 19.4% |
  | EW basket, all 27 stocks added as they list | 15.5% | −45.4% | 19.4% |
  | NIFTYBEES | 11.0% | −36.3% | 14.9% |
  | Median single stock (n = 22) | 10.2% | −63.9% | 34.2% |

  — [repo: probs.py output]
- **COVID crash** (2020-01-14 → 2020-03-31 peak-to-trough): basket −37.3%, Nifty −36.3%. — [repo: probs.py output]
- **Random equal-weight sub-baskets** (monthly rebalanced, drawn from the 22 full-history names; 300 draws per size; Nifty monthly-compounded CAGR 11.0%):

  | k | CAGR p10 / median / p90 | P(beat Nifty) | Median MDD | 10th-pct-worst MDD |
  |---|---|---|---|---|
  | 1 | 5.9 / 9.5 / 23.0% | 42.7% | −58% | −80% |
  | 3 | 10.0 / 15.0 / 19.4% | 83% | −40% | −62% |
  | 5 | 11.6 / 15.5 / 18.9% | 93% | −37% | −57% |
  | 10 | 13.4 / 15.5 / 17.6% | 100% | −39% | −50% |
  | 15 | 14.4 / 15.7 / 16.9% | 100% | −39% | −45% |

  — [repo: probs.py output]

### Inferences
- Moving from 1 to about 5 names removes most of the idiosyncratic risk: the worst-decile MDD goes from −80% to −57%, and the CAGR spread narrows from 17pp to 7pp. Beyond 10 names the gains are small.
- The basket's outperformance of Nifty comes from (i) a hindsight-selected universe (survivor and selection bias) and (ii) the rebalancing bonus across very volatile names. It should not be read as "equal-weighting these names beats the index going forward". The persistent finding is the *risk* reduction, not the return.

### Gaps
- No costs or taxes on the monthly rebalancing. No sector-matched comparison (for example a PSU or energy index) to separate factor tilt from diversification.

## 7. Missing the best (or worst) days

### Takeaway
Over 2017-06 → 2026-10, Nifty's 11.0% CAGR falls to **8.1% / 6.0% / 2.9%** if the 5 / 10 / 20 best days are missed (sitting in 0% cash). Missing the 5 / 10 / 20 worst days lifts it to 15.3% / 17.6% / 21.4%. The best and worst days cluster together: 12 of the 20 best days fell within 10 sessions of one of the 20 worst days, mostly March–April 2020. Missing both the best and the worst days leaves CAGR at about 12.3–12.5%, close to buy-and-hold.

### Cited Findings
- **CAGR when specific days are removed:**

  | Days missed | Best only | Worst only | Both |
  |---|---|---|---|
  | 5 | **8.1%** | **15.3%** | 12.3% |
  | 10 | **6.0%** | **17.6%** | 12.3% |
  | 20 | **2.9%** | **21.4%** | 12.5% |

  Full: 11.0% over 2,312 days. — [repo: probs.py output]
- **10 best days:** 2020-04-07 +6.7%, 2019-09-20 +5.3% (corporate tax cut), 2020-03-25 +5.2%, 2021-02-01 +4.4%, 2020-03-20 +3.9%, 2026-04-08 +3.9%, 2025-05-12 +3.9%, 2020-04-09 +3.7%, 2020-03-26 +3.6%, 2019-05-20 +3.6%. — [repo: probs.py output]
- **10 worst days:** 2020-03-23 −10.2%, 2020-03-12 −7.5%, 2020-03-19 −6.9%, 2020-05-04 −5.2%, 2020-03-09 −4.7%, 2020-03-16 −3.8%, 2022-02-24 −3.6%, 2021-02-26 −3.5%, 2020-02-28 −3.5%, 2020-05-18 −3.2%. — [repo: probs.py output]
- **Clustering:**
  - 12 of the 20 best days were within 10 sessions of one of the 20 worst days.
  - 15 of the 20 best days occurred while Nifty was below its 200-DMA. — [repo: probs.py output]

### Inferences
- "Missing the 10 best days halves your return" is true on this path: 11.0% becomes 6.0%. But it is a one-sided framing. Any exit rule that misses the best days probably also misses some of the worst, because they arrive in the same high-vol weeks (see §2 on vol clustering and §3 on the 200-DMA).
- The measurable lesson is narrower: being out of the market *during high-vol drawdowns* is when the asymmetry bites. The 200-DMA switch (§3) lost 4pp of CAGR mainly for this reason.

### Gaps
- Results depend heavily on a single episode (March–April 2020). Removing that one month would change all of these numbers materially. That sensitivity was not computed.

---

## Measured probability table

All figures come from NIFTYBEES and repo stocks, 2017-06 → 2026-10: one market path. 95% CIs account for overlap through effective-n Wilson intervals, block bootstrap, or path resampling, as labelled. No taxes or costs.

| Decision / claim | Measured probability (95% CI) | Horizon | Caveat |
|---|---|---|---|
| Nifty is up over a 1-year hold | **86%** (path-resample 55–96%; Wilson n_eff=9: 53–97%) | 1y, daily starts | 2,061 overlapping windows ≈ 9 independent |
| Nifty beats 6.5% p.a. over 1 year | **64%** (39–86%) | 1y | FD-like hurdle, pre-tax |
| Nifty is up over a 3-year hold | **100%** (Wilson n_eff=3: 44–100%; path 51–100%) | 3y | Only about 3 independent windows; worst was +4.4% p.a. |
| Nifty beats 6.5% p.a. over 3 years | **95%** (Wilson 40–100%; path 21–100%) | 3y | Same |
| Nifty is up / beats 6.5% over 5 years | **100% / 99.8%** (Wilson n_eff=1.8: 32–100%) | 5y | About 2 independent windows; essentially anecdote |
| Any given day is up | **54.3%** (52–56%) | 1 day | Days near-independent (autocorr 0.007) |
| Any given month is up | **58.9%** (50–68%) | 1 month | 112 months |
| A full calendar year is up | **8/8 = 100%** (68–100%) | 1 calendar year | 2018–2025; 2026 YTD is −11.4% |
| High vol persists: next month vol > median given this month > median | **68%** (MBB 49–83%); 74.5% with no-look-ahead expanding median | 1 month ahead | vs 50% base; vol corr 0.57 (0.37–0.71) |
| Top-quartile vol month is followed by another | **61%** (38–77%) | 1 month | vs 25% base; n=28 |
| Direction persists: next month up given this month up | **63%** (54–75%) | 1 month | vs 58% unconditional; return autocorr −0.04 (−0.20 to 0.16), so no usable edge |
| Next 63d return > 0 when Nifty is **above** its 200-DMA | **62%** (47–74%) | 63 sessions | State at t, outcome after t |
| Next 63d return > 0 when Nifty is **below** its 200-DMA | **85%** (79–97%) | 63 sessions | Below-state dips mean-reverted on this path; 35 short spells |
| ≥5% drawdown in next 63d, above 200-DMA | **56%** (42–73%) | 63 sessions | Not different from the below state (diff CI −26 to +18pp) |
| ≥5% drawdown in next 63d, below 200-DMA | **60%** (42–79%) | 63 sessions | Same |
| ≥10% drawdown in next 63d, above / below 200-DMA | **19%** (9–31%) / **8%** (1–19%) | 63 sessions | Small n of events |
| 200-DMA in/out switch beats buy-and-hold CAGR | **Did not** (6.9% vs 11.0%; MDD −16.7% vs −36.3%) | 2018–2026 | One path, no costs, 73 switches |
| ≥10% Nifty drawdown occurs | **6 in 9.4y** (≈0.64/yr) | Any year | Recovery 157–391 calendar days; current one is unrecovered |
| ≥20% Nifty drawdown occurs | **1 in 9.4y** | Any year | n=1 (COVID −36%, recovered in 297 days) |
| A held stock beats NIFTYBEES over its full history | **44%** (12/27; Wilson 28–63%) | 1–9.4y | Survivor- and hindsight-selected universe |
| A held stock beats NIFTYBEES over a 3-year window | **56%** pooled (by-stock 53%, 45–62%) | 3y rolling | Survivor-biased; excess spread p10 −20pp to p90 +38pp |
| A single stock loses money over 3 years | **17.7%** (vs 0% for Nifty) | 3y rolling | Survivor-biased, so understated |
| A single stock's max drawdown is worse than Nifty's | **95.5%** (21/22) | 2017–2026 | Median stock MDD −64% vs Nifty −36% |
| A random 5-stock EW basket beats Nifty | **93%** of draws | 9.4y | Reflects the hindsight-selected universe, not skill; MDD median −37% |
| A random 1-stock "basket" beats Nifty | **43%** of draws | 9.4y | Same universe |
| Missing the 10 best days | CAGR 11.0% → **6.0%** | 9.4y | 12/20 best days sit within 10 sessions of a worst day |
| Missing the 10 worst days | CAGR 11.0% → **17.6%** | 9.4y | Missing both: 12.3% |
