# Multi-Asset Allocation with ETFs/Index Funds for an Indian Retail Investor (Loss Control with Long-Term Growth)

Research date: 2026-10-15. Researcher note on method: WebFetch could not resolve most domains in this session (gold.org, freefincal.com, businesstoday.in, qodeinvest.com, finvezto.com all failed DNS), so cited findings below come from search-result extracts of those pages and are **not full-text verified**. To make up for this, I computed primary statistics from the repo's own cached ETF price files (`/home/user/Portfolio/data/prices/adj/*.csv`, fetched 2026-10-15). They are labelled **[Repo-computed]**. Their methodology and caveats are given in place. Yahoo Finance was blocked by the egress proxy, so I could not pull longer histories (2008, 2013), S&P 500 or Nasdaq in INR, or debt indices.

---

## Q1. Historical returns, volatility, drawdowns and correlations in INR: crisis behaviour, and whether gold is a reliable crisis diversifier

### Takeaway
Gold in INR has been a **good but not reliable** equity-crisis diversifier for Indian investors. It clearly helped in 2008, in the Sep 2024 to Mar 2025 correction and in the 2026 equity drawdown. It did not help in 2013 (both fell) or in the first panic weeks of March 2020. Its weekly correlation with Nifty is about zero, but its own volatility is roughly 1.5 to 2 times Nifty's, and it can suffer large drawdowns of its own (about 26% in Jan to Mar 2026). Silver behaves as a high-beta version of gold (about 47% volatility, 45% drawdown in 2026) and adds little diversification beyond gold. The rupee is a large, under-appreciated driver: INR weakness in Indian equity crises (28% in 2008, 20% in 2013) lifts INR returns on gold and on US equity.

### Cited Findings
**Crisis episodes (Nifty vs rupee vs gold)**
- 2008 GFC (Apr 2008 to Feb 2009): rupee fell 28% and Nifty lost 43%. 2011–12: rupee fell 26%, Nifty 12%. 2013 taper tantrum (Jan to Aug 2013): rupee fell 20%, Nifty 8%. These are window returns, not verified peak-to-trough figures. — [BloombergQuint](https://www.bloombergquint.com/amp/charts/nifty-and-rupee-no-longer-correlated)
- 2013: the rupee went from 54 to 69 (about 28%) between Apr and Aug 2013. Nifty took nearly 3 years from its Nov 2010 high to pass its Jan 2008 high (about 6357). — [Chola Securities](https://www.cholasecurities.com/research/fundamental/why-this-time-its-different-from-2011-to-2013-period)
- 2008 in rupee terms: ₹100 in gold became about ₹126.94, while ₹100 in Nifty 50 fell to about ₹48.21 by end-2008. Other blogs give conflicting figures (gold +16% vs Nifty −55%; gold ETFs +69%), so treat these as **unverified**. — [Angel One](https://www.angelone.in/news/nifty-50-vs-gold); [SafeGold blog](https://www.safegold.com/blog/gold-price-market/gold-price-during-market-crash-india/); [BKS MyGold](https://www.bksmygold.com/blog/what-happens-to-gold-during-a-financial-crisis)
- 2013: gold and Nifty fell together, gold being in a global bear market. A blog also claims rupee depreciation added 15–20% to INR gold over 2013–2024 and that the 2013 import-duty hike lifted retail prices about 6% overnight (**unverified**, gold-seller blogs). — [SafeGold blog](https://www.safegold.com/blog/gold-price-market/gold-price-during-market-crash-india/); [BKS MyGold](https://www.bksmygold.com/blog/what-happens-to-gold-during-a-financial-crisis)
- March 2020: both fell in the initial panic before gold recovered. Another source claims gold +14% vs Nifty −38% over Jan to Apr 2020. The two accounts conflict, and the difference depends on the window chosen. — [BKS MyGold](https://www.bksmygold.com/blog/what-happens-to-gold-during-a-financial-crisis); [SafeGold blog](https://www.safegold.com/blog/gold-price-market/gold-price-during-market-crash-india/)
- Sep 2024 to Mar 2025: Nifty peaked at 26,277.35 on 27 Sep 2024 and was down about 16% by late Feb 2025, after 5 straight negative months. March 2025 then rose +6.3%. — [Business Standard](https://www.business-standard.com/markets/news/can-nifty-fall-20-from-peak-to-enter-bear-phase-chart-check-125022800318_1.html); [Stable Investor](https://stableinvestor.com/2025/03/5-consecutive-negative-months-nifty50.html/amp)
- FY25 (Apr 2024 to Mar 2025): gold +37.7% in USD to $3,070/oz, its best year since FY08, while equities disappointed. — [Business Standard](https://www.business-standard.com/markets/news/fy25-rear-view-equities-disappoint-gold-shines-as-standout-performer-125032801017_1.html)

**Correlation evidence**
- Academic results are mixed. One study (daily data, Nov 2008 to Jan 2020) finds bidirectional short-run causality between Nifty and gold, while another finds no short-term relationship. A 2024 DCC-GARCH study is cited as finding negative gold–Indian-equity correlation in 2008, 2020 and 2022. — [ResearchGate](https://www.researchgate.net/publication/348689181_DO_INTERNATIONAL_GOLD_PRICES_AND_NSE_NIFTY_50_MOVE_TOGETHER); [RJWave JAAFR paper](https://rjwave.org/jaafr/papers/JAAFR2606427.pdf)
- World Gold Council (an industry body, so not independent): gold's negative correlation to equities tends to *strengthen* in sell-offs, while it is often positively correlated in rising markets. Over 15 years to 2021, INR gold returned 11.7% p.a. vs equities at 11.6%, though it lagged over the 5 years to 2021. — [WGC: Strategic case for gold, India (2022)](https://www.gold.org/goldhub/gold-focus/2022/01/strategic-case-gold-india); [WGC: Why gold in 2026, India](https://www.gold.org/goldhub/research/why-gold-2026-anchor-indian-portfolios)

**[Repo-computed] statistics from cached ETF closes** (NIFTYBEES = Nifty 50 ETF; GOLDIETF = ICICI Pru Gold ETF; SILVERIETF = ICICI Pru Silver ETF. These are ETF prices, net of TER, and are only a proxy for TRI. Source files are `/home/user/Portfolio/data/prices/adj/{NIFTYBEES,GOLDIETF,SILVERIETF}.NS.csv`.)
- COVID: NIFTYBEES fell 36.3% peak-to-trough from 17 Jan 2020 to 23 Mar 2020.
- 2022: NIFTYBEES fell 15.7% (17 Jan to 17 Jun 2022). The calendar year ended +3.8% (price).
- 27 Sep 2024 to 4 Mar 2025: NIFTYBEES −15.2% while GOLDIETF **+14.2%**. Gold clearly diversified in this episode.
- 2025 calendar year: NIFTYBEES +11.2%, GOLDIETF +72.1%.
- 2026 YTD to 15 Oct: NIFTYBEES −11.5%, GOLDIETF +8.4%, SILVERIETF −8.3%.
- Gold's own drawdown: GOLDIETF −26.0% (29 Jan to 23 Mar 2026). SILVERIETF −45.4% over the same window. Silver is +118.9% since its data begins on 3 Feb 2025.
- Window Dec 2023 to Oct 2026: GOLDIETF +132.5% vs NIFTYBEES +13.2%. This is an extreme, regime-specific gold outperformance and should not be extrapolated.
- Correlations (Dec 2023 to Oct 2026): daily Nifty–gold 0.18 and Nifty–silver 0.25. Weekly Nifty–gold −0.00 and Nifty–silver 0.04. Gold–silver: 0.83 daily, 0.76 weekly. The rolling 52-week Nifty–gold correlation ranged from −0.27 to +0.15 (latest −0.03).
- Annualised daily volatility over the same window: Nifty 12.2%, gold 22.7%, silver 47.2%.
- Simple Nifty/gold mixes, monthly rebalanced, Dec 2023 to Oct 2026 (monthly data): 100/0 gave 3.1% CAGR with a −14.5% max drawdown. 80/20 gave 9.0% CAGR (−11.3%). 70/30 gave 12.0% CAGR (−11.2%). Gold both raised returns and cut drawdowns here, but only because gold rallied hard; this ~3-year window is not representative.

### Inferences
- Gold's crisis behaviour for INR investors comes from two hedges stacked together: global gold as a safe haven, and INR depreciation during Indian or EM stress. In 2013 the global gold leg failed (gold bear market), but the INR leg partly cushioned it. The model should therefore treat gold as a *probabilistic* diversifier with a near-zero long-run correlation, not as a guaranteed hedge.
- Gold's volatility is higher than Nifty's in recent data, so a 10–15% gold sleeve can itself drive a meaningful share of portfolio risk. Drawdown statistics need to be computed per asset as well as for the portfolio.
- Silver's 0.76–0.83 correlation with gold, together with roughly double gold's volatility, means it is not a separate diversifier. At most it is a small "high-beta precious metals" satellite.
- For the same reason, US equity in INR probably also diversifies Indian-specific crises (INR falls when Nifty falls), but I could not source or compute this; see Gaps.

### Gaps
- No verified long-history INR series (2008, 2013) for Nifty 50 TRI, Nifty 500 TRI, gold, silver, gilt and liquid indices, or S&P 500 / Nasdaq 100 in INR. The Yahoo proxy was blocked, NSE and WGC pages could not be fetched, and the repo cache starts in 2017 (Nifty), Dec 2023 (gold ETF) and Feb 2025 (silver ETF).
- No sourced figures for S&P 500 or Nasdaq in INR during 2008, 2013, 2020 or 2022. In 2022 the US fell (Nasdaq about −33% in USD) while INR fell about 10% against USD. This is from general knowledge and is **unverified here**.
- No sourced behaviour of gilt or liquid funds in the episodes. In the 2013 taper tantrum Indian G-sec yields spiked (RBI liquidity tightening in July 2013), so long gilts likely fell alongside equity. This is **unverified**.
- Repo data-quality issue found: `NIFTYBEES.NS.csv` in `data/prices/adj/` is **not split-adjusted** for the 1:10 split on 2019-12-19 (close 129.25 to 13.02). A naive max-drawdown reads −89.9%. Any full-history Nifty statistic computed from this file is wrong unless it is corrected.

---

## Q2. Evidence on simple allocations (60/30/10, permanent portfolio, all-weather/risk parity) in India, and the rebalancing benefit

### Takeaway
India-specific evidence consistently shows that adding debt and gold to equity **cuts drawdowns materially at a modest long-run return cost**. Over some windows (2008–2013 and 2024–2026, when gold surged) it even raised returns. WGC finds 7.5–15% gold improves risk-adjusted returns for a 70/30 INR portfolio. A permanent portfolio (25% each) roughly kept about 90% of Sensex CAGR over 2000–2019, but critics argue that 25% equity is too low to beat Indian inflation over long horizons. On rebalancing, the robust evidence (Vanguard) is that frequency matters little. Threshold or "check on a calendar, trade only on band breach" approaches save a few basis points and much turnover. The main benefit of rebalancing is **risk control (keeping the target allocation)**, not return enhancement.

### Cited Findings
- FundsIndia-based analysis reported by Business Today (13 Oct 2026), covering Jan 2000 to Sep 2026: adding debt and gold to equity shrinks drawdowns but lags in strong equity rallies. Its method was annual rebalancing when weights drift more than 5 percentage points from target. Specific CAGR and drawdown figures could not be fetched. — [Business Today, 2026-10-13](https://www.businesstoday.in/personal-finance/story/can-adding-gold-and-debt-to-equities-boost-long-term-returns-while-reducing-portfolio-drawdowns-561126-2026-10-13)
- A SEBI-referenced explainer claims 60/30/10 equity/debt/gold "historically matched pure-equity returns with significantly lower drawdowns". This is a secondary claim and is **unverified**. — [share.market](https://www.share.market/buzz/learn/importance-of-asset-allocation/)
- WGC 2026 India report: gold allocations of 7.5–15% improved risk-adjusted returns and reduced drawdowns for a hypothetical average INR portfolio over 19 years. The benchmark was 70% equity (60% BSE Sensex TRI, 10% MSCI World NTR) and 30% fixed income, with gold replacing equity and bonds pro-rata. The 2025 edition tested 7.5/10/12.5/15% with similar conclusions. The 2022 edition found 7–18% for an institutional portfolio over the decade to 2021. WGC is industry-funded. — [WGC 2026](https://www.gold.org/goldhub/research/why-gold-2026-anchor-indian-portfolios); [WGC 2025](https://www.gold.org/goldhub/research/why-gold-2025-building-indian-portfolio-resilience); [WGC 2022](https://www.gold.org/goldhub/gold-focus/2022/01/strategic-case-gold-india)
- WGC's global work puts the optimum at 2–10% for traditional portfolios and 5–8% within alternatives. — [WGC Portfolio Continuum](https://www.gold.org/goldhub/research/portfolio-continuum-rethinking-gold-alternatives-investing)
- Business Today (Jul 2025), "Would allocating 15–20% to gold reduce my portfolio risk": a gold allocation can improve risk-adjusted returns, but it requires attention to instrument choice, costs and disciplined rebalancing. — [Business Today](https://www.businesstoday.in/amp/personal-finance/investment/story/rethinking-all-equity-portfolios-a-strategic-gold-allocation-may-be-your-missing-shield-486757-2025-07-29)
- Permanent portfolio in India (Sensex / 10-yr G-sec / gold / cash, 2000–2019, quarterly rebalancing): 9.79% CAGR with about 8% standard deviation, vs Sensex 10.60% CAGR and 10-yr G-sec 8.09%. No max drawdown is reported. — [ClearTax](https://cleartax.in/glossary/permanent-portfolio)
- Freefincal's permanent portfolio study uses Sensex TRI (from Sep 1996), JM Liquid NAV, INR gold and the I-BEX long gilt index. The author argues that equity should exceed 25% to beat inflation, that gold has not been an effective inflation hedge in India, and that liquid debt is unsuitable for long-term growth. Numbers were not retrievable. — [Freefincal](https://freefincal.com/this-portfolio-works-in-all-market-conditions-will-you-invest/); [Freefincal (older version)](https://freefincal.com/the-permanent-portfolio-a-fascinating-low-volatility-option-for-the-long-term-indian-investor/)
- A US reference point: the permanent portfolio lost about 25% vs about 60% for a pure S&P 500 portfolio in the GFC. This is not India data. — [Monevator](https://monevator.com/the-permanent-portfolio/)
- Morningstar India (Apr 2020) analysed asset allocation and rebalancing through the COVID crash (equity −30% in Feb to Mar 2020) for a 70:30 portfolio. The result figures could not be retrieved. — [Morningstar India](https://www.morningstar.in/posts/57709/difference-asset-allocation-rebalancing-makes.aspx)
- Rebalancing mechanics (Value Research): in March 2020 you would have sold debt to buy equity, then later sold equity as it recovered. — [Value Research](https://www.valueresearchonline.com/stories/48893/strategies-for-an-overheated-market/)

**Rebalancing evidence (Vanguard, US/global)**
- "The Rebalancing Edge" (Dec 2024): a 200 bp threshold with a 175 bp destination beat calendar approaches by 5–21 bp a year for target-date investors. Against monthly rebalancing the gain was 15–22 bp in accumulation and 22–25 bp in decumulation. — [Vanguard Rebalancing Edge PDF](https://corporate.vanguard.com/content/dam/corp/research/pdf/the_rebalancing_edge_optimizing_target_date_fund_rebalancing_through_threshold_based_strategies.pdf); [Vanguard summary](https://corporate.vanguard.com/content/corporatesite/us/en/corp/articles/balancing-act-enhancing-target-date-fund-efficiency.html)
- Vanguard: smaller thresholds mean lower tracking error but higher transaction cost. Pure threshold rebalancing needs daily monitoring, which is impractical for DIY investors; checking on a calendar and trading only when a band is breached is the practical hybrid. — [Vanguard Canada](https://www.vanguard.ca/en/investor/insights/when_and_how_to_rebalance); [Vanguard "Rational rebalancing"](https://corporate.vanguard.com/content/dam/corp/research/pdf/rational_rebalancing_analytical_approach_to_multiasset_portfolio_rebalancing.pdf)
- Jaconetti, Kinniry and Zilbering (Vanguard, via a secondary summary): no meaningful risk or return difference between monthly and annual rebalancing; higher frequency just adds turnover. A claim that "5% threshold ≈ annual" is **unverified** against the primary source. — [eco3min summary](https://eco3min.fr/en/qa/rebalancing-discipline-returns/); [Vanguard tuning frequency](https://corpaemdisp.essp.c1.vanguard.com/content/corporatesite/us/en/corp/articles/tuning-frequency-for-rebalancing.html)
- Indian practitioner advice: direct new SIP money to the underweight asset to rebalance without triggering capital-gains tax. — [share.market](https://www.share.market/buzz/learn/how-to-rebalance-your-portfolio/)

### Inferences
- For an Indian retail investor, a 55–70% equity / 20–35% debt / 10–15% gold mix is where the evidence clusters. Gold above about 15–20% relies on continued INR depreciation or gold momentum. Equity below about 40% (permanent portfolio style) gives up too much long-run real return in India by Freefincal's argument.
- Risk parity or all-weather in India would push weight toward debt, because Indian debt volatility is low. Without leverage this mostly becomes a conservative-hybrid portfolio with a large slab-taxed debt sleeve, which is tax-inefficient after April 2023. That makes it a weak default for a taxable retail investor (inference).
- Rebalancing rules should be: check monthly or quarterly, trade only on band breach (for example ±5 pp absolute, or ±25% relative for small sleeves), and use cash flows first. This captures the risk-control benefit while minimising tax events. The Indian tax regime (realised gains taxed, ₹1.25 lakh equity LTCG exemption) magnifies the value of cash-flow-first rebalancing compared with US research that assumes tax-free accounts.

### Gaps
- No full-text India backtest numbers (CAGR, max drawdown) for 60/30/10, permanent portfolio or risk parity across 2008, 2013, 2020, 2022 and 2024–25. The FundsIndia, Freefincal and Morningstar pages could not be fetched.
- No India-specific study of threshold vs calendar rebalancing that includes Indian taxes and exit loads was found.

---

## Q3. Practical instruments in 2026: menu, tracking and premiums, costs, international access constraints

### Takeaway
Every sleeve can be filled by an ETF or index fund at low cost. Nifty 50 ETFs cost about 0.02–0.05%, and Bharat Bond, gilt and liquid ETFs are also cheap. The practical frictions are **premium/discount risk in ETFs where unit creation is constrained**: silver ETFs in Oct 2025 (5.7% premium, FoF lump-sum suspensions), and international ETFs (MON100, MAFANG etc.) under the RBI/SEBI industry overseas cap ($7 bn for MF overseas investment, $1 bn for overseas ETFs). The cap is still binding in 2026, with fresh-subscription pauses in Apr–May 2026. LRS ($250k per person per year) is the route outside the cap.

### Cited Findings
**Equity and cost**
- Nifty 50 / Sensex ETFs commonly charge 0.02–0.05% a year. SBI ETF Nifty 50 is cited at 0.04% and UTI Nifty 50 ETF at 0.05%. — [Equity Research India](https://www.equityresearchindia.com/post/lowest-expense-ratio-etfs-in-india-a-comparison-table); [5paisa](https://www.5paisa.com/index.php/blog/best-lowest-expense-ratio-mutual-funds-in-india); [Rupeezy](https://rupeezy.in/blog/best-mutual-funds-with-lowest-expense-ratio)
- Nippon India Gold BeES is listed at 0.79% TER. This looks high and is **unverified**; check the AMC factsheet. Gold ETF TERs are typically 0.3–0.8% (general knowledge, unverified). — [Finowings](https://www.finowings.com/mutual-fund/best-low-cost-high-return-etfs)

**Silver premiums and creation constraints**
- Oct 2025: Kotak (from 10 Oct), UTI, SBI (13 Oct), Axis and Tata (14 Oct) paused lump-sum subscriptions to silver ETF FoFs because of a physical silver shortage. Kotak said the domestic premium rose from 0.51% (4 Sep) to 5.7% (9 Oct 2025). SIPs and STPs mostly continued (Tata paused new SIP/STP registrations too), and redemptions were unaffected. — [Business Standard](https://www.business-standard.com/markets/mutual-fund/axis-tata-mf-suspend-investments-silver-etf-fof-supply-shortage-125101301245_1.html); [Business Standard explainer](https://www.business-standard.com/amp/finance/personal-finance/why-mfs-are-freezing-silver-etf-investments-and-what-it-means-for-you-125101400231_1.html); [Moneylife](https://moneylife.in/article/5-mutual-funds-freeze-silver-etf-subscriptions-as-prices-surge-and-physical-shortage-bites/78585.html); [Cafemutual](https://cafemutual.com/news/passives/36030-fund-houses-suspend-new-subscription-to-silver-fof)
- Silver ETFs were up as much as 86% YTD by 10 Oct 2025. — [Business Standard](https://www.business-standard.com/amp/markets/news/silver-etfs-down-up-to-4-after-strong-rally-still-up-as-much-as-86-percent-year-to-date-125101000612_1.html)

**International access**
- The industry cap is $7 bn for MF overseas investment, plus a separate $1 bn for overseas ETFs (reported at $300 mn per AMC for ETFs). AMCs at their cap must pause fresh subscriptions. Nippon India reportedly paused from 21 Apr 2026 and Axis from 6 May 2026. AMFI again asked for a review of the $7 bn limit in June 2026, including a proposal to link it to forex reserves. LRS allows $250k per person per year outside the MF cap. — [VMint Capital (2026 update)](https://vmintcapital.com/international-mutual-funds-india-investment-status-2026/); [Equity Research India](https://www.equityresearchindia.com/post/the-usd-7-billion-wall-why-indian-mutual-funds-keep-pausing-their-overseas-schemes); [Outlook Money](https://www.outlookmoney.com/invest/amfi-reiterates-need-to-relook-mutual-funds-7-billion-overseas-investment-limit); [Nippon India investor education](https://mf.nipponindiaim.com/investoreducation/international-mutual-funds-rbi-oversight)
- History: in Feb 2022 Motilal Oswal halted lump-sum and switch-ins to international schemes and suspended unit creation for its Nasdaq 100 ETF (MON100) and Nasdaq Q50 ETF. AMCs asked RBI for higher limits in Feb 2024. — [Business Standard 2022](https://www.business-standard.com/article/markets/foreign-funds-in-a-bind-over-sebi-s-curbs-on-overseas-investments-by-mfs-122022400056_1.html); [Business Standard 2024](https://www.business-standard.com/markets/mutual-fund/mutual-funds-knock-rbi-door-for-hike-in-foreign-investment-limits-124020701069_1.html)
- MON100 premium: a Zerodha broker nudge warned of "no market-making in this ETF due to RBI restrictions on overseas limit", with a premium of about 14% cited at the time. One analysis reports an average MON100 premium of about 3.7% over Jun 2023 to Jun 2026, with a typical day near 0.7%. These are the source's own calculations and are **unverified**. — [Zerodha TradingQnA](https://tradingqna.com/t/kite-nudge-for-mon100-etf-inav/130815); [Finvezto](https://finvezto.com/reports/global-etf-premium-to-nav); [1 Finance](https://1finance.co.in/blog/why-are-international-etfs-trading-at-a-premium-understand-the-concept-of-inav/)

### Inferences
- Category-level menu (no product recommendations):
  - **Equity core**: a Nifty 50 or Nifty 500 index ETF or index fund.
  - **Gold**: a gold ETF, or a gold FoF if SIP convenience matters. FoF stacks TER and has a 24-month LTCG threshold.
  - **Silver**: optional, small, and only via an ETF with an iNAV check.
  - **Debt, by job**: liquid ETFs or overnight/liquid funds for cash and dry powder; arbitrage funds for 3–24 month parking (equity taxation); target-maturity gilt, SDL or Bharat Bond-type ETFs/funds to lock duration to a goal date; gilt index funds for crisis duration exposure.
  - **International**: an FoF or ETF *only when open and near NAV*, otherwise LRS.
- The ETF premium to iNAV/NAV must be checked before any buy, especially for international and silver ETFs. A 3–14% premium can wipe out years of diversification benefit, and premiums tend to collapse when creation reopens.
- The repo already holds ICIGOL (a gold ETF) and equity ETFs, so a gold sleeve exists. The missing pieces are debt and international sleeves.

### Gaps
- Could not verify current (Oct 2026) TERs for specific gold, silver, liquid, Bharat Bond or gilt ETFs, LIQUIDBEES yields, or gold ETF tracking errors. AMC factsheets and NSE pages were unreachable.
- Could not confirm the current (Oct 2026) MON100 or MAFANG premium, or whether any international schemes have reopened.

---

## Q4. Tax as of FY2026-27 for each instrument (it shapes instrument choice)

### Takeaway
The working assumption is that Budget 2026 and the Income-tax Act 2025 (effective 1 Apr 2026) **carried over** the post-July-2024 capital-gains rates. This rests on secondary sources and should be verified against the Act. The treatment by instrument:
- **Equity ETFs/funds and arbitrage funds**: STCG 20% (≤12 months), LTCG 12.5% above ₹1.25 lakh a year.
- **Listed gold and silver ETFs**: LTCG 12.5% after 12 months, slab rate if shorter.
- **Gold/silver FoFs and international FoFs (unlisted)**: 12.5% after 24 months, slab rate if shorter.
- **Debt funds bought on or after 1 Apr 2023**: slab rate regardless of holding period.

This makes **arbitrage funds the tax-efficient short-term parking vehicle** and penalises large debt sleeves for high-slab investors.

### Cited Findings
- Listed gold and silver ETFs: holding over 12 months (for transfers from 23 Jul 2024) is long-term, taxed at 12.5% without indexation. Shorter holdings are taxed at slab. The ₹1.25 lakh exemption applies to equity only, not gold ETFs. — [Basunivesh](https://www.basunivesh.com/taxation-of-gold-and-silver-in-india-in-2026-explained-simply/); [Zerodha Fund House](https://www.zerodhafundhouse.com/blog/how-is-silver-taxed-in-india-etfs-fofs-and-physical-silver/); [IIFL](https://www.iifl.com/blogs/gold-loan/silver-etf-tax-india-2026-rate-holding-period-and-filing)
- Unlisted gold and silver FoFs and MFs have a 24-month long-term threshold. — [Basunivesh](https://www.basunivesh.com/taxation-of-gold-and-silver-in-india-in-2026-explained-simply/)
- Budget 2024 narrowed "specified mutual fund" (Sec 50AA). Gold ETFs, gold MFs and ETFs are not specified funds. Overseas FoFs and gold FoFs have a 24-month threshold with 12.5% LTCG; short-term gains are at slab. The sources conflict on the effective date (23 Jul 2024 per DSP and Mirae vs Apr 2025 per Stableinvestor). — [DSP note](https://www.dspim.com/latest-literature/dsp-note-budget-2024.pdf); [Mirae note](https://miraeassetmf.co.in/docs/default-source/default-document-library/tax-changes-post-union-budget-2024.pdf); [Stableinvestor](https://stableinvestor.com/2024/07/mutual-fund-taxation-rules-fy-2024-25.html/amp); [Freefincal](https://freefincal.com/budget-2024-big-change-in-mutual-fund-taxation-rules); [Business Today](https://www.businesstoday.in/amp/personal-finance/investment/story/capital-gains-tax-despite-tax-hike-equity-mfs-remain-attractive-experts-on-rejigging-investment-portfolio-439016-2024-07-27)
- Arbitrage funds are equity-oriented (at least 65% equity): STCG 20% and LTCG 12.5% after 12 months, with the ₹1.25 lakh exemption. An FoF needs at least 90% in Indian equity ETFs to get equity treatment. — [DSP note](https://www.dspim.com/latest-literature/dsp-note-budget-2024.pdf); [Stableinvestor](https://stableinvestor.com/2024/07/mutual-fund-taxation-rules-fy-2024-25.html/amp); [TaxClue](https://taxclue.in/blog/debt-mutual-fund-tax-post-2023-ita-2025)
- Debt MF units bought on or after 1 Apr 2023 are taxed at slab regardless of holding period. One guide wrongly lists 12.5% LTCG for debt, which conflicts with the others. — [Equentis](https://www.equentis.com/blog/tax-on-debt-mutual-funds/); [TaxClue](https://taxclue.in/blog/debt-mutual-fund-tax-post-2023-ita-2025)
- Budget 2026 reportedly made no change to MF capital-gains rates. SGB maturity exemption now applies only to bonds bought in the original RBI issue, from 1 Apr 2026. The Income-tax Act 2025 mainly restructures the law and keeps core capital-gains principles. These are secondary sources; verify. — [Regitom](https://www.regitom.com/what-does-budget-2026-mean-for-individual-taxpayers); [TaxGuru](https://taxguru.in/income-tax/capital-gains-income-tax-act-2025-tax-period-2026-27.html); [TaxGuru (key changes)](https://taxguru.in/income-tax/capital-gains-income-tax-act-2025-finance-act-2026-key-provisions-structural-income-tax-act-1961.html)

### Inferences
- **Instrument choice by tax:**
  - Gold: use a listed ETF rather than an FoF (12 vs 24 months to LTCG, lower stacked TER).
  - Short-horizon cash and dry powder: use arbitrage funds rather than liquid funds for high-slab investors. Liquid funds or ETFs suit low-slab investors or very short (<1 month) parking.
  - Duration debt: accept slab taxation, or for high-slab investors keep the debt sleeve smaller and lean on target-maturity funds held to maturity (for predictability, not tax benefit).
  - International: FoF LTCG needs 24 months; LRS direct holdings are also 24-month unlisted foreign shares under current rules (inference, unverified).
- Tax-aware rebalancing should (a) prefer new cash and redirected SIPs, (b) when selling, harvest equity gains within the ₹1.25 lakh annual exemption first, (c) avoid selling gold or equity lots under 12 months old (and FoF lots under 24 months), and (d) note that trimming debt costs the same tax whenever it is sold, so selling debt is often the cheapest rebalancing leg.

### Gaps
- I did not read the primary Income-tax Act 2025 or Finance Act 2026 text. Rates are from secondary sources and need verification.
- Tax treatment of the repo owner's specific holdings (for example, gold ETF lots bought before Apr 2023 under the old specified-fund regime) was not researched.

---

## Q5. What an allocation model can and cannot genuinely help with

### Takeaway
A model adds value through **discipline and arithmetic**: target weights matched to risk tolerance, drift monitoring, cash-flow-first and tax-aware rebalancing, premium/iNAV checks, and honest drawdown and correlation statistics. It cannot reliably predict which asset will win next. Gold's 2024–26 surge and the 2013 failure, the regime-dependent correlations, and Vanguard's finding that rebalancing frequency barely affects returns all argue against tactical prediction.

### Cited Findings
- The gold–equity correlation is regime-dependent: negative in sell-offs, positive in rallies (WGC). It is mixed academically. — [WGC 2022](https://www.gold.org/goldhub/gold-focus/2022/01/strategic-case-gold-india); [ResearchGate](https://www.researchgate.net/publication/348689181_DO_INTERNATIONAL_GOLD_PRICES_AND_NSE_NIFTY_50_MOVE_TOGETHER)
- Rebalancing frequency has little return effect; the benefit is staying at target risk, and threshold rules mainly reduce cost. — [Vanguard Rebalancing Edge](https://corporate.vanguard.com/content/dam/corp/research/pdf/the_rebalancing_edge_optimizing_target_date_fund_rebalancing_through_threshold_based_strategies.pdf); [Vanguard Canada](https://www.vanguard.ca/en/investor/insights/when_and_how_to_rebalance)
- Diversified mixes lag in strong equity rallies, which is the accepted cost of lower drawdowns. — [Business Today 2026-10-13](https://www.businesstoday.in/personal-finance/story/can-adding-gold-and-debt-to-equities-boost-long-term-returns-while-reducing-portfolio-drawdowns-561126-2026-10-13)

### Inferences
- **Can help with:**
  - Choosing a strategic allocation from a drawdown budget: "max tolerable peak-to-trough loss X%" maps to an equity weight using historical drawdowns (for example, equity drawdowns of about 36% in 2020 and 40–55% in 2008).
  - Drift alerts and band logic.
  - Routing new cash to the most underweight sleeve.
  - Tax-lot-aware sell selection.
  - Computing realised portfolio volatility, drawdown and correlation.
  - Flagging ETF premium versus iNAV.
  - Stress-testing the current mix against replayed historical episodes.
- **Cannot help with:**
  - Forecasting gold vs equity leadership.
  - Timing INR moves or the reopening of international subscription windows.
  - Guaranteeing that gold hedges the next crisis (2013 is a counterexample).

### Gaps
- No evidence was found on whether tactical tilts (momentum, valuation) on top of strategic allocation reliably add value net of Indian taxes. One practitioner source (Qode "Gold, Momentum, and All Weather") was found but not fetched. — [Qode](https://qodeinvest.com/quicktakes/gold-momentum-and-all-weather)

---

## Implications for the repo

*(Repo context: `/home/user/Portfolio` has `core_satellite.py`, `risk_manager.py` (equity-sizing focused), `tax_planner.py`, and `performance.py`. The current portfolio is about ₹4.8 lakh, almost all Indian equity plus one gold ETF holding (ICIGOL, about ₹31k, roughly 6%). It has no debt or international sleeve. Portfolio XIRR is −6.81% vs Nifty at +3.79% per README.md.)*

1. **New module `allocation.py` (or extend `core_satellite.py`)**
   - **Config** (in `config.py`): sleeve targets, for example `{"IN_EQUITY": 0.60, "DEBT": 0.25, "GOLD": 0.10, "INTL_EQUITY": 0.05, "SILVER": 0.0}`. Use per-sleeve bands as absolute ±pp with a relative floor, for example `max(5pp, 25% of target)`, so small sleeves like gold at 10% use ±2.5–5pp. Add a `check_frequency = "monthly"` setting so trades happen only on band breach.
   - **Sleeve classification**: map each symbol to a sleeve. Examples: ICIGOL / GOLDIETF go to GOLD, SILVERIETF to SILVER, NIFTYBEES / NIFTYIETF / HDFCSML250 / MIDCAPETF / ITBEES and stocks to IN_EQUITY, liquid / arbitrage / gilt / TMF funds to DEBT, and international FoF / ETF to INTL_EQUITY. Arbitrage funds belong in the DEBT/cash sleeve for *risk* purposes but in the equity bucket for *tax* purposes, so keep `risk_sleeve` and `tax_class` as separate fields.
   - **Drift report**: current vs target weight, distance to band edge, and the ₹ needed to restore each sleeve.
2. **Cash-flow-first rebalancing**
   - Allocate each new contribution or SIP greedily to the sleeve(s) furthest below target. Prescribe sales only if a band is still breached after expected inflows over N months.
   - When selling, rank lots in this order:
     1. Debt lots, since tax is the same regardless of holding period.
     2. Equity or gold lots with LTCG status. Equity first, to use the ₹1.25 lakh exemption.
     3. Avoid lots under 12 months old (24 months for FoFs).
   - Reuse lot logic from `tax_planner.py`.
3. **Drawdown and risk stats** (extend `performance.py`)
   - Per-sleeve and total-portfolio: running max drawdown, time to recover, annualised volatility, and rolling 52-week correlation matrix (Nifty, gold, silver, debt, international).
   - Historical stress replay of current weights over 2008, 2013, Feb–Mar 2020, 2022, Sep 2024–Mar 2025, and Jan–Mar 2026 (gold −26%, Nifty down).
   - Show the "drawdown budget → max equity weight" mapping.
4. **ETF premium guard**
   - Before any buy order for an ETF, compare LTP with the iNAV from the AMC or NSE.
   - Block or warn above a threshold (for example 1% for international or silver ETFs, 0.5% otherwise). The motivating cases are the silver premium of 5.7% in Oct 2025 and MON100 premiums of 3–14%.
5. **Data the module needs**
   - Long-history daily INR series:
     - Nifty 50 TRI and Nifty 500 TRI, from NSE Indices (Yahoo `^NSEI` is price-only; README already notes the TRI gap).
     - Gold INR (MCX/IBJA or LBMA × USDINR).
     - Silver INR.
     - CRISIL / NSE G-sec or gilt index, and a liquid fund NAV (from AMFI daily NAV text files).
     - S&P 500 TR and Nasdaq 100 TR in USD, plus USDINR from RBI/FBIL reference rates.
   - Also: AMFI scheme NAVs for MFs/FoFs, ETF iNAVs, TERs (from factsheets), and a tax-class mapping per instrument.
   - **Fix first**: `data/prices/adj/NIFTYBEES.NS.csv` is not adjusted for the 1:10 split on 2019-12-19. Add split-adjustment, or a validation step that flags daily moves beyond ±40% in index ETFs. Any full-history Nifty stats, backtest or benchmark XIRR using this file may be wrong. Check `backtest_engine.py` and `performance.py` usage.
6. **Scope discipline**: the module should output target, drift and rebalancing actions plus risk statistics only. Tactical gold or equity "views" should be excluded or clearly labelled as not evidence-backed (see Q5).
