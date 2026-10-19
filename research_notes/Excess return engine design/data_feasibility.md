# Data feasibility for a factor-based (momentum / quality / low-vol) selection engine on Indian equities

Scope: free or low-cost data for a retail Python repo (/home/user/Portfolio), as of 15 Oct 2026. The repo today pulls daily prices with yfinance (`hindcast/fetch.py`, `backtest/yfinance_adapter.py`, `backtest_engine.py`) for 34 current holdings only. It caches them in `data/prices/{raw,adj}` with a `manifest.json`, and keeps `data/corporate_actions.csv`. That makes the existing hindcast survivorship-biased.

**Method caveat:** this sandbox's proxy blocked nseindia.com, nsearchives.nseindia.com, niftyindices.com, kite.trade, tradingqna.com and forum.unofficed.com (CONNECT 403 / DNS failure). So no NSE file was downloaded or opened directly. NSE-related claims come from search-engine extracts of those pages, and items marked UNVERIFIED should be checked from an Indian residential connection before code depends on them. PyPI was reachable, and the library release dates below were read directly from the PyPI JSON API.

## 1. Historical Nifty 200/500 constituents (point-in-time membership)

### Takeaway
No free official file gives full point-in-time Nifty 500 or Nifty 200 membership. It can be rebuilt, though: start from a current constituent list and walk backwards through the semi-annual NSE Indices "replacement of stocks" press releases plus ad-hoc changes (mergers, delistings, F&O-related). Those releases appear to exist at predictable URLs back to at least 2020, and an NSE-hosted inclusions/exclusions workbook reportedly goes back to 1998. Expect hand-reconciliation work. A cheaper approximation is to rebuild the universe yourself from bhavcopy market-cap and turnover ranks, without index membership.

### Cited Findings
- NSE Indices posts semi-annual review press releases as PDFs at `niftyindices.com/Press_Release/ind_prsDDMMYYYY.pdf`. Examples surfaced include 13-May-2020, 15-Sep-2021, 20-Sep-2021, 01-Sep-2022, 17-Aug-2023, 23-Aug-2024, 21-Feb-2025 (mirrored on nsearchives), 23-Feb-2026 and 10-Aug-2026. Each has per-index "excluded"/"included" tables under "Replacements on account of semi-annual review" — [ind_prs10082026](https://niftyindices.com/Press_Release/ind_prs10082026.pdf); [ind_prs23022026](https://niftyindices.com/Press_Release/ind_prs23022026.pdf); [ind_prs23082024](https://niftyindices.com/Press_Release/ind_prs23082024.pdf); [ind_prs21022025](https://nsearchives.nseindia.com/web/sites/default/files/2025-02/ind_prs21022025.pdf); [ind_prs13052020](https://niftyindices.com/Press_Release/ind_prs13052020.pdf)
- The Aug-2026 review takes effect 30-Sep-2026 (close of 29-Sep-2026). It removes Wipro from and adds BSE Ltd. to Nifty 50, and its Nifty 500 exclusions start with 3M India. In the Feb-2026 review (effective 30-Mar-2026), Nifty 500 exclusions start with Akums Drugs; Nifty 50 was unchanged — [ind_prs10082026](https://niftyindices.com/Press_Release/ind_prs10082026.pdf); [ind_prs23022026](https://niftyindices.com/Press_Release/ind_prs23022026.pdf)
- Nifty 500 is rebalanced semi-annually, with four weeks' notice to the market before a change — [Nifty 500 factsheet](https://www.niftyindices.com/Factsheet/ind_nifty_500.pdf) (via search extract)
- Community reports (UNVERIFIED, forum):
  - niftyindices posted monthly constituent files from Apr-2013 to Mar-2022; after that, only F&O index constituents were posted — [TradingQnA: historical composition](https://tradingqna.com/t/where-can-i-find-historical-composition-of-nifty-indices/7163)
  - An NSE archive spreadsheet has a "Nifty 500" sheet of inclusions/exclusions from 1-Aug-1998 — [Unofficed forum](https://forum.unofficed.com/t/get-historical-nifty-500-constituent/1375)
  - The site now covers only major indices — [TradingQnA: historical constituents of various NSE indices](https://tradingqna.com/t/historical-constituents-of-various-nse-indices/176515)
- TradingQnA has community threads summarising each semi-annual change (e.g., Aug-2024) — [TradingQnA Aug-2024 thread](https://tradingqna.com/t/nses-periodic-semi-annual-replacement-of-stocks-in-various-indices-august-2024/172217)
- Terms: NSE's website terms prohibit "systematic or automated data collection activities (including scraping, data mining, data extraction…)" and copying or redistribution without written permission — [NSE Terms of Use](https://www.nseindia.com/static/nse-terms-of-use)

### Inferences
- **Feasible rebuild:** take the current Nifty 500 CSV (the `ind_nifty500list.csv` pattern on niftyindices). Then apply the press-release diffs in reverse for each March/September effective date, back to ~2015–2018. Manually downloading about 20 PDFs and parsing their tables (pdfplumber) is a small one-off job and stays within "personal use".
- **Ad-hoc changes are the weak spot.** Mid-period replacements (mergers, demergers, suspensions) appear in separate press releases. Missing them leaves small membership errors. Diff the rebuilt list against any monthly constituent files you can get (2013–2022) to catch these.
- **Recommended practical alternative:** define the universe point-in-time from bhavcopy data, e.g. top 200/500 by trailing 6-month average traded value or free-float market-cap proxy, re-ranked semi-annually. This is fully survivorship-free and needs no index files. It is also close to how NSE selects Nifty 500 (full-market-cap rank plus liquidity filters). Official membership then only matters for benchmarking.
- The press-release PDFs are public announcements. Downloading them manually for personal research is low-risk, but bulk automated crawling of nseindia.com conflicts with the ToU.

### Gaps
- Could not open any press release or the factsheet. The exact first year of the `ind_prs` series and the existence and URL of the 1998+ inclusions/exclusions workbook are unconfirmed.
- Unconfirmed whether niftyindices still serves archived monthly constituent files (Apr-2013 to Mar-2022).
- No free, cleaned, point-in-time Nifty 500 membership dataset was found on GitHub or Kaggle; this was not searched exhaustively.

## 2. Daily prices for ~500+ stocks including delisted names

### Takeaway
The only free source that is both official and survivorship-free is NSE's daily equity bhavcopy. It has every traded symbol each day, including names later delisted. It uses the legacy `cmDDMONYYYYbhav.csv.zip` format through early July 2024 and UDiFF "Common Bhavcopy" after that, so the parser must handle two schemas. yfinance is fine for live holdings but loses delisted tickers. Broker APIs (Kite, Upstox, Angel) are designed around currently tradable instruments and are not good for delisted history. Bhavcopy prices are unadjusted, so you must build your own corporate-action adjustment.

### Cited Findings
- **UDiFF cutover**
  - SEBI's Market Data Advisory Committee required standardised exchange file formats, named UDiFF — [NSE circular COM63365](https://nsearchives.nseindia.com/content/circulars/COM63365.pdf)
  - NSE discontinued the old multi-file downloads w.e.f. 08-Jul-2024 and points users to UDiFF Common Bhavcopy zips (NSE circular 62424, 12-Jun-2024) — [NSE derivatives reports page](https://nseindia.com/all-reports-derivatives)
  - BSE similarly discontinued legacy files from 08-Jul-2024 — [BSE UDiFF page](https://bseindia.com/static/members/udiff.aspx)
  - Some legacy F&O/CDS files were dropped earlier (2-May and 20-May-2024) — [NSE circular CMPT60453](https://nsearchives.nseindia.com/content/circulars/CMPT60453.pdf)
  - A separate interim CM bhavcopy DAT layout change was effective 05-Aug-2024 — [NSE circular CMTR62825](https://nsearchives.nseindia.com/content/circulars/CMTR62825.pdf)
- **yfinance and delisted names**
  - Yahoo removes delisted symbols entirely, including the history from when they were listed — [node-yahoo-finance2 docs](https://github.com/gadicc/node-yahoo-finance2/blob/devel/docs/modules/historical.md)
  - yfinance logs "possibly delisted; no price data found" for such tickers (example is a non-NSE ticker) — [yfinance issue #2280](https://github.com/ranaroussi/yfinance/issues/2280)
- **EODHD (paid alternative)**
  - Keeps delisted tickers' prices, fundamentals, splits and dividends, and lists about 940 delisted NSE symbols. Reused tickers get an `_old` suffix — [EODHD delisted data](https://eodhd.com/financial-apis/review-delisted-stock-companies-data)
  - Plans: free starter tier with limited calls; EOD about $19.99/mo; fundamentals about $59.99/mo (€59.99 on G2); All-in-One about $99.99/mo — [G2 EODHD pricing](https://www.g2.com/products/eodhd-financial-data-apis/pricing); [NexusFi](https://nexusfi.com/d/data-providers/eodhd-eod-historical-data/)
- **Zerodha Kite Connect**
  - Historical data is no longer a separate add-on from 08-Feb-2025, but it requires the paid base Connect subscription. The free "Personal" API has no market or historical data — [marketcalls](https://www.marketcalls.in/algo-trading/zerodha-makes-trading-api-free-for-personal-use-bundles-historical-data-with-connect-api.html); [Kite forum](https://kite.trade/forum/discussion/comment/49021/)
  - Price conflict: Zerodha's FAQ says ₹500/month per API key, while an Apr-2025 Z-Connect update and a third party cite ₹2,000 — [Zerodha Kite API FAQ](https://support.zerodha.com/category/trading-and-markets/general-kite/kite-api/articles/kite-connect-api-faqs); [Z-Connect update](https://zerodha.com/z-connect/?p=411859)
  - Rate limit is about 3 req/s per a forum moderator (a 2016 post said 2 req/s for historical) — [Kite forum rate limit](https://kite.trade/forum/discussion/8899/rate-limit-of-kite-connect-historical-data-api-and-lookback); [Kite forum 2016](https://kite.trade/forum/discussion/comment/922)
  - Zerodha says the historical API is "for backtesting purposes" — [Kite forum](https://kite.trade/forum/discussion/8899/rate-limit-of-kite-connect-historical-data-api-and-lookback)
- **Upstox and Angel One**
  - Upstox staff: the API provides 6 months of 1-minute history, and historical calls fall under the general rate limits — [Upstox community](https://community.upstox.com/t/historical-candle-data-from-upstox-api/7649)
  - Angel SmartAPI `getCandleData`: users report a cap of about 500 candles per request and empty responses; moderators dispute the cap — [SmartAPI forum topic 2338](https://smartapi.angelone.in/topic/2338/historical-api-is-returning-a-maximum-of-500-records-only/3); [SmartAPI forum 13395](https://smartapi.angelone.in/smartapi/forum/post/13395)
- **NSE access and terms**
  - NSE has blocked server/cloud-IP requests, and libraries like nsepython stop working on AWS/GCP — [Unofficed forum](https://forum.unofficed.com/t/update-nsepython-not-working-in-aws-google-cloud-and-webservers/670)
  - NSE's ToU bars automated collection. The licensed bulk route is the paid NSE Data & Analytics portal, with a published price list (Mar-2026) — [NSE ToU](https://www.nseindia.com/static/nse-terms-of-use); [NSE pricing file Mar-2026](https://nsearchives.nseindia.com//web/mediaattachment/2026-03/NSE_Pricing_file_-_Domestic_clients_20260309171343.pdf)

### Inferences
- **Bhavcopy coverage:** about 2,000 trading days × 1 file each covers 2018–2026. A polite, rate-limited (≈1 req/2–3 s), resumable, cache-once download takes a few hours and runs once. After that, the job is one file per day.
- **Legal posture:** downloading reports that NSE publishes for manual download is grey under the ToU for automated access. It is low-risk for personal, non-redistributed use; do not publish the raw data. Flag: terms-restricted.
- **Delisted names:** bhavcopy rows stop on the last trading day. The backtest must treat that as an exit at the last price, or as a configurable haircut for compulsory delistings and suspensions. It must not drop the stock.
- **Adjustments:** legacy bhavcopy has PREVCLOSE, which on ex-dates is NSE's adjusted previous close. The ratio PREVCLOSE / prior-day CLOSE gives a split/bonus/rights adjustment factor without needing a corporate-actions feed. This is a well-known trick (UNVERIFIED for every action type). Check it against NSE's corporate actions report and the repo's existing `data/corporate_actions.csv`. Dividends need a separate source for total-return; NSE's corporate-actions CSV lists them.
- **Symbol changes:** NSE symbols get renamed (e.g., after mergers or name changes). Key on ISIN, which is present in both legacy and UDiFF bhavcopies, not on SYMBOL.
- **BSE bhavcopy** is a fallback with a broader listed universe, also UDiFF since Jul-2024. It is not needed for a Nifty-500-type universe.
- **Broker APIs** are good for refreshing current tradable names with exchange-grade candles. They are not good for delisted history, and their ToS is tied to your brokerage account.

### Gaps
- Exact URL patterns for legacy and UDiFF CM bhavcopy archives, and how far back NSE's archive serves files today (believed to be the 1990s for legacy CM), are UNVERIFIED because NSE was blocked here.
- Current Kite Connect price (₹500 vs ₹2,000) is unresolved.
- No authoritative statement on whether Kite returns daily candles for delisted equities. Instrument tokens for delisted names generally disappear from the instrument dump (inference).

## 3. Fundamentals with as-of (publication) dates

### Takeaway
A free, point-in-time quality factor (ROE, leverage, earnings stability) for 500 Indian stocks over 10+ years is not realistically feasible.
- yfinance fundamentals are shallow (about 4 annual / 4–5 quarterly periods) and not point-in-time.
- Screener.in, Trendlyne and Tijori are not licensed for bulk extraction.
- NSE/BSE XBRL filings are the right official, free, date-stamped source, but India-specific tooling doesn't exist, so you'd build the pipeline yourself.
- CMIE Prowess is mostly accessed through institutional licences.

Build price-only first (momentum, low-vol). Add quality later via a paid vendor (EODHD fundamentals about $60/mo, not PIT-verified) or an XBRL pipeline.

### Cited Findings
- NSE introduced XBRL-based filing for listed-company periodic compliance (results, shareholding), aligned with MCA structures — [NSE circular NSE/CML/2018/08](https://archives.nseindia.com/content/equities/NSE_Circular_13042018.pdf)
- No India-specific Python XBRL downloader was found. Generic parsers exist (e.g., brel-xbrl opens XBRL/iXBRL from path or URL); others target SEC EDGAR or ESEF — [brel-xbrl on PyPI](https://pypi.org/project/brel-xbrl/0.8.1a4); [xbrl-filings-api](https://pypi.org/project/xbrl-filings-api)
- CMIE Prowess IQ is distributed via university and institution subscriptions (e.g., IIM Indore, IIM Calcutta, Manipal). No individual price was published. Coverage claims vary (37,780 to 51,500+ companies) — [IIM Indore guide](https://iimidr.ac.in/wp-content/uploads/2025/10/User-Guide-CMIE-prowess-IQ.pdf); [IIM Calcutta library](https://library.iimcal.ac.in/cmie-prowessiq/); [Manipal e-resources](https://mahelibportal.manipal.edu/doc-eresources)
- EODHD's fundamentals plan is about $59.99/mo; its India ticker pages advertise fundamentals — [G2](https://www.g2.com/products/eodhd-financial-data-apis/pricing); [EODHD India page](https://eodhd.com/financial-summary/INDIA01.BK)
- Screener.in terms: the search did not surface its ToU. General legal commentary says site terms can contractually prohibit scraping, and India's law on scraping is unsettled — [PromptCloud](https://www.promptcloud.com/blog/is-screen-scraping-legal/); [Peakhour](https://www.peakhour.io/blog/is-it-legal-to-scrape-a-competitors-website/)

### Inferences
- **The as-of discipline is the hard part, more than the numbers.** Under SEBI LODR, quarterly results are due within 45 days of quarter end (60 for Q4/annual) (from background knowledge, not re-verified here). If you lack actual filing timestamps, a conservative rule is to lag fundamentals 60 days after quarter end and 90 days after fiscal year end. That avoids most look-ahead bias, though not restatement bias.
- **yfinance `.financials` / `.quarterly_financials`** for `.NS` tickers return only recent periods and current restated values (training knowledge, about 4 years; UNVERIFIED for 2026). They are suitable only for a current-snapshot quality screen on today's portfolio, not for backtests.
- **Screener.in** offers manual Excel export per company to logged-in users (paid "premium" for screens and exports, per training knowledge). It is fine for occasional manual checks. Automating 500 exports likely breaches its terms. Flag: terms-restricted, UNVERIFIED.
- **Trendlyne, Tijori and Tickertape** are consumer subscription products with no public bulk API for retail. Treat them as non-viable for a pipeline (inference; no pricing pages fetched).
- **Proxy quality factors from price data** (e.g., low drawdown, low beta, return stability) are a defensible stand-in until real fundamentals exist. Note that NSE's own Quality 30 index uses ROE, D/E and EPS growth variability, so a price proxy is not the same factor.

### Gaps
- Screener.in, Trendlyne and Tijori ToU and pricing were not retrieved.
- Unverified whether NSE's corporate-filings XBRL endpoints are reachable without a browser session, and how far back structured XBRL results go (likely about FY2012+ on BSE, about 2018+ for NSE's XBRL mandate).
- Whether EODHD India fundamentals keep filing dates and original as-reported values (true PIT) is unverified.

## 4. Factor index levels as free, survivorship-free benchmarks

### Takeaway
NSE Indices publishes daily price and TRI history for its strategy indices (Nifty200 Momentum 30, Nifty Alpha Low-Volatility 30, Nifty100 Low Volatility 30, Nifty200 Quality 30, Nifty500 Momentum 50, etc.) through the niftyindices historical-data page. These are the best free, survivorship-free evidence of factor premia in India. A caveat: pre-launch history is back-tested by NSE.

### Cited Findings
- Nifty200 Momentum 30 picks the top 30 momentum stocks from Nifty200. As a new index, its whole early history is back-tested — [FreeFinCal](https://freefincal.com/?p=39782)
- Third parties state the index history runs from about April 2005 (UNVERIFIED base date) — [Angel One news](https://www.angelone.in/news/baroda-bnp-paribas-nifty-fund)
- Third-party mirrors of index return series exist (non-official) — [Wright Research](https://www.wrightresearch.in/track/index/nifty-200-momentum-30/); [Sharpely](https://sharpely.in/indices/nifty-200-momentum-30/58)

### Inferences
- Use the TRIs in three ways:
  - (a) Benchmarks for the engine: Nifty 500 TRI as the market; Momentum 30 and Low Vol 30 TRIs as "can I beat the free ETF/index fund" hurdles.
  - (b) A sanity check: a home-built momentum backtest on a PIT universe should roughly track the Momentum 30 TRI. Large divergence signals bias or bugs.
  - (c) A realistic implementation option: index funds/ETFs on these indices exist (e.g., Baroda BNP Paribas Nifty200 Momentum 30 Index Fund), so the engine must beat them after costs and taxes to be worth running.
- Back-tested pre-launch periods are survivorship-free by construction if NSE used PIT data, but they are subject to methodology selection bias. Report live-only (post-launch) performance separately.
- Download is a manual CSV export per index and date range on niftyindices.com (about 1-year windows per query, per training knowledge, UNVERIFIED). Libraries such as nsepython and jugaad-data wrap index history (inference from library docs; not tested here). yfinance has `^NSEI`, `^CRSLDX` (Nifty 500) and a few others, but not the strategy TRIs (training knowledge, UNVERIFIED).

### Gaps
- Official base dates and launch dates for each factor index were not confirmed (factsheets blocked).
- Exact niftyindices historical-data endpoint behaviour (date-range limits, TRI availability per index) is unverified.

## 5. Python library status (Oct 2026) and rate-limit / caching strategy

### Takeaway
All three NSE scraping libraries are actively maintained in 2026. nsepy is dead. yfinance is on 1.x. All NSE libraries depend on undocumented NSE web endpoints, need cookies and headers, and break when blocked or changed. They also fail from cloud IPs. Treat them as convenience wrappers and cache everything locally.

### Cited Findings (read directly from the PyPI JSON API on 15-Oct-2026)
| Library | Latest version | Latest release date | Repo / docs |
|---|---|---|---|
| jugaad-data | 0.35.10 | 2026-10-06 (also 0.35.9 on 2026-09-23) | [GitHub jugaad-py/jugaad-data](https://github.com/jugaad-py/jugaad-data) |
| nsepython | 2.101 | 2026-10-07 | [GitHub aeron7/nsepython](https://github.com/aeron7/nsepython) |
| nselib | 2.5.1 | 2026-05-01 | [GitHub RuchiTanmay/nselib](https://github.com/RuchiTanmay/nselib) |
| yfinance | 1.7.0 | 2026-08-26 | [GitHub ranaroussi/yfinance](https://github.com/ranaroussi/yfinance) |
| nsepy | 0.8 | 2020-03-07, abandoned | [GitHub swapniljariwala/nsepy](https://github.com/swapniljariwala/nsepy) |

- jugaad-data documents `bhavcopy_save` / `bhavcopy_fo_save`, ships a CLI, and claims to support the new NSE website — [jugaad-data on PyPI](https://pypi.org/project/jugaad-data)
- Other bhavcopy helpers: `bhavcopy`, `pybhav` (caches downloads, covers SME/F&O) and `nsefin` (EOD bhavcopy example, Aug-2025) — [bhavcopy](https://pypi.org/project/bhavcopy/3.0); [pybhav](https://pypi.org/project/pybhav/); [nsefin](https://pypi.org/project/nsefin/)
- NSE blocks requests from cloud and server IPs, so nsepython breaks on AWS/GCP — [Unofficed forum](https://forum.unofficed.com/t/update-nsepython-not-working-in-aws-google-cloud-and-webservers/670)
- Verified in this session: the sandbox's outbound proxy refused NSE, niftyindices and kite domains, so any CI or cloud job will need a cached data snapshot.

### Inferences
- **Caching strategy:**
  - (1) Raw immutable layer: store each day's bhavcopy zip as downloaded under `data/bhavcopy/raw/{YYYY}/`. Never re-download a date that exists.
  - (2) Normalised layer: one Parquet (or CSV) per year with columns date, ISIN, symbol, series, OHLC, prevclose, volume, turnover, trades. Merge legacy and UDiFF schemas here.
  - (3) Derived layer: adjusted close panel and a universe membership table, both versioned in `manifest.json` (the repo already uses this pattern in `data/prices/manifest.json`).
- **Rate limits:** NSE publishes none for web downloads. Use a single session with browser headers, ~1 request per 2–3 s, exponential backoff on 401/403, and resume from the last cached date. Run from a home connection, not CI.
- **yfinance:** unofficial Yahoo endpoints, with throttling reported in 2025–26 (training knowledge). Keep it only for current holdings and as a cross-check on the bhavcopy-derived adjusted series.
- **Pinning:** pin library versions in `requirements.txt`; current repo has `yfinance>=0.2.38` while PyPI is at 1.7.0. Prefer writing a small in-repo bhavcopy downloader (about 100 lines) over depending on a scraping library whose NSE endpoint logic changes monthly. Use the libraries as reference implementations for URL patterns.

### Gaps
- Not tested whether each library's bhavcopy function currently handles UDiFF dates (post-Jul-2024) correctly. jugaad-data's frequent Sep–Oct 2026 releases suggest active endpoint fixes.
- No official NSE rate limit exists to cite.

## Recommended data plan for the repo

*This section is a synthesis of the findings above, so its claims are not separately sourced.*

**Phase 1 — minimum viable, price-only (momentum + low-vol), free**

1. **Prices.** Build a survivorship-free equity panel from NSE CM bhavcopy, EQ series (plus BE/BZ for stocks moved to trade-to-trade), from 2012 (or 2015) to today.
   - Parse the legacy format through about 05-Jul-2024 and UDiFF after that.
   - Key on ISIN.
   - Download manually or semi-automatically from a home IP, slowly, once. Cache raw zips; do not redistribute.
   - Fallback: EODHD EOD plan (about $20/mo) for delisted NSE history, cross-checked against bhavcopy.
2. **Adjustments.** Derive split/bonus/rights factors from bhavcopy PREVCLOSE vs prior CLOSE. Validate against NSE's corporate-actions download and the existing `data/corporate_actions.csv`. Add dividends for a total-return series later; price-return momentum is acceptable at first.
3. **Universe.** Build a PIT universe in-house: every six months (end-Mar/end-Sep, matching NSE), rank by trailing 6-month median traded value and price × volume proxies. Take the top 200/500, applying a minimum-history (≥12 months) filter and excluding BE/BZ/suspended names. Optionally reconcile against Nifty 500 membership rebuilt from the `ind_prs*.pdf` semi-annual press releases. Do that only where it changes results.
4. **Delisting handling.** Exit at the last traded price. Also run a stress case with a −30% to −100% haircut for compulsory or suspension delistings, and report both.
5. **Benchmarks and evidence.** Manually download daily TRI CSVs from niftyindices for:
   - Nifty 500 TRI
   - Nifty 200 TRI
   - Nifty200 Momentum 30 TRI
   - Nifty Alpha Low-Volatility 30 TRI
   - Nifty100 Low Volatility 30 TRI
   - Nifty500 Momentum 50 TRI (if available)

   Store them under `data/indices/`. The engine must beat the relevant factor TRI after costs, STT and taxes, because an index fund already offers it.
6. **Costs.** Model brokerage, STT, stamp duty, exchange and SEBI fees, slippage tied to traded value, and STCG/LTCG. Monthly or quarterly rebalancing keeps turnover manageable.
7. **Live refresh.** Keep yfinance for daily marks on current holdings. Optionally use Kite Connect (paid; ₹500 vs ₹2,000/mo unresolved) for exchange-grade daily candles of currently listed names.

**Phase 2 — optional fundamentals (quality)**

- **Option A (cheapest, rough):** add a current-snapshot quality screen (ROE, D/E) from yfinance or a manual Screener export, applied only as a live filter. Do not backtest it.
- **Option B (honest PIT, more work):** build an XBRL pipeline from NSE/BSE corporate filings for quarterly results. Use the filing timestamp as the as-of date; if it is missing, lag 60/90 days. Parse with a generic XBRL library, starting with Nifty 200 names and about 2018+.
- **Option C (paid):** EODHD fundamentals (about $60/mo; check India depth and as-reported vs restated values before relying on it) or institutional CMIE Prowess access through a university library, if available.
- **Until A, B or C is validated,** keep quality as a price-based "defensiveness" proxy and label it as such in reports.

**Flags to carry into design:**
- NSE ToU prohibits automated scraping.
- All NSE-domain specifics above are UNVERIFIED from this environment.
- Factor-index pre-launch histories are back-tested.
- Kite pricing conflict is unresolved.
- Screener/Trendlyne terms were not reviewed.
