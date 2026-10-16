# Rebalancing and Indian capital-gains tax mechanics for a retail investor (FY2026-27)

Scope: step-by-step procedures, with numbers, for (a) rebalancing a simple equity/debt/gold portfolio and (b) capital-gains tax optimisation in India for FY2026-27 (1 Apr 2026 – 31 Mar 2027), under the Income-tax Act, 2025 as amended by Finance Act 2026. These are research notes, not tax advice.

Research caveat: during this session most primary sites (incometaxindia.gov.in, AMC tax reckoners, freefincal.com, patronaccounting.com) could not be fetched because of DNS failures. Findings below rely on search-result summaries of those pages and on secondary sources. Items marked **[UNVERIFIED]** come from general knowledge, or from a single source I could not confirm. Check them against the Act text or an AMC "Tax Reckoner 2026-27" before acting.

## Q1. Rebalancing: calendar vs threshold bands, new-money-first, when to sell, small portfolios, crashes

### Takeaway
The best-supported method is to check the portfolio on a calendar, once or twice a year, and act only when an asset is more than about 5 percentage points away from its target. Route new money (SIPs) and income to the underweight asset first. Sell only when cash flows cannot close the gap in a reasonable time, or in a large move such as a crash. Vanguard's backtest found this approach controls risk with very few trades, which in India also means less capital-gains tax and fewer exit loads.

### Cited Findings
- Vanguard (2010, "Best practices for portfolio rebalancing"): for most broadly diversified stock/bond portfolios, "annual or semiannual monitoring, with rebalancing at 5% thresholds, is likely to produce a reasonable balance between risk control and cost minimization." Annual rebalancing is likely preferred when taxes or substantial time and costs are involved. — [Vanguard 2010 paper (PDF mirror)](https://indexacapital.com/bundles/unaiadvisor/docs/papers/2010-Vanguard-Best-practices-for-portfolio-rebalancing.pdf?v=241); summarised in [WealthManagement, "The Art of Rebalancing"](https://www.wealthmanagement.com/investment/art-rebalancing)
- Vanguard backtest (60/40, 1926–2009 period as reported in secondary summaries): annual monitoring with a 5% threshold gave about 9.8% volatility, about 1.6% annual turnover and 36 rebalancing events, among the lowest of the strategies tested. A never-rebalanced portfolio drifted to about 81% stocks with 13.2% volatility. Monthly rebalancing with no threshold needed about 1,008 events, versus 15 for annual with a 10% threshold. — [WealthManagement](https://www.wealthmanagement.com/investment/art-rebalancing); [Vanguard 2010 PDF](https://indexacapital.com/bundles/unaiadvisor/docs/papers/2010-Vanguard-Best-practices-for-portfolio-rebalancing.pdf?v=241). (The search summary reported the period as "1926–2014", which conflicts with a 2010 paper. Treat the exact period as unverified; the 9.8%/13.2% figures are consistently reported.)
- Vanguard (2024, target-date funds): a threshold-based method (200/175 bp bands) beat calendar-based rebalancing by about 5–21 bp a year in relative terms. — [Vanguard research summary](https://corporate.vanguard.com/content/corporatesite/us/en/corp/articles/balancing-act-enhancing-target-date-fund-efficiency.html)
- Cash-flow rebalancing (sending contributions, dividends and interest to the underweight asset, and taking withdrawals from the overweight one) is described as the simplest and most tax-efficient way to rebalance a taxable account, because nothing is sold. It is slow when the drift is large. — [MyMoneyBlog summarising Vanguard tips](https://www.mymoneyblog.com/practical-portfolio-rebalancing-tips.html); [SmartAsset](https://smartasset.com/investing/how-to-rebalance-portfolio-without-selling); [Freenance](https://freenance.io/strategies/portfolio-rebalancing-when-and-how/). (Secondary sources. I did not reach the original Vanguard article.)
- Rebalancing costs are trading costs, possible capital-gains taxes and time, and they rise sharply with frequency. — [WealthManagement](https://www.wealthmanagement.com/investment/art-rebalancing)

### Inferences
- **Procedure (bands plus cash flow):**
  1. Fix targets, e.g. 70/20/10 equity/debt/gold. Bands are ±5 percentage points for equity (65–75%), and for the smaller sleeves either ±5pp absolute or ±25% relative (debt 15–25%, gold 7.5–12.5%).
  2. **Monthly (5 minutes):** compute current weights. Send the whole month's SIP to whichever sleeve is furthest below target. This is "new money first", and it is the only rebalancing most months need.
  3. **Semi-annual check (e.g. April and October):** if every sleeve is inside its band, do nothing. If a sleeve is outside, first ask whether the next 3–6 months of SIPs would close the gap. If yes, redirect SIPs. If no, sell the overweight sleeve back to target (not just to the band edge; Vanguard's tests restore to target).
  4. **When you must sell, choose in this order:** units already held more than 12 months whose gain fits inside the ₹1.25 lakh LTCG exemption → lots with losses → lots outside the exit-load window. Avoid lots held 12 months or less (20% STCG on equity) and lots within the exit-load period (usually 1% within 1 year on equity funds **[UNVERIFIED general practice; check each scheme]**).
  5. **Crash rule:** a 30% equity fall pushes equity well below its 65% band. Rebalance by selling debt/gold and buying equity. Debt gains are taxed at slab but are usually small, so the tax cost of this rebalance is low (see the worked example). Pre-commit in writing to execute it; behaviour is the main risk.
- **Small portfolios (under about ₹5–10 lakh, or while SIPs are large relative to the corpus):** contributions alone almost always rebalance faster than drift. A ₹30,000/month SIP on a ₹5 lakh corpus is 6% of the portfolio each month, so selling is practically never needed. Widen the bands (e.g. ±7.5pp) and skip any rebalance trade under about ₹5,000, where fixed costs dominate.
- Use the annual-only check if harvesting and ITR work are done once a year. Bands plus annual review fits India well because the LTCG exemption resets each financial year.

### Gaps
- No India-specific study (e.g. Nifty/gilt/gold 1990–2025) comparing calendar and band rebalancing was found. The Vanguard evidence is US stock/bond.
- I could not confirm Vanguard's own wording on cash-flow rebalancing from the primary source.

## Q2. FY2026-27 tax rules (Income-tax Act 2025; sections replacing 111A/112A)

### Takeaway
Budget 2026 (1 Feb 2026) left the equity rates unchanged. The rules are:
- **Listed equity and equity-oriented funds (STT paid):** gains on units held 12 months or less (STCG) are taxed at 20%. Gains on units held more than 12 months (LTCG) are taxed at 12.5% on the amount above ₹1.25 lakh per financial year. The new Act generally maps 111A to section 196 and 112A to section 198.
- **Debt mutual funds bought on or after 1 Apr 2023:** taxed at slab rate whatever the holding period.
- **Gold ETFs:** gains on units held more than 12 months are taxed at 12.5%, with no indexation and no ₹1.25 lakh exemption.
- **Gold fund-of-funds:** need more than 24 months to qualify for 12.5%.
- **Losses:** short-term losses offset any capital gain, long-term losses offset only long-term gains, and unused losses carry forward 8 years only if the ITR is filed by the due date.

### Cited Findings
- **Section mapping:** under the Income-tax Act, 2025 (in force from 1 April 2026), STCG on STT-paid equity, equity-oriented fund units and business trust units falls under section 196 at 20%. LTCG over ₹1,25,000 falls under section 198 at 12.5%; these correspond to old sections 111A and 112A. Section 197 is the general 12.5% LTCG rule. Section 198 requires STT to have been paid. — [Ebizfiling on sections 196/198](https://ebizfiling.com/blog/section-196-and-198-short-term-and-long-term-capital-gains/); [EZTax section 198](https://eztax.in/income-tax-act-2025/section-198); [Income Tax Dept, section 197 page](https://www.incometaxindia.gov.in/w/section-197-78); [Taxsutra](https://www.taxsutra.com/lsi/act/section/print/146804). **[Statute text not fetched; section numbers rely on secondary sources.]**
- **Budget 2026:** LTCG (12.5%) and STCG (20%) rates on equity are unchanged. — [Tata MF post-Budget 2026 note](https://www.tatamutualfund.com/blogs/post-budget-2026-new-tax-map-equity-investors); [Angel One](https://oga-prod.angelone.in/news/taxation/union-budget-2026-ltcg-tax-unchanged-at-12-5-stt-on-commodity-futures-hiked); [Finlecture FY2026-27](https://finlecture.in/indian-tax-system/capital-gains-tax-fy-2026-27/)
- **Buybacks:** from 1 April 2026, proceeds are taxed as capital gains for shareholders (cost deductible, 12.5%/20%) instead of as deemed dividend. Promoters face an additional levy. — [Tata MF](https://www.tatamutualfund.com/blogs/post-budget-2026-new-tax-map-equity-investors); [Wright Research](https://www.wrightresearch.in/blog/buyback-taxation-in-india-2026-budget-changes-old-vs-new-rules-examples-and-benefits/) (the Wright Research page is internally inconsistent; prefer Tata MF)
- **Holding period:** shares and equity-oriented fund units are long-term if held more than 12 months. — [Kanakkupillai](https://www.kanakkupillai.com/learn/how-to-set-off-and-carry-forward-capital-losses/); [Outlook Money](https://www.outlookmoney.com/personal-finance/how-to-carry-forward-and-set-off-a-loss-under-income-from-capital-gain--news-304497)
- **FIFO in demat:** CBDT Circular 768 (24 Jun 1998) says that for demat holdings the earliest-acquired securities are treated as sold first. Its example has 2,500 shares sold, with the first 2,000 taking the oldest lot's cost and date. — [Income Tax Dept, Circular 768](https://www.incometaxindia.gov.in/w/768-circular-no.-768-dated-24-6-1998-1); [TaxGuru](https://taxguru.in/?p=73202). A later (2007) CBDT circular applies FIFO separately for each demat account. — [Outlook Money](https://www.outlookmoney.com/tax/tax-saving-tips-why-having-only-one-demat-account-can-make-you-lose-profit-from-your-equities). Conflicting case law: the Bombay HC applied Circular 704 (contract-note date) to demat securities, and the Calcutta HC read 768 as covering physical holdings too. — [ITAT Online digest](https://itatonline.org/digest/nawal-kishore-kejriwal-v-cit-2024469-itr-543-151-taxmann-com-117-calhc). **[Status of these circulars under the 2025 Act not verified.]**
- **Set-off and carry-forward:** STCL can be set off against STCG and LTCG. LTCL can be set off only against LTCG. Unabsorbed losses carry forward for 8 assessment years only if the return is filed by the due date (old s.139(1)); a belated return forfeits carry-forward. The loss must be reported in Schedule CFL, and filing is needed even if income is below the taxable limit. — [Kanakkupillai](https://www.kanakkupillai.com/learn/how-to-set-off-and-carry-forward-capital-losses/); [Outlook Money](https://www.outlookmoney.com/personal-finance/how-to-carry-forward-and-set-off-a-loss-under-income-from-capital-gain--news-304497); [TaxGuru](https://taxguru.in/income-tax/set-carry-capital-loss.html); [Patron Accounting, AY2026-27](https://www.patronaccounting.com/blog/set-off-carry-forward-losses-ay-2026-27)
  - Conflict: Patron Accounting (Apr 2026) claims a Budget 2025 relaxation let LTCL from before 31 Mar 2026 offset STCG. No other source mentions it, and it contradicts the standard rule. **Treat as unverified and likely wrong**; do not rely on it.
- **Same-day buy and sell:** income from intraday equity (no delivery) is speculative business income taxed at slab. Very frequent short-term delivery trading may be treated as business income. — [Zerodha Varsity, Taxation for Traders](https://zerodha.com/z-connect/category/taxation-for-traders); [Slideshare copy of Varsity notes](https://www.slideshare.net/slideshow/taxation-for-traders-markets-and-taxation-notes/251912576). Community answers on whether selling holdings and rebuying the same scrip the same day is netted as intraday conflict; one recommends rebuying on T+1 or later. — [TradingQnA thread](https://tradingqna.com/t/tax-loss-harvesting-related/128956); [TradingQnA intraday vs holdings](https://tradingqna.com/t/if-i-do-intraday-trading-in-a-stock-which-i-am-holding-in-long-term-will-there-be-cap-gain-tax-for-it-if-i-sell-it/3112)
- **Grandfathering (pre-1 Feb 2018 lots):** cost = higher of (a) actual cost and (b) the lower of the FMV on 31 Jan 2018 and the sale price. FMV is the highest traded price on 31 Jan 2018 (or the last prior trading day), or the NAV on that date for MFs. Grandfathering cannot create a loss. — [Geojit support](https://support.geojit.com/support/solutions/articles/89000006851-what-is-grandfathering-how-are-long-term-capital-gains-ltcg-treated-under-the-grandfathering-provi); [EZTax](https://eztax.in/questions/what-is-section-112a-grandfathering-rule); [Arthgyaan](https://arthgyaan.com/blog/pay-lower-capital-gains-taxes-for-equity-how-grandfathering-works.html). **[Section number under the 2025 Act not found.]**
- **Debt funds ("specified mutual funds"):** funds with more than 65% in debt/money-market instruments (and FoFs investing 65%+ in such funds), bought on or after 1 Apr 2023, are taxed at slab rate however long they are held, with no indexation. This covers liquid, money-market and conservative hybrid funds with less than 35% equity. The ICICI Pru Tax Reckoner 2026-27 cites section 76(5)(b) of the 2025 Act for the definition. Gold ETFs, gold FoFs and international funds moved out of this bucket after Finance (No.2) Act 2024. — [Freefincal Budget 2024](https://freefincal.com/budget-2024-big-change-in-mutual-fund-taxation-rules); [ICICI Pru Tax Reckoner 2026-27](https://www.icicipruamc.com/blob/knowledgecentre/tax_reckoner/Tax%20Reckoner%202026-27.pdf); [HSBC Tax Reckoner FY2026-27](https://www.assetmanagement.hsbc.co.in/assets/documents/mutual-funds/en/da5d1d18-343c-41d2-aaf9-e6967d009ee8/tax-reckoner-fy-2026-2027.pdf); [Kuvera](https://kuvera.in/blog/which-debt-mutual-fund-investments-are-taxed-at-different-rates-and-how-does-indexation-impact-them-2/); [TaxGuru](https://taxguru.in/?p=1057273)
- **Gold:**
  - Gold ETFs: units held more than 12 months are taxed at 12.5% with no indexation. Units held 12 months or less are taxed at slab. The 12-month threshold applies to transfers on or after 1 Apr 2025.
  - Gold mutual funds/FoFs (unlisted) need more than 24 months.
  - The ₹1.25 lakh exemption does not apply to gold.
  - One guide (IPOMarket) says post-April-2023 gold funds are always at slab; this looks outdated.
  — [ClearTax gold ETF vs MF](https://cleartax.in/s/gold-etfs-vs-mutual-funds-taxation-guide); [Aditya Birla Capital](https://www.adityabirlacapital.com/abc-of-money/tax-on-gold-etf); [BasuNivesh 2026](https://www.basunivesh.com/taxation-of-gold-and-silver-in-india-in-2026-explained-simply/); contra [IPOMarket](https://www.ipomarket.in/news/capital-gains-tax-on-gold-india)

### Inferences
- **No wash-sale rule:** India has no wash-sale rule like the US one (no source found imposing one), so selling and rebuying the same security to reset cost is legal. **[UNVERIFIED that no anti-avoidance provision applies; GAAR thresholds make it practically irrelevant for retail amounts.]**
- **Clock and order:** the holding-period clock runs from the purchase trade date, and each SIP instalment is a separate lot with its own 12-month clock. Under FIFO, a redemption always consumes the oldest units first.
- **[UNVERIFIED, general knowledge]:**
  - Surcharge on equity capital gains is capped at 15%, plus 4% cess.
  - A resident individual with total income below the basic exemption limit can use the unused limit against STCG/LTCG.
  - The section 87A rebate is not available against special-rate capital gains from FY2025-26.
- **Set-off happens before the exemption [UNVERIFIED but standard computation]:** losses are set off against gains first, and the ₹1.25 lakh exemption applies to what remains. A long-term loss booked in a year when LTCG is already under ₹1.25 lakh is therefore wasted, because it offsets gains that would have been tax-free anyway.

### Gaps
- I could not read the Income-tax Act 2025 text for sections 196/198, the carry-forward section (old s.74), the due-date section (old s.139(1)) or grandfathering (old s.55(2)(ac)). The new section numbers are unconfirmed.
- I could not confirm whether Circulars 704/768 were expressly continued under the 2025 Act.

## Q3. Step-by-step LTCG harvesting

### Takeaway
Each financial year, in January–March (after checking that no further big gains are planned), sell enough long-term units to realise about ₹1.25 lakh of LTCG minus any LTCG already realised that year. Rebuy on the next trading day. The rebought units carry a higher cost and a fresh purchase date. This saves up to ₹15,625 a year plus cess, per person, and the saving is deferred rather than permanent.

### Cited Findings
- Equity fund LTCG up to ₹1.25 lakh a year is exempt. The method is to sell units to book gains within the limit and reinvest in the same or a similar fund. Without reinvestment the strategy is pointless. — [Kuvera](https://kuvera.in/blog/?p=41428); [Outlook Money](https://www.outlookmoney.com/tax/tax-harvesting-for-mutual-funds-simple-strategies-to-lower-your-ltcg-tax)
- The maximum yearly saving is about ₹15,625 (12.5% × ₹1.25 lakh). The method does not improve investment returns and is only worth doing if the saving exceeds transaction costs. — [Kuvera](https://kuvera.in/blog/save-up-to-%E2%82%B910000-in-ltcg-taxes-with-tax-harvesting/amp/); [Kotak Securities](https://www.kotaksecurities.com/investing-guide/articles/tax-harvesting-strategy) (note: Kotak's page has a typo, "₹25 lakh")
- Rebuy on T+1 or later rather than the same day, so the trades are not netted as intraday. — [TradingQnA](https://tradingqna.com/t/tax-loss-harvesting-related/128956) (community source)

### Inferences — procedure
1. **Mid-January:** run a FIFO lot report: lot date, units, cost (or grandfathered cost for pre-Feb-2018 lots), current price.
2. Compute the remaining exemption as ₹1,25,000 minus the LTCG already realised this FY. If that net figure is negative, it is a net LTCL and there is nothing to harvest.
3. Walk the FIFO queue from the oldest lot. Only lots held more than 12 months count. Accumulate gain per unit × units until the remaining exemption is reached. The units needed is the sell quantity.
4. Check exit loads. Lots over 1 year are usually load-free on equity funds **[UNVERIFIED per scheme]**. Check ELSS lock-in (3 years from each instalment).
5. Sell on day T, before about 20 March to stay clear of settlement and holiday risk near 31 March. Rebuy the same quantity or amount on T+1 (shares/ETFs). For MFs, place the purchase after the redemption is processed. For MFs, alternatively switch to a near-identical index fund from another AMC.
6. **Record:** sale date, units, sale value, FIFO cost, gain, and the new lot's date and cost. Keep the broker's tax P&L and the CAS (CAMS/KFin) as evidence.
7. **Family:** each PAN (spouse, adult children, parents) has its own ₹1.25 lakh exemption, but only on assets genuinely owned by that person. **[UNVERIFIED nuance:** clubbing under old s.64 applies to income from assets gifted to a spouse or minor child, so gifting money to a spouse to harvest their exemption generally does not work. Adult children's and parents' own investments do.]
8. **Trade-off:** the rebought units are short-term for the next 12 months. If you might need to sell them within a year, the 20% STCG risk can outweigh the ₹15,625 saving.
9. **Costs [UNVERIFIED rates]:**
   - Equity MF redemption STT is about 0.001%, and MF purchase stamp duty about 0.005%: negligible.
   - Shares/ETFs: delivery STT is about 0.1% on each side, plus stamp duty of about 0.015% on the buy. On ₹2.8 lakh that is roughly ₹600 + brokerage. It is still clearly worth it against ₹15,625.

### Gaps
- I found no official guidance on whether a same-day sell and rebuy of shares is treated as speculative for tax purposes (as opposed to broker netting). The T+1 advice is community practice.

## Q4. Tax-loss harvesting

### Takeaway
Book unrealised losses before 31 March to offset gains you have realised, or will realise, this year. Apply short-term losses to 20% STCG first (the highest saving). Rebuy on T+1 if you still want the position. Unused losses carry forward 8 years only if you file your ITR on time.

### Cited Findings
- Sell loss-making stocks to book a loss, net it against profits, and buy back if you still want to hold the stock. Doing this before 31 March reduces the year's tax. — [Zerodha Z-Connect tax-loss harvesting](https://zerodha.com/z-connect/taxation-for-traders/tax-loss-harvesting-opportunity-fy-18-19); [Share.market](https://www.share.market/buzz/learn/tax-loss-harvesting/)
- Set-off rules (STCL against anything, LTCL against LTCG only) and the 8-year carry-forward with timely ITR — see Q2 sources ([Kanakkupillai](https://www.kanakkupillai.com/learn/how-to-set-off-and-carry-forward-capital-losses/); [TaxGuru](https://taxguru.in/income-tax/set-carry-capital-loss.html)).

### Inferences
- **Which loss to book first:** an STCL (lot held 12 months or less) is more valuable than an LTCL, because it can offset STCG taxed at 20% and can also offset LTCG.
- **FIFO trap:** you cannot pick a high-cost recent lot to book a loss if older low-cost lots of the same scrip in the same demat account come first. FIFO will match the old lot and may book a gain instead. The only way to reach the loss lot is to sell everything ahead of it in that account.
- **Wasted LTCL:** if total LTCG for the year is already ₹1.25 lakh or less, booking an LTCL gives no current saving. Its only value is carry-forward, and current-year set-off is applied first.

### Gaps
- I found no source confirming whether the taxpayer may choose to set off STCL against STCG before LTCG. The ITR schedules (CG/BFLA) appear to allow the beneficial ordering. **[UNVERIFIED]**

## Q5. Common mistakes

### Takeaway
The costly errors are:
- FIFO surprises (selling a different lot than intended).
- Switching from regular to direct plans without counting the tax.
- Exit loads on units held under a year.
- Same-day rebuys.
- Missing the ITR due date, which forfeits carried-forward losses.
- Forgetting that every SIP instalment and every rebought lot restarts its own 12-month clock.

### Cited Findings
- A switch from a regular to a direct plan is a redemption plus a fresh purchase, so it triggers capital gains, and the holding period restarts for the direct-plan units. Lock-in funds (ELSS) cannot be switched until lock-in ends. One suggestion is to spread large switches over 12–15 months (i.e. across two FYs, using two exemptions). — [ClearTax](https://cleartax.in/s/switch-regular-to-direct-plans); [Value Research](https://www.valueresearchonline.com/stories/51826/should-you-make-the-switch-from-regular-to-direct-mutual-fund-plans/); [Kuvera switch guide](https://kuvera.in/blog/a-guide-on-how-to-shift-or-switch-mutual-funds/); [Money9](https://money9.com/news/investment-planning/understand-implications-while-switching-from-one-mutual-fund-scheme-to-another-73082.html)
- SEBI has reportedly removed exit loads on switches from a regular to a direct plan within the same scheme (DSP and Quant applied this). Older guides still say exit loads apply. — [5paisa](https://5paisa.com/news/sebi-eliminates-exit-loads-for-switching-from-regular-to-direct-mutual-fund-plans). **[Verify per scheme.]**
- FIFO is applied account-wise, so holdings split across demat accounts are matched separately. — [Outlook Money](https://www.outlookmoney.com/tax/tax-saving-tips-why-having-only-one-demat-account-can-make-you-lose-profit-from-your-equities)
- A belated ITR forfeits loss carry-forward. — [Kanakkupillai](https://www.kanakkupillai.com/learn/how-to-set-off-and-carry-forward-capital-losses/)

### Inferences
- **Switch planning:** do regular→direct switches lot by lot. Switch lots held more than 12 months first, and keep each FY's realised gain within ₹1.25 lakh. Leave lots held 12 months or less until they age.
- **Harvesting and bonds:** do not harvest debt funds. Gains on debt funds bought on or after 1 Apr 2023 are at slab whenever realised, so harvesting saves nothing and only advances tax.
- **Ageing lots:** a lot "a few days short of 12 months" costs 20% instead of 0–12.5%. Always check lot dates before any sale in March.

### Gaps
- None beyond the verification flags above.

## Q6. What `tax_planner.py` already provides and what is missing

### Takeaway
`/home/user/Portfolio/tax_planner.py` already does the core FIFO accounting for one financial year:
- realised and unrealised STCG/LTCG;
- the remaining ₹1.25 lakh exemption and the harvestable tax-free LTCG;
- per-symbol loss-harvest candidates.

It does not yet:
- produce per-lot sell quantities;
- apply set-off ordering or carried-forward losses;
- distinguish asset classes (debt at slab, gold rules);
- handle grandfathering;
- give rebalancing instructions.

It also has a few correctness edge cases.

### Cited Findings (from reading the code: `/home/user/Portfolio/tax_planner.py`, `config.py` lines 79–81, test `tests/test_analysis.py::test_tax_planner_fifo_and_exemption`)
- **What it computes:**
  - It reads `trades.csv` (Date, Stock Symbol, Action, Qty, Price), sorts by date and keeps FIFO open lots per symbol. SELLs consume the oldest lots.
  - For sales inside the current FY (Apr–Mar via `get_financial_year`), it classifies each matched slice as LTCG if `holding_days > 365`, else STCG. It sums realised STCG/LTCG and lists each matched trade.
  - It values open lots at CMP (from `portfolio.csv` "Current Market Price" or `current_prices`) to get unrealised STCG/LTCG.
  - `remaining_exemption = 1,25,000 − max(0, realised LTCG)`, and `harvestable_tax_free_ltcg = min(unrealised LTCG, remaining_exemption)`.
  - It lists loss lots with "Tax Savings" = loss × flat rate (12.5% for long-term, 20% for short-term), aggregated by symbol and sorted by loss.
  - Rates come from `config.py`: `STCG_RATE=0.20`, `LTCG_RATE=0.125`, `LTCG_EXEMPTION_LIMIT=125000`, all overridable by env.
  - `format_tax_plan_markdown` renders the summary into the README; it is called from `analysis.py` (~line 954).
- **Data:** `trades.csv` has about 341 BUY rows and 2 SELL rows (all equity symbols), so realised gains are currently minimal.

### Inferences — gaps and risks in the current code
1. **No harvest order list:** the tool says how much tax-free LTCG is available, but not which lots and how many units to sell. Add a "units to sell per symbol, walking FIFO, to realise exactly X of LTCG" function. Under FIFO a partial sale takes the oldest lots, which matches the legal rule.
2. **No set-off engine:** realised STCL is not applied against STCG then LTCG, and LTCL is not restricted to LTCG. There is no input for carried-forward losses from earlier years (Schedule CFL), and no estimate of tax payable. Net LTCG is used for the exemption, but STCL is ignored.
3. **Overstated "Tax Savings":** each loss is valued at a flat rate without checking for gains to absorb it. An LTCL valued at 12.5% saves nothing if LTCG is below ₹1.25 lakh, and an STCL used against LTCG saves 12.5%, not 20%.
4. **FIFO trap not flagged:** loss lots are listed even when older gain lots of the same symbol must be sold first under FIFO. A candidate should show the net result of a FIFO sale up to and including that lot, not the lot's loss alone.
5. **Holding-period edge:** `> 365 days` can disagree with "more than 12 months" around leap years. Example: bought 28 Feb 2024 and sold 28 Feb 2025 is 366 days, so the code says LTCG, but that is exactly 12 months, not more. Compare calendar months instead (sale date > purchase date + 12 months).
6. **Missing price defaults to 0:** `prices.get(sym, 0.0)` turns a missing CMP into a fake 100% loss candidate.
7. **No asset classes:** debt funds (slab), gold ETFs (12.5%, no exemption) and gold FoFs (24 months) are all treated as equity. The ₹1.25 lakh exemption must only cover STT-paid equity and equity-fund gains.
8. **No grandfathering** for lots before 1 Feb 2018 (FMV on 31 Jan 2018). There is no handling of corporate actions (splits, bonuses, mergers) or same-day buy/sell (intraday/speculative) separation. A SELL with no open lots is silently ignored, and there is no account-wise FIFO across multiple demat accounts.
9. **No cess or surcharge**, no family/PAN dimension, and no link to rebalancing (target weights, bands, SIP routing).

### Gaps
- I did not run the planner on live data, because current prices are needed.

## Monthly / yearly checklist

**Monthly (SIP day)**
1. Update holdings and prices. Compute weights against targets (e.g. 70/20/10).
2. Send the entire SIP to the sleeve furthest below target. No selling.
3. Log each purchase as a lot (date, units, price). Each SIP is its own 12-month clock.

**Semi-annual (April and October)**
4. Check bands (equity 65–75%, debt 15–25%, gold 7.5–12.5%). If all are inside, stop.
5. If a sleeve is outside: can 3–6 months of SIPs fix it? If yes, redirect SIPs. If no, sell the overweight sleeve back to target, using in order: equity lots over 12 months within the exemption → loss lots → lots outside the exit-load window.
6. **Crash trigger (any time):** if equity falls below 65% (e.g. after a 25–30% market fall), sell debt/gold and buy equity back to 70%. Do it within a week.

**Yearly (January–March)**
7. Run `tax_planner.py`. Note realised STCG/LTCG, remaining exemption, and loss candidates (check them against FIFO).
8. Book losses first if you have realised STCG/LTCG worth offsetting. Rebuy on T+1.
9. Harvest LTCG up to the remaining ₹1.25 lakh (per PAN). Sell by about 20 March and rebuy T+1. Record the new lots.
10. Check for lots about to cross 12 months before any planned March sale.
11. Plan regular→direct switches lot by lot within the exemption.

**July (ITR)**
12. File by the due date (typically 31 July for non-audit individuals **[UNVERIFIED for AY2027-28]**). Use ITR-2/3 with schedules CG and CFL. Keep the broker tax P&L and CAS. Pay any advance tax on large gains in the quarter they arise **[UNVERIFIED instalment detail]**.

## Worked examples

All figures are illustrative.

**A. ₹10 lakh at 70/20/10: normal year (no action)**
- Start: equity ₹7.00L, debt ₹2.00L, gold ₹1.00L.
- Returns: equity +25%, debt +7%, gold +10%.
- End: equity ₹8.75L, debt ₹2.14L, gold ₹1.10L. Total ₹11.99L.
- Weights: equity 73.0%, debt 17.8%, gold 9.2%. All inside the bands, so no action. SIPs go to debt (furthest below target).

**B. Equity boom (band breached)**
- End values: equity +40% → ₹9.80L; debt ₹2.14L; gold ₹1.10L. Total ₹13.04L. Equity is at 75.2%, a breach.
- **Option 1 (cash flow):** equity reaches 70% when the total is ₹9.80L ÷ 0.70 = ₹14.0L. That needs about ₹0.96L of new money all into debt/gold, roughly 3.2 months of a ₹30k SIP. Preferred: no tax.
- **Option 2 (sell):** the targets are equity ₹9.128L, debt ₹2.608L, gold ₹1.304L.
  - Sell ₹67,200 of equity. Buy ₹46,800 of debt and ₹20,400 of gold.
  - The equity sleeve has a gain of ₹2.8L on ₹9.8L (28.6%), so the sale realises about ₹19,200 of gain (more if FIFO hits older, cheaper lots).
  - If those lots are over 12 months, it falls inside the ₹1.25L exemption, so tax is ₹0. If the lots are 12 months or less, tax is 20% × ₹19,200 = ₹3,840 + cess.

**C. Crash (equity −30%)**
- From the start: equity ₹4.90L, debt ₹2.14L, gold +15% → ₹1.15L. Total ₹8.19L. Equity is at 59.8%, below 65%.
- Targets: equity ₹5.733L, debt ₹1.638L, gold ₹0.819L.
- Trades: sell ₹50,200 of debt and ₹33,100 of gold, and buy ₹83,300 of equity.
- **Tax on debt:** the gain fraction is ₹14k/₹2.14L = 6.5%, so about ₹3,280 of gain at slab. At 30% that is about ₹985 + cess.
- **Tax on gold ETF:** the gain fraction is ₹15k/₹1.15L = 13%, so about ₹4,320 of gain. Held over 12 months, tax at 12.5% is about ₹540. If held 12 months or less, it is at slab.
- Total tax is about ₹1,500 to restore the 70% equity weight at depressed prices.

**D. LTCG harvesting (equity index fund, FIFO)**
- Lots: A, Mar 2023: 2,000 units @ ₹50. B, Mar 2024: 2,000 units @ ₹70. C, monthly SIPs from Apr 2026 (12 months or less).
- NAV on 10 Feb 2027: ₹100. Realised LTCG so far in FY26-27: ₹0, so the target is ₹1,25,000.
- FIFO: all of lot A (2,000 units × ₹50 gain = ₹1,00,000), then ₹25,000 ÷ ₹30 gain per unit = 833 units of B.
- **Sell 2,833 units** (about ₹2.83L) on 10 Feb. Realised LTCG ₹1,24,990, so tax is ₹0. Rebuy about ₹2.83L on 11 Feb at about ₹100.
- **Effect:** the cost basis on 2,833 units rises from about ₹55.9 average to about ₹100. Future taxable gain falls by ₹1.25L, which defers about ₹15,625 + 4% cess = ₹16,250 of future tax. The new lot is short-term until Feb 2028.
- A spouse and an adult child who own their own fund units can each do the same for another ₹1.25L.

**E. Tax-loss harvesting**
- **This FY:** realised STCG of ₹1.5L (a fund sold after 8 months) and realised LTCG of ₹2.5L.
- **Stock X:** bought Nov 2025, 1,000 shares @ ₹400 (₹4L). Now ₹200, an unrealised STCL of ₹2L (the lot is still 12 months or less in Oct 2026, so book it before Nov 2026 to keep it short-term). It is the only lot of X in the account, so there is no FIFO trap.
- **Without harvesting:** STCG ₹1.5L × 20% = ₹30,000. LTCG (₹2.5L − ₹1.25L) × 12.5% = ₹15,625. Total ₹45,625 + cess.
- **With harvesting:** sell X and rebuy T+1 if still wanted. The STCL of ₹2L offsets the ₹1.5L STCG, leaving STCG at 0. The remaining ₹0.5L offsets LTCG, which becomes ₹2.0L. After the exemption, ₹0.75L × 12.5% = ₹9,375.
- **Saving:** about ₹36,250 + cess.
- **FIFO-trap variant:** if X also had an older lot (bought 2021 @ ₹150), a sale of 1,000 shares would match the 2021 lot first and book a *gain* of ₹50 per share. The loss lot is only reachable after selling the older lot.

**F. Regular→direct switch across two FYs**
- Regular-plan units are worth ₹8L, with an LTCG of ₹2.4L spread evenly across lots over 12 months old.
- Switch about half (gain about ₹1.2L) in Feb–Mar 2027 (FY26-27) and the rest in April 2027 (FY27-28). Both fall within the exemption, so tax is about ₹0, versus 12.5% × (₹2.4L − ₹1.25L) = ₹14,375 if done at once.
- The direct-plan units restart their 12-month clock. Check exit loads (SEBI reportedly waived them for same-scheme regular→direct switches **[verify]**).
