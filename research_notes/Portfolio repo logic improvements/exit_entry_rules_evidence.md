# Evidence on rule-based SELL / TRIM / ACCUMULATE triggers for a long-term Indian retail equity portfolio

Research date: 2026-10-14. Method note: several primary-source hosts (dspace.mit.edu, alphaarchitect.com, cxoadvisory.com, niftyindices.com, quantpedia.com) could not be fetched from this environment (DNS failure), so a number of findings below rely on search-engine abstracts/summaries of those sources rather than full-text reads. This is flagged where it matters. Most rigorous stop-loss / trend-filter evidence is **US-only**; Indian evidence is thinner and mostly index-level or momentum-factor-level.

Repo context checked: `/home/user/Portfolio/signal_engine.py` currently fires "STRG SELL" on a single print `current_price <= invalidation_price`, and also "STRG SELL" for "Below 200 DMA structural breakdown" when return is negative and conviction < 4; trailing stop = max(invalidation, 52w-high − N·ATR) → TRIM half; overextension (>25% above 50-DMA) → TRIM.

---

## 1. Do stop-loss and trailing-stop rules help long-term holders of single stocks (vs indices)?

### Takeaway
Theory and evidence say stops only add value when returns are positively autocorrelated (momentum/regime persistence); under a random walk they always lower expected return. On large samples of individual US stocks, tight stops underperform buy-and-hold after costs. Wide stops roughly match buy-and-hold on a risk-adjusted basis by cutting downside volatility. Stops look strong mainly as an overlay on *momentum portfolios*, and even there the results are sensitive to implementation.

### Cited Findings
- Kaminski & Lo, "When do stop-loss rules stop losses?" (Journal of Financial Markets, 2014). Under the Random Walk Hypothesis, simple 0/1 stop-loss rules *always decrease* expected return. With momentum (positive serial correlation) they can add value. On US futures data 1993–2011 at monthly frequency, some volatility-based stop rules raised monthly returns by ~1.5% and substantially cut volatility (search summary of the paper; full text not fetched) — [MIT DSpace record](https://dspace.mit.edu/entities/publication/bb69ca4b-0cdc-487f-831d-63b2e84fafee); [PDF](https://dspace.mit.edu/bitstream/handle/1721.1/114876/Lo_When%20Do%20Stop-Loss.pdf). Note that the empirical test is on asset-class futures (a stock/bond switch), not single stocks.
- Lo & Remorov, "Stop-loss strategies with serial correlation, regime switching, and transaction costs" (MIT, ~2015/2017). On a large sample of individual US stocks, **tight stop-loss strategies underperform buy-and-hold in a mean-variance framework because of excessive trading costs**. Outperformance is possible only for stocks with sufficiently high serial correlation, and downside-risk reduction is "not substantial" — [MIT DSpace 1721.1/107017](https://dspace.mit.edu/handle/1721.1/107017).
- CXO Advisory's summary of the same paper (US stocks 1964–2014): *wide* stops checked over 10-day intervals matched buy-and-hold risk-adjusted performance through lower downside volatility. *Tight daily* stops underperformed because of trading costs and **negative short-horizon autocorrelation** in single stocks. Very large bid-ask spreads tend to come with crashes. **Delaying execution by one day** worked marginally better than immediate execution, and significantly better for tight stops, because prices revert during the delay — [CXO Advisory](https://www.cxoadvisory.com/equity-premium/stop-losses-on-stock-positions-in-depth) (via search summary).
- Trailing stop-loss study (AUT/Massey). The downside-risk-reduction benefit of trailing stops **disappears for stops tighter than 10% once transaction costs are included**, driven by turnover and by costs that rise in declines — [ACFR/AUT](https://acfr.aut.ac.nz/research/using-trailing-stop-loss-rules-to-reduce-risk); [Massey repository](https://mro.massey.ac.nz/handle/10179/16877).
- Han, Zhou & Zhu, "Taming Momentum Crashes: A Simple Stop-Loss Strategy" (2014). Data: the top-decile 6-month momentum portfolio of US stocks, 1926–2011, with any stock sold if it fell 10% below its start-of-month price. The equal-weighted worst monthly loss fell from −49.79% to −11.34%, and the value-weighted from −65.34% to −23.69%. Average returns and Sharpe ratios "more than doubled" — [Alpha Architect review](https://alphaarchitect.com/2016/08/taming-the-momentum-roller-coaster-fact-or-fiction/); [Seeking Alpha summary](https://seekingalpha.com/article/3257295-momentum-and-stop-losses). Alpha Architect's review (title "fact or fiction") questions how implementable this is: it needs daily monitoring of every position and is hard for average investors. Its replicated figures differ slightly (−64.97% to −23.28%) — same sources.
- Odean (1998, Journal of Finance). Retail investors sell winners too early and hold losers too long (the disposition effect). Winners that were sold went on to outperform the losers that were held, so the behaviour lowers returns, "particularly for taxable accounts". Secondary sources put the gap at ~2–3 pp over the following year, but those figures are unverified — [Odean paper page](https://faculty.haas.berkeley.edu/odean/papers/disposition/disposition.html); [Business Today summary](https://www.businesstoday.in/magazine/investment/story/disposition-effect-14954-2010-12-24).

### Inferences
- A rule that **sells on a single close below a price level** is exactly the "tight, immediate-execution" case that Lo & Remorov found loses money on single stocks, because single stocks show short-horizon *reversal*, not continuation. The planned "3 consecutive closes" confirmation and the evidence that a one-day delay helps both point the same way. Indian evidence of short-term reversal (Section 4) strengthens the case.
- Stops look best when the asset trends (futures, indices, momentum portfolios). A long-term, conviction-based single-stock portfolio is the setting where stops add the least. For a multi-year holder, price breaches are better used as **review triggers** than as automatic sells.
- The "trim one third when gain ≥ 50% and ≥ 30% below 52-week high" rule is a wide trailing stop (30%). That is in the range where the evidence says stops are roughly neutral on a risk-adjusted basis. It is not clearly harmful, but it is not clearly value-adding either, and in India it creates a tax event (Section 5 / tax notes).
- Trimming on overextension (>25% above 50-DMA) means selling strength. It runs against the momentum and disposition-effect evidence. No supporting evidence was found.

### Gaps
- No Indian (NSE single-stock) study of stop-loss or trailing-stop rules was found.
- Full text of Kaminski & Lo and Lo & Remorov was not retrievable here. The parameter-level results (best stop width, re-entry rules) could not be verified.
- No study was found that tests "price-based invalidation levels set by the investor" specifically.

---

## 2. 200-DMA / 10-month trend filters in India; hysteresis and confirmation bands

### Takeaway
The 10-month / 200-day trend filter is well supported for **indices and asset classes** (mostly US and global data), where it lowers drawdowns and often raises Sharpe ratios but usually lowers raw returns because of whipsaws. Indian studies of moving-average rules on Nifty/Sensex find predictive ability that is often eroded by costs. There is little evidence for applying it to single stocks as a sell rule, and no rigorous India-specific evidence on confirmation bands was found.

### Cited Findings
- Faber, "A Quantitative Approach to Tactical Asset Allocation" (Journal of Wealth Management). A 10-month SMA filter (≈200-day) on US stocks, foreign stocks, bonds, REITs and commodities cut volatility and drawdowns while keeping competitive returns. Asset classes only, no single stocks, no India — [R-bloggers summary](https://www.r-bloggers.com/mebane-faber-tactical-asset-allocation-in-r/); [TradingView GTAA description](https://www.tradingview.com/script/pFE8Udyy-Mebane-Faber-GTAA-5).
- Zakamulin (S&P Composite 1860–2009). All MA timing rules produce many false signals in both bull and bear markets but tend to beat the market in bear states. Mean returns are below buy-and-hold while Sharpe ratios are generally higher. The median optimal lookback is about 5–7 months. A rebuttal paper argues that a widely cited strong result came from look-ahead bias, and the corrected performance is only marginally better than buy-and-hold — [SSRN 2677212](https://papers.ssrn.com/abstract=2677212); [Alpha Architect review](https://alphaarchitect.com/the-moving-average-research-king-valeriy-zakamulin/); [CXO](https://www.cxoadvisory.com/technical-trading/market-timing-with-moving-averages-over-the-very-long-run).
- Clare, Seaton, Smith & Thomas. A trend rule (price vs a 6/8/10/12-month MA) applied across asset classes gave "substantial improvement in risk-adjusted performance" over buy-and-hold. In commodity futures, the trend filter's marginal impact "far outweighs" momentum or risk-parity adjustments. These are not single-stock tests — [City Research Online](https://openaccess.city.ac.uk/id/eprint/17846/); [IDEAS](https://ideas.repec.org/a/eee/finana/v31y2014icp1-12.html).
- S&P 500 200-DMA since 1951: risk-adjusted returns improved, but price return underperformed the index — [Seeking Alpha](https://seekingalpha.com/article/4020451-s-and-p-500-moving-average-strategies-since-1951-evidence-from-backtesting). A practitioner backtest notes that outside recessions, "you are unlikely to beat buy-and-hold because of the many whipsaws" (commercial site, lower quality) — [Quantified Strategies](https://quantifiedstrategies.substack.com/p/200-day-moving-average-trading-strategy-87a).
- India, Mitra (2011, Quantitative Finance). MA rules on four Indian index series captured direction and gave significant gross returns, but **real-world transaction costs prevent investors from capturing them** — [IDEAS](https://ideas.repec.org/a/taf/quantf/v11y2011i2p287-297.html).
- India, Sundhar & Kakani (XLRI working paper, 2006). Simple and displaced MAs on Nifty, Sensex and individual stocks, 1991–2005. The displaced MA was profitable after costs. This is an older working paper and its peer review is not confirmed — [PDF](https://c.mql5.com/forextsd/forum/214/Profiting%20from%20Technical%20Analysis%20in%20Indian%20Equity%20Market%20-%20Using%20Moving%20Averages.pdf).
- India, Gunasekarage & Power (2001), as cited in a review. Indian index MA rules had predictive ability, but India was the weakest of the South Asian markets tested — [Virtus review](https://virtusinterpress.org/IMG/pdf/10-22495cocv11i2c5p6.pdf).
- India, Muruganandan (2020), BSE Sensex 2000–2018. RSI lost money before costs. MACD sell signals beat the mean in bear phases, but risk-adjusted returns were weak, and the author doubts that consistent abnormal returns are possible — [Colombo Business Journal](https://mgmt.cmb.ac.lk/cbj/?p=1280).
- Nifty below its 200-DMA for 100 sessions: commentary (not a backtest) says the duration alone does not determine future returns — [Equentis](https://www.equentis.com/blog/nifty50-marks-100-days-below-200-dma-what-does-it-mean-for-investors/). Stable Investor's 2011 charts of Nifty distance-from-200-DMA vs 3- and 5-year forward CAGR exist, but their numbers could not be extracted — [Stable Investor](https://stableinvestor.com/2011/11/analysis-of-returns-on-investment-based.html).

### Inferences
- The 200-DMA is defensible as a **portfolio/index-level risk regime indicator** and as a **REVIEW flag** for single stocks. It is weak as an automatic single-stock SELL. The current code path "Below 200 DMA structural breakdown → STRG SELL" is the least evidence-backed rule in the engine.
- The planned REVIEW rule (>3% below 200-DMA for 20+ trading days) is a sensible hysteresis design: a percentage band plus a time filter is the standard whipsaw reducer in MA practice. However, I found no source quantifying the optimal band or duration for NSE. The parameters below are judgement calls aligned with the monthly (10-month) evaluation cadence that Faber and Zakamulin use.
- Evaluating trend monthly (month-end close vs 10-month SMA) rather than daily is the closest match to the published evidence and naturally cuts whipsaw.

### Gaps
- No peer-reviewed study of a 200-DMA filter on **individual NSE stocks** with modern (post-2010) data and costs was found.
- No quantitative evidence on optimal band width (e.g., 2% vs 3% vs 5%) or day-count confirmation for Indian markets was found.
- No official NSE/academic study of Nifty forward returns conditional on being above or below the 200-DMA was retrievable.

---

## 3. Momentum and 52-week-high effects in India — should ACCUMULATE favour strength?

### Takeaway
Cross-sectional momentum (6–12-month returns) is well documented in India and is the basis of the NSE's flagship momentum index. Nearness to the 52-week high is a strong momentum proxy in US data, but it was found weak in emerging-market *indices*. On balance, the evidence favours adding to holdings that show relative strength (trend intact, near highs) over adding on 200-DMA pullbacks. Momentum comes with severe crash risk; the 2024–25 Indian drawdown is an example.

### Cited Findings
- Nifty200 Momentum 30 methodology. It picks the top 30 of the Nifty 200 by a "Normalised Momentum Score" built from **6-month and 12-month price returns adjusted for daily return volatility**. Weight is free-float market cap × score, capped at min(5%, 5× the cap weight). Constituents must be F&O-listed with ≥ 1 year of listing. It rebalances **semi-annually (June/December)** — [NSE factsheet](https://www.niftyindices.com/Factsheet/Factsheet_Nifty200_Momentum30.pdf). An NSE 2026 whitepaper reports that quarterly rebalancing adds ~20–50% more annual churn, while the semi-annual framework shows a slight performance edge over longer periods (via search summary; PDF not fetchable) — [NSE momentum whitepaper 2026](https://www.niftyindices.com/docs/default-source/indices/nifty200-momentum-30/momentum-strategy-whitepaper_2026.pdf).
- Reconstitutions are large: about 20 changes in June 2025 and 19 in December 2025 — [Business Standard Jun-2025](https://www.business-standard.com/amp/markets/stock-market-news/nifty200-momentum-30-index-to-see-20-stock-changes-on-june-27-125062600872_1.html); [Business Standard Dec-2025](https://www.business-standard.com/amp/markets/news/nifty200-momentum30-a-flip-of-index-switch-jolts-16k-cr-across-the-grid-125121400388_1.html).
- Momentum crash risk in India. Nifty200 Momentum 30 index funds had max drawdowns of about −27% to −30% (peak Sep/Oct 2024 → trough 14-Mar-2025), the worst 1-year rolling return was about −21% (window ending Sep-2025), and they had not regained their peaks by Aug-2026 — [Arthgyaan HDFC fund page](https://arthgyaan.com/fund/hdfc-nifty200-momentum-30-index-fund-direct-growth/152430); [Arthgyaan Baroda fund page](https://arthgyaan.com/fund/baroda-bnp-paribas-nifty200-momentum-30-index-fund-direct-growth/152931); [Curious Investing Insights](https://curiousinvestinginsights.substack.com/p/momentum-or-mayhem-unpacking-the).
- Indian academic momentum evidence:
  - Momentum strategy robust in India over 2000–2013 (Garg & Varshney, Global Business Review 2015).
  - Strong momentum profits over 1995–2006 that CAPM and Fama-French do not explain, with a behavioural explanation favoured.
  - Short-term momentum plus long-term overreaction (reversal) on NSE over 1997–2013.

  Sources (via search summaries): [Emerald: "Momentum anomaly: evidence from India"](https://emerald.com/insight/content/doi/10.1108/03074351211193730/full/html); [NSE research paper](https://nsearchives.nseindia.com/content/research/res_paperfinal223.pdf); [IIMB repository](https://repository.iimb.ac.in/handle/2074/18321?mode=full); [publishingindia](https://publishingindia.com/storage/PDFBrochures/3029.pdf).
- George & Hwang (2004, Journal of Finance), US 1963–2001. Nearness to the 52-week high explains a large share of momentum profits and **dominates past-return measures** for forecasting. Short-term momentum and long-term reversal are largely separate effects — [SUFE newsletter abstract](https://academicnewsletter.sufe.edu.cn/info/361244). Malin & Bornholt (2010) found the 52-week-high strategy **unprofitable in emerging-market indices** and weaker there than standard momentum — [NAU experts / related](https://experts.nau.edu/en/publications/the-52-week-high-and-momentum-investing-in-international-stock-in/); [CFA FAJ 2023, Momentum Crashes and the 52-Week High](https://rpc.cfainstitute.org/research/financial-analysts-journal/2023/momentum-crashes-and-the-52-week-high).
- India 52-week-high: a QuantInsti/Quantpedia out-of-sample test on Indian stocks (2014–2017) of the Hong–Jordan–Liu industry 52-week-high strategy exists, but its results could not be retrieved — [Quantpedia](https://quantpedia.com/an-analysis-of-52-weeks-high-effect-on-indian-stocks/).

### Inferences
- The engine's ACCUMULATE "buy zone" (close within ±5% of the 200-DMA) selects stocks whose 6–12-month momentum is fading, so their momentum rank is falling. That is the opposite of what the Indian momentum index rewards. The repo's own forward-return scoring (ACCUMULATE averaging −6% at 20 days) is consistent with this. Note that 20 days is a short horizon and the sample is small, so that result is suggestive, not conclusive.
- A better ACCUMULATE condition is relative strength: positive 6- and 12-month returns (volatility-adjusted) vs the Nifty 500/benchmark, a price above a rising 200-DMA, and within ~15–20% of the 52-week high. Momentum can crash, so this should be paired with position caps (already in the engine) rather than unlimited adding.
- The semi-annual NSE cadence and its low-churn finding support evaluating ACCUMULATE monthly or quarterly rather than daily.

### Gaps
- No peer-reviewed India-specific 52-week-high single-stock study with results was retrieved.
- The official Nifty200 Momentum 30 index-level return and drawdown series (vs Nifty 200) was not retrieved; the figures above are fund-level.

---

## 4. "Buy the dip near the 200-DMA" vs "buy strength"; mean reversion in Indian large/mid caps

### Takeaway
India shows **short-term (≈1-month) reversal** and **long-term (1–3-year) reversal**, sandwiched around **intermediate (3–12-month) momentum**. A pullback to the 200-DMA in an otherwise strong stock sits in an ambiguous zone. Pure dip-buying is supported mainly at very short horizons after large moves in liquid stocks. For multi-year adds, strength/trend is better supported than proximity to the 200-DMA.

### Cited Findings
- Parthasarathy & Sendilvelu (2022). Large, liquid Indian stocks show significant reversals for up to six months after large monthly declines *and* increases. Bigger shocks were followed by bigger reversals, and the abnormal returns after large declines may be economically significant — [CEEOL](https://ceeol.com/search/article-detail?id=1054639).
- Indian 1-1 (one-month formation/holding) winner-loser portfolios show return reversals for all combinations (1991–2006 sample; authorship unclear) — [publishingindia](https://www.publishingindia.com/storage/PDFBrochures/2481.pdf).
- Losers outperform prior winners over 1–2-year formation periods (Saji, 2023) — [Inderscience](https://inderscience.com/filter.php?aid=132959).
- University of Nottingham dissertation (2000–2020): at 1-month horizons only 5 of 12 anomalies predict returns, and momentum and reversal coexist — [Nottingham eprints](https://eprints.nottingham.ac.uk/66413).
- Jegadeesh–Titman baseline (as summarised in Indian studies): momentum pays over 3–12-month holding periods, contrarian strategies over 1–3 years — [NSE research paper](https://nsearchives.nseindia.com/content/research/res_paperfinal223.pdf); [publishingindia](https://publishingindia.com/storage/PDFBrochures/3029.pdf).

### Inferences
- Short-term reversal argues against *selling* on a fresh sharp drop (sell-the-low risk) and for confirmation delays. It is a weaker argument for *buying* the dip for a multi-year holder, because the reversal gains are short-lived and accrue mostly to traders.
- "Within ±5% of the 200-DMA while 50-DMA > 200-DMA" is a mid-trend pullback. If kept at all, it should require that relative strength over 6–12 months is still positive. The pullback should be judged against a *rising* 200-DMA, not just a crossover state.
- Long-term (1–3-year) reversal is a caution against concentrating adds in stocks that have already multi-bagged. That supports the existing position-cap TRIM, which is size discipline, over price-based trims.

### Gaps
- No study was found that directly compares "buy near 200-DMA" vs "buy near 52-week high" entry rules on NSE stocks.
- Large-cap vs mid-cap differences in Indian reversal/momentum strength were not quantified in the retrieved sources.

---

## 5. Distinguishing "price fell" from "thesis broken"; price as a review vs sell trigger

### Takeaway
The evidence (random-walk result for stops, negative short-horizon autocorrelation in single stocks, the disposition effect, and Indian tax drag) supports using price breaches as **REVIEW triggers that force a fundamental re-check**, with SELL reserved for documented thesis failure or a confirmed, severe breach. Taxes in India make unnecessary round-trips especially costly within 12 months.

### Cited Findings
- Under a random walk, stop-loss rules always reduce expected return; they add value only with momentum or regime persistence — [Kaminski & Lo](https://dspace.mit.edu/entities/publication/bb69ca4b-0cdc-487f-831d-63b2e84fafee).
- Tight stops on single stocks lose to buy-and-hold after costs. Negative short-horizon autocorrelation and wide spreads during crashes work against stops — [Lo & Remorov](https://dspace.mit.edu/handle/1721.1/107017); [CXO summary](https://www.cxoadvisory.com/equity-premium/stop-losses-on-stock-positions-in-depth).
- Retail investors' selling decisions lower returns, especially in taxable accounts — [Odean](https://faculty.haas.berkeley.edu/odean/papers/disposition/disposition.html).
- Indian tax (from 23-Jul-2024, reportedly unchanged through Budget 2026): listed-equity **STCG is 20%** for holdings ≤ 12 months, and **LTCG is 12.5%** on gains above **₹1.25 lakh per FY**, with no indexation. Surcharge and cess are extra — [Outlook Money](https://www.outlookmoney.com/news/budget-2024-25-ltcg-raised-to-125-what-it-means-for-you); [DSP AMC](https://www.dspim.com/knowledge-hub/personal-finance-guide/capital-gains-filing-in-india-what-to-report-where-and-how/stcg-and-ltcg-rules-in-india); [5paisa](https://www.5paisa.com/blog/evolution-of-ltcg-stcg-tax-in-india).

### Inferences
- A practical "thesis broken" checklist: earnings/ROE deterioration across 2+ quarters, a broken guidance or capital-allocation promise, governance events, or a structural industry change. Price should *open* the case, and fundamentals should *close* it.
- Tax drag: a TRIM of a position with a 50% gain realises tax of about 12.5% on the gain (LTCG) or 20% (STCG). For a held-for-<12-months winner, a one-third trim on a 50% gain costs about 0.2 × 0.5 × 1/3 ≈ 3.3% of the original position value, before re-entry slippage. Trims should prefer lots that are > 12 months old, and annual LTCG harvesting up to ₹1.25 lakh is a free benefit.
- Single-close invalidation SELLs combine all three documented harms: whipsaw from short-term reversal, selling near lows when spreads are wide, and tax realisation.

### Gaps
- No empirical study of "investor-defined invalidation prices" was found.
- No Indian retail-account study of the disposition effect with performance outcomes was retrieved.

---

## Recommended rule changes for the repo

Parameters marked (J) are judgement calls consistent with the cited evidence but not directly optimised in any found study. Indian single-stock evidence is thin, so treat these as defaults to backtest with `backtest/` and `signal_scorer.py` using ≥ 60/120/250-day forward returns, not 20-day.

1. **Invalidation SELL (signal_engine.py lines ~131–132): replace the single-print trigger.**
   - Day 1 close ≤ invalidation → **REVIEW (INVALIDATION WATCH)**, not SELL.
   - **SELL** only if either (a) **3 consecutive daily closes** ≤ invalidation, or (b) a **weekly close** ≤ invalidation, or (c) a single close ≥ **10% below** invalidation (the gap-down/catastrophe case). This is consistent with Lo & Remorov's delayed-execution finding (J for the exact counts).
   - Use closing prices only, never intraday or broker LTP, for the SELL path. The broker-fallback path should also downgrade to REVIEW.
2. **Remove "Below 200 DMA structural breakdown → STRG SELL"** (signal_engine.py ~line 186). Convert it to **REVIEW** using the planned hysteresis: close > **3% below** the 200-DMA for **≥ 20 trading days** (J), or a month-end close below the 10-month SMA, Faber-style. Exit REVIEW only after the close is **≥ 2% above** the 200-DMA (asymmetric band → hysteresis, J). Escalate to SELL only if REVIEW persists for **≥ 60 trading days** *and* a fundamental flag (ROE decline or thesis_status ≠ intact) is present.
3. **Trailing profit protection (TRIM ⅓ at gain ≥ 50% and ≥ 30% below 52w high): keep it, but widen it and make it tax-aware.**
   - Keep the 30% drawdown-from-high threshold. The evidence shows trailing stops < 10% are cost-destructive, while ~30% is in the roughly neutral zone. Prefer **max(30%, 3 × 1-year daily-vol-scaled ATR)** so that volatile mid/small caps are not stopped by noise (J).
   - Require a **month-end** confirmation, not intraday.
   - Fire it only on lots held **> 12 months** where possible (LTCG 12.5% vs STCG 20%). Otherwise defer, or show as "TRIM WATCH (STCG)".
   - The current "TRIM half on ATR trailing stop" is more aggressive than this and should be aligned to ⅓.
4. **Overextension TRIM (> 25% above 50-DMA): drop it, or demote it to an informational "EXTENDED – don't add" flag.** No evidence supports selling strength, and momentum/disposition evidence argues against it. Concentration control should come from the existing **position cap (8%) and sector cap (25%)**, which are size-based and evidence-neutral. If kept, raise it to **> 40% above the 200-DMA** and only when the position weight is > cap (J).
5. **ACCUMULATE: switch from "buy-the-dip near 200-DMA" to "buy strength with the thesis intact".** Proposed conditions (all required):
   - thesis intact and price above invalidation;
   - **price > 200-DMA and 200-DMA rising** (200-DMA today > 200-DMA 20 days ago);
   - **positive volatility-adjusted 12-month and 6-month returns**, mirroring the Nifty200 Momentum 30 score: return/annualised σ. Optionally require relative strength vs Nifty 500 > 0 over 6 months;
   - price **within 20% of the 52-week high** (J; George–Hwang proximity, US evidence);
   - not "EXTENDED" (≤ 25% above the 50-DMA) and weight < cap.

   Evaluate **monthly** (or at most weekly), not daily, consistent with the NSE semi-annual-rebalance finding that lower churn did slightly better.
   - Optional "quality pullback" variant: allow a small add when price is 5–15% below a *recent* 52w high with 12-month momentum still positive. Do **not** add when price is at or below a flat or falling 200-DMA.
6. **ETFs vs stocks.** For broad index ETFs (Nifty 50/Next 50/500), a Faber-style **month-end 10-month SMA** rule is the best-supported trend filter. Even there, use it to pause new contributions or flag REVIEW, not to liquidate, because Indian MA-rule gains are eroded by costs (Mitra 2011) and the rule mainly reduces drawdowns rather than raising returns. Do not apply single-stock invalidation logic to diversified ETFs.
7. **Scoring/validation.** Re-score the signals at **60, 120 and 250 trading days**, plus max adverse excursion. Benchmark them against "do nothing", and report the after-tax result (20%/12.5%, ₹1.25 lakh exemption). A 20-day horizon sits inside the documented 1-month reversal window and will systematically mis-rate long-horizon rules.
