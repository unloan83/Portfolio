# Portfolio Construction, Sizing and Rebalancing for an Indian Retail Long-Term Equity Portfolio

Context: 34 holdings (~₹6.75L); top 10 = 71%; 14 holdings < 1% each; energy+power ~29% across 12 names; PSU ~19.5%; gold+silver ETFs 12.4%; index ETFs (Nifty 50, Nifty Bank, Nifty IT, Smallcap 250, Midcap 150) overlap direct stocks (HDFC Bank, Reliance, Wipro). Current repo rules (config.py / risk_manager.py): max 8% per position, 25% per sector (Financials grouped), ATR sizing risking 0.5% per trade, max_open_positions = 15, 2x ATR stop, 3x ATR trailing stop. Research date: 14 Oct 2026. Note: spglobal.com could not be fetched directly (DNS failure); SPIVA figures below come from search-result extracts of the S&P primary page.

## 1. Optimal number of holdings and retail over-/under-diversification

### Takeaway
Classic literature puts adequate diversification for a randomly chosen equal-weight stock portfolio at ~10-15 (Evans & Archer) to 30-40 (Statman) names, with later work wider still; but what matters is *effective* diversification (correlations and weights), not the count. The current portfolio has 34 line items but is effectively concentrated (top 10 = 71%, 12 correlated energy/power names), while 14 sub-1% "tail" positions add attention cost without meaningful diversification.

### Cited Findings
- Evans & Archer (1968) simulated random portfolios 1958-67 and concluded the benefit of adding securities beyond roughly ten was questionable — [Kiplinger summary](https://kiplinger.com/investing/stocks/604724/how-many-stocks-should-you-have-in-your-portfolio); [Kellogg practicum report](https://kellogg.northwestern.edu/faculty/jagannathan/teaching/practicum/2004/files/Final-Reports/DiversificationBenefits.pdf)
- Statman (1987) argued a well-diversified portfolio of randomly chosen stocks needs at least 30 stocks (borrowing investor) to 40 (lending investor), benchmarked against the alternative of a low-cost index fund — [Financial Services Review article](https://openjournals.libs.uga.edu/fsr/article/download/3710/3191)
- Later literature splits into camps: 20-30 stocks, 60-80, and "200+"; answer depends on benchmark, costs, and whether volatility or terminal-wealth dispersion is measured; diversification depends more on stock volatility than count — [WealthManagement / Advisor Perspectives "Volatility Matters More Than Size"](https://www.advisorperspectives.com/articles/2022/11/26/diversifying-volatility-matters-more-than-size); [Strawman forum review](https://strawman.com/forums/topic/6846)
- Goetzmann & Kumar (40,000+ US discount-broker accounts, 1991-96): most individual investors were under-diversified; they diversified "naively" — adding stocks without regard to correlations among them; least-diversified group earned ~2.40%/yr lower risk-adjusted return than most-diversified — [NBER w8686](https://www.nber.org/papers/w8686); [Review of Finance 2008 record](https://ideas.repec.org/p/nbr/nberwo/8686.html)
- Campbell, Ramadorai & Ranish (Indian retail equity accounts): experienced investors hold better-performing portfolios, have lower turnover and smaller disposition effect; under-diversification, turnover and disposition bias diminish after investors experience poor returns from them — [NBER w20000](https://www.nber.org/papers/w20000.pdf); [Harvard draft](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/campbell/files/gettingbetterfeelingbetter_1dec2014.pdf). Secondary summary: oldest-cohort accounts outperformed newest by ~0.2-0.4%/month 2002-2011 (unverified against paper) — [CXO Advisory](https://www.cxoadvisory.com/individual-investing/individual-investor-learning)
- SEBI study (Jul 2024, FY23 equity cash segment): 71% of individual intraday traders made net losses; loss-makers traded more and their trading costs were ~57% of trading losses — [SEBI press release](https://www.sebi.gov.in/media-and-notifications/press-releases/jul-2024/sebi-study-finds-that-7-out-of-10-individual-intraday-traders-in-equity-cash-segment-make-losses_84948.html); [Business Standard](https://www.business-standard.com/markets/news/over-70-intra-day-traders-incur-losses-during-fy23-reveals-sebi-study-124072401110_1.html)

### Inferences
- The portfolio exhibits Goetzmann-Kumar "naive diversification": many tickers, but 12 energy/power names plus PSU overlap behave as one bet. Count-based rules (max_open_positions = 15) are less informative than an effective-N metric (1/Σw², and a correlation-adjusted version).
- For a ₹6.75L portfolio, 14 sub-1% positions (each < ₹6,750) cannot move outcomes and generate monitoring cost; a minimum meaningful weight (e.g., 2%) or explicit "exit/consolidate" rule is justified.
- A sensible target for the direct-stock sleeve is ~12-20 stocks, given that index ETFs already provide broad diversification (Statman's 30-40 figure assumes stocks are the whole portfolio; with an index core, the satellite can be more concentrated).
- SEBI evidence on trading costs supports low-turnover rules (bands, min trade size), even though it concerns intraday traders, not long-term holders.

### Gaps
- No SEBI study found specifically on number of stocks held/diversification of Indian demat holders; the 2024 study concerns intraday traders only.
- No India-specific replication of Evans-Archer/Statman found within the search budget.

## 2. Conviction-weighted vs equal-weight vs risk-parity sizing; is ATR sizing appropriate for long-term holders?

### Takeaway
Equal weight (1/N) is a very hard baseline to beat out-of-sample because estimated inputs (expected returns, convictions) are noisy; inverse-volatility/risk-parity weights do not consistently beat equal weight either. Conviction weighting is defensible only as a modest tilt around equal weight with hard caps. ATR-per-trade risk sizing (0.5% risk, 2x ATR stop) is a trading-system construct; for long-term holdings it should be replaced by volatility-aware *weight caps*, not stop-loss-based share counts.

### Cited Findings
- DeMiguel, Garlappi & Uppal (RFS 2009): of 14 optimisation models across 7 datasets, none consistently beat 1/N on Sharpe ratio, certainty-equivalent return or turnover; estimation error offsets optimisation gains; mean-variance would need ~3,000 months of data to beat 1/N with 25 assets, ~6,000 months with 50 — [IDEAS/RePEc](https://ideas.repec.org/a/oup/rfinst/v22y2009i5p1915-1953.html); [LBS](https://london.edu/faculty-and-research/academic-research/o/optimal-versus-naive-diversification-how-inefficient-is-the-1n-portfolio-strategy-p7805)
- Tu & Zhou argue some strategies can beat 1/N in settings other than a pure one-factor model — [SMU](https://ink.library.smu.edu.sg/lkcsb_research/1106)
- Equal-risk-contribution and inverse-volatility portfolios do not consistently outperform equal weight, though they often match or surpass it — [BI Norwegian Business School thesis 2023](https://biopen.bi.no/bi-xmlui/handle/11250/3095282)
- Clare, Motson & Thomas (US 1963-2011): inverse-volatility indexes returned 11.4-11.5% vs 9.4% for cap-weight (gross; vs cap-weight, not equal weight) — [CXO Advisory](https://www.cxoadvisory.com/strategic-allocation/performance-and-risk-of-equity-strategy-indexes/)
- Low-volatility anomaly (since Haugen & Heins 1972): high-volatility stocks not rewarded with commensurately higher returns; low-vol lags in fast rallies and outperforms in sharp falls — [BNP Paribas AM](https://www.bnpparibas-am.com/portfolio-perspectives/the-low-volatility-anomaly-still-going-strong-after-50-years/); [Eastspring](https://eastspring.com/insights/the-low-volatility-anomaly-examining-the-evidence)
- Dimensional critique: non-price weighting schemes (equal, inverse-vol, etc.) can produce large uncontrolled deviations and excess turnover — [Dimensional](https://www.dimensional.com/chmedia/148303/source/ce-credit-on-demand_weighting-for-the-right-one-weighting-scheme-design-for-systematic-equity-portfolios.pdf) (vendor source)

### Inferences
- Planned conviction ladder (5→8%, 4→5%, 3→3%, 2→1.5%) is a 5.3x spread between top and bottom tiers; given 1/N evidence, a narrower spread (e.g., 1.5x-2x around an equal base) is more robust to conviction errors. A conviction-2 holding at 1.5% is effectively a "watchlist" position — better rule: conviction ≤ 2 → exit/no add, rather than hold at 1.5%.
- Use volatility as a *cap modifier*: high-vol (e.g., smallcap/PSU/commodity) names get a lower max weight (e.g., cap × min(1, median_vol / stock_vol)), which approximates risk-budgeting without full optimisation.
- ATR 0.5%-risk sizing implies position size = 0.5% × equity / (2 × ATR). For a stock with ATR ~2.5% of price, that is 0.5/5 = 10% weight — but for high-vol names it gives tiny weights; and it presumes a stop that a long-term holder will not execute. Keep ATR logic only for an explicitly tactical sleeve.

### Gaps
- No India-specific study comparing equal vs conviction vs risk-parity weighting for retail found.
- No direct evidence on accuracy of retail "conviction scores".

## 3. Rebalancing: calendar vs threshold bands, band widths, cash-flow rebalancing

### Takeaway
Vanguard finds no optimal frequency/threshold; risk-adjusted returns are similar across monthly/quarterly/annual, while costs rise with frequency. Its default: monitor annually or semi-annually and rebalance when drift exceeds ~5 percentage points (asset-class level). Daryanani's opportunistic rebalancing: check frequently (~every 2 weeks) but trade only when a relative band (~20% of target weight) is breached, and trade only the out-of-band assets. In India, taxes (STCG 20% < 12 months; LTCG 12.5% above ₹1.25L/yr) strongly favour rebalancing with new cash and harvesting within the LTCG exemption.

### Cited Findings
- Vanguard (1926-2009 US data): no optimal rebalancing frequency or threshold; risk-adjusted returns not meaningfully different across monthly/quarterly/annual, but number of rebalancing events and costs rise with frequency; annual/semi-annual monitoring with ~5% drift threshold gives reasonable risk-control/cost balance; annual preferred when taxes/costs are material — [Vanguard 2010 Best Practices](https://indexacapital.com/bundles/unaiadvisor/docs/papers/2010-Vanguard-Best-practices-for-portfolio-rebalancing.pdf?v=241); [AAII summary](https://aaii.com/journal/article/best-practices-for-portfolio-rebalancing); [Vanguard research summary on tuning frequency](https://corpaemdisp.essp.c1.vanguard.com/content/corporatesite/us/en/corp/articles/tuning-frequency-for-rebalancing.html)
- Smaller thresholds → lower tracking error but higher transaction cost — [Vanguard ISGPORE](https://www.financieelonafhankelijkblog.nl/wp-content/uploads/2021/11/Vanguard-ISGPORE.pdf)
- Daryanani (J. Financial Planning, 2008) "Opportunistic Rebalancing": rebalance frequency is a function of how often you look; with a 20% band, rebalance benefit rose from ~0.16% (250-day look) to ~0.38-0.39% (5-10 day look); 0% band (pure calendar) had negative benefit at short intervals — [Kitces webinar handout reproducing Table 3](https://kitces.com/wp-content/uploads/2016/11/An-In-Depth-Look-At-Optimal-Rebalancing-Strategies-Webinar-Handouts.pdf)
- Practitioner implementation: wider bands, biweekly evaluation, trade only out-of-balance assets; 20% band → 2-3 trades/yr vs 10% band → 5-10 trades/yr — [Yeske Buie "Two Week Look"](https://yebu.com/economy-investing/the-two-week-look-systematic-rebalancing); [FA Mag](https://www.fa-mag.com/news/optimal-rebalancing-with-tolerance-bands-29623.html?page=2)
- Caveat: a separate backtest found annual rebalancing beat 20% bands for leveraged funds; results may not generalise — [Risk Parity Chronicles](https://riskparitychronicles.substack.com/p/does-threshold-rebalancing-work-with)
- India tax (from 23 Jul 2024, unchanged in Budgets 2025/2026 per sources): listed equity LTCG 12.5% above ₹1.25L/FY exemption (holding > 12 months), STCG 20% — [DSP MF guide](https://www.dspim.com/knowledge-hub/personal-finance-guide/capital-gains-filing-in-india-what-to-report-where-and-how/stcg-and-ltcg-rules-in-india); [5paisa](https://www.5paisa.com/blog/evolution-of-ltcg-stcg-tax-in-india). Gold/silver ETFs are equity-oriented? — sources say non-equity assets (gold) use a 24-month threshold with 12.5% LTCG — [5paisa](https://www.5paisa.com/blog/evolution-of-ltcg-stcg-tax-in-india)

### Inferences
- Planned "+2% absolute tolerance" is too tight for small weights (a 1.5% target with +2pp band can grow to 3.5%, +133%) and too loose-ish relative to nothing for large ones. Use a hybrid band: max(absolute floor, relative %) e.g. trim only when weight > target × 1.25 AND > target + 1.5pp (Daryanani's ~20-25% relative band, plus an absolute floor so tiny positions don't trigger trades).
- Hard caps (e.g., 10% single stock) should still trigger action regardless of band.
- Before any sell: prefer directing new cash/SIP and dividends to underweights; when selling, prefer lots held > 12 months and stay within the ₹1.25L LTCG exemption per FY where possible; flag STCG (20%) trims as needing a higher threshold.
- Look frequency: tool can evaluate weekly/biweekly (cheap) but should only emit trade suggestions on band breach.

### Gaps
- No India-specific rebalancing backtest (with STT, brokerage, STCG) found.
- Full Daryanani paper not accessed; figures from Kitces' reproduction.

## 4. Concentration risk beyond sector labels: risk groups and ETF look-through

### Takeaway
Sector labels understate risk when names share a common driver (state ownership/government policy, commodity prices, interest rates). Indian PSU stocks fall together sharply (e.g., Nifty PSE −16.4% on 4 Jun 2024 vs Nifty 50 −5.9%), and the CPSE index itself is ~80%+ power and oil & gas — so "PSU" and "energy/power" are overlapping, not independent, groups. Index ETFs must be decomposed into constituents: HDFC Bank ~10% of Nifty 50 (and roughly 25-30% of Nifty Bank), Reliance ~8% of Nifty 50, Wipro ~8% of Nifty IT (May 2025).

### Cited Findings
- Nifty PSE fell ~13.75% between 4 and 15 Mar 2024 — [Business Standard](https://www.business-standard.com/amp/markets/news/are-the-nifty-psu-indices-staring-at-up-to-15-fall-from-current-levels-124031100550_1.html); BSE CPSE index −6% in one day (13 Mar 2024) with RITES, IRFC, RVNL, HUDCO, IRCON down up to 12% — [Business Standard](https://www.business-standard.com/amp/markets/news/bse-cpse-index-plunges-6-rites-irfc-ircon-rvnl-tank-up-to-12-124031300329_1.html)
- 4 Jun 2024 (election result day): Nifty PSE −16.38%, Nifty Energy −12.47%, Nifty 50 −5.93% — [ICICI Direct](https://www.icicidirect.com/share-market-today/market-news-commentary/quick-wrap-nifty-pse-index-declines-1638percentage,-nifty-tumbles-593percentage/1518809)
- CPSE index sector mix: power ~46.5%, oil & gas ~36.1% — [Arthgyaan CPSE ETF review](https://arthgyaan.com/blog/cpse-etf-review.html)
- Goetzmann-Kumar: individual investors ignore correlations among holdings when diversifying — [NBER w8686](https://www.nber.org/papers/w8686)
- Nifty 50 weights (29 Sep 2026, third-party, not NSE-verified): HDFC Bank 9.89%, ICICI Bank 9.35%, Reliance 8.02%, Infosys 3.68%, TCS 2.19% — [Stockmojo](https://stockmojo.in/index-weightage/nifty); HDFC Bank ~10.0% in Aug 2026 constituent files — [Taurus MF](https://taurusmutualfund.com/sites/default/files/2026-08/nifty-index-constituent-as-on-17_08_2026.pdf)
- Nifty Bank: HDFC Bank projected ~29.1%, ICICI ~23.3% post-merger (2023 projection; no 2026 figure found) — [5paisa](https://5paisa.com/news/hdfc-bank-now-holds-more-weight-than-reliance-industries-in-nifty) / search extract
- Nifty IT (May 2025): TCS 39.73%, Infosys 20.32%, Wipro 8.14% — search extract from [TradingView IT sector review](https://www.tradingview.com/chart/TATATECH/yzqwfdnZ-IT-Sector-Review) (dated, secondary)
- Nifty 500 (Jul 2026): HDFC Bank 5.72%, ICICI 5.14% — [Bajaj Broking](https://www.bajajbroking.in/share-market-news/inside-the-nifty-500-index-how-it-changed-from-2021-to-2026)

### Inferences
- Define overlapping "risk groups" (tags; a stock can belong to several) in addition to GICS-like sectors, each with its own cap: STATE_OWNED (PSU), ENERGY_POWER (oil, gas, coal, power generation/transmission/finance e.g. PFC/REC), RATE_SENSITIVE/FINANCIALS, COMMODITY_LINKED (metals, energy, gold/silver ETFs), SMALLCAP. Current 29% energy+power and ~19.5% PSU would both breach a 20%/15% group cap.
- Look-through example: if Nifty 50 ETF = 5% of portfolio, it adds ~0.5% HDFC Bank and ~0.4% Reliance; Nifty Bank ETF at 3% adds ~0.8-0.9% HDFC Bank. Single-name and sector caps should be tested on look-through exposure (direct + Σ ETF weight × constituent weight).
- Constituent weights should be loaded from NSE Indices monthly factsheets / AMC monthly portfolio disclosures (free) and cached, refreshed monthly.
- Optionally compute a correlation-based cluster check (e.g., 1-yr daily return correlation > 0.6 → same cluster) to catch groupings labels miss.

### Gaps
- No official NSE factsheet for Sep 2026 fetched; Nifty Bank/IT current weights unverified.
- No systematic correlation statistic for PSU vs energy indices found; only event drawdowns.

## 5. Core-satellite: active underperformance (SPIVA India) and core % ranges

### Takeaway
SPIVA India year-end 2025: ~75-84% of active large-cap funds underperformed the S&P India LargeMidCap over 1-10 years; mid/small-cap active funds did better in 2025 (majority outperformed, best since 2014), though over 10 years most still lag per earlier scorecards. If professionals mostly fail to beat large-cap indices, a retail stock picker should hold a sizeable index core; practitioner ranges are 60-80% core, while Vanguard observes advisers' indexed share averages ~50% (normal 20-65%).

### Cited Findings
- SPIVA India Year-End 2025: Indian Equity Large-Cap funds underperformance rate 75.0% (1-yr), 74.2% (3-yr), 84.4% (5-yr), 76.3% (10-yr) vs S&P India LargeMidCap (index +8.9% in 2025; funds +7.3% equal-weighted, +9.4% asset-weighted); active mid/small-cap funds had majority outperformance, best relative result since 2014 — [S&P DJI SPIVA India YE2025](https://www.spglobal.com/spdji/en/spiva/article/spiva-india-year-end-2025/); [PDF](https://www.spglobal.com/spdji/en/documents/spiva/spiva-india-scorecard-year-end-2025.pdf) (via search extract; page not directly fetchable). Mid-year 2025 figures differ (e.g., 5-yr 89.7% cited in secondary sources) — [SPIVA India mid-year 2025](https://www.spglobal.com/spdji/en/spiva/article/spiva-india-mid-year-2025)
- Earlier scorecard coverage: 73% of large-cap and 82% of mid/small-cap funds underperformed over 10 years — [Cafemutual](https://cafemutual.com/news/industry/35917-73-of-indian-large-cap-and-82-of-mid-and-small-cap-funds-have-underperformed-sp-india-benchmarks-over-a-10-year-period)
- Core-satellite ranges: core ~65-80% — [etf.com](https://www.etf.com/sections/blog/etfs-all-you-need-portfolios); 60-80% core for long-horizon investor — [interactive investor](https://ii.co.uk/analysis-commentary/core-and-satellite-funds-ps100k-isa-portfolio-ii530728)
- Vanguard 2026 Adviser Portfolio Trends: average indexed exposure ~50%, normal range ~20-65%; warns of loosely applied core-satellite creating overlapping exposures — [Financial Standard](https://www.financialstandard.com.au/news/core-satellite-models-can-only-be-effective-with-purpose-vanguard-179812344)
- Vanguard framing: indexed core captures market returns at low cost/risk; satellites seek outperformance — [Vanguard Canada](https://www.vanguard.ca/en/investor/learn/featured-group/strategies/active-passive-combinations)
- Experience improves Indian retail outcomes but primarily via lower turnover/better diversification — [NBER w20000](https://www.nber.org/papers/w20000.pdf)

### Inferences
- Current index ETF share appears modest; tool should report "core %" (broad index ETFs: Nifty 50/Next 50/500, Midcap 150, Smallcap 250) vs satellite (direct stocks + sector ETFs like Nifty Bank/IT, which are concentrated satellites, not core).
- Suggested policy: equity core ≥ 50% (target 60%), satellite ≤ 40-50%, with the stock sleeve benchmarked against the Nifty 500/LargeMidCap; if the satellite lags the core over a rolling 3-yr window, the tool should recommend shifting the core target up 10pp.
- Sector ETFs (Nifty Bank, Nifty IT) duplicate direct holdings; consider consolidating them into broad core or counting them as satellite.

### Gaps
- No SPIVA-equivalent study measuring Indian *retail direct-stock* portfolios vs index (SEBI studies cover F&O/intraday). The SPIVA evidence is about mutual funds, applied by analogy.

## 6. Role and sizing of gold/silver in Indian portfolios

### Takeaway
Indian advisory consensus is ~10-15% gold for diversification; evidence is period-dependent (one 20-yr analysis suggests 20-25%, 15-yr 10-15%). The portfolio's 12.4% gold+silver sits within range; silver is more volatile and industrially linked (commodity-correlated), so it should be a smaller sub-cap and counted in the commodity risk group.

### Cited Findings
- Most Indian experts suggest limiting gold to 10-15%; ideal depends on risk profile and horizon — [Bajaj Finserv](https://bajajfinserv.in/investments/how-much-of-your-portfolio-should-be-invested-in-gold); [smallcase](https://www.smallcase.com/blog/gold-and-asset-allocation-striking-the-right-balance/)
- One backtest: 20-year analysis suggests 20-25% gold for best risk-adjusted return, 15-year view ~10-15% — [iVentures](https://iventures.in/feeds/blog/gold-allocation-portfolio)
- IIM Kozhikode paper: optimal gold weight in India historically could be as high as ~30% (household context), expected to fall toward ~10% as banking penetration rises — [IIMK](https://iimk.ac.in/uploads/publications/251fullp.pdf)
- WGC research reportedly finds gold's average correlation with equities/bonds ~0.1 (secondary attribution, not India-specific, unverified) — [share.market](https://share.market/buzz/golden-path-to-diversification-decoding-the-role-of-gold-in-your-portfolio-this-dhanteras)
- Gold LTCG uses 24-month threshold, 12.5% without indexation (post Jul 2024) — [5paisa](https://www.5paisa.com/blog/evolution-of-ltcg-stcg-tax-in-india)

### Inferences
- Treat precious metals as a separate asset-class sleeve with its own target (e.g., 10%, band 7.5-12.5%) rather than a "sector" competing for the 25% sector cap; silver sub-cap ~3-4%.
- Gold rebalancing is the clearest use of threshold bands (low correlation to equity → rebalancing premium most plausible).

### Gaps
- No verified primary WGC India correlation figure; no primary source found on silver sizing for Indian portfolios.
- Tax treatment of gold/silver ETFs specifically (vs physical gold) not verified in this pass.

## Recommended rule changes for the repo

Parameters are suggestions grounded in the findings above; all should live in `RiskConfig` (config.py) with env overrides.

1. **Two-level structure (asset class → holding).**
   - `ASSET_CLASS_TARGETS`: equity_core 55%, equity_satellite 35%, precious_metals 10% (gold ≤ 8%, silver ≤ 4%). Bands: ±25% relative (e.g., metals 7.5-12.5%).
   - Classify ETFs: broad index (Nifty 50/500/Next 50/Midcap 150/Smallcap 250) = core; sector ETFs (Nifty Bank, Nifty IT) = satellite.
   - Report `core_pct`; warn if < 50%.

2. **Look-through exposures.** Add `etf_constituents.csv` (ticker, constituent, weight, as_of) refreshed monthly from NSE Indices factsheets / AMC disclosures. Compute effective single-stock, sector and risk-group exposure = direct + Σ(ETF weight × constituent weight). Apply all caps on look-through numbers.

3. **Position caps.**
   - `MAX_POSITION_PCT` = 8% (keep) on look-through basis for direct stocks; hard cap 10% triggers a trim regardless of band.
   - Volatility-adjusted cap: `cap_i = MAX_POSITION_PCT × min(1, median_vol / vol_i)` with 1-yr daily vol, floor 3%.
   - `MIN_POSITION_PCT` = 2% (≈ ₹13,500 at current value): positions below this get "add to target or exit" recommendation; no new position opened below 2%.
   - Satellite stock count target 12-20 (`MAX_OPEN_POSITIONS` 15 → apply to direct stocks only, max 20); report effective N = 1/Σw² (target ≥ 12 for the stock sleeve).

4. **Conviction weighting — narrower ladder.** Replace 8/5/3/1.5 with base-weight multipliers around equal weight: conviction 5 → 6%, 4 → 4.5%, 3 → 3%, ≤ 2 → 0% (exit/no add). Normalise so satellite targets sum to the satellite sleeve. (Rationale: 1/N robustness; 2x not 5x spread.)

5. **Risk groups (overlapping tags) with caps** in addition to the 25% sector cap:
   - STATE_OWNED (PSU) ≤ 15%
   - ENERGY_POWER (oil & gas, coal, power gen/transmission, power financiers PFC/REC) ≤ 20%
   - FINANCIALS (banks + NBFC + insurance, look-through incl. Nifty Bank/Nifty 50) ≤ 25% (keep)
   - COMMODITY_LINKED (metals, energy, silver) ≤ 25%
   - SMALLCAP (direct + Smallcap 250 ETF) ≤ 15%
   - Optional: correlation cluster check — flag any group of holdings with pairwise 1-yr correlation > 0.6 summing > 20%.
   - Excess allocation: pro-rata trim within the group but trim lowest-conviction / highest-vol first (sort by conviction asc, then vol desc) instead of pure pro-rata.

6. **Rebalancing logic (opportunistic bands).**
   - Evaluate on each run (weekly/biweekly is fine), trade only on breach.
   - Holding-level trim trigger: weight > max(target × 1.25, target + 1.5pp) (replaces flat +2pp); add trigger: weight < target × 0.75 and funds available.
   - Asset-class bands: ±25% relative of target (metals) / ±5pp absolute (equity core vs satellite), per Vanguard's 5pp and Daryanani's ~20%.
   - Trim back to target + half-band, not to target (reduces turnover).
   - **Cash-flow first:** new contributions and dividends allocated to most-underweight sleeves/holdings before any sell is suggested.

7. **Tax and cost awareness.**
   - `MIN_TRADE_INR` = 5,000 (keep) and also ≥ 0.5% of portfolio.
   - Prefer selling lots held > 12 months (equity) / > 24 months (gold/silver per source); track FY realised LTCG against ₹1.25L exemption (`LTCG_EXEMPTION_INR = 125000`); flag trims that would realise STCG (20%) and require weight > target × 1.5 before suggesting them.

8. **Retire ATR trade sizing for core holdings.** Keep `RISK_PER_TRADE_PCT`/ATR stops only for a flagged `tactical` sleeve (≤ 10% of portfolio). For long-term holdings, use weight targets + caps above; demote ATR trailing stop to an informational "review thesis" alert rather than a sell signal.

9. **Reporting metrics to add:** effective N, top-10 concentration, look-through top-10 single names, risk-group table, core %, satellite vs Nifty 500 rolling 3-yr relative return (recommend raising core target by 10pp if satellite lags by > 2%/yr).
