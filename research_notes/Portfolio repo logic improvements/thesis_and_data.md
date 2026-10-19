# Thesis Monitoring with Fundamentals & Reliable Data Sources for Indian Equities/ETFs

Scope note: research done 2026-10-14. One environment limit: direct downloads from amfiindia.com and the GitHub API were blocked by the sandbox proxy, so AMFI file contents and GitHub repo activity could not be checked first-hand. PyPI release dates *were* checked directly (via the pypi.org JSON API), see Q3.

Repo observations (from reading `thesis.csv`, `analysis.py`, `signal_engine.py`). These are first-hand reads of the repo, not web findings:
- All 36 theses share the same pattern ("Long-term wealth building through conviction in the company's X franchise and growth potential"). None names a measurable KPI, and none can be tested.
- `Invalidation_Price` is the only kill trigger. `signal_engine.py` fires "STRG SELL / thesis invalidated" when `current_price <= Invalidation_Price`. That is a price stop, not a thesis test.
- Some thesis texts and ticker maps disagree:
  - `TATGLO` → `TATACONSUM.NS` (Tata Consumer), but its thesis describes "global digital-connectivity" (that is Tata Communications).
  - `ICIPSE` → `SILVERIETF.NS` (a silver ETF), but its thesis talks about an "underlying equity portfolio".
  - `GUJPPL` → `GPPL.NS`. GPPL is Gujarat Pipavav Port on NSE, but the thesis describes "gas-transmission infrastructure", which is GSPL. GSPL was merged into Gujarat Gas/Gujarat Energy in May 2026 (see Q4). This mapping is very likely wrong.
- `adjust_unadjusted_splits` only treats a day-over-day ratio above 2.5x (or below 0.4x) as a corporate action. A 1:1 bonus or a 2:1 split gives a 0.5x ratio, so it is **not** caught. Demergers (value-redistribution gaps of roughly 10–40%) are not caught either.

---

## Q1. Which KPIs best monitor thesis health per business type, and how do professionals write "kill criteria"?

### Takeaway
Practitioners write the sell triggers *before* buying. They do it as a short pre-mortem: a list of specific, fact-based breaches (not daily price moves) that would force a sale or a re-underwrite. Each holding should carry 3–5 sector-specific KPIs taken from quarterly results and investor presentations, each with a numeric threshold and a persistence rule (for example, 2 consecutive quarters). Price is kept as a secondary "review" trigger.

### Cited Findings
**Kill criteria / thesis-writing practice**
- One UK fund manager writes a one-page pre-mortem for each holding. It lists the sell triggers and the circumstances that would compromise the original thesis, which takes emotion out of the exit decision — [AJ Bell](https://www.ajbell.co.uk/news/why-fund-manager-calls-it-quits-stock)
- Vontobel defines "kill criteria" as a clearly specified set of breaches that trigger a sale. It pairs them with a "would I buy it today?" test and an opportunity-cost check — [Vontobel AM](https://am.vontobel.com/en/insights/quitters-never-win-or-do-they)
- Fidelity describes the pre-mortem: assume the investment has failed at a future date, then work backward to the flaws and warning signs — [Fidelity Canada](https://fidelity.ca/en/insights/articles/lessons-from-three-decades-of-investing)
- A thesis should state what evidence would weaken or invalidate it. Review triggers should be set before purchase and tied to facts, not daily price moves — [Kubera](https://www.kubera.com/blog/investment-thesis)
- Example of explicit rules: sell if revenue growth stays below a threshold for two consecutive years, or if the P/E passes a set multiple — [TIKR](https://www.tikr.com/blog/how-to-know-when-to-sell-a-stock)
- Pre-mortem format: a dated, past-tense paragraph describing a hypothetical 40% loss, then a check of whether a trigger would have caught that cause — [InvestSkill (GitHub)](https://raw.githubusercontent.com/yennanliu/InvestSkill/main/site/content/LEARNING-PSYCHOLOGY.md)
- Evidence quality: the sources are practitioner and educational. No empirical study validating kill criteria was found.

**Banks (HDFC Bank, Federal Bank; also the Kotak bank ETF look-through)**
- Analyst coverage of Indian banks tracks these KPIs every quarter: CASA ratio (e.g., Indian Bank ~41% in FY24 → 38.9% in 2QFY25), GNPA/NNPA (3.95%/0.43% → 3.48%/0.27%), provision coverage ratio (PCR, 92–96%), NIM (~3.4–3.5%), RoA (~0.8–1.2%) and cost-to-income — [Geojit via Indian Bank](https://indianbank.in/wp-content/uploads/2024/08/Analyst-Coverage-by-Geojit-dated-10th-June-2024-Target-Price-Rs.619.pdf); [Motilal Oswal via Indian Bank](https://indianbank.in/wp-content/uploads/2024/08/Analyst-Coverage-by-Motilal-Oswal-dated-28th-October-2024-Target-Price-Rs.650.pdf); [Axis Capital via Indian Bank](https://indianbank.in/wp-content/uploads/2024/02/Analyst-Coverage-by-Axis-Capital-dated-06-May-2024-Target-Price-Rs.650.pdf); [Emkay via Indian Bank](https://indianbank.in/wp-content/uploads/2024/02/Analyst-Report-by-Emkay-Global-dated-07th-May-2024-Target-Price-Rs.650.pdf)
- Analysts treat credit cost (provisions/loans) as the main earnings swing factor, with PCR as the cushion — [Emkay 2022 via Indian Bank](https://www.indianbank.in/wp-content/uploads/2022/09/Analyst-Report-by-Emkay-Global-dated-05.11.2022-Target-Price-Rs.310.pdf)

**Life insurers (LIC)**
- The core KPIs are VNB, VNB margin, APE growth and 13th-month persistency. Examples:
  - HDFC Life Q1FY27: VNB +9% YoY to ₹879 cr, VNB margin ~25%, 13M persistency 84% (vs 86%), APE +9% to ₹3,515 cr — [ICICI Securities](https://mailcontent.icicidirect.com/mailcontent/idirect_hdfclife_q1fy27.pdf)
  - ICICI Pru Life Q3FY26: VNB margin 24.4% (+320 bps), 13M persistency 84.4% (−540 bps), APE +3.6% — [Sharekhan](https://research.sharekhan.com/Research_Uploads/c01ec76d-82be-4edb-a640-fe896342d3c5_ICICI_Prudential_Life-Jan13_2026_2.pdf)
- APE = annualised first-year regular premiums + 10% of single premiums — [Business Standard](https://www.business-standard.com/companies/news/hdfc-life-q2fy26-profit-up-3-percent-on-premium-growth-125101501394_1.html)
- The market reprices insurers sharply on VNB-margin misses: ICICI Pru Life fell 10% on a VNB margin miss — [Business Standard](https://www.business-standard.com/amp/markets/news/icici-pru-life-down-10-as-vnb-margin-misses-estimates-analysts-cut-target-125012200477_1.html)

**PSU / regulated utilities (NTPC, NHPC, SJVN, NTPC Green, Tata Power)**
- NTPC's earnings track regulated capacity commissioning. CERC's cost-plus framework gives about 15.5% RoE on regulated equity. Standalone regulated equity was ₹94,454 cr as of Sep-2025 (+6% YoY), and consolidated ₹1,16,022 cr. Execution of the under-construction pipeline is the key monitorable — [FundsIndia](https://fundsindia.com/blog/equities/alpha-ntpc-ltd-equity-research-desk-2/34293)
- FY24 figures: regulated equity ₹87,700 cr (+13% YoY), standalone commercial capacity 59.1 GW — [ICICI Direct Q4FY24](https://icicidirect.com/mailimages/IDirect_NTPC_Q4FY24.pdf)
- The 15.5% RoE dates from CERC's FY2010-14 regulations — [Angel Research 2013](https://www.angelone.in/get-html-report/NTPC-OFS-060213.html). Tariff-regulation changes have cut utility EPS before (a 2014 RoE rationalisation was expected to dent NTPC EPS by up to 15%) — [Business Standard](https://www.business-standard.com/amp/article/companies/new-tariff-guidelines-to-dent-earnings-114022400856_1.html). Regulated RoE is therefore a kill-criterion KPI, not a constant.

**IT services (Wipro)**
- The KPIs management guides on and analysts track are:
  - quarterly constant-currency (CC) revenue growth against the guided range (Q2FY27 guidance: −1.5% to +0.5% QoQ CC; Q1FY27 actual −1.2% QoQ)
  - large-deal bookings/TCV (Q1FY27: $1.63 bn, +12.9% QoQ)
  - IT services EBIT margin (16.0%, down 130 bps QoQ, a 15-quarter low)

  Sources: [IndiaInfoline](https://www.indiainfoline.com/news/companies/wipro-q1-fy27-results-profit-rises-marginally-margins-fall-to-15-quarter-low-stock-gains-1-77); [IndMoney](https://www.indmoney.com/blog/stocks/wipro-q1-results-analysis); [Wipro Q2FY26 release via Business Wire](https://www.businesswire.com/news/home/20251016051874/en)
- Wipro reports Q2FY27 on 2026-10-15, so the next data point lands the day after this research — [NewsBytes](https://www.newsbytesapp.com/news/business/wipro-to-announce-q2-and-h1-fy27-results-october-15/tldr)

**ETFs (HDFC Smallcap 250, ICICI Nifty 50, Mirae Midcap 150, Nifty IT, Kotak Bank, gold/silver ETFs)**
- For an ETF the thesis-health metrics are tracking error, premium/discount to NAV/iNAV, and liquidity. They are not company fundamentals.
- SEBI's May 2022 circular (as summarised by secondary sources) requires iNAV dissemination during market hours with at most a 15-second lag for equity ETFs. Market makers quote around real-time NAV — [Outlook Money](https://www.outlookmoney.com/news/sebi-postpones-direct-etf-buying-rule-what-it-means-for-eligible-investors--news-212848); [Bajaj AMC](https://www.bajajamc.com/knowledge-centre/indicative-net-asset-value-and-its-work)
- Some Indian ETFs (notably international ETFs) have traded at steep premiums. A June 15, 2026 SEBI circular moves the ETF base price for price bands to the previous day's NAV from April 1, 2027 — [Multibagg (secondary)](https://www.multibagg.ai/market-pulse/articles/international-etfs-nav-premium-warning-cmuwiyeex00013apjziyih41q). Not verified against SEBI's primary text.

### Inferences
- Proposed KPI sets and illustrative kill/review triggers (thresholds are judgement calls for the user to set; they are not taken from sources):
  - **Banks:** loan growth YoY vs system, deposit growth, CASA %, NIM, RoA, GNPA/NNPA, PCR, credit cost, CET1/CRAR.
    - Kill: RoA < 1.0% for 2 consecutive quarters (private bank), or GNPA up >100 bps YoY, or CET1 < 12%.
    - Review: CASA down >300 bps YoY, or NIM compression >30 bps.
  - **NBFC / financial platforms (Tata Capital, Jio Financial):** AUM growth, Stage-3 %, credit cost, RoA, cost of funds, CRAR.
  - **Life insurers (LIC):** APE growth, VNB margin, VNB growth, 13th/61st-month persistency, EV operating RoEV, solvency ratio.
    - Kill: VNB margin falls more than 300 bps below the entry level for 2 quarters while APE is flat or negative, or solvency < 1.5x regulatory minimum.
  - **Regulated power PSUs:** regulated equity growth, commercial capacity added vs plan, PAF/PLF, receivable days, the CERC RoE regime, dividend payout.
    - Kill: CERC lowers allowed RoE, or capacity commissioning <50% of guided for 2 years, or receivable days spike.
  - **Oil & gas:**
    - upstream (ONGC): production volumes, realised price, net of windfall levies
    - OMCs/refiners (HPCL): GRMs, marketing margins, under-recoveries
    - gas transmission/CGD (GAIL, Gujarat Energy, Petronet): volumes (mmscmd), tariff orders from the PNGRB regulator, utilisation of terminals and pipelines
    - Kill: an adverse tariff order, or volume decline over 2 years
  - **IT services:** CC revenue growth vs guidance, TCV/large-deal bookings, book-to-bill, EBIT margin, attrition, top-client concentration.
    - Kill: revenue below the low end of guidance for 3+ quarters together with EBIT margin < X%.
  - **Consumer / durables (Tata Consumer, LG Electronics India):** volume growth, gross margin, ad spend %, market share, working capital days.
  - **Pharma (Dr Reddy's):** US generics revenue, key-product concentration, USFDA inspection outcomes (OAI/warning letter = review trigger), R&D %, India branded growth.
  - **Engineering / defence / capital goods (BEL, Engineers India):** order inflow, order book / sales (years of revenue visibility), execution, EBITDA margin, working capital.
  - **ETFs:** tracking difference vs index (annual), premium/discount vs NAV (flag >1% for equity ETFs, >2–3% for gold/silver), average daily traded value, expense ratio.
    - The "thesis" should be an allocation role (e.g., "core large-cap beta, 10% target weight"), and the trigger should be rebalancing drift, not price.
- Price-based invalidation at ~88% of cost is really a stop-loss. Keep it as a *review* trigger that forces the user to re-check the KPIs, and do not let it auto-flag "thesis invalidated". Holding-specific cases:
  - **Gujarat Energy:** the 1-for-3 GTL demerger (record date 2026-07-02) mechanically lowers the share price, which could falsely trip the price trigger.
  - **Gold/silver ETFs:** price-based triggers suit the tactical trend holds (e.g., ICIGOL, conviction 2/5). For these, a price/trend kill rule is the correct form.

### Gaps
- No authoritative, India-specific "sector KPI primer" (e.g., CFA Institute) was found. The KPI lists come from analyst result notes plus standard practice.
- The current CERC tariff regulation (2024–29 block) RoE value was not verified. The 15.5% figure may carry over from earlier regulations.
- Sector-wide benchmark thresholds (e.g., median private-bank RoA) were not sourced.

---

## Q2. How reliable are yfinance fundamentals for Indian stocks?

### Takeaway
yfinance is an unofficial wrapper around Yahoo's endpoints, intended for personal use. It is rate-limited without published limits, and Indian fundamentals are shallow: about 4 years of statements, frequently missing ratio fields such as `returnOnEquity`, and no bank or insurer KPIs (GNPA, CASA, VNB) at all. It is acceptable for price and dividend history after cross-checking, but it should not be the source of thesis KPIs.

### Cited Findings
- The project is unaffiliated with Yahoo and meant for research and education. Yahoo's API is "intended for personal use only" — [yfinance on PyPI](https://pypi.org/project/yfinance/0.2.39)
- Rate limiting (`YFRateLimitError`) has no published threshold. Blocks are IP-tied and sometimes last over 24 hours. Caching and throttling are recommended — [yfinance GitHub discussion #2431](https://github.com/ranaroussi/yfinance/discussions/2431)
- Users report yfinance gives no more than about 4 years of Indian fundamentals, small price discrepancies against NSE, and missing early-history quotes — [TradingQnA](https://tradingqna.com/t/what-are-api-for-getting-fundamental-data-for-stocks-trading-in-nse-india-free-or-paid/145292); [Quantra](https://quantra.quantinsti.com/community/t/reliable-stock-data-than-yfinance/24919)
- Unadjusted bonuses and splits distort per-share and ratio figures (e.g., book value per share) — [Capitalmind](https://premium.capitalmind.in/2011/02/great-indian-data-suckage-story/)
- yfinance is actively maintained: the latest release is 1.7.0 (2026-08-26), checked directly on [PyPI](https://pypi.org/project/yfinance/)

### Inferences
- In this repo, ROE is the only fundamental, and yfinance often leaves it missing. Treat a missing value as "unknown" rather than as a pass or fail. It is better to source sector KPIs from company results and investor presentations (manual quarterly entry) or from Screener.in exports.
- For banks and insurers, ROE alone is a weak signal anyway. The relevant metrics (RoA, GNPA, VNB margin) are not in yfinance.

### Gaps
- No systematic study was found that measures the yfinance field fill-rate for NSE tickers. The repo could measure this itself, for example by logging the share of holdings with non-null `returnOnEquity`.
- Yahoo's current ToS text was not retrieved directly.

---

## Q3. Alternatives: official NSE/BSE data, Screener.in, broker APIs, AMFI, and Python libraries (cost, terms, maintenance as of Oct 2026)

### Takeaway
The most reliable free *price* source is the official NSE/BSE end-of-day bhavcopy (UDiFF format since July 2024). For a long-term tool, the most robust path is one bhavcopy download per day, or a broker API. Zerodha Kite Connect costs ₹2,000/month with historical data now included. Angel One SmartAPI is free.

NSE's website ToS prohibits automated scraping. The NSE wrapper libraries (nsepython, jugaad-data, nselib) are actively released in 2026, but they scrape nseindia.com and break when the site changes.

For fundamentals, Screener.in premium CSV export is the practical low-cost option; it has no API. ETF NAVs come free from AMFI's daily NAVAll.txt.

### Cited Findings
**NSE/BSE official**
- NSE retired the old CM bhavcopy "w.e.f. July 08, 2024" (circular 62424, dated 12-Jun-2024) in favour of the SEBI-mandated UDiFF format. Legacy .MS/.MD extranet bhavcopy files are being retired, with the date extended from 12-Oct-2026 to 16-Nov-2026 — [NSE All Reports](https://www.nseindia.com/all-reports); [NSE circular MSD74764](https://nsearchives.nseindia.com/content/circulars/MSD74764.pdf); [TeamLease RegTech summary](https://teamleaseregtech.com/updates/article/59714/nse-notified-regarding-the-streamlining-of-eod-information-disseminati); [BSE UDiFF](https://bseindia.com/static/members/udiff.aspx)
- NSE ToS: users may not use "any automated means… scraping, data mining, extraction, harvesting" on the website or app. The data-products terms require express written consent for scraping — [NSE Terms of Use](https://www.nseindia.com/static/nse-terms-of-use); [NSE FIXEDIN terms](https://analytics.nseindia.com/assets/images/FIXEDIN-Terms-of-Use.pdf)
- Users report NSE banning IPs that scrape — [Quantra forum](https://quantra.quantinsti.com/community/t/fetching-data-from-nse-site-and-nsepy/22667) (anecdotal)
- XBRL financial results are filed through NSE's NEAPS and made downloadable on the NSE website in XBRL format — [NSE circular 2018](https://archives.nseindia.com/content/equities/NSE_Circular_13042018.pdf). No public XBRL API was found.

**Broker APIs**
- Zerodha Kite Connect costs ₹2,000 per app per month. Historical data has been free with the base subscription since 8-Feb-2025 (previously a separate ₹2,000 add-on) — [Zerodha support](https://support.zerodha.com/category/trading-and-markets/kite-api/articles/what-are-the-charges-for-kite-apis); [Kite forum announcement](https://kite.trade/forum/discussion/comment/49021/)
- Kite users report historical candles that were not adjusted after corporate actions, with >20% single-day gaps — [Kite forum](https://kite.trade/forum/discussion/comment/52478/). Broker data still needs validation.
- Angel One SmartAPI is free of cost, including historical data (NSE, BSE, NFO, MCX, etc.), but rate limits apply — [Angel One](https://www.angelone.in/knowledge-center/smartapi/detailed-introduction-to-smartapi); [SmartAPI forum](https://smartapi.angelone.in/smartapi/forum/post/14627)
- Upstox API was described as free in an early-2024 forum post. Current pricing was not verified — [Upstox community](https://community.upstox.com/t/developer-api-pricing/3796)
- Dhan: no information found.

**Screener.in**
- Has no API. CSV export of screen results is premium-only, up to 50 columns — [Screener support](https://support.screener.in/article/28-export-screen-results)
- The current premium price was not verified. An old figure of ₹100/month introductory is likely stale — [Zerodha Z-Connect](https://zerodha.com/z-connect/wp-json/wp/v2/posts/6992)

**AMFI (ETF/MF NAV)**
- AMFI publishes NAVAll.txt daily: semicolon-delimited, with scheme code, ISINs, scheme name, NAV and date. Historical NAV downloads are capped at 90 days per request — [AMFI NAV download](https://www.amfiindia.com/net-asset-value/nav-download); [Portfolio Performance help](https://help.portfolio-performance.info/en/how-to/downloading-historical-prices/indian/)
- It was not confirmed first-hand whether every ETF appears in NAVAll.txt (the download was blocked from this sandbox). The Portfolio Performance guide points to AMFI as the ISIN lookup for ETFs.

**Python libraries (latest release, checked on PyPI 2026-10-14)**
- jugaad-data 0.35.10, released 2026-10-06. It supports the "new NSE website" and includes bhavcopy helpers — [PyPI](https://pypi.org/project/jugaad-data)
- nsepython 2.101, released 2026-10-07 — [PyPI](https://pypi.org/project/nsepython/); [Unofficed](https://unofficed.com/nse-python/)
- nselib 2.5.1, released 2026-05-01 (frequent releases Feb–May 2026) — [piwheels](https://www.piwheels.org/project/nselib/)
- aynse 1.4.0, released 2026-03-10 — [piwheels](https://www.piwheels.org/project/aynse/)
- bhavkit downloads and cleans NSE bhavcopies into DuckDB — [PyPI](https://pypi.org/project/bhavkit/)
- Wrapper libraries "may not always function as expected" — [Quantra](https://quantra.quantinsti.com/community/t/nsepy-library/26341)

### Inferences
- Frequent 2026 releases of nsepython and jugaad-data suggest active maintenance, and also suggest frequent breakage from NSE site changes. They all scrape nseindia.com, which conflicts with NSE's ToS. For a personal long-term tool, one daily download of the published bhavcopy archive is low-risk in practice but not formally permitted, so the user should decide.
- Suggested source hierarchy:
  1. **Prices:** bhavcopy (NSE/BSE) as primary, yfinance as secondary or cross-check. If the user already trades through Angel One or Zerodha, use that API.
  2. **ETF NAV:** AMFI.
  3. **Corporate actions:** NSE/BSE corporate announcements and actions, kept in a manually maintained local CSV (see Q4).
  4. **Fundamental KPIs:** quarterly manual entry from results and investor presentations, or a Screener premium export.

### Gaps
- Tickertape: pricing and export terms not researched (out of budget).
- Dhan and current Upstox API pricing, plus exact rate limits for SmartAPI and Kite, were not verified.
- No official NSE/BSE fundamentals API was found. BSE's XBRL download path was not checked.
- GitHub commit and issue activity for these libraries could not be checked (access blocked). Maintenance is inferred from PyPI release dates only.

---

## Q4. How should corporate actions (splits, bonuses, demergers, mergers) be handled robustly?

### Takeaway
Use explicit corporate-action records with official ratios, not jump heuristics.

For splits and bonuses, NSE's own factor is: split factor = new/old shares, bonus factor = (A+B)/B for an A:B bonus. Divide pre-ex-date prices by the combined factor and multiply quantities by it.

Demergers redistribute value. They need the company-declared cost-of-acquisition split, and the tool must add the new listed entity as a holding. Vendors, including brokers, sometimes leave these gaps unadjusted.

### Cited Findings
- In NSE's BAJAJFINSV circular, the 5:1 split factor is 5 and the 1:1 bonus factor is 2, giving a combined factor of 10. Strikes are divided by the factor and lots multiplied by it — [NSE circular FAOP53548](https://archives.nseindia.com/content/circulars/FAOP53548.pdf)
- Demergers redistribute value, so a gap remains in price history. Siemens' chart was adjusted using a company-declared cost-of-acquisition ratio (76.18%). Vendor data for the ABFRL demerger showed unadjusted gaps — [TradingQnA (Siemens)](https://tradingqna.com/t/why-siemens-nse-chart-is-still-not-adjusted-for-corporate-action-on-4-apr-2025/183188); [TradingQnA](https://tradingqna.com/t/has-anyone-found-wrong-adjusted-prices-in-nse-historical-data-for-backtesting/192938) (user forum, not official)
- Broker historical data has also been reported unadjusted after corporate actions — [Kite forum](https://kite.trade/forum/discussion/comment/52465/)
- **Gujarat Gas → Gujarat Energy (directly relevant to holding GUJGA/GUJPPL):**
  - A composite scheme took effect on 1 May 2026: GSPC, GSPL and GSPC Energy were merged into Gujarat Gas, and the gas transmission business was demerged into GSPL Transmission Ltd (GTL) — [NSE filing 01-May-2026](https://nsearchives.nseindia.com/corporate/GUJGASLTD_01052026181737_1563SECEffectivedatecomm01052026.pdf)
  - Renamed Gujarat Energy Ltd w.e.f. 14 May 2026. 62,27,14,719 shares were allotted to GSPC/GSPL shareholders around 16 May 2026 — [FilingReader](https://filingreader.com/news-wire/mumbai/2026-05-16/gujarat-energy-allots-6227-crore-shares-in-major-restructuring); [Investor presentation](https://nsearchives.nseindia.com/corporate/GUJGASLTD_01062026130105_1575InvestorspresenetationMay26.pdf)
  - GTL demerger ratio: 1 GTL share (₹10 FV) for every 3 Gujarat Energy shares (₹2 FV), with record date 2 July 2026 — [NSE filing 19-Jun-2026](https://nsearchives.nseindia.com/corporate/GUJGASLTD_19062026181348_1583IntiofRD319062026.pdf)
  - Whether GTL has actually listed (and under which symbol) was **not confirmed**.

### Inferences
- The current 2.5x heuristic misses common Indian actions: 1:1 bonus (0.5x), 2:1 split (0.5x), 1:2 bonus (0.67x), and all demergers.
- NSE price bands do not apply to F&O stocks in the same way, so a "no move larger than X" assumption is fragile. Lowering the threshold to catch 0.5x would collide with genuine large moves. An explicit corporate-actions table is the robust fix.
- For mergers and demergers, the portfolio's *quantity and cost basis* must change, not just the price series:
  - A former GSPL holder now holds Gujarat Energy shares (at the scheme swap ratio) plus GTL shares.
  - The cost basis should be split using the company-declared cost-of-acquisition apportionment, which is published for tax purposes after demergers.
  - The `Invalidation_Price` must be rescaled by the same factor.
- The ticker map should carry an `effective_from` / `effective_to` per symbol, so history stitches correctly across renames (GUJGASLTD → GUJENERGY).

### Gaps
- NSE's official equity corporate-actions adjustment page (products-services/equity-derivatives-corporate-actions-adjustments) was not retrieved, so the formal cost-of-acquisition formula for demergers is unverified.
- The GTL listing date and symbol, and the GSPL → Gujarat Energy swap ratio, were not confirmed.

---

## Q5. What data-quality checks should the tool run?

### Takeaway
Cross-source price checks, staleness checks, corporate-action gap detection, ETF premium/discount vs NAV, and ticker-identity checks would have caught every failure the repo has hit so far: wrong tickers, unadjusted splits, the Gujarat restructuring, short-history ETFs, and empty Yahoo responses.

### Cited Findings
- Small price discrepancies between Yahoo and NSE are reported — [Quantra](https://quantra.quantinsti.com/community/t/reliable-stock-data-than-yfinance/24919). Unadjusted gaps also appear in broker data — [Kite forum](https://kite.trade/forum/discussion/comment/52478/)
- Equity ETF iNAV is disseminated with at most a 15-second lag. Market makers quote around NAV, but premiums can be steep (international ETFs) — [Bajaj AMC](https://www.bajajamc.com/knowledge-centre/indicative-net-asset-value-and-its-work); [Multibagg](https://www.multibagg.ai/market-pulse/articles/international-etfs-nav-premium-warning-cmuwiyeex00013apjziyih41q)
- yfinance rate limiting causes silent or empty responses unless they are handled — [yfinance #2431](https://github.com/ranaroussi/yfinance/discussions/2431)

### Inferences (proposed checks)
1. **Identity check:** the ISIN from the broker statement must match the ISIN of the mapped ticker in the bhavcopy or AMFI file. This would catch `GUJPPL→GPPL.NS` (port company vs gas transmission) and similar errors. Also check that the thesis "business type" matches the instrument sector (would catch TATGLO and ICIPSE).
2. **Staleness:** the last bar date must be within 1–3 trading days of today (using an NSE holiday calendar). Flag zero-volume or flat-price streaks.
3. **Cross-source price:** compare the yfinance close with the bhavcopy close (or the broker LTP already in `portfolio.csv`). Flag if the difference is above 1–2%. The repo already has a broker `fallback_price`, so use it as the reference.
4. **Corporate-action gaps:**
   - Any |1-day return| above ~15% that has no news or known action in the local `corporate_actions.csv` should be flagged for manual review rather than auto-rescaled.
   - Any known action whose ratio does not match the observed gap should also be flagged.
5. **History sufficiency:** if bars are fewer than 200, mark the 200-DMA as unavailable instead of computing it on short data (relevant for new ETFs).
6. **ETF premium/discount:** (price − latest AMFI NAV) / NAV. Flag above 1% for equity ETFs and above 2–3% for commodity ETFs, and use NAV for valuation when the spread is large.
7. **Fundamentals freshness:** each KPI row carries `as_of_quarter`. Flag KPIs older than 2 quarters (i.e., results season passed with no update).
8. **Empty/null fetches:** log them explicitly and fall back to the secondary source. Never treat a missing value as a pass.

### Gaps
- No published industry standard for retail data-validation thresholds was found. The thresholds above are suggestions.

---

## Recommended changes for the repo

These are inferences that synthesise the findings above.

**1. Replace `thesis.csv` with a structured schema.** Use two files, or a single YAML per holding:

`thesis.csv` (one row per holding):

| column | example |
|---|---|
| symbol | HDFBAN |
| isin | INE040A01034 |
| instrument_type | stock / etf |
| business_type | bank / nbfc / life_insurer / regulated_utility / oil_gas_upstream / omc / gas_midstream / it_services / consumer / pharma / capital_goods / equity_etf / commodity_etf |
| role | core / satellite / tactical |
| thesis | 1–3 specific, falsifiable sentences ("deposit franchise sustains CASA >35% and RoA ≥1.8% while loan growth ≥ system") |
| pre_mortem | "If this loses 40% in 3 yrs it will be because…" |
| conviction | 1–5 (integer; move the text label to `role`) |
| entry_date, entry_price | |
| review_price | price that forces a re-check (renamed from Invalidation_Price; not an auto-sell) |
| hard_stop_price | optional, only for `tactical` holdings |
| target_weight, max_weight | for ETF/allocation roles |
| next_review_date | e.g. results date + 7 days |
| last_reviewed | date |

`thesis_kpis.csv` (one row per KPI per holding):
`symbol, kpi, direction(>=,<=), threshold, persistence_quarters, severity(kill|review), source(manual|screener|yfinance), latest_value, as_of_quarter, notes`

Example rows:
- `HDFBAN, roa_pct, >=, 1.7, 2, kill`
- `LIC, vnb_margin_pct, >=, <entry−3pp>, 2, review`
- `NTPC, regulated_equity_yoy_pct, >=, 5, 4, review`
- `WIPRO, cc_rev_growth_vs_guidance_low, >=, 0, 3, kill`
- `ICINIF, premium_to_nav_pct, <=, 1, 1, review`

**2. Change `signal_engine.py`:**
- "THESIS INVALIDATED" should fire on KPI kill breaches (with persistence), not on price.
- Price ≤ `review_price` should give "REVIEW THESIS", not "STRG SELL", except for `role=tactical`, where a price stop is legitimate.
- Missing or stale KPI data should give "THESIS UNVERIFIED".

**3. Data pipeline:**
- Prices: NSE/BSE UDiFF bhavcopy, downloaded once a day and cached locally (e.g., parquet or DuckDB), as primary. yfinance becomes the secondary source and cross-check, with caching and throttling. A broker API (Angel SmartAPI free; Kite ₹2,000/month) is an option if the user already has an account there.
- ETFs: AMFI NAVAll.txt, mapped by ISIN, for NAV, premium/discount and as a fallback when Yahoo returns nothing.
- Fundamentals: a quarterly manual update of `thesis_kpis.csv` from results and investor presentations, optionally assisted by a Screener.in premium CSV export. Drop the dependency on yfinance `returnOnEquity`, or keep it as informational only.
- Ticker master `instruments.csv`: `broker_symbol, isin, nse_symbol, bse_code, yf_ticker, effective_from, effective_to, successor_symbol`. Replaces the hard-coded `TICKER_MAP` and handles renames and successions (GUJGASLTD→GUJENERGY, GSPL→GUJENERGY+GTL).
- `corporate_actions.csv`: `isin, ex_date, type(split|bonus|merger|demerger|consolidation), ratio_new, ratio_old, cost_apportion_pct, new_isin`. Use it to adjust history, quantities, cost basis and review prices. Remove reliance on the 2.5x jump heuristic, or keep the heuristic only as a *detector* that raises a warning.

**4. Validation checks (run on every refresh; print a data-quality section in the report):**
- ISIN identity match; staleness; cross-source price deviation; unexplained gaps above 15%; history length below 200 bars; ETF premium/discount; KPI freshness; null-fetch logging.

**5. Immediate data fixes found while reading the repo:**
- `GUJPPL→GPPL.NS` is very likely wrong. GPPL is Gujarat Pipavav Port, while the thesis describes GSPL gas transmission, which merged into GUJENERGY in May 2026, with GTL shares due from the July 2026 demerger. Reconcile holdings with the broker statement.
- `TATGLO` thesis text describes Tata Communications, but the ticker is Tata Consumer.
- `ICIPSE` thesis describes an equity portfolio, but the ticker is a silver ETF.
- Rescale the GUJGA `Invalidation_Price` for the 1:3 GTL demerger.
- Rewrite all boilerplate theses using the schema above.
