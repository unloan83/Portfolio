# Implementing a Systematic Excess-Return Strategy for a ~₹6.75 lakh Indian Retail Portfolio: Factor Funds vs DIY Selection, Universe, Construction, Rebalancing

Research constraints: this session's WebFetch and curl were blocked (DNS/proxy 403 on niftyindices.com, zerodha.com and the AMC sites), so every finding below comes from **web-search result summaries**, not from reading the full documents. Numbers marked **[UNVERIFIED]** should be checked against the primary PDF before code relies on them. Today's date is 2026-10-15.

Repo context (checked locally): `/home/user/Portfolio/core_satellite.py` already classifies `ICINIF`, `HDF250` and `MIR150` as "Core" index ETFs and everything else as "Satellite". The engine has no ranking or selection layer, and its universe is limited to the holdings already owned.

---

## Q1. Indian factor ETFs and index funds in 2026: costs, tracking, liquidity, AUM, realised returns

### Takeaway
Cheap, liquid index funds in **Direct** plans exist for the main Indian smart-beta indices. Base TER runs about 0.2–0.4% for Nifty200 Momentum 30 and about 0.3–0.7% for Alpha Low-Vol and multi-factor funds, with tracking error around 0.1–0.5%. The biggest hidden cost is **rebalance-day market impact inside the fund**. Momentum indices turn over about 60–70% one-way every six months, and the flow is large enough that the stocks are front-run. Realised momentum returns have been weak over the last ~5 years: TRI 5Y CAGR was about 9% as of Sep 2026, against a 10Y CAGR of about 16%. The long-run premium is real but very lumpy.

### Cited Findings
**Costs and tracking (Nifty200 Momentum 30 products)**
- Kotak Nifty 200 Momentum 30 Index Fund, Aug 2026 factsheet: TER 0.68% Regular and **0.20% Direct**, tracking error 0.20%, AUM about ₹601 cr. TE was 0.13% in the Apr/May 2026 factsheets and 0.20% in Jun/Aug. The TER is a "base" figure that excludes brokerage and transaction costs. — [Kotak factsheet Aug 2026](https://www.kotakmf.com/factsheet/August_2026/kotak/NIFTY-200-MOMENTUM-30-INDEX-FUND.html); [Apr 2026](https://www.kotakmf.com/factsheet/April_2026/kotak/NIFTY-200-MOMENTUM-30-INDEX-FUND.html)
- Kotak Nifty200 Momentum 30 ETF, Jun 2026: TER 0.26%, TE 0.32%. — [Kotak ETF factsheet Jun 2026](https://www.kotakmf.com/factsheet/June_2026/kotak/Download_pdf/KOTAK%20NIFTY200%20MOMENTUM%2030%20ETF.pdf)
- Baroda BNP Paribas Nifty200 Momentum 30 Index Fund, Jun 2026: base TER 0.90% Regular and 0.37% Direct, TE 0.48. — [Baroda BNP factsheet Jun 2026](https://www.barodabnpparibasmf.in/efactsheet/Jun2026/Innerpages/Nifty200-Momentum-30-Index-Fund.html)
- Motilal Oswal Nifty 200 Momentum 30 ETF (MOMOMENTUM): one snapshot shows TER 0.33% and a 0.2% premium to NAV (undated). Another source shows TER 1.28% and AUM about ₹154 cr (Aug 2026), which is likely a data error. Volume on 12 Jun 2026 was only about 1,506 units, i.e. thin. **[UNVERIFIED / conflicting]** — [TradingView](https://in.tradingview.com/symbols/BSE-MOMOMENTUM/analysis); [5paisa](https://www.5paisa.com/gujarati/stocks/etf/motilal-oswal-nifty-200-momentum-30-etf)
- ICICI Pru Nifty 200 Momentum 30 ETF showed a 0.09% premium/discount on one snapshot. **[UNVERIFIED, undated]** — [TradingView MOM30IETF](https://in.tradingview.com/symbols/BSE-MOM30IETF/)

**Other factor products**
- Edelweiss Nifty500 Multicap Momentum Quality 50 Index Fund, Direct: TER about 0.70–0.84% (Oct 2026), AUM about ₹600–626 cr. Regular plan about 1.5%. Edelweiss's ETF version is listed at TER 0.94% and AUM about ₹32 cr. Aggregator figures conflict. **[UNVERIFIED]** — [Dezerv](https://www.dezerv.in/mutual-funds/edelweiss-nifty500-multicap-momentum-quality-50-index-fund-direct-growth-inf754k01tn5/); [INDmoney](https://www.indmoney.com/mutual-funds/edelweiss-nifty500-multicap-momentum-quality-50-index-fund-direct-growth); [Value Research](https://www.valueresearchonline.com/funds/44648/edelweiss-nifty500-multicap-momentum-quality-50-index-fund-direct-plan/)
- Nifty Alpha Low-Volatility 30: Edelweiss direct fund TER about 0.7% with fund size about ₹92 cr. Nippon India direct base TER about 0.30%. ICICI Pru ETF TER about 0.42%. **[UNVERIFIED, aggregator]** — same search set ([Value Research](https://www.valueresearchonline.com/funds/44648/edelweiss-nifty500-multicap-momentum-quality-50-index-fund-direct-plan/), [TradingView ALPL30IETF](https://www.tradingview.com/symbols/BSE-ALPL30IETF/analysis))
- Nifty200 Quality 30 fund: the searches returned no TER or AUM data. See Gaps.

**Rebalance mechanics and impact (key execution-realism finding)**
- Nifty200 Momentum 30 rebalances semi-annually (June and December). The Normalised Momentum Score uses 6M and 12M price return adjusted for volatility. Weights are score × free-float market cap, capped at the lower of 5% or 5× the stock's free-float-mcap weight. — [Business Standard, Dec 2025](https://www.business-standard.com/markets/news/nifty200-momentum30-a-flip-of-index-switch-jolts-16k-cr-across-the-grid-125121400388_1.html)
- The **Dec 2025** rebalance replaced 19 of 30 constituents, about ₹16,130 cr round-trip. Flows in 27 stocks were estimated to exceed one day's ADV. The **Jun 2025** rebalance changed about 20 stocks, with estimated **one-way turnover of 68.4%** (Periscope Analytics). — [Business Standard Dec 2025](https://www.business-standard.com/markets/news/nifty200-momentum30-a-flip-of-index-switch-jolts-16k-cr-across-the-grid-125121400388_1.html); [Business Standard Jun 2025](https://www.business-standard.com/amp/markets/stock-market-news/nifty200-momentum-30-index-to-see-20-stock-changes-on-june-27-125062600872_1.html)
- A freefincal piece argues that Indian momentum returns are tied to a liquidity premium and that alpha fades as AUM forces funds into heavily traded names. This is an opinion/backtest piece. — [freefincal](https://freefincal.com/?p=345828)
- Nifty Alpha Low-Vol 30 is a multi-factor index built on a Jensen's-alpha z-score (1Y, vs Nifty 50) plus low volatility, reconstituted semi-annually in Jun/Dec. — [Edelweiss presentation Apr 2024](https://www.edelweissmf.com/Files/downloads/Product%20Collateral/Presentation/2024/Apr/published/Edelweiss%20Nifty%20Alpha%20Low%20Vol%2030%20Index%20Fund%20Presentation_25042024_104449_AM.pdf)

**Realised returns**
- Nifty200 Momentum 30 TRI as of 30 Sep 2026: **5Y CAGR 9.28%, 10Y CAGR 15.98%**. No Nifty 200 TRI comparison was shown. — [Bandhan fund page](https://bandhanmutual.com/mutual-funds/index-funds-and-etfs/bandhan-nifty200-momentum-30-index-fund/regular)
- Older comparison (Jan 2024): Momentum 30 TRI 5Y CAGR 23.2% vs Nifty 200 TRI 17.4%. — [HDFC NFO presentation](https://files.hdfcfund.com/s3fs-public/Others/2024-02/NFO%20Presentation%20-HDFC%20NIFTY200%20Momentum%2030%20Index%20Fund.pdf)
- ABSL: Nifty200 Momentum 30 TRI earned about 7% p.a. excess return over Nifty 200 TRI on a 10Y rolling basis (2006–Jun 2022, largely back-tested). — [ABSL NFO doc](https://mutualfund.adityabirlacapital.com/-/media/BSL/Files/Documents/NFO_ABSL-Nifty-200-Momentum-30-ETF)
- Nifty 50 (NSE tracker, 15 Oct 2026, price): 1Y −9.19%, 3Y 16.44%, 5Y 25.40%. These look like cumulative rather than annualised figures. **[UNVERIFIED: annualised vs absolute unclear]** — [NSE tracker](https://www.nseindia.com/index-tracker/NIFTY%2050)
- Factsheet readings (column labels garbled, **[UNVERIFIED]** whether these are 1Y/3Y): Nifty500 Momentum 50 13.89 / 20.66 (Aug 2026); Nifty Quality Low-Vol 30 6.15 / 14.05, beta 0.69; Nifty500 Multifactor MQVLv50 13.70 / 17.51 (Jul 2026). — [Nifty500 Momentum 50](https://www.niftyindices.com/Factsheet/FactsheetNifty500Momentum50.pdf); [Quality LV 30](https://www.niftyindices.com/Factsheet/Factsheet_NIFTY_Quality_Low-Volatility_30.pdf); [MQVLv50](https://www.niftyindices.com/Factsheet/Factsheet_Nifty500MultifactorMQVLv50.pdf)
- Edelweiss long-run factor study (Apr 2005–May 2026, NSE data): Momentum CAGR 21.7% at 22.4% volatility; Low-Vol 17.4% at 16.1%; Quality and Value about 17%, with Value the most volatile at 25.6%. — [Edelweiss MQ50 presentation May 2026](https://www.edelweissmf.com/Files/downloads/Product%20Collateral/Presentation/2026/May/published/Edelweiss%20Nifty500%20Multicap%20Momentum%20Quality%2050%20Presentation%20May%202026_10062026_054533_PM.pdf)

### Inferences
- The 5Y momentum TRI (9.3%) against the 10Y (16.0%) shows the premium arrives in bursts. Momentum lagged badly through the 2024–25 correction. A strategy chosen on trailing 3–5Y returns will look poor right now, and that is precisely when abandoning it is most tempting (see Q5).
- For momentum, Direct index funds beat the ETFs on practical grounds. Fund TER is about 0.2–0.4% and units buy at NAV, with no bid-ask spread and no iNAV premium. The ETFs are thin, with low daily volume and premiums up to about 0.2%. ETFs only win on STT (see Q2) and intraday control, and that is irrelevant at this size.
- The index funds' **rebalance-day impact** is a real, unreported cost. Front-running of 60–70% semi-annual turnover where flows exceed ADV in 27 stocks falls on fund holders and shows up as tracking difference against the TRI, not in the TER. A DIY replicator trading ₹20–30k tickets **off** the official rebalance dates avoids it entirely. This is the main structural edge DIY has.

### Gaps
- Official niftyindices.com factsheet numbers (3/5/10Y TRI vs Nifty 50/500 TRI) could not be read because fetching was blocked. Nifty200 Quality 30 and Nifty Midcap150 Momentum 50 realised returns and fund TER/AUM were not found.
- Tracking *difference* (fund return minus TRI) for any momentum fund was not found; only tracking *error* was.
- No iNAV premium/discount time series was found.

---

## Q2. DIY replication: universe, names, weighting, rebalance frequency, buffers, costs, minimum sizes

### Takeaway
At ₹5–10 lakh, DIY is **feasible on cost**. Zero brokerage plus about 0.22% statutory round trip plus about ₹16 DP per sell makes semi-annual or quarterly rebalancing with a buffer cost roughly 0.3–0.6% a year. DIY is **expensive on tax**: realising short-term gains at 20% inside a high-turnover momentum book is a bigger drag than all trading costs, while a mutual fund rebalances internally with no tax to the unitholder. The design levers that matter are a Nifty 200 or LargeMidcap 250 universe, 20–25 names, near-equal or inverse-vol weights, semi-annual or quarterly rebalancing, and a wide buy/hold buffer.

### Cited Findings
**Transaction costs (equity delivery, NSE)**
- Zerodha: ₹0 brokerage on delivery; STT 0.1% on buy **and** sell for delivery. — [Zerodha charges](https://zerodha.com/charges)
- Stamp duty 0.015% on buys only; NSE transaction charge about 0.00297–0.00322% (sources/versions disagree); SEBI fee ₹10/crore; GST 18% on transaction and SEBI charges. — [Rupeezy](https://support.rupeezy.in/support/solutions/articles/2100044912-what-are-nse-transaction-and-other-charges-as-per-exchange-and-government); [Upstox](https://upstox.com/help-center/t-257195/); [Zerodha](https://www.zerodha.com/charges)
- DP charge about ₹13.5 + GST ≈ **₹15.93 per scrip per day on sells**. **[UNVERIFIED from Zerodha directly]** — [stockcalc.in](https://stockcalc.in/calculator/brokerage/zerodha); [sum.money](https://sum.money/in/brokerage-calculator/)
- Worked arithmetic from those rates: buying ₹1 lakh costs about ₹118.6 and selling about ₹103.6 (excluding DP), so **round trip ≈ 0.222%**. — derived from the [search-reported rates](https://zerodha.com/charges)
- Equity ETF units carry **no STT on purchase and 0.001% on sale**. This appears unchanged by Budget 2026, which raised STT on futures. **[Budget text not verified]** — [Angel One](https://www.angelone.in/knowledge-center/income-tax/what-is-securities-transaction-tax-stt); [Business Standard 2013](https://www.business-standard.com/amp/article/budget/govt-to-reduce-securities-transaction-tax-on-certain-segments-113022800305_1.html)

**Turnover and buffers (academic)**
- Novy-Marx & Velikov (RFS 2016): the **buy/hold spread** (enter on a strict threshold, keep holding until a looser threshold is breached) is the most effective cost-mitigation technique. Most anomalies with <50% monthly turnover keep significant net spreads after cost mitigation; few higher-turnover ones do. Capacity is inversely related to turnover. — [NBER w20721](https://www.nber.org/papers/w20721.pdf); [IDEAS/RFS](https://ideas.repec.org/a/oup/rfinst/v29y2016i1p104-147..html)
- MSCI Momentum indexes rebalance quarterly with a buffer set at 50% of the fixed security count. — [MSCI Momentum methodology Jul 2025](https://www.msci.com/indexes/documents/methodology/2_MSCI_Momentum_Indexes_Methodology_20250725.pdf)
- Nifty momentum indices apply a buffer on normalised score ranks to cut turnover; the exact thresholds were not found in an official source. Nifty500 Momentum 50 rebalances semi-annually. — [Nifty500 Momentum 50 factsheet](https://www.niftyindices.com/Factsheet/FactsheetNifty500Momentum50.pdf); [Axis Max Life blog](https://www.axismaxlife.com/blog/investments/nifty-500-momentum-50-index)
- Even with buffers, Nifty200 Momentum 30 one-way turnover was about 68% in the Jun 2025 reconstitution. — [Business Standard](https://www.business-standard.com/amp/markets/stock-market-news/nifty200-momentum-30-index-to-see-20-stock-changes-on-june-27-125062600872_1.html)

### Inferences (cost model for the repo — my arithmetic, not sourced)
- **Per-name size:** ₹6.75L / 20 names ≈ ₹34k per name; / 25 ≈ ₹27k; / 30 ≈ ₹22.5k. The DP fee of ₹15.93 is about 0.05–0.07% of a ₹22–34k sell, which is negligible. Impact is negligible for Nifty 200 names at this size. The bid-ask half-spread is about 0.02–0.10% for large/mid caps (**assumption**). Set a **minimum trade size of about ₹5,000** and **minimum position about 2.5%** so DP and rounding friction stay below about 0.3%.
- **Annual trading-cost drag** = one-way turnover × (0.222% + about 0.1% spread) + DP:
  - Semi-annual with buffer, about 50% one-way per rebalance → about 1.0×/yr → about **0.35–0.45%/yr**.
  - Quarterly with buffer, about 30–35% per rebalance → about 1.2–1.4×/yr → about **0.45–0.55%/yr**.
  - Monthly without buffer, about 25–30% per rebalance → about 3×/yr → about **1.0–1.2%/yr**. Too high relative to the gain from a fresher signal.
- **Tax drag dominates.** Most momentum exits happen within 12 months, so gains on sold winners are taxed at STCG 20%. If a quarter of the book is realised each year at an average 20% gain, that is roughly 1% of NAV a year in tax (illustrative). A mutual fund defers all of this until the investor redeems, and then the gain is LTCG at 12.5% above ₹1.25L if held >12 months. **For a taxable retail account, this is the single strongest argument for using a fund for the momentum sleeve.**
- **Universe:** Nifty 200 or Nifty LargeMidcap 250 (top 250 by market cap) keeps liquidity high and survivorship manageable with point-in-time membership. Nifty 500 adds small caps, which have wider spreads, more crash risk and are where the "liquidity premium" critique bites. Use a liquidity screen: median 3M daily traded value > ₹10 cr (assumption).
- **Number of names:** 20–25. Fewer than 15 gives too much idiosyncratic risk, and more than 30 dilutes the factor exposure and pushes positions below about ₹20k.
- **Weighting:** equal weight or inverse-vol, capped at 6–8% per name and about 25–30% per sector. Score-tilted weighting adds turnover for little gain at this size (inference). The indices' score × mcap weighting concentrates in mega caps.
- **Buffer rule (concrete):** for a target N=20, buy only names ranked ≤20 and keep an existing name until it falls below rank 40 (2N, as Nifty/MSCI-style buffering does) or its 12M return turns negative.

### Gaps
- Official Nifty buffer thresholds for the momentum indices were not confirmed.
- No India-specific estimate of retail bid-ask spreads by market-cap bucket was found.
- No published realised-turnover figure for a DIY Indian momentum book was found.

---

## Q3. Core-satellite sizing, combining momentum with quality/low-vol, factor timing

### Takeaway
Keep a broad market-cap core and a multi-factor satellite. Pair momentum with low-vol or quality: the two have historically had different drawdown profiles, and momentum's crash risk is the main way it fails. Do not time factors. The best-known evidence says value-spread timing adds little after costs and that a strategic allocation captures the same diversification more cheaply.

### Cited Findings
- Momentum has deeper and longer drawdowns than the parent index. Motilal Oswal's own material (data to Jun 2025) notes drawdowns lasting longer than Nifty 200 TRI's. NSE's Apr 2026 whitepaper concedes that momentum exposure "can lead to sharper drawdowns" in down markets. — [Motilal Oswal presentation Jun 2025](https://www.motilaloswalmf.com/CMS/assets/uploads/Documents/aa841-presentation-motilal-oswal-nifty-200-momentum-30-etf-index-fund-rd-june-2025.pdf); [NSE momentum whitepaper Apr 2026](https://www.niftyindices.com/docs/default-source/indices/nifty200-momentum-30/momentum-strategy-whitepaper_2026.pdf)
- A third-party backtest (Dec 2006–Jun 2025, a broader momentum universe, not the index) shows about a −70% drawdown in 2008 and a 65-month recovery, against about −44% for a generic low-vol strategy. **[third-party backtest]** — [BacktestIndia](https://backtestindia.com/blog/momentum-investing-india-backtest)
- In the 2024–25 correction, momentum fell about −27% over 6 months while Nifty 50 fell about −12% and Nifty 200 about −15% (Substack; secondary). — [Curious Investing Insights](https://curiousinvestinginsights.substack.com/p/momentum-or-mayhem-unpacking-the)
- Edelweiss factsheet (Apr 2024, window unstated): max drawdown −30.4% for Nifty Alpha Low-Vol 30 vs −33.5% for Nifty200 Momentum 30. — [Edelweiss ALV30 presentation](https://www.edelweissmf.com/Files/downloads/Product%20Collateral/Presentation/2024/Apr/published/Edelweiss%20Nifty%20Alpha%20Low%20Vol%2030%20Index%20Fund%20Presentation_25042024_104449_AM.pdf)
- Value Research: momentum and alpha indices beat their parents over time but "suffer deeper cuts in bearish markets." — [Value Research](https://www.valueresearchonline.com/stories/222021/momentum-alpha-funds-analysis/)
- Asness, Chandra, Ilmanen & Israel (JPM 2017), "Contrarian Factor Timing is Deceptively Difficult": no robust evidence that value-spread timing delivers meaningful outperformance. Timing helped single-factor momentum, but a strategic value allocation gave the same benefit more cheaply, and the gain shrank as more factors were added, even before costs. Arnott et al. argue timing is possible but hard in practice. — [AQR](https://www.Aqr.Com/Insights/Research/Journal-Article/Contrarian-Factor-Timing-is-Deceptively-Difficult-Supplement); [Validea](https://blog.validea.com/asness-versus-arnott-the-factor-timing-debate-continues/)
- Products that already combine the factors: Nifty500 Multicap Momentum Quality 50; Nifty500 Multifactor MQVLv50 (momentum/quality/value/low-vol); Nifty Quality Low-Vol 30 (beta about 0.69). — [MQVLv50 factsheet](https://www.niftyindices.com/Factsheet/Factsheet_Nifty500MultifactorMQVLv50.pdf); [QLV30 factsheet](https://www.niftyindices.com/Factsheet/Factsheet_NIFTY_Quality_Low-Volatility_30.pdf)

### Inferences
- Suggested split: **50–60% core** (Nifty 50 / LargeMidcap 250 index), **40–50% factor satellite**, with the satellite split roughly 50/50 between momentum and a defensive factor (low-vol/quality or Alpha-LowVol). Momentum alone at 100% of satellite risks underperforming for several years (5Y CAGR 9.3% as of Sep 2026), and that is the main way a retail investor ends up quitting.
- A composite score inside a DIY sleeve (e.g. 50% momentum rank + 50% quality/low-vol rank) gives most of the diversification at lower turnover than pure momentum, because quality ranks are sticky.
- The only "timing" to allow is mechanical risk control that is part of the rule set (e.g. vol-scaling the momentum sleeve, or the absolute-momentum filter in Q2). Do not make discretionary switches based on recent factor returns.

### Gaps
- No primary data were found on Indian momentum/low-vol return correlation or blended-portfolio drawdown statistics.
- No evidence was found specific to Indian volatility-managed momentum.

---

## Q4. Transitioning from the current 34 holdings

### Takeaway
No source covers this directly; it is design reasoning built on the costs in Q2 and the tax rates given in the brief. Transition gradually and tax-aware. Route new cash and exits with losses or long-term gains first, and leave short-term winners until they cross 12 months.

### Cited Findings
- STT 0.1% on each side of delivery trades plus ₹15.93 DP per sell scrip means exiting 34 positions costs about 0.1% of the sold value plus about ₹540 in DP. — derived from [Zerodha charges](https://zerodha.com/charges) and [stockcalc.in](https://stockcalc.in/calculator/brokerage/zerodha)
- Tax rates per the brief: STCG 20% (<12 months); LTCG 12.5% above ₹1.25L per year (no further research).

### Inferences (proposed procedure)
1. Score all 34 holdings with the same ranking model used on the universe. Tag each one: *in target* (keep), *in buffer zone* (keep, no top-ups), or *out of buffer* (exit candidate).
2. Order the exits as follows: (a) positions at a loss, sold first to harvest losses that offset STCG/LTCG; (b) LTCG positions while the realised gain stays inside the ₹1.25L annual exemption; (c) STCG winners only once they are past 12 months, unless they breach a hard risk rule.
3. Route all new cash and sale proceeds to underweight target names or the factor funds first, so less selling is needed.
4. Plan to converge over **2–4 rebalance cycles (6–12 months)**. Cap forced selling at about 25–30% of NAV per cycle.
5. Keep the existing index ETFs (`ICINIF`, `HDF250`, `MIR150`) as the core. Treat thematic and commodity ETFs as outside the factor sleeve and size them by policy.

### Gaps
- No Indian retail-specific literature on tax-aware transition was found.

---

## Q5. Behavioural and practical: discipline, monitoring cadence, when to abandon

### Takeaway
The factor premium needs years of tolerance. Momentum had a strong 10Y CAGR but a weak 5Y, and multi-year drawdowns longer than the market's. Pre-commit in writing to a calendar, rules and abandonment criteria, and judge the strategy against a factor benchmark rather than recent Nifty returns.

### Cited Findings
- Momentum recovery can take years. The third-party backtest shows a 65-month recovery after 2008, and the index has had longer drawdowns than Nifty 200 TRI. — [BacktestIndia](https://backtestindia.com/blog/momentum-investing-india-backtest); [Motilal Oswal](https://www.motilaloswalmf.com/CMS/assets/uploads/Documents/aa841-presentation-motilal-oswal-nifty-200-momentum-30-etf-index-fund-rd-june-2025.pdf)
- Business Standard reports AMC framing of momentum as "high risk, high reward" with a **7-year horizon**; Kotak's ETF factsheet states 5 years+. — [Business Standard 2024](https://www.business-standard.com/markets/mutual-fund/enter-momentum-funds-high-risk-high-reward-strategy-with-7-year-horizon-124091701111_1.html); [Kotak ETF factsheet](https://www.kotakmf.com/factsheet/June_2026/kotak/Download_pdf/KOTAK%20NIFTY200%20MOMENTUM%2030%20ETF.pdf)
- Freefincal (2022): "no strategy will work at all times"; momentum had the widest 5Y risk spreads among the factors. — [freefincal](https://freefincal.com/tata-nifty-midcap-150-momentum-50-index-fund-review/)

### Inferences
- **Monitoring cadence:** check the risk rules monthly (existing engine), rebalance on the calendar only (quarterly or semi-annual), and review attribution annually.
- **Benchmark:** compare the DIY sleeve with the Nifty200 Momentum 30 TRI (or a blend for a multi-factor sleeve), net of costs and tax. If DIY trails the index fund by more than about 1.5%/yr over 3 years, switch the sleeve to the fund.
- **Abandon only for structural reasons**, not underperformance under about 5 years. Valid reasons: implementation error, costs or tax running above model, or a change in the rules or index methodology. Do not abandon over a 1–3Y drawdown.

### Gaps
- No Indian investor behaviour-gap data (fund return vs investor return) were found for factor funds.

---

## Recommended implementation for the repo

This combines the sources above with inference. All parameters are design choices to backtest, not sourced facts.

**Architecture: hybrid core + fund + small DIY sleeve**

| Sleeve | Weight | Vehicle | Why |
|---|---|---|---|
| Core | 50% | Existing Nifty 50 / LargeMidcap 250 / Midcap 150 ETFs (`ICINIF`, `HDF250`, `MIR150`) | Low cost; beta anchor |
| Factor fund | 25% | Direct-plan index fund: Nifty200 Momentum 30 (TER about 0.20–0.37%) + Alpha Low-Vol 30 or Quality LV 30, split about 60/40 | Tax deferral on internal turnover; no DIY tax drag |
| DIY factor sleeve | 25% (about ₹1.7L) | 12–15 stocks built by the engine | Avoids rebalance-day front-running; the place to add the ranking engine. Kill switch if it lags the fund benchmark |

If the user wants the engine to do the selection (as the request implies), the **DIY sleeve** spec is:

- **Universe:** Nifty 200 or Nifty LargeMidcap 250 using **point-in-time** membership. Liquidity filter: median 63-day traded value ≥ ₹10 cr. Exclude stocks in ASM/GSM and those with circuit-limit days in the last 3 months.
- **Signal:** composite rank = 50% momentum + 25% quality + 25% low-vol.
  - Momentum: volatility-adjusted 12-1M and 6-1M return, Nifty-style normalised score.
  - Quality: ROE, low debt/equity and earnings stability.
  - Low-vol: 1Y daily volatility.
- **Absolute filter:** hold nothing with a negative 12M return.
- **Holdings:** N = 20 at full scale (or 12–15 if only the 25% sleeve is DIY). Minimum position 2.5% of the sleeve, or about ₹10k, whichever is larger. Minimum trade ₹5,000.
- **Weighting:** equal weight or inverse 1Y vol, capped at 8% per name and 30% per sector. Use no score tilt.
- **Rebalance:** **quarterly** for full-scale DIY, or semi-annual if the user insists on the lowest tax drag. Set dates **off** the NSE June/December reconstitution windows (e.g. mid-Feb/May/Aug/Nov) to avoid trading alongside the index flows. No monthly rebalancing.
- **Buffer (hysteresis):** enter at rank ≤ N; keep while rank ≤ 2N and 12M return > 0. Between rebalances, sell only on existing hard risk rules (trailing stop / cap breach).
- **Drift:** do not re-equalise weights between rebalances unless a name exceeds 1.5× its target weight.
- **Cost model in the backtest:** buy 0.12% + sell 0.104% + ₹16 per sell scrip + 0.10% spread per side. Add a **tax model** that charges STCG 20% on gains held <12 months and LTCG 12.5% above ₹1.25L per year. Give priority to holding winners that are 10–12 months old until they pass 12 months, provided they remain within the 2N buffer.
- **Expected drag:** about 0.4–0.6%/yr trading costs plus about 0.5–1.5%/yr tax at quarterly cadence (illustrative). The sleeve must beat the momentum index fund by more than that to justify itself.
- **Validation:** walk-forward hindcast against Nifty 200 TRI, the Nifty200 Momentum 30 TRI and the factor fund NAV, all net of costs and tax. Report turnover, hit-rate and max drawdown. Survivorship-free universe required.
- **Transition:** converge the 34 holdings over 2–4 quarterly cycles. Order exits as losses first, then LTCG within the exemption, then let STCG winners age. Send all new cash to underweights or the fund sleeve, and cap selling at 30% of NAV per cycle.
- **Governance:** monthly risk check, calendar-only rebalancing and an annual review. Switch the DIY sleeve to the index fund if it trails the fund by more than 1.5%/yr over 36 months. Do not abandon the factor over drawdowns shorter than 5 years.
