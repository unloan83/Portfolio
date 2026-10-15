# Systematic sources of excess return in Indian equities: evidence, magnitudes, and failure modes (long-only, retail)

Research method note: done 2026-10-15. WebFetch failed on every domain tried (DNS errors for niftyindices.com, iima.ac.in, jrvarma.in, freefincal.com and quantpedia.com), so **every finding below comes from search-result snippets and summaries, not the full primary documents**. Treat the magnitudes as indicative. Before any number goes into the repo, check it against the NSE factsheets and whitepapers and the IIMA data library, which are linked inline. Numbers I could not verify are flagged with "(unverified)".

---

## 1. Cross-sectional momentum (6-1 / 12-1, risk-adjusted) in India

### Takeaway
Momentum has the strongest raw premium of any factor in Indian equities. The evidence covers academic long-short work from 1993 onward, the NSE index back-test from 2005, and about six years of live index funds. It also has the worst crash profile of any factor: about -70% peak-to-trough in the 2008 back-test, and -30% to -32% in Sep 2024 to Mar/Apr 2025, roughly twice the Nifty 50 fall. Since 2024 it has had a long, painful live underperformance.

### Cited Findings
- **Academic long-short premium.** Agarwalla, Jacob & Varma (IIMA WP 2013-09-05, "Four Factor Model in Indian Equities Market") build Fama-French and Carhart factors for India for Oct 1993 to Dec 2013. They exclude illiquid stocks so the portfolios are investable and correct for survivorship bias from vanishing companies. The abstract reports momentum (WML) as the standout factor at about 21.9%/yr, against about 11.5% for the market premium, with SMB and HML much lower. The snippet was garbled, so verify against the PDF. The factor series are published in a data library the authors said would be updated monthly. — [IIMA publication page](https://www.iima.ac.in/publication/four-factor-model-indian-equities-market); [WP PDF](https://web.iima.ac.in/~iffm/legacy/four-factors-India-90s-onwards-IIM-WP-Version-original-Sep13.pdf); [Varma data library](https://www.jrvarma.in/fama-french.html)
- Ansari & Khan (2012, *Managerial Finance*) find strong momentum profits in India for 1995–2006 that CAPM and Fama-French do not explain. — [Emerald](https://emerald.com/insight/content/doi/10.1108/03074351211193730/full/html)
- Maheshwari & Dhankar (2017, *Vision*) find momentum profits are strong in India but that momentum strategies crash during financial crises. — [IDEAS](https://ideas.repec.org/a/sae/vision/v21y2017i1p1-12.html)
- Singh et al. (2022, *FIIB Business Review*, 450 BSE stocks) find momentum profits are negatively skewed and prone to occasional severe losses, and propose a risk-managed (vol-scaled) version. — [IDEAS](https://ideas.repec.org/a/sae/fbbsrw/v11y2022i3p347-358.html)
- **Long-only implementation.** Raju & Chandrasekaran (SSRN 3510433) test a long-only, monthly-rebalanced portfolio of the top-decile NIFTY100 stocks by momentum. It beat the index by about 10.7%/yr, with mean monthly turnover of about 32.1%. The authors argue the edge survives costs given discount brokers. — [SSRN](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3510433_code3354364.pdf?abstractid=3510433&mirid=1)
- Raju & Teli ("'Long' Factors, not 'Short' Change", SSRN 4000418) test equal-weighted, monthly-rebalanced long-only portfolios from the top 200 stocks. Alpha for momentum, low volatility and quality survives realistic costs, and low volatility and quality have fairly low turnover. — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4000418)
- Raju ("Shades of Momentum", SSRN 4977717, 2024) finds momentum returns are substantial at short holding periods and weaken significantly as the holding period lengthens. — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4977717)
- **Practitioner tax drag.** Raju notes that monthly momentum models run 25–30% average monthly turnover, which "leads to 4% tax costs on 1% gains" (15% STCG, no loss offset). STCG has since risen to 20% (July 2024 budget, not sourced here), so the drag would now be higher. — [Raju on X](https://x.com/rajanraju26/status/1859091783231177157)
- An IIMA webinar (Rajan Raju) argues that the Indian momentum factor earns higher long-run returns *because* it suffers short- and medium-term crashes, and that India's top-heavy market poses implementation challenges. — [IIMA webinar](https://iima.ac.in:443/eventswebinar-systematic-long-only-momentum-strategy-financial-markets-evidence-india)
- **NSE Nifty200 Momentum 30 methodology:**
  - It holds the top 30 Nifty 200 stocks (F&O-eligible, with at least one year of listing) ranked by a Normalised Momentum Score: 6-month and 12-month returns adjusted for daily volatility.
  - Weights are free-float market cap × score, capped at the lower of 5% or 5× the stock's free-float market-cap weight.
  - It is rebalanced semi-annually in June and December, with a rank buffer to reduce turnover.
  - — [NSE factsheet](https://www.niftyindices.com/Factsheet/Factsheet_Nifty200_Momentum30.pdf); [NSE static page](https://niftyindices.com/indices/equity/strategy-indices/nifty200-momentum-30-index-static)
  - HDFC AMC describes the score as 50% 12-month and 50% 6-month price return, vol-adjusted. — [HDFC PPT Jul 2026](https://files.hdfcfund.com/s3fs-public/Others/2026-07/HDFC%20NIFTY200%20Momentum%2030%20Index%20Fund_PPT%20%28July%202026%29.pdf)
- **Turnover at index rebalances:**
  - About 20 of 30 constituents were expected to change at the June 2025 reshuffle. — [Business Standard](https://www.business-standard.com/amp/markets/stock-market-news/nifty200-momentum-30-index-to-see-20-stock-changes-on-june-27-125062600872_1.html)
  - 19 constituents were replaced in Dec 2025, an event that moved about ₹16k cr. — [Business Standard](https://www.business-standard.com/amp/markets/news/nifty200-momentum30-a-flip-of-index-switch-jolts-16k-cr-across-the-grid-125121400388_1.html)
- **Long-run index performance.** The NSE 2026 whitepaper reports 19.19% annualised for Nifty200 Momentum 30 against 15.08% for Nifty 200, about +4.1 pp/yr. The period is roughly Apr 2005 to Feb 2026, per a secondary summary. Momentum volatility is "marginally higher". The index launched on 25 Aug 2020 with a base date of 1 Apr 2005, so about 15 of the 21 years are back-tested. — [NSE whitepaper 2026](https://www.niftyindices.com/docs/default-source/indices/nifty200-momentum-30/momentum-strategy-whitepaper_2026.pdf); [DealPlexus summary](https://www.dealplexus.com/blog/momentum-funds-india)
- **2024–25 crash:**
  - From 27 Sep 2024 to 7 Apr 2025, Nifty200 Momentum 30 fell about 31.8% against about 15.4% for the Nifty 50. — [Wright Research](https://www.wrightresearch.in/blog/momentum-mutual-funds-in-bull-bear-markets/)
  - Kotak and HDFC Nifty200 Momentum 30 index funds show max drawdowns of about -30% (27 Sep 2024 to 14 Mar 2025). As of Aug 2026 they had not regained the peak, and their 1-year returns were 0.7–1.8% against a category average of 7–8%. — [Arthgyaan Kotak](https://arthgyaan.com/fund/kotak-nifty-200-momentum-30-index-fund-direct-growth/151781); [Arthgyaan HDFC](https://arthgyaan.com/fund/hdfc-nifty200-momentum-30-index-fund-direct-growth/152430)
  - The index's all-time high was 38,115 on 27 Sep 2024. It stood at 30,718 on 4 Sep 2026, still about 19% below the peak about two years later (CEIC data via secondary summary, unverified). — [DealPlexus](https://www.dealplexus.com/blog/momentum-funds-india)
- **Back-test drawdown:**
  - A third-party 18-year back-test (Dec 2006 to Jun 2025, net of costs) shows a momentum max drawdown of -70.5% (2008), with about 65 months to recover, against -55.1% for the Nifty 50. — [BacktestIndia momentum](https://backtestindia.com/blog/momentum-investing-india-backtest); [BacktestIndia low-vol](https://backtestindia.com/blog/low-volatility-anomaly-india-nse-backtest)
  - In a separate summary, the same author reports a base Momentum-30 net CAGR of about 14.6% with a -70.6% max drawdown. — [freefincal (search snippet)](https://freefincal.com/is-indian-momentum-investing-just-a-liquidity-illusion/)
- **Liquidity split (Mar 2026, hypothetical, unverified).** Splitting the momentum universe by liquidity, the *less-liquid* half returned 19.4% net CAGR with a -66.4% drawdown, while the *more-liquid* half returned 8.5% net CAGR with a -75.1% drawdown. Much of the premium sits in less-liquid names, where impact costs are highest. — [freefincal](https://freefincal.com/is-indian-momentum-investing-just-a-liquidity-illusion/)
- Over Sep 2024 to Jan 2025, the average momentum strategy lost ₹21,000 per ₹1 lakh invested, against ₹12,600 for the broad market. — [Wright Research](https://www.wrightresearch.in/blog/momentum-mutual-funds-in-bull-bear-markets/)
- In 2026, momentum lagged while value led in India. UTI Nifty200 Momentum 30's trailing 1-year return was about -1% for much of the year, while Nifty500 Value 50 trackers were in the high teens to mid-20s. — [Value Research](https://www.valueresearchonline.com/learn/equity-funds/momentum-vs-value-factor-investing-2026/)
- Delisted stocks are excluded from some practitioner back-tests (e.g., Momo India), which inflates their results. — [Momo India](https://momoindia.substack.com/p/backtest-reducing-momentum-drawdowns)
- **International crash mechanism.** Momentum crashes occur in panic states, after market declines and when volatility is high, as the market rebounds. — [Daniel & Moskowitz, NBER w20439](https://www.nber.org/system/files/working_papers/w20439/w20439.pdf)

### Inferences
- Evidence quality is high for existence: multiple independent academic samples since 1993, out-of-sample relative to the US literature, survivorship-corrected IIMA factors, and live index funds. Evidence is moderate for the *magnitude of the long-only, after-tax premium*. The headline +4 pp/yr is gross, mostly back-tested, and spans 2005–2026.
- The 2008 index drawdown of about -70% and the 2024–25 relative drawdown of about -16 to -17 pp against the Nifty 50 over six months are the planning numbers for crash risk. Live funds took about 2 years and still had not recovered.
- Monthly momentum at about 30% monthly turnover is a tax-and-cost machine for a retail taxable account. Semi-annual or quarterly rebalancing with a rank buffer, as NSE does, keeps most of the premium. "Shades of Momentum" suggests short holding periods earn more, so slower rebalancing trades away some premium for lower cost.
- Fund AUM growth (factor funds over ₹70,000 cr by FY26, momentum leading inflows) plus the ₹16k cr rebalance flows mean crowding is now material. Front-running of the Jun/Dec index rebalance is a plausible new cost for anyone using the same signal at the same dates. Inferred; not measured in any source found.

### Gaps
- I could not open the IIMA paper or library to confirm the 21.9% WML figure, its t-stat, or the post-2013 (out-of-sample) WML series. Pulling the library's monthly WML CSV is the single most valuable next step.
- No primary NSE year-by-year table of Nifty200 Momentum 30 vs Nifty 200 relative returns, so I cannot report the 2008 and 2020 *relative* drawdowns precisely.
- I found no rigorous study of post-2020 (post-ETF) decay in the Indian momentum premium.

---

## 2. Quality / profitability, low volatility, value, size, and multi-factor combinations

### Takeaway
Low volatility and quality have the best risk-reduction evidence in India, plus low turnover, and the academic low-vol alpha is large. Their *return* premium over the cap-weighted index is smaller and regime-dependent: they lag sharply in junk and value rallies (2021, 2023). Value had a huge 2021–2024 run and led again in 2026, but it is cyclical. Momentum and quality, or alpha and low vol, combine well because the factors' bad years differ (2020 vs 2021/2023 vs 2025).

### Cited Findings
- **Low volatility, academic.** Joshipura et al. report an annual alpha spread of 25.53% between low- and high-volatility quintile portfolios in India for Jan 2000 to Sep 2018. The effect is not explained by size, value or momentum. (The figure is a long-short quintile spread, not long-only excess over the index.) — [Mayank Joshipura author page, Business Perspectives](https://www.businessperspectives.org/index.php/journals/author/mayank-joshipura)
- An IIMB study finds the volatility anomaly is stronger at medium- and long-term horizons than short-term. — [IIMB IMR June 2023](https://iimb.ac.in/imr/previous-issues/volatility-june-2023.php)
- **S&P BSE.** In S&P DJI's "An Index Approach to Factor Investing in India", the lowest-volatility quintile beat the highest on both annualised and risk-adjusted returns. The quality, low-vol and multi-factor indices had better drawdowns than the LargeMidCap benchmark in the three largest market drawdowns. The S&P BSE Enhanced Value, Quality, Momentum and Low Volatility indices launched on 3 Dec 2015. — [S&P DJI](https://www.spglobal.com/spdji/en/documents/research/research-an-index-approach-to-factor-investing-in-india.pdf)
- **NSE multi-factor whitepaper (calendar years from 2005).** In 2008, low volatility fell about 44.6% against about 51.8% for the cap-weighted parent, quality about 50.8%, and value about 52.6%. So quality and value gave little crash protection in 2008; low vol gave about 7 pp. — [NSE Multi-Factor whitepaper](https://archives.nseindia.com/content/indices/NIFTY_Multi-Factor_Indices_whitepaper.pdf)
- **Third-party 18-year back-test (Dec 2006 to Jun 2025, net):** low-vol max drawdown -44.6% against -55.1% for the Nifty 50, and low-vol annual volatility 16.7% against 20.8%. The headline low-vol CAGR is 12.38% (the Nifty CAGR comparison was not captured in the snippet). Quality-momentum max drawdown was about -61.7%. — [BacktestIndia low-vol](https://backtestindia.com/blog/low-volatility-anomaly-india-nse-backtest); [BacktestIndia quality-momentum](https://backtestindia.com/blog/quality-momentum-india-backtest)
- Nifty100 Low Volatility 30 is claimed to have had lower drawdowns than the Nifty 100 in 16 of 19 calendar years since 2006 (blog claim, unverified). — [Wright Research](https://www.wrightresearch.in/blog/factor-investing-capital-protection-quality-low-volatility-india/)
- **Calendar-year factor rotation (UTI NFO document and freefincal 2023 table):**

  | Year | Nifty200 Quality 30 TRI | Nifty500 Value 50 TRI | Nifty100 Low Vol 30 TRI | Note |
  |---|---|---|---|---|
  | 2020 | 26.3% | 8.5% | n/a | COVID; quality led |
  | 2021 | 26.2% | 56.4% | n/a | junk/value rally |
  | 2022 | -4.4% | 23.2% | n/a | value led |
  | 2023 | 31.7–31.8% | 62.6–62.8% | 31.9% | PSU/value boom |
  | 2024 (to late Jul) | 13.1% | 30.4% | n/a | partial year |

  — [UTI Nifty200 Quality 30 NFO](https://static.smartspends.com/static/docs/nfo/nfo-uti-nifty200-quality-30-index-fund.pdf); [freefincal 2023 index review](https://freefincal.com/index-observer-how-did-indices-perform-in-2023/)
- In mid-2026, value outperformed momentum in India, with Nifty500 Value 50 trackers at high-teens to mid-20s 1-year returns. — [Value Research](https://www.valueresearchonline.com/learn/equity-funds/momentum-vs-value-factor-investing-2026/)
- An ICICI Direct page shows a -10.0% 1-year return for Nifty200 Quality 30 (undated, unverified). — [ICICI Direct](https://www.icicidirect.com/equity/index/nse/nifty200-quality-30/73733)
- **Nifty Alpha Low-Volatility 30** (launched 10 Jul 2017, base 1 Apr 2005; 30 stocks from Nifty 100 + Midcap 50, alpha and low-vol combined). Reported 5-yr CAGR figures conflict: 14.7% (ICICI ETF page, "5Y+") against 9.79% (Screener). — [NSE factsheet](https://www.niftyindices.com/Factsheet/Factsheet_NIFTY_Alpha_Low-Volatility_30.pdf); [ICICI ETF](https://www.icicietf.com/funds/equity-etf/icici-prudential-nifty-alpha-low-volatility-30-etf); [Screener](https://www.screener.in/company/ALPHALOWVO/)
- **Small-cap momentum + quality.** NSE's Nifty Smallcap250 Momentum Quality 100 whitepaper reports a -72.4% max drawdown in COVID against -49% for the Smallcap 250, although it says the index had smaller drawdowns than its parent for most of its history. Small-cap factor portfolios can crash *harder* than the parent. — [NSE whitepaper 2024](https://www.niftyindices.com/docs/default-source/indices/nifty-smallcap250-momentum-quality-100/nifty-smallcap250-momentum-quality-100-whitepaper_2024.pdf?sfvrsn=2fd56e35_4)
- **Low vol + momentum combination (anecdotal, unverified).** A Reddit back-test (filter low-vol first, then rank by momentum) reports 14.61% CAGR against 14.01% for pure momentum, with about 21% lower volatility. — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1pmyk1u/snapshots/2025-12-15T06%3A31%3A43.54541Z)
- **Long-only quality.** Raju (SSRN 3490999) implements a systematic long-only quality strategy in India. Raju & Teli find quality and low-vol alpha survives costs with low turnover. — [SSRN 3490999](https://autopapers.ssrn.com/sol3/papers.cfm?abstract_id=3490999); [SSRN 4000418](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4000418)
- NSE launched Nifty500 Quality 50 and Nifty500 Low Volatility 50 in Dec 2024, a sign of product proliferation and crowding. — [Business Standard](https://www.business-standard.com/amp/markets/capital-market-news/nse-launches-two-new-strategy-indices-nifty500-quality-50-and-nifty500-low-volatility-50-124122300345_1.html)
- Indian factor fund AUM grew from under ₹15,000 cr (2022) to over ₹70,000 cr (end FY26), led by momentum and quality inflows (secondary blog). — [Creget](https://www.creget.com/blog/factor-investing-funds-india-2026)

### Inferences
- **Size.** The IIMA abstract places SMB well below momentum. I found no recent India evidence of a robust standalone size premium. In 2024–25 small-cap factor portfolios showed deeper crashes. Do not treat size as a return source; treat it as a risk exposure.
- **Value.** Strongly positive 2021–2024 and again in 2026, but negative relative to quality in 2020. It offered no 2008 protection. In India its returns concentrate in PSU and commodity cycles, so it is a regime bet with moderate evidence quality.
- **Diversification.** The calendar table shows quality and value nearly mirror each other (2020 vs 2021/2022/2023), and momentum's worst stretch (Sep 2024 to 2026) coincided with value leading. That supports a blend. Formal correlation coefficients were not found (gap).
- **Low vol and quality.** Expect them to cut drawdowns by about 7–11 pp against the Nifty in severe bears, with modest or near-zero excess return in strong beta rallies. Their long-run excess return over the cap-weighted index appears to be low single digits.

### Gaps
- No primary-source long-run CAGR (since 2005) for Nifty200 Quality 30, Nifty100 Low Vol 30, Nifty500 Value 50 or Alpha Low-Vol 30 against their parents. The factsheets could not be opened. **Pull these from the niftyindices.com factsheets before using any number.**
- No published pairwise factor correlation matrix for Indian factor indices was found.
- No full-year 2024/2025 calendar figures for quality, value or low vol.

---

## 3. Time-series trend / market-regime filters (200-DMA, 10-month SMA)

### Takeaway
I found no rigorous after-cost, after-tax evidence that index-level 200-DMA timing beats buy-and-hold on Nifty. The available India-specific evidence says it does not do so consistently. Its value is drawdown reduction, not excess return, which matches the repo's own hindcast (lower drawdown, about -3.7%/yr return).

### Cited Findings
- Kuvera's analysis finds the common 21-day/200-day SMA crossover "does not consistently beat a buy-and-hold strategy in the U.S. or India over the past 10 years or 5-year subperiods". Costs and taxes make it worse, and parameter sensitivity is a red flag for overfitting. — [Kuvera](https://kuvera.in/blog/promises-and-pitfalls-of-simple-moving-average-strategies/)
- US long-run evidence: the 200-DMA rule's edge is defensive. Without recessions and falling prices it is unlikely to beat buy-and-hold because of whipsaws. — [Quantified Strategies](https://quantifiedstrategies.substack.com/p/200-day-ma-strategy-backtest-rules-1bb)
- Practitioner momentum blogs test regime filters to reduce momentum drawdowns (results not extracted). — [Momo India](https://momoindia.substack.com/p/backtest-reducing-momentum-drawdowns)
- Academic evidence of risk-managed (vol-scaled) momentum in India reducing crash losses. — [Singh et al. 2022](https://ideas.repec.org/a/sae/fbbsrw/v11y2022i3p347-358.html)

### Inferences
- For a taxable Indian retail investor, an exit-to-cash trend filter on the whole portfolio crystallises STCG/LTCG and STT, then pays re-entry costs after whipsaws. Expect negative excess return after costs, offset by lower drawdown.
- The defensible use is as a *crash overlay on momentum specifically*: reduce momentum weight or tilt to low vol when the market is below its 200-DMA or market volatility is high. That targets the Daniel–Moskowitz crash state rather than timing beta. This is an inference; it is not tested on Indian data in the sources found.

### Gaps
- No peer-reviewed Indian study of a 10-month SMA or 200-DMA filter on Nifty TRI after costs and taxes. This needs an in-repo back-test (Nifty TRI, 1999–2026, with 0.1% STT each side plus tax).

---

## 4. Post-earnings announcement drift (PEAD), insider/promoter buying, delivery volume, and other India-specific anomalies

### Takeaway
The evidence is weak or mixed. PEAD appears mainly after *bad* news and in older samples. Insider-purchase abnormal returns exist in 2007–2015 disclosures, but I found no out-of-sample promoter-buying strategy study. Delivery-percentage signals have no credible academic support as a cross-sectional predictor. None should be a core engine; insider buying is at best a secondary tilt.

### Cited Findings
- **PEAD, mixed evidence:**
  - Gupta & Dhusia (2021; 100 NSE firms, 2014–2018, 1,130 events) find the market is efficient with respect to earnings announcements, with heterogeneity by liquidity. — [Trends Econ. & Mgmt](https://journals.vutbr.cz/index.php/trends/article/view/541)
  - A Nottingham event study finds efficient reaction to good news but negative drift lasting over a week after bad news, especially in the 2009–2010 bull market. — [Nottingham eprints](https://eprints.nottingham.ac.uk/26569)
  - IIMB work (Kudalkar & Chandra, 2014) describes PEAD lasting over 2 months and finds pre-announcement price moves. — [IIMB repository](https://repository.iimb.ac.in/handle/2074/20501); [IIMB 2013](https://repository.iimb.ac.in/handle/2074/17935)
- **Insider trading (legal disclosures):**
  - An NITK thesis (2018; BSE disclosures 2007–2015, four-factor event study) finds insider *purchase* portfolios earn positive abnormal returns and sales negative ones, and that outsiders mimicking them earn no significant abnormal returns. Insiders prefer large-cap, low B/M, high-momentum, low-P/E firms. — [NITK](https://idr.nitk.ac.in/handle/123456789/14150)
  - A Leap Journal blog (2026) finds no significant market reaction to SEBI insider-trading enforcement announcements. — [Leap blog](https://blog.theleapjournal.org/2026/05/market-reaction-to-insider-trading.html)
- **Bulk deals and delivery:**
  - On NSE in 2012–2021, volume and delivery percentage rise significantly before bulk deals, alongside large pre-event abnormal returns that suggest informed trading or front-running. This is not a tradable forward signal. — [NDL record](https://rcca.ndl.gov.in/items/4fbafa21-3191-40dd-8288-8fa6019189c0/full)
  - Delivery-percentage claims are broker heuristics. Heavy F&O activity mechanically lowers the ratio, which confounds cross-stock comparisons. — [Share.market](https://www.share.market/buzz/learn/stock-volume-technical-analysis/)
- **52-week high effect.** A study of the 52-week-high effect and momentum in India exists; the details were not extracted. — [ResearchGate](https://www.researchgate.net/publication/374825583_The_52-Week_High_Effect_and_Momentum_Investing_Evidence_from_India)
- **Enhanced momentum.** Sehgal, Pandey & Sen (2024, IJoEM) test whether enhanced momentum variants are more resilient in adverse conditions. — [Emerald](https://www.emerald.com/insight/content/doi/10.1108/IJOEM-09-2023-1518/full/html)

### Inferences
- The PEAD sample sizes are small and the conclusions conflict. Even where drift exists, it is concentrated in negative surprises, which a long-only investor can use only as an *exit or avoid* rule. That might help the repo's sell rules, but it is unproven.
- Insider or promoter purchases are the most plausible India-specific add-on, as a tie-breaker inside a momentum or quality shortlist. The evidence is a single 2007–2015 thesis, so expect a small effect, and SEBI PIT data cleanliness is an issue.
- I found no credible support for delivery volume.

### Gaps
- No analyst-revision (earnings momentum) study for India was found. Internationally this is a robust signal and it deserves a targeted search.
- No promoter-specific (as distinct from all-insider) or pledge-reduction study with out-of-sample tests.

---

## 5. Implementation survival: costs, taxes, impact, decay, crowding

### Takeaway
Long-only Indian factor premiums *are* reported to survive realistic brokerage and STT (Raju & Teli; Raju & Chandrasekaran). The biggest retail drags are short-term capital gains tax on high-turnover momentum and impact cost in the less-liquid names where much of the momentum premium lives. Crowding via ETFs and index funds has grown five-fold since 2022, and the Jun/Dec index rebalances now move about ₹16k cr.

### Cited Findings
- Long-only momentum, quality and low-vol alpha survive real-world costs; quality and low vol have low turnover. — [Raju & Teli SSRN 4000418](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4000418)
- Top-decile NIFTY100 momentum has about 32% monthly turnover and still shows about 10.7%/yr excess, which the authors judge implementable with discount brokers. — [Raju & Chandrasekaran](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3510433_code3354364.pdf?abstractid=3510433&mirid=1)
- Monthly momentum taxes: "25–30% average turnover … leads to 4% tax costs on 1% gains" (practitioner estimate). — [Raju on X](https://x.com/rajanraju26/status/1859091783231177157)
- **Liquidity dependence.** The less-liquid half of the momentum universe earned 19.4% net CAGR against 8.5% for the more-liquid half (hypothetical, unverified). — [freefincal](https://freefincal.com/is-indian-momentum-investing-just-a-liquidity-illusion/)
- **Crowding:**
  - Factor fund AUM grew from under ₹15k cr to over ₹70k cr (2022 to FY26). — [Creget](https://www.creget.com/blog/factor-investing-funds-india-2026)
  - The Dec 2025 rebalance of Nifty200 Momentum 30 moved about ₹16k cr. — [Business Standard](https://www.business-standard.com/amp/markets/news/nifty200-momentum30-a-flip-of-index-switch-jolts-16k-cr-across-the-grid-125121400388_1.html)

### Inferences
- **Rough cost arithmetic (assumptions; not sourced in this pass):**
  - STT is 0.1% on each side of a delivery trade. Add exchange, stamp and other charges of about 0.02–0.05% and midcap impact of about 0.1–0.3% per side.
  - At semi-annual 60–70% one-way turnover per rebalance (about 20 of 30 names), that is about 130% annual one-way turnover, or roughly 0.6–1.0%/yr in frictions.
  - STCG at 20% on realised short-holding gains adds a further drag. In a 20%-up year that could be 1.5–3 pp, partly deferrable by holding past 12 months for LTCG at 12.5%. These are my estimates.
- **Survival estimate.** Of a gross long-only momentum premium of about +4 pp/yr (NSE index), perhaps +1 to +3 pp/yr survives for a retail taxable account rebalanced semi-annually or quarterly. Monthly rebalancing likely surrenders most of the increment to tax.
- **Low vol and quality** turn over far less (about 20–40%/yr inferred), so most of their small premium survives.
- **Decay.** The post-2020 live record of momentum (2024–2026 drought) is consistent with crowding or decay, but also with a normal crash episode (as in 2008). The data cannot yet tell these apart.

### Gaps
- No primary STT, brokerage or impact-cost study for NSE midcaps was retrieved. Confirm current STT, STCG/LTCG rates and the ₹1.25 lakh LTCG exemption from official sources.
- No measured post-publication decay estimate for India.

---

## 6. What can add excess return to a concentrated 15–30 stock retail portfolio (monthly/quarterly rebalance)?

### Takeaway
A rules-based, vol-adjusted 6/12-month momentum ranking within a liquid large/mid universe (Nifty 200 or 500), with quality and low-vol screens and quarterly or semi-annual rebalancing with rank buffers, has the best evidence. It is essentially Nifty200 Momentum 30 with a quality and low-vol overlay. The repo's current risk-only rules (stops, trims) have no source of alpha. Expect long, painful relative drawdowns.

### Cited Findings
- The NSE index (30 stocks, semi-annual rebalance) earned about +4.1 pp/yr over the Nifty 200 from 2005 to 2026, so concentration at 30 names is consistent with the premium. — [NSE whitepaper 2026](https://www.niftyindices.com/docs/default-source/indices/nifty200-momentum-30/momentum-strategy-whitepaper_2026.pdf)
- Top-decile NIFTY100 momentum (about 10 stocks) earned about +10.7%/yr gross of tax. — [Raju & Chandrasekaran](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3510433_code3354364.pdf?abstractid=3510433&mirid=1)
- Quality, low-vol and multi-factor indices drew down less than the benchmark in the three worst drawdowns. — [S&P DJI](https://www.spglobal.com/spdji/en/documents/research/research-an-index-approach-to-factor-investing-in-india.pdf)

### Inferences — Ranked candidates for the repo (best evidence first)

Expected excess return is the plausible net-of-cost, pre-tax long-run range against Nifty 200 or Nifty 50 TRI. These are my estimates from the cited evidence, not sourced forecasts. The worst relative drawdown is the historical worst underperformance against the benchmark.

| Rank | Candidate | Evidence quality | Expected excess (net, long-run) | Worst historical drawdown / relative drawdown | Main failure regime |
|---|---|---|---|---|---|
| 1 | **Vol-adjusted 6m+12m momentum, top 20–30 of Nifty 200/500, semi-annual or quarterly rebalance with rank buffer** | High (IIMA 1993–2013 factors; NSE index 2005–2026; live funds since 2020; Raju long-only) | +1 to +4 pp/yr (gross index +4.1 pp; less costs and tax) | Absolute -70% (2008 back-test, about 65 months to recover). Relative to Nifty 50: about -16 pp in Sep 2024 to Apr 2025 (-31.8% vs -15.4%), with the fund still about 19% below its peak in Sep 2026 | Sharp V-shaped reversals and junk rallies (2009, 2020 rebound, 2021); rotation into value/PSU (2025–26); crowded rebalance dates |
| 2 | **Momentum + quality / low-vol overlay** (e.g., momentum ranked inside a quality- or low-vol-screened universe; Alpha Low-Vol 30 style) | Moderate-high (NSE multi-factor whitepaper, S&P BSE, Raju & Teli; combination evidence partly anecdotal) | +1 to +3 pp/yr, with lower volatility than pure momentum | Quality-momentum about -61.7% max drawdown (back-test). Relative drawdowns smaller than pure momentum (not quantified) | Strong beta or junk rallies where low-vol and quality lag (2021, 2023) |
| 3 | **Low volatility (Nifty100 Low Vol 30 style)** | High for risk reduction; moderate for return (Joshipura 25.5% long-short spread, 2000–2018; S&P BSE) | 0 to +2 pp/yr | Absolute -44.6% vs -55.1% for Nifty (back-test); 2008: -44.6% vs -51.8%. Lags in strong rallies (about -30 pp vs value in 2023: 31.9% vs 62.6%) | High-beta bull markets; rate-sensitive defensives sell-offs |
| 4 | **Quality / profitability (Nifty200 Quality 30 style)** | Moderate (Raju long-only quality; NSE; S&P BSE) | 0 to +2 pp/yr | 2008 about -50.8% vs -51.8% (little protection). Relative: 2021 -30 pp vs value (26.2% vs 56.4%); 2022 -27.6 pp vs value | Value/PSU/commodity booms; valuation de-rating of quality compounders (2022–2025) |
| 5 | **Value (Nifty500 Value 50 style)** | Moderate; strongly cyclical | 0 to +3 pp/yr, highly regime-dependent | 2008 about -52.6% (no protection). Lagged quality by about 18 pp in 2020 | Growth/quality-led markets; commodity downturns; PSU sentiment |
| 6 | **Insider/promoter purchases as a tie-breaker** | Low-moderate (single 2007–2015 thesis) | 0 to +1 pp/yr (inferred) | Unknown | Data noise; disclosure lags |
| 7 | **Index 200-DMA / 10-month trend exit** | Low for return (Kuvera: does not consistently beat buy-and-hold) | Negative to 0 after costs and tax; reduces drawdown | Lags in V-shaped recoveries (2020) | Whipsaw markets |
| 8 | **PEAD, delivery %, size** | Low or mixed | About 0 (possibly useful as a sell/avoid rule after bad earnings surprises) | n/a | — |

Design implications (inferred):
1. The engine must *rank and select*. Use a momentum core with quality and low-vol guardrails, not stops and trims on legacy holdings.
2. Rebalance quarterly or semi-annually with a rank buffer (e.g., buy in the top 20, hold until rank falls below 40), and avoid NSE's exact Jun/Dec dates to sidestep crowded flows.
3. Add a crash-state de-risk for momentum only: cut momentum weight when market drawdown or volatility is high or the index is below its 200-DMA. This is not market timing of the whole book.
4. Consider holding winners past 12 months where ranks allow, to convert STCG into LTCG.
5. Expect two or more consecutive years of underperformance, as in Sep 2024 to 2026. Set this expectation with the user up front, or the strategy will be abandoned at the bottom.

### Gaps
- Robust net-of-tax back-tests for a 15–30 stock retail implementation need to be run in-repo, with survivorship-free point-in-time Nifty 200/500 constituents.
- Verify all NSE index CAGR and drawdown figures from the official factsheets (WebFetch to niftyindices.com failed in this session).
