# Hindcast summary

Engine commit `f1ca5fd` · price manifest sha256 `595381de6a92b810` · grid sha256 `045f1d1f42a932fb` · benchmark NIFTYBEES.NS (adjusted close) · bootstrap seed 42

## 1. Verdict per decision type (primary window, incumbent parameters)

Decision dates 2022-10-01 to 2025-10-31 (37 month-ends). Outcome = 252-session excess return vs NIFTYBEES from the next close. Hit rate at a ±5% neutral band, one count per episode.

| Class | Decisions | Episodes | Hit rate | 95% CI (naive) | 95% CI (effective N) | Avg XR | NW t | Bootstrap CI | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| SELL | 0 | 0 | n/a | [n/a, n/a] | [n/a, n/a] | n/a | n/a | [n/a, n/a] | **INSUFFICIENT EVIDENCE** |
| TRIM | 63 | 33 | 34.62% | [19.41%, 53.78%] | [4.69%, 85.07%] | 4.18% | -0.75 | [-13.10%, 4.87%] | **INSUFFICIENT EVIDENCE** |
| REVIEW | 282 | 76 | 41.27% | [29.96%, 53.58%] | [8.61%, 83.98%] | 13.57% | -3.96 | [-19.23%, -7.21%] | **OUT OF LINE** |
| ACCUMULATE | 194 | 62 | 59.52% | [44.49%, 72.96%] | [17.01%, 91.34%] | 1.83% | 1.31 | [-4.35%, 9.22%] | **INSUFFICIENT EVIDENCE** |
| HOLD | 463 | 128 | – | – | – | 13.99% | – | – | baseline (|XR|≤10%: 32.09%) |

Information coefficient (signed decision score vs XR, per date): mean -0.02, NW t -0.25, dates 36.

## 2. Acting on the recommendations

| Window | Book | CAGR | Vol | Max DD | DD days | Turnover/yr | Trades |
|---|---|---|---|---|---|---|---|
| primary (incumbent) | FOLLOW-MODEL | 14.14% | 14.65% | -20.89% | 806 | 0.13 | 100 |
| primary (incumbent) | DO-NOTHING | 17.54% | 18.73% | -26.30% | 806 | n/a |  |
| primary (incumbent) | NIFTYBEES | 7.52% | 11.45% | -15.23% | 391 | n/a |  |
| TEST (tuned: trail_trim_half) | FOLLOW-MODEL | 14.23% | 15.96% | -20.13% | 520 | 0.12 | 71 |
| TEST (tuned: trail_trim_half) | DO-NOTHING | 15.84% | 19.26% | -24.58% | 806 | n/a |  |
| TEST (tuned: trail_trim_half) | NIFTYBEES | 7.53% | 12.13% | -15.23% | 391 | n/a |  |
| TEST (incumbent) | FOLLOW-MODEL | 14.35% | 16.19% | -20.47% | 520 | 0.10 | 68 |

Primary FOLLOW-MODEL minus DO-NOTHING: -3.70% a year, bootstrap 95% CI [-9.26%, 0.84%].

## 3. Tuning result

TRAIN 2019-01-01–2022-09-30 (44 decision dates after purging labels that overlap TEST); TEST 2023-10-01–2025-10-31 (25 dates), looked at once. Grid: 14 configs from `data/hindcast/grid.json`.

Best on TRAIN: **trail_trim_half** {"trailing_trim_fraction": 0.5}. DSR 0.18, PBO 0.45.

| Acceptance check | Pass |
|---|---|
| chosen differs from incumbent | yes |
| TEST: tuned beats incumbent (A-B) | no |
| TEST: follow-model >= do-nothing | no |
| TEST: follow-model >= NIFTYBEES | yes |
| DSR > 0.95 | no |
| PBO < 0.3 | no |
| improvement holds above and below the benchmark 200-DMA | no |

**Recommendation: keep current parameters.**
Rule types to make advisory-only (verdict OUT OF LINE): REVIEW.
Next-best TRAIN config: incumbent.

Parameter robustness (share of grid neighbours with the same sign of TRAIN benefit; ≥70% = robust):

| parameter               | neighbours                             |   same_sign_share | robust   |
|:------------------------|:---------------------------------------|------------------:|:---------|
| trailing_drawdown_pct   | trail_dd_20, trail_dd_40               |                 1 | True     |
| trailing_min_gain_pct   | trail_gain_25, trail_gain_75           |                 1 | True     |
| trailing_trim_fraction  | trail_trim_half                        |                 1 | True     |
| overextension_multiple  | overext_1.40, overext_off              |                 1 | True     |
| dma_200_breach_sessions | review_sessions_10, review_sessions_40 |                 1 | True     |
| dma_200_breach_pct      | review_band_2, review_band_5           |                 1 | True     |
| accumulate_high_52w_pct | acc_high_10, acc_high_30               |                 1 | True     |

## 4. Coverage and data log

| symbol     | ticker        |   rows | first      | tags                           | notes                                                                                                                                                                                             |
|:-----------|:--------------|-------:|:-----------|:-------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ASHLEY     | ASHOKLEY.NS   |   2317 | 2017-06-01 | OK                             | ASHOKLEY.NS bonus 2025-07-16 (sourced): series already adjusted (max one-day move in window x0.986)                                                                                               |
| BHAELE     | BEL.NS        |   2317 | 2017-06-01 | OK                             | BEL.NS bonus 2022-09-15 (sourced): series already adjusted (max one-day move in window x0.984)                                                                                                    |
| DRREDD     | DRREDDY.NS    |   2317 | 2017-06-01 | OK                             | DRREDDY.NS split 2024-10-28 (sourced): series already adjusted (max one-day move in window x0.972)                                                                                                |
| ENGIND     | ENGINERSIN.NS |   2317 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| FEDBAN     | FEDERALBNK.NS |   2317 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| GAIL       | GAIL.NS       |   2317 | 2017-06-01 | OK                             | GAIL.NS bonus 2022-09-06 (sourced): series already adjusted (max one-day move in window x0.992)                                                                                                   |
| GUJGA      | GUJENERGY.NS  |   2316 | 2017-06-01 | ADJ_DEMERGER_OBSERVED,STITCHED | GUJENERGY.NS demerger 2026-07-02 (sourced): observed drop x0.917 on 2026-07-02 back-adjusted                                                                                                      |
| GUJPPL     | GPPL.NS       |   2317 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| HDF250     | HDFCSML250.NS |    896 | 2023-02-21 | OK                             |                                                                                                                                                                                                   |
| HDFBAN     | HDFCBANK.NS   |   2317 | 2017-06-01 | OK                             | HDFCBANK.NS bonus 2025-08-26 (sourced): series already adjusted (max one-day move in window x0.984)                                                                                               |
| HINPET     | HINDPETRO.NS  |   2317 | 2017-06-01 | OK                             | HINDPETRO.NS bonus 2024-06-21 (sourced): series already adjusted (max one-day move in window x0.972)                                                                                              |
| ICIGOL     | GOLDIETF.NS   |    698 | 2023-12-12 | OK                             |                                                                                                                                                                                                   |
| ICINIF     | 537007.BO     |   2350 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| ICIPSE     | SILVERIETF.NS |    417 | 2025-02-03 | OK                             |                                                                                                                                                                                                   |
| IDECEL     | IDEA.NS       |   2317 | 2017-06-01 | CA_SUSPECT                     | IDEA.NS: unexplained one-day move x1.360 on 2019-11-19 | IDEA.NS: unexplained one-day move x1.400 on 2020-02-19 | IDEA.NS: unexplained one-day move x0.649 on 2020-03-18                          |
| JIOFIN     | JIOFIN.NS     |    779 | 2023-08-21 | OK                             |                                                                                                                                                                                                   |
| JSWENE     | JSWENERGY.NS  |   2317 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| KOTAKBKETF | BANKNIFTY1.NS |   2315 | 2017-06-01 | ADJ_FIXED                      | BANKNIFTY1.NS split 2026-02-27 (sourced): unadjusted x0.099 on 2026-02-27 fixed with factor 0.1000                                                                                                |
| LGELEC     | LGEINDIA.NS   |    249 | 2025-10-14 | OK                             |                                                                                                                                                                                                   |
| LIC        | LICI.NS       |   1093 | 2022-05-17 | OK                             |                                                                                                                                                                                                   |
| MIR150     | MIDCAPETF.NS  |    574 | 2024-06-19 | OK                             |                                                                                                                                                                                                   |
| NHPC       | NHPC.NS       |   2317 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| NIPNIT     | ITBEES.NS     |   1559 | 2020-06-30 | OK                             |                                                                                                                                                                                                   |
| NTPC       | NTPC.NS       |   2317 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| NTPGRE     | NTPCGREEN.NS  |    468 | 2024-11-27 | OK                             |                                                                                                                                                                                                   |
| ONGC       | ONGC.NS       |   2317 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| PETLNG     | PETRONET.NS   |   2317 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| RELIND     | RELIANCE.NS   |   2317 | 2017-06-01 | ADJ_DEMERGER_OBSERVED          | RELIANCE.NS demerger 2023-07-20 (sourced): observed drop x0.969 on 2023-07-21 back-adjusted | RELIANCE.NS bonus 2024-10-28 (sourced): series already adjusted (max one-day move in window x0.973) |
| SEQSCI     | VIYASH.NS     |   2317 | 2017-06-01 | STITCHED                       |                                                                                                                                                                                                   |
| SJVLIM     | SJVN.NS       |   2317 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| TATCAP     | TATACAP.NS    |    250 | 2025-10-13 | OK                             |                                                                                                                                                                                                   |
| TATGLO     | TATACONSUM.NS |   2317 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| TATPOW     | TATAPOWER.NS  |   2317 | 2017-06-01 | OK                             |                                                                                                                                                                                                   |
| WIPRO      | WIPRO.NS      |   2317 | 2017-06-01 | OK                             | WIPRO.NS bonus 2024-12-03 (sourced): series already adjusted (max one-day move in window x0.982)                                                                                                  |

Decision coverage (primary): ENTRY=5, NOT_LISTED=173, OK=1002, SHORT_HISTORY=78

## 5. Sensitivities and regimes

| variant                 |   decisions_changed |   active_ann |
|:------------------------|--------------------:|-------------:|
| conviction=3            |                 195 |   -0.0403814 |
| invalidation=cost x0.85 |                  34 |   -0.0562571 |
| invalidation=52w low    |                   0 |   -0.0369754 |

| class      | regime               |   dates |   signed_mean_XR |
|:-----------|:---------------------|--------:|-----------------:|
| SELL       | bench above 200DMA   |       0 |      nan         |
| SELL       | bench below 200DMA   |       0 |      nan         |
| SELL       | bench drawdown > 10% |       0 |      nan         |
| TRIM       | bench above 200DMA   |      18 |       -0.0529541 |
| TRIM       | bench below 200DMA   |       5 |       -0.071977  |
| TRIM       | bench drawdown > 10% |       1 |       -0.0693498 |
| REVIEW     | bench above 200DMA   |      28 |       -0.140352  |
| REVIEW     | bench below 200DMA   |       6 |       -0.140535  |
| REVIEW     | bench drawdown > 10% |       1 |       -0.130878  |
| ACCUMULATE | bench above 200DMA   |      30 |        0.0330658 |
| ACCUMULATE | bench below 200DMA   |       6 |        0.181523  |
| ACCUMULATE | bench drawdown > 10% |       1 |        0.311253  |

SELL/TRIM/REVIEW issued 2024-10-01 to 2025-03-31: 118 decisions, resolved avg XR 0.88%.

## 6. Caveats

- No tax or transaction costs: every return is an upper bound.
- Universe = today's 34 holdings, as if held throughout (survivorship-biased: SELL looks worse, ACCUMULATE better). FOLLOW-MODEL vs DO-NOTHING uses the same names, so the bias largely cancels there.
- thesis.csv is never read (written in 2026): thesis INTACT, conviction 4, ROE 0.15, no invalidation price in the primary run.
- Overlapping 1-year windows: the primary window holds about 3 non-overlapping years, TEST about 2; one market path.
- Decisions are monthly; daily confirmation rules (3 closes) are only approximated at month-ends.
