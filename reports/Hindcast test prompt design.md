# Replay the engine monthly, then grade it

The prompt below asks a coding agent to build one thing the repo does not have yet: a **point-in-time, monthly replay of `signal_engine.evaluate_signal`** over 37 decision dates (Oct 2022 to Oct 2025). Each `decision` is scored on its **252-trading-day excess return over a dividend-inclusive Nifty 50** (Nifty 50 TRI, or NIFTYBEES adjusted close as a proxy). Three shadow portfolios run alongside it: follow-model, do-nothing and benchmark. Costs and tax are excluded. The design reuses the engine's pure decision function and the repo's existing fill and forward-return patterns. It does not build on `backtest_engine.py`, which carries look-ahead and weekly-proxy defects. The main tension is your wish to tweak parameters. Overlapping one-year labels leave roughly four or five independent observations in three years, which is too few to tune on. The prompt therefore makes **validation of the current parameters the primary result**. Tuning is allowed only through a preregistered six-config grid on an extended, purged, technical-only window, and the agent proposes a diff but never applies one. Expect most decision classes to come back "insufficient evidence". That result is real information, and the prompt forces the agent to say it rather than overclaim.

## The prompt (copy-paste into the IDE agent)

```text
ROLE: principal quant engineer. Repo /home/user/Portfolio, branch claude/happy-hawking-9b8pow.
GOAL: point-in-time monthly HINDCAST of the live engine; verify every decision against its actual
1-year outcome vs Nifty 50; flag parameters that are out of line. EXCLUDE tax and transaction costs
everywhere (no fees, slippage, STT or tax model).

REUSE, DON'T REBUILD
1. Call signal_engine.evaluate_signal unchanged. Pass variants as dataclasses.replace(config.RISK_CONFIG, ...).
   Do NOT edit config.py or signal_engine.py.
2. Move the indicator math in analysis.fetch_market_data (daily 50/200 SMA, 252-day high, 14-day Wilder ATR
   via indicators.atr) into a pure features_asof(daily_df) called by both live code and the hindcast.
   Live outputs must not change.
3. Reuse frame.loc[:t] slicing + next-bar fills (backtest/backtester.py), forward-index logic
   (signal_scorer.py) and analysis.size_action for sizing. Leave backtest_engine.py UNTOUCHED: its weekly
   proxies, same-bar fills and today's thesis.csv/roe/sector inputs are look-ahead.
4. New files: hindcast/fetch.py (network, run once), hindcast/run.py (offline, cache only),
   hindcast/stats.py, tests/test_hindcast.py. Use numpy/pandas only.

DATA (fetch once, then run offline)
5. fetch.py: daily OHLCV from 2017-06-01 to today for every symbol in analysis.TICKER_MAP and trades.csv,
   plus NIFTYBEES.NS, ^NSEI, NIFTYIETF.NS and the old tickers SEQUENT.NS (->VIYASH.NS on 23 Jan 2026) and
   GUJGASLTD.NS (->GUJENERGY.NS; ticker unverified). Save raw (auto_adjust=False) AND adjusted
   (auto_adjust=True, repair=True) to data/prices/{raw,adj}/<ticker>.csv. Write a manifest.json with fetch
   time, yfinance version, row counts and sha256. Stitch renamed tickers at the change date. Commit the cache.
6. data/corporate_actions.csv (symbol, ex_date, type, ratio, status, source):
   BEL 2:1 bonus ~15 Sep 2022 | GAIL 1:2 bonus 6 Sep 2022 | HINDPETRO 1:2 bonus rec 21 Jun 2024 |
   DRREDDY 1:5 split 28 Oct 2024 | RELIANCE 1:1 bonus 28 Oct 2024 | WIPRO 1:1 bonus 3 Dec 2024 |
   ASHOKLEY 1:1 bonus rec 16 Jul 2025 | BANKNIFTY1 10:1 unit split 27 Feb 2026 |
   RELIANCE->JIOFIN 1:1 demerger Jul 2023 (JFS 261.85) | GUJGASLTD->GTL 1:3 demerger rec 2 Jul 2026.
   UNVERIFIED (confirm/reject from raw series; log verdict): HDFCBANK 1:1 bonus ~Aug 2025; RIL demerger
   session ~20 Jul 2023; NIFTYBEES unit split ~2019; listing dates LICI 17 May 2022, SILVERIETF late Jan 2022,
   MIDCAPETF launch.
7. On each split/bonus ex-date, assert the adjusted close ratio is in 0.85-1.15. If it matches the event ratio,
   back-apply the factor and tag ADJ_FIXED. Do NOT use SPLIT_JUMP_RATIO=2.5, which misses 0.5x/0.67x bonuses.
   Never "repair" demergers: credit child shares and add child value to the parent's forward return.
   If child prices are missing, tag UNRESOLVED_CA.
8. Benchmark: use data/benchmark/nifty50_tri.csv if present, else NIFTYBEES.NS adjusted close as a TRI proxy,
   and log which. Stocks also use dividend-adjusted closes. ^NSEI is reference only.

POINT-IN-TIME
9.  Decision dates t = last NSE trading day of each month, Oct 2022 to Oct 2025 (37). Inputs use bars <= t only.
10. Exclude a symbol before it lists. It needs >=200 valid sessions (DMA) and >=252 (52w high), else NO DATA
    (counted, not scored). Never backfill.
11. thesis.csv was set 2026-09-26 (look-ahead): NEVER read it. Primary: thesis_text="INTACT",
    invalidation_price=None, conviction=4, roe=0.15. Sensitivities: conviction=3; invalidation = avg cost at
    t x 0.75; invalidation = 52w low at t. Report decision-change counts vs primary.
12. Universes. (a) ACTUAL-BOOK (primary): holdings at t replayed from trades.csv (date <= t) plus CA credits.
    Average cost uses the same split-adjusted basis as prices. Reconcile to portfolio.csv qty; mismatches
    (ASHLEY BHAELE HDFBAN JIOFIN LIC RELIND WIPRO LGELEC NTPGRE TATCAP) count only once reconciled, else are
    excluded with a reason. (b) HINDSIGHT-34 (label as biased): today's symbols, existence-gated, equal-weight,
    bought at each symbol's first eligible t (= cost basis). GUJPPL->GPPL.NS (Gujarat Pipavav, INE517F01014)
    is correct; do not change it.
13. stock_weight, sector_risk_exposure (analysis.py Financials bucket), risk_group_exposure (direct holdings
    only; the 2026 ETF look-through is not point-in-time) and total_return all come from that universe's book
    at t, never from today's portfolio.

VERIFICATION
14. R = close(t+1) -> close(t+1+252 sessions), for stock and benchmark. XR = (1+R_s)/(1+R_b) - 1
    (also report R_s - R_b). A window beyond the last close is UNRESOLVED, never truncated.
15. Score the `decision` field (also log `signal`). Band b = 5% primary; 0% and 2% as sensitivities.
    SELL/TRIM correct if XR < -b, wrong if XR > +b. BUY/ACCUMULATE correct if XR > +b, wrong if XR < -b.
    Otherwise neutral (out of the hit-rate denominator, share reported). HOLD: XR distribution as base rate
    + share with |XR| <= 10%. NO DATA/VERIFY DATA/NO THESIS: coverage table only.
16. Episodes: collapse runs of the same decision per symbol and score at episode start. Report decision-level
    and episode-level stats side by side.
17. Signed score SELL=-2, TRIM=-1, HOLD=0, BUY/ACCUMULATE=+1. Per date: mean score*XR, Spearman IC, Kendall tau-b.
18. Inference only on per-date series: Newey-West t (Bartlett, lag 11) + moving-block bootstrap over dates
    (block 12, 10,000 draws, seed 42). Report n_raw, n_episodes, n_eff_time = n_dates/8, and the design effect
    1+(m-1)*rho_hat (rho_hat = mean pairwise corr of XR). Wilson 95% CIs on raw n ("naive") and on n_eff.
19. Verdict per class: SKILL only if episode effect has the right sign, NW t>3.0 or bootstrap CI excludes 0,
    >=10 episodes, and the same sign in every regime. OUT OF LINE if wrong sign with CI excluding 0.
    Else INSUFFICIENT EVIDENCE.
20. Regimes. Per date: benchmark above/below its 200-DMA; drawdown >10%. Per outcome window: benchmark-return
    terciles. Separate table for SELL/TRIM issued Oct 2024 - Mar 2025.

SHADOW PORTFOLIOS (same start NAV/book at first date; no costs, no external flows)
21. A follow-model: decide at close t, trade at close t+1. SELL exits 100%. TRIM/BUY/ACCUMULATE use
    size_action; if it gives no size, ACCUMULATE = +1% NAV from cash capped at max_position_pct, pro rata if
    cash is short. No leverage. B do-nothing (hold start book). C benchmark. Cash at 0%; variant: park
    proceeds in the benchmark.
22. Report CAGR, vol, max DD + duration, turnover, trades, and A-B daily active return with a bootstrap CI.

TUNING (only if a class is OUT OF LINE; the primary run uses current params)
23. Before any tuning run, commit data/hindcast/grid.json: incumbent (trailing_stop_atr_multiple 3.0,
    overextension_multiple 1.25) + one-at-a-time trailing in {2,4,5}, overextension in {1.15,1.40} = 6 configs.
    Objective = per-date mean score*XR.
24. Technical-only engine (step-11 primary inputs, HINDSIGHT-34): train Jan 2019 - Sep 2022; purge Oct 2022 -
    Sep 2023; test Oct 2023 - Oct 2025. Log every config run to reports/hindcast_trials.csv. Compute the
    Deflated Sharpe Ratio (N = trials; Bailey & Lopez de Prado 2014) on test A-B returns, and PBO via CSCV (S=6).
25. Accept only if: test improvement NW t>3.0 or bootstrap CI>0; DSR>0.95; PBO<0.2; it holds in rally and
    drawdown regimes; plus a one-paragraph economic rationale. Then write reports/hindcast_param_proposal.diff
    and DO NOT apply it. Otherwise write "keep current parameters".

OUTPUTS, TESTS, DONE
26. reports/hindcast_decisions.csv: date, universe, config_id, symbol, ticker, data_tag
    (OK/SHORT_HISTORY/NOT_LISTED/ADJ_FIXED/STITCHED/UNRESOLVED/UNRESOLVED_CA), every evaluate_signal input,
    decision, signal, rationale, episode_id, R_s, R_b, XR, correct_b0/b2/b5, regime labels.
27. reports/hindcast_summary.md sections: header (commit, data sha256, benchmark used, seed); caveats (no
    costs/tax, ~3 non-overlapping years, thesis/conviction/ROE neutralised, one market path); coverage;
    per-class hit rates; IC and payoff; regimes; shadow portfolios; sensitivities; CA log; verdicts; tuning.
28. tests/test_hindcast.py: a poisoned bar after t changes no decision at t; fills at close t+1, never t;
    episode collapse; XR/band scoring incl. neutral + UNRESOLVED; purge drops every train date whose label
    overlaps test; existence gate; CA table fixes a synthetic 0.5x bonus; total_return equal on raw vs adjusted
    basis; thesis.csv never opened. The FULL pytest suite passes.
29. Two reruns from cache give byte-identical outputs. Commit and push to claude/happy-hawking-9b8pow.
```

## Why this design and not an extension of the existing backtest

The repo has the parts but not the test. **`evaluate_signal` is pure and deterministic.** Its only global is the frozen `RiskConfig`, which can be overridden per call, so a parameter grid needs no edit to `config.py` ([signal_engine.py:30-99](../signal_engine.py), [config.py:26-62](../config.py)). `backtest_engine.py` is the only module that replays the full decision tree, and it cannot be the test. It fills on the **same weekly close** it decides on. It uses weekly proxies for daily indicators: a 40-week 200-DMA, and a weekly ATR roughly √5 the size of the daily one. It also back-applies **today's thesis, invalidation prices, `roe=0.15` and `sector=15`** to 2021 ([backtest_engine.py:116-157](../backtest_engine.py)). Its 0.64% CAGR against 13.28% buy-and-hold therefore says little about the live logic ([reports/backtest_summary.md](backtest_summary.md)). The other tools cover different ground. `backtest/backtester.py` tests only the DMA trend layer, though its `loc[:date]` slicing and next-bar fills are worth reusing ([backtest/backtester.py:115-131](../backtest/backtester.py)). `signal_scorer.py` scores emoji signals at 5, 10 and 20 days with no benchmark ([signal_scorer.py:126-162](../signal_scorer.py)). None of them does 252-day, per-decision, benchmark-relative verification. That is the gap this prompt fills.

**Thesis inputs are neutralised because they are hindsight.** All 34 `thesis.csv` rows were last updated on 2026-09-26, after every decision date, so conviction and invalidation levels embed knowledge of later prices. ROE does not enter `decision` at all ([signal_engine.py:234-284](../signal_engine.py)). Because `total_return` depends on cost basis, holdings come from `trades.csv`. Twenty-four of the 34 symbols reconcile exactly with `portfolio.csv`. The ten that do not reflect bonuses, the JIOFIN demerger and IPO allotments ([refresh_portfolio.py:20-27](../refresh_portfolio.py)). That is why the prompt runs an "actual-book" universe as primary and a labelled hindsight-34 universe as secondary.

The **explicit corporate-actions table** replaces the 2.5x jump heuristic in [analysis.py:51](../analysis.py). The 1:1 bonuses at Reliance and Wipro, and the 1:2 bonuses at GAIL and HPCL, produce 0.5x and 0.67x one-day ratios that the heuristic lets through ([Business Today, RIL bonus](https://www.businesstoday.in/amp/markets/stocks/story/ril-bonus-shares-reliance-fixes-monday-october-28-as-record-date-for-issue-450406-2024-10-16); [Business Standard, Wipro](https://www.business-standard.com/amp/markets/news/dividend-bonus-issue-wipro-rajoo-engg-8-others-to-go-ex-date-next-week-124112900423_1.html); [GAIL filing](https://GAILONLINE.COM/pdf/InvestorsZone/GeneralDisclosure/RecordDateIntimationBonus.pdf)). Practitioners report yfinance producing wrong Indian adjusted histories around corporate events ([Zerodha TradingQnA](https://tradingqna.com/t/has-anyone-found-wrong-adjusted-prices-in-nse-historical-data-for-backtesting/192938)). Renamed tickers are stitched, for example SEQUENT to VIYASH from 23 Jan 2026 ([NSE circular](https://nsearchives.nseindia.com/content/circulars/CML72374.pdf)). Late listings such as Tata Capital (13 Oct 2025) are gated out until they have enough history ([Business Standard](https://www.business-standard.com/markets/news/tata-capital-debuts-flat-on-d-street-should-you-buy-sell-or-hold-125101300172_1.html)).

The **benchmark must include dividends** because the stocks do. Comparing adjusted stock prices with the Nifty 50 price index inflates outperformance by roughly the index dividend yield ([m.Stock](https://www.mstock.com/articles/total-return-index-vs-price-index); [NSE Nifty 50 factsheet](https://www.niftyindices.com/Factsheet//ind_nifty50.pdf)). **Inference runs per date with Newey-West lag 11 and a block bootstrap.** Overlapping 12-month labels make naive errors badly optimistic ([Britten-Jones et al.](https://openaccess.city.ac.uk/id/eprint/15212/1/JBFA%20Overlapping%20observations%20with%20BrittenJones.pdf)). Wilson intervals replace Wald intervals at small n ([Brown, Cai & DasGupta](https://projecteuclid.org/euclid.ss/1009213286)). **The t > 3.0 bar** follows Harvey, Liu and Zhu ([NBER w20592](https://www.nber.org/papers/w20592)). **Purging** stops overlapping labels leaking between train and test ([temporalcv](https://temporalcv.readthedocs.io/en/latest/api/cv_financial.html)). Splitting only the 2023–2025 sample would purge away almost the whole training set, so tuning moves to a 2019–2022 technical-only window. That tuning is penalised by **DSR** ([SSRN 2460551](https://papers.ssrn.com/abstract=2460551)) and **PBO** ([SSRN 2326253](https://papers.ssrn.com/abstract=2326253)). The window starts in Oct 2022 to match your "~3-year" request; the notes analysed Oct 2023 onward. The actual book is thin at the start: it held 10 reconstructable positions at Oct 2023, and the agent should expect fewer in late 2022.

## What the results will and will not tell you

The hindcast will show, for this market path, **whether SELL and TRIM calls were followed by underperformance and BUY/ACCUMULATE calls by outperformance** one year later. It will show how far following the engine beat or lagged simply holding the book (A minus B), and how often trailing-stop TRIMs fire on daily rather than weekly ATR. The path includes Nifty's late-Sep 2024 peak near 26,277 and a roughly 16–17% fall into March 2025 ([Business Standard](https://www.business-standard.com/amp/markets/news/nifty-fall-since-october-2nd-biggest-in-10-years-16-stocks-tank-over-20-125012800225_1.html); [Daily Pioneer](https://dailypioneer.com/news/lessons-from-nifty-50-crash-every-investor-must-know)). Bearish calls made near that trough and scored through the recovery are the stress test for a trend-following engine.

The hindcast will **not** establish general skill. Thirty-seven monthly dates with 12-month overlap hold the information of about **four or five independent observations**, and same-date stocks share market moves. The thesis-invalidation, conviction and ROE paths are switched off, so they remain untested. Because costs and tax are excluded, follow-model results are an **upper bound**. High turnover would face Indian short-term capital-gains tax in real life ([DSP AMC](https://www.dspim.com/knowledge-hub/personal-finance-guide/capital-gains-filing-in-india-what-to-report-where-and-how/stcg-and-ltcg-rules-in-india)). Excess return against Nifty 50 also captures size and style tilt, not only decision quality. Mid-caps diverged from large-caps in 2026 ([Cafemutual](https://cafemutual.com/news/industry/38496-nifty-50-needs-8-gain-to-reclaim-its-peak-abakkus-mutual-fund)). Finally, decisions dated around Oct 2025 cannot be resolved until their 252-session windows close in roughly Nov 2026.

## Decisions for you before pasting

| Decision | Default in prompt | Alternative |
|---|---|---|
| Benchmark | NIFTYBEES adjusted close (TRI proxy) | Download Nifty 50 TRI from niftyindices.com into `data/benchmark/nifty50_tri.csv` |
| Decision window | Oct 2022 – Oct 2025 (37 dates) | Oct 2023 – Oct 2025 (25 dates; fuller actual book) |
| Primary universe | Actual book from `trades.csv` | Hindsight-34 (more names, biased) |
| Tuning stage | Runs only if a class is OUT OF LINE | Skip entirely; validate only |
| Cash rate | 0% | A liquid-fund rate as a sensitivity run |
| Commit price cache | Yes (reproducible) | Keep local if repo size or data licensing concerns you |

## Conclusion

The most useful outcome is a precise "insufficient evidence" verdict, not a headline CAGR. It shows which rules the data can and cannot speak to, and it stops a three-year sample from rewriting parameters on noise. A wrong-sign class, such as trailing-stop TRIMs consistently followed by outperformance, is the signal that justifies a tweak. Even then, the tweak must survive a purged, deflated, preregistered test, and you apply it yourself.
