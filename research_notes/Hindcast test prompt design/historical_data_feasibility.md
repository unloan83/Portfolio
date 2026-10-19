# Historical Data Feasibility for the 2022-2026 Hindcast (Indian NSE/BSE holdings + Nifty 50 benchmark)

Scope: the symbols in `analysis.py` `TICKER_MAP` (lines 19-31), daily history from early 2022 to Oct 2026, with Yahoo Finance via yfinance as the primary source. Yahoo is blocked in this sandbox, so nothing here was checked against a live download. Every date below comes from news, exchange or company sources found by web search. Items marked **UNVERIFIED** come from memory or a single weak source and need checking before use.

Date convention: "usable from" means listing date + 200 NSE sessions. It was estimated with weekday arithmetic plus about 8 days for exchange holidays, so it can be off by roughly ±1 week. Re-derive it from the cached price file once the data is downloaded.

---

## Q1. Listing dates: which holdings lack 200 sessions at early decision dates?

### Takeaway
Five equities and one ETF in the map have no full 200-session history at a 2022 decision date: LIC (May 2022), HDFC Smallcap 250 ETF (Feb 2023), Jio Financial (Aug 2023), NTPC Green (Nov 2024), Tata Capital (13 Oct 2025) and LG Electronics India (14 Oct 2025). Tata Capital and LG only clear 200 sessions around late July 2026. Two symbols were renamed (SEQUENT→VIYASH in Jan 2026, Gujarat Gas→Gujarat Energy in May 2026), so Yahoo may hold their older history under the old symbol.

### Cited Findings
- **Tata Capital (TATACAP)** listed on NSE/BSE on **13 Oct 2025**. The IPO was priced at ₹326, the stock opened at ₹330 on NSE and the debut was flat. — [Business Standard](https://www.business-standard.com/markets/news/tata-capital-debuts-flat-on-d-street-should-you-buy-sell-or-hold-125101300172_1.html); [Outlook Money](https://www.outlookmoney.com/invest/equity/tata-capital-ipo-nbfcs-shares-make-muted-debut-list-with-1-premium-on-nse-bse); [Bajaj Broking](https://www.bajajbroking.in/share-market-news/tata-capital-lists-flat-at-rs-330-on-nse-after-rs-15000-crore-ipo)
- **LG Electronics India (LGEINDIA)** listed on **14 Oct 2025** at ₹1,710.10 on NSE, a 50% premium to the ₹1,140 issue price. One early report said 13 Oct, but the company release and later reports say 14 Oct. — [Motilal Oswal](https://www.motilaloswal.com/news/stocks/106887); [Angel One](https://oga-prod.angelone.in/news/ipos/lg-electronics-ipo-listing-date-set-for-tomorrow-october-14-2025); [Korea Times](https://www.koreatimes.co.kr/path/A2025101413450005975)
- **NTPC Green Energy (NTPCGREEN)** listed on **27 Nov 2024** at ₹111.50 on NSE against a ₹108 issue price. — [Angel One](https://www.angelone.in/news/share-market/ntpc-green-energy-shares-listed-on-nse-at-a-modest-premium); [Business Standard](https://www.business-standard.com/markets/news/ntpc-green-energy-joins-rs-1-trillion-market-cap-club-on-debut-124112700413_1.html)
- **Jio Financial Services (JIOFIN)** was admitted to dealings on **21 Aug 2023** and listed at ₹262 on NSE (discovered price ₹261.85). It traded in the T2T segment for 10 days. — [Business Standard](https://www.business-standard.com/markets/news/jio-financial-services-set-to-be-listed-on-stock-exchanges-on-august-21-123081800389_1.html); [5paisa](https://5paisa.com/news/jio-financial-services-lists-on-nse-at-rs262-and-on-bse-at-rs265)
- **HDFC Nifty Smallcap 250 ETF (HDFCSML250)**: the NFO ran 30 Jan to 13 Feb 2023 (extended) and trading started around **15 Feb 2023**. Its NSE symbol is HDFCSML250 and its BSE code is 543775. — [AdvisorKhoj](https://www.advisorkhoj.com/news/NFO/HDFC-Mutual-Fund-launches-HDFC-NIFTY-Smallcap-250-ETF); [Value Research](https://www.valueresearchonline.com/stories/52135/nfo-period-extends-for-recently-launched-three-etfs-of-hdfc-mutual-fund/); [TradingView](https://in.tradingview.com/symbols/NSE-HDFCSML250); [HDFC MF](https://www.hdfcfund.com/product-solutions/overview/hdfc-nifty-smallcap-250-etf/regular)
- **ICICI Prudential Silver ETF (SILVERIETF)**: fund inception was **24 Jan 2022**. The exchange listing came a few days later; the exact date is **UNVERIFIED**. — [IIFL Silver ETF page](https://live-next.indiainfoline.com/company/icici-prudential-silver-etf-historical-data)
- **Viyash Scientific (VIYASH, formerly SEQUENT)**: the legal name changed with effect from 8 Jan 2026, after a 28 Dec 2025 shareholder postal ballot. The NSE symbol changed from SEQUENT to VIYASH with effect from **23 Jan 2026**. The rename depended on a composite scheme of amalgamation. — [NSE circular](https://nsearchives.nseindia.com/content/circulars/CML72374.pdf); [Company filing](https://nsearchives.nseindia.com/corporate/SEQUENT1_09012026154543_Viyash_Scientific_SE_Intimation.pdf); [NSE Clearing SLB circular](https://nsearchives.nseindia.com/content/circulars/CMPT72442.pdf); [FilingReader](https://filingreader.com/news-wire/mumbai/2025-11-27/sequent-scientific-to-rebrand-as-viyash-scientific-limited)
- **Gujarat Gas → Gujarat Energy (GUJENERGY)**: the GSPC Group restructuring took effect on **1 May 2026**. GSPC and GSPL merged into Gujarat Gas Ltd, and the gas-transmission undertaking was demerged into GSPL Transmission Ltd (GTL). The company transcript gives the name change to Gujarat Energy as effective from **14 May 2026**; a 5paisa blog says 1 Jul 2026, which conflicts with the company filing. GSPL holders received 10 GGL shares per 13 GSPL shares (record date 12 May 2026). — [Company press release](https://gujarat-energy.com/pdf/press-release-gspc-group-merger-effective-date.pdf); [NSE filing](https://nsearchives.nseindia.com/corporate/GUJGASLTD_01052026185056_1564SECIntiPressRelease.pdf); [Q4 transcript](https://nsearchives.nseindia.com/corporate/GUJGASLTD_05062026230023_1579SEITRANSCRIPTQ4FY252601062026.pdf); [FilingReader GSPL record date](https://filingreader.com/news-wire/mumbai/2026-05-04/gujarat-state-petronet-sets-record-date-for-gujarat-gas-merger); contradicted on rename date by [5paisa community](https://tradebetter.5paisa.com/t/what-does-the-gujarat-gas-demerger-mean-for-shareholders/932)
- **537007.BO** is the BSE scrip code of the **ICICI Prudential Nifty 50 ETF**. Its NSE symbol is NIFTYIETF and its ISIN is INF109K012R6. — [BSE](https://bseindia.com/stock-share-price/icici-prudential-nifty-etf/icicinifty/537007); [JM Financial](https://www.jmfinancialservices.in/company-information/icici-prudential-nifty-etf)
- **LIC (LICI)** listed on **17 May 2022**. — **UNVERIFIED in this session** (from memory; widely reported), no source fetched.

### Inferences
- If the decision dates start in early 2022, these names cannot be evaluated on a 200-DMA basis at the earliest decision dates: LICI (usable around 2 Mar 2023), SILVERIETF (around mid-Nov 2022), HDFCSML250 (around 1 Dec 2023), JIOFIN (around 5 Jun 2024), NTPCGREEN (around 12 Sep 2025), TATACAP (around 29 Jul 2026) and LGEINDIA (around 30 Jul 2026).
- In a hindcast these names can only be *bought* after they exist. Any rule that holds them at an earlier decision date leaks information from the present-day portfolio.
- For renamed symbols, Yahoo usually moves history to the new symbol (VIYASH.NS should carry SEQUENT history). This often breaks, though: the new ticker returns only post-rename bars, or the old ticker returns empty. Fetch both the old and new tickers and stitch them (SEQUENT.NS + VIYASH.NS; GUJGASLTD.NS + GUJENERGY.NS).
- **GUJENERGY.NS as a Yahoo symbol is UNVERIFIED.** No NSE symbol-change circular from GUJGASLTD was found. The 19 Jun 2026 filing was still filed under the GUJGASLTD prefix.
- Mapping caution: `GUJPPL` maps to `GPPL.NS`, which is Gujarat Pipavav Port, not GSPL. That matches its "Infrastructure" sector label, but it is worth confirming against the broker statement. If GUJPPL actually meant GSPL, that symbol was delisted in 2026 after the merger.

### Gaps
- LIC and SILVERIETF exact first-trading dates were not confirmed with a primary source in this session.
- No listing dates were fetched for long-history names (ITBEES, MIDCAPETF, BANKNIFTY1, GOLDIETF, NIFTYIETF/537007). They are believed to predate 2022 (Mirae Midcap 150 ETF launched around Jan 2023? **UNVERIFIED**; check it, because if it launched in 2023 it belongs on the late-listing list).
- No GTL (GSPL Transmission) listing date was found.

---

## Q2. Corporate actions 2022-2026 that cause jumps, and yfinance adjustment behaviour

### Takeaway
At least nine bonus, split or demerger events in 2022-2026 affect the map. The most dangerous for this codebase are the **1:1 and 1:2 bonuses** (Reliance, Wipro, Ashok Leyland, HDFC Bank, GAIL, HPCL). Their one-day ratio is 0.5x or 0.67x, inside `SPLIT_JUMP_RATIO = 2.5` (`analysis.py` line 51), so the home-grown fallback will **not** catch them if Yahoo serves them unadjusted. Demergers (Reliance→JFS 2023, Gujarat Gas→GTL 2026) are never adjusted by Yahoo as splits, and they appear as genuine-looking price drops.

### Cited Findings
- **BEL** had a 2:1 bonus with record date 16 Sep 2022 (ex around 15 Sep 2022). — [NSE filing](https://nsearchives.nseindia.com/corporate/BEL_05092022110745_NSE.pdf); [Angel One](https://angelone.in/announcements/market/bonus-issue-of-bel)
- **GAIL** had a 1:2 bonus with record date 7 Sep 2022 (ex 6 Sep 2022). An earlier article said 2 Aug; the later company filing supersedes it. — [GAIL filing](https://GAILONLINE.COM/pdf/InvestorsZone/GeneralDisclosure/RecordDateIntimationBonus.pdf); [Goodreturns](https://www.goodreturns.in/personal-finance/investment/this-maharatna-psu-stock-s-ex-bonus-date-is-approaching-fast-key-points-1260466.html)
- **HPCL** had a 1:2 bonus with record date 21 Jun 2024. — [Business Standard](https://www.business-standard.com/amp/markets/capital-market-news/hpcl-slips-after-q4-pat-drops-12-yoy-to-rs-2-843-cr-board-oks-1-2-bonus-issue-124050900763_1.html); [Bajaj Broking](https://www.bajajbroking.in/blog/hpcl-declares-1-2-bonus-issue-and-rs-16-50-final-dividend)
- **Dr Reddy's** had a 1:5 split (FV ₹5→₹1) with record and ex date 28 Oct 2024. — [Goodreturns](https://www.goodreturns.in/personal-finance/investment/1-5-stock-split-of-dr-reddys-laboratories-record-date-on-october-28-buy-sell-1380799.html); [Angel One](https://www.angelone.in/blog/dr-reddy-share-price-down-executes-stock-split)
- **Reliance** had a 1:1 bonus with record and ex date 28 Oct 2024. — [Business Today](https://www.businesstoday.in/amp/markets/stocks/story/ril-bonus-shares-reliance-fixes-monday-october-28-as-record-date-for-issue-450406-2024-10-16); [Angel One](https://www.angelone.in/news/share-market/reliance-industries-sets-oct-28-record-date-bonus-issue)
- **Reliance → Jio Financial demerger**: JFS's price was discovered at ₹261.85 in a special pre-open session in July 2023, and RIL's price dropped by that amount. JFS listed 21 Aug 2023. — [5paisa](https://5paisa.com/news/jio-financial-services-lists-on-nse-at-rs262-and-on-bse-at-rs265). The exact special-session date (20 Jul 2023) is **UNVERIFIED**.
- **Wipro** had a 1:1 bonus with ex and record date 3 Dec 2024. — [Business Standard](https://www.business-standard.com/amp/markets/news/dividend-bonus-issue-wipro-rajoo-engg-8-others-to-go-ex-date-next-week-124112900423_1.html)
- **Ashok Leyland** had a 1:1 bonus with record date 16 Jul 2025, its first bonus since 2011. — [Business Standard](https://www.business-standard.com/markets/capital-market-news/ashok-leyland-fixes-record-date-for-bonus-issue-125070900380_1.html); [IIFL](https://www.indiainfoline.com/news/companies/ashok-leyland-fixes-july-16-as-record-date-for-11-bonus-issue)
- **Kotak Nifty Bank ETF (BANKNIFTY1)** had a 10:1 unit split (FV ₹10→₹1) with record and ex date **27 Feb 2026**. Kotak Nifty PSU Bank ETF is a separate scheme, with its split on 10 Jul 2026. — [NSE Clearing circular](https://nsearchives.nseindia.com/content/circulars/CMPT73022.pdf); [MSE circular](https://www.msei.in/SX-Content/Circulars/2026/February/Circular-18647.pdf)
- **Gujarat Energy (ex-Gujarat Gas) → GTL demerger**: record date 2 Jul 2026, at 1 GTL share (FV ₹10) per 3 Gujarat Energy shares (FV ₹2). GTL is expected to list on BSE/NSE, but no listing date was found. — [Gujarat Gas/Energy NSE filing](https://nsearchives.nseindia.com/corporate/GUJGASLTD_19062026181348_1583IntiofRD319062026.pdf); [FilingReader](https://filingreader.com/news-wire/mumbai/2026-06-19/gujarat-energy-sets-record-date-for-gspl-transmission-share-allotment)
- **ICICI Prudential Gold ETF** last split in Nov 2018 (₹10→₹1). No 2022-2026 split was found for the Gold or Silver ETF. — [Arihant Capital](https://www.arihantcapital.com/company-information/splits/40430)
- **HDFC Bank** 1:1 bonus, record date around 27 Aug 2025: **UNVERIFIED** (from memory; the search did not confirm it). HDFC Ltd also merged into HDFC Bank on 1 Jul 2023. No HDFCBANK price adjustment was needed, but HDFC.NS history ends there.
- **Vodafone Idea FPO** (Apr 2024, around ₹10-11 per share) and the 2025 government dues-to-equity conversions: **UNVERIFIED**, not confirmed by search. An FPO at market price causes no price jump, only dilution, so no adjustment is needed.
- **yfinance and NSE corporate actions**: practitioners report that yfinance mishandled the HDFC Bank/HDFC merger and "produced completely wrong returns for two years of data". Users on other broker APIs report the same class of unadjusted-history problem. — [Zerodha TradingQnA](https://tradingqna.com/t/has-anyone-found-wrong-adjusted-prices-in-nse-historical-data-for-backtesting/192938); [Angel SmartAPI forum](https://smartapi.angelone.in/smartapi/forum/post/4761)
- The yfinance issue tracker carries an open class of "incorrect handling of historic prices for corporate actions" for non-US exchanges (#1937, GCC stocks). Its details were not opened. — [yfinance issues](https://redirect.github.com/ranaroussi/yfinance/issues)

### Inferences
- yfinance `auto_adjust=True` (the default since 0.2.x) multiplies OHLC by Yahoo's own split and dividend factors. When Yahoo has the split or bonus recorded, history is back-adjusted correctly. When Yahoo misses or delays recording an Indian bonus, the raw jump stays in. This happens most often for ETF unit splits and small-caps. The `repair=True` option in `history()` tries to detect 100x and split errors, but it should not be relied on for bonuses.
- **Code-specific pitfall:** `adjust_unadjusted_splits` only fires on ratios above 2.5x or below 0.4x. Any 1:1 bonus (0.5x) or 1:2 bonus (0.67x) that Yahoo fails to adjust passes through. It produces a fake 50% or 33% one-day crash and corrupts the 50/200-DMA, ATR and 52-week high for about 200 sessions. The NSE ±20% band for non-F&O names, and no band for F&O names, also means a 0.5x day is never a genuine move for these large caps.
- **Recommended approach:** keep a hand-maintained corporate-action table (the dates above) and assert, after download, that the close-to-close ratio on each ex-date is around 1 (adjusted). If it is around 0.5, 0.67, 0.33, 0.2 or 0.1, apply the known factor. This is safer than a generic threshold.
- Demergers (RIL July 2023, Gujarat Gas/Energy July 2026) are not splits. Yahoo typically leaves a real-looking drop, about 9-10% for RIL (₹261.85 / around ₹2,840; exact pre-demerger price UNVERIFIED). For a hindcast this should be treated as a cost-basis transfer to the spun-off share, not as a loss.
- Lower-liquidity ETFs on Yahoo (537007.BO, SILVERIETF, GOLDIETF, MIDCAPETF) often show stale, zero-volume or missing days. BSE `.BO` ETF series are especially sparse. NIFTYIETF.NS is likely a better-populated series for the same fund than 537007.BO.

### Gaps
- The HDFC Bank bonus date and the Vodafone Idea capital events are unverified.
- Whether Yahoo correctly adjusted each 2024-2026 event could not be tested (Yahoo is blocked). This must be checked on the first real download.
- No NHPC, NTPC, SJVN, ONGC, Petronet, JSW Energy, Tata Power, Federal Bank, Tata Consumer or Engineers India splits or bonuses in 2022-2026 were searched. None are known, but this is **UNVERIFIED**.

---

## Q3. Best free benchmark series

### Takeaway
Use Nifty 50 TRI from niftyindices.com as the reference if it can be downloaded (manually or via its historical-data form). Otherwise use NIFTYBEES.NS adjusted close as a TRI proxy. `^NSEI` is a price index that omits dividends of about 1.2-1.5% a year, so over a roughly 4.5-year window it understates the benchmark by an estimated 5-7% cumulative (an inference, not a sourced figure).

### Cited Findings
- NSE/NSE Indices publishes total-returns-index (TRI) series, with dividends reinvested, for its indices. These can be downloaded from the niftyindices.com historical-data section, and community Excel tools exist to pull them. — [freefincal](https://freefincal.com/download-historical-total-returns-index-data-52-nse-indices/) (the page fetch failed with DNS; content comes from the search snippet only)
- Free daily Nifty 50 *price* OHLC datasets exist (Kaggle/Baselight), but they are price indices, not TRI. Index-level volume is often 0. — [Multibagg](https://www.multibagg.ai/market-pulse/articles/nifty50-ohlc-data-download-cmr4lxk3x00x4po0joly0a3p3); [Baselight Kaggle mirror](https://baselight.app/u/kaggle/dataset/sudalairajkumar_nifty_indices_dataset)

### Inferences
- niftyindices.com "Historical Data → Total Returns Index" serves CSV/table output through a POST form. It is known to cap each request to roughly a 1-year window and to block non-browser scrapers. Plan on several manual downloads cached to `data/benchmark/nifty50_tri.csv`. **UNVERIFIED** in this session.
- NIFTYBEES.NS (Nippon India ETF Nifty 50 BeES) with `auto_adjust=True` is a reasonable TRI proxy: it lags the TRI by expense ratio and tracking error, roughly 0.05-0.1% a year. Watch for its own unit-split history (a 2019 split is believed; **UNVERIFIED**). ICICI's NIFTYIETF (537007) is an equivalent alternative. Using 537007.BO as both a holding and the benchmark is fine, but the BSE series is sparser.
- `^NSEI` on Yahoo is generally complete for daily closes, but it is a price index. If it is used, state the dividend-yield bias explicitly or add about 1.3%/yr pro rata.

### Gaps
- The exact current niftyindices.com form limits, and whether TRI can be fetched programmatically in Oct 2026, are not verified.
- No sourced current Nifty 50 dividend-yield figure was found. The 1.2-1.5% range comes from the brief and is **UNVERIFIED** here.

---

## Q4. Reconstructing past holdings from broker "Global Transaction Statement" PDFs

### Takeaway
This is reasonable in principle, because transaction statements list every trade and can be replayed into a holdings ledger. It needs explicit handling of corporate-action credits (bonus, split, demerger allotments), which appear as non-trade entries or not at all. No public specification of the "Global Transaction Statement" format was found in this session.

### Cited Findings
- No source was found that documents the fields of a broker "Global Transaction Statement". **No citable source.**

### Inferences
- Typical Indian broker transaction or tradebook statements (ICICI Direct style, which the broker codes like ASHLEY, HDFBAN and ICINIF suggest) contain: trade date, settlement date, exchange, broker scrip code or name, ISIN (sometimes), buy/sell, quantity, price, trade value, brokerage and charges, and contract-note number. Bonus, split and demerger shares usually do not show up as trades. They appear only in the demat holding statement (CDSL/NSDL CAS) as corporate-action credits.
- Rebuild rule: replay trades in date order, then apply the corporate-action table from Q2 (for example, double ASHOKLEY quantity on 16 Jul 2025; ×10 BANKNIFTY1 units on 27 Feb 2026; credit JIOFIN = RIL qty on the 2023 record date; credit GTL = GUJGA qty / 3 on 2 Jul 2026). Reconcile against the current `portfolio.csv` quantities as the final check.
- Prefer ISIN as the join key, because broker short codes and NSE symbols both change (SEQUENT→VIYASH).

### Gaps
- No example statement or field list was available, so the field list above is an inference.

---

## Q5. Recommended handling rules

### Takeaway
Build the price panel once, cache it, and gate every decision date on data that existed at that date. Exclude names that do not exist yet rather than imputing them.

### Cited Findings
- The current code already requires `len(clean_close) >= 200` before computing the 200-DMA (`analysis.py` around line 89) and tags NO_DATA/NO_TICKER. — local repo, `/home/user/Portfolio/analysis.py`

### Inferences
- See the rules list at the end of this file.

### Gaps
- None beyond those listed above.

---

## Summary table

| Symbol (broker) | Yahoo ticker | First trading date | Usable from (≈ +200 sessions) | Known data issues |
|---|---|---|---|---|
| ASHLEY | ASHOKLEY.NS | pre-2022 | from start | 1:1 bonus, record date 16 Jul 2025 (0.5x, NOT caught by 2.5x rule) |
| FEDBAN | FEDERALBNK.NS | pre-2022 | from start | none known (unverified) |
| HDFBAN | HDFCBANK.NS | pre-2022 | from start | HDFC Ltd merger 1 Jul 2023; 1:1 bonus around Aug 2025 (UNVERIFIED) |
| HDF250 | HDFCSML250.NS | ~15 Feb 2023 | ~1 Dec 2023 | young ETF, thin volume |
| ICIGOL | GOLDIETF.NS | pre-2022 | from start | last split 2018; thin days possible |
| ICINIF | 537007.BO | pre-2022 | from start | BSE ETF series sparse; consider NIFTYIETF.NS |
| ICIPSE | SILVERIETF.NS | ~late Jan 2022 (inception 24 Jan 2022) | ~mid-Nov 2022 | listing date unverified; thin volume |
| NIPNIT | ITBEES.NS | pre-2022 | from start | none known |
| MIR150 | MIDCAPETF.NS | UNVERIFIED (possibly 2023) | UNVERIFIED | check launch date |
| KOTAKBKETF | BANKNIFTY1.NS | pre-2022 | from start | 10:1 unit split 27 Feb 2026 (caught by 2.5x rule if unadjusted) |
| BHAELE | BEL.NS | pre-2022 | from start | 2:1 bonus 16 Sep 2022 (ratio 0.33x, caught) |
| TATGLO | TATACONSUM.NS | pre-2022 | from start | none known |
| JIOFIN | JIOFIN.NS | 21 Aug 2023 | ~5 Jun 2024 | demerged from RIL; T2T first 10 days |
| WIPRO | WIPRO.NS | pre-2022 | from start | 1:1 bonus 3 Dec 2024 (0.5x, NOT caught) |
| ENGIND | ENGINERSIN.NS | pre-2022 | from start | none known |
| LIC | LICI.NS | 17 May 2022 (UNVERIFIED) | ~2 Mar 2023 | none known |
| DRREDD | DRREDDY.NS | pre-2022 | from start | 1:5 split 28 Oct 2024 (0.2x, caught) |
| SEQSCI | VIYASH.NS (old SEQUENT.NS) | pre-2022 | from start if stitched | symbol change 23 Jan 2026; amalgamation; old history may sit under SEQUENT.NS |
| JSWENE | JSWENERGY.NS | pre-2022 | from start | none known (unverified) |
| NHPC | NHPC.NS | pre-2022 | from start | none known |
| NTPC | NTPC.NS | pre-2022 | from start | none known |
| NTPGRE | NTPCGREEN.NS | 27 Nov 2024 | ~12 Sep 2025 | none known |
| SJVLIM | SJVN.NS | pre-2022 | from start | none known |
| TATPOW | TATAPOWER.NS | pre-2022 | from start | none known |
| GAIL | GAIL.NS | pre-2022 | from start | 1:2 bonus 7 Sep 2022 (0.67x, NOT caught) |
| GUJGA | GUJENERGY.NS (old GUJGASLTD.NS) | pre-2022 | from start if stitched | 1 May 2026 GSPC/GSPL merger; rename 14 May 2026 (conflicting 1 Jul); GTL demerger record date 2 Jul 2026 (real-looking drop); Yahoo ticker UNVERIFIED |
| HINPET | HINDPETRO.NS | pre-2022 | from start | 1:2 bonus 21 Jun 2024 (0.67x, NOT caught) |
| ONGC | ONGC.NS | pre-2022 | from start | none known |
| PETLNG | PETRONET.NS | pre-2022 | from start | none known |
| RELIND | RELIANCE.NS | pre-2022 | from start | JFS demerger Jul 2023 (around -₹261.85, real-looking drop); 1:1 bonus 28 Oct 2024 (0.5x, NOT caught) |
| GUJPPL | GPPL.NS | pre-2022 | from start | confirm that broker code = Gujarat Pipavav Port, not GSPL |
| IDECEL | IDEA.NS | pre-2022 | from start | FPO Apr 2024 and govt equity conversions (UNVERIFIED); dilution only, no price jump expected |
| TATCAP | TATACAP.NS | 13 Oct 2025 | ~29 Jul 2026 | very short history |
| LGELEC | LGEINDIA.NS | 14 Oct 2025 | ~30 Jul 2026 | very short history |
| Benchmark | Nifty 50 TRI (niftyindices) / NIFTYBEES.NS adj / ^NSEI | pre-2022 | from start | ^NSEI is price-only (dividend-yield bias of about 1.2-1.5%/yr, unverified) |

## Recommended data rules for the prompt
1. **Point-in-time only:** at decision date D, use bars with date ≤ D-1 (or ≤ D if decisions are made at the close). Never compute indicators on data after D.
2. **Existence gate:** a symbol whose first trading date is after D is **excluded** from the universe at D. Do not impute, backfill or proxy it, and do not count it in weights or sector caps.
3. **Minimum history:** require ≥ 200 valid sessions for 200-DMA signals and ≥ 252 for a 52-week high. Between 50 and 199 sessions, allow only 50-DMA/ATR rules and tag the symbol `SHORT_HISTORY`. Below 50, tag it `INSUFFICIENT_HISTORY` and hold or no-action, with no new buys.
4. **Corporate actions:** use yfinance `auto_adjust=True` (plus `repair=True`), then validate against a hand-maintained ex-date table (the Q2 list). On each known ex-date, a close ratio far from 1 means applying the known factor. Lower or remove the generic `SPLIT_JUMP_RATIO = 2.5` fallback for known events, because 1:1 and 1:2 bonuses slip through it.
5. **Demergers are not splits:** for RIL→JFS (2023) and Gujarat Energy→GTL (2026), carry the parent's position through the drop and credit the child shares on the record date in the holdings ledger. Do not "repair" the price.
6. **Renamed symbols:** fetch both old and new tickers (SEQUENT.NS/VIYASH.NS, GUJGASLTD.NS/GUJENERGY.NS) and stitch on the change date. Treat an empty result as `NO_DATA`, not as zero price.
7. **Missing days:** forward-fill only for valuation (at most 5 sessions). Never forward-fill into indicator inputs. Drop zero-volume ETF days from ATR.
8. **Benchmark:** use Nifty 50 TRI (niftyindices.com, cached CSV) as primary and NIFTYBEES.NS adjusted close as fallback. If `^NSEI` is used, label it a price index and disclose the dividend-yield bias.
9. **Reproducibility:** download once, save raw (unadjusted) and adjusted panels to disk (e.g. `data/prices/{ticker}.parquet` with fetch timestamp and yfinance version), and run the hindcast from the cache only. Yahoo revises adjusted history retroactively, so re-downloads will not match.
10. **Holdings reconstruction:** replay broker transaction-statement trades by ISIN, apply the corporate-action table for bonus, split and demerger credits, and reconcile the final quantities to `portfolio.csv` before trusting any past-date portfolio.
11. **Flag, do not hide:** every decision row should carry a data-quality tag (`OK`, `SHORT_HISTORY`, `NOT_LISTED`, `ADJ_FIXED`, `STITCHED`), so hindcast results can be filtered.
