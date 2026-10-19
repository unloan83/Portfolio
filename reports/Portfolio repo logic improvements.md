# Make the engine stop trading a long-term portfolio

The decision logic in this repo is built like a trading system, but it is advising a long-term investor. That mismatch is now the biggest problem. It is bigger than any single threshold. The repo's own evidence shows it. The 5-year walk-forward in `reports/backtest_summary.md` has the decision engine compounding at **0.64% CAGR with 500.7% annual turnover**, against **13.28% for buy-and-hold** of the same 34 names. The latest run in `re-engineering.csv` (13 Oct 2026) recommends **TRIM on 21 of 34 holdings and SELL on 10**, and most of those trims cite "trailing stop hit", including the Nifty 50 index ETF. The published evidence points the same way. Tight, single-print stops on individual stocks lose to buy-and-hold after costs, because single stocks show short-horizon reversal rather than continuation ([Lo & Remorov, MIT](https://dspace.mit.edu/handle/1721.1/107017)). Indian tax adds a 20% STCG penalty for churn ([DSP AMC](https://www.dspim.com/knowledge-hub/personal-finance-guide/capital-gains-filing-in-india-what-to-report-where-and-how/stcg-and-ltcg-rules-in-india)). The fix has four parts:

- **Price breaches become review triggers.** Sell only on documented thesis failure, which needs falsifiable KPIs in `thesis.csv`, or on a confirmed, severe breach.
- **Size control moves to weights, caps and bands.** It replaces ATR stops.
- **Every proposed trade carries FIFO-based tax and cost estimates.**
- **Signals are scored over 3–12 months against a total-return benchmark.** They are scored by episode, not by intraday run.

The branch `claude/happy-hawking-9b8pow` already has useful scaffolding: data-quality gates, sized actions, Financials and risk-group caps, ETF look-through, XIRR, a FIFO tax planner and a backtest harness. Most of the work is recalibrating rules, not building new modules. Nothing here is personalised financial or tax advice. The thresholds are defaults for you to set and backtest.

## The repo's own numbers show the engine is churning

Three internal measurements agree.

**The backtest.** `backtest_engine.py` replays `evaluate_signal` on weekly bars. It trims **50%** of a position on every TRIM and deducts 0.2% per trade. It produced 500.7% turnover and almost no return. Do not take the 0.64% CAGR at face value, because the harness is flawed in ways that cut both ways:

- It hard-codes `roe=0.15`, `sector_risk_exposure=15.0` and `thesis_text="INTACT"`.
- It applies **today's** `Invalidation_Price` values to 2021 prices, which is look-ahead and likely fires many spurious SELLs early in the window.
- It fills at the same bar's close.
- It falls back to the current price as the "200-DMA" for the first 40 weeks.
- Its universe is today's holdings, which is survivorship bias and flatters buy-and-hold.
- It benchmarks against the ^NSEI price index rather than a TRI.

Even so, a 500% turnover figure cannot come from harness bugs alone. It reflects how readily the rules fire.

**The live run.** On 13 Oct 2026 the engine flagged 31 of 34 holdings for action. The trailing stop is `max(invalidation, 52-week high − 3 × ATR14)`. A daily ATR of roughly 1.5–2.5% of price puts that stop only about 5–8% below the 52-week high (my estimate from typical large-cap ATR, not measured in the repo). That is inside the range where the evidence says trailing stops destroy value: the risk-reduction benefit "disappears for stops tighter than 10% once transaction costs are included" ([AUT/ACFR](https://acfr.aut.ac.nz/research/using-trailing-stop-loss-rules-to-reduce-risk)). On top of that, `size_action` sells half the position whenever the trailing stop is hit.

**The signal scores.** `reports/signal_scores.csv` holds 1,388 scored rows. Collapsing consecutive identical signals per symbol leaves only **about 138 episodes**. The rows are mostly the same standing signal logged three times a day. Every signal class had a negative mean 20-day return over the window: STRG SELL −3.4%, HOLD −5.3%, ACCUMULATE −6.2%. With no benchmark adjustment, this measures the market drawdown, not signal skill. It also shows SELL names falling *less* than HOLD names. Treat this as suggestive at best. Twenty days falls inside India's documented one-month reversal window ([Parthasarathy & Sendilvelu](https://ceeol.com/search/article-detail?id=1054639)), and the sample is tiny.

## Price should open the case and fundamentals should close it

The exit evidence is consistent. Under a random walk, stop-loss rules **always reduce expected return**. They help only when returns persist ([Kaminski & Lo](https://dspace.mit.edu/entities/publication/bb69ca4b-0cdc-487f-831d-63b2e84fafee)). On US single stocks from 1964 to 2014, wide stops checked every 10 days roughly matched buy-and-hold on a risk-adjusted basis. Tight daily stops underperformed. Delaying execution by one day helped, because prices revert ([CXO Advisory](https://www.cxoadvisory.com/equity-premium/stop-losses-on-stock-positions-in-depth)). The 10-month/200-day trend filter is well supported for **indices and asset classes** ([Faber via R-bloggers](https://www.r-bloggers.com/mebane-faber-tactical-asset-allocation-in-r/); [Clare et al.](https://openaccess.city.ac.uk/id/eprint/17846/)). Its evidence for single stocks is thin, and Indian index moving-average gains are eroded by real costs ([Mitra 2011](https://ideas.repec.org/a/taf/quantf/v11y2011i2p287-297.html)). No NSE single-stock stop-loss study was found, so the parameters below are judgement calls that need backtesting.

Against the current `signal_engine.py`, I recommend five changes, in order of impact.

**1. Rebuild the trailing stop.** Today it is "52-week high − 3×ATR14 → TRIM half". Make it **TRIM one-third when the position is up 50% or more and the month-end close is at least `max(30%, 3 × annualised-vol-scaled ATR)` below the 52-week high**. Fire it only on lots older than 12 months; otherwise show "TRIM WATCH (STCG)". A 30% distance sits in the roughly neutral zone of the evidence rather than the destructive one. Exempt broad index ETFs entirely. Trimming a Nifty 50 ETF on a 6% pullback has no thesis rationale.

**2. Demote "price ≤ `Invalidation_Price`" from an immediate STRG SELL to REVIEW.** Escalate to SELL only when one of these holds:
- three consecutive closes below the level;
- a weekly close below it;
- a single close 10% or more below it.

The broker-price fallback path should also produce REVIEW, not SELL. The `role=tactical` exception, such as the conviction-2 gold ETF, can keep a hard price stop.

**3. Remove "BEARISH + negative return + conviction < 4 → SELL".** Replace it with a hysteresis REVIEW. Enter REVIEW when the close is more than 3% below the 200-DMA for 20 or more sessions, or when the month-end close is below the 10-month SMA. Exit REVIEW above 200-DMA + 2%. Escalate to SELL only if REVIEW lasts 60 or more sessions **and** a KPI kill flag is present.

**4. Drop the overextension TRIM** (currently >25% above the 50-DMA, trimming 25%). Keep it as an "EXTENDED – don't add" flag. Selling strength runs against Indian intermediate-horizon momentum evidence ([NSE research paper](https://nsearchives.nseindia.com/content/research/res_paperfinal223.pdf)) and the disposition-effect literature ([Odean](https://faculty.haas.berkeley.edu/odean/papers/disposition/disposition.html)).

**5. Tighten ACCUMULATE.** The current engine already mostly buys strength (price > 50-DMA > 200-DMA), so an earlier note's "±5% of 200-DMA buy zone" no longer applies. The exception is the "Add on weakness (small)" path, which buys **below** the 200-DMA when the return exceeds 25%. Remove it, or require positive 12-month momentum. Add these conditions to ACCUMULATE:
- a *rising* 200-DMA;
- positive volatility-adjusted 6- and 12-month returns, mirroring the Nifty200 Momentum 30 score ([NSE factsheet](https://www.niftyindices.com/Factsheet/Factsheet_Nifty200_Momentum30.pdf));
- price within about 20% of the 52-week high.

Evaluate ACCUMULATE monthly. Momentum carries crash risk: Nifty200 Momentum 30 funds fell about 27–30% from Sep 2024 to Mar 2025 ([Arthgyaan](https://arthgyaan.com/fund/hdfc-nifty200-momentum-30-index-fund-direct-growth/152430)). Weight caps, not unlimited adding, should bound it.

## Construction should run on weights, sleeves and look-through caps, not ATR stops

`risk_manager.size_position` still sizes buys so that a 2×ATR stop risks 0.5% of equity, and quotes an ATR "target". That is a trading-system construct. For a stock with ATR around 2.5% of price it implies roughly a 10% weight; for volatile names it implies tiny ones. It also presumes a stop the investor will not execute. Out-of-sample, **none of 14 optimisation models consistently beat 1/N** ([DeMiguel, Garlappi & Uppal](https://ideas.repec.org/a/oup/rfinst/v22y2009i5p1915-1953.html)). So conviction should be a modest tilt around equal weight with hard caps, and volatility should shrink the cap rather than drive share counts.

The notes conflict on the conviction ladder: 8/5/3/1.5% versus 6/4.5/3/0%. **I recommend 6/4.5/3/0%** for convictions 5/4/3/≤2. A 5.3× spread between tiers bets heavily on conviction scores that have never been validated. A 1.5% "conviction-2" holding is really a watchlist entry, and with about ₹6.4–6.75L invested it is worth about ₹10k. Conviction ≤2 should mean "exit or don't add". The exception is a deliberately tactical sleeve, such as gold.

Precious metals should leave the equity ladder entirely and get their own sleeve: a 10% target, a 7.5–12.5% band, and silver at 4% or less. Indian advisory consensus is 10–15% gold ([Bajaj Finserv](https://bajajfinserv.in/investments/how-much-of-your-portfolio-should-be-invested-in-gold)).

The current code has a single `max_risk_group_pct = 25%`, applied with a "major holding ≥ 4%" rule. The risk groups overlap in practice. On 4 Jun 2024, Nifty PSE fell **16.4%** and Nifty Energy 12.5%, against 5.9% for the Nifty 50 ([ICICI Direct](https://www.icicidirect.com/share-market-today/market-news-commentary/quick-wrap-nifty-pse-index-declines-1638percentage,-nifty-tumbles-593percentage/1518809)). The CPSE index is about 46% power and 36% oil and gas ([Arthgyaan](https://arthgyaan.com/blog/cpse-etf-review.html)). Differentiate the caps:

| Risk group | Cap |
|---|---|
| State-owned | 15% |
| Energy & power | 20% |
| Financials, with look-through | 25% |
| Commodity-linked | 25% |
| Smallcap | 15% |

Apply these to the look-through numbers that `lookthrough.py` already computes. Refresh `data/etf_constituents_*.json` monthly. Separately, `size_action` trims a sector-capped stock by the *entire* sector excess. If two holdings in an over-cap sector both qualify, the sector gets over-trimmed. Allocate the excess across the sector's holdings, trimming lowest-conviction and highest-volatility names first.

For rebalancing, replace the flat "+2pp" idea with **trim only when weight > max(target × 1.25, target + 1.5pp)**, trimming back to target plus half the band. This follows Daryanani's opportunistic ~20% relative band, which with frequent looks added about 0.38% a year ([Kitces reproduction](https://kitces.com/wp-content/uploads/2016/11/An-In-Depth-Look-At-Optimal-Rebalancing-Strategies-Webinar-Handouts.pdf)). It also follows Vanguard's finding that no frequency is optimal while costs rise with frequency ([Vanguard](https://indexacapital.com/bundles/unaiadvisor/docs/papers/2010-Vanguard-Best-practices-for-portfolio-rebalancing.pdf?v=241)). New cash and dividends should go to underweights before any sell is suggested.

Raise `target_core_pct` from 50% toward 55–60%, counting only broad-index ETFs as core. SPIVA India year-end 2025 shows **84.4% of large-cap funds underperforming over five years** ([S&P DJI](https://www.spglobal.com/spdji/en/spiva/article/spiva-india-year-end-2025/)). Add effective-N (1/Σw²) as a reported metric. The portfolio's 34 line items behave like far fewer independent bets, which is the "naive diversification" Goetzmann and Kumar document ([NBER w8686](https://www.nber.org/papers/w8686)).

## Theses need falsifiable KPIs, and data needs an identity layer

All 34 rows of `thesis.csv` follow one template ("Long-term wealth building through conviction in the company's X franchise…"). That leaves `Invalidation_Price` as the only test of a thesis, so "thesis invalidated" in the engine is really a price stop. Practitioners write kill criteria before buying. These are specific, fact-based breaches paired with a "would I buy it today?" test ([Vontobel](https://am.vontobel.com/en/insights/quitters-never-win-or-do-they); [AJ Bell](https://www.ajbell.co.uk/news/why-fund-manager-calls-it-quits-stock)).

Add a `thesis_kpis.csv` with one row per KPI: `symbol, kpi, direction, threshold, persistence_quarters, severity, latest_value, as_of_quarter`. Rename `Invalidation_Price` to `review_price`. Then:
- "THESIS BROKEN" fires only on a persistent KPI kill breach.
- Stale or missing KPIs show as "THESIS UNVERIFIED" and never count as a pass.

Sector KPI sets follow what analysts already track:
- **Banks:** CASA, NIM, RoA, GNPA/NNPA, PCR ([Motilal Oswal via Indian Bank](https://indianbank.in/wp-content/uploads/2024/08/Analyst-Coverage-by-Motilal-Oswal-dated-28th-October-2024-Target-Price-Rs.650.pdf)).
- **Life insurers:** VNB margin, APE and 13th-month persistency. ICICI Pru Life fell 10% on a VNB-margin miss ([Business Standard](https://www.business-standard.com/amp/markets/news/icici-pru-life-down-10-as-vnb-margin-misses-estimates-analysts-cut-target-125012200477_1.html)).
- **Regulated utilities:** regulated-equity growth and the CERC allowed RoE ([FundsIndia](https://fundsindia.com/blog/equities/alpha-ntpc-ltd-equity-research-desk-2/34293)).
- **IT services:** constant-currency growth against guidance, deal TCV and EBIT margin ([IndiaInfoline](https://www.indiainfoline.com/news/companies/wipro-q1-fy27-results-profit-rises-marginally-margins-fall-to-15-quarter-low-stock-gains-1-77)).
- **ETFs:** tracking difference and premium to NAV, with drift-from-target as the trigger.

Drop the `minimum_roe` gate's dependence on yfinance `returnOnEquity`. Yahoo gives only about four years of Indian fundamentals and often omits ratio fields ([TradingQnA](https://tradingqna.com/t/what-are-api-for-getting-fundamental-data-for-stocks-trading-in-nse-india-free-or-paid/145292)). ROE also misreads banks and insurers.

Three thesis rows need correction now:
- **GUJPPL.** The ticker is right. `portfolio.csv` lists the holding as Gujarat Pipavav Port (ISIN INE517F01014), so `GPPL.NS` is correct. The thesis text, which describes gas transmission, is wrong and should be rewritten as a port thesis.
- **TATGLO.** The thesis describes Tata Communications, but the holding is Tata Consumer.
- **ICIPSE.** The thesis describes an "underlying equity portfolio", but the holding is a silver ETF.

The GUJGA holding also needs its quantity, cost basis and review price adjusted for the Gujarat Energy restructuring. GSPL Transmission was demerged at **1 GTL share per 3 Gujarat Energy shares**, record date 2 Jul 2026 ([NSE filing](https://nsearchives.nseindia.com/corporate/GUJGASLTD_19062026181348_1583IntiofRD319062026.pdf)).

`adjust_unadjusted_splits` only catches jumps beyond 2.5×. A 1:1 bonus or 2:1 split shows up as a 0.5× ratio and slips through, and so does every demerger. The current ±25% broker-price gate partly backstops this. The robust fix is an explicit `corporate_actions.csv` using NSE's factor convention: split factor = new/old, bonus (A+B)/B, combined multiplicatively ([NSE circular](https://archives.nseindia.com/content/circulars/FAOP53548.pdf)). Demergers use the company-published cost apportionment. Keep the jump heuristic only as a warning detector.

Add an `instruments.csv` (broker symbol, ISIN, NSE symbol, yf ticker, effective dates, successor) and an ISIN identity check on every run. For data, use the official NSE/BSE UDiFF bhavcopy (the format since Jul 2024) as the primary price source or cross-check ([NSE All Reports](https://www.nseindia.com/all-reports)). Use AMFI `NAVAll.txt` for ETF NAV and premium/discount ([AMFI](https://www.amfiindia.com/net-asset-value/nav-download)). Two cautions apply. NSE's terms prohibit automated scraping ([NSE ToS](https://www.nseindia.com/static/nse-terms-of-use)), so scheduled downloads are your call. If you already hold an account, Angel One SmartAPI (free) or Kite Connect (₹2,000/month with historical data) are sanctioned alternatives ([Zerodha](https://support.zerodha.com/category/trading-and-markets/kite-api/articles/what-are-the-charges-for-kite-apis)).

## Every proposed trade should show its tax and cost before it is suggested

The tax regime from 23 Jul 2024 still applies in FY 2026-27, now under ss.196/198 of the Income-tax Act 2025 ([Income Tax Dept s.196](https://www.incometaxindia.gov.in/w/section-196-78)):
- **STCG:** 20% for listed equity held 12 months or less.
- **LTCG:** 12.5% above ₹1.25 lakh per year, with no indexation ([ClearTax](https://cleartax.in/s/long-term-capital-gains-on-shares)).

`tax_planner.py` already does FIFO matching and tracks the ₹1.25 lakh exemption. It does not distinguish gold and silver ETFs. Those are listed but **not** equity-oriented:
- held over 12 months, they are taxed at 12.5% with **no** ₹1.25 lakh exemption;
- held 12 months or less, they are taxed at slab rates ([Zerodha Fund House](https://www.zerodhafundhouse.com/blog/gold-etf-taxation-2025/)).

One portfolio note cites a 24-month threshold for gold. That applies to gold FoFs and physical gold. For listed ETFs, 12 months is correct. Add an `asset_class` field, a `slab_rate` input and cess. The FIFO ledger also needs corporate-action lots: a zero-cost bonus lot dated at allotment, a demerger child lot inheriting the parent's date, and splits that keep the date. FIFO is mandatory for demat holdings ([CBDT Circular 768](https://www.incometaxindia.gov.in/w/768-circular-no.-768-dated-24-6-1998-1)), so "tax-aware trimming" means choosing *which symbol* and *how many shares* to sell, stopping before FIFO reaches short-term lots. It does not mean choosing lots. Defer any trim whose next lot turns long-term within about 60 days, unless the thesis is broken.

Costs are small next to tax but matter at small ticket sizes. At a zero-brokerage broker, a delivery round trip costs about 0.22% plus a DP charge of about ₹15.34 per scrip per sell day ([Zerodha charges](https://www.zerodha.com/charges); [Finology](https://select.finology.in/articles/broker/dp-charges-in-zerodha)). That works out to roughly **0.53% on a ₹5,000 trade versus 0.38% at ₹10,000**.

The notes conflict on minimum trade size: ₹5k versus ₹10k. **I recommend ₹10,000**, with a soft warning below ₹25k. The one exception is a full exit of a sub-₹10k tail position during consolidation, because otherwise those positions could never be cleaned up.

On harvesting:
- **Loss harvesting** saves tax only when there is STCG to offset, or LTCG above the exemption. Otherwise it merely creates a carry-forward, which requires filing the ITR on time ([Angel One](https://angelone.in/knowledge-center/share-market/wash-sale)).
- **Never rebuy the same scrip the same day.** Zerodha treats a same-day sell and rebuy from holdings as intraday ([Zerodha Z-Connect](https://zerodha.com/z-connect/taxation-for-traders/tax-loss-harvesting)).
- **Gain harvesting** up to the remaining exemption before 31 March is close to free, but the rebought lots restart the 12-month clock. Exclude them from trim candidates for a year.

## Evaluation and alerting must match a multi-month decision horizon

`signal_scorer.py` fetches only `period="1y"`, scores 5/10/20-day raw returns, and mixes the raw logged entry price with dividend-adjusted exits. Redesign it as follows:
- **Score episodes, not runs.** Count one row per state entry, and only after-close runs.
- **Use long horizons.** Score at 63/126/252 trading days, measured as log excess return against Nifty 50 TRI and Nifty 500 TRI. SEBI has required TRI benchmarking for mutual funds since 2018 ([SEBI circular](https://www.sebi.gov.in/sebi_data/attachdocs/jan-2018/1515066187290.pdf)).
- **Report statistics with honest uncertainty.** Give hit rate with Wilson intervals, payoff, expectancy and a bootstrap CI. Mark anything under 30 episodes "insufficient evidence". Hold tuned rules to a t-stat around 3, not 2 ([Harvey, Liu & Zhu](https://nber.org/papers/w20592)).

`performance.py` should also add dividends to the XIRR cash flows and swap the ^NSEI price benchmark for a TRI series. If no TRI feed is available, a Nifty 50 ETF adjusted close is an acceptable flagged fallback.

`backtest_engine.py` needs these changes:
- refactor the engine into a pure `decide(state_at_t)` function shared by live runs and the backtest;
- fill at t+1;
- use point-in-time review prices and fundamentals;
- run a survivorship test on historical holdings plus a Nifty 500 universe;
- deduct real Indian costs and STCG/LTCG;
- log every parameter variant tried, so the Probability of Backtest Overfitting can be computed ([Bailey et al.](https://papers.ssrn.com/abstract=2326253)) and the Deflated Sharpe Ratio applied ([SSRN 2460551](https://papers.ssrn.com/abstract=2460551)).

Keep the custom loop. Avoid backtrader, whose last release was in 2023 ([PyPI](https://pypi.org/project/backtrader/)).

Alerting should follow SRE paging discipline: page only for actionable state changes ([Google SRE](https://sre.google/sre-book/monitoring-distributed-systems/)). Heavy trading is what hurts retail returns. The most active households earned 11.4% against the market's 17.9% ([Barber & Odean](https://faculty.haas.berkeley.edu/odean/papers/returns/returns.html)).

The notes conflict on cooldown: 10 days versus 14. **I recommend 14 calendar days per (symbol, alert type)**, bypassed only when severity escalates. With a Mon/Wed/Fri after-close cadence, 14 days spans about six runs. That is long enough to stop the repeated STRG SELL pages visible in the scores file, and short enough that a real escalation still gets through. Persist state in `alert_state.json`. Require two consecutive after-close confirmations, except for hard triggers. Batch everything else into a Friday digest. Attach an `alert_id` plus tax status to each page, and record your decision in `decision_journal.csv`.

On operations:
- **Schedule.** Replace the three intraday crons (03:50/06:50/09:45 UTC, all before the 15:30 IST close) and the push trigger with off-the-hour after-close crons. GitHub warns that top-of-hour runs may be delayed or dropped ([GitHub docs](https://docs.github.com/en/enterprise-server@3.21/actions/tutorials/manage-your-work/close-inactive-issues)).
- **Holidays.** Add an NSE holiday check using the `holidays` XNSE calendar ([docs](https://holidays.readthedocs.io/en/latest/auto_gen_docs/national_stock_exchange_of_india/)).
- **Concurrency.** Add a concurrency group and `pull --rebase` with retry on both workflows.
- **Missed runs.** Add a dead-man's-switch heartbeat, because `if: failure()` cannot detect a run that never started.
- **Secrets.** Remove the hard-coded Telegram bot-ID prefix and the inline `${{ secrets.* }}` interpolation from `intraday_analysis.yml`. Pass secrets via `env:`, unify the secret names, and consider rotating the token.

## What to do first

| Priority | Change | Files | Why first |
|---|---|---|---|
| 1 | Stop over-trading. Trailing stop becomes 30%+ month-end and trims ⅓ with LT lots only; index ETFs exempt. Invalidation and the 200-DMA SELL become REVIEW with confirmation. Overextension TRIM becomes a flag. Remove "add on weakness" below the 200-DMA. | `signal_engine.py`, `analysis.py`, `config.py` | Today 31 of 34 holdings carry action flags. This is the largest source of cost and tax leakage. |
| 2 | Fix the thesis text for GUJPPL, TATGLO and ICIPSE. Apply the GUJGA/GTL demerger to quantity, cost and review price. Add `corporate_actions.csv` and an ISIN identity check. | `thesis.csv`, `analysis.py`, new CSVs | Wrong inputs corrupt every downstream rule. |
| 3 | Ops and security: after-close crons, holiday check, concurrency, heartbeat, secret hygiene, token rotation. | `.github/workflows/` | Cheap, and it removes the duplicate intraday signals. |
| 4 | Tax and cost layer: gold/silver `asset_class`, slab rate and cess, corporate-action lots, LT-deferral window, ₹10k minimum trade, cost + tax shown on every action. | `tax_planner.py`, `config.py`, `analysis.py` | Makes each remaining recommendation economically honest. |
| 5 | Alert state machine: 14-day cooldown, two-run confirmation, Friday digest, decision journal. | new `alert_state.json`, `analysis.py` | Fewer, better pages; your overrides become measurable. |
| 6 | Construction: 6/4.5/3/0 conviction targets, metals sleeve, differentiated look-through risk-group caps, hybrid bands, ATR sizing confined to a tactical sleeve, core ≥ 55%. | `config.py`, `risk_manager.py`, `core_satellite.py` | Replaces trade sizing with portfolio sizing. |
| 7 | Structured theses: `thesis_kpis.csv`, quarterly manual KPI updates, THESIS UNVERIFIED state. | `thesis.csv`, new `thesis_kpis.csv`, `signal_engine.py` | Gives SELL a non-price basis. Needs your input each results season. |
| 8 | Evaluation: episode scorer at 63/126/252 days against TRI. Backtest refactor (shared `decide()`, t+1 fills, point-in-time inputs, taxes, survivorship variant, PBO/DSR). TRI and dividends in XIRR. | `signal_scorer.py`, `backtest_engine.py`, `performance.py` | Validates steps 1–7. Rerun the 5-year backtest after step 1 as a first check. |

Some choices are yours alone, not the engine's:
- your income-tax slab rate and any surcharge, which drive gold/silver STCG and dividend tax;
- KPI kill and review thresholds and their persistence rules per holding (for example, a private-bank RoA floor);
- conviction scores and which holdings are "tactical" and so keep hard price stops;
- the core target (55% or 60%) and the metals target (10% or higher);
- whether daily scheduled downloads from NSE are acceptable given its terms of use, or whether to pay for a broker API;
- whether to harvest the LIC and Wipro losses now or carry them forward, given your realised gains this year;
- an acceptable alert budget (for example, at most 1–2 urgent pages a week).

Before hard-coding them, re-verify the items the notes flag as unconfirmed: the official s.198 text, STT on equity and gold ETFs, the surcharge cap, and current NSE transaction charges. This report is research synthesis, not personalised financial or tax advice. Consult a chartered accountant before acting on the tax logic.

## Conclusion

The repo has outgrown its weakest assumption. Its infrastructure (data gates, look-through, FIFO tax, XIRR, a backtest harness) is ahead of its decision rules, and those rules still treat a five-year holding like a swing trade. Turnover is the quantity to control. The rest of the roadmap follows from turnover, so judge every rule change first by how many trades it removes. Only after that, by how much downside it avoids.

The deeper shift is in what "SELL" means. Today it means "price crossed a line". After these changes it should mean "a pre-written, measurable reason for owning this is gone". That moves the engine's main input from Yahoo's price feed to your own quarterly reading of results, which is slower and more manual, but it is the only version that can be evaluated honestly. Until the episode-based, TRI-relative scorer has at least a year of matured 126- and 252-day results, treat every rule in this repo, including the ones recommended here, as an unproven hypothesis.
