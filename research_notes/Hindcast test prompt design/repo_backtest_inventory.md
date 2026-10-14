# Repo backtest / hindcast inventory and gap analysis

Scope: what already exists in `/home/user/Portfolio` (branch `claude/happy-hawking-9b8pow`, HEAD `9381933`) compared with the target test: replay `signal_engine.evaluate_signal` / `analysis.py` logic at monthly decision dates from Oct 2023 to Oct 2025, using only data known at each date. Each decision is then checked against the actual result 252 trading days later, measured against Nifty 50. The test reports per-decision hit rates and compares follow-the-model, do-nothing and Nifty. It then tunes a small parameter grid on a train window and confirms on a held-out window. Tax and transaction costs are excluded.

The notes cite repo files as sources (path:line). All checks were run locally and offline: `git log`, pandas snippets on the CSVs, the existing `ingest_pdf_statements.parse_agts_pdf` called read-only, and `pytest` on 3 test files (26 passed). Nothing in the repo was modified.

## Q1. What do the existing backtest/scoring modules do?

### Takeaway
The repo has three replay tools and one forward-return scorer. None of them comes close to the target test. `backtest_engine.py` (added 2026-10-13) is the only one that calls the full `evaluate_signal` decision tree. It runs weekly bars from 2021-10 to 2026-10 with same-bar fills, and it applies today's thesis, invalidation prices, ROE and sector exposure to the past. It reports only CAGR, max drawdown and turnover. It has no per-decision verification, no 1-year horizon and no train/test split. `backtest/` and `scratch/run_cross_validation.py` test only the 50/200-DMA trend layer. `signal_scorer.py` scores live-logged signals at 5, 10 and 20 days, without a benchmark.

### Cited Findings

**backtest_engine.py (356 lines, commit c5d6361, 2026-10-13, "Part L")**
- Fetches `period="5y"` daily history per symbol from Yahoo and resamples it to weekly `W-FRI` bars. It can cache to `scratch/weekly_5y.pkl`. — [backtest_engine.py:20-60](backtest_engine.py), [backtest_engine.py:346](backtest_engine.py)
- Universe: today's `portfolio.csv` symbols (34). That brings survivorship and hindsight selection into the test. — [backtest_engine.py:344](backtest_engine.py); report header "Current 34 portfolio holdings" in [reports/backtest_summary.md](reports/backtest_summary.md)
- Decision dates: every weekly benchmark bar (`dates = bench_closes.index`). — [backtest_engine.py:79-94](backtest_engine.py)
- Indicators are weekly proxies: 50 DMA is a 10-week mean, 200 DMA is a 40-week mean, the 52-week high is the max of 52 weekly highs, and ATR is a 14-period ATR on weekly bars. Live `analysis.fetch_market_data` uses 50/200 daily SMAs, 1-year daily highs and a 14-day daily ATR. A weekly ATR is roughly √5 times a daily ATR, so the 3×ATR trailing stop sits much further away than it does live. — [backtest_engine.py:117-124](backtest_engine.py) vs [analysis.py:82-102](analysis.py)
- Before 40 weeks of history exist, `dma_200 = current_px`, so the first ~10 months cannot read as BEARISH. — [backtest_engine.py:118-119](backtest_engine.py)
- Hard-coded or look-ahead inputs passed to `evaluate_signal`:
  - `roe=0.15` constant
  - `sector_risk_exposure=15.0` constant, so sector caps never bind
  - `thesis_text="INTACT"` always
  - `risk_group_exposure` not passed (defaults to 0)
  - `conviction` and `invalidation_price` taken from today's `thesis.csv`, where every row has `Last_Updated` = 2026-09-26. Those values are applied back to 2021.

  — [backtest_engine.py:142-157](backtest_engine.py), [backtest_engine.py:334-342](backtest_engine.py); thesis dates checked in thesis.csv (all 34 rows `2026-09-26`)
- Execution: signals are evaluated on week *d*'s close and filled at the same close. There is no next-bar fill. — [backtest_engine.py:116](backtest_engine.py), [backtest_engine.py:159-189](backtest_engine.py)
- Action mapping:
  - SELL exits the full position.
  - TRIM always sells 50%. Live `size_action` instead trims to the cap, by 25% when overextended, or by 50% on a trailing stop.
  - BUY and ACCUMULATE both buy `min(25% of cash, 5% of initial capital)` every week while weight is below 8%.
  - A 0.2% fee is charged on each side.

  — [backtest_engine.py:159-189](backtest_engine.py) vs [analysis.py:157-208](analysis.py)
- Baselines: equal-weight buy-and-hold of the same universe from the first date, and Nifty 50 `^NSEI` price index (not TRI). — [backtest_engine.py:193-229](backtest_engine.py)
- Metrics: CAGR, max drawdown and annual turnover only. There are no per-decision outcomes, no hit rates, no 1-year-forward verification and no train/test split. The report states "Zero parameter tuning." — [backtest_engine.py:234-256](backtest_engine.py), [backtest_engine.py:284](backtest_engine.py)
- Output in [reports/backtest_summary.md](reports/backtest_summary.md), period 2021-10-15 to 2026-10-16:

  | Strategy | CAGR | Max drawdown | Turnover |
  |---|---|---|---|
  | Engine | 0.64% | -14.24% | 500.7% |
  | Buy-and-hold | 13.28% | -26.00% | 6.7% |
  | Nifty 50 | 4.38% | -16.60% | 8.6% |

  The narrative text praises "capital preservation" even though the engine badly underperforms both baselines. No CSV of trades or decisions is written.
- Test: `tests/test_analysis.py::test_backtest_engine_simulation_and_report` runs 60 weeks of synthetic data for 2 stocks and asserts only that the keys and types exist and the file was written. — [tests/test_analysis.py:767-833](tests/test_analysis.py)

**backtest/backtester.py + backtest/run_dma_backtest.py + backtest/yfinance_adapter.py (commit a1f2e27, 2026-09-23)**
- `run_backtest` is a generic walk-forward loop. Signals come from bar-close data (`frame.loc[:date]`) and fill at the *next bar's open* with 5 bps slippage. It warms up for 199 bars, force-closes open trades at the end, and summarises trades as win rate, expectancy, payoff and drawdown. It works on the common date index across all frames. — [backtest/backtester.py:91-154](backtest/backtester.py), [backtest/backtester.py:57-88](backtest/backtester.py)
- `DmaCrossoverStrategy` calls `evaluate_signal(current_price, dma_50, dma_200, roe=None, stock_sector)` only. It uses `technical_trend` and `is_overextended`, not `decision`: enter when BULLISH and not overextended, exit when BEARISH. No thesis, conviction, invalidation, weights, ATR or 52-week high are passed. — [backtest/run_dma_backtest.py:20-57](backtest/run_dma_backtest.py)
- Runs one symbol at a time over `--period 3y` of daily data (default) for `portfolio.csv` symbols, and prints a markdown table to stdout. Nothing is saved to `reports/`. — [backtest/run_dma_backtest.py:68-126](backtest/run_dma_backtest.py)
- `fetch_history` uses Yahoo `auto_adjust=True`, validates OHLC and has no cache. — [backtest/yfinance_adapter.py:9-43](backtest/yfinance_adapter.py)
- Test: one synthetic test asserts 1 trade and that the metric keys exist. — [tests/test_backtester.py](tests/test_backtester.py)

**scratch/run_cross_validation.py (commit cd03089, 2026-09-26; `scratch/` is in `.gitignore`)**
- Cross-checks `backtester.py` against `vectorbt` using the same DMA strategy, next-open fills and 5 bps slippage. It runs per symbol over 3 years of daily data and prints MATCH or DIVERGED. It also checks current Nifty-50 breadth below the 200 DMA. — [scratch/run_cross_validation.py:23-217](scratch/run_cross_validation.py)
- `vectorbt` and `scipy` are not installed in this sandbox (import fails), and neither is in `requirements.txt`. — [requirements.txt](requirements.txt)

**signal_scorer.py (commit a1f2e27; run by `.github/workflows/signal_scoring.yml`)**
- Reads the live log `re-engineering.csv` and scores the `Model_Signal` column (emoji signal, not `Decision`) at **5, 10 and 20 trading days** forward. It uses `Price_At_Signal`, which is the price logged at signal time. Yahoo history is limited to `period="1y"`. There is no benchmark and no hit-rate aggregation, and it writes `reports/signal_scores.csv`. — [signal_scorer.py:11-22](signal_scorer.py), [signal_scorer.py:27-185](signal_scorer.py), [.github/workflows/signal_scoring.yml:30](.github/workflows/signal_scoring.yml)
- `reports/signal_scores.csv` has 1,388 rows for signals dated 2026-05-31 to 2026-09-25 (outside the target window). Mean 20-day returns by signal: STRG SELL -3.43% (n=383), HOLD -5.27% (n=190), ACCUMULATE -6.18% (n=86). The 5-day minimum is -88.9%, which looks like a split or price-basis artifact. — computed locally from [reports/signal_scores.csv](reports/signal_scores.csv)
- The ingestion logic is unit-tested with an injected loader: once-only scoring, too-recent rows skipped, NO DATA rows skipped. — [tests/test_signal_scorer.py:15-221](tests/test_signal_scorer.py)

**performance.py (commit a241f0c, 2026-10-13)**
- Computes portfolio XIRR from `trades.csv` cash flows plus current value. The benchmark XIRR replays each buy and sell into `^NSEI` units on the same dates, a "same cash flows into Nifty" comparison. It also gives per-holding XIRR and reports coverage gaps against `portfolio.csv`. It is not a decision backtest. — [performance.py:16-242](performance.py)
- The benchmark is the Nifty 50 price index, not TRI, as noted in the code. Nifty data is fetched from Yahoo starting at the first trade date. — [performance.py:87-104](performance.py)
- Tests: XIRR math and a synthetic gap test. — [tests/test_analysis.py:438-495](tests/test_analysis.py)

### Inferences
- `backtest_engine.py`'s result (engine CAGR 0.64% vs buy-and-hold 13.28%) cannot be read as a test of the live logic. Today's invalidation prices applied to 2021–2023 prices may trigger "thesis invalidated" SELLs early on, because current invalidation levels sit near recent prices. The weekly ATR proxy also changes the trailing-stop behaviour. Both are look-ahead or mis-specification effects.
- The next-bar fill and `frame.loc[:date]` slicing in `backtest/backtester.py` can be reused for the hindcast execution loop. Its trade-level summary does not fit "verify each decision at +252 days".

### Gaps
- No stored per-week decision log from `backtest_engine.py`, so its decision mix (how many SELL, TRIM or BUY) cannot be checked without re-running it, and Yahoo is blocked here.
- Whether the cached `scratch/weekly_5y.pkl` ever existed outside this sandbox is unknown. It is not present here and `scratch/` is gitignored.

## Q2. Is `evaluate_signal` a pure function usable with point-in-time inputs?

### Takeaway
Yes. `evaluate_signal` is a pure, deterministic function with no IO and no globals other than the immutable `RiskConfig` default. That default can be overridden per call, which makes a parameter grid easy. All IO and portfolio context (prices, ROE, weights, sector and risk-group exposure, thesis) is gathered in `analysis.run_weekly_analysis`, which is not pure: it uses live Yahoo, today's CSVs, Telegram and `datetime.now`. A hindcast must rebuild those inputs point-in-time itself.

### Cited Findings
- Signature: `evaluate_signal(current_price, dma_50, dma_200, roe=None, stock_sector, sector_risk_exposure, technical_trend_override, total_return, thesis_text="INTACT", conviction, invalidation_price, stock_weight, config=RISK_CONFIG, fallback_price, data_issue, high_52w, atr, risk_group_exposure)`. It returns a frozen `SignalEvaluationResult` with `decision` ∈ {SELL, TRIM, ACCUMULATE, BUY, HOLD, NO THESIS, NO DATA, VERIFY DATA}. — [signal_engine.py:30-48](signal_engine.py), [signal_engine.py:80-99](signal_engine.py)
- The only module-level dependency is `from config import RISK_CONFIG, RiskConfig`. `RiskConfig` is a frozen dataclass whose defaults are read from env vars at import: max_position 8%, max_sector 25%, minimum_roe 0.10, overextension 1.25, trailing_stop_atr_multiple 3.0, max_risk_group 25%. — [signal_engine.py:9](signal_engine.py), [config.py:26-62](config.py)
- Decision rules: [signal_engine.py:234-284](signal_engine.py)

  | Order | Decision | Condition |
  |---|---|---|
  | 1 | SELL | Thesis invalidated (price ≤ invalidation) |
  | 2 | SELL | BEARISH (price < 200 DMA) and total_return < 0 and (conviction < 4 or missing) |
  | 3 | TRIM | Trailing stop hit, where stop = max(invalidation, 52w high − 3×ATR) |
  | 4 | TRIM | Overextended (price > 1.25 × 50 DMA), or weight > 8%, or sector/risk-group > 25% with weight ≥ 4% |
  | 5 | BUY / ACCUMULATE | Conviction ≥ 4, weight < 8%, caps OK, and BULLISH or (BEARISH with return > 25%). BUY if weight = 0, else ACCUMULATE |
  | 6 | HOLD | Everything else |

- ROE does not affect `decision`. ROE feeds only the emoji `signal` (HOLD / RISK, HOLD / REVIEW) and `fundamental_pass`. This follows from the decision tree, which never references `fundamental_pass` or `roe`. — [signal_engine.py:101-102](signal_engine.py), [signal_engine.py:197-209](signal_engine.py), [signal_engine.py:234-284](signal_engine.py)
- How the live inputs are built, all in `analysis.py`:

  | Input | Live source | Where |
  |---|---|---|
  | Price, 50/200 DMA | 1 year of daily history; needs ≥ 200 bars | [analysis.py:83-94](analysis.py) |
  | high_52w | Max of the 1-year daily High | [analysis.py:95-98](analysis.py) |
  | ATR | 14-day daily ATR (Wilder EWM) | [analysis.py:99-102](analysis.py), [indicators.py:24-35](indicators.py) |
  | ROE | Today's `yfinance .info['returnOnEquity']`, not point-in-time | [analysis.py:78-80](analysis.py) |
  | Weights | From the price × `portfolio.csv` Qty | [analysis.py:352-363](analysis.py) |
  | Sector exposure | Sector sum; Banking + Financial Services + Insurance combined into one Financials bucket | [analysis.py:364-365](analysis.py), [analysis.py:402-405](analysis.py) |
  | Risk-group exposure | ETF look-through, using `data/etf_constituents_2026_10.json` | [analysis.py:366](analysis.py), [analysis.py:407-408](analysis.py) |
  | total_return | (price − avg_cost) / avg_cost | [analysis.py:409](analysis.py) |
  | Thesis, conviction, invalidation | `thesis.csv` | [analysis.py:412-436](analysis.py) |
  | Share counts | `size_action` / `RiskManager` turn the decision into shares | [analysis.py:157-208](analysis.py), [analysis.py:458-469](analysis.py) |

- There are 21 unit tests of the decision tree, including invalidation, bearish pullbacks, NO DATA and BAD DATA, and action/decision consistency. They pass locally. — [tests/test_signal_engine.py](tests/test_signal_engine.py); `pytest` run: 26 passed (test_backtester, test_signal_engine, test_signal_scorer)

### Inferences
- A hindcast can call `evaluate_signal` directly. It needs a small point-in-time feature builder that slices daily data to `≤ t` and computes 50/200 DMA, the 252-day high and 14-day ATR in the same way as `fetch_market_data`. Refactoring `fetch_market_data` into a pure `compute_features(history_up_to_t)` would keep live and hindcast in sync.
- Thesis, conviction and invalidation have no history. The only option without look-ahead is a documented assumption. Either use thesis = INTACT and conviction = a fixed value, with invalidation derived mechanically at time *t* (for example a % below cost or the 200 DMA at entry), or run the test twice, with and without the invalidation rule. Using today's `thesis.csv` levels is look-ahead.
- Parameter-grid candidates already exposed as `RiskConfig` fields: `trailing_stop_atr_multiple`, `overextension_multiple`, `max_position_pct`, `max_sector_pct`, `max_risk_group_pct`. The 25% return threshold and the conviction ≥ 4 cutoff are hard-coded literals at [signal_engine.py:179](signal_engine.py), [signal_engine.py:252](signal_engine.py), [signal_engine.py:269](signal_engine.py) and [signal_engine.py:275](signal_engine.py). Tuning them needs a small refactor. ROE thresholds do not affect `decision`.

### Gaps
- No point-in-time ROE or fundamentals source exists in the repo. This matters only for the emoji `signal`, not `decision`.
- No point-in-time ETF constituent history exists; only the 2026-10 snapshot does. Risk-group exposure for ETFs would therefore be approximate.

## Q3. What historical data exists locally?

### Takeaway
No cached price history exists anywhere locally: no `.pkl` or `.parquet` files, and `scratch/` is empty apart from the script. Yahoo is blocked, so any hindcast run in this sandbox needs a price source fixed first. `trades.csv` (346 rows, 2021-04-16 to 2026-09-10) can reconstruct dated holdings for 24 of the 34 current symbols. Ten symbols have incomplete history, including 3 with no trades at all. The annual PDF statements are FY-level summaries with no per-trade dates. They cannot give month-level positions. The live decision log `re-engineering.csv` starts 2026-05-31, after the target window.

### Cited Findings
- **trades.csv**
  - Columns: `Date, Stock Symbol, Action, Qty, Price, Notes`.
  - 346 rows; 343 come from the Upstox order book import and 3 are marked "NO TRADE HISTORY FOUND - manual entry required".
  - Dates run 2021-04-16 to 2026-09-10 (111 distinct dates). Rows by year: 2021: 2, 2022: 70, 2023: 6, 2024: 94, 2025: 47, 2026: 124.
  - 35 symbols: the 34 holdings plus AWL, which was exited.
  - 341 BUY and only 2 SELL rows (AWL on 2023-02-07, IDECEL on 2024-10-04).

  — computed locally; ingest code [ingest_trades.py](ingest_trades.py); source export [reports/orderBook_Equity_1790345624080.csv](reports/orderBook_Equity_1790345624080.csv) (343 rows, same date range, includes STT and brokerage columns)
- Reconciling net trades.csv quantity with `portfolio.csv` gives 24 exact matches and 10 mismatches:

  | Symbol | portfolio.csv qty | trades.csv qty |
  |---|---|---|
  | ASHLEY | 106 | 53 |
  | BHAELE | 80 | 48 |
  | HDFBAN | 130 | 75 |
  | JIOFIN | 53 | 28 |
  | LGELEC | 13 | 0 |
  | LIC | 80 | 45 |
  | NTPGRE | 138 | 0 |
  | RELIND | 76 | 74 |
  | TATCAP | 46 | 0 |
  | WIPRO | 220 | 170 |

  This matches the code's `PARTIAL_HISTORY_SYMBOLS` allowlist (11 symbols including GUJPPL). Likely causes are bonus or split shares, demerger (JIOFIN), and IPO allotments (LIC, TATCAP, LGELEC, NTPGRE). — computed locally; [refresh_portfolio.py:20-27](refresh_portfolio.py)
- Count of holdings reconstructable from trades.csv (net qty > 0): 2023-10-31: 10; 2024-04-30: 14; 2024-10-31: 21; 2025-04-30: 23; 2025-10-31: 24. First-trade dates show the book was built up over the target window. — computed locally from trades.csv
- **PDF annual statements**
  - 5 files: `reports/AnnualGlobalTransactionStatement-20XX-20YY_SUMMARY.pdf`, FY2021-22 to FY2025-26, 2–5 pages each.
  - They are ICICI Direct AGTS *summaries*: per-ISIN sale and purchase quantity and value totals for the year, with no trade dates.
  - `parse_agts_pdf` stamps every extracted row with the FY end date (e.g. `2024-03-31`). Row counts: 11, 5, 5, 21 and 14.
  - They contain personal identifiers (name, PAN, address); avoid copying them.

  — [ingest_pdf_statements.py:37-89](ingest_pdf_statements.py), especially the `Date: date_str` (period end) at [ingest_pdf_statements.py:46-50](ingest_pdf_statements.py); local run of `parse_agts_pdf`
- **re-engineering.csv** (live decision log)
  - 2,430 rows; `Analysis_Date` 2026-05-31 to 2026-10-13 (41 distinct dates).
  - Full decision columns (`Decision`, `Conviction`, `dma_50/200`, weight, etc.) are filled only for later rows. `Decision` counts: NaN 2,022, HOLD 195, SELL 120, TRIM 43, ACCUMULATE 40, NO DATA 10.
  - Several dates have duplicate runs (e.g. 363 rows on 2026-09-24).

  — computed locally
- **reports/signal_scores.csv**: 1,388 rows, 2026-05-31 to 2026-09-25, 5/10/20-day horizons only (see Q1). — [reports/signal_scores.csv](reports/signal_scores.csv)
- **Other data**
  - `thesis.csv`: 34 rows, all `Last_Updated` 2026-09-26.
  - `data/etf_constituents_2026_10.json`: current snapshot only.
  - `~/.cache/py-yfinance` holds only `cookies.db` and `tkr-tz.db`, no prices.
  - A search for `*.pkl` and `*.parquet` outside site-packages found nothing.

  — local `ls` / `find`

### Inferences
- A "follow the user's actual book" variant (replaying decisions on the holdings actually held each month) is feasible from trades.csv for most of the window. The mismatched symbols need manual quantity adjustments or exclusion. LGELEC, TATCAP and NTPGRE have no trades and are probably post-2024 IPOs, so they mostly fall outside the window anyway.
- A cleaner design is to evaluate a fixed universe (e.g. the 34 tickers, plus Nifty 50 constituents to reduce selection bias) on every monthly date. Holdings-based weights would then be a second, optional layer.
- Hindcast window Oct 2023 to Oct 2025 plus a 252-day forward check means outcomes run to about Oct 2026. Warm-up needs about 200 trading days before Oct 2023, so the price history needed is roughly **Dec 2022 to Oct 2026, daily, adjusted**, for each symbol and `^NSEI`. None of this is local.

### Gaps
- No offline price data, so no numeric results could be produced here. Whether the hindcast runs in GitHub Actions, where Yahoo works (the existing workflows call yfinance), or needs a committed CSV price cache is a design decision for the prompt.
- No Nifty 50 TRI source exists in the repo; `performance.py` notes that Yahoo lacks TRI.

## Q4. Coverage of the target test: covered, partial, missing

### Takeaway
Only the building blocks exist: the pure `evaluate_signal`, the slice-to-date pattern and next-bar fills, Nifty price fetching, a forward-return scoring pattern, and `RiskConfig` for parameters. The core of the target test is missing. That core is monthly point-in-time replay of the *decision* field, a 252-day forward check against Nifty per decision, per-decision-type hit rates, a three-way strategy comparison over 2023-10 to 2025-10, and a train/test parameter grid. Look-ahead in `backtest_engine.py` should be fixed or bypassed, not reused as is.

### Cited Findings
- Full `evaluate_signal` decision replay exists only in `backtest_engine.py`, with the defects listed in Q1. — [backtest_engine.py:142-157](backtest_engine.py)
- Next-bar fills and point-in-time slicing exist in `backtest/backtester.py`. — [backtest/backtester.py:115-131](backtest/backtester.py)
- The forward-return-at-N-bars pattern exists in `signal_scorer.py` for N = 5, 10, 20, with no benchmark. — [signal_scorer.py:126-162](signal_scorer.py)
- Nifty comparisons exist as equity curves (`backtest_engine.py`) and as cash-flow-matched XIRR (`performance.py`). — [backtest_engine.py:223-229](backtest_engine.py), [performance.py:125-172](performance.py)
- No code in the repo uses a 252-day horizon, train/test split or parameter grid. `grep` finds no "252" horizon logic, and the summary states "Zero parameter tuning". — [reports/backtest_summary.md](reports/backtest_summary.md)

### Inferences
Recommended reuse and changes for the new hindcast prompt:
1. Reuse `evaluate_signal` unchanged, passing a `RiskConfig(...)` per grid point.
2. Factor `analysis.fetch_market_data`'s computations into a pure function that runs on daily data sliced to ≤ t.
3. Use daily bars, not weekly proxies.
4. Use monthly decision dates: last trading day of each month, Oct 2023 to Oct 2025 (25 dates).
5. Record each (date, symbol, decision, inputs). The outcome is the stock return over t+1 to t+252 trading days minus the Nifty return over the same span.
6. Define a hit per decision type, for example:
   - BUY / ACCUMULATE hit = excess return > 0
   - SELL hit = excess return < 0
   - TRIM hit = stock underperforms Nifty, or falls
   - HOLD reported as a distribution
7. Strategies:
   - Follow-the-model: applies decisions with next-bar fills.
   - Do-nothing: holds the starting book or equal-weight universe.
   - Nifty: buys the index once.
8. Split the window into train (e.g. Oct 2023 to Oct 2024) and test (Nov 2024 to Oct 2025). Outcome windows overlap the train/test boundary by up to 252 days, so the split needs an embargo or purge.
9. Keep thesis and invalidation off, or derive them mechanically, rather than using today's `thesis.csv`.

### Gaps
- How to define "do-nothing" (actual book at Oct 2023 from trades.csv, or the equal-weight universe) is a product choice the repo does not settle.

## Summary table

| Component | Exists? | Where | What to reuse | What to add/fix |
|---|---|---|---|---|
| Pure decision function | Yes | signal_engine.py:80-393 | Call `evaluate_signal` as is; pass `config=RiskConfig(...)` for the grid | Optionally lift hard-coded 25% return and conviction ≥ 4 literals (lines 179, 252, 269, 275) into RiskConfig if they are to be tuned |
| Point-in-time feature builder (DMA50/200, 52w high, ATR14) | Partial | analysis.py:69-107 (live only, Yahoo IO); backtest_engine.py:116-124 (weekly proxies) | Formulas from `fetch_market_data`, `indicators.atr` | Pure `features_asof(daily_df, t)` on daily bars sliced ≤ t; enforce ≥ 200 bars |
| Monthly decision-date replay, Oct 2023 to Oct 2025 | No | — (backtest_engine is weekly, 2021-2026) | Loop skeleton of backtest_engine.py:94-189 | Monthly last-trading-day schedule; per-row decision log CSV |
| No look-ahead in thesis, invalidation, ROE, sector | No | backtest_engine.py:146-152, 334-342 use today's thesis.csv, roe=0.15, sector=15 | — | Mechanical or neutral thesis inputs; point-in-time weights and sector and risk-group exposure from simulated book; ROE irrelevant to `decision` |
| Universe without survivorship | No | backtest_engine.py:344, run_dma_backtest.py:62-65 (today's portfolio.csv) | TICKER_MAP / SECTOR_MAP in analysis.py | Fixed documented universe (34 tickers ± Nifty 50 names); note bias |
| Execution timing (next bar) | Partial | backtest/backtester.py:115-145 (next open); backtest_engine.py same-bar close | backtester's `loc[:date]` + next-bar fill pattern | Fill at t+1 open or close in the model-follow simulation |
| Holdings-based sizing (TRIM/BUY share counts) | Partial | analysis.py:157-208 `size_action` + risk_manager.py; backtest_engine uses fixed 50% trim / 5% buys | `size_action`, `trim_quantity`, `RiskManager` | Wire into simulator so trims and buys match live sizing |
| 252-day forward verification vs Nifty per decision | No | signal_scorer.py does 5/10/20d, no benchmark | Forward-index logic, signal_scorer.py:126-162 | 252-bar horizon, excess vs ^NSEI, per-decision hit-rate table |
| Follow-model vs do-nothing vs Nifty comparison | Partial | backtest_engine.py:193-256 (B&H equal-weight + Nifty equity curves) | Metric function `get_metrics`, B&H and Nifty curve code | Restrict to 2023-10 to 2025-10 (+252d); define do-nothing; no fees (costs excluded) |
| Train/test parameter tuning | No | — | RiskConfig dataclass fields | Small grid (e.g. trailing_stop_atr_multiple, overextension_multiple, max_position_pct), train window, held-out confirm, embargo for overlapping 252d labels |
| Historical holdings per month | Partial | trades.csv (2021-04 to 2026-09, 24/34 reconcile); refresh_portfolio.py:20-27 | Net-qty-by-date from trades.csv | Handle 10 mismatched symbols (bonus/split/IPO); PDFs unusable (FY totals only, ingest_pdf_statements.py:46-50) |
| Historical price data | No | No local cache; Yahoo blocked in sandbox | `backtest/yfinance_adapter.fetch_history` (validated, auto_adjust) | Cache daily OHLC Dec 2022 to Oct 2026 for universe + ^NSEI (CSV/parquet), or run in CI |
| Logged live decisions for comparison | Partial | re-engineering.csv (2026-05-31 onward), reports/signal_scores.csv | Format/columns as template for hindcast log | Not usable for 2023-2025 window |
| Tests | Partial | tests/test_signal_engine.py (21), test_backtester.py (1), test_analysis.py:767-833 (smoke) | Synthetic-frame fixtures | Tests for no-look-ahead slicing, 252d labelling, hit-rate math, train/test split |
| Costs / tax | Excluded | backtest_engine fee_rate=0.002; tax_planner.py | — | Set fees = 0 for this test |
