# Evaluation, Backtesting, Monitoring and Alerting for a Rule-Based Advisory Engine (Indian long-term equity portfolio)

Research date: 2026-10-14. Some primary sites (docs.github.com, niftyindices.com) could not be fetched from the research environment (DNS failure); where that matters, it is flagged in Gaps. PyPI release dates below were pulled live from the PyPI JSON API on 2026-10-14.

Repo observations (read directly from /home/user/Portfolio, not web-sourced):
- `signal_scorer.py` fetches `yf.Ticker(...).history(period="1y")` — so any signal older than ~1 year cannot be scored, and 6/12-month horizons are structurally impossible. `history()` returns dividend/split-adjusted closes by default (yfinance `auto_adjust=True`), but the entry price used is the raw logged `Price_At_Signal` — mixing an unadjusted entry with adjusted exits biases returns downward around ex-dividend dates (and badly around splits/bonuses).
- Scorer measures raw 5/10/20 trading-day returns, no benchmark, one row per (symbol, run_timestamp) — with 3 intraday runs/day, the same standing signal is logged repeatedly, producing heavily overlapping, autocorrelated samples.
- `re-engineering.csv` header: `Analysis_Date, Stock_Symbol, Price_At_Signal, Model_Signal, Trigger_Reason, run_timestamp_ist, current_price, dma_50, dma_200, roe, portfolio_weight_pct, sector, technical_trend, Recommended_Action, Thesis_Status, Conviction, Decision, Horizon_Short_Term, Horizon_Long_Term, Rationale, Data_Status`. Early rows have most columns empty (schema drift).
- `backtest/backtester.py` is a small next-bar-fill walk-forward backtester driven by a `Strategy` protocol; only `run_dma_backtest.py` (DMA crossover) uses it — the real decision engine is never backtested.
- `.github/workflows/intraday_analysis.yml`: crons at 03:50, 06:50, 09:45 UTC Mon–Fri (intraday, i.e. *before* NSE close at 15:30 IST) plus `0 12 * * 5` (top of the hour); also runs on every push to main; comment admits NSE holidays are not excluded. No `concurrency:` group. Secrets are interpolated directly into `run:` scripts via `${{ secrets.* }}`; the success step hard-codes a Telegram bot-ID prefix (`8526197794:`) into the workflow file; success and failure steps use different secret-name fallbacks (failure step only reads `TELEGRAM_TOKEN`/`TELEGRAM_TO`). Failure alert fires only on `failure()` of steps in this job — a schedule that never fires produces no alert.
- `.github/workflows/signal_scoring.yml`: Sunday `0 0 * * 0` (top of hour, UTC), checkout without `fetch-depth`, pushes to main with no rebase/retry and no failure notification.

---

## 1. Correct portfolio performance measurement (XIRR vs TWR, benchmark, TRI data, dividends)

### Takeaway
Report both: money-weighted return (XIRR) answers "how did *my* money do", time-weighted return (TWR) answers "how good were the *decisions/engine*" independent of when the investor added cash. Compare against a Total Return Index (dividends reinvested), not a price index — Nifty 50 TRI as the headline and Nifty 500 TRI (or a multicap TRI) as a breadth check if the portfolio holds mid/small caps; the benchmark must be run through the same cash-flow dates ("PME"/mirror-portfolio XIRR) to be comparable to the investor's XIRR.

### Cited Findings
- GIPS requires time-weighted returns as the default because TWR "removes the effects of external cash flows, which are generally client-driven" — [AcadiFi summary of GIPS](https://www.acadifi.com/community/gips-performance-calculation-time-weighted-money-weighted); [AnalystPrep CFA L3 notes](https://analystprep.com/study-notes/cfa-level-iii/time-weighted-return/)
- Money-weighted returns are permitted under GIPS when the firm *controls* external cash flows (closed-end/fixed-life/fixed-commitment, or illiquid holdings significant); since the 2020 GIPS standards, daily external cash flows must be considered; returns for periods under one year should not be annualized — [AnalystPrep](https://analystprep.com/study-notes/cfa-level-iii/time-weighted-return/) (secondary; verify against GIPS 2020 text)
- TWR is best for comparing managers of liquid portfolios; MWR (= dollar-weighted = IRR) is best for judging an investor's actual outcome — [Asora](https://www.asora.com/blog/time-weighted-vs-money-weighted-return); see also the "whose performance matters, investor's or manager's" framing — [Thinking Ahead Institute](https://www.thinkingaheadinstitute.org/news/article/whose-performance-matters-more-the-investors-or-the-managers/); [PWL Capital](https://pwlcapital.com/calculating-understanding-portfolio-returns/)
- SEBI circular SEBI/HO/IMD/DF3/CIR/P/2018/04 (4 Jan 2018, effective 1 Feb 2018): "The performance of the schemes of a mutual fund shall be benchmarked to the Total Return variant of the index"; TRI "takes into account all dividends/interest payments ... in addition to the capital gains"; where TRI history is missing, use a composite CAGR of PRI up to TRI start then TRI thereafter, with disclosure — [SEBI circular PDF](https://www.sebi.gov.in/sebi_data/attachdocs/jan-2018/1515066187290.pdf); [Business Standard](https://www.business-standard.com/amp/article/pti-stories/adopt-total-return-index-to-benchmark-schemes-sebi-to-mfs-118010400873_1.html)
- Before the mandate most equity schemes used price-return indices; coverage noted TRI makes it harder to show wide outperformance — [Business Standard](https://www.business-standard.com/amp/article/pti-stories/adopt-total-return-index-to-benchmark-schemes-sebi-to-mfs-118010400873_1.html)
- APMI (portfolio managers' association) in 2023 applied the same composite PRI→TRI method for PMS reporting against BSE 500 TRI, noting BSE 500 TRI history is ~15 years — [APMI Circular 6](https://www.apmiindia.org/storagebox/images/Circulars/APMI%20Circular%206-%20Reporting%20of%20Performance%20(BSE%20500%20TRI)%20-28th%20Apr'23_1.pdf)
- Nifty 50 TRI assumes every dividend is reinvested into the index on its ex-date — [Craytheon (Nifty 50 rolling returns)](https://craytheon.com/charts/nifty-50-rolling-returns/); Nifty 50 TRI 10-yr CAGR ~13.38% as of 5 May 2026 citing NSE Indices — [Bajaj AMC](https://www.bajajamc.com/knowledge-centre/nifty-50-historical-returns)
- TRI history for ~52 NSE indices has historically been pulled from NSE Indices' site; freefincal's Excel tool automates this (2017-era, may be outdated) — [freefincal](https://freefincal.com/download-historical-total-returns-index-data-52-nse-indices/); [freefincal Nifty data](https://freefincal.com/download-nifty-historical-data-price-total-returns-pe-pb-div-yield/)
- Python XIRR: `pyxirr` 0.10.8 (released 2025-11-03) — [PyPI pyxirr](https://pypi.org/project/pyxirr/)

### Inferences
- Use XIRR for the investor's headline and a "benchmark XIRR": replay every actual buy/sell/dividend date as a purchase/redemption of Nifty 50 TRI units and compute that XIRR (public-market-equivalent). Comparing portfolio XIRR to a point-to-point index CAGR is apples-to-oranges when cash flows are irregular.
- Use TWR (daily or sub-period linked at each cash flow) to evaluate the *engine*, since the investor, not the engine, decides contribution timing.
- Dividends: record them as positive cash flows in the XIRR stream (or reinvested in TWR). If only price index is used for the benchmark while portfolio includes dividends (or vice-versa), the comparison is biased by roughly the index dividend yield (~1–1.5%/yr for Nifty 50 — not verified this session).
- Benchmark choice: Nifty 50 TRI is appropriate if holdings are mostly large caps; if the portfolio holds small/mid caps (ASHLEY etc. appear in the CSV), Nifty 500 TRI is the fairer "investable universe" benchmark. Report both.
- Practical fallback when TRI download is awkward: track an index ETF (e.g., a Nifty 50 ETF on yfinance) using adjusted close — this approximates TRI minus the ETF's expense ratio and tracking error.

### Gaps
- Could not fetch niftyindices.com (DNS failure) to confirm current URL, format, and date-range limits for TRI downloads, or whether an API/CSV endpoint exists in 2026.
- Official GIPS 2020 text not fetched; GIPS points rely on CFA-study secondary sources.
- Did not verify whether the 2018 SEBI circular was later superseded (e.g., by SEBI Master Circular for MFs, 2024); the TRI requirement is believed to persist.

---

## 2. How to evaluate signals properly

### Takeaway
Measure *excess* return vs the benchmark (or vs the stock's sector), at horizons matched to the engine's intent (for a long-term portfolio: 3, 6, 12 months, with 1-month only as a sanity check), using one observation per *signal episode* (state entry), not per daily run. With small samples, report hit rate *and* payoff ratio with bootstrap confidence intervals, treat t < ~3 as unproven given the number of rules tried, and use rank IC (Spearman) between signal score and forward excess return when the engine outputs graded scores.

### Cited Findings
- Harvey, Liu & Zhu: given extensive data mining, a newly discovered factor needs a t-ratio above ~3.0 rather than the conventional 2.0; "most claimed research findings in financial economics are likely false" — [NBER w20592](https://nber.org/papers/w20592); [SSRN 2513152](https://papers.ssrn.com/abstract=2513152); published RFS 29(1):5–68 (2016)
- Deflated Sharpe Ratio (Bailey & López de Prado, JPM 40(5):94–107, 2014) corrects for selection bias under multiple testing and non-normal returns; not controlling for the number of trials leads to over-optimistic expectations — [SSRN 2460551](https://papers.ssrn.com/abstract=2460551); [Wikipedia: DSR](https://en.wikipedia.org/wiki/Deflated_Sharpe_ratio)
- DSR also accounts for sample length — i.e., short track records need much higher observed Sharpe to be credible — [Wikipedia: DSR](https://en.wikipedia.org/wiki/Deflated_Sharpe_ratio)

### Inferences (methodology; standard practice, not individually sourced here)
- **Excess return**: `r_excess = r_stock(t→t+h) − r_benchmark_TRI(t→t+h)`; use log returns so horizons aggregate. For SELL/WATCH signals, "correct" means negative excess return (avoided underperformance); for BUY/ADD, positive.
- **Non-overlapping samples**: collapse consecutive runs with the same `Decision` into one episode (start date = first run in new state). Score each episode once at each horizon. Alternatively, keep overlapping data but compute standard errors with Newey–West (lag = horizon − 1) or a block bootstrap.
- **Horizon choice**: an engine driven by 200-DMA, ROE, and thesis status is a multi-month signal; 5/10/20-day returns are mostly noise for it. Use 63/126/252 trading days (≈3/6/12 months). This requires ≥ 1–2 years of price history beyond the signal date (current `period="1y"` makes 12-month scoring impossible).
- **Hit rate vs payoff**: report `hit_rate`, `avg_win`, `avg_loss`, `payoff = avg_win/|avg_loss|`, and `expectancy = hit·avg_win − (1−hit)·|avg_loss|`. A 40% hit rate SELL rule can still be valuable if it avoids large drawdowns.
- **Small samples**: with, e.g., 20 SELL episodes, a 95% CI on hit rate is roughly ±22 pp (binomial); use Wilson intervals for hit rate and bootstrap CIs (10k resamples, block by month to respect cross-sectional correlation) for mean excess return. Signals on the same date across stocks are correlated (common market factor), so the effective N is closer to the number of distinct dates than the number of rows.
- **Information coefficient**: if the engine has an ordinal score (e.g., STRONG SELL < SELL < WATCH < HOLD < BUY, or Conviction), compute the Spearman rank correlation between score and subsequent excess return per date (cross-sectional IC), then average across dates; report mean IC, IC std, and IC t-stat (= mean/std·√N_dates). For a ~20–40 stock portfolio cross-sectional IC will be very noisy; pool across time.
- **Baseline comparisons**: compare every signal class against "all holdings unconditional excess return" in the same windows — a SELL signal that is followed by −2% excess is meaningless if every holding averaged −2% excess.
- **Multiple testing**: count how many rule variants/thresholds were tried when tuning the engine; carry that number into DSR / Bonferroni-style hurdles.

### Gaps
- Did not retrieve a primary reference for Grinold's Fundamental Law / IC conventions; IC methodology is standard practice but uncited here.
- No sourced guidance found specific to evaluating *advisory* (non-trading) signals for Indian retail portfolios.

---

## 3. Backtesting pitfalls and tools

### Takeaway
The real decision engine must be run point-in-time on historical data (walk-forward, next-day fills, Indian costs and taxes), on a survivorship-free universe, with corporate actions adjusted from verified data; any parameter tuning should be assessed with PBO (CSCV) and the Deflated Sharpe Ratio. The existing in-house `backtester.py` is adequate if extended with a strategy adapter; of the libraries, vectorbt and bt are actively maintained in 2026, zipline-reloaded is maintained but slower-moving, backtrader is effectively unmaintained.

### Cited Findings
- **PBO**: Bailey, Borwein, López de Prado & Zhu, "The Probability of Backtest Overfitting" — standard hold-out safeguards are "unreliable and inaccurate in the context of investment backtests"; they propose PBO estimated via combinatorially symmetric cross-validation (CSCV) — [SSRN 2326253](https://papers.ssrn.com/abstract=2326253); published J. Computational Finance 20(4) (2017), DOI 10.21314/jcf.2016.322 — [RePEc](https://ideas.repec.org/a/rsk/journ0/2471206.html); full text — [eScholarship PDF](https://escholarship.org/content/qt4w1110bb/qt4w1110bb.pdf)
- R package `pbo` implements CSCV (using Omega ratio; authors used Sharpe) — [CRAN pbo README](https://ftp.fau.de/cran/web/packages/pbo/readme/README.html)
- **Deflated Sharpe** — see Q2 — [SSRN 2460551](https://papers.ssrn.com/abstract=2460551)
- **Corporate actions / data quality on NSE via yfinance**: user reports of yfinance dividend values not matching NSE (Reliance 2020: 3.25 vs 6.50, later reported correct), adjusted values that "don't always match NSE", and a reported mishandling of the HDFC Bank demerger (anecdotal); advice to verify splits/corporate actions against NSE — [Zerodha TradingQnA](https://tradingqna.com/t/has-anyone-found-wrong-adjusted-prices-in-nse-historical-data-for-backtesting/192938); adjustment conventions differ (multiplicative dividend factor vs subtraction) — [MathWorks adjusted prices](https://www.mathworks.com/help/finance/adjustedclosingprices.html)
- **Indian taxes (from 23 Jul 2024)**: STCG on listed equity 20%; LTCG 12.5% on gains above ₹1.25 lakh per FY; long-term holding period remains 12 months; concessional treatment conditional on STT paid — [DSP MF](https://www.dspim.com/knowledge-hub/personal-finance-guide/capital-gains-filing-in-india-what-to-report-where-and-how/stcg-and-ltcg-rules-in-india); [Outlook Money](https://www.outlookmoney.com/news/budget-2024-25-ltcg-raised-to-125-what-it-means-for-you); secondary source says no significant change in Budgets 2025/2026 — [Finnovate](https://www.finnovate.in/learn/blog/capital-gains-tax-india-explained) (unverified against Finance Act)
- **Library maintenance (PyPI latest release, fetched 2026-10-14)**:
  - vectorbt 1.1.2 — released 2026-10-09 — [PyPI](https://pypi.org/project/vectorbt/); Snyk rates maintenance "sustainable", ~6k stars — [Snyk](https://security.snyk.io/package/pip/vectorbt); a paid "PRO" version exists — [stork.ai](https://www.stork.ai/en/vectorbt) (vendor page)
  - bt 1.4.1 — released 2026-10-10 — [PyPI](https://pypi.org/project/bt/)
  - zipline-reloaded 3.1.1 — released 2025-07-19 — [PyPI](https://pypi.org/project/zipline-reloaded/); community fork after Quantopian shutdown — [quantt.co.uk](https://www.quantt.co.uk/resources/quantopian-alternatives-guide) (secondary)
  - backtrader 1.9.78.123 — last release 2023-04-19 — [PyPI](https://pypi.org/project/backtrader/); described as stable but no longer actively maintained by the original author — [quantt.co.uk comparison](https://www.quantt.co.uk/resources/backtesting-platforms-comparison); [AlgoLab 2026 comparison](https://algolab.co.kr/blog/python-backtesting-library-comparison-2026)
  - Supporting libs: quantstats 0.0.86 (2026-09-27), empyrical-reloaded 0.5.12 (2025-06-01), exchange-calendars 4.13.2 (2026-03-10), pandas-market-calendars 5.5.0 (2026-10-05) — PyPI JSON API

### Inferences
- **Look-ahead bias**: the engine uses close-based DMAs and fundamentals (ROE). In a backtest, (a) a signal computed from day-t close can only be acted on at day t+1 open/close; (b) ROE must be the value *as published* at t (point-in-time), not today's trailing ROE — yfinance fundamentals are current snapshots, so backtesting ROE-based rules with yfinance is look-ahead-biased. Either freeze fundamentals as logged in `re-engineering.csv` (true point-in-time going forward) or lag annual-report data by ≥ 60–90 days.
- **Survivorship bias**: backtesting only today's holdings (stocks the investor still owns or that survived) overstates returns. For engine evaluation, use the historical holdings set as of each date (from `portfolio.csv`/trades history) plus delisted names, or a historical index-constituent universe (e.g., Nifty 500 constituents by date).
- **Costs to model** (per side, delivery): brokerage (₹0 at many discount brokers for delivery), STT, exchange transaction charges, SEBI fee, stamp duty (buy), GST on brokerage+charges, DP charge on sell, plus slippage (≥ 10–25 bps for small caps). Taxes: apply STCG 20% if sold < 12 months, LTCG 12.5% above ₹1.25 lakh/FY — tax drag strongly penalizes SELL rules that churn sub-12-month positions. (Exact non-tax charge rates were not verified this session.)
- **Thin "real" history**: the engine's decision log starts ~2026-05; it's too short for statistical conclusions. A historical replay of the engine (re-running decision logic on past data) is the only way to get multi-year evidence, but it inherits the look-ahead issues above.
- **Walk-forward**: tune on rolling windows (e.g., 5-yr train / 1-yr test, step 1 yr), report only concatenated out-of-sample results; freeze parameters between reviews.
- **Tool choice**: For a portfolio of ~20–50 names with weekly decisions, a custom event-driven loop (the existing `backtester.py`) is simpler and more transparent than any framework; use vectorbt only for fast parameter sweeps (feed sweep results into CSCV/PBO), and `quantstats`/`empyrical-reloaded` for tear-sheet metrics. Avoid backtrader for new work given no release since 2023.

### Gaps
- No Python PBO/CSCV package verified (R `pbo` exists); implementing CSCV in ~50 lines of numpy is straightforward but uncited.
- Current Indian delivery charge schedule (STT %, stamp duty, exchange fees) not verified this session — check NSE/broker charge pages.
- Point-in-time Indian fundamentals sources (free) not researched.

---

## 4. Alert design for investors (hysteresis, cooldown, fatigue, journaling) and behavioural evidence

### Takeaway
Behavioural evidence (Barber & Odean; Odean's disposition effect; SEBI's derivatives-trader studies) shows frequent, emotionally-driven trading destroys retail returns, so the alert system should be deliberately low-frequency and "page" only on actionable state transitions confirmed after close, with hysteresis bands, minimum dwell time and cooldowns, and everything else batched into a weekly digest; each alert should require a journaled decision.

### Cited Findings
- Barber & Odean, "Trading Is Hazardous to Your Wealth" (66,465 households, 1991–96): average household earned 16.4%/yr with ~75% annual turnover; the most active traders earned 11.4% vs market 17.9%; attributed to overconfidence — [Odean faculty page](https://faculty.haas.berkeley.edu/odean/papers/returns/returns.html); counter-view: rational agents with adjustment costs can reproduce these patterns — [NBER w16022](https://www.nber.org/papers/w16022.pdf)
- Odean (1998, J. Finance 53(5):1775–1798), 10,000 discount-brokerage accounts: investors realize gains more readily than losses (disposition effect), which is non-optimal for taxable investors and lowers after-tax returns — [Odean faculty page](https://faculty.haas.berkeley.edu/odean/papers/disposition/disposition.html); reported PGR ≈14.8% vs PLR ≈9.8% outside December (secondary) — [Wikipedia](https://en.wikipedia.org/wiki/Disposition_effect)
- SEBI FY24 study (Sept 2024): >91% of individual F&O traders lost money; FY22–FY24, 93% of >1 crore traders lost, aggregate >₹1.8 lakh crore — [Value Research](https://www.valueresearchonline.com/stories/222075/sebi-report-91-per-cent-f-o-traders-lost-money-in-fy-24); FY25 update (July 2025): net losses rose ~41% to ₹1,05,603 crore, >91% still loss-making — [Business Standard](https://www.business-standard.com/amp/markets/news/net-losses-of-traders-in-fo-widens-in-fy25-sebi-study-125070701221_1.html); [Moneylife](https://moneylife.in/article/91-percentage-of-retail-traders-lost-money-in-derivatives-losses-in-fo-surged-41-percentage-to-rs105-lakh-crore-in-fy25-sebi-study/77613.html) (Moneylife describes a Dec 2024–May 2025 window — period labeling conflicts between sources)
- Google SRE book: paging a human is expensive; never alert because "something seems a bit weird"; separate pages (immediate action), tickets (action later) and logs (no notification) — [SRE book ch. 6](https://sre.google/sre-book/monitoring-distributed-systems/); transient unactionable alerts taught engineers to ignore alerts, masking real problems (Bigtable example, secondary) — [Bizarro DEV summary](https://bizarro.dev.to/codingblocks/site-reliability-engineering-still-monitoring-distributed-systems)

### Inferences
- The SEBI studies concern F&O traders, not long-term cash-equity investors; they support the general case against high-frequency retail activity but should be cited as such, not as evidence about delivery investing.
- Map SRE tiers to the engine: **Urgent (page)** = new entry into SELL / STRONG SELL, thesis BROKEN, or price entering a predefined buy zone for a watchlist stock; **Digest (ticket)** = WATCH entries/exits, conviction changes, weight drift; **Log only** = unchanged states, intraday noise.
- **Hysteresis**: use separate entry/exit thresholds, e.g., enter "below-200DMA breakdown" at close < 0.97 × DMA200, exit only at close > 1.02 × DMA200; buy-zone enter at ≤ target, exit at ≥ target × 1.05. This prevents flip-flopping around a line.
- **Debounce / confirmation**: require the condition on N consecutive *after-close* evaluations (e.g., 2 of the Mon/Wed/Fri runs) before alerting SELL, except for hard triggers (thesis break, >X% single-day drop).
- **Cooldown**: per (symbol, alert_type), suppress repeats for e.g. 14 calendar days unless severity escalates (WATCH→SELL→STRONG SELL); cooldown resets on state exit.
- **Fatigue budget**: target ≤ 1–2 urgent alerts per week across the whole portfolio; if exceeded over a month, review thresholds.
- **Decision journaling**: each urgent alert carries an ID; the investor records `acted / deferred / overridden` + reason; later scoring compares engine-vs-human decisions (makes disposition effect measurable: e.g., overrides of SELLs on losers).
- **Tax-aware alerts**: annotate SELL alerts with holding-period days and whether selling now crystallizes STCG (20%) vs waiting for LTCG (12.5%) — directly counters the disposition-effect/tax interplay Odean documents.

### Gaps
- No peer-reviewed study found specifically on alert frequency for retail investors (e.g., push-notification effects on trading); evidence is indirect (trading frequency studies, SRE practice).
- Did not retrieve SEBI's cash-segment (intraday equity) study, which would be more relevant than F&O.

---

## 5. Operational robustness for GitHub Actions cron jobs

### Takeaway
GitHub cron is best-effort: runs can be delayed or dropped at high load (worst at the top of the hour), are UTC-only, run from the default branch, and may be auto-disabled after repository inactivity — so make jobs idempotent (keyed by NSE trading date), holiday-aware via a calendar library, concurrency-guarded, and monitored by an external heartbeat/"dead man's switch" that alerts when an expected run did *not* happen.

### Cited Findings
- GitHub docs (via mirrored text): "The schedule event can be delayed during periods of high loads ... High load times include the start of every hour. If the load is sufficiently high enough, some queued jobs may be dropped. To decrease the chance of delay, schedule your workflow to run at a different time of the hour." — [GitHub docs mirror (close inactive issues tutorial)](https://docs.github.com/en/enterprise-server@3.21/actions/tutorials/manage-your-work/close-inactive-issues); [docs mirror commit](https://source-hub.etos-pro.ru/github/docs/commit/6e33ce1553a5ad6c5a560a399ac41a5031132156)
- Third-party sources state scheduled workflows in public repos are auto-disabled after 60 days without repository activity, silently — [cronuru guide](https://cronuru.com/guides/github-actions-scheduled-workflows); [runhooks blog](https://runhooks.app/blog/github-actions-scheduled-workflows-unreliable/) (not verified against official docs this session)
- A community thread reports a pushed commit to the default branch resynced stuck schedules — [GitHub community #185355](https://github.com/orgs/community/discussions/185355)
- Vendor monitoring services (heartbeat/dead-man's-switch) for GitHub Actions exist — [cronping](https://cronping.com/solutions/github-actions)
- NSE holiday calendars in Python: `holidays` library has a financial calendar for NSE (code XNSE) — [holidays docs](https://holidays.readthedocs.io/en/latest/auto_gen_docs/national_stock_exchange_of_india/); pandas_market_calendars ships an XBOM (BSE) calendar as package code, not fetched at runtime — accuracy depends on installed version — [pandas_market_calendars docs](https://pandas-market-calendars.readthedocs.io/en/latest/pandas_market_calendars.html); a vendor post claims pandas_market_calendars misses special sessions such as Muhurat trading (unverified, commercial) — [DEV post](https://dev.to/aion-analytics-india/why-pandasmarketcalendars-fails-for-indian-markets-and-what-to-use-instead-1207)

### Inferences
- **Holiday check**: first step of the job: `python -m ops.is_trading_day` exits 0/"skip" if today (IST) is not an NSE session; plus a data-freshness check — if the latest yfinance bar date ≠ today's IST date, mark run `STALE` and do not emit decision-change alerts. Belt-and-braces: keep a small `nse_holidays_<year>.csv` committed from NSE's annual holiday circular and assert library and file agree.
- **After-close timing**: NSE closes 15:30 IST (= 10:00 UTC); yfinance EOD bars settle later. Schedule e.g. `17 12 * * 1,3,5` (17:47 IST) — off the hour — and accept delays; idempotency handles late/duplicate runs.
- **Idempotency**: key every write by `(trading_date, symbol)`; if a row for today's trading date already exists, update rather than append; alert dedupe via a persisted `alert_state.json` so a re-run never re-sends.
- **Concurrency**: add `concurrency: {group: portfolio-main, cancel-in-progress: false}` to *both* workflows (both push to main); use `git pull --rebase` with retry before push.
- **Missed-run detection**: a dead-man's switch (healthchecks.io-style ping at end of successful run; external service alerts if no ping in ~50 h), since `if: failure()` cannot fire for a run that never started. Also a weekly keepalive commit (the Friday digest commit naturally serves this) avoids inactivity disablement.
- **Secrets**: pass secrets via `env:` and reference `$TELEGRAM_TOKEN` in shell, rather than `${{ secrets.X }}` inside `run:` text (avoids script-injection patterns and accidental echo); store the full bot token as a single secret — don't hard-code the bot ID in the workflow; unify secret names; set least-privilege `permissions:` per job; pin actions to commit SHAs. (GitHub's security-hardening guide recommends these but could not be fetched this session.)

### Gaps
- docs.github.com was unreachable; the 60-day inactivity rule, scheduling minimum interval (5 min), timezone support for `schedule`, and hardening guidance are stated from memory/third parties and should be verified.
- Did not verify whether exchange_calendars includes an XNSE calendar in v4.13.2 (only XBOM confirmed via pandas_market_calendars docs).

---

## Recommended changes for the repo

### A. Scorer redesign (`signal_scorer.py` → `evaluation/`)
1. **Episodes, not runs**: build `signal_episodes.csv` from `re-engineering.csv`: one row per (symbol, decision-state entry) with `episode_id, symbol, state, entry_trading_date, entry_close_raw, exit_trading_date, prev_state, conviction, data_status`. Only after-close runs count.
2. **Prices**: fetch `period="max"` (or since earliest signal − 1 y), `auto_adjust=False`; compute total-return series yourself from raw close + dividends + splits, and verify corporate actions against NSE for held names. Entry price = *same series* as exit price (never mix logged raw price with adjusted closes).
3. **Benchmarks**: Nifty 50 TRI (headline) and Nifty 500 TRI (breadth) from NSE Indices historical data, cached in `data/benchmarks/*.csv`; fallback: Nifty 50 ETF adjusted close, flagged.
4. **Horizons**: 21/63/126/252 trading days; primary metric = log excess return vs TRI at 126 and 252 days. Mark horizons `pending` until matured; never drop immature rows.
5. **Metrics per state**: N episodes, N distinct dates, hit rate (Wilson 95% CI), mean/median excess return (block-bootstrap CI by month), payoff ratio, expectancy, max adverse excursion; rank IC (Spearman) of ordinal decision/conviction vs 126-day excess return; compare against unconditional "all holdings" baseline. Flag any result with N < 30 episodes as "insufficient evidence".
6. **Engine vs human**: join with trade history and decision journal to report (a) engine-recommended vs actual action, (b) excess return of overridden recommendations.

### B. Backtest harness spec (`backtest/`)
1. Add an `EngineStrategy` adapter implementing the existing `Strategy` protocol that calls the *same* decision function used by `analysis.py` (refactor the decision logic into a pure function `decide(state_at_t) -> Decision`), so live and backtest share code.
2. Point-in-time inputs only: prices up to t close; fundamentals lagged (≥ 90 days after FY end) or sourced from logged values; actions filled at t+1 close (or open).
3. Universe: historical holdings by date (from trades/portfolio history) plus a Nifty 500 historical-constituents variant to test survivorship sensitivity.
4. Costs: per-side delivery charges + slippage (bps by market-cap bucket) + Indian capital-gains tax (STCG 20% < 12 m, LTCG 12.5% above ₹1.25 lakh/FY) applied on realized gains; report pre- and post-tax.
5. Outputs: TWR, XIRR, CAGR, max drawdown, turnover, tax paid, excess vs Nifty 50 TRI and Nifty 500 TRI, plus a "buy-and-hold initial portfolio" and "all-in index" baseline.
6. Validation: walk-forward (e.g., 5y train/1y test rolling); any parameter sweep (DMA lengths, buffers, ROE cutoffs) logs the number of trials; compute DSR for the chosen config and PBO via CSCV over the sweep matrix (S=16 blocks); reject configs with PBO > 0.5 or DSR < 0.95.
7. Libraries: keep custom loop; optional vectorbt (actively released, 1.1.2 Oct 2026) for sweeps; quantstats for tear sheets; pyxirr for XIRR; do not adopt backtrader.

### C. Alerting/state rules
1. Persist `state/alert_state.json` (committed): per symbol `{state, state_since, confirm_count, last_alert_at, last_alert_type, cooldown_until, journal_status}`.
2. Runs Mon/Wed/Fri after close only; drop the three intraday crons (or keep them as log-only, never alerting).
3. Urgent alert iff: transition into SELL/STRONG SELL/THESIS BROKEN/BUY-ZONE, confirmed on 2 consecutive after-close runs (hard triggers bypass confirmation), hysteresis buffer satisfied (e.g., ±2–3% around DMA/target), and not in cooldown (14 days per symbol+type, bypassed only on severity escalation).
4. Friday digest: all state changes of the week, WATCH list, cooldown-suppressed events, pending journal entries, portfolio XIRR vs benchmark-XIRR (Nifty 50 TRI PME), TWR YTD, and signal-scorecard snapshot.
5. Each urgent alert includes holding period, unrealized gain, tax status (STCG/LTCG, days to LTCG), and an `alert_id`; journal file `decision_journal.csv` (`alert_id, decided_at, action, reason`). Unanswered alerts resurface in the digest, not as new pages.
6. Fatigue guard: if > 4 urgent alerts in 7 days, collapse further ones into the digest and flag "threshold review".

### D. Ops fixes (`.github/workflows/`)
1. Cron off the hour, after close: e.g. `47 11 * * 1,3,5` (17:17 IST) and digest `47 12 * * 5`; scorer `23 1 * * 6`. Remove `push:` trigger from analysis (or make push runs dry-run/no-alert).
2. First step: NSE trading-day check (`holidays` XNSE / pandas_market_calendars + committed NSE holiday CSV); data-freshness check (latest bar date == today IST) else `STALE`, no alerts.
3. Idempotency: upsert by `(trading_date, symbol)`; alert dedupe through `alert_state.json`.
4. `concurrency: { group: portfolio-main, cancel-in-progress: false }` on both workflows; `git pull --rebase` + retry loop before push; `fetch-depth: 0` in scorer too.
5. Dead-man's switch: ping an external heartbeat at end of each successful run; alert if no ping within ~50 h on trading weeks. Add failure notifications to `signal_scoring.yml`.
6. Secrets: move the full Telegram token into one secret; delete the hard-coded `8526197794:` prefix from `intraday_analysis.yml`; pass via `env:` and use `$VAR` in scripts; standardize on `TELEGRAM_BOT_TOKEN`/`TELEGRAM_CHAT_ID`; consider rotating the token since part of it is in git history; pin actions by SHA; per-job least-privilege permissions.
7. Schema hygiene: `re-engineering.csv` early rows lack most columns; add a `schema_version` column and a validation step that fails the run on missing required fields.
