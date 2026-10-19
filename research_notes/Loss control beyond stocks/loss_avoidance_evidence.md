# Systematic loss-avoidance at the portfolio/index level: evidence, costs, and India application

Scope: long-only or cash/debt switching, no leverage, Indian long-term investor, as of Oct 2026. Context: the repo's stock-level risk rules cut max drawdown from -26% to -21% but cost about 3.7%/yr against buy-and-hold over Oct 2022–Oct 2025 (repo hindcast, `reports/hindcast_summary.md`).

Note on verification: several pages could not be fetched (DNS failures on capitalmind.in, morningstar.in, cxoadvisory.com), so some figures come from search-result summaries rather than the primary text. Figures I recall from the papers but could not re-verify in this session are marked **[UNVERIFIED, from memory]**.

---

## Q1. Index-level trend filters (10-month SMA / 200-DMA, Faber; time-series momentum, MOP; Hurst-Ooi-Pedersen): global and Indian evidence, whipsaw, after-tax effect

### Takeaway
Trend filters reliably cut **deep** drawdowns (the 2000–02 and 2008 kind), because those bear markets are slow and long. They do not reliably raise return. In long bull runs and V-shaped crashes (March 2020) they lose to buy-and-hold through whipsaw. In India the evidence is thin and mostly practitioner-grade. A 20% STCG on every exit (12.5% LTCG above ₹1.25 lakh) plus loss of tax deferral makes the after-tax case weaker than the gross backtests suggest.

### Cited Findings
- **Faber (2007; 2013 update), method.** A 10-month SMA filter on each risky asset, checked monthly; hold cash (or bonds) when price is below the SMA. Applied to S&P 500, 10-yr Treasuries, MSCI EAFE, GSCI and NAREIT, equal-weighted, with data back to 1901. Transaction costs and taxes are excluded. Because checks are monthly, large drawdowns can still happen between rebalances. — [QuantConnect summary of Faber GTAA](https://www.quantconnect.com/forum/discussion/8285/a-quantitative-approach-to-tactical-asset-allocation-gtaa-5-with-simplemovingaverage/)
- **Faber headline.** Timing cut the 5-asset portfolio's max drawdown from about 46% to under 10%. — [QuantConnect summary](https://www.quantconnect.com/forum/discussion/8285/a-quantitative-approach-to-tactical-asset-allocation-gtaa-5-with-simplemovingaverage/) (secondary)
- **Faber S&P 500 results, 1901–2012 [UNVERIFIED, from memory].**
  - Buy-and-hold: CAGR about 9.3%, volatility about 17.9%, max drawdown about -83.7%.
  - 10-month SMA timing: CAGR about 10.2%, volatility about 12.0%, max drawdown about -50.3%.
  - GTAA 1973–2012: timing CAGR about 10.5% vs about 9.9% buy-and-hold; max drawdown about -9.5% vs about -46%.
  - Check against the SSRN paper (abstract 962461) before quoting.
- **Moskowitz, Ooi & Pedersen (2012, JFE), time-series momentum.**
  - Covers 58 liquid futures across equity indices, currencies, commodities and bonds, over 25+ years.
  - Returns persist for 1–12 months, then partly reverse over longer horizons.
  - The 12-month TSMOM return was positive for every one of the 58 contracts.
  - Source: [SSRN 2089463](https://papers.ssrn.com/abstract=2089463); [Yale-hosted PDF](https://fairmodel.econ.yale.edu/ec439/jpde.pdf)
- **Hurst, Ooi & Pedersen (2017, JPM), "A Century of Evidence on Trend-Following".**
  - Covers 67 markets, 1880–2016, blending 1-, 3- and 12-month signals.
  - Net annualised return about 11.2% at about 9.7% volatility. Positive average return in every decade.
  - Trend was positive in 8 of the 10 worst 60/40 drawdowns.
  - Note: this is a **long-short, leveraged, multi-asset** futures strategy, not long-only index timing. The authors are at AQR, which sells trend products.
  - Source: [Alpha Architect](https://alphaarchitect.com/portfolio-efficiency/); [The Idea Farm](https://theideafarm.com/alternative-investment/a-century-of-evidence-on-trend-following-investing/); [paper PDF](https://oxfordstrat.com/coasdfASD32/uploads/2016/03/A-Century-of-Evidence-on-Trend-Following-Investing.pdf)
- **Hurst-Ooi-Pedersen, 20% allocation [UNVERIFIED secondary].** A 20% trend allocation reportedly raised the 60/40 Sharpe from 0.39 to 0.55 and cut max drawdown from -62.3% to -50.2%. — [The Idea Farm](https://theideafarm.com/alternative-investment/a-century-of-evidence-on-trend-following-investing/)
- **Whipsaw frequency (S&P 500, 1994–2019).**
  - The index crossed its 200-DMA about 180 times, roughly 7 crosses a year.
  - Of 90 completed bullish signals, 20 won (average +13.69%) and 70 lost (average -1.32%), a win rate of about 22–30%.
  - The profile is a small number of big wins paying for many small losses. Smoothing the signal (5-day MA crossing the 200-day) cut signals to 34 over 25 years.
  - Source: [StockCharts / Arthur Hill](https://articles.stockcharts.com/article/articles-arthurhill-2019-02-just-how-effective-is-the-200-day-moving-average/)
- **S&P 500 200-DMA, one practitioner backtest.** CAGR 6.45% vs 7% buy-and-hold, with a 28% max drawdown (2002). The rule rarely beats buy-and-hold without a recession and falling prices. — [Quantified Strategies](https://quantifiedstrategies.substack.com/p/200-day-moving-average-trading-strategy-dd3) (practitioner, unaudited)
- **India, Nifty 50, Capitalmind (2020).**
  - Tested MA thresholds from 10 to 250 days.
  - A 10-day MA reportedly gave 13.9%/yr vs 10.1% buy-and-hold, but with 293 trades and large tax/cost drag.
  - 200-day figures were not visible in the snippet.
  - Source: [Capitalmind, "Time the market, sleep better"](https://premium.capitalmind.in/2020/05/time-the-market-sleep-better/) (paywalled, page could not be fetched; figures from search snippet only, **unverified**)
- **India, academic (Slivka, Keswani & Li 2014, Indian Journal of Finance).**
  - Tested 80 trend algorithms on Nifty, 2005–2012.
  - They worked well in sharply falling markets and poorly or not at all in gradually rising, mixed or trendless markets.
  - No costs, shorts or leverage were assumed.
  - Source: [Indian Journal of Finance](https://www.indianjournalofentrepreneurship.com/index.php/IJF/article/view/71980)
- **India, time-series momentum on BSE stocks, 1996–2020.**
  - A substantial absolute-momentum effect exists, but it is exposed to occasional severe (crash) losses.
  - A risk-managed version reportedly delivers 2.5x the return with better downside.
  - This is a stock-level long-short study.
  - Source: [Risk-managed TSMOM: an emerging economy experience (JEFAS / RePEc)](https://ideas.repec.org/a/eme/jefasp/jefas-08-2021-0159.html)
- **India, freefincal (1999–2016).** Compares investing only when Nifty is above vs below its 200-DMA. This is a recurring-investment test, not a sell rule. The author warns the sample is short. — [freefincal: Nifty 200 DMA buying high vs buying low](https://freefincal.com/nifty-200-dma-buying-high-vs-buying-low/)
- **Indian tax.**
  - STCG on listed equity (held 12 months or less): 20%. LTCG: 12.5% above a ₹1.25 lakh/yr exemption, no indexation. Both effective 23 Jul 2024.
  - Secondary sources say no change in Budgets 2025/2026; verify against the Finance Act.
  - Source: [DSP MF](https://www.dspim.com/knowledge-hub/personal-finance-guide/capital-gains-filing-in-india-what-to-report-where-and-how/stcg-and-ltcg-rules-in-india); [5paisa](https://www.5paisa.com/blog/evolution-of-ltcg-stcg-tax-in-india)

### Inferences
- **Mechanism.** Trend filters work because big equity bear markets are mostly slow, macro- or valuation-driven declines (2000–03, 2008). Prices fall below the 10-month SMA early enough to dodge the middle of the loss. They fail when the loss is fast and the rebound faster (1987, Mar 2020, the Jun 2022 Nifty dip, Apr 2025). There the filter sells near the low and buys back higher, which turns a temporary loss into a permanent one.
- **Expected effect for Nifty (long-only, switching to liquid/debt fund).**
  - Max drawdown: roughly 50–60% deep crashes cut to roughly 25–35% (inferred from the global studies; India-specific magnitudes unverified).
  - Gross return: anywhere from about -1%/yr to slightly positive.
  - In a strong bull window like 2022–2025, expect to trail buy-and-hold by about 1–3%/yr.
- **After tax in India.**
  - Every exit after a gain held under 12 months pays 20% STCG immediately. That destroys the deferral benefit.
  - Re-entry resets the 12-month clock, so a whipsaw-heavy year can turn much of the long-term gain into short-term gain.
  - Cash parked in debt funds is taxed at slab rate.
  - Running the rule inside tax-neutral wrappers removes this drag: a balanced advantage fund (equity taxation, no tax on internal switches) or switching only new SIP flows.
  - The most tax-efficient way to "time" for an individual: never sell; only redirect new money and rebalancing flows.
- **Parameter sensitivity.**
  - 150–250 day (or 8–12 month) windows give broadly similar drawdown reduction. That is a robust plateau, not a knife-edge.
  - Daily checking raises whipsaw several-fold compared with monthly checking.
  - A band (e.g. exit at 2–3% below the SMA, re-enter above it) or a monthly check cuts trade count a lot.
  - The 10-day MA "winner" in the Capitalmind snippet is very likely overfit and uninvestable after tax.

### Gaps
- No peer-reviewed, cost- and tax-inclusive study of a 200-DMA / 10-month SMA rule on the Nifty 50 TRI back to the 1990s was found. Capitalmind's full table (drawdowns, 200-DMA row) could not be accessed.
- No Indian whipsaw count (crosses per year on Nifty) was found. This can be computed from repo data (NIFTYBEES).
- Faber's exact figures need checking against the SSRN PDF.

---

## Q2. Volatility targeting / volatility-managed portfolios (Moreira-Muir 2017; Cederburg et al. 2020): does it work out-of-sample, and at what turnover?

### Takeaway
Volatility scaling of the equity market reliably makes **left tails less severe**: crashes tend to happen when volatility is already high, so exposure is already lower. The claimed **alpha/Sharpe improvement does not survive** real-time implementation across most factors (Cederburg et al.), nor transaction costs. For a no-leverage investor it reduces to "hold less equity when realised volatility is high". That gives a modest drawdown cut at a modest return cost, with more monthly turnover than a trend filter.

### Cited Findings
- **Moreira & Muir (2017, JF 72(4)).**
  - For the market, the October 2016 draft reports 4.9% alpha, an appraisal ratio of 0.33, and about a 25% higher Sharpe than buy-and-hold.
  - Across factors, Sharpe rises 50–100%.
  - Mechanism: changes in volatility are not matched by changes in expected return.
  - Note: the strategy uses **leverage** in calm periods.
  - Source: [NBER w22208](https://www.nber.org/papers/w22208.pdf); [NBER page](https://www.nber.org/papers/22208)
- **Cederburg, O'Doherty, Wang & Yan (2020, JFE).**
  - Covers 103 equity strategies. Spanning-regression alphas are positive in-sample, but the real-time versions earn lower certainty-equivalent returns and Sharpe ratios than the unmanaged portfolios.
  - Cause: structural instability in the spanning regressions.
  - Per a summary, out-of-sample implementations show lower Sharpe and certainty-equivalent returns in 72 of 103 cases, **gross** of costs.
  - Source: [COWY PDF (Lehigh)](https://www.lehigh.edu/~xuy219/research/COWY.pdf); [Alpha Architect](https://alphaarchitect.com/?p=59058); [CXO summary](https://www.cxoadvisory.com/volatility-effects/does-volatility-management-work-for-equity-factor-portfolios/)
- **Barroso & Detzel (2020).** Volatility-managed strategies do not survive transaction costs. — cited via [HKU seminar abstract, Martin-Utrera/Uppal/DeMiguel](https://hkubs.hku.hk/event/a-multifactor-perspective-on-volatility-managed-portfolios)
- **Harvey, Hoyle, Korgaonkar, Rattray, Sargaison & Van Hemert (2018, JPM), "The Impact of Volatility Targeting" (Man Group).**
  - Sharpe improves only for risk assets (equities, credit), via the leverage effect.
  - Volatility targeting reduces extreme returns in all asset classes. Left-tail events are less severe because they come when volatility is high and exposure is already small.
  - US equity vol-of-vol falls from 4.6% to 1.8% (secondary).
  - Source: [Duke PDF](https://people.duke.edu/~charvey/Research/Published_Papers/P135_The_impact_of.pdf); [Quantpedia](https://quantpedia.com/the-impact-of-volatility-targeting-on-equities-bonds-commodities-and-currencies); [Alpha Architect](https://alphaarchitect.com/volatility-targeting-improves-risk-adjusted-returns/)

### Inferences
- **Without leverage**, volatility targeting is capped at 100% equity. Only the de-risking half remains, so the strategy is structurally underweight equity on average and pays the equity premium on that underweight. Expect about 0.5–2%/yr less return than 100% equity, with better risk-adjusted return and a shallower worst month. This is my estimate, not sourced.
- **V-shaped failure.** Realised volatility peaks *at* or *after* the low (Mar 2020). The rule de-risks late and re-risks slowly, missing the rebound. Using a longer volatility lookback reduces turnover but makes this lag worse.
- **Turnover.** Monthly scaling on 1-month realised volatility can move exposure 20–40 percentage points a month in turbulent spells (inference). Indian tax on those trims makes a no-leverage version of Moreira-Muir worse after tax than gross.
- **Simplest robust variant.** Scale between, say, 100% and 60% equity using the ratio of target to realised 3–6 month volatility, apply a no-trade band, and act through flows rather than sales.

### Gaps
- No India-specific (Nifty) volatility-targeting study was found.
- Left-tail and drawdown figures from Harvey et al. for equities were not verified from the full text.

---

## Q3. Drawdown-control, CPPI and "risk budget" rules (cut equity when portfolio drawdown exceeds X%)

### Takeaway
CPPI and drawdown-floor rules **guarantee** a bound on drawdown only in continuous-trading theory. In practice they face gap risk, and more importantly **cash-lock**: after a deep fall they sit in cash and miss the recovery. They are path-dependent and mechanically sell after losses, which is the opposite of rebalancing. For a long-horizon investor they convert temporary drawdowns into permanent shortfall. They are best used to meet a liability or behavioural constraint, not as a return-neutral loss avoider.

### Cited Findings
- **Grossman & Zhou (1993).** Extend Merton's portfolio problem with a constraint that wealth stays above a fraction α of its running maximum. The optimal risky exposure is proportional to the cushion above the floor, i.e. a CPPI on a rising floor. — [Columbia drawdown-minimisation note](https://drupalgsb-test.paas.cc.columbia.edu/sites/default/files-efs/pubfiles/6358/drawdownminimization.pdf)
- **Gap risk and cash-lock in CPPI.**
  - Gap risk: the risky asset can fall through the floor between rebalances.
  - Cash-lock: after a deep drawdown the strategy can end up all in cash and miss recoveries.
  - A drawdown-CPPI variant sets the floor as a percentage of the running peak.
  - Source: [Quantpedia CPPI intro](https://quantpedia.com/introduction-to-cppi-constant-proportion-portfolio-insurance/); [MetricGate CPPI](https://metricgate.com/docs/constant-proportion-portfolio-insurance/); [THEMA working paper 2023-22](https://thema.u-cergy.fr/IMG/pdf/2023-22.pdf)
- **Practitioner backtest.** Drawdown-CPPI on SPY, 2015–2020: slightly lower returns, much better drawdown than plain CPPI. Short sample. — [Alpaca CPPI](https://alpaca.markets/learn/cppi-1/)
- **Behavioural motivation.** Investors typically withdraw after about a 20% one-year drawdown (Chekhlov et al., cited in the source). — [THEMA 2023-22](https://thema.u-cergy.fr/IMG/pdf/2023-22.pdf)

### Inferences
- A "cut equity to X% if portfolio drawdown exceeds 15%" rule sells **after** the loss has happened. The decision is only right if losses keep going (momentum) and wrong if they mean-revert (V-shape).
  - Indian episodes Mar 2020, Jun 2022 and Oct 2024–Mar 2025 were mostly mean-reverting within 6–12 months.
  - 2008 was continuing. A drawdown trigger would have helped there.
  - Without a **re-entry** rule (time, trend or valuation), the strategy is cash-locked. The re-entry rule is where most of the performance lives, and it is a free parameter that invites overfitting.
- **Path dependence.** Two investors with the same assets but different start dates (different running peaks) get different exposures. That is undesirable for a long-term plan.
- **Relation to Kaminski-Lo (Q5).** A portfolio drawdown trigger is a stop-loss on the whole portfolio. It adds value only if index returns show momentum at the trigger horizon.

### Gaps
- No Indian empirical study of drawdown-trigger or CPPI rules on Nifty was found.
- No empirical gap-risk magnitudes for India were found.

---

## Q4. Valuation-based allocation (Nifty P/E or earnings-yield bands; Indian Balanced Advantage / Dynamic Asset Allocation funds), realised record vs static 60/40 or 65/35

### Takeaway
Indian BAF/DAA funds are the live, tax-efficient version of valuation- and trend-based allocation. They did **reduce drawdowns** (e.g. category about -30% vs BSE 500 about -38% over the 5 years to Jun 2022, per Morningstar). Returns are **widely dispersed by fund** and have generally not beaten aggressive hybrid (65–80% equity) funds in strong markets. Drawdown depended mostly on **average equity exposure**, not on clever timing. Valuation signals have weak short-horizon timing power.

### Cited Findings
- **Morningstar India (as of 7 Jun 2022, 5 years).**
  - BAF category drawdown was about -30% vs -38% for the S&P BSE 500.
  - Drawdown tracked each fund's equity exposure. The category's worst performer averaged about 81% equity in early 2020.
  - Source: [Morningstar India: Hybrid funds which protected the most downside](https://morningstar.in/posts/68775/hybrid-funds-which-protected-the-most-downside.aspx) (via search snippet; page not fetched)
- **One-year comparison (2025, secondary).** Aggressive hybrid averaged about 8.1% vs about 5.5–6% for BAF. — [Belong blog citing Business Standard/Scripbox](https://getbelong.com/blog/mutual-funds/hybrid-vs-pure-equity-funds/) (secondary, single year)
- **Sep 2024–Mar 2025 correction.** BAFs fell less than large-cap funds. — same [Belong blog citing NISM](https://getbelong.com/blog/mutual-funds/hybrid-vs-pure-equity-funds/)
- **5-year CAGR examples, Direct-Growth, Jul–Sep 2026.** Benchmark is NIFTY 50 Hybrid Composite Debt 50:50.

  | Fund | 5-yr CAGR | Benchmark | Rank (5-yr) |
  |---|---|---|---|
  | Baroda BNP Paribas BAF | 11.39% | 7.77% | 2/23 (6 Sep 2026) |
  | Bank of India BAF | 10.97% | 9.72% | 5/23 |
  | Invesco India BAF | 9.29% | 9.90% | 14/22 |

  Dates differ across funds. Source: [sharpely – Baroda BNP](https://sharpely.in/mutual-funds/baroda-bnp-paribas-balanced-advantage-fund-directgrowth/38113/performance); [sharpely – Bank of India](https://sharpely.in/mutual-funds/bank-of-india-balanced-advantage-fund/24756/performance); [sharpely – Invesco](https://sharpely.in/mutual-funds/invesco-india-balanced-advantage-fund/16740/performance) (aggregator)
- **BAF category 1-year average.** Conflicting snapshots: 3.37% (11 Sep 2026) vs -1.51% (7 Oct 2026). Unreconciled. — [Arthgyaan comparison pages](https://arthgyaan.com/fund/compare/baroda-bnp-paribas-balanced-advantage-fund-direct-growth-vs-iti-balanced-advantage-fund-direct-growth/145396-vs-147789)
- **Valuation timing on Indian data.** The question "can we find support for buying when Nifty falls 15% from a peak?" proved elusive. — [freefincal: How often has the Nifty crashed?](https://freefincal.com/nifty-crash/)
- **Structural difference.** BAF vs aggressive hybrid: BAFs vary net equity (typically 30–80%) by model and keep equity taxation through arbitrage hedges. Aggressive hybrids hold 65–80% equity statically. — [PGIM India explainer](https://www.pgimindia.com/mutual-funds/learn-more/balanced-advantage-funds-vs-aggressive-hybrid-funds)

### Inferences
- The fair comparison for a BAF is a **static mix with the same average equity** (e.g. 55/45). Against that, the evidence that BAF timing adds value net of fees (about 0.5–1% direct TER, plus arbitrage carry drag) is weak and fund-specific. The drawdown reduction comes mostly from lower average equity, which an investor can get for free with a static allocation.
- **Tax advantage.** A BAF rebalances internally with no capital-gains event for the unitholder, and keeps equity taxation via arbitrage. This is the main real benefit over DIY timing in India.
- **Long-horizon evidence.** Valuation bands (P/E, P/B, earnings yield minus G-sec yield) have documented long-horizon (5–10 year) return predictability globally, but poor 1-year timing power. Long periods of "expensive" markets (India 2021–2024) keep valuation-driven funds underweight through rallies.

### Gaps
- No verified category-level BAF vs 65/35 or 60/40 static comparison was found over a full cycle (e.g. 2008–2026), whether rolling returns or max drawdowns. Value Research category data could not be retrieved.
- Morningstar's full numbers were not fetched (DNS failure).
- No verified study of Nifty P/E-band switching rules after costs and tax was found.

---

## Q5. Stop-loss evidence (Kaminski & Lo 2014): whole portfolio vs single stock

### Takeaway
Stop-losses are not free insurance. Under a random walk they **always reduce expected return**. They add value only when returns show **momentum (positive autocorrelation)** at the horizon of the rule. Index and asset-class returns show time-series momentum (MOP 2012), while single stocks show more short-term reversal and idiosyncratic noise. So whole-portfolio and index-level stops (trend filters are a smooth stop-loss) have a better theoretical basis than single-stock trailing stops. This matches the repo's finding that stock-level stops cost about 3.7%/yr.

### Cited Findings
- **Kaminski & Lo (2014), "When do stop-loss rules stop losses?"**
  - Under the random walk hypothesis, simple all-or-nothing stop-loss rules reduce expected return. Under momentum they can add value.
  - On US equity monthly data 1950–2004 (switching to bonds), some rules added about 50–100 bp/month **during stop-out periods**.
  - Source: [MIT DSpace record](https://dspace.mit.edu/entities/publication/bb69ca4b-0cdc-487f-831d-63b2e84fafee); [dailyspeculations](https://dailyspeculations.com/wordpress/?p=14247)
- **Lo & Remorov (follow-up).** High trading costs can erase stop-loss benefits even when returns are serially correlated. — [search summary; see Lund/UPC stop-loss studies](https://upcommons.upc.edu/bitstream/handle/2117/169672/stop-loss%20rules.pdf;jsessionid=1136A05242F123307C8BE06C8CE30C54?sequence=3)
- **Index-level momentum.** 1–12 month time-series momentum exists for equity indices. — [MOP 2012](https://papers.ssrn.com/abstract=2089463)

### Inferences
- The "50–100 bp/month during stop-out periods" figure is conditional on being stopped out. Unconditional annual gains are much smaller and depend heavily on the period.
- Single-stock trailing stops in the repo fire mostly on idiosyncratic noise. Selling a stock does not avoid market risk, because the proceeds are reinvested. That is consistent with the repo hindcast: some drawdown cut, high return cost.

### Gaps
- Kaminski-Lo did not include Indian tax. No India-specific stop-loss study (index level) was found.

---

## Q6. Simplest robust loss-limiting approach for a retail investor; is "avoid all losses" achievable? Ranked evidence review

### Takeaway
**No model can "avoid all losses" without giving up most of the equity return.** Every reliable drawdown reducer either holds less equity on average or sells after prices fall, so it pays an insurance premium in expected return, tax or whipsaw. The cheapest, most robust loss-limiter is a **static strategic allocation with rebalancing** (e.g. 65/35 or 70/30 equity/debt), sized to the drawdown the investor can live with. A **slow, banded, monthly trend filter** applied to new flows or one sleeve is a defensible optional overlay against deep, slow bear markets.

### Ranked evidence review
Ranked by robustness of evidence and drawdown cut per unit of after-tax return cost, for an Indian long-only investor. All magnitudes are inferences synthesised from Q1–Q5, not sourced point estimates.

| Rank | Technique | Evidence quality | Typical max-drawdown change | Expected return cost (after tax, India) | Main failure regime |
|---|---|---|---|---|---|
| 1 | **Static equity/debt mix + periodic or band rebalancing** (e.g. 65/35) | Very high: arithmetic, no prediction needed | Proportional to the debt share. 35% debt cuts a 60% equity crash to about 40% | Equity-premium give-up on the debt share (about 1.5–2.5%/yr at 35% debt, assuming a 4–7% equity-debt spread). Rebalancing tax is small if done with flows | None structural. Lower terminal wealth in long bulls |
| 2 | **Slow trend filter at index level** (10-month SMA / 200-DMA, monthly check, ±2–3% band), equity to liquid/short-debt fund | High globally (Faber, MOP, HOP); low/moderate in India (Slivka et al.; practitioner) | Large in slow bears (2008-type: about -60% to about -25–35%). Little help in V-crashes | About 0 to -2%/yr gross. Worse after STCG if run on taxable holdings; near zero if run via flows or a wrapper | Whipsaw in choppy or V-shaped markets (2020, 2022, 2025); about 1–3 false signals/yr even with banding |
| 3 | **BAF/DAA fund** (outsourced valuation + trend allocation) | Moderate: live records exist, but dispersion is high | Category drawdown about 8 points shallower than BSE 500 (2017–22) | Roughly in line with a 50:50 benchmark; trails aggressive hybrid in bulls; TER about 0.5–1% direct | Manager or model risk. Stays underweight equity in prolonged "expensive" rallies |
| 4 | **Volatility targeting, no leverage** (100% down to 50–60% equity) | High for tail reduction (Harvey et al.); low for alpha OOS (Cederburg) | Moderate cut in crash months | About 0.5–2%/yr plus turnover tax | V-shaped crashes (de-risks late, re-risks late) |
| 5 | **Time-series momentum across asset classes** (long-only: equity/gold/debt each on or off by 12-month return) | High globally; India untested | Moderate to large | Similar to rank 2; more instruments, more turnover | Trend reversals; correlation spikes |
| 6 | **Portfolio drawdown trigger / CPPI** (cut equity when drawdown exceeds X%) | Theory solid (Grossman-Zhou); weak empirical support for long-horizon investors | Bounds drawdown in theory (gap risk aside) | Potentially large: cash-lock after crashes; re-entry rule is a free parameter | V-shaped recoveries; path dependence |
| 7 | **Single-stock stops / trailing stops** | Kaminski-Lo: negative under random walk; repo hindcast: -3.7%/yr | Small (repo: -26% to -21%) | High (repo: about 3.7%/yr) | Idiosyncratic noise; does not remove market beta |

### Cited Findings
- Stop-losses reduce expected return under a random walk. Loss-avoidance has a cost unless there is momentum. — [Kaminski & Lo, MIT](https://dspace.mit.edu/entities/publication/bb69ca4b-0cdc-487f-831d-63b2e84fafee)
- Trend works in sharp declines, not in gradual or trendless markets (Nifty 2005–2012). — [Slivka, Keswani & Li](https://www.indianjournalofentrepreneurship.com/index.php/IJF/article/view/71980)
- 200-DMA rules: low win rate and frequent whipsaw. — [StockCharts](https://articles.stockcharts.com/article/articles-arthurhill-2019-02-just-how-effective-is-the-200-day-moving-average/)
- Volatility-managed alpha fails out of sample. — [Cederburg et al.](https://www.lehigh.edu/~xuy219/research/COWY.pdf)
- BAF drawdowns depend on average equity exposure. — [Morningstar India](https://morningstar.in/posts/68775/hybrid-funds-which-protected-the-most-downside.aspx)

### Inferences
- **Honest framing.** Drawdown protection is insurance. Its long-run premium is roughly the equity premium forgone on average de-risked exposure, plus whipsaw, plus tax. Cash-switching rules that occasionally *raise* return (Faber's S&P result) do so because of a few huge bear markets (1929–32, 1973–74, 2000–02, 2008). The investor needs one of those in their horizon to be paid.
- **Why the repo's 2022–2025 window was costly.** It was a strong Indian bull market with only shallow or V-shaped corrections, the worst case for all loss-avoidance rules. That a rule underperformed in this window is expected and is not evidence that it is useless. Equally, the 2022–2025 data cannot validate any of these rules, because there was no deep bear market to test them against.
- **"Avoid losses" is achievable only in the trivial sense of holding debt or cash.** A realistic goal: cap drawdown at roughly X% in deep bear markets, accepting about Y%/yr lower expected return and occasional whipsaw.

### Gaps
- No sourced, India-specific, cost- and tax-adjusted numbers were found for ranks 2, 4 and 5. Those must come from the repo's own backtest on Nifty data.

---

## Q7. Implications for the repo (/home/user/Portfolio)

### Takeaway
Do not add more stock-level stops. If any rule is implemented, the most defensible is an **index-level, monthly, banded 10-month-SMA (about 200-DMA) overlay on the total equity sleeve**:
- Signal: NIFTYBEES/Nifty 50 TRI vs its 200-DMA, checked monthly, with an exit band of -2% to -3%.
- Action: shift a **partial** amount (e.g. 30–50% of equity) to a liquid/short-duration debt fund, preferably by redirecting new money first and selling long-term lots second.

It should be judged on deep-drawdown reduction per unit of after-tax CAGR lost, over a sample that **includes 2008 and 2020**. The 2022–2025 window alone is not enough.

### Cited Findings
- **Harness structure** (repo code: `hindcast/run.py`, `hindcast/stats.py`, `hindcast/data.py`):
  - Benchmark is `NIFTYBEES.NS` (`hindcast/data.py:14`).
  - `regime_labels()` already computes `bench_above_200dma` and `bench_drawdown_gt_10pct`.
  - `book_summary()` reports FOLLOW-MODEL / DO-NOTHING / NIFTYBEES books with `nav_metrics`, turnover and a block-bootstrap CI on active returns.
  - `deflated_sharpe` and `pbo_cscv` gate parameter acceptance (DSR ≥ 0.95, PBO ≤ 0.30).
  - The grid is pre-committed in `data/hindcast/grid.json`. Windows: TRAIN 2019-01 to 2022-09, PRIMARY 2022-10 to 2025-10, TEST 2023-10 to 2025-10.
- Evidence basis for choosing a slow index-level trend filter over stock stops: [MOP 2012](https://papers.ssrn.com/abstract=2089463), [Kaminski & Lo](https://dspace.mit.edu/entities/publication/bb69ca4b-0cdc-487f-831d-63b2e84fafee), [Hurst-Ooi-Pedersen](https://alphaarchitect.com/portfolio-efficiency/).

### Inferences: validation plan
1. **Add a book "D: NIFTYBEES + overlay"** (and optionally "A + overlay") alongside A/B/C in `book_summary`.
   - Overlay: on each monthly decision date, if close is below 200-DMA × (1 − band), set equity weight to w_low (e.g. 0.5–0.7). Otherwise use 1.0. Proceeds go to a debt proxy (liquid fund NAV, or a 6–7% p.a. accrual series).
   - Reuse `regime_labels()` for the signal, so no new feature code is needed.
2. **Extend the sample.** NIFTYBEES has history from about 2002. Fetch at least 2005–2026 (or Nifty 50 TRI) so the test includes 2008, 2011, 2015–16, 2020, 2022 and 2024–25.
   - The rule must be judged across **multiple bear markets**: report per-episode drawdown, time-to-recover and missed-rebound cost.
   - The existing 2019–2025 TRAIN/TEST split contains one V-crash and no slow bear, so it is structurally unable to show the benefit.
3. **Model Indian costs and tax explicitly.**
   - 20% STCG on gains of lots held 12 months or less; 12.5% LTCG above ₹1.25 lakh/yr; STT and brokerage about 0.1–0.2% per switch; debt-fund returns taxed at slab rate.
   - Report pre- and post-tax CAGR. Also simulate a "flow-only" variant: redirect monthly contributions and rebalancing without selling.
4. **Pre-register a tiny grid** in `grid.json`:
   - SMA {150, 200, 250 days or 10 months}
   - band {0, 2%, 3%}
   - w_low {0.5, 0.7}
   - check frequency monthly only

   That is 12–18 configs. Run DSR/PBO as for other parameters. Expect PBO to be informative only with the long sample. Look for a **plateau**, not a peak.
5. **Metrics to report.**
   - Max drawdown, CDaR/Ulcer index, worst 12-month return.
   - CAGR (pre- and post-tax), number of switches per year, whipsaw cost (sum of losses on round-trips under 3 months).
   - Calmar ratio, and capture ratios in up and down months against NIFTYBEES.
6. **Acceptance criterion (suggested).**
   - Adopt only if, over 2005–2026, post-tax max drawdown falls by at least 10 points and post-tax CAGR falls by no more than about 1%/yr.
   - The result must hold across the parameter plateau (not one cell), and in at least two of three bear episodes (2008, 2020, 2024–25).
   - Otherwise, recommend the static-allocation answer (rank 1), sized by the drawdown the user can tolerate.
7. **Comparator.** Include a static 65/35 (NIFTYBEES/debt) rebalanced-annually book. If the overlay does not beat static 65/35 on Calmar and post-tax CAGR at equal average equity exposure, it is not adding timing value. It is just holding less equity, as with BAFs.

### Gaps
- Debt or liquid-fund NAV history is not in the current cache. It is needed for realistic cash returns; a constant accrual proxy is a fallback.
- The harness's tax model (`tax_planner.py`) was not inspected for lot-level STCG/LTCG support. Check before relying on post-tax outputs.
