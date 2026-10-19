# Options hedging, option income and short selling for an Indian retail investor (~₹6.75L, 34 NSE stocks/ETFs), as of Oct 2026

Scope note: this is a feasibility assessment, not trading advice. Numbers marked **[UNVERIFIED]** come from memory or from my own model calculations, not a fetched source. The research was limited to about 15 tool calls. Primary SEBI and NSE circular PDFs were not fetched directly, so most regulatory facts below are cited through broker and press summaries. Cboe's site could not be fetched because DNS failed.

**Bottom line in one paragraph:** SEBI's minimum index contract size is ₹15 lakh, and after the Dec-2025 lot revision one Nifty lot is 65 units, roughly ₹16–17L at Nifty ~25–26k. That makes the smallest index hedge about 2.4–2.6x this portfolio's notional. A "protective put" here is therefore mostly a leveraged bearish bet, not a hedge. Covered calls are physically impossible on a ₹6.75L book: you would need to own a full Nifty lot (~₹16L of NIFTYBEES) or a full stock lot. Retail short selling is limited to intraday in cash, to F&O (the same big lots) or to a thin SLB market. Even setting size aside, the global evidence (Israelov 2019; Cboe PPUT/CLL) says that systematically buying puts is an expensive and path-dependent way to cut drawdowns compared with simply holding less equity. SEBI's own data shows about 91% of individual F&O traders lose money. The defensible model output is a **hedge-cost / exposure-equivalence calculator**. It is not an options strategy engine.

---

## 1. Current SEBI F&O framework and whether ₹6.75L can be hedged with index options

### Takeaway
Index derivative contracts must be worth ₹15–20 lakh when they are set or reviewed, and a Nifty lot is now 65 units (from Dec 2025/Jan 2026). One lot is therefore about 2.5x a ₹6.75L portfolio. You cannot hedge this portfolio in fractions, so any index option position either over-hedges heavily or does not happen at all.

### Cited Findings
- SEBI's 1 Oct 2024 circular requires an index derivative to be worth at least ₹15 lakh at launch, with lot sizes set so that contract value on the review day is between ₹15 and ₹20 lakh. — [Business Standard](https://www.business-standard.com/amp/markets/news/sebi-announces-six-key-changes-to-curb-speculation-in-derivatives-trading-124100101316_1.html); [Arihant Capital](https://blog.arihantcapital.com/sebi-tightens-the-reins-introduces-6-new-measures-for-fo-trading/)
- Nifty lot moved from 25 to 75 for new contracts from 20 Nov 2024. Some sources give 21 Nov because of a holiday. — [Groww](https://groww.in/blog/nse-increases-lot-sizes-for-index-derivatives); [Zerodha bulletin](https://zerodha.com/marketintel/bulletin/393605/revision-in-lot-size-of-index-derivative-contracts-from-november-20-2024)
- NSE circular of 3 Oct 2025 cut the Nifty lot from 75 to 65, Bank Nifty to 30 and Fin Nifty to 60. Nifty Next 50 stayed at 25. The change applied from 30 Dec 2025. The first weekly expiry with 65 was 6 Jan 2026 and the monthly switched at the 27 Jan 2026 expiry. — [Zerodha bulletin](https://zerodha.com/marketintel/bulletin/429705/revision-in-lot-size-of-index-derivative-contracts-from-december-30-2025); [Business Standard](https://www.business-standard.com/amp/markets/news/key-f-o-changes-from-today-lower-nifty-bank-nifty-lots-swiggy-3-more-to-debut-125123100084_1.html)
- Other measures in the Oct 2024 package:
  - weekly expiries limited to one benchmark index per exchange
  - option premium collected upfront from buyers
  - extra tail-risk margin (ELM) on expiry day
  - calendar-spread margin benefit removed on expiry day
  - intraday monitoring of position limits

  — [Groww](https://groww.in/blog/nse-increases-lot-sizes-for-index-derivatives); [Outlook Business / summaries](https://www.outlookbusiness.com/markets/sebi-measures-reduce-equity-fo-losses-for-retail-investors-in-fy26)
- In one broker example, margin for selling one Nifty option roughly tripled, from about ₹70k to about ₹2.1L, after the lot increase. — [Groww](https://groww.in/blog/nse-increases-lot-sizes-for-index-derivatives)
- India VIX was about 12.2 on 29 Jul 2026. Its 52-week range was about 8.7–28.9. — [Kotak Neo](https://www.kotakneo.com/indices/indian-indices/india-vix/)
- Nifty 50 was 25,471 on 12 Feb 2026. — [5paisa](https://www.5paisa.com/share-market-today/india-vix)

### Inferences
- At Nifty 24,000–27,000, one 65-unit lot is about **₹15.6L–17.6L notional**. That is **2.3–2.6x** the ₹6.75L portfolio, before any beta adjustment.
- **The hedge ratio is integer-only:** 0 lots gives 0% hedge and 1 lot gives about 250%. Bank Nifty (30 × ~55–60k) and Nifty Next 50 (25 × ~65–70k) land in the same ₹15–20L band by design. No index contract is small enough.
- A deep-OTM put has delta well below 1. For example, a 10% OTM 3-month put might have delta of about −0.1 to −0.15 **[UNVERIFIED model estimate]**. In delta terms it hedges only about ₹1.6–2.5L of exposure at inception, and the hedge grows only once the market falls. Its convexity is ~2.5x what the portfolio "needs", so in a crash the position becomes net short. That is speculation, not insurance.
- Buying a put is a defined-risk trade (the premium), so the large selling margins do not apply to a pure put buyer. Collars and covered calls do involve short options and therefore margin, unless the long underlying is pledged with the broker.
- **Gap [UNVERIFIED]:**
  - Weekly expiry days were moved to Tuesday (NSE) and Thursday (BSE) from Sep 2025.
  - SEBI introduced delta-based (future-equivalent) open-interest position limits in 2025.
  - Neither was verified against SEBI circulars in this session.
  - Neither affects the size conclusion.

### Gaps
- SEBI and NSE circular PDFs were not read directly.
- I did not confirm whether stock-derivative minimum contract value is still ₹5L, or whether SEBI raised it in 2025–26 **[UNVERIFIED]**.
- I did not find the Nifty spot level or India VIX for Oct 2026 itself. The latest found is Jul 2026.
- I did not verify the current per-stock lot values for the investor's 34 holdings.

---

## 2. SEBI studies on retail F&O outcomes

### Takeaway
Across FY22–FY26, about 9 in 10 individual F&O traders lost money. Losses peaked at about ₹1.06–1.12 lakh crore in FY25 and were about ₹91.7k crore in FY26, with average loss per trader rising to about ₹1.17L. Persistent traders do worse, not better.

### Cited Findings
- **FY25 (SEBI study, July 2025):**
  - about 91% of individual traders in equity derivatives lost money
  - net losses after costs were ₹1,05,603 crore, up from ₹74,812 crore in FY24
  - average loss per trader was about ₹1.1L
  - unique individual traders fell from 61.4L in Q1 FY25 to 42.7L in Q4

  — [Business Standard](https://www.business-standard.com/amp/markets/news/net-losses-of-traders-in-fo-widens-in-fy25-sebi-study-125070701221_1.html); [Value Research](https://www.valueresearchonline.com/stories/225398/average-trader-lost-rs-1-1-lakh-fo-fy25/); [Business Standard (91%)](https://www.business-standard.com/markets/capital-market-news/sebi-sees-dip-in-derivatives-turnover-91-of-retail-traders-lose-money-in-fy25-125070800660_1.html)
- **FY26 (Finance Ministry reply in Rajya Sabha):**
  - individual traders' net F&O losses were ₹91,685 crore, against ₹1,11,788 crore for FY25 on this basis (about −18%)
  - average loss rose to ₹1,16,654 from ₹1,13,913
  - individual traders fell to 78.6L from 98.1L

  The FY25 aggregate differs from SEBI's ₹1,05,603 crore, probably because of a different universe or cost treatment (note the conflict). — [Moneylife](https://www.moneylife.in/article/retail-fo-traders-lose-rs91685-crore-in-fy26-despite-sebi-curbs-average-loss-hits-rs117-lakh-govt/81318.html); [Bajaj Broking](https://www.bajajbroking.in/share-market-news/f-and-o-losses-fall-18-percent-average-loss-per-trader-rose-to-rupees-1-16-lakh)
- A later SEBI analysis is reported to find that the loss-maker share rises from about 91% among first-year traders to over 95% among those trading 4+ consecutive years. This is from a search summary and was not verified at the primary source. — [Value Research](https://www.valueresearchonline.com/stories/225398/average-trader-lost-rs-1-1-lakh-fo-fy25/) **[secondary]**

### Inferences
- These studies cover mostly speculative, short-dated, often expiry-day trading, not long-dated protective hedges. They do not prove that hedging loses money. They do show three things relevant here: retail execution costs are high, the volatility risk premium (VRP) runs against option buyers on average, and behavioural drift from "hedging" to "trading" is common.
- A ~₹1.17L average annual loss is about 17% of this investor's whole portfolio. The downside of mission creep is material.

### Gaps
- There is no SEBI breakdown of hedgers versus speculators, or of long-dated option buyers specifically.

---

## 3. Protective puts and collars on Nifty: cost, drag and evidence

### Takeaway
Under typical India VIX levels (about 11–15), a 3-month 5% OTM Nifty put costs roughly 0.4–0.8% of notional, or about 1.5–3% a year, and more after skew. Because of the lot size, the rupee cost is spread over a 2.5x notional. For this portfolio that is about 1–1.8% of portfolio value per quarter, or about 4–7% a year. Israelov (AQR) shows protective puts are path-dependent and usually cut drawdowns less effectively than simply holding less equity.

### Cited Findings
- **Israelov, "Pathetic Protection: The Elusive Benefits of Protective Puts"** (J. Alternative Investments 21(3), 2019):
  - put protection is "quite ineffective" at reducing drawdowns compared with statically reducing exposure
  - it works only if option tenor matches the (unknowable) drawdown length
  - over 250-day windows, the max drawdown was −32.1% protected against −20.9% for an equal-cost divested portfolio
  - because of path dependence and option expensiveness (the VRP), puts "may do more harm than good"

  — [AQR](https://www.aqr.com/Insights/Research/White-Papers/Pathetic-Protection-The-Elusive-Benefits-of-Protective-Puts); [Alpha Architect summary](https://alphaarchitect.com/pathetic-protection/)
- Cambridge Associates (2021) also discusses the challenges of portfolio protection with equity puts. — [Cambridge Associates PDF](https://publishedresearch.cambridgeassociates.com/wp-content/uploads/2021/05/2021-05-Portfolio-Protection-Challenges-with-Equity-Put-Options.pdf) (not read in full)
- **Cboe benchmarks:**
  - A 2016 Wilshire study (1986–2016) of option strategy indices, including PPUT, BXM and CLLZ, found max drawdowns about 24% lower on average than the S&P 500. PUT and BXMD had the best absolute and risk-adjusted returns. Note that PUT is put *writing*, not buying. — [Hedgeweek](https://www.hedgeweek.com/options-indices-offered-noteworthy-returns-over-30-years-says-study/)
  - A 2012 Cboe-commissioned study (1986–2011) gave cumulative growth of PUT 1153%, BXM 830%, S&P 500 807% and CLL (collar) 368%. Volatility of PUT, BXM and CLL was about 30% below the S&P 500's. — [Mondo Visione](https://mondovisione.com/media-and-resources/news/new-study-compares-25-year-performance-of-options-strategy-benchmarks-to-traditi-2012214/)
  - Israelov & Klein (2016, data to 2014): the CLL collar index had annualised excess return of 3.2% against 7.3% for the S&P 500. — [CXO Advisory](https://www.cxoadvisory.com/equity-options/equity-index-collar-performance)
- A 2007 Indian academic paper on Nifty options reports that covered-call and protective-put portfolios beat unhedged ones on risk and return. The sample is small and old, and I treat it as weak evidence. — [Management Dynamics](https://managementdynamics.researchcommons.org/journal/vol7/iss2/3)

### Model payoff math (Black-Scholes, r = 6%, no skew, no dividends) **[UNVERIFIED — my own calculation, not market quotes]**

| 3-month Nifty put | IV 12% | IV 15% | IV 20% |
|---|---|---|---|
| ATM, % of notional | 1.70% | 2.28% | 3.26% |
| 5% OTM | 0.39% | 0.75% | 1.47% |
| 10% OTM | 0.05% | 0.16% | 0.52% |
| 5% OTM, rolled 4x/yr (annual) | ~1.6% | ~3.0% | ~5.9% |

- OTM Nifty puts trade at higher IV than ATM (put skew), so real 5–10% OTM prices are likely above the flat-IV numbers **[UNVERIFIED]**.
- **Rupee cost for this investor:** one lot at about ₹16.6L notional, 5% OTM, IV 15%, costs about ₹12.5k per quarter. That is about **1.8% of a ₹6.75L portfolio per quarter (~7%/yr)**. At IV 12% it is about ₹6.5k per quarter (~3.8%/yr). Long-run Nifty equity premium is plausibly about 5–7%/yr **[UNVERIFIED]**, so continuous hedging could consume most of it.
- **Equivalent "hold less equity" alternative:** cutting equity from 100% to 80% gives a deterministic 20% cut in loss on any drawdown. It costs only the forgone equity premium on ₹1.35L, about 0.7–1.0% of the portfolio a year at a 5–7% premium **[UNVERIFIED]**. It also needs no lots, no rolls and no margin.

### Inferences
- **Hypothesis:** "Puts reduce tail loss cheaply." Evidence: rejected, both globally (Israelov, CLL underperformance) and structurally for this investor (lot size, VRP).
- **Failure modes:**
  - Slow grinding bear markets: puts expire worthless repeatedly.
  - Crashes that recover before expiry.
  - Basis risk between a 34-stock book (with mid and small caps) and Nifty 50.
  - Over-hedging turns the position into a directional short.
  - Roll timing and liquidity in far-OTM quarterly strikes.
  - Behavioural drift into short-dated trading.
- **A zero-cost collar** (sell an OTM call to fund the put) needs the short call to be covered. Otherwise it is margined as a naked short call on ~₹16L notional with uncapped upside loss above the call strike, which is exactly what happens in Indian bull runs.

### Gaps
- I found no NSE Indices protective-put or collar strategy index for Nifty with a factsheet.
- Historical Nifty IV skew data (and India VIX history versus realised volatility) was not pulled. The size of the VRP in India is therefore unquantified here.

---

## 4. Covered calls on Nifty and on stocks

### Takeaway
Globally, buy-write (BXM) has historically delivered roughly equity-like returns with about 30% lower volatility. The cost is capped upside in strong rallies. For this investor it is infeasible: you must own a full lot of the underlying (~₹16L of Nifty, or ₹5L+ per stock lot), and the portfolio averages about ₹20k per holding.

### Cited Findings
- From 1986–2011, BXM grew 830% against 807% for the S&P 500, with about 30% lower volatility. — [Mondo Visione](https://mondovisione.com/media-and-resources/news/new-study-compares-25-year-performance-of-options-strategy-benchmarks-to-traditi-2012214/)
- The Wilshire 2016 study found options-based indices had smaller drawdowns, and BXMD was among the best risk-adjusted performers. — [Hedgeweek](https://www.hedgeweek.com/options-indices-offered-noteworthy-returns-over-30-years-says-study/)
- I did not find an NSE "Nifty 50 BuyWrite / Covered Call" strategy index factsheet in this session.

### Model payoff math **[UNVERIFIED — my own calculation]**
- A 1-month Nifty call 3% OTM at IV 12% is worth about 0.49% of notional; 5% OTM is about 0.17%. At IV 15% the figures are 0.78% and 0.36%.
- That is about 2–6% a year in gross premium, but in exchange Nifty's upside is capped at 3–5% a month. Monthly Nifty moves above +5% happen regularly in Indian bull phases, and each one is forfeited.

### Inferences
- **Operational blockers:**
  - Covering one Nifty call needs about 65 × Nifty in an index ETF (~₹16L), which is more than 2x the whole portfolio.
  - Stock calls need a full lot per stock (₹5L+ minimum **[UNVERIFIED]**), while the investor has 34 positions averaging ~₹20k.
  - A naked short call against a diversified book is not "covered". It is a short-vol position with unlimited upside risk and ₹2L+ margin.
- Assignment and physical settlement of stock F&O at expiry, plus STT on exercise, complicate stock covered calls further.
- Covered calls are short volatility. Their "income" is compensation for crash exposure plus forgone upside, not free yield.

### Gaps
- There is no India-specific long-run buy-write performance series from NSE Indices.
- I did not verify current stock lot sizes for the investor's holdings.

---

## 5. Short selling in India for retail

### Takeaway
Retail investors can short in cash only intraday; overnight naked cash shorts are not allowed. Overnight shorts need SLB borrowing, which is thin, operationally clunky and not offered by many discount brokers, or F&O futures/options with the same large lots. Shorting has unlimited loss, squeeze and margin-call risk. It is not a sensible loss-control tool for a ₹6.75L long-only book.

### Cited Findings
- SEBI's short-selling framework allows short selling in F&O-eligible securities. Retail must disclose by the end of the trading day. — [Jainam / SEBI framework summary](https://www.jainam.in/?p=36198); [NSE circular](https://archives.nseindia.com/content/circulars/cmtr9953.htm)
- SLB runs on exchange platforms through clearing corporations as central counterparties. Only eligible securities (mostly F&O stocks and index ETFs) can be lent or borrowed. — [Angel One](https://oga-prod.angelone.in/knowledge-center/share-market/securities-lending-and-borrowing); [PFRDA SLB note](https://www.pfrda.org.in/documents/33652/293853/SECURITIES+LENDING+AND+BORROWING+%28SLB%29.pdf)
- In 2021 Zerodha described SLB as back-office-complex. It said the market is thin because shorting via F&O is easier and cheaper. Forum users cite 18% GST on borrow fees and recalls around corporate actions. — [Zerodha Z-Connect](https://zerodha.com/z-connect/trending/shorting-and-indian-capital-markets); [TradingQnA](https://tradingqna.com/t/an-slb-platform-on-zerodha/124052) (forum, low authority)

### Inferences
- **For this investor:**
  - Shorting Nifty futures means about ₹16L of short exposure against a ₹6.75L long, a 2.5x over-hedge, with MTM margin calls.
  - Single-stock futures shorts are ₹5L+ per lot and give idiosyncratic, not portfolio, protection.
  - SLB is the only way to short small quantities overnight, but liquidity in most names and series is sparse.
- **Failure modes:**
  - unlimited loss
  - short squeezes, as in ban-period dynamics
  - forced closeouts and corporate actions
  - daily MTM liquidity drain
  - futures roll costs
- **Equivalent hedge without shorting:** sell some of the long book. The same exposure reduction is achieved with no margin and no squeeze risk, though it may trigger capital gains tax.

### Gaps
- I did not verify current SLB volumes or which major discount brokers offer SLB to retail in 2026.

---

## 6. Tax and transaction costs of F&O for individuals

### Takeaway
F&O gains and losses are non-speculative business income, taxed at slab rates. That makes hedge P&L tax-asymmetric against LTCG on the stocks, and it brings ITR-3 and bookkeeping. STT on options rose to 0.15% of premium on sale, and to 0.15% on exercise, from 1 Apr 2026. Futures STT rose to 0.05%.

### Cited Findings
- Budget 2026 (effective for trades on or after 1 Apr 2026):
  - futures STT rose from 0.02% to 0.05%
  - STT on sale of options rose from 0.10% to 0.15% of premium
  - STT on options exercise rose to 0.15% (prior rate given as 0.125% by most sources, 0.13% by ICICI)

  — [Outlook Money](https://www.outlookmoney.com/invest/stt-hike-from-april-1-2026-budget-what-it-means-for-futures-and-options-traders); [ICICI Direct](https://www.icicidirect.com/ilearn/futures-and-options/articles/stt-changes-in-budget-2026-what-f-o-traders-should-know); [5paisa](https://www.5paisa.com/news/stt-hike-on-fo-to-take-effect-from-april-1-amid-rising-options-activity)
- The government says it is not reviewing the STT structure, and F&O volumes did not fall after the hike. — [Basis Point Insight](https://www.basispointinsight.com/Story/govt-says-no-review-of-stt-structure--f-o-volumes-rise-despite-budget-tax-hike_9c6d75f3c414.html)
- **Tax treatment of F&O income and losses:**
  - F&O income is non-speculative business income under s.43(5), taxed at slab rates.
  - Losses can be set off in the same year against other heads except salary, and carried forward 8 years against business income only, provided the return is filed by the due date.
  - Turnover is the sum of absolute profit and loss per contract.
  - The s.44AB audit threshold is ₹1 cr, or ₹10 cr if 95%+ of transactions are digital.
  - A loss alone does not trigger audit, but there are 44AD presumptive-scheme interactions. Sources disagree on details.

  — [TaxGuru](https://taxguru.in/?p=1068347); [Jainam](https://www.jainam.in/blog/fo-income-tax-filing-guide/); [Kanakkupillai](https://www.kanakkupillai.com/learn/fo-trading-income-tax/)

### Inferences
- **Asymmetry:** a hedge that loses money in a bull year (the usual case) creates a business loss. It can offset same-year non-salary income, but carried forward it can offset only business income. Meanwhile the equity gain is taxed as LTCG at 12.5% above the ₹1.25L exemption. A winning hedge in a crash is taxed at slab rate, up to 30%+ **[UNVERIFIED rates/thresholds — the equity tax notes in this repo's `research_notes/Portfolio repo logic improvements/india_tax_costs.md` may cover these]**.
- **Per-trade costs:** brokerage (~₹20 flat per order at discount brokers **[UNVERIFIED]**), exchange charges, GST, stamp duty and SEBI fees. These are small against a ₹10k+ premium, but compound with quarterly rolls.
- The Income Tax Act 2025 may have taken effect on 1 Apr 2026 and renumbered sections. I did not verify this **[UNVERIFIED]**.

### Gaps
- I did not get exact current NSE transaction charges, or confirm any 44AD changes for FY27.

---

## 7. Data for honest backtesting of hedges

### Takeaway
End-of-day F&O bhavcopy (settlement and close prices, OI, by strike and expiry) is freely available from NSE archives, with community tooling. That is enough for a coarse EOD backtest of monthly or quarterly put rolls. It cannot capture bid-ask spreads, intraday fills or far-OTM illiquidity. Honest results therefore need explicit spread haircuts.

### Cited Findings
- The R package `nser` (CRAN v1.5.8, Jan 2026) downloads NSE F&O bhavcopy:
  - its `bhav` function covers data from 1 Jan 2020
  - its `bhav1` function covers the old format from 1 Jan 2016 to 5 Jul 2024, which implies a format change (UDiFF) in July 2024

  NSE archive requests can time out. — [nser fobhav vignette](https://cran.nics.utk.edu/cran/web/packages/nser/vignettes/fobhav.html); [nser manual](https://nandp1.r-universe.dev/nser/doc/manual.html)

### Inferences
- **What a backtest needs:**
  - daily Nifty option settle prices by strike and expiry (bhavcopy)
  - India VIX history (NSE)
  - Nifty TRI
  - historical lot sizes, which changed in Nov 2024 and Dec 2025, plus earlier revisions
  - STT and charge regimes by date (Apr 2026 change)
- **Honesty traps:**
  - Using settle or close prices instead of the ask for buys.
  - Ignoring that far-OTM quarterly strikes may have no trades on the chosen day.
  - Survivorship in strike availability.
  - Fractional-lot assumptions, which are fatal here because the real constraint is integer lots.
  - Look-ahead in roll rules.
- Broker APIs (Kite Connect, etc.) provide live chains, but historical option data is typically limited or paid **[UNVERIFIED]**.

### Gaps
- I did not find NSE's own UDiFF specification. I did not test a download.
- I found no free source of historical Nifty bid/ask spreads or intraday option data.

---

## Implications for the repo

1. **Do not build an options or shorting strategy engine.** For a ₹6.75L book the binding constraint is structural: the minimum index contract is ₹15–20L, and stock lots are ₹5L+ against ~₹20k average positions. Any backtest that assumes fractional lots would be fiction, and one that respects integer lots shows a 0% or ~250% hedge.
2. **Worth modelling (cheap, honest): a hedge-cost / exposure-equivalence calculator** in the risk layer (`risk_manager.py` / `analysis.py`). Inputs:
   - portfolio value and beta to Nifty, from the existing returns data
   - Nifty spot, current lot size (65), India VIX or manual IV, strike % OTM, tenor

   Outputs:
   - number of lots and the resulting hedge ratio (showing the over-hedge)
   - premium in ₹, as % of the portfolio and annualised
   - scenario P&L table (Nifty −30%, −20%, −10%, 0, +10%, +20%) for: (a) unhedged, (b) 1-lot put, (c) **equivalent-cost "hold X% less equity"**, (d) a cash or liquid-fund buffer

   The key output is (c) against (b). It operationalises Israelov's finding for this user. Use Black-Scholes with a skew bump. Label everything as an estimate.
3. **Preferred loss-control levers to model instead:** the equity/cash (or debt) allocation dial, position caps, and beta/concentration reduction. These are divisible, cost-transparent and tax-understood (LTCG/STCG), unlike F&O business income.
4. **Optional, later:** a small EOD bhavcopy-based study of the historical cost of rolling 3-month 5–10% OTM Nifty puts since 2016, with ask-side haircuts and integer lots. Its purpose would be to quantify Indian VRP and drag, not to trade. Its value is low relative to the effort.
5. **Guardrail:** if any options feature is added, it should say outright that SEBI data shows about 91% of individual F&O traders lose money (average ~₹1.17L in FY26), and the tool should never produce trade signals.
