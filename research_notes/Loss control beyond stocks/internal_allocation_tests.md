# Internal allocation & loss-control tests (repo price cache, Indian ETFs)

Scope: can simple, pre-registered allocation and loss-control rules limit losses for an Indian ETF investor, judged only on the repo's committed daily adjusted prices? All numbers below are from deterministic scripts run on `data/prices/adj/*.csv` loaded via `hindcast/data.load_adjusted` (which dropped the two bad NIFTYBEES prints of 2019-12-19/20, closes ~13 vs median ~129). Scripts: `/tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/alloc.py` (simulator + tables) and `.../scratchpad/extra.py` (whipsaw, episodes, correlations, bootstrap). They are scratch files, not committed. Throughout, "Source: backtest" means output of those scripts on [NIFTYBEES.NS.csv](../../data/prices/adj/NIFTYBEES.NS.csv) / [GOLDIETF.NS.csv](../../data/prices/adj/GOLDIETF.NS.csv) / [SILVERIETF.NS.csv](../../data/prices/adj/SILVERIETF.NS.csv) and the other cached ETFs.

**Setup (fixed before running; every strategy is reported):**
- Data availability forced two windows, because the gold ETF starts **2023-12-12** (not 2017) and silver starts **2025-02-03**. Midcap 150 ETF starts 2024-06-19, smallcap 250 starts 2023-02-21 and ITBEES starts 2020-06-30. BANKNIFTY1 has an unexplained x0.10 move on 2026-02-27, so it was not used.
  - **Window A (equity + debt): 2017-06-01 to 2026-10-15 (9.37 yrs)**, NIFTYBEES only. Covers COVID 2020, 2022 and Sep 2024–Mar 2025.
  - **Window B (equity + debt + gold): 2023-12-12 to 2026-10-15 (2.84 yrs)**, the common window for gold mixes. Covers Sep 2024–Mar 2025 and the Q1 2026 fall only.
- Debt = **"debt proxy (assumed)"**, a constant 6.5% p.a. accrual compounded by calendar days. A 0% cash variant was also run. No debt ETF is cached.
- Mechanics: signals use data up to and including close t, and trades execute at close t+1. Costs are 0.1% one-way on every traded leg, including the debt leg (the cash leg is costless), with 0.25% as a sensitivity. The initial allocation carries no cost.
- Strategies:
  - **S1** 100% NIFTYBEES buy-and-hold.
  - **S2** static mixes, with annual rebalance (decided on the last session of the year) and with a 5pp band (any sleeve more than 5pp off target): 80/20 equity/debt, 60/30/10 equity/debt/gold, 50/30/20 equity/debt/gold, and 80/20 equity/gold.
  - **S3** 10-month SMA filter (210 sessions) on NIFTYBEES, checked at month-end close, switching 100% to debt when below. A variant needs 2 consecutive month-ends to flip. During the SMA warm-up it stays invested.
  - **S4** 60/30/10 with the same filter applied separately to the equity and gold sleeves; a sleeve that is off goes to debt. Band rebalancing applies to the current target. The gold SMA is warm only from about Oct 2024.
  - **S5** volatility targeting: equity weight = min(1, 15% / 63-day realised vol), set at month-end, with the remainder in debt.
  - **S6** drawdown rule: if the portfolio falls more than 15% below its own high-water mark (HWM), cut equity to 50% (re-trimmed if it drifts more than 5pp). Return to 100% once within 5% of the HWM.
- Metrics: CAGR; volatility (daily std ×√252); MaxDD; worst rolling 252-session return (W12); recovery = days from trough back to the prior peak, with "underwater" = peak to recovery; Calmar = CAGR/|MaxDD|; turnover/yr = Σ|Δw|/2 per year, where a full switch counts as 1.0; risky-sell events/yr. Sub-period figures slice the full-run equity curve, so strategy state is carried in.

## Q1. Which approaches materially cut max drawdown and worst-12-month loss, and at what CAGR cost?

### Takeaway
Over 9.4 years of Nifty, only the 1-month 10-month-SMA trend filter roughly halved the max drawdown (-14% vs -36%) at little CAGR cost (-0.3pp). That result rests on one well-timed exit in March 2020; most of its other exits lost money. A static 80/20 equity/debt mix reliably shaved about 7pp off MaxDD and about 7pp off the worst-12m loss, at a cost of about 0.6–0.9pp CAGR (about 2pp with 0% cash). Volatility targeting, the 2-month-confirm trend filter and the drawdown rule gave up 2–5pp CAGR and did not cut MaxDD versus 80/20.

### Cited Findings
**Window A, full period 2017-06-01 to 2026-10-15** (debt 6.5%, cost 0.1%):

| Strategy | CAGR | Vol | MaxDD (peak→trough) | Recovery / underwater (days) | Worst 12m | Calmar | Turnover/yr | Trades/yr |
|---|---|---|---|---|---|---|---|---|
| S1 B&H Nifty | 11.0% | 14.8% | -36.3% (2020-01-17→03-23) | 231 / 297 | -28.3% | 0.30 | 0 | 0 |
| S2 80/20 eq/debt, annual | 10.2% | 11.6% | -28.9% | 228 / 294 | -21.1% | 0.35 | 1% | 0.96 |
| S2 80/20 eq/debt, band 5pp | 10.4% | 12.0% | -29.6% | 205 / 271 | -21.7% | 0.35 | 2% | 0.32 |
| S3 SMA210 trend (1 mo) | 10.7% | 11.2% | -14.1% (2018-08-28→10-26) | 741 / 800 | -10.4% | 0.76 | 139% | 1.39 |
| S3 SMA210 trend (2 mo confirm) | 6.2% | 13.2% | -36.3% | 504 / 570 | -28.7% | 0.17 | 75% | 0.75 |
| S5 Vol target 15% | 8.8% | 13.7% | -36.3% | 295 / 361 | -28.5% | 0.24 | 39% | 4.16 |
| S6 DD rule (-15%→50% eq) | 8.3% | 12.1% | -28.9% | 280 / 346 | -21.4% | 0.29 | 38% | 1.07 |

Source: backtest ([NIFTYBEES.NS.csv](../../data/prices/adj/NIFTYBEES.NS.csv)).

- **0% cash variant (Window A):** 80/20 annual 8.9% CAGR / -29.1% MaxDD; S3 1-mo 9.5% / -14.3% (W12 -11.5%); S5 8.5%; S6 7.4%. With 0% cash, every defensive rule falls 1.2–1.5pp further behind B&H's 11.0%. — Source: backtest
- **Cost sensitivity (0.25% one-way):** S3 1-mo CAGR falls from 10.7% to 10.2% (about 0.5pp, because of 139% turnover/yr). Static mixes and S5/S6 move by 0.1pp or less. — Source: backtest
- **Sub-periods (debt 6.5%, cost 0.1%), shown as CAGR / MaxDD / W12:**
  - 2017-06 to 2020-12:
    - S1: 12.4% / -36.3% / -28.3%
    - 80/20 annual: 11.2% / -28.9% / -21.1%
    - S3 1-mo: 10.7% / -14.1% / -10.4%
    - S3 2-mo: 3.6% / -36.3% / -28.7%
    - S5: 7.0% / -36.3% / -28.5%
    - S6: 8.7% / -28.9% / -21.4%
  - 2021-2023:
    - S1: 17.1% / -16.1% / -4.4%
    - 80/20: 15.0% / -12.3% / -2.4%
    - S3 1-mo: 13.9% / -13.8% / -8.4%
    - S3 2-mo: 13.1% / -16.6% / -13.9%
    - S5: 16.7% / -14.0% / -4.2%
    - S6: 14.4% / -16.2% / -9.1%
  - 2024-01 to 2026-10-15:
    - S1: 3.1% / -15.2% / -9.8%
    - 80/20: 3.8% / -12.0% / -6.4%
    - S3 1-mo: 7.1% / -10.5% / -4.9%
    - S3 2-mo: 2.2% / -16.6% / -9.3%
    - S5: 2.9% / -15.2% / -10.1%
    - S6: 1.5% / -16.9% / -8.1%
  - Source: backtest
- **Recovery cost of the trend filter:** S3 1-mo's own maximum drawdown (-14.1%, Aug–Oct 2018) occurred *before* the month-end exit signal. The 1 Nov 2018 exit and the Sep 2019 exit were then whipsawed, so the strategy needed 741 days to regain its Aug 2018 peak, versus 231 days for B&H's (deeper) COVID drawdown. — Source: backtest
- **Window B (gold window 2023-12-12 to 2026-10-15), all strategies, as CAGR / Vol / MaxDD / W12 / Calmar / turnover per year:**
  - S1 B&H: 4.5% / 12.2% / -15.2% / -9.4% / 0.29 / 0
  - 80/20 eq/debt: annual 5.0% / 9.7% / -12.0% / -6.1% / 0.41; band 4.9% / -12.1%
  - 60/30/10 eq/debt/gold: annual 8.3% / 8.1% / -9.6% / -0.8% / 0.87 / 2%; band 8.4% / -9.9%
  - 50/30/20 eq/debt/gold: annual 11.4% / 8.5% / -11.5% / +2.2% / 0.99 / 4%; band 11.3% / -11.4%
  - 80/20 eq/gold: annual 10.7% / 11.7% / -15.0% / -2.6% / 0.71; band 10.5% / -14.8%
  - S3 1-mo: 8.4% / 8.9% / -10.5% / -4.9% / 0.80 / 106%
  - S3 2-mo: 3.6% / 9.7% / -16.6% / -9.3% / 0.22
  - S4 60/30/10 + sleeve trend: **10.5% / 6.0% / -6.3% / +3.2% / 1.68 / 75%** (2.46 trades/yr, 2.1 risky-sell events/yr)
  - S4 with 2-mo confirm: 7.7% / 6.7% / -9.4% / +0.7% / 0.82
  - S5: 4.3% / 12.0% / -15.2%
  - S6: 2.9% / 9.7% / -16.9%
  - With 0% cash: 60/30/10 6.4%, 50/30/20 9.5%, S4 7.2%.
  - Source: backtest ([GOLDIETF.NS.csv](../../data/prices/adj/GOLDIETF.NS.csv))
- **Path dependence of the drawdown rule (S6):**
  - In 2020 it cut on 2020-03-12, at -15% from the HWM, and the crash continued to the 03-23 trough. It saved about 7pp of MaxDD (-28.9% vs -36.3%) but re-risked only on 2020-12-03. COVID-year return was +1.2% vs B&H +13.8%.
  - In 2025 it cut on **2025-03-04, the exact Nifty trough**, and stayed at 50% until 2025-11-28. The Sep 2024–Mar 2025 episode return was -12.3% vs B&H -9.7%.
  - Because it measures against its *own* HWM, it re-risked after recovering to within 5% and then fell again in 2026 (cut 2026-03-16). Its MaxDD of -16.9% from 2024-09-27 to 2026-03-30 is *worse* than B&H's -15.2%.
  - The same rule with 0% cash followed a different path (fewer trades: 0.35 vs 1.06 per year in Window B). Small parameter or data changes flip outcomes.
  - Source: backtest

### Inferences
- "Material" loss reduction that survives across sub-periods came only from **holding less equity** (static debt/gold sleeves). The trend filter's large full-period MaxDD cut is real in this sample but comes from one or two episodes. In 2021–2023 it had a worse W12 (-8.4%) and lower CAGR than B&H.
- Vol targeting at a 15% target barely bites on Nifty, whose realised vol is usually below 15%. It was fully invested going into Feb 2020, when pre-crash vol was low, then under-invested in the recovery. That is the classic failure mode for a fast crash.
- A portfolio-HWM drawdown rule sells after the loss has happened and re-buys late. In this sample it behaved as a CAGR drag, not a loss limiter.

### Gaps
- Only one market path. Window A has a single deep crash (COVID), and Window B is under 3 years. No 2008-style prolonged bear market is in the cache.
- The debt proxy is a constant 6.5%. Real debt funds had mark-to-market losses (e.g., when rates rose in 2022) that are not captured, and no debt ETF price series is cached.

## Q2. How many whipsaw switches did trend filters make, and did they help in COVID-2020 (V-shaped) vs Sep 2024–Mar 2025?

### Takeaway
The 1-month SMA filter made 13 switches in 9.4 years (7 exits). Five of the 7 exits cost 0.2–4.5% versus staying invested. It helped strongly in COVID (+18.6% vs +13.8% for the 2020 calendar, MaxDD -9.9% vs -36.3%) and in 2026 (still out; +12.1pp vs staying so far), but only slightly in Sep 2024–Mar 2025. The 2-month-confirm variant was the worst rule tested: it exited after the COVID bottom and missed a +36.7% rebound.

### Cited Findings
- **S3 1-mo round trips** (exit date → re-entry date, Nifty move while out, net effect vs staying including the debt accrual):
  - 2018-11-01→2018-12-03: +4.7%, net **-4.0%**
  - 2019-09-03→2019-10-01: +5.2%, net **-4.5%**
  - 2020-03-02→2020-08-03: -1.9%, net **+4.7%**
  - 2022-06-01→2022-08-01: +5.0%, net **-3.8%**
  - 2023-04-03→2023-05-02: +4.1%, net **-3.5%**
  - 2025-01-01→2025-05-02: +2.3%, net **-0.2%**
  - 2026-03-02→still out at 2026-10-15: -7.2%, net **+12.1%**
  - Four round trips lasted 28–61 days (classic whipsaws). — Source: backtest
- **S3 2-mo confirm round trips:**
  - 2020-04-01→2020-09-01: Nifty +36.7% while out, net **-24.9%**
  - 2022-07-01→2022-09-01: net -9.6%
  - 2025-02-01→2025-06-02: net -3.6%
  - 2026-04-01→still out: net +1.9%
  - Source: backtest
- **COVID episode (2020-01-14 to 2020-12-31):**

  | Strategy | 2020 return | MaxDD |
  |---|---|---|
  | B&H | +13.8% | -36.3% |
  | 80/20 | +12.3% | -28.9% |
  | S3 1-mo | **+18.6%** | **-9.9%** |
  | S3 2-mo | -14.9% | -36.3% |
  | S5 | -3.4% | -36.3% |
  | S6 | +1.2% | -28.9% |

  Crash leg only (2020-01-14 to 2020-06-30): B&H -16.4%, S3 1-mo -7.9%, S3 2-mo -30.9%, S5 -26.1%, S6 -17.4%. — Source: backtest
- **Sep 2024–Mar 2025 (2024-09-26 to 2025-03-28):**

  | Strategy | Return | MaxDD |
  |---|---|---|
  | B&H | -9.7% | -15.2% |
  | 80/20 | -7.4% | -12.0% |
  | S3 1-mo | -7.7% | -10.5% |
  | S3 2-mo | -9.4% | -12.4% |
  | S5 | -9.7% | -15.2% |
  | S6 | -12.3% | -15.3% |

  Extended to 2025-06-30, after the rebound, S3 1-mo was -2.3% vs B&H -1.7%: the benefit fully reversed because re-entry came on 2025-05-02. The Nifty peak was 2024-09-27, but the filter exited only on 2025-01-01, after most of the fall. — Source: backtest
- **2026 (Nifty peak 2026-01-02, trough 2026-03-30, -14.8%):** S3 1-mo exited on 2026-03-02. Its 2026-to-date return is -0.9% vs B&H -11.5%, with 2026 MaxDD -5.4% vs -14.8%. The outcome is still open, and an unrealised whipsaw is possible if the market rebounds. — Source: backtest
- **Tax exposure (not modelled):**
  - S3 1-mo made 0.75 equity sell events/yr. By holding period, 4 of its 7 equity exits sold units held under 12 months (2019-09, 2020-03, 2023-04, 2026-03), which would be short-term gains or losses. — Source: backtest
  - Risky-sell events/yr in Window B: S4 2.1, S5 1.1, 60/30/10 band 0.7. — Source: backtest
  - Listed-equity STCG under section 111A rose from 15% to 20% for transfers on or after 23 July 2024; LTCG under 112A is 12.5% above ₹1.25 lakh, with the 12-month holding threshold unchanged. — [Business Standard](https://www.business-standard.com/amp/finance/personal-finance/budget-2024-all-the-key-changes-to-capital-gains-tax-explained-124072500330_1.html); [freefincal ready reckoner](https://freefincal.com/?p=216021)

### Inferences
- In this sample the 10-month SMA filter's edge comes from two episodes, COVID 2020 and Mar 2026, in which the exit happened before the deepest losses. Its routine cost is about 4% per whipsaw, roughly once every 1.5 years.
- Sharp V-shaped crashes punish slower confirmation. Adding a 2-month confirmation to "reduce whipsaw" turned a helpful rule into a harmful one in 2020, so the rule is fragile to its own parameters.
- In the Sep 2024–Mar 2025 grind lower, the monthly SMA signal came too late to cut much loss, and the static 80/20 mix did about as well.

### Gaps
- With 7 exits, the sample is too small to estimate a whipsaw rate with any confidence. No other SMA lengths were tested, to avoid data-mining; parameter sensitivity therefore remains unmeasured.

## Q3. Did gold reduce drawdowns in these episodes?

### Takeaway
Gold was a strong diversifier in Sep 2024–Mar 2025: it rose +13.7% while Nifty fell -15.1% to its trough, and a 10–20% gold sleeve cut that episode's drawdown from -15% to -5.5% to -7.5%. In Q1 2026, however, gold crashed 26% (2026-01-29 to 03-23) during an 11% Nifty fall, so mixes holding it still drew down 10–15%. Gold's 34.6% CAGR in this window inflates every gold-mix return figure. COVID 2020 cannot be tested because there is no gold data before 2023-12.

### Cited Findings
- **Sep 2024–Mar 2025 (2024-09-26 to 2025-03-04):**

  | Asset | Return | MaxDD |
  |---|---|---|
  | GOLDIETF | **+13.7%** | -7.7% |
  | NIFTYBEES | -15.1% | -15.2% |
  | MIDCAPETF | -20.4% | -20.5% |
  | HDFCSML250 | -24.6% | -25.7% |
  | ITBEES | -10.5% | -18.7% |

  Source: backtest ([MIDCAPETF.NS.csv](../../data/prices/adj/MIDCAPETF.NS.csv), [HDFCSML250.NS.csv](../../data/prices/adj/HDFCSML250.NS.csv))
- **Portfolio results for the same episode (to 2025-03-28)**, return (MaxDD):
  - 60/30/10: -3.7% (-7.5%)
  - 50/30/20: -1.1% (-5.5%)
  - 80/20 eq/gold: -4.8% (-9.9%)
  - 80/20 eq/debt: -7.4% (-12.0%)
  - B&H: -9.7% (-15.2%)
  - Source: backtest
- **Q1 2026:**
  - From 2026-01-29 to 2026-03-23, gold fell -26.0% and silver -45.4% while Nifty fell -11.2%. That includes a single-day GOLDIETF drop of about 11% (139.6 → 124.2) on 2026-02-02 after a spike to 153.3 on 01-29.
  - Over calendar Q1 2026, gold was still +9.5% vs Nifty -14.2%.
  - 2026-to-date MaxDD: 60/30/10 -9.6%, 50/30/20 -11.5%, 80/20 eq/gold -15.0% (no better than Nifty's -14.8%), 80/20 eq/debt -11.6%. The window-B MaxDD of every gold mix comes from this 2026 episode.
  - Source: backtest ([SILVERIETF.NS.csv](../../data/prices/adj/SILVERIETF.NS.csv))
- **Correlation, 2023-12-12 to 2026-10-15:** daily Nifty/gold 0.18, weekly about 0.0, silver/gold 0.83, silver/Nifty 0.25. — Source: backtest
- **Standalone stats over each ETF's history in the cache:**
  - GOLDIETF: 34.6% CAGR, 22.8% vol, MaxDD -26.0%, worst 12m +20.4%
  - SILVERIETF: 58.8% CAGR, 47.3% vol, MaxDD -45.4%, since 2025-02
  - Source: backtest

### Inferences
- Gold's low correlation is real in this short sample. However, much of the gold mixes' CAGR advantage over B&H (+4 to +7pp/yr) is gold's exceptional 2024–2026 rally, not diversification, and should not be extrapolated.
- Gold can fall sharply at the same time as equity (Q1 2026). A sleeve of at most 10–20% kept the joint drawdown tolerable. Silver behaves like a leveraged gold bet (vol 47%, MaxDD -45%) and is unsuitable as a loss-control sleeve.

### Gaps
- There is no cached gold price for 2017–2023, so gold's behaviour in COVID 2020 (and in 2018 and 2022) cannot be tested internally. A longer gold series (e.g., GOLDBEES or the domestic gold price) would be needed. Silver's history (about 20 months) is too short for any conclusion.

## Q4. Block-bootstrap confidence intervals on CAGR difference vs buy-and-hold

### Takeaway
No strategy's CAGR difference from B&H is statistically distinguishable from zero. The drawdown reduction is robust only for static debt and gold mixes: 80/20 eq/debt was shallower than B&H in 100% of resamples. The trend filter's MaxDD benefit is likely but not certain (74–91%). The drawdown rule's CAGR cost was significant in the realised-path resampling (P(diff>0) = 0.04).

### Cited Findings
- **Method 1 (paired, circular block bootstrap of realised daily strategy and B&H returns; block 63, 5,000 reps, seed 42).** CAGR difference vs B&H [2.5%, median, 97.5%], P(diff>0); MaxDD improvement (positive = shallower) median, P(shallower):

  | Window | Strategy | Observed CAGR diff | CI [2.5%, median, 97.5%] | P(diff>0) | MaxDD gain (median) | P(shallower) |
  |---|---|---|---|---|---|---|
  | A | S3 1-mo trend | -0.35pp | [-7.7, -0.5, +6.8]pp | 0.44 | +16.1pp | 0.91 |
  | A | 80/20 eq/debt band | -0.63pp | [-3.0, -0.7, +1.7]pp | 0.29 | +6.8pp (CI 3.0–10.9) | 1.00 |
  | A | S6 DD rule | -2.75pp | [-6.5, -2.7, +0.3]pp | 0.04 | +4.8pp | 0.85 |
  | B | S4 60/30/10 + trend | +6.2pp | [-4.1, +6.2, +15.4]pp | 0.88 | +11.5pp | 1.00 |
  | B | 50/30/20 annual | +7.1pp | [-1.9, +7.0, +15.0]pp | 0.94 | — | 1.00 |
  | B | 60/30/10 band | +4.0pp | [-2.4, +4.0, +9.5]pp | 0.89 | — | 1.00 |
  | B | S3 1-mo trend | +4.1pp | [-4.2, +4.0, +12.0]pp | 0.83 | — | 0.97 |

  Source: backtest
- **Method 2 (synthetic Nifty paths from a block-63 bootstrap, seed 7, 500 reps, with the strategy re-run on each path so signals respond to the resampled prices).** Median CAGR diff [95% CI], P(diff>0); MaxDD improvement median, P(shallower); worst-12m P(better):

  | Strategy | Median CAGR diff [95% CI] | P(diff>0) | MaxDD gain (median) | P(shallower) | Worst-12m P(better) |
  |---|---|---|---|---|---|
  | S3 1-mo | -1.7pp [-6.1, +5.0] | 0.28 | +4.2pp | 0.74 | 0.63 |
  | S3 2-mo | -1.6pp | 0.25 | +0.9pp | 0.63 | 0.62 |
  | S5 | -0.7pp | 0.15 | +0.4pp | 0.69 | 0.59 |
  | S6 | -0.4pp | 0.38 | +8.9pp | 0.97 | 0.88 |
  | 80/20 band | -0.67pp | 0.28 | +6.7pp | 1.00 | 1.00 |

  Source: backtest

### Inferences
- The robust, model-independent statement is: **holding 20% in debt costs about 0.7pp CAGR and buys about 7pp less MaxDD and about 6pp better worst-12m, with near certainty.** Trend filters offer a larger but much less reliable drawdown cut, with a likely CAGR cost of about 1–2pp outside this specific path.
- Method 2 is biased against trend rules, because 63-day blocks break trends longer than about 3 months. Method 1 keeps the realised timing but not the path dependence of signals. The truth for S3 probably lies between the two.
- The Window-B CIs are very wide (only about 11 independent 63-day blocks) and are dominated by gold's rally.

### Gaps
- The bootstrap cannot create regimes absent from the sample (e.g., a long 2008-style bear market or a debt-market sell-off), and it ignores tax.

## Implications for the repo
- **Worth implementing as an advisory module:** a *strategic allocation and rebalancing advisor*. It would set target sleeves (e.g., 60/30/10 equity/debt/gold, the mix tested here; other splits are untested) and flag a rebalance when any sleeve drifts more than 5pp, or once a year. In Window B, band rebalancing traded 0–0.7 times/yr with turnover of 4% or less. This is the only loss-control lever that cut MaxDD and worst-12m in every sub-period and in 100% of bootstrap resamples, at a small and transparent CAGR cost. Its outputs should show the expected trade-off (about -0.7pp CAGR per 20% moved to debt) rather than promise loss avoidance.
- **Optional, clearly labelled "risk signal", not an auto-switch:** a month-end 10-month SMA status for Nifty and gold (above/below, days since cross). It is useful as context, and partial de-risking (e.g., cutting equity by a fixed fraction) is less tax- and whipsaw-exposed than a 100% switch. Any output must disclose that the rule whipsawed in 5 of 7 exits here, that 4 of 7 exits would have realised short-term gains (20% STCG post-July 2024), and that a 2-month confirmation variant was much worse. A full in/out switch should not be presented as validated.
- **Not worth implementing on this evidence:** a 15% vol-target overlay (barely active on Nifty; lagged into COVID) and a portfolio-HWM drawdown stop (sold at the 2020 crash and the 2025 trough, re-risked late, ended with a deeper MaxDD in 2024–26; strongly path-dependent).
- **Data work before any of this ships:**
  1. Cache a debt-fund or liquid ETF series (e.g., a liquid or gilt ETF) to replace the 6.5% proxy.
  2. Cache a longer gold history (e.g., GOLDBEES, which has a longer listing history than GOLDIETF; its start date was not checked here) so gold can be tested in 2018/2020/2022.
  3. Repair or ignore BANKNIFTY1 (unexplained x0.10 jump on 2026-02-27).
  4. Keep reporting results over both windows, and with the 0% cash variant, so gold's 2024–26 rally does not drive conclusions.
