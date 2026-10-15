# Signal Hit Rates: Which Market Signals Beat a Coin Flip for Indian Equities

> Method note: In this session WebFetch failed for every domain (DNS errors: indexpe.in, niftyindices.com, freefincal.com, arxiv.org). Every finding below comes from search-engine summaries of the cited pages, not from reading the full text. Treat exact figures as "reported by the source, not independently checked against the original table". Numbers from my background knowledge that I could not re-source this session are labeled **[UNVERIFIED – background knowledge]** and appear only under Inferences or Gaps.

## Valuation signals (Nifty P/E, P/B, earnings yield vs bond yield, market-cap-to-GDP) vs subsequent 1/3/5/7-year returns

### Takeaway
In India, Nifty P/E bands shift the *level* of medium-term (3–7-year) forward returns: cheap starting points have had roughly twice the median 5-year CAGR of expensive ones. But even from the most expensive band, 5-year returns were rarely negative, and at 1 year valuation is close to useless. The Indian sample is small (P/E data since 1999, about one or two independent cycles), and NSE changed the P/E basis in April 2021, so these results are in-sample descriptions, not validated out-of-sample forecasts.

### Cited Findings
- **Nifty 50 P/E bands (indexpe.in, data since 1999, dividends reinvested):** The cheapest 20% of days (P/E < 17.3) had a median 3-year forward return of +28.06% and a 5-year median of +23.56%. The most expensive 20% (P/E > 23.9) had a 3-year median of +14.61% and a 5-year median of +13.40%. The worst 3-year outcome was negative in every band, reaching −15.22% in the most expensive band. — [indexPe: PE ratio vs future returns, 27 years](https://indexpe.in/pe-vs-forward-returns)
- The same site reports sector results the same way. Nifty IT in P/E band 1 of 5 had a 5-year median of +23.49%/yr, positive in 100% of 1,321 overlapping windows. Nifty Realty in band 3 had +7.33%/yr, positive in 67% of 539 windows. Nifty Bank in band 2 had +17.54%/yr, positive in 100% of 725 windows. The windows overlap heavily, so the real number of independent observations is far smaller. — [indexPe Nifty IT](https://www.indexpe.in/nifty-it); [indexPe Nifty Realty](https://www.indexpe.in/nifty-realty); [indexPe Nifty Bank](https://www.indexpe.in/nifty-bank)
- **Capitalmind (2017):** At a Nifty P/E of about 23, the historical average forward return was −10% at 1 year, −1.89% annualised at 3 years, 6.94% annualised at 5 years, 12.12% annualised at 7 years and 13.44% annualised at 10 years. The author warns that P/E data only starts in 1999, so "it's really been one earnings cycle." — [Capitalmind: Nifty's PE and how returns have historically come](https://premium.capitalmind.in/2017/02/niftys-pe-and-how-returns-have-historically-come-around-from-here/)
- **Methodology break:** In April 2021 NSE moved the Nifty P/E from standalone to consolidated earnings, so the current P/E "is not directly comparable" to the pre-2021 series. Any historical P/E-to-return mapping "can not directly be applied" to today's P/E. — [Capitalmind Nifty PE ratio page](https://premium.capitalmind.in/nifty-pe-ratio/)
- **arXiv multi-scale study (Nifty 50, 1990–2024):** It reports a 5-year negative-return probability of 0 for the P/E 24–25 band and 0.03 for 25–26. A secondary summary of the paper says P/E > 27 carried a 1-year loss probability of about 40–50% and breakeven periods of more than 6 years. The high-P/E bands have small samples. — [arXiv 2509.00697](https://arxiv.org/pdf/2509.00697); [Pith summary](https://pith.science/paper/2509.00697)
- **Freefincal counterpoint:** Negative 3-year returns occurred across P/E levels of roughly 16–20, not only above 22, and averages hide a wide spread. — [Freefincal: Misconceptions about the Nifty PE](https://freefincal.com/misconceptions-about-the-nifty-pe/)
- **Unconditional base rate:** Nifty 50 TRI rolling returns over 1999–2023 had a minimum 5-year return of about −1%, and the probability of a negative 5-year return was "close to nil" whatever the valuation. — [BasuNivesh](https://www.basunivesh.com/how-much-returns-to-expect-from-nifty-50/)
- **Bond yield / earnings yield gap (India):** A CLSA analysis says most Nifty tops came when the bond yield minus earnings yield was about 2 percentage points. It also says 1- and 2-year returns were muted whenever the gap exceeded 1.5 points. This is a brokerage rule of thumb with no disclosed statistics. — [Business Standard: Mind the gap](https://www.business-standard.com/amp/markets/news/mind-the-gap-as-g-sec-and-nifty-earnings-yield-enters-danger-zone-123071600355_1.html)
- A DSIJ article on BEER (bond-equity earnings yield ratio, 25 years of daily data) reports a "clear, monotonic" link in which lower BEER goes with stronger forward returns. The excerpt gives no coefficients. — [DSIJ: BEER vs Buffett](https://insights.dsij.in/dsijarticledetail/beer-vs-buffett-decoding-indias-most-reliable-valuation-signal-53982)
- Over 15 years, the correlation between the US Treasury yield and the Nifty P/E multiple averaged about −0.4. This measures the multiple, not forward returns. — [Business Standard](https://www.business-standard.com/amp/article/markets/higher-bond-yields-in-the-us-led-to-lower-nifty-p-e-shows-data-121022700035_1.html)
- **Market-cap-to-GDP (India):** I found no forward-return backtest, only levels. The ratio was about 103% at the 2008 peak and about 55% in FY09. It was 56% in March 2020, about 112% in 2021-22, and about 100% in 2022 against a long-term average of about 81%. — [Business Standard 2012](https://www.business-standard.com/amp/article/markets/india-s-market-cap-to-gdp-indicate-valuations-at-historical-low-112101303013_1.html); [Business Standard 2022](https://www.business-standard.com/article/markets/india-s-market-cap-to-gdp-at-100-versus-long-term-average-of-81-122060500887_1.html)
- **Global evidence:**
  - Goyal, Welch & Zafirov (Review of Financial Studies 2024, 37(11), data to end-2021) tested 29 predictors published after 2008. More than a third were no longer significant even in-sample, and half of the remainder did poorly out-of-sample; only a handful still worked. The original 2008 paper found none would have helped a real-time investor beat the historical mean. — [SFI summary](https://sfi.ch/en/publications/a-comprehensive-2022-look-at-the-empirical-performance-of-equity-premium-prediction); [Ivo Welch](https://book.ivo-welch.info/home/card-eqpredict.html)
  - A later paper reports that most of these models produce "negative or barely positive out-of-sample R²." — [arXiv 2312.05593](https://arxiv.org/pdf/2312.05593)
- **CAPE and the Fed model (global):**
  - PGIM finds that 1/CAPE minus the real 10-year yield ("excess CAPE yield") gave the best 10-year estimates among the models it tested, consistently since 2003. — [PGIM: Using CAPE to estimate future returns](https://www.pgim.com/us/en/borrower/insights/asset-class/multi-asset/multi-asset-solutions/using-cape-to-estimate-future-stock-returns)
  - A January 2026 paper (Rui Ma et al.) reports out-of-sample R² above 50% for 10-year returns using a refined CAPE construction. This is a single new paper. — [Capital Spectator, Feb 2026](https://www.capitalspectator.com/2026/02/20/)
  - A BI thesis found the Fed model did better than CAPE at the 1-year horizon out-of-sample. — [BI Open](https://biopen.bi.no/bi-xmlui/handle/11250/2477121)

### Inferences
- Valuation is a usable **expected-return-level** signal at 5–10 years and a weak one at 3 years. It is a coin flip at 1 year.
- In India, "expensive" has historically meant about 13% CAGR instead of about 23% over 5 years, not losses. The probability of a positive 5-year return was high (roughly 95–100%) in every band, so valuation should change allocation tilts, not trigger exits.
- **[UNVERIFIED – background knowledge]** For the US, Shiller CAPE in-sample R² for 10-year real returns is often cited at about 0.4–0.5, and for 1-year returns about 0.0–0.1. Out-of-sample R² is lower, and Goyal-Welch-style tests often show it negative at short horizons.
- Even within India, overlapping windows inflate the apparent precision. With about 25 years of P/E data there are only about 5 non-overlapping 5-year periods.

### Gaps
- I could not open the indexpe tables to get 1- and 7-year band statistics, or to compute "probability of a positive 5-year return when P/E > 24 vs < 16" directly. From the excerpts, it appears to be near 100% for both on this sample. That is unverified.
- I found no Indian study reporting R² of P/E (or P/B) against 1/3/5-year Nifty returns. I also found no out-of-sample test.
- I found no backtest of market-cap-to-GDP as a predictor in India.
- I could not verify AMC valuation-based allocation research (ICICI Pru, Edelweiss balanced advantage models). Their hit rates are not public in the results I found.

## Volatility predictability (GARCH / clustering, India VIX)

### Takeaway
Risk is forecastable even though direction is not. Volatility is highly persistent. Next month's realised volatility is strongly correlated with this month's (about 0.8 in one US measurement). GARCH(1,1) is competitive for Nifty and India VIX, and adding implied volatility (VIX) to GARCH improves forecasts of Nifty realised volatility.

### Cited Findings
- **Range-based measure, S&P 500:** The following month's average daily range is about 80% correlated with the prior month's (blog analysis, not peer-reviewed). — [Daily Speculations](https://dailyspeculations.com/wordpress/?p=3941)
- **S&P 500 realised variance, 1970–2017:** Autocorrelation decays as a power law at first, then exponentially with a time constant of about 120 days. That implies strong persistence at monthly horizons. — [arXiv 1906.02306](https://arxiv.org/pdf/1906.02306)
- **Indian market (Physica A 2018):** Found evidence of persistence in monthly realised volatility. — [IDEAS/RePEc](https://ideas.repec.org/a/eee/phsmap/v492y2018icp343-359.html)
- **Rajvanshi, Santra & Basu (IIM Calcutta WPS 797):** GARCH models augmented with implied volatility gave the best forecasts of Nifty realised volatility on MAE and RMSE. — [IIMC WPS 797](https://studentlive.iimcal.ac.in/sites/all/files/pdfs/wps_797.pdf)
- **Naik & Reddy (2021):** GARCH(1,1) beat TGARCH and EGARCH in forecasting India VIX, which shows high volatility persistence. — [IDEAS](https://ideas.repec.org/a/asi/aeafrj/v11y2021i3p252-262id2072.html)
- **Kumar, Kumar & Sharma (2022):** Past volatility had a stronger effect on future India VIX than ARCH shocks (daily data, 2008–2017). — [Inderscience](https://www.inderscience.com/filter.php?aid=123777)
- **Banerjee & Kumar (IIMC WPS 688)** studied how India VIX relates to realised volatility. The search excerpt gave no numbers. — [IIMC WPS 688](https://studentlive.iimcal.ac.in/sites/all/files/pdfs/wps_688.pdf)

### Inferences
- Volatility forecasts are usable for position sizing, volatility targeting and setting expectations.
- **[UNVERIFIED – background knowledge]** Implied volatility (VIX or India VIX) typically exceeds subsequent realised volatility, a variance risk premium, so VIX is a biased but informative forecast. HAR-RV models typically reach R² of about 0.5–0.7 for next-period realised variance in developed markets.
- High volatility does not reliably predict direction. Volatility persistence and return unpredictability coexist.

### Gaps
- I found no India-specific published coefficient for monthly realised-volatility autocorrelation, or for the R² of India VIX regressed on subsequent 30-day Nifty realised volatility. This could be computed from NSE data.

## Trend / time-series momentum at index level

### Takeaway
Time-series momentum (TSMOM) is one of the few signals with long, multi-asset, partly out-of-sample support. Its value is mainly drawdown reduction and crisis convexity, not a high win rate. On a single index, simple moving-average rules capture direction but often lose much of the edge after costs and whipsaw, and can lag buy-and-hold for years.

### Cited Findings
- **Moskowitz, Ooi & Pedersen (2012):** Found significant time-series momentum in each of 58 liquid futures (equity indices, currencies, commodities, bonds). Returns persist for 1–12 months and partially reverse at longer horizons. — [SSRN: Time Series Momentum](https://papers.ssrn.com/abstract=2089463)
- **Hurst, Ooi & Pedersen, "A Century of Evidence on Trend-Following":** Positive returns in every decade since about 1880/1903, with low correlation to traditional assets. Most large 60/40 drawdowns unfolded over about 15 months, giving trend signals time to react. — [AQR](https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing)
- **S&P 500 200-day moving-average rule, monthly, 1960 onward:** CAGR 6.45% vs 7% for buy-and-hold (ex-dividends), with a maximum drawdown of 28%. In other words, lower return but much smaller drawdowns. — [Quantified Strategies](https://quantifiedstrategies.substack.com/p/trend-following-strategy-in-s-and-33c)
- A Seeking Alpha / ETFreplay analysis says a single-index trend rule beat SPY buy-and-hold after 1999 but "can substantially underperform over several years." — [Seeking Alpha](https://seekingalpha.com/article/4241434-how-to-beat-the-market-in-the-long-run-with-trend-following-strategies)
- **India, Mitra (2011, Quantitative Finance):** Moving-average rules on four Indian indices "capture the direction of market movements reasonably well" with significant gross returns, but "these returns cannot be exploited fully due to real world transaction costs." — [IDEAS](https://ideas.repec.org/a/taf/quantf/v11y2011i2p287-297.html)
- A Zerodha study ran trend-following tests on Nifty spot for January 2015 to October 2025 (8 EMA and Supertrend). The figures were not shown in the excerpt. — [Zerodha](https://aftermarketreport.zerodha.com/p/nifty-trims-losses-with-200-point)

### Inferences
- **[UNVERIFIED – background knowledge]** Trend-following systems typically win only about 35–45% of trades, with average wins several times average losses. A low hit rate is normal for a profitable trend system, so "hit rate" is the wrong metric here.
- Expect a TSMOM or moving-average filter on Nifty to reduce the probability and depth of large (>30%) drawdowns. Also expect it to lag in V-shaped recoveries (for example March 2020) and in choppy markets.

### Gaps
- I found no published India index-level TSMOM hit rate, average win/loss, or drawdown-reduction probability. A CJFA paper on time-series vs cross-sectional momentum in India exists, but its results were not visible in the excerpt. — [CJFA 2020](https://apcz.umk.pl/CJFA/article/view/CJFA.2020.018)

## Cross-sectional momentum and other factors (Indian factor indices)

### Takeaway
Factor tilts, especially momentum, have very high probabilities of beating Nifty 200 over 5+ year rolling windows: about 98% for momentum (largely backtested). Over 1 year this falls to about 63–79%, and year-to-year it is far from certain. Quality beat in about 9 of 14 years. Factors go through multi-year droughts and lose together in some months.

### Cited Findings
- **Nifty200 Momentum 30 (NSE whitepaper, data to August 2020):** Beat Nifty 200 on 98.3% of 5-year daily rolling windows. The same table reportedly shows 100% for 7 and 10 years and about 79% for 1 year. Most of this period is a back-test (the index launched in 2020). — [NSE Momentum 30 whitepaper](https://www.niftyindices.com/docs/default-source/indices/nifty200-momentum-30/nifty200_momentum_30_index_whitepaper_sep_20.pdf)
- Another review puts momentum's 1-year rolling hit rate vs Nifty 200 at about 63%. — [PrimeInvestor](https://primeinvestor.in/reports/prime-review-which-passive-factor-index/) / [Curious Investing Insights](https://curiousinvestinginsights.substack.com/p/momentum-or-mayhem-unpacking-the)
- A Motilal Oswal deck shows momentum beating its comparison on 98.5% of 5-year rolling periods. — [Motilal Oswal presentation](https://www.motilaloswalmf.com/CMS/assets/uploads/Documents/c51b5-motilal-oswal-nifty-200-momentum-30-etf-index-fund-presentation-rd-28-02-2023.pdf)
- A UTI-linked analysis says the index beat Nifty 50 on 95% of rolling 5-year windows, averaging about 13 percentage points a year more, but it "takes a hit during corrections or flat markets." — [Morningstar India](https://morningstar.in/posts/66398/nfo-mosl-nifty200-momentum-30-etf-index-fund.aspx)
- **Nifty200 Quality 30:** Beat Nifty 200 in 9 of 14 calendar years (2005–2018), a hit rate of about 64%. — [NSE Quality 30 whitepaper](https://archives.nseindia.com/content/indices/NIFTY200_Quality30_Whitepaper_Final.pdf)
- **Low volatility (2009–2024):** "Strong defensively" but often in the bottom two during bull runs. — [Momentum Lab / Curious Investing summaries](https://momentumlab.substack.com/p/factor-this-october-2024)
- **ICICI Securities, July 2007 to December 2022:** Momentum, Quality and Low Vol all lagged Nifty 200 together in 30 months. — [ICICI Sec multifactor PMS deck](https://www.icicisecurities.com/PMS_PDF/PMS_ISec_Multifactor_Portfolio.pdf)
- HDFC AMC notes that momentum indices can see larger drawdowns than the market. — [HDFC MF](https://www.hdfcfund.com/learn/deep-dives/tuesday-talking-point/momentum-factor-long-term-outperformer)

### Inferences
- Long-window factor hit rates (95–100%) are partly backtest artefacts: index design was chosen with hindsight, and there are few independent 5-year periods. Live performance since 2020 includes the sharp 2024–25 momentum drawdown, which these backtests do not capture.
- Momentum has a usable long-horizon edge but a weak one at 1 year (about 63–79%). Monthly win rates vs the market are likely only modestly above 50%. **[UNVERIFIED]**

### Gaps
- I did not find monthly win-rate figures (% of months beating Nifty 200) for NSE factor indices, or post-launch live hit rates to 2026. The whitepapers predate launch.

## Macro / global signals (FII flows, US drawdowns, crude, USD-INR, US yields, yield-curve inversion)

### Takeaway
Evidence that macro variables predict Indian equity returns out-of-sample is weak. FII flows mostly *follow* returns rather than lead them. US yields correlate with the Nifty *multiple* rather than reliably forecasting returns. Yield-curve inversions predicted most US recessions but with long, variable lags and false positives, and forward equity returns after inversion have been close to normal.

### Cited Findings
- **FII flows, Indian Granger-causality studies:** Several (mostly on pre-2010 data) find that FIIs "chase" returns. Causality is either bidirectional, with impulse responses showing flows are return-driven, or runs from returns to flows. Results vary by index and period. — [IUP India IJAF](https://www.iupindia.in/305/IJAF_Foreign_Institutional_Investment_16.html); [Emerald](https://www.emerald.com/insight/content/doi/10.1108/17554191211274794/full/html); [Publishing India GJRIM](https://publishingindia.com/archive/gjrim/effect-of-fiis-and-foreign-exchange-on-indian-stock-market)
- **US yields:** The correlation between the US 10-year yield and Nifty P/E has averaged about −0.4 over 15 years. This is contemporaneous and affects the multiple; it is not a forecast. — [Business Standard](https://www.business-standard.com/amp/article/markets/higher-bond-yields-in-the-us-led-to-lower-nifty-p-e-shows-data-121022700035_1.html)
- **Yield-curve inversion:**
  - 7 of 9 inversions (78%) preceded US recessions, with false signals in 1966. One source counts inversions before 7 of the last 8 recessions. Lead times run 7–24 months, or 9–30 months with an average of 16.5. — [Advisor Perspectives](https://www.advisorperspectives.com/commentaries/2019/03/26/blue-red-and-grey-yield-curve-inversions); [Counterpoint Funds](https://counterpointfunds.com/how-and-when-to-look-for-a-recession/)
  - Counterpoint lists 1998 and 2006 as seemingly false signals in which stocks did well. — [Counterpoint Funds](https://counterpointfunds.com/how-and-when-to-look-for-a-recession/)
  - The 2022–23 inversion, the longest on record, had not been followed by a recession as of late 2025. — [YCharts](https://get.ycharts.com/resources/blog/yield-curve-inversion-2025/)
- **S&P 500 after inversions:** 1-year returns ranged from −15.3% to +37.1%, averaging 10.9%, roughly the normal range. Over 18 months, returns were positive after 6 of 10 inversions and negative after 4. — [Dollars and Sense](https://dollarsandsense.sg/inverted-yield-curve-mean-theres-recession-coming-investors-now/); [Greenleaf Trust](https://greenleaftrust.com/news/how-to-think-about-last-years-inverted-yield-curve/)
- **Global predictor survey:** Most published return predictors fail out-of-sample (see Goyal-Welch-Zafirov above). — [SFI](https://sfi.ch/en/publications/a-comprehensive-2022-look-at-the-empirical-performance-of-equity-premium-prediction)

### Inferences
- FII flow data is coincident or lagging. As a forward signal for Nifty it is roughly a coin flip.
- Inversion is a weak-to-moderate recession signal and a coin flip for 1-year equity direction.
- **[UNVERIFIED – background knowledge]** Crude oil and USD-INR are contemporaneously correlated with Nifty moves but have no robust out-of-sample forecasting record in the literature I am aware of.

### Gaps
- I found no out-of-sample test (OOS R² or hit rate) for crude, USD-INR, US-drawdown spillovers or US yields as predictors of Nifty forward returns. Post-2015 Indian FII causality studies were not retrieved.

## Short-term signals (technical patterns, news sentiment, analyst targets, tips, trading)

### Takeaway
Short-horizon signals are at best marginal before costs and are generally coin-flips or worse after them. Analyst 12-month price targets are met at the horizon only about 26–38% of the time and are optimistic by about 15%. Over 91% of individual Indian F&O traders lose money.

### Cited Findings
- **Muruganandan (2020), Sensex, 2000–2018:** RSI rules failed to earn positive returns even before costs. A MACD sell signal beat the mean in bear markets, but before costs, and Sharpe ratios did not compensate for the risk. — [Colombo Business Journal](https://cbj.sljol.info/articles/56)
- **Mitra (2011):** Moving-average rules have significant gross returns that "cannot be exploited fully" after transaction costs. — [IDEAS](https://ideas.repec.org/a/taf/quantf/v11y2011i2p287-297.html)
- **Weaker, non-peer-reviewed sources claiming profits after costs:** An XLRI working paper (displaced moving average) and a 2006 Nottingham dissertation. — [Nottingham eprints](https://eprints.nottingham.ac.uk/20281)
- **Analyst targets:**
  - Bradshaw & Brown (1997–2002, about 100k targets): prices were at or above target at 12 months only 26% of the time, and touched the target at some point in 35% of cases. — [CXO Advisory](https://www.cxoadvisory.com/investing-expertise/do-stocks-ever-hit-analyst-target-prices)
  - Bradshaw, Brown & Huang (Review of Accounting Studies 2013, 2000–2009): 38% met at 12 months and 64% at some point. Implied returns exceeded actual returns by 15% on average, with a mean absolute error of 45%. — [IDEAS](https://ideas.repec.org/a/spr/reaccs/v18y2013i4d10.1007_s11142-012-9216-5.html)
- **SEBI F&O studies:** 91.1% of individual F&O traders lost money in FY24, with an average loss of ₹1.20 lakh. 93% lost over FY22–24 (aggregate losses above ₹1.8 lakh crore). In FY25 net losses rose to ₹1,05,603 crore, with more than 91% losing. — [Value Research](https://www.valueresearchonline.com/stories/222075/sebi-report-91-per-cent-f-o-traders-lost-money-in-fy-24); [Business Standard](https://www.business-standard.com/markets/news/net-losses-of-traders-in-fo-widens-in-fy25-sebi-study-125070701221_1.html); [Moneylife](https://moneylife.in/article/77613.html)

### Inferences
- For retail investors, short-term technical and tip-based signals perform worse than a coin flip after costs. The SEBI data is the most direct Indian evidence.
- **[UNVERIFIED – background knowledge]** SEBI's 2023 intraday study reported about 70% of individual intraday cash traders losing money in FY23. The search did not confirm this.

### Gaps
- I found no Indian study of measured news-sentiment hit rates, or of "tip" or Telegram-channel accuracy.

## Recession / crash prediction track records

### Takeaway
Economists' recession forecasts have a very poor record: consensus forecasts flagged only about 5 of 153 recessions a year ahead. Probability models such as the yield curve do better on recessions but have long, variable lags and false positives, and do not translate into reliable equity timing.

### Cited Findings
- **An, Jalles & Loungani (2018), 153 recessions in 63 countries, 1992–2014:** Only 5 were predicted by the consensus of private-sector economists by April of the preceding year. Forecasters also badly missed the magnitude. — [vLex: How well do economists forecast recessions?](https://international.vlex.com/vid/how-well-do-economists-855661849)
- **Loungani's earlier work:** 2 of 60 recessions were predicted a year ahead. Loungani has said "the record of failure to predict recessions is virtually unblemished." The popular "only 2 of 150" version is attributed to him in secondary sources. "148 of 150" is a rephrasing and unverified. — [BNN Bloomberg](https://www.bnnbloomberg.ca/why-are-economists-so-bad-at-forecasting-recessions-1.1250945); [Cobden Centre](https://www.cobdencentre.org/?p=21367)
- **Yield curve:** About 78% of inversions preceded recessions, with variable 7–30-month lags. The 2022–23 inversion had produced no recession as of late 2025. — [Advisor Perspectives](https://www.advisorperspectives.com/commentaries/2019/03/26/blue-red-and-grey-yield-curve-inversions); [YCharts](https://get.ycharts.com/resources/blog/yield-curve-inversion-2025/)

### Inferences
- Recession calls are close to a coin flip at best (in practice worse, since recessions are usually missed). Crash-timing based on them carries a high opportunity cost.

### Gaps
- I found no India-specific recession or crash-forecast track record, and no false-positive rate for India crash models.

---

## Signal league table

All verdicts are conditional on the caveats above. "OOS?" means whether there is out-of-sample or live evidence.

| Signal | Horizon | Measured strength (hit rate / R² / conditional) | OOS? | Verdict |
|---|---|---|---|---|
| Volatility persistence (this month's realised vol → next month's) | 1 day – 3 months | About 0.8 month-to-month correlation (S&P range measure); GARCH and GARCH+IV best for Nifty RV | Yes (forecast-evaluation studies) | **Usable** (for risk and sizing, not direction) |
| India VIX → future realised vol | 1 month | Improves GARCH forecasts (IIMC); biased upward | Partly | **Usable** (risk) |
| Nifty P/E band → forward return level | 5–7 years | Cheapest quintile median 5-yr about 23.6% vs about 13.4% for the most expensive; negative 5-yr outcomes rare in all bands | No (in-sample, about 1–2 cycles, 2021 method break) | **Usable but weak**: tilts expected return, not the sign |
| Nifty P/E band | 3 years | Median 28% vs 14.6%; worst case negative in every band | No | **Weak** |
| Nifty P/E band | 1 year | Capitalmind: P/E 23 → −10% average, but wide dispersion; global 1-yr R² about 0 [UNVERIFIED] | No | **Coin-flip** |
| Earnings yield minus bond yield (India) | 1–2 years | Brokerage rule: muted returns when gap > 1.5 pp; no statistics | No | **Weak / unverified** |
| Excess CAPE yield / CAPE (global) | 10 years | Best 10-yr model per PGIM; new paper OOS R² > 50% (single study); in-sample R² about 0.4 [UNVERIFIED] | Partly | **Usable** (long horizon only) |
| Market-cap-to-GDP (India) | 3–5 years | No backtest found | No | **Unproven** |
| Goyal-Welch predictor set (dividend yield, term spread, etc.) | 1 month – 1 year | Most have negative or barely positive OOS R² | Yes | **Coin-flip** |
| Time-series momentum / trend (multi-asset) | 1–12 months | Positive in every decade for over 100 years; trade win rate likely <50% [UNVERIFIED]; cuts drawdowns | Yes (long history, post-publication) | **Usable** (drawdown control) |
| 200-DMA on a single index (S&P / Nifty) | Months | S&P: CAGR 6.45% vs 7%, maxDD 28%; India: gross edge eroded by costs | Partly | **Weak** (risk reducer, not return enhancer) |
| Nifty200 Momentum 30 vs Nifty 200 | 5-yr rolling | 98.3% (backtest to 2020) | Mostly backtest | **Usable**, with a backtest haircut |
| Momentum vs Nifty 200 | 1-yr rolling | About 63–79% | Mostly backtest | **Weak** |
| Quality 30 vs Nifty 200 | Calendar year | 9 of 14 years (about 64%) | Mostly backtest | **Weak-to-usable** |
| Low volatility vs Nifty 200 | Calendar year | Wins in down years, lags in bull runs | Partly | **Weak** (regime-dependent) |
| FII flows → Nifty | Days – months | Flows mostly follow returns (Granger) | No | **Coin-flip** |
| US 10-yr yield → Nifty | Months | −0.4 correlation with P/E (contemporaneous) | No | **Coin-flip** for returns |
| Yield-curve inversion → recession | 7–30 months | About 78% hit rate (7/9), recent miss in 2022–23 | Yes (real time) | **Weak** |
| Yield-curve inversion → equities | 12–18 months | 1-yr S&P return after inversion averaged +10.9%; 6/10 positive at 18 months | Yes | **Coin-flip** |
| Crude / USD-INR → Nifty | Months | No OOS evidence found | No | **Coin-flip** (unproven) |
| Technical rules (RSI, MACD, short MAs), India | Days – weeks | RSI negative even before costs; MA gross gains eroded by costs | Yes | **Coin-flip or worse after costs** |
| Analyst 12-month price targets | 12 months | 26–38% met at horizon; 15% optimistic bias | Yes | **Worse than coin-flip** |
| Retail F&O / short-term trading (proxy for tips) | Intraday – weeks | More than 91% of individuals lose (SEBI FY24, FY25) | Yes (population data) | **Worse than coin-flip** |
| Economists' recession forecasts | 1 year | 5 of 153 predicted (about 3%) | Yes | **Worse than coin-flip** (misses) |
