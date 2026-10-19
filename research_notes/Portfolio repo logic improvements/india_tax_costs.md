# Indian Tax and Transaction-Cost Rules for SELL / TRIM / Rebalance Logic (FY 2026-27 = "Tax Year 2026-27")

> **How these notes were researched.** Written 14 Oct 2026. Direct page fetching was blocked in this environment: the proxy refused connections to cleartax.in, zerodha.com, fyers.in, outlookmoney.com and others. Every citation below therefore rests on search-engine result snippets, not on a full reading of the page. Statements marked **[BK]** are background knowledge that no source in this session confirmed. Treat them as items to verify before you hard-code them. Rates are for resident individuals.

## Q1. STCG/LTCG rates, holding periods and the annual LTCG exemption for listed equity and equity ETFs; Budget 2025/2026; Income-tax Act 2025; grandfathering

### Takeaway
The regime set on 23 Jul 2024 still applies in FY 2026-27, and Budget 2025 and Budget 2026 did not change it:
- **STCG:** 20% if held 12 months or less.
- **LTCG:** 12.5% if held more than 12 months, with no indexation.
- **Annual exemption:** ₹1.25 lakh per taxpayer per year, applied to net LTCG.

The Income-tax Act 2025 replaced the 1961 Act on 1 Apr 2026. Section 111A became s.196 and s.112A became s.198. The substance is unchanged and STT on the transfer is still a condition. Grandfathering at the 31 Jan 2018 fair market value (FMV) still matters, but only for lots bought before 1 Feb 2018.

### Cited Findings
- **LTCG on listed equity:** taxed at 12.5% without indexation for sales on or after 23 Jul 2024. The ₹1.25 lakh exemption applies every year — [ClearTax](https://cleartax.in/s/long-term-capital-gains-on-shares); [Aditya Birla Capital](https://www.adityabirlacapital.com/abc-of-money/long-term-capital-gain-on-shares)
- **How the exemption is applied:** it is deducted from the gains when computing tax, not from total income. Chapter VI-A deductions and the s.87A rebate cannot be used against s.112A LTCG — [ClearTax](https://cleartax.in/s/long-term-capital-gains-on-shares)
- **Budget 2025:** made no change to s.112A LTCG taxation — [Business Today](https://www.businesstoday.in/amp/personal-finance/tax/story/tax-calculation-what-ltcg-exemptions-are-available-under-new-tax-regime-check-details-460044-2025-01-08)
- **Exemption scope:** it is per taxpayer per financial year, summed across all equity and equity-fund sales. It is not per stock — [InCred Money](https://www.incredmoney.com/knowledge-center/share-market/tax-loss-harvesting-in-india-everything-you-need-to-know-to-save-on-capital-gains/)
- **ITR-1:** taxpayers whose LTCG is ₹1.25 lakh or less can file ITR-1 — [Business Standard](https://www.business-standard.com/amp/economy/news/individual-taxpayers-with-ltcg-up-to-1-25-lakh-can-use-simplified-itr-1-125043001472_1.html)
- **s.196 of the Income-tax Act 2025 (replaces 111A):**
  - It covers STCG on equity shares, units of equity-oriented funds and units of business trusts, where STT is charged on the transfer.
  - The rate is 20%.
  - A resident individual or HUF can use any unused basic exemption limit to reduce these gains.
  - Sections 196 and 198 correspond to 111A and 112A and apply from 1 Apr 2026.
  - Sources: [Income Tax Dept – s.196](https://www.incometaxindia.gov.in/w/section-196-78); [Income Tax Dept – s.198](https://www.incometaxindia.gov.in/w/section-198-78); [ebizfiling](https://ebizfiling.com/blog/section-196-and-198-short-term-and-long-term-capital-gains/)
- **s.198 (replaces 112A):** taxes LTCG above ₹1,25,000 at 12.5%. Only a commentary site states this rate; I could not read the official text — [ebizfiling](https://ebizfiling.com/blog/section-196-and-198-short-term-and-long-term-capital-gains/)
- **New Act framework:**
  - The 2025 Act replaces the 1961 Act from 1 Apr 2026.
  - "Previous year" becomes "tax year" (s.3).
  - Holding periods are standardised at 12 months for listed assets and 24 months for others.
  - Sources: [TaxHeal mapping](https://www.taxheal.com/?p=116245); [eztax mapping](https://eztax.in/income-tax-act-2025/compare-old-new-section-codes)
- **Budget 2026 (1 Feb 2026):**
  - STT on futures rose from 0.02% to 0.05%, and on options from 0.10% to 0.15%.
  - STT on equity delivery and mutual funds is unchanged.
  - Buyback proceeds are now taxed as capital gains for all shareholders. Promoters face an effective 22% (corporate) or 30% (non-corporate).
  - No other change to general capital-gains rates was reported.
  - Sources: [Business Today](https://www.businesstoday.in/amp/markets/stocks/story/budget-2026-fm-sitharaman-raises-stt-on-fo-trades-signals-tighter-market-oversight-513932-2026-02-01); [Outlook Money](https://www.outlookmoney.com/invest/union-budget-2026-buyback-proceeds-to-be-taxed-as-capital-gains-stt-raised-on-futures-and-options); [Fyers](https://fyers.in/blog/union-budget-2026-highlights/)
- **s.87A rebate:** from FY 2025-26 (Finance Act 2025 proviso) it applies only to tax at slab rates. It cannot be used against s.111A STCG or s.112A LTCG — [TaxGuru](https://taxguru.in/?p=1022823); [Freefincal](https://freefincal.com/is-87a-rebate-applicable-for-capital-gains-after-budget-2025/)
- **Grandfathering for listed shares bought before 1 Feb 2018:**
  - Cost of acquisition = the higher of (a) the actual cost and (b) the lower of the 31 Jan 2018 FMV and the sale price.
  - Grandfathering cannot create a long-term capital loss (LTCL).
  - Bonus shares allotted before 31 Jan 2018 also get the benefit.
  - Sources: [Business Standard](https://www.business-standard.com/amp/article/pf/how-to-minimise-your-tax-liability-on-the-sale-of-your-bonus-shares-118022400813_1.html); [equitiesindia](https://equitiesindia.com/glossary/tax-on-bonus-shares)

### Inferences
- **Config values for FY 2026-27:**
  - `STCG_EQUITY = 20%`
  - `LTCG_EQUITY = 12.5%`
  - `LTCG_EXEMPTION = 125000`
  - `LT_THRESHOLD_LISTED = held > 12 months`
  - Add 4% health and education cess to both rates. The surcharge on these gains is capped at 15% **[BK]**.
  - Effective marginal rates before surcharge are about 20.8% (STCG) and 13.0% (LTCG).
- **What "more than 12 months" means:** a lot becomes long-term on the day after its 1-year anniversary **[BK]**. To be safe, the tool should require that the sell date is later than the buy date plus 12 months. A conservative rule is `sell_date >= buy_date + 12 months + 1 day`.
- **Rate cliff:** if a lot is within about 60 days of turning long-term, the rate drops from 20.8% to 13%, or to 0% inside the exemption. A trim recommendation should flag this and suggest deferring unless the thesis is broken.
- **Grandfathering:** only needed if `trades.csv` contains buys dated before 1 Feb 2018. The code would also need a per-ISIN table of 31 Jan 2018 FMVs, i.e. the highest price on that day. Otherwise it can be skipped and logged as "not modelled".
- **Low-income households:** because of the unused basic exemption limit adjustment, gains can be fully tax-free. This is an edge case and does not need to be modelled.

### Gaps
- I could not read the official s.198 text to confirm the ₹1.25 lakh and 12.5% figures under the 2025 Act. Commentary says they carried over unchanged.
- I did not confirm that the grandfathering formula (old s.55(2)(ac)) is carried into the 2025 Act. I assume it is, because the Act was billed as a no-policy-change rewrite.
- I did not verify the surcharge cap or the 4% cess for 2026-27 **[BK]**.

## Q2. Gold ETFs and silver ETFs

### Takeaway
Gold and silver ETFs are listed securities but not equity-oriented funds:
- **Long-term:** held more than 12 months. Taxed at 12.5% with no indexation and **no** ₹1.25 lakh exemption.
- **Short-term:** held 12 months or less. Taxed at slab rates, typically 30% plus cess for a high earner.
- **Gold fund-of-funds:** these are unlisted, so they need more than 24 months to be long-term.

### Cited Findings
- **Rates:**
  - Held 12 months or less: STCG at slab rates.
  - Held more than 12 months: LTCG at 12.5% with no indexation, plus surcharge and cess.
  - Classification: listed non-equity securities.
  - The ₹1.25 lakh equity exemption does not apply.
  - Sources: [Zerodha Fund House](https://www.zerodhafundhouse.com/blog/gold-etf-taxation-2025/); [Business Standard](https://www.business-standard.com/finance/personal-finance/gold-and-silver-surge-know-how-etfs-are-taxed-before-you-invest-in-them-125101000906_1.html); [Aditya Birla Capital](https://www.adityabirlacapital.com/abc-of-money/tax-on-gold-etf)
- **Gold FoFs and physical gold:** need more than 24 months for the 12.5% rate — [Finnovate](https://www.finnovate.in/learn/blog/taxation-of-gold-in-india-explained)
- **Transition rules (sources conflict):**
  - One source says the 12-month rule applies to units sold on or after 1 Apr 2025.
  - An HDFC AMC leaflet sets out separate rules for redemptions between 23 Jul 2024 and 31 Mar 2025, depending on acquisition date.
  - Sources: [HDFC AMC leaflet](https://files.hdfcfund.com/s3fs-public/Others/2024-08/Gold%20and%20Silver%20simplified%20taxation%20Leaflet%20(August%202024).pdf); [TaxGuru](https://taxguru.in/?p=1059604)

### Inferences
- **Why the dates conflict:** this matches my understanding **[BK]** that Finance (No. 2) Act 2024 narrowed the definition of a "specified mutual fund" (s.50AA) to funds with more than 65% in debt, effective for transfers from 1 Apr 2025. Before that, gold ETFs bought on or after 1 Apr 2023 were taxed at slab rates however long they were held. For any sale in FY 2026-27 the transition no longer matters: the tool should apply >12 months → 12.5% LT and ≤12 months → slab rate.
- **Tool logic:**
  - Use an `asset_class` field with values {`equity`, `equity_etf`, `gold_etf`, `silver_etf`}.
  - Gold and silver LTCG must **not** use the ₹1.25 lakh exemption.
  - Gold and silver STCG is taxed at the user's slab rate. Add a config field `SLAB_RATE`, defaulting to 30% plus 4% cess = 31.2%.
  - So selling a gold or silver ETF lot held under 12 months costs about 31% of the gain, versus about 13% after 12 months. That is a much bigger cliff than for equity.
- **Loss set-off:** gold and silver ETF losses are ordinary capital losses. They can be set off against equity capital gains, and vice versa, under the normal STCL/LTCL rules in Q3.

### Gaps
- No search result confirmed the current STT treatment of gold ETFs. I believe they carry no STT because they are not equity-oriented **[BK]**.

## Q3. Set-off and carry-forward; wash-sale rule; tax-loss and tax-gain harvesting caveats

### Takeaway
- **Set-off:** short-term capital loss (STCL) can be set off against both STCG and LTCG. LTCL can only be set off against LTCG.
- **Carry-forward:** unused losses carry forward for 8 years, but only if the ITR is filed by the s.139(1) due date.
- **Wash sales:** India has no statutory wash-sale rule. However, selling and rebuying the same stock on the same day is treated as an intraday trade, which ruins the harvest. The general anti-avoidance and sham-transaction doctrine is a residual risk.

### Cited Findings
- **Set-off and carry-forward rules:**
  - STCL can be set off against STCG and LTCG.
  - LTCL can be set off only against LTCG.
  - Unused losses carry forward for up to 8 assessment years.
  - Carry-forward requires the ITR to be filed by the s.139(1) due date; a late return forfeits it.
  - Source: [Angel One](https://angelone.in/knowledge-center/share-market/wash-sale); [Kotak Securities](https://kotaksecurities.com/share-market/what-is-wash-sale-rule); [share.market](https://www.share.market/buzz/learn/tax-loss-harvesting/)
- **No wash-sale rule:** India has no rule that automatically disallows a loss when the same stock is bought back within a set window — [Kotak Securities](https://kotaksecurities.com/share-market/what-is-wash-sale-rule); [Angel One](https://angelone.in/knowledge-center/share-market/wash-sale)
- **Anti-avoidance risk:**
  - The tax department may dispute losses from circular, pre-arranged trades with no investment purpose, using GAAR or substance-over-form principles.
  - One dissenting blog advises waiting more than 30 days, or buying a similar but not identical asset. This is a conservative opinion, not law.
  - Source: [Angel One](https://angelone.in/knowledge-center/share-market/wash-sale)
- **Same-day rebuy:**
  - Zerodha support staff say that selling from holdings and buying back the same day counts as an intraday transaction, because no shares leave the demat account.
  - Rebuy the same stock on a later day, after settlement. Buying a *different* stock the same day is fine.
  - Tax-loss harvesting applies only to delivery holdings.
  - Sources: [TradingQnA](https://tradingqna.com/t/tax-loss-harvesting-effective-way/144717); [Zerodha Z-Connect](https://zerodha.com/z-connect/taxation-for-traders/tax-loss-harvesting); [Quicko](https://learn.quicko.com/?p=25510)
- **Gain harvesting:** after a sell and rebuy, the holding-period clock restarts from the new purchase date — [InCred Money](https://www.incredmoney.com/knowledge-center/share-market/tax-loss-harvesting-in-india-everything-you-need-to-know-to-save-on-capital-gains/)

### Inferences
- **Harvesting losses can waste them.** Under s.112A/s.198 the ₹1.25 lakh exemption applies to LTCG *after* set-off **[BK, consistent with the CBDT FAQ cited by ClearTax]**. If the user's realised LTCG for the year is under ₹1.25 lakh, booking a loss saves no tax this year and only uses up the loss. The tool should therefore:
  - estimate the year's realised STCG and LTCG from `trades.csv`, plus the gains from proposed trims;
  - recommend harvesting only when it reduces taxable gains: STCG greater than 0, or LTCG above ₹1.25 lakh;
  - otherwise **defer**. The exception is a loss that is otherwise idle, such as LIC at −₹39k. Booking it in a year with no gains still produces a carry-forward worth up to 20.8% (STCL) or 13% (LTCL), but only if the user files the ITR on time.
- **Long-term vs short-term losses:** an STCL is more valuable than an LTCL, because it can offset 20%-taxed STCG. Check whether the LIC and Wipro losing lots are long-term or short-term. If a losing lot is about to turn long-term, harvesting it *before* it does keeps the loss short-term, which is more flexible.
- **Tax-gain harvesting:** each year, realise about ₹1.25 lakh of LTCG minus any LTCL already booked, then rebuy on the **next** trading day (India settles T+1). This permanently steps up the cost basis tax-free. Two downsides:
  - each round trip costs about 0.22% plus DP fees (see Q5);
  - the new lots restart the 12-month clock, so for one year any sale becomes STCG.

  The tool should exclude gain-harvested lots from trim candidates for 12 months, or flag them.
- **Planned LIC and Wipro harvest:**
  - Rebuying the same scrip is allowed in law, but wait at least one trading day. A same-sector substitute (e.g. Wipro → another IT name, or an IT ETF) avoids any sham-transaction argument.
  - The tool should add a `harvest_rebuy_after_days` config, defaulting to 1. Optionally add a conservative mode at 30 days.

### Gaps
- I found no CBDT circular aimed specifically at tax-loss harvesting. The anti-avoidance basis is general doctrine (McDowell 1985 and GAAR **[BK]**), not a rule targeting harvesting.
- I did not confirm the order in which the ITR utility sets off STCL against STCG and LTCG. I believe the taxpayer may set STCL against the higher-taxed STCG first **[BK]**.
- I did not confirm the 2025 Act section numbers for set-off and carry-forward (old ss.70, 74, 80, 139(1)).

## Q4. FIFO lot matching in demat; corporate-action adjustments

### Takeaway
- **FIFO:** for demat holdings, FIFO matching is mandatory under CBDT Circular 768 (1998), and is applied within each demat account.
- **Holding period:** runs from the trade date on the contract note, not the settlement date.
- **Bonus shares:** cost is nil and the holding period runs from the allotment date.
- **Splits:** keep the original acquisition date and spread the cost across the new shares.
- **Demergers:**
  - Cost is split between parent and resulting company by net book value / net worth (old s.49(2C)/(2D)), using a ratio the company publishes.
  - The resulting company's shares inherit the original acquisition date.

### Cited Findings
- **Circular 768 (24 Jun 1998):** for dematerialised securities, sets the date of transfer and the holding period. Its example treats the earliest-acquired shares as sold first, i.e. FIFO — [Income Tax Dept – Circular 768](https://www.incometaxindia.gov.in/w/768-circular-no.-768-dated-24-6-1998-1)
- **Holding period start:** it runs from the date of the broker's contract note (Circular 704), and this applies to demat shares — [Calcutta HC, Nawal Kishore Kejriwal (via itatonline)](https://itatonline.org/digest/nawal-kishore-kejriwal-v-cit-2024469-itr-543-151-taxmann-com-117-calhc); [TMI](https://www.taxmanagementindia.com/web/tmi_blog_details.asp?id=180041)
- **Multiple demat accounts:** FIFO is applied within each demat account — [Business Standard](https://www.business-standard.com/finance/personal-finance/explained-how-to-calculate-capital-gains-tax-on-multiple-demat-accounts-124080200149_1.html)
- **Bonus shares:**
  - Cost of acquisition is nil.
  - Holding period runs from the allotment date.
  - Under FIFO, the original shares are sold before the bonus shares.
  - Sources: [equitiesindia](https://equitiesindia.com/glossary/tax-on-bonus-shares); [Studycafe](https://studycafe.in/?p=425370); [Business Standard](https://www.business-standard.com/amp/article/pf/how-to-minimise-your-tax-liability-on-the-sale-of-your-bonus-shares-118022400813_1.html)
- **Demergers:**
  - Cost of the resulting company's shares = original cost × (net book value of assets transferred ÷ net worth of the demerged company). The parent's cost is reduced by the same amount.
  - Companies publish this ratio in exchange filings (e.g. Strides 7.20%).
  - The resulting company's shares take the original acquisition date.
  - Sources: [Strides disclosure](https://www.strides.com/pdf/pressrelease/2018/intimation_to_se_on_cost_of_acquisition_20180420.pdf); [Allcargo NSE filing (2025)](https://nsearchives.nseindia.com/corporate/ALLCARGO_27112025173123_Cost_of_aquisition_Signed.pdf); [Motherson](https://www.motherson.com/storage/Corporate%20Announcements/FY%202021-22/Stock-Exchange-Disclosure-ApportionmentofCost-12JAN22.pdf)

### Inferences
- **The current cost basis is the wrong one for tax.** `refresh_portfolio.py` uses a rolling average cost, where a SELL keeps the average. That is fine for showing returns but **wrong for tax**. Tax needs a FIFO lot ledger, built from `trades.csv` and keyed by (symbol, account), with fields `buy_date`, `qty_remaining`, `unit_cost`, `source` ∈ {buy, bonus, split, demerger, rights}. The tool cannot pick which lots to sell, so the realised gain on a trim is fixed by FIFO.
- **Practical impact of forced FIFO:**
  - Selling part of a position always sells the oldest lots first. These usually carry the biggest gains but are also usually long-term.
  - The tool **cannot** pick high-cost lots to shrink the realised gain. "Tax-aware trim" therefore means choosing **which symbol** and **how many shares** to sell (stopping where FIFO crosses from long-term into short-term lots), not which lot.
- **Corporate actions to model:**
  - **Split / consolidation:** multiply quantity and divide unit cost by the ratio; keep `buy_date`.
  - **Bonus:** add a zero-cost lot dated on the allotment date. The FIFO position is by allotment date.
  - **Demerger:** create a child lot with cost = parent cost × ratio and the parent's `buy_date`, and reduce the parent cost by the same amount. Read the ratio from a `corporate_actions.csv`.
  - **Rights issues:** treat as a new buy at the subscription date and price **[BK]**.
- **Holding period dates:** use the trade date (contract-note date) in `trades.csv` as `buy_date`. Do not use the settlement date.

### Gaps
- No source in this session stated the stock-split rule. "Keep the original date, divide the cost" is standard practice **[BK]**.
- I found no 2025 Act section numbers for the old 49(2C)/(2D), 55(2)(aa) or 2(42A).
- I could not confirm whether CBDT has re-issued Circular 768 under the 2025 Act. The FIFO principle is in the statute itself (old s.45(2A)) **[BK]**.

## Q5. Transaction costs per delivery trade; round-trip cost; sensible minimum trade size

### Takeaway
For delivery equity at a zero-brokerage discount broker such as Zerodha:
- **Buy:** about 0.119% of value.
- **Sell:** about 0.104% of value, plus a flat DP charge of about ₹15.34 per scrip per day.
- **Round trip:** about 0.22% plus ₹15.34.

STT is 0.1% on each side and dominates the cost. Equity ETFs and gold ETFs pay little or no STT **[BK]**, so they are far cheaper to trade.

### Cited Findings
- **Zerodha equity delivery charges:**
  - Brokerage: ₹0.
  - STT: 0.1% on buy and on sell.
  - SEBI fee: ₹10 per crore.
  - Stamp duty: 0.015% on the buy side only.
  - GST: 18% on (brokerage + SEBI fee + transaction charges).
  - NSE transaction charge (cached pages disagree): 0.00322% on one version, 0.00307% on another. The 0.00297% figure that took effect from Oct 2024 was not confirmed.
  - Source: [Zerodha charges](https://www.zerodha.com/charges); [Zerodha charges (alt)](https://zerodha.com/charges?c=ZMPQWC)
- **DP charge:**
  - ₹13 + 18% GST = ₹15.34 per scrip per day on sells (₹15.05 for a female primary holder).
  - It is per scrip, not per share. Two sells of the same stock on the same day count once.
  - Source: [Finology](https://select.finology.in/articles/broker/dp-charges-in-zerodha)
- **Budget 2026:** STT on equity delivery is unchanged — [Fyers](https://fyers.in/blog/union-budget-2026-highlights/)

### Inferences (computed from the cited schedule, using a 0.00307% transaction charge)

| Trade value | Buy cost | Sell cost (incl. DP ₹15.34) | Round trip | % of value |
|---|---|---|---|---|
| ₹5,000 | ₹5.9 | ₹20.5 | ₹26 | 0.53% |
| ₹10,000 | ₹11.9 | ₹25.7 | ₹38 | 0.38% |
| ₹25,000 | ₹29.7 | ₹41.3 | ₹71 | 0.28% |
| ₹50,000 | ₹59 | ₹67 | ₹126 | 0.25% |
| ₹1,00,000 | ₹119 | ₹119 | ₹238 | 0.24% |

How the rates in the table break down:
- **Buy side:** 0.1% STT + 0.015% stamp duty + about 0.0031% transaction charge + 0.0001% SEBI fee + about 0.0006% GST = about 0.1188%.
- **Sell side:** about 0.1038% + ₹15.34.

What this means for the tool:
- **Minimum trade size:** the fixed DP charge stops mattering above about ₹25k. Below about ₹10k, a sell costs more than 0.25%.
- **Recommended setting:** `MIN_TRADE_VALUE = ₹10,000`, with a soft warning below ₹25k. Also suppress any trim smaller than 2–3% of the position *and* below ₹10k.
- **Batch trims:** combine all trims of one scrip into a single day, because the DP charge is per scrip per day.
- **Equity ETFs (Nifty, Bank, IT, Smallcap, Midcap BeES etc.):**
  - STT on sale of equity-oriented fund units on the exchange is 0.001%, and nil on purchase **[BK — verify]**.
  - That makes the round trip about 0.03% plus DP charge.
  - ETFs are therefore the cheapest instruments for rebalancing and for gain or loss harvesting.
- **Gold and silver ETFs:** no STT **[BK — verify]**, so cost is mainly stamp duty, exchange charges and DP.
- **Total cost of a trim:** transaction cost plus tax on the realised gain. Tax dominates: a trim realising 50% gain as STCG costs about 10% of the trade value in tax, against about 0.1% in charges.

### Gaps
- I could not fetch the live NSE circular to get the exact FY 2026-27 transaction charge. The difference between candidate rates is about 0.0003% and does not matter here.
- I did not verify the STT rates for ETF units, or whether gold ETFs are exempt.
- Other brokers' DP charges vary, roughly ₹13–25. Make the charge configurable.

## Q6. Dividend taxation and TDS

### Takeaway
- **Tax:** dividends are taxed at the investor's slab rate.
- **TDS:** 10% is deducted when dividends from one company exceed ₹10,000 in a year (threshold raised from ₹5,000 on 1 Apr 2025).
- **Budget 2026:** removed the deduction for interest paid to earn dividends (2025 Act s.93).
- **Buybacks:** from 1 Apr 2026, buyback proceeds are taxed as capital gains, not as deemed dividend.

### Cited Findings
- **TDS threshold:** rose from ₹5,000 to ₹10,000 per company or mutual fund per financial year from 1 Apr 2025. Dividends are taxed at slab rates on the gross amount — [Motilal Oswal](https://www.motilaloswal.com/personal-finance/tax/dividend-tax-guide-2025-rates-tds-new-rules); [mStock](https://www.mstock.com/articles/avoid-tds-on-dividend-income-fy-2025-26)
- **Interest deduction removed:**
  - Finance Bill 2026 amends s.93(2) of the 2025 Act, so no deduction is allowed for interest incurred to earn dividends or mutual fund income. Previously up to 20% of the dividend could be deducted.
  - Sources disagree on whether this applies from tax year 2025-26 or 2026-27.
  - Sources: [Freefincal](https://freefincal.com/?p=336743); [CA Rajput](https://carajput.com/blog/no-interest-deduction-allowed-against-dividend-income/)
- **Buybacks:** from 1 Apr 2026, buyback proceeds are taxed as capital gains for all shareholders — [Outlook Money](https://www.outlookmoney.com/invest/union-budget-2026-buyback-proceeds-to-be-taxed-as-capital-gains-stt-raised-on-futures-and-options)

### Inferences
- **Dividends rarely change a hold or sell decision.** For a 30%-bracket investor, a dividend costs about 31.2% in tax. Capital gains are taxed at about 13% (long-term) or 0% within the exemption.
  - This tilts gently toward growth or low-payout holdings and accumulating ETFs.
  - It does not justify trades by itself, given transaction costs.
- **Dividend and bonus stripping [BK — verify]:** these rules (old ss.94(7)/(8)) disallow a loss on securities bought within 3 months before a record date and sold soon after.
  - Dividend stripping: sold within 3 months after the record date; the loss is disallowed up to the dividend received.
  - Bonus stripping: original shares sold within 9 months after a bonus record date; the loss is ignored and added to the cost of the bonus shares.
  - The tool should flag a harvest candidate bought within 3 months before a recent record date.
- **Buyback tenders:** treat these like any other sale for capital gains purposes, using FIFO and holding period.

### Gaps
- The effective year of the s.93 change is inconsistent across sources.
- I found no 2025 Act section number for dividend TDS (old s.194).
- I did not verify that ss.94(7)/(8) continue in the 2025 Act.

## Recommended changes for the repo
*(Synthesis built on the cited findings above; items depending on [BK] are marked.)*

1. **Configuration (`config.py`).** Add a `TAX` block holding these values:
   - Rates: `STCG_EQUITY=0.20`, `LTCG_EQUITY=0.125`, `LTCG_EXEMPTION=125000`, `CESS=0.04`.
   - User inputs: `SLAB_RATE=0.30` (user-set; used for gold/silver STCG and dividends), `SURCHARGE=0.0` (user-set; capped at 0.15 on equity gains **[BK]**).
   - Holding periods: `LT_MONTHS_LISTED=12` for listed equity, equity ETFs and gold/silver ETFs; `LT_MONTHS_UNLISTED=24` for gold FoFs and unlisted holdings.
   - Exemption scope: `EXEMPTION_APPLIES={'equity','equity_etf'}`.
   - Costs: `STT_DELIVERY=0.001`, `STT_ETF_SELL=0.00001` **[BK]**, `STAMP_BUY=0.00015`, `EXCH_TXN=0.0000307`, `SEBI_FEE=0.000001`, `GST=0.18`, `DP_CHARGE=15.34`.
   - Trading thresholds: `MIN_TRADE_VALUE=10000`, `HARVEST_REBUY_AFTER_DAYS=1` (option of 30).
   - Version the block as `TAX_RULES_VERSION="FY2026-27 / Income-tax Act 2025 ss.196/198"` so the rules can be revisited after each Budget.
2. **Asset classification.** Add an `Asset_Class` column to `portfolio.csv`, or an ISIN/symbol map, with values {equity, equity_etf, gold_etf, silver_etf}. GOLDBEES and SILVERBEES-type ETFs must not get the ₹1.25 lakh exemption, and their STCG uses the slab rate.
3. **FIFO lot ledger.** Add a new module, e.g. `lots.py`:
   - Rebuild lots from `trades.csv` per (symbol, account) using strict FIFO, with dates from the contract-note trade date (Circular 768).
   - Keep `refresh_portfolio.py`'s average cost for display only.
   - Each lot records `qty, unit_cost, buy_date, is_long_term(as_of), days_to_LT, unrealised_gain`.
   - Apply corporate actions from a new `corporate_actions.csv`:
     - split: scale quantity and cost, keep date;
     - bonus: zero-cost lot on allotment date;
     - demerger: carve out cost by the company-published ratio and keep the parent's date.
   - Grandfathering: if any lot is dated before 1 Feb 2018, apply the formula when an FMV value is available; otherwise warn.
4. **Tax-aware trim sizing.** Selling is forced FIFO, so for any proposed SELL or TRIM of N shares:
   - Simulate which lots are consumed, then report realised STCG/LTCG, estimated tax and charges, and net proceeds.
   - Prefer a quantity that stops before FIFO reaches short-term lots.
   - If the next lot turns long-term within `LT_DEFER_DAYS` (suggest 60), recommend deferring unless the signal is a hard thesis break or stop.
   - Across symbols, rank trim candidates by tax drag per rupee raised, e.g. tax ÷ proceeds. Prefer equity ETFs and long-term lots inside the remaining exemption.
5. **Annual exemption tracker.** Compute the year's realised LTCG and STCG so far from `trades.csv`, for the tax year April to March, then:
   - Allocate the remaining exemption to recommended long-term trims first.
   - Before 31 March, suggest gain harvesting up to the remaining exemption, net of any LTCL already booked. Rebuy on the next trading day, mark the new lots as restarting the 12-month clock, and exclude them from trims.
6. **Tax-loss harvesting module.** For lots with unrealised losses (e.g. LIC −₹39k, Wipro −₹7k):
   - Label each loss as short-term or long-term.
   - Recommend harvesting only if (a) realised or planned STCG is greater than 0, or (b) LTCG exceeds ₹1.25 lakh, or (c) the user opts into carry-forward. Warn that carry-forward needs an ITR filed by the due date.
   - Prefer harvesting before a losing lot turns long-term, because an STCL can offset 20% STCG.
   - Never rebuy the same day. Suggest a next-day rebuy or a same-sector or ETF substitute.
   - Flag the s.94(7)/(8) record-date window **[BK]**.
7. **Minimum trade and cost model.**
   - Suppress trades below `MIN_TRADE_VALUE`.
   - Combine trims of the same scrip into one day (one DP charge).
   - Show `cost = charges + tax` next to every recommendation.
   - Rebalancing bands should exceed about 0.25% round-trip cost plus expected tax. In practice, rebalance only on drift of 5 percentage points or more, or use new cash, ETFs or dividends to rebalance instead of selling.
8. **Disclaimers and recheck items.** Show "estimate, not tax advice". Re-verify these before relying on them:
   - the s.198 figures in the official Act text;
   - ETF and gold-ETF STT;
   - the effective date of the s.93 interest change;
   - the surcharge cap.
