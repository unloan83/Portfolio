# Tax-aware transition plan: from 34 holdings to an index core plus a capped satellite (numbers from the repo)

**Scope and method.**
- **Inputs:** every number here comes from `portfolio.csv`, `trades.csv`, `data/corporate_actions.csv` and the last run in `re-engineering.csv` (2026-10-15).
- **Prices:** the base case uses the `portfolio.csv` prices (broker snapshot dated 2026-09-26). A sensitivity check uses the 2026-10-15 prices in `re-engineering.csv`. Nothing was fetched.
- **Dates:**
  - Valuation and plan date: **2026-10-16**.
  - A lot counts as long-term (LT) when the sale date is on or after buy date + 12 months + 1 day.
- **Lot matching:** FIFO lots are built from `trades.csv`, adjusted for the bonus and demerger events in `data/corporate_actions.csv`.
- **Calculator:** `research_notes/Near certain investing playbook/transition.py`. Run it with `python3 transition.py` (base case) or `python3 transition.py reeng` (2026-10-15 prices). It is deterministic and writes no repo files.
- **Tax rules** come from the repo's own earlier research note (`research_notes/Portfolio repo logic improvements/india_tax_costs.md`). Its citations are repeated below.
- **This is not tax advice.** The target allocation is an **example only**. The user picks the real targets.

**Tax assumptions used in the calculator** (each one is a flag):
- **Listed equity and equity ETFs:**
  - Short-term capital gains (STCG): 20%.
  - Long-term capital gains (LTCG): 12.5% on the amount above ₹1.25 lakh per financial year (FY). The exemption is per taxpayer and applies after set-off.
- **Cess:** 4% cess is added. Surcharge is ignored.
- **Gold and silver ETFs:**
  - Short-term gains are taxed at the slab rate, assumed to be 30% + cess.
  - Long-term gains (after 12 months) are taxed at 12.5% with no exemption.
- **Set-off order:**
  - Short-term capital loss (STCL) is applied first to the highest-taxed short-term gain, then to LTCG.
  - Long-term capital loss (LTCL) is applied only to LTCG.
  - **[BK]** I assume the taxpayer can choose this order.
- **STT and charges:**
  - STT: 0.1% on stock sales, 0.001% on equity-ETF sales, 0 on gold and silver ETFs **[BK]**.
  - DP charge: about ₹15/scrip/day, mentioned but not modelled.
- **Realised gains so far in FY 2026-27:** zero assumed. `trades.csv` has no SELL rows after 2024-10-04. Any sales in other accounts, or mutual fund redemptions, would use up the same ₹1.25 lakh exemption.

---

## Q1. Current allocation, concentration and sectors (prices of 2026-09-26)

### Takeaway
The portfolio is worth **₹6,75,074**:
- **82.3%** is in 27 individual stocks.
- **5.3%** is in equity ETFs: 4.7% in broad ETFs (ICINIF, HDF250, MIR150) and 0.6% in sector ETFs (NIPNIT, KOTAKBKETF).
- **12.4%** is in gold and silver ETFs.

Concentration:
- Two stocks, RELIND (14.9%) and HDFBAN (14.3%), make up **29.2%**.
- The top 10 holdings make up **71.4%**.
- Oil & Gas is the largest sector at 19.7%, then Banking at 16.4% (stocks only).

There is **no debt allocation at all**.

### Cited Findings
- **Per-symbol inputs:** quantity, average cost and current market price come from the broker snapshot — `portfolio.csv` (repo, as of 2026-09-26)
- **Bucket totals:**
  - Stocks: ₹5,55,892 (82.35%).
  - Broad equity ETFs: ₹31,442 (4.66%). ICINIF is ₹22,877 (3.39%), MIR150 ₹4,470 and HDF250 ₹4,096.
  - Sector ETFs: ₹4,212 (0.62%). NIPNIT is ₹2,453 and KOTAKBKETF ₹1,760.
  - Gold and silver: ₹83,528 (12.37%). ICIPSE (silver) is ₹50,248 (7.44%) and ICIGOL (gold) ₹33,280 (4.93%).
  - Source: calculator on `portfolio.csv`
- **Top 10 holdings (71.4% in total):**

  | Holding | Weight |
  |---|---|
  | RELIND | 14.87% |
  | HDFBAN | 14.34% |
  | ICIPSE | 7.44% |
  | WIPRO | 6.66% |
  | TATGLO | 5.24% |
  | ICIGOL | 4.93% |
  | LIC | 4.87% |
  | BHAELE | 4.87% |
  | JSWENE | 4.76% |
  | ICINIF | 3.39% |

  Source: calculator
- **Sector weights** (direct stock holdings only; sector labels from the `re-engineering.csv` 2026-10-15 run):

  | Sector | Weight | Holdings |
  |---|---|---|
  | Oil & Gas | 19.69% | RELIND, ONGC, GAIL, HINPET, PETLNG, GUJGA |
  | Banking | 16.39% | HDFBAN, FEDBAN; +0.26% via KOTAKBKETF |
  | Power | 9.45% | JSWENE, NTPGRE, SJVLIM, NHPC, NTPC, TATPOW |
  | IT | 6.66% | WIPRO; +0.36% via NIPNIT |
  | Consumption | 5.24% | |
  | Insurance | 4.87% | |
  | Defense | 4.87% | |
  | Financial Services | 3.96% | |
  | Telecom | 3.11% | |
  | Consumer Electronics | 2.93% | |
  | Auto | 2.44% | |
  | Pharma | 1.55% | |
  | Infrastructure | 1.19% | |

  Source: `re-engineering.csv`; calculator
- **Repo risk limits and the last run's verdicts:**
  - The repo's own limits are `MAX_POSITION_PCT` 8% and `MAX_SECTOR_PCT` 25% — `config.py`
  - The 2026-10-15 run says TRIM for HDFBAN (62 sh) and RELIND (35 sh), and also TRIM for JSWENE.
  - It says SELL for ICIGOL, ICIPSE, WIPRO, LIC, NTPGRE and SJVLIM.
  - It says VERIFY DATA for ENGIND and GUJGA.
  - Source: `re-engineering.csv` (last run)

### Inferences
- **The equity "core" today is only 4.7% of the portfolio.** Reaching a 60% core means redeploying about ₹3.7 lakh.
- **Overlap with the index:** HDFBAN and RELIND are the two largest Nifty 50 weights **[BK]**. Keeping them as satellites on top of a Nifty core double-counts them. The guide should mention this.
- **Price sensitivity:** at the 2026-10-15 prices the portfolio is worth ₹6,23,577 (−7.6%). The broker's unrealised P&L turns from +₹37,723 to −₹13,774. Silver ETF fell from 260 to 206 and LIC from 411 to 394.

### Gaps
- The sector view does not look through ETF holdings. `data/etf_constituents_2026_10.json` exists but was not used.
- The gold and silver split matters: the example target says "10% gold", but today's bucket is 60% silver.

---

## Q2. Per-holding unrealised gain/loss and long-term vs short-term split (as of 2026-10-16, prices of 2026-09-26)

### Takeaway
The broker shows a net unrealised gain of **+₹37,723**. The FIFO lot view, which adjusts for corporate actions, gives **+₹40,146**. That net hides much bigger offsetting amounts:
- **Long-term gains:** ₹1,44,997.
- **Long-term losses:** −₹99,626.
- **Short-term gains:** ₹5,686.
- **Short-term losses:** −₹10,912.

Bonus issues are the reason. HDFBAN, WIPRO and ASHLEY each hold expensive pre-bonus shares (long-term losses) alongside zero-cost bonus shares (long-term gains). Under FIFO, a partial sale sells the expensive original shares first.

### Cited Findings
- **Reconciliation of `trades.csv` with `portfolio.csv`:**
  - **Matches once corporate actions are applied:**
    - ASHLEY: 1:1 bonus, 16 Jul 2025.
    - BHAELE: 2:1 bonus, 16 Sep 2022.
    - HDFBAN: 1:1 bonus, 27 Aug 2025.
    - WIPRO: 1:1 bonus, 3 Dec 2024.
    - JIOFIN: 25 shares from the RELIND demerger on 20 Jul 2023.
    - Source: `data/corporate_actions.csv`; calculator
  - **Still unreconciled:**
    - **RELIND:** trades plus corporate actions give 101 shares; the broker shows 76. 25 shares are missing and no SELL is recorded in `trades.csv` or the annual transaction statement PDFs.
    - **LIC:** `trades.csv` has 45 shares; the broker shows 80. The 35 missing shares imply a cost of ₹901.8 each, close to the LIC IPO retail price, so the calculator treats them as an IPO lot dated about 12 May 2022 **[BK]**.
    - **TATCAP, LGELEC, NTPGRE:** no trades at all. Broker average costs of ₹326, ₹1,140 and ₹108 equal the IPO prices, so these are treated as IPO allotments of about Oct 2025, Oct 2025 and Nov 2024 **[BK]**.
    - Source: `trades.csv` (rows "NO TRADE HISTORY FOUND"); `reports/AnnualGlobalTransactionStatement-*.pdf`
- **Tax rules behind the lot treatment:**
  - FIFO is mandatory for demat holdings.
  - Bonus shares have nil cost and their holding period starts at allotment.
  - Demerged shares inherit the parent's acquisition date and a share of its cost.
  - Sources: [Income Tax Dept – Circular 768](https://www.incometaxindia.gov.in/w/768-circular-no.-768-dated-24-6-1998-1); [equitiesindia – bonus shares](https://equitiesindia.com/glossary/tax-on-bonus-shares); [Allcargo NSE filing on cost apportionment](https://nsearchives.nseindia.com/corporate/ALLCARGO_27112025173123_Cost_of_aquisition_Signed.pdf)
- **Lot breakdown for the bonus and demerger cases:**

  | Holding | Original / bought lots | Bonus / demerger lots | Short-term lots |
  |---|---|---|---|
  | HDFBAN | 55 sh at about ₹1,460, LT **−₹39,101** | 55 bonus sh at ₹0, LT **+₹40,950** | 20 sh (Apr 2026) −₹151 |
  | WIPRO | 50 sh at about ₹550, LT **−₹17,455** | 50 bonus sh, LT **+₹10,212** | 120 sh (Feb–Apr 2026) +₹445 |
  | LIC | 35 IPO sh LT −₹17,166; 30 sh LT −₹14,420 | — | 15 sh (23 Oct–6 Nov 2025) **−₹7,346** |
  | ASHLEY | 53 sh, LT −₹2,161 | 53 bonus sh, LT +₹8,238 | — |
  | BHAELE | 48 traded sh, LT +₹7,202 | 32 bonus sh, LT +₹13,144 | — |
  | JIOFIN | 28 bought sh, LT −₹2,952 | 25 demerger sh, LT +₹3,415 | — |
  | RELIND | 51 "older" sh at implied cost ₹1,081, LT +₹12,240 (fallback) | — | 25 sh (Jun–Jul 2026) +₹111 |

  Source: calculator
- **Per-holding results:** the full table is in the final section. Source: calculator

### Inferences
- **Trimming HDFBAN realises a loss.** A FIFO sale of up to 55 shares sells the 2022 shares, about −₹711 each, for a total LTCL of up to −₹39.1k. The broker screen shows HDFBAN as +1.2%. A partial sale of WIPRO (first 50 shares, −₹17.5k) or ASHLEY behaves the same way.
- **Gain harvesting on the remaining HDFBAN lots is impossible while the 2022 shares remain.** FIFO always sells them first.
- **RELIND fallback.** The 51 shares without a known lot are treated as LT ("first trade >12 months ago") at an implied cost of ₹1,081. Worst case: if the true basis is closer to the bonus-adjusted lots (27 zero-cost bonus shares + 2 at ₹2,751 + 22 at about ₹1,240), the realised LTCG on a 51-share trim rises by about ₹22k. That still fits inside the exemption in every plan below.

### Gaps
- **RELIND:** where the 25 shares went (gift, transfer, or an unrecorded sale) is unknown. An unrecorded sale would also mean realised gains in an earlier year.
- **Approximate dates:**
  - IPO allotment dates for LIC, TATCAP, LGELEC and NTPGRE are background knowledge. Check them against the CAS or allotment notes.
  - Bonus allotment dates are approximated by the record dates.
- **JIOFIN cost split:** the 4.68% demerger apportionment from RELIND is background knowledge **[BK]**.
- **GUJGA:** the GSPL Transmission demerger of 2 Jul 2026 (1 GTL share per 3) should give about 2 GTL shares. They are not in `portfolio.csv`, and the cost split is unknown. Not modelled.
- **Cost basis differences:** broker average costs include charges and sometimes differ from trade prices. Lot-based and broker gains differ by ₹2.4k in total.

---

## Q3. Totals, and which losses can offset which gains

### Takeaway
**Unrealised totals (FIFO lots, 2026-09-26 prices):**

| Category | All holdings | Stocks only |
|---|---|---|
| LTCG | **+₹1,44,997** | +₹1,44,997 |
| LTCL | **−₹99,626** | −₹99,626 |
| STCG | **+₹5,686** | +₹2,357 |
| STCL | **−₹10,912** | −₹7,601 |
| Lots of unknown term | ₹0 | — |

All of the long-term amounts are in stocks: no ETF lot is long-term yet. The rest of the short-term figures come from gold/silver (+₹3,203 / −₹2,554), broad ETFs (+₹87 / −₹684) and sector ETFs (+₹39 / −₹74).

**Which losses can offset which gains:**
- **Long-term losses (LTCL), which can only offset LTCG:**

  | Holding / lots | Loss |
  |---|---|
  | HDFBAN 2022 lots | −₹39.1k |
  | LIC IPO + Sep–Oct 2025 lots | −₹31.6k |
  | WIPRO 2022/2024 lots | −₹17.5k |
  | Small JSWENE, JIOFIN, ASHLEY, GAIL and PETLNG lots, plus TATCAP, NTPGRE, SJVLIM and GUJGA | remainder of the −₹99.6k total |

- **Short-term losses (STCL), which can offset any gain:**
  - LIC's 15 shares bought 23 Oct–6 Nov 2025: −₹7,346.
  - ICIGOL: −₹1,280 (gold ETF loss, usable against equity gains as well).
  - Small ETF systematic investment plan (SIP) lots.

### Cited Findings
- **Set-off and carry-forward:**
  - STCL can be set off against both STCG and LTCG. LTCL can be set off only against LTCG.
  - Unused losses carry forward for 8 years, but only if the return is filed by the s.139(1) due date.
  - Sources: [Angel One](https://angelone.in/knowledge-center/share-market/wash-sale); [Kotak Securities](https://kotaksecurities.com/share-market/what-is-wash-sale-rule); [share.market](https://www.share.market/buzz/learn/tax-loss-harvesting/)
- **Rates and exemption:** for FY 2026-27, STCG is 20% and LTCG 12.5% above ₹1.25 lakh. Sections 196 and 198 of the Income-tax Act 2025 replaced 111A and 112A from 1 Apr 2026 — [ClearTax](https://cleartax.in/s/long-term-capital-gains-on-shares); [Income Tax Dept – s.196](https://www.incometaxindia.gov.in/w/section-196-78); [Income Tax Dept – s.198](https://www.incometaxindia.gov.in/w/section-198-78)
- **Gold and silver ETFs:** taxed at 12.5% if held more than 12 months, with no ₹1.25 lakh exemption, and at slab rates if held 12 months or less — [Zerodha Fund House](https://www.zerodhafundhouse.com/blog/gold-etf-taxation-2025/); [Business Standard](https://www.business-standard.com/finance/personal-finance/gold-and-silver-surge-know-how-etfs-are-taxed-before-you-invest-in-them-125101000906_1.html)
- **s.87A rebate:** from FY 2025-26 it cannot be used against special-rate STCG or LTCG — [TaxGuru](https://taxguru.in/?p=1022823)
- **Debt mutual funds** bought on or after 1 Apr 2023 are taxed at slab rate whatever the holding period. This matters for the new 15% debt sleeve — [Equentis](https://www.equentis.com/blog/tax-on-debt-mutual-funds/); [TaxClue](https://taxclue.in/blog/debt-mutual-fund-tax-post-2023-ita-2025)

### Inferences
- **The LTCG exemption is applied after set-off [BK].** Because of this, losses booked in the same year as gains below ₹1.25 lakh save nothing and are simply used up.
  - **Example:** sell everything in FY 2026-27. Gross LTCG of ₹1.45 lakh is reduced by ₹99.6k LTCL and ₹10.9k STCL to **₹40,146 net**, inside the exemption.
  - Tax would be ₹0 even with no losses, since the gross LTCG of the plan's sales (₹1.19 lakh) is itself below ₹1.25 lakh. So about ₹1.07 lakh of losses would be used up for no benefit.
- **The LIC loss lots change category in the next three weeks.**
  - The 15 shares bought 23 Oct–6 Nov 2025 are still short-term (−₹7,346).
  - They turn long-term on **24 Oct, 30 Oct and 7 Nov 2026**.
  - Selling before 24 Oct 2026 keeps −₹7.3k as the more flexible STCL. This only matters if the loss would otherwise be carried forward or used against STCG.
- **Repo data and tax data agree.** The positions the repo flags SELL (LIC, WIPRO, NTPGRE, SJVLIM, ICIGOL, ICIPSE) are mostly loss or near-zero positions.

### Gaps
- **Set-off order:** I have not confirmed that a taxpayer may choose to set STCL against higher-taxed STCG first. I also have not confirmed that brought-forward losses must be set off against LTCG that falls inside the exemption. Both are treated as **[BK]**.

---

## Q4. Staged plan toward an EXAMPLE target: 60% index core / 15% satellite (≤8 stocks, ≤5% each) / 15% debt / 10% gold

### Takeaway
**At 2026-09-26 prices, every route through the transition costs ₹0 in capital-gains tax.** The real choice is a different one: either spend about ₹1.07 lakh of losses now, or keep about **₹66k of LTCL** for future years. Keeping them means selling the gains in FY 2026-27 and the losses on or after 1 Apr 2027.

The example plan:
- Keeps 5 satellite stocks, worth ₹98.8k (14.6%).
- Sells ₹4.77 lakh of holdings.
- Buys about ₹3.74 lakh of Nifty/broad index (core) and about ₹1.01 lakh of debt.
- Trims silver so that gold + silver = 10%.

### Cited Findings (computed; source: calculator on repo files)
- **Example satellite rule:** take the top 8 stocks by repo conviction, then by value. Exclude stocks marked SELL or VERIFY DATA. Cap each at 5% (₹33,754) and the total at 15%. Skip a partial fill below ₹10k.

  | Stock | Keep | Value | Note |
  |---|---|---|---|
  | RELIND | 25 sh | ₹33,030 | |
  | HDFBAN | 45 sh | ₹33,505 | |
  | LGELEC | 13 sh | ₹19,811 | |
  | DRREDD | 6 sh | ₹7,821 | |
  | NTPC | 12 sh | ₹4,643 | |
  | **Total** | | **≈₹98.8k (14.6%)** | |
  | ASHLEY | — | — | Would only have fitted as a ₹1.5k stub, so skipped |

  - The 25 RELIND shares kept are the Jun–Jul 2026 lots.
  - The 45 HDFBAN shares kept are 25 zero-cost bonus shares plus the 20 bought Apr 2026.
- **Sales:**
  - All of 22 other stocks.
  - FIFO trims: HDFBAN 85 sh and RELIND 51 sh.
  - NIPNIT and KOTAKBKETF in full.
  - ICIPSE 62 sh.
  - Total sales: ₹4,77,436.
- **Buys:**
  - Core: ₹3,73,602, which with the existing ₹31,442 of broad ETFs gives ₹4,05,044 (60%).
  - Debt: ₹1,01,261 (15%).
  - Gold + silver after the trim: ₹67,386 (10.0%).
- **Lots crossing to long-term within 3 months (to 2027-01-16):**
  - **LIC:** 15 sh, loss −₹7,346, turns LT 24 Oct, 30 Oct and 7 Nov 2026. Sell before then if STCL is wanted.
  - **ONGC:** 25 sh bought 27 Nov–26 Dec 2025, gain +₹662, turns LT 28 Nov–27 Dec 2026. **Defer the sale until after 27 Dec 2026.**
- **Lots that have just turned long-term:**
  - TATCAP: about 10 Oct 2026 (IPO date inferred).
  - LGELEC: about 11 Oct 2026 (IPO date inferred).
  - LIC: 2025-10-15 lot, on 16 Oct 2026.
- **Lots turning long-term 17 Jan–31 Mar 2027:**

  | Holding / lots | Gain or loss | Turns LT |
  |---|---|---|
  | ICIGOL 250 sh | net −₹1,280 | 3–20 Mar 2027 |
  | ICIPSE 151 sh | net +₹922 | 2 Feb–28 Mar 2027 |
  | WIPRO 100 sh | +₹448 | 25 Feb 2027 |
  | GAIL 40 sh | +₹1,036 | 28 Mar 2027 |

- **Lots turning long-term only after FY 2026-27:**
  - ICIPSE 42 sh (2 Apr 2027).
  - HDFBAN 20 sh (2 Apr 2027).
  - WIPRO 20 sh (Apr 2027).
  - RELIND 25 sh (Jun–Jul 2027).
  - All SIP ETF lots in ICINIF, MIR150, HDF250, NIPNIT and KOTAKBKETF (Apr–Sep 2027). These are all small losses.

**Plan S1 (recommended illustration): gains first, losses second**

- **FY 2026-27 (now to 31 Mar 2027).** Sell the 16 net-gain exits and trims:
  - BHAELE +₹20,346, RELIND trim +₹12,240, TATGLO +₹11,492, IDECEL +₹9,938, FEDBAN +₹6,739, ASHLEY +₹6,078, JSWENE +₹4,913.
  - GUJPPL, SEQSCI, NHPC, ENGIND, TATPOW, JIOFIN and HINPET, each under ₹1.5k.
  - ONGC after 27 Dec 2026 (+₹902); GAIL after 28 Mar 2027 (+₹599).

  | FY 2026-27 result | Amount |
  |---|---|
  | Sale value | ₹2,75,957 |
  | Gross LTCG | ₹88,414 |
  | LTCL inside those positions | ₹8,087 |
  | **Net LTCG** | **₹80,327** (inside the ₹1.25 lakh exemption) |
  | **Tax** | **₹0** |
  | Unused exemption | ₹44,673 |
  | STT | about ₹276 |

- **FY 2027-28 (from 1 Apr 2027).** Sell the 11 net-loss exits and trims:
  - LIC −₹38,933, HDFBAN trim of 85 sh −₹16,764, WIPRO −₹6,798.
  - TATCAP −₹925, SJVLIM −₹790, NTPGRE −₹618, PETLNG −₹587, GUJGA −₹443.
  - The ICIPSE trim, NIPNIT and KOTAKBKETF (each under ₹100).

  | FY 2027-28 result | Amount |
  |---|---|
  | Sale value | ₹2,01,479 |
  | LTCL | ₹99,006 |
  | LTCG on the bonus shares sold in the same FIFO sales | ₹33,030 |
  | **Net loss carried forward** | **₹65,962 LTCL** |
  | **Tax** | **₹0** |
  | STT | about ₹181 |

  Do not book other gains in FY 2027-28, or they will absorb this loss.

**Plan S2 = "do it all in FY 2026-27" (same as the immediate switch, except ONGC and GAIL)**
- Net LTCG: ₹14,365. Tax: **₹0**.
- Losses used up: ₹1,07,182.
- Nothing is carried forward.

**New money needed to reach the targets without selling** (stock share must fall from 82.3% to 15%):
- **Total portfolio needed:**
  - ₹37,05,945 for stocks to be ≤15%, i.e. **₹30.3 lakh** of new money.
  - ₹20,08,224 for RELIND to be ≤5%.

| Monthly SIP | Assumption | Stocks ≤15% | Largest stock ≤5% |
|---|---|---|---|
| ₹10k | no growth | **304 months (25.3 yrs)** | 134 months (11.2 yrs) |
| ₹25k | no growth | **122 months (10.2 yrs)** | 54 months (4.5 yrs) |
| ₹10k | all assets +10%/yr | **never** (stock share levels off at about 29%) | never |
| ₹25k | all assets +10%/yr | about 429 months (35.8 yrs) | 70 months |

The "≤8 stocks" rule cannot be met at all without selling, because there are 27 stocks today.

### Inferences
- **S1 versus S2:**
  - S1's only tax advantage is the ₹65,962 LTCL carried forward. It is worth at most about **₹8,575** (×13%), and only if a later year has LTCG above ₹1.25 lakh after set-off.
  - S1's cost is about 5.5 months' delay in exiting LIC and WIPRO, which the repo flags SELL now.
  - If the user wants those exits now, S2 costs nothing in tax today.
  - **Middle route:** sell LIC and WIPRO now (FY 2026-27) together with the gainers, and accept losing the carry-forward.
- **Using the spare FY 2026-27 exemption in S1:**
  - The spare ₹44.7k can step up the cost of the satellites at zero tax: sell and rebuy the next trading day.
  - Candidates: LGELEC +₹4,991, NTPC +₹1,346 and DRREDD +₹749.
  - Not RELIND: the 25 shares kept are still short-term.
  - Not HDFBAN: FIFO would sell the 2022 loss shares first.
- **Using the FY 2027-28 exemption:** it is free for gain harvesting only if the loss tranche is moved again, so the two goals compete.
- **Debt sleeve:** new debt is taxed at slab rate (post-Apr-2023 rule). For a high-slab investor, a smaller debt sleeve or an arbitrage fund for short-term parking is more tax-efficient. This is a choice for the user.
- **Gold:** the repo's last run says SELL for ICIGOL and ICIPSE, which conflicts with the example's 10% gold. Whichever way the user goes, silver trims should wait until the lots turn long-term (Feb–Apr 2027). Before then, gains are slab-taxed.
- **Rebuys:** never sell and rebuy the same scrip on the same day; that is treated as intraday — [Zerodha Z-Connect](https://zerodha.com/z-connect/taxation-for-traders/tax-loss-harvesting); [TradingQnA](https://tradingqna.com/t/tax-loss-harvesting-effective-way/144717)

### Gaps
- **Pick order affects the tax split.** The satellite pick is mechanical, from repo conviction. A different pick (for example keeping BHAELE or IDECEL) changes which gains are realised, but not the ₹0 tax result.
- **Prices move the numbers.** At 2026-10-15 prices:
  - The immediate switch has net LTCG ≤ 0, and tax is again ₹0.
  - S1's FY 2026-27 net LTCG is ₹59,910. Tax is about ₹28, on a small STCG.
  - S1's FY 2027-28 carry-forward LTCL is ₹80,621.
  - The split between "gain" and "loss" positions also shifts: JSWENE, JIOFIN, ONGC, HINPET and ICIPSE become losers.

---

## Q5. Estimated tax cost: immediate full switch vs staged plan

### Takeaway
- **Immediate switch** (all ₹4.77 lakh of sales on 2026-10-16): tax **₹0**, STT about **₹457**. Net LTCG after set-off is ₹14,365.
- **Full liquidation** of all 34 holdings: tax ₹0, STT about ₹556. Net LTCG is ₹40,146.
- **Staged plan S1:** tax ₹0 + ₹0, STT about ₹457 in total. It preserves ₹65,962 of LTCL.

The staged plan does not lower today's tax. It keeps a loss carry-forward worth up to about ₹8.6k.

### Cited Findings
- **Rates used:** 20% STCG and 12.5% LTCG above ₹1.25 lakh, plus 4% cess — [ClearTax](https://cleartax.in/s/long-term-capital-gains-on-shares); [ebizfiling on s.196/198](https://ebizfiling.com/blog/section-196-and-198-short-term-and-long-term-capital-gains/)
- **Delivery charges:** STT is 0.1% on delivery sales, plus a DP charge of about ₹15.34 per scrip per day — [Zerodha charges](https://www.zerodha.com/charges); [Finology](https://select.finology.in/articles/broker/dp-charges-in-zerodha)

### Inferences
- **DP charges:** selling 27 scrips adds about ₹414. The all-in cost of either route is therefore about ₹0.9k (about 0.2% of the amount switched).
- **Worst-case data gaps would not change the ₹0 result:**
  - RELIND cost basis about ₹22k lower: FY 2026-27 net LTCG would be about ₹1.03 lakh in S1, still exempt.
  - LGELEC turning out to be short-term (if not an IPO lot): +₹4,991 STCG, about ₹1,038 tax unless offset by STCL.
- **When the result would change:** only if the user already has more than about ₹45k of realised LTCG elsewhere in FY 2026-27 under S1, or more than about ₹1.1 lakh under S2.

### Gaps
- Not checked: surcharge, low-income use of the basic exemption limit, other demat accounts and mutual fund redemptions.

---

## Transition numbers for the guide

### Takeaway
These tables can be pasted directly. Base case: prices of 2026-09-26 (`portfolio.csv`), tax status as of 2026-10-16, FIFO lots adjusted for corporate actions. The target is an EXAMPLE, and none of this is tax advice.

### Cited Findings (all computed by the calculator from repo files)

**Table 1 – Allocation today**

| Bucket | ₹ | % |
|---|---|---|
| Individual stocks (27) | 5,55,892 | 82.3 |
| Broad equity ETFs (ICINIF, HDF250, MIR150) | 31,442 | 4.7 |
| Sector ETFs (NIPNIT, KOTAKBKETF) | 4,212 | 0.6 |
| Gold / silver ETFs (ICIGOL, ICIPSE) | 83,528 | 12.4 |
| Debt | 0 | 0 |
| **Total** | **6,75,074** | 100 |

**Table 2 – Concentration**

| Measure | Value |
|---|---|
| Top 2 (RELIND, HDFBAN) | 29.2% |
| Top 10 | 71.4% |
| Holdings | 34 (27 stocks, 7 ETFs) |
| Largest sectors (direct stocks) | Oil & Gas 19.7%, Banking 16.4%, Power 9.5%, IT 6.7% |

**Table 3 – Per holding (₹; LT/ST = FIFO-lot unrealised gain by term)**

| Sym | Class | Sector | Value | Wt% | Broker P&L | P&L % | LT | ST | Lot status | Repo decision 15-Oct |
|---|---|---|---|---|---|---|---|---|---|---|
| RELIND | Stock | Oil & Gas | 100,411 | 14.9 | 12,351 | +14.0% | 12,240 | 111 | UNREC: fallback (assumed-LT remainder) | TRIM |
| HDFBAN | Stock | Banking | 96,792 | 14.3 | 1,110 | +1.2% | 1,849 | -151 | reconciled (after bonus) | TRIM |
| ICIPSE | Gold/silver ETF | Silver | 50,248 | 7.4 | 1,754 | +3.6% | 0 | 1,929 | reconciled | SELL |
| WIPRO | Stock | IT | 44,935 | 6.7 | -7,075 | -13.6% | -7,242 | 445 | reconciled (after bonus) | SELL |
| TATGLO | Stock | Consumption | 35,352 | 5.2 | 11,333 | +47.2% | 11,492 | 0 | reconciled | REVIEW |
| ICIGOL | Gold/silver ETF | Gold | 33,280 | 4.9 | -1,405 | -4.1% | 0 | -1,280 | reconciled | SELL |
| LIC | Stock | Insurance | 32,908 | 4.9 | -38,933 | -54.2% | -31,587 | -7,346 | UNREC: 35 sh gap = IPO lot (inferred) | SELL |
| BHAELE | Stock | Defense | 32,860 | 4.9 | 20,234 | +160.2% | 20,346 | 0 | reconciled (after bonus) | REVIEW |
| JSWENE | Stock | Power | 32,133 | 4.8 | 4,663 | +17.0% | 4,913 | 0 | reconciled | TRIM |
| ICINIF | Equity ETF (broad) | Broad Market | 22,877 | 3.4 | -436 | -1.9% | 0 | -436 | reconciled | REVIEW |
| IDECEL | Stock | Telecom | 20,985 | 3.1 | 9,900 | +89.3% | 9,938 | 0 | reconciled | HOLD |
| LGELEC | Stock | Consumer Electronics | 19,811 | 2.9 | 4,991 | +33.7% | 4,991 | 0 | NO TRADES – IPO inferred | ACCUMULATE |
| ASHLEY | Stock | Auto | 16,477 | 2.4 | 5,985 | +57.0% | 6,078 | 0 | reconciled (after bonus) | REVIEW |
| NTPGRE | Stock | Power | 14,286 | 2.1 | -618 | -4.1% | -618 | 0 | NO TRADES – IPO inferred | SELL |
| TATCAP | Stock | Financial Services | 14,071 | 2.1 | -925 | -6.2% | -925 | 0 | NO TRADES – IPO inferred | HOLD |
| FEDBAN | Stock | Banking | 13,870 | 2.1 | 6,675 | +92.8% | 6,739 | 0 | reconciled | HOLD |
| JIOFIN | Stock | Financial Services | 12,664 | 1.9 | 359 | +2.9% | 463 | 0 | reconciled (after demerger) | REVIEW |
| ONGC | Stock | Oil & Gas | 10,351 | 1.5 | 853 | +9.0% | 240 | 662 | reconciled | REVIEW |
| GAIL | Stock | Oil & Gas | 10,035 | 1.5 | 547 | +5.8% | -437 | 1,036 | reconciled | HOLD |
| DRREDD | Stock | Pharma | 7,821 | 1.2 | 695 | +9.8% | 749 | 0 | reconciled | HOLD |
| HINPET | Stock | Oil & Gas | 5,514 | 0.8 | 306 | +5.9% | 349 | 0 | reconciled | REVIEW |
| SJVLIM | Stock | Power | 5,036 | 0.7 | -833 | -14.2% | -790 | 0 | reconciled | SELL |
| ENGIND | Stock | Infrastructure | 4,866 | 0.7 | 1,117 | +29.8% | 1,148 | 0 | reconciled | VERIFY DATA |
| NTPC | Stock | Power | 4,643 | 0.7 | 1,316 | +39.6% | 1,346 | 0 | reconciled | REVIEW |
| MIR150 | Equity ETF (broad) | Broad Market | 4,470 | 0.7 | -29 | -0.6% | 0 | -30 | reconciled | HOLD |
| NHPC | Stock | Power | 4,338 | 0.6 | 1,125 | +35.0% | 1,153 | 0 | reconciled | HOLD |
| HDF250 | Equity ETF (broad) | Broad Market | 4,096 | 0.6 | -130 | -3.1% | 0 | -130 | reconciled | HOLD |
| PETLNG | Stock | Oil & Gas | 3,795 | 0.6 | -624 | -14.1% | -587 | 0 | reconciled | HOLD |
| TATPOW | Stock | Power | 3,366 | 0.5 | 1,098 | +48.4% | 1,118 | 0 | reconciled | HOLD |
| GUJPPL | Stock | Infrastructure | 3,147 | 0.5 | 1,439 | +84.3% | 1,454 | 0 | reconciled | HOLD |
| GUJGA | Stock | Oil & Gas | 2,808 | 0.4 | -469 | -14.3% | -443 | 0 | reconciled (GTL demerger not modelled) | VERIFY DATA |
| SEQSCI | Stock | Pharma | 2,619 | 0.4 | 1,385 | +112.2% | 1,396 | 0 | reconciled | HOLD |
| NIPNIT | Equity ETF (sector) | IT | 2,453 | 0.4 | -7 | -0.3% | 0 | -7 | reconciled | HOLD |
| KOTAKBKETF | Equity ETF (sector) | Banking | 1,760 | 0.3 | -28 | -1.5% | 0 | -28 | reconciled | HOLD |

**Table 4 – Unrealised totals by tax bucket (FIFO lots)**

| Bucket | ₹ |
|---|---|
| LT gains | +1,44,997 |
| LT losses (offset LTCG only) | −99,626 |
| ST gains | +5,686 (equity 2,483; gold/silver 3,203) |
| ST losses (offset any gain) | −10,912 (LIC −7,346; gold/silver −2,554; ETFs/other) |
| Net (lot basis) / broker net | +40,146 / +37,723 |

**Table 5 – Lots changing tax status soon**

| When | Lots | Unrealised | Action |
|---|---|---|---|
| 24 Oct / 30 Oct / 7 Nov 2026 | LIC 15 sh (3 lots) | −7,346 (STCL → LTCL) | Sell before 24 Oct to keep the loss short-term (only if the STCL will be used) |
| 28 Nov – 27 Dec 2026 | ONGC 25 sh (5 lots) | +662 | Defer the sale until after 27 Dec 2026 |
| 2 Feb – 28 Mar 2027 | ICIPSE 151 sh | +922 net | Defer silver trims (slab rate → 12.5%) |
| 25 Feb 2027 | WIPRO 100 sh | +448 | Immaterial; LIC STCL can absorb it |
| 3 – 20 Mar 2027 | ICIGOL 250 sh | −1,280 | Loss; no need to wait |
| 28 Mar 2027 | GAIL 40 sh | +1,036 | Sell after 28 Mar 2027, or in FY 2027-28 |
| Apr – Sep 2027 | ETF SIP lots, HDFBAN 20, WIPRO 20, ICIPSE 42, RELIND 25 | ≈ 0 to small losses | No action needed |

**Table 6 – EXAMPLE end state (60 / 15 / 15 / 10)**

| Sleeve | Target ₹ | How it is reached |
|---|---|---|
| Equity index core 60% | 4,05,044 | Keep ICINIF/MIR150/HDF250 (31,442) + buy about 3,73,602 |
| Satellite 15% (≤8, ≤5% each) | 98,810 | RELIND 25 sh, HDFBAN 45 sh, LGELEC 13, DRREDD 6, NTPC 12 |
| Debt 15% | 1,01,261 | Buy (slab-taxed) |
| Gold/silver 10% | 67,386 | Trim ICIPSE by 62 sh after Feb 2027 |
| Total sold | 4,77,436 | 22 stocks in full, HDFBAN −85, RELIND −51, 2 sector ETFs, ICIPSE −62 |

**Table 7 – Staged plan S1 vs immediate switch**

| Route | FY 2026-27 net LTCG | FY 2026-27 tax | FY 2027-28 net | FY 2027-28 tax | Losses carried forward | STT |
|---|---|---|---|---|---|---|
| Immediate switch (all sales 16 Oct 2026) | 14,365 | **0** | — | — | 0 (1,07,182 used up) | about 457 |
| Liquidate all 34 holdings now | 40,146 | **0** | — | — | 0 | about 556 |
| **S1:** gain positions in FY 2026-27, loss positions from 1 Apr 2027 | 80,327 (unused exemption 44,673) | **0** | −65,962 | **0** | **65,962 LTCL** (worth ≤ about 8,575 if used later) | about 276 + 181 |
| Same, at 15-Oct-2026 prices | 59,910 | about 28 | −80,621 | 0 | 80,621 LTCL | about 427 |

**Table 8 – New money to reach the target without selling**

| SIP | Stocks ≤15% (no growth) | Stocks ≤15% (all assets +10%/yr) | Largest stock ≤5% (no growth) |
|---|---|---|---|
| ₹10,000/month | 25.3 yrs | Never (levels off at about 29%) | 11.2 yrs |
| ₹25,000/month | 10.2 yrs | about 35.8 yrs | 4.5 yrs |

New money needed: ₹30.3 lakh, giving a portfolio of ₹37.1 lakh with no growth. The "≤8 stocks" rule cannot be met without selling.

### Inferences
- **Headline for the guide:** "Because ₹1.0 lakh of hidden long-term losses (mainly HDFBAN's 2022 shares, LIC and WIPRO's pre-bonus shares) offset ₹1.45 lakh of long-term gains, the whole transition can be done in this financial year at ₹0 capital-gains tax. The only tax-related reason to stage it across 31 March is to carry forward about ₹66k of losses."
- **Why selling is the only practical route:** reaching the targets only by adding new money takes 10–25+ years.

### Gaps
Verify these before acting:
- **Missing lot records:**
  - RELIND: 25 shares unaccounted for.
  - LIC: the 35-share IPO lot.
  - TATCAP, LGELEC, NTPGRE: IPO allotment dates.
- **Corporate-action details:**
  - JIOFIN: the 4.68% cost split.
  - GUJGA: the GTL demerger shares.
- **Gains realised elsewhere in FY 2026-27.**
- **The set-off order assumption** (see Q3).
- **Gold and silver tax rates** used in the calculator: slab rate assumed to be 30% + cess.
