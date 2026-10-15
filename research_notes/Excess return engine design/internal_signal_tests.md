# Internal signal tests: do simple price signals pick winners inside the 34-name portfolio universe?

Sources used throughout (all local, nothing fetched from the network):
- Test script: [signal_tests.py](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/signal_tests.py), output [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)
- Placebo, calendar-year and stocks-only add-on: [addon.py](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/addon.py), output [addon_out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/addon_out.txt)
- Data: `data/prices/adj/*.csv` loaded through `hindcast/run.py::load_universe` (repo commit `4f47ccb`), which applies the repo's ticker stitching and corporate-action repair — [repo: hindcast/data.py](file:///home/user/Portfolio/hindcast/data.py), [repo: hindcast/run.py](file:///home/user/Portfolio/hindcast/run.py)
- Prior result: [repo: reports/hindcast_summary.md](file:///home/user/Portfolio/reports/hindcast_summary.md)

## Q1. Do the signals have cross-sectional rank IC against forward 1/3/6/12-month returns?

### Takeaway
Only 6-1 month momentum shows a meaningful full-period rank IC (about +0.09 at 3 and 6 months, NW t 2.5 to 2.7). 12-1 momentum and its volatility-adjusted version are positive but weak (IC about +0.055, t 1.1 to 1.9). 52-week-high proximity is borderline (+0.06 at 6 months, t 1.8). Low volatility and 1-month reversal show nothing, and reversal turns slightly negative at 6 months. Even the momentum edge comes almost entirely from 2018–2022.

### Cited Findings

**Method (point-in-time, no look-ahead)**
- Universe = the 34 symbols in `portfolio.csv`, loaded with the repo's own loader. A name enters the cross-section on a signal date only if it has at least 253 sessions of history and a close on that date. That gives 24 eligible names from 2018 through 2021, 25 to 26 in 2022–2024 and 29 to 31 in 2025–2026 (min 24, max 32). Ten of the 34 (GOLDIETF, HDFCSML250, ITBEES, JIOFIN, LGEINDIA, LICI, MIDCAPETF, NTPCGREEN, SILVERIETF, TATACAP) list after 2017, so for most of the sample this is a 24-name test — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)
- Signal date t = last trading day of each month on the NIFTYBEES calendar, from 2018-06-29 (the first date with 24 or more eligible names), 101 dates in all. Signals use closes at or before t. Forward returns and portfolio trades start at the close of t+1, so execution is next-day — [signal_tests.py](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/signal_tests.py)
- Signal definitions: MOM12_1 = P(t−21)/P(t−252) − 1 (Jegadeesh-Titman style, skipping the last month — [Jegadeesh & Titman 1993](https://doi.org/10.1111/j.1540-6261.1993.tb04702.x)); MOM6_1 = P(t−21)/P(t−126) − 1; VAMOM12_1 = MOM12_1 / 252-day annualised volatility; HIGH52W = P(t)/max(P over 252 days) ([George & Hwang 2004](https://doi.org/10.1111/j.1540-6261.2004.00695.x)); LOWVOL1Y = −252-day volatility (in the spirit of [Ang, Hodrick, Xing & Zhang 2006](https://doi.org/10.1111/j.1540-6261.2006.00836.x)); REV1M = −(P(t)/P(t−21) − 1).
- IC = per-month Spearman correlation between the signal and the forward return over h = 21/63/126/252 sessions. The t-statistic uses Newey-West with ceil(h/21) lags to allow for overlapping windows — [signal_tests.py](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/signal_tests.py)

**Full-period IC, all eligible names (mean IC / NW t / share of months with IC > 0)** — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)

| Signal | 21d | 63d | 126d | 252d |
|---|---|---|---|---|
| MOM12_1 | 0.026 / 1.00 / 56% | 0.054 / 1.39 / 66% | 0.057 / 1.11 / 63% | 0.003 / 0.05 / 59% |
| MOM6_1 | 0.045 / 1.75 / 57% | **0.088 / 2.73 / 67%** | **0.090 / 2.49 / 68%** | 0.070 / 1.58 / 71% |
| VAMOM12_1 | 0.031 / 1.35 / 58% | 0.059 / 1.88 / 66% | 0.055 / 1.47 / 62% | 0.002 / 0.04 / 56% |
| HIGH52W | 0.008 / 0.31 / 57% | 0.031 / 1.00 / 58% | 0.060 / 1.84 / 61% | 0.038 / 0.93 / 61% |
| LOWVOL1Y | 0.015 / 0.55 / 47% | 0.002 / 0.04 / 53% | −0.010 / −0.14 / 52% | −0.050 / −0.63 / 47% |
| REV1M | 0.021 / 0.84 / 57% | −0.005 / −0.23 / 46% | −0.035 / −1.67 / 42% | −0.025 / −1.18 / 49% |

Months used: 99 / 97 / 94 / 88 for the four horizons.

- With the 7 ETFs removed (ICINIF, KOTAKBKETF, ITBEES, HDFCSML250, MIDCAPETF, GOLDIETF, SILVERIETF), MOM6_1 gets slightly stronger: IC 0.096 at 63d (t 2.97) and 0.096 at 126d (t 2.88). The other signals barely move. LOWVOL1Y stays at zero and HIGH52W at 126d is 0.067 (t 2.00) — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)

### Inferences
- An IC of about 0.09 is a typical size for momentum in large universes, but with 24 to 31 names a single month's IC carries a standard error of about 0.2, so the result rests on roughly 97 noisy monthly draws that are not independent of each other.
- Six signals × four horizons = 24 IC tests. Seeing one or two with |t| > 2.5 is not much more than chance would produce, so the MOM6_1 result should be treated as a lead to check, not a finding.
- Short-term reversal, which is a known effect in individual US stocks, is not present here. At 6 months it even has the momentum sign (IC −0.035, t −1.7, where negative means past 1-month losers keep lagging).

### Gaps
- No sector-neutral IC: the universe is too small to demean by sector (the Power sector alone has 6 names, Oil & Gas 6).
- Only one rebalance day per month was tested (month-end). The effect of shifting the trading day was not measured.

## Q2. Do monthly long-only top-N portfolios beat equal-weight-all and NIFTYBEES?

### Takeaway
Momentum books (especially MOM6_1) beat equal-weighting all 34 names by about 2 to 4%/yr net over 2018-07 to 2026-10. They rank at the 99th to 100th percentile of random-selection books with the same N and buffer. Only one variant has a bootstrap CI that excludes zero: MOM6_1 top-15 with a top-20 buffer, +3.7%/yr, CI [+0.5, +7.3]. That variant is also the best of 24 tried. Low-vol, 52-week-high and reversal books underperform equal weight. Most of the gap between "the portfolio" and NIFTYBEES (+6.7%/yr) comes from the universe, held equal-weight, not from selection.

### Cited Findings

**Setup** — [signal_tests.py](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/signal_tests.py)
- Equal weight at each rebalance (close of t+1), with weights drifting daily between rebalances. Buffer variant: an existing holding is kept while it ranks in the top 20, and empty slots are filled from the top of the ranking. EW_ALL holds every eligible name, rebalanced monthly. NIFTYBEES is buy-and-hold.
- Costs: 0.25% one-way × (buys + sells), charged on the trade day. The initial build is included. Turnover = one-way %/yr.
- Active return = annualised arithmetic mean of the daily net-return difference. 95% CI from a circular block bootstrap (63-day blocks, 2,000 resamples, seed 42).
- Data fix: the cached NIFTYBEES series has two unadjusted bars, 2019-12-19 (close 13.02) and 2019-12-20 (13.03), against about 130 on either side (a leftover from the 1:10 unit split). Untreated, they produce a fake −90% drawdown. The script masks bars more than 2× away from a centred 21-day median and forward-fills them. The repo's own loader and `hindcast/` code do not catch this — [repo: data/prices/adj/NIFTYBEES.NS.csv lines 629–630](file:///home/user/Portfolio/data/prices/adj/NIFTYBEES.NS.csv)

**Full period 2018-07-02 → 2026-10-15 (net unless noted)** — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)

| Book | CAGR gross | CAGR net | Vol | Max DD | Turnover/yr | Active vs EW_ALL [95% CI] | Active vs NIFTYBEES [95% CI] |
|---|---|---|---|---|---|---|---|
| NIFTYBEES | 11.14% | 11.14% | 15.4% | −36.3% | 0 | – | – |
| EW_ALL | 18.28% | 18.03% | 19.1% | −37.6% | 43% | – | +6.7% [+0.3, +12.8] |
| MOM12_1 top10 | 20.27% | 18.84% | 22.1% | −38.7% | 238% | +1.3% [−5.0, +7.5] | +8.0% [−2.8, +18.6] |
| MOM12_1 top10 buf20 | 19.93% | 19.39% | 21.9% | −36.4% | 91% | +1.7% [−3.2, +6.7] | +8.4% [−0.4, +17.8] |
| MOM12_1 top15 | 20.16% | 19.17% | 20.3% | −35.3% | 165% | +1.2% [−2.5, +4.8] | +7.9% [+0.4, +16.2] |
| MOM12_1 top15 buf20 | 18.02% | 17.47% | 19.9% | −33.6% | 92% | −0.3% [−4.1, +3.7] | +6.4% [−0.7, +13.8] |
| MOM6_1 top10 | 23.36% | 21.33% | 21.6% | −37.5% | 333% | +3.3% [−2.1, +8.9] | +10.0% [+1.5, +19.9] |
| MOM6_1 top10 buf20 | 22.64% | 21.86% | 21.5% | −35.9% | 128% | +3.7% [−1.2, +8.5] | +10.4% [+2.0, +19.2] |
| MOM6_1 top15 | 21.86% | 20.35% | 20.2% | −37.4% | 250% | +2.2% [−1.3, +5.5] | +8.8% [+1.9, +16.8] |
| **MOM6_1 top15 buf20** | 23.17% | **22.36%** | 19.7% | −33.7% | 132% | **+3.7% [+0.5, +7.3]** | +10.4% [+2.9, +18.4] |
| VAMOM12_1 top10 | 20.71% | 19.27% | 21.0% | −34.7% | 239% | +1.4% [−4.0, +7.4] | +8.1% [−0.8, +17.5] |
| VAMOM12_1 top10 buf20 | 19.01% | 18.51% | 20.3% | −36.0% | 85% | +0.6% [−4.4, +5.9] | +7.3% [−1.0, +17.4] |
| VAMOM12_1 top15 | 20.40% | 19.36% | 19.8% | −34.6% | 174% | +1.3% [−2.2, +5.0] | +7.9% [+0.6, +15.4] |
| VAMOM12_1 top15 buf20 | 18.44% | 17.89% | 19.5% | −33.8% | 93% | −0.0% [−3.5, +3.9] | +6.6% [−0.3, +14.2] |
| HIGH52W top10 | 18.44% | 16.49% | 18.2% | −34.4% | 334% | −1.5% [−7.3, +4.3] | +5.2% [−1.3, +11.7] |
| HIGH52W top10 buf20 | 16.65% | 16.17% | 17.9% | −36.7% | 84% | −1.8% [−6.6, +2.6] | +4.9% [−0.5, +9.9] |
| HIGH52W top15 | 17.01% | 15.75% | 18.1% | −38.2% | 216% | −2.1% [−6.2, +1.5] | +4.5% [−1.0, +10.0] |
| HIGH52W top15 buf20 | 18.39% | 17.85% | 17.8% | −35.8% | 93% | −0.4% [−3.8, +3.0] | +6.3% [+1.1, +11.7] |
| LOWVOL1Y top10 | 14.83% | 14.37% | 15.2% | −32.6% | 80% | −3.8% [−10.3, +2.4] | +2.8% [−1.7, +7.1] |
| LOWVOL1Y top10 buf20 | 13.55% | 13.34% | 15.9% | −35.7% | 38% | −4.6% [−10.7, +0.8] | +2.0% [−1.9, +6.0] |
| LOWVOL1Y top15 | 16.34% | 15.87% | 16.1% | −36.9% | 80% | −2.4% [−6.9, +2.4] | +4.3% [−0.1, +8.7] |
| LOWVOL1Y top15 buf20 | 15.81% | 15.55% | 16.5% | −35.2% | 45% | −2.6% [−6.5, +1.3] | +4.1% [−0.7, +9.2] |
| REV1M top10 | 19.70% | 15.15% | 21.5% | −42.7% | 776% | −2.0% [−6.8, +2.8] | +4.7% [−3.3, +12.7] |
| REV1M top15 | 21.12% | 17.81% | 19.9% | −38.4% | 555% | −0.0% [−3.6, +3.5] | +6.6% [−0.1, +13.3] |
| REV1M top10 buf20 | 17.09% | 15.22% | 21.5% | −39.5% | 322% | −1.9% [−7.4, +3.6] | +4.7% [−3.1, +12.3] |
| REV1M top15 buf20 | 16.03% | 14.28% | 19.8% | −40.1% | 305% | −3.1% [−6.9, +1.0] | +3.6% [−3.3, +10.4] |

(Vol is from gross returns. Max DD and the active columns are net. Active figures are arithmetic and can differ from CAGR gaps. HIGH52W has many tied values at 1.0, i.e. names sitting at their 52-week high. The add-on's stable tie-break therefore gives slightly different HIGH52W numbers, e.g. top10 buf20 −1.63% vs −1.82% here. All other books reproduce exactly, with a maximum daily difference of 1e-17.)

- **Costs and buffers:** without a buffer, momentum books turn over 165 to 333% a year one-way, which costs 1.0 to 2.0%/yr at 0.25% (MOM6_1 top10: 23.36% gross → 21.33% net). The top-20 buffer cuts turnover by about 60% (MOM6_1 top10: 333% → 128%) and raised net returns in both MOM6_1 cases. For MOM12_1 top15 and VAMOM12_1 the buffer cut the edge as well as the cost. REV1M's gross edge (top15 +21.1% gross) is entirely eaten by 555% turnover (+17.8% net) — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)
- **Placebo:** 200 seeded random-selection books per (N, buffer) setting. Random picks lose to EW_ALL net: median −3.7%/yr for top10 with no buffer (5th to 95th percentile −7.7 to +0.8), −2.5% for top15, −1.5% for top10 buf20 and −1.0% for top15 buf20. The drag comes from concentration plus turnover cost. Full-period percentile of each real book against its own placebo: MOM6_1 at 99 to 100 for all four variants; MOM12_1 and VAMOM12_1 non-buffered at 96 to 98; HIGH52W at 48 to 76; LOWVOL1Y at 12 to 52; REV1M at 12 to 94 — [addon_out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/addon_out.txt)
- **Stocks only** (ETFs excluded from both the book and its EW benchmark), active vs stocks-only EW, full period: MOM6_1 top10 +4.0%/yr, MOM6_1 top10 buf20 +4.5%, MOM12_1 top10 +1.4%, VAMOM12_1 top10 +1.0%, HIGH52W top10 −1.0%, LOWVOL1Y top10 −4.3% — [addon_out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/addon_out.txt)
- For comparison, the repo's existing hindcast found that following the engine's decisions underperformed doing nothing by −3.70%/yr (CI [−9.26%, +0.84%]), with REVIEW/ACCUMULATE IC −0.02 (t −0.25) — [repo: reports/hindcast_summary.md](file:///home/user/Portfolio/reports/hindcast_summary.md)

### Inferences
- Within this universe, the largest and most reliable source of return over NIFTYBEES was owning the names equal-weight (+6.7%/yr, CI just above zero). Selection by momentum added a further +2 to 4%/yr, but that estimate is much less certain.
- The best single result (MOM6_1 top15 buf20) is the maximum of 24 configurations. Its CI lower bound of +0.5% would very likely fall below zero after a multiple-testing adjustment. The fact that all four MOM6_1 variants sit at the 99th to 100th placebo percentile is more convincing than any one CI.
- A rank buffer is clearly worthwhile as an implementation device: it cut turnover by roughly 2.5× with no consistent loss of edge. Even so, the gain from the buffer was not uniform across signals.
- Low-vol did what it is known for (lowest vol and smallest drawdown in the 2024–25 sell-off) but gave no excess return. In this universe it mainly tilts toward the broad-market ETFs and defensive names.

### Gaps
- No tax, slippage beyond the flat 0.25%, or market-impact modelling, as instructed.
- Weighting schemes (inverse-vol, signal-weighted) and combinations of signals (e.g. MOM6_1 + VAMOM) were not tested, to avoid adding more configurations to choose from.

## Q3. Are the results stable across 2018–2022 vs 2023–2026, and what happened in the Sep 2024 – Mar 2025 momentum drawdown?

### Takeaway
No. Almost all of the momentum edge sits in 2018–2022, and calendar 2021 alone contributes about 24 points of it. In 2023–2026 the IC of every signal is statistically zero: MOM6_1 63d IC falls from +0.162 (t 6.1) to −0.009, and HIGH52W turns negative. Buffered momentum books stayed ahead of EW in 2023–26, but with CIs that include zero. In the Sep 2024 – Mar 2025 sell-off, MOM12_1 top10 lost about 32% against −17% for EW. MOM6_1 roughly matched EW.

### Cited Findings
- **IC by sub-period** (mean IC, NW t) — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)

| Signal, horizon | 2018–2022 (55 months) | 2023–2026 (33–44 months) |
|---|---|---|
| MOM6_1, 63d | 0.162 (t 6.13) | −0.009 (t −0.17) |
| MOM6_1, 126d | 0.147 (t 4.49) | 0.009 (t 0.14) |
| MOM12_1, 63d | 0.082 (t 2.32) | 0.016 (t 0.22) |
| VAMOM12_1, 63d | 0.083 (t 2.41) | 0.028 (t 0.51) |
| HIGH52W, 63d | 0.113 (t 3.49) | −0.075 (t −1.80) |
| HIGH52W, 126d | 0.123 (t 3.14) | −0.028 (t −0.68) |
| LOWVOL1Y, 63d | 0.046 (t 0.94) | −0.056 (t −0.67) |
| REV1M, 126d | −0.051 (t −2.08) | −0.013 (t −0.37) |

- **Active return vs EW_ALL by sub-period (net, %/yr, [95% CI], placebo percentile)** — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt), [addon_out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/addon_out.txt)
  - MOM6_1 top15 buf20: 2018–22 +6.1 [+1.1, +11.0] (p100); 2023–26 +0.8 [−3.5, +5.1] (p85)
  - MOM6_1 top10 buf20: 2018–22 +3.6 [−3.5, +10.8] (p91); 2023–26 +3.8 [−2.9, +10.8] (p96)
  - MOM6_1 top10: 2018–22 +6.8 [+1.0, +13.0] (p100); 2023–26 −0.9 [−10.6, +8.2] (p76)
  - MOM12_1 top10 buf20: 2018–22 −1.1 (p56); 2023–26 +5.1 [−3.8, +13.5] (p98)
  - VAMOM12_1 top10: 2018–22 +1.0 (p90); 2023–26 +2.0 [−5.1, +9.4] (p93)
  - HIGH52W top10: 2018–22 +2.2 (p96); 2023–26 −5.9 [−12.6, +1.0] (p25)
  - LOWVOL1Y top10 buf20: 2018–22 −1.0; 2023–26 −8.9 [−17.6, +0.5] (p1)
  - EW_ALL vs NIFTYBEES: 2018–22 +3.4 [−3.3, +11.3]; 2023–26 +10.6 [+0.0, +21.9]
- **Calendar-year active vs EW_ALL (compounded, net, percentage points)**, MOM6_1 top15 buf20: 2018 −1.9, 2019 +4.4, 2020 +7.8, **2021 +24.8**, 2022 +3.5, 2023 +4.4, 2024 +4.3, 2025 −1.1, 2026 YTD −3.3. MOM12_1 top10 buf20: −3.6, +3.8, −3.4, −3.7, −0.1, +13.2, −4.2, +10.7, +0.3. Both MOM6_1 buffered books and VAMOM12_1 top10 lost to EW in 2025–26 (VAMOM −4.5 and −6.2) — [addon_out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/addon_out.txt)
- **Sep 2024 – Mar 2025 window** (2024-09-01 to 2025-03-31, total net return): NIFTYBEES −6.4%; EW_ALL −16.6%; MOM12_1 top10 −31.8% (max DD −34.3%); MOM12_1 top10 buf20 −23.7%; MOM12_1 top15 −22.8%; VAMOM12_1 top10 −19.1%; MOM6_1 top10 −14.3%; MOM6_1 top15 buf20 −14.3%; HIGH52W top15 buf20 −11.3%; LOWVOL1Y top10 −4.9%; REV1M top10 buf20 −26.1% — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)
- MOM6_1 top 10 on 2024-08-30 (going into the sell-off): BEL, ASHOKLEY, JSWENERGY, GAIL, FEDERALBNK, PETRONET, NTPC, SJVN, ONGC, TATAPOWER, which is mostly PSU, power and energy names. On 2025-03-28 it had rotated to GOLDIETF, WIPRO, ASHOKLEY, HDFCBANK, ITBEES, FEDERALBNK, BANKNIFTY ETF, PETRONET, BEL and the Nifty ETF — [addon_out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/addon_out.txt)

### Inferences
- The 2018–2022 momentum IC is largely the 2020–2021 rally in PSU, power and energy names, which make up much of this portfolio. Because many holdings share a sector, "momentum" here is mostly a sector-rotation bet among Power and Oil & Gas names. The universe offers too few independent bets for the result to generalise.
- 12-1 momentum was hit hardest in the 2024–25 reversal, because its 12-month window was full of the 2023–24 PSU and power winners. The shorter 6-1 window rotated out faster. That fits the usual momentum-crash pattern, but this is a single episode.
- The 2023–2026 period is when an engine built today would have been running. In that period no signal shows significant IC, and the most recent ~21 months (2025 to 2026 YTD) were negative for MOM6_1 and VAMOM books. The evidence for "turn on momentum now" is therefore weak.

### Gaps
- The 2023–26 sub-period has only 33 to 44 monthly ICs and 3.8 years of daily returns, which is too short to distinguish a decayed effect from noise.
- No regime conditioning (e.g. benchmark above/below 200-DMA) was tested for the signal books, to avoid adding more configurations to choose from.

## Q4. Limitations: how far can this evidence be trusted?

### Takeaway
Treat everything above as directional evidence only. The universe is the owner's current survivors, small, clustered in a few sectors, and observed over one Indian bull-market path.

### Cited Findings
- **Survivorship and selection bias:** the universe is the 34 *current* holdings in `portfolio.csv`, so every name survived to 2026 and was chosen by the owner, partly with hindsight. Losers that were sold or delisted are absent. This biases EW_ALL upward (+6.7%/yr vs NIFTYBEES) and may favour momentum, since names that kept rising are more likely to still be held — [repo: hindcast/run.py](file:///home/user/Portfolio/hindcast/run.py)
- **Tiny cross-section:** 24 eligible names for 2018–2021 and at most 32 by the end. Top-10 of 24 is a 42% slice, so the books are mild tilts of EW, not concentrated factor portfolios — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)
- **Sector concentration:** the repo's own sector map puts 6 names in Power (JSWENERGY, NHPC, NTPC, NTPCGREEN, SJVN, TATAPOWER), 6 in Oil & Gas (GAIL, GUJENERGY, HINDPETRO, ONGC, PETRONET, RELIANCE), 3 in Banking and 3 in Broad Market — [repo: hindcast/run.py](file:///home/user/Portfolio/hindcast/run.py)
- **Mixed instruments:** 7 ETFs (Nifty, Bank Nifty, IT, smallcap 250, midcap 150, gold, silver) are ranked alongside single stocks. The stocks-only rerun gives similar momentum conclusions — [addon_out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/addon_out.txt)
- **Data quality:** the IDEA series has three unexplained one-day moves (2019-11-19 ×1.36, 2020-02-19 ×1.40, 2020-03-18 ×0.65) that the repo loader flags `CA_SUSPECT`. GUJENERGY and VIYASH are stitched across renames. The NIFTYBEES 2019-12-19/20 bars are unadjusted (fixed in this script only) — [repo: hindcast/data.py](file:///home/user/Portfolio/hindcast/data.py)
- **Multiple testing:** 24 IC cells and 24 portfolio books were evaluated, and no deflated Sharpe ratio or PBO correction was applied, unlike the repo hindcast's DSR/PBO checks — [repo: reports/hindcast_summary.md](file:///home/user/Portfolio/reports/hindcast_summary.md)

### Inferences
- The one robust-looking conclusion is a relative one: the momentum family ranks above random selection and above low-vol, 52-week-high and reversal in this universe. The size of any edge (2 to 4%/yr) should not be carried forward as an expected value.

### Gaps
- There is no survivorship-free Indian universe (e.g. historical Nifty 500 constituents with delisted names) in the repo, so the result cannot be checked out-of-sample here.

## Q5. Implications for the repo

### Takeaway
Of the six signals, intermediate-horizon momentum (6-1, and possibly volatility-adjusted 12-1) is the only one worth taking to a proper test, run with a rank buffer. Low-vol, 52-week-high and 1-month reversal showed nothing usable here and should be low priority. Before any signal drives trades, the repo needs a survivorship-free universe and the benchmark-data fix.

### Cited Findings
- MOM6_1 had the strongest IC (0.088 to 0.090 at 3 to 6 months, t 2.5 to 2.7). All four MOM6_1 portfolio variants rank at the 99th to 100th placebo percentile, with +2.2 to +3.7%/yr net over EW_ALL. But the edge is concentrated in 2018–2022, and 2025–26 YTD was negative — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt), [addon_out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/addon_out.txt)
- VAMOM12_1 was the only signal with positive IC in both sub-periods (63d: 0.083 then 0.028; 126d: 0.059 then 0.048). It also had a smaller loss than raw MOM12_1 in the 2024–25 sell-off (−19.1% vs −31.8% for top10) — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)
- The top-20 rank buffer cut momentum turnover from about 250 to 330% to about 130%/yr with no consistent loss of edge. Unbuffered reversal (555 to 776%/yr) is not viable at 0.25% one-way cost — [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)
- The existing engine's REVIEW/ACCUMULATE decisions have an IC of −0.02 (t −0.25), against +0.09 for a one-line 6-1 momentum rank on the same names — [repo: reports/hindcast_summary.md](file:///home/user/Portfolio/reports/hindcast_summary.md), [out.txt](file:///tmp/claude-0/-home-user-Portfolio/a8dc17ce-abc0-5fe4-beed-8ca4e391f0bb/scratchpad/out.txt)

### Inferences
- **Worth a proper test on a broad, survivorship-free Indian universe** (e.g. point-in-time Nifty 500 or NSE-listed stocks above a liquidity floor, with delisted names included):
  1. 6-1 momentum (primary candidate).
  2. Volatility-adjusted 12-1 momentum (looked more stable across sub-periods and suffered less in the momentum crash).
  3. A momentum-crash guard (e.g. a shorter lookback or vol-scaling in high-volatility regimes), motivated by the 2024–25 episode.

  Use sector-neutral ranking, a hold-until-rank-falls-out buffer, at least 0.25% one-way cost, and a DSR/PBO-style multiple-testing check, as the repo's hindcast already does for its own parameters.
- **Low priority / drop:** LOWVOL1Y (negative active return in both sub-periods; useful only as a risk overlay), HIGH52W (positive in 2018–22, then IC −0.075 in 2023–26), REV1M (no IC, prohibitive turnover).
- **For this repo specifically:** a cheap, defensible change is to add a 6-1 / vol-adjusted momentum rank as a *read-only diagnostic* column alongside REVIEW/ACCUMULATE, and to record it in the hindcast so its live IC builds up out-of-sample. It should not drive trades on the strength of this 34-name evidence.
- **Data fix (separate from the research question):** `data/prices/adj/NIFTYBEES.NS.csv` has unadjusted closes on 2019-12-19 and 2019-12-20 (≈13 vs ≈130). This can distort the hindcast's 200-DMA and drawdown regime labels and any 252-day excess return that starts or ends near those dates in the TRAIN window (2019–2022).

### Gaps
- Whether the 6-1 momentum effect survives in a broad Indian universe after 2022 could not be checked here. That is the decisive test, and it needs data the repo does not have.
