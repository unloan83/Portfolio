"""Deterministic tax-aware transition calculator (research only; reads repo, writes nothing to repo)."""
import sys, json
from datetime import date, timedelta
import pandas as pd

REPO = "/home/user/Portfolio"
ASOF = date(2026, 10, 16)
FY1_END = date(2027, 3, 31)
FY2_END = date(2028, 3, 31)
PRICE_MODE = sys.argv[1] if len(sys.argv) > 1 else "portfolio"   # or "reeng"

def add_year(d):
    try: return d.replace(year=d.year + 1)
    except ValueError: return d.replace(year=d.year + 1, day=28)

def lt_from(d):          # first date a sale is long-term: buy date + 12 months + 1 day (conservative)
    return add_year(d) + timedelta(days=1)

port = pd.read_csv(f"{REPO}/portfolio.csv", index_col=False)
port = port[["Stock Symbol", "Company Name", "Qty", "Average Cost Price", "Current Market Price"]].copy()
port.columns = ["sym", "name", "qty", "avg", "px"]
reeng = pd.read_csv(f"{REPO}/re-engineering.csv")
last = reeng[reeng.Analysis_Date == reeng.Analysis_Date.max()].set_index("Stock_Symbol")
if PRICE_MODE == "reeng":
    port["px"] = [last.current_price.get(s) if pd.notna(last.current_price.get(s)) else p for s, p in zip(port.sym, port.px)]
port["value"] = port.qty * port.px
port["cost"] = port.qty * port.avg
V = port.value.sum()

BROAD_ETF = {"ICINIF", "HDF250", "MIR150"}
SECTOR_ETF = {"NIPNIT", "KOTAKBKETF"}
EQ_ETF = BROAD_ETF | SECTOR_ETF
GOLD = {"ICIGOL", "ICIPSE"}
def cls(s): return "Gold/silver ETF" if s in GOLD else ("Equity ETF (broad)" if s in BROAD_ETF else ("Equity ETF (sector)" if s in SECTOR_ETF else "Stock"))
port["class"] = port.sym.map(cls)
port["sector"] = [("Gold" if s == "ICIGOL" else "Silver") if s in GOLD else last.sector.get(s, "?") for s in port.sym]

# ---------------- FIFO lots with corporate actions ----------------
tr = pd.read_csv(f"{REPO}/trades.csv").dropna(subset=["Date", "Qty", "Price"])
tr["Date"] = pd.to_datetime(tr.Date).dt.date
tr = tr.sort_values("Date", kind="stable")
# corporate actions from data/corporate_actions.csv mapped to repo symbols (date = record/ex date used as allotment proxy)
CA = [("BHAELE", date(2022, 9, 16), "bonus", 2.0),
      ("RELIND", date(2023, 7, 20), "demerger_JIOFIN", 1.0),
      ("RELIND", date(2024, 10, 28), "bonus", 1.0),
      ("WIPRO", date(2024, 12, 3), "bonus", 1.0),
      ("ASHLEY", date(2025, 7, 16), "bonus", 1.0),
      ("HDFBAN", date(2025, 8, 27), "bonus", 1.0)]
JFSL_COST_SHARE = 0.0468  # [BK] RIL-announced cost apportionment to JFSL (4.68%); verify
events = [(r.Date, 0, r["Stock Symbol"], r.Action, float(r.Qty), float(r.Price)) for _, r in tr.iterrows()]
events += [(d, 1, s, t, k, 0.0) for s, d, t, k in CA]
events.sort(key=lambda e: (e[0], e[1]))
lots = {}
for d, _, s, act, q, p in events:
    L = lots.setdefault(s, [])
    if act == "BUY":
        L.append(dict(date=d, qty=q, px=p, src="trade"))
    elif act == "SELL":
        while q > 1e-9 and L:
            m = min(q, L[0]["qty"]); L[0]["qty"] -= m; q -= m
            if L[0]["qty"] <= 1e-9: L.pop(0)
    elif act == "bonus":
        held = sum(l["qty"] for l in L)
        if held > 0: L.append(dict(date=d, qty=held * q, px=0.0, src="bonus"))
    elif act == "demerger_JIOFIN":
        J = lots.setdefault("JIOFIN", [])
        for l in L:
            J.append(dict(date=l["date"], qty=l["qty"], px=l["px"] * JFSL_COST_SHARE, src="demerger"))
            l["px"] *= (1 - JFSL_COST_SHARE)
        lots["JIOFIN"] = sorted(J, key=lambda x: x["date"])

IPO = {  # [BK] inferred from broker avg == IPO price; allotment dates approximate, verify against CAS/contract notes
    "NTPGRE": (date(2024, 11, 25), "IPO Nov-2024 @108 (inferred)"),
    "TATCAP": (date(2025, 10, 9), "IPO Oct-2025 @326 (inferred)"),
    "LGELEC": (date(2025, 10, 10), "IPO Oct-2025 @1140 (inferred)"),
}
LIC_IPO = date(2022, 5, 12)  # [BK] LIC IPO allotment ~12 May 2022

rows, lotrows = [], []
for _, h in port.iterrows():
    s = h.sym; L = [dict(l) for l in lots.get(s, []) if l["qty"] > 1e-9]
    lq = sum(l["qty"] for l in L)
    status, note = "", ""
    if s in IPO:
        d, note = IPO[s]
        L = [dict(date=d, qty=h.qty, px=h.avg, src="ipo-inferred")]; status = "NO TRADES - IPO inferred"
    elif abs(lq - h.qty) < 1e-6:
        status = "reconciled" + (" (after CA)" if any(l["src"] != "trade" for l in L) else "")
    elif s == "LIC" and h.qty > lq:
        gap = h.qty - lq; gap_cost = h.cost - sum(l["qty"] * l["px"] for l in L)
        L = [dict(date=LIC_IPO, qty=gap, px=gap_cost / gap, src="ipo-inferred")] + L
        status = "UNRECONCILED - gap filled as IPO lot"; note = f"{gap:.0f} sh missing; implied cost {gap_cost/gap:.1f} ~ LIC IPO retail price"
    else:
        # fallback: keep trades.csv lots bought within last 12 months as ST (latest first), remainder at implied broker cost
        recent = [l for l in L if lt_from(l["date"]) > ASOF]
        keep, need = [], h.qty
        for l in sorted(recent, key=lambda x: x["date"], reverse=True):
            m = min(need, l["qty"]);
            if m > 0: keep.append(dict(l, qty=m)); need -= m
        keep = sorted(keep, key=lambda x: x["date"])
        rem_cost = h.cost - sum(l["qty"] * l["px"] for l in keep)
        first = min(l["date"] for l in lots.get(s, [])) if lots.get(s) else None
        old_src = "assumed-LT" if (first and lt_from(first) <= ASOF) else "unknown"
        L = ([dict(date=first, qty=need, px=rem_cost / need, src=old_src)] if need > 1e-9 else []) + keep
        status = f"UNRECONCILED - fallback ({old_src} remainder)"; note = f"trades+CA give {lq:.0f} sh vs broker {h.qty:.0f}"
    for l in L:
        l["lt"] = lt_from(l["date"]) <= ASOF if l["src"] != "unknown" else None
        l["gain"] = (h.px - l["px"]) * l["qty"]
        l["matures"] = lt_from(l["date"])
        lotrows.append(dict(sym=s, cls=h["class"], **l))
    ltg = sum(l["gain"] for l in L if l["lt"] is True); stg = sum(l["gain"] for l in L if l["lt"] is False)
    ung = sum(l["gain"] for l in L if l["lt"] is None)
    rows.append(dict(sym=s, cls=h["class"], sector=h.sector, qty=h.qty, value=h.value, broker_gain=h.value - h.cost,
                     broker_pct=(h.value / h.cost - 1) * 100, lot_gain=ltg + stg + ung, LT=ltg, ST=stg, UNK=ung,
                     status=status, note=note, decision=last.Decision.get(s), conv=last.Conviction.get(s)))
H = pd.DataFrame(rows).set_index("sym"); LOTS = pd.DataFrame(lotrows)

# ---------------- tax engine ----------------
SLAB = 0.312  # 30% + 4% cess assumption for gold/silver STCG
def tax_of(real, b_f_ltcl=0.0):
    """real: list of dicts with gain, lt(bool), cls. Returns tax (incl 4% cess) with favourable set-off order."""
    e_st = sum(r["gain"] for r in real if not r["lt"] and r["cls"] != "Gold/silver ETF" and r["gain"] > 0)
    g_st = sum(r["gain"] for r in real if not r["lt"] and r["cls"] == "Gold/silver ETF" and r["gain"] > 0)
    e_lt = sum(r["gain"] for r in real if r["lt"] and r["cls"] != "Gold/silver ETF" and r["gain"] > 0)
    g_lt = sum(r["gain"] for r in real if r["lt"] and r["cls"] == "Gold/silver ETF" and r["gain"] > 0)
    stcl = -sum(r["gain"] for r in real if not r["lt"] and r["gain"] < 0)
    ltcl = -sum(r["gain"] for r in real if r["lt"] and r["gain"] < 0) + b_f_ltcl
    gross = dict(e_st=e_st, g_st=g_st, e_lt=e_lt, g_lt=g_lt, stcl=stcl, ltcl=ltcl)
    # STCL: slab ST first, then equity ST, then gold LT, then equity LT
    for k in ["g_st", "e_st", "g_lt", "e_lt"]:
        m = min(stcl, gross[k] if k not in locals() else 0);
    rem = dict(g_st=g_st, e_st=e_st, g_lt=g_lt, e_lt=e_lt)
    for k in ["g_st", "e_st", "g_lt", "e_lt"]:
        m = min(stcl, rem[k]); rem[k] -= m; stcl -= m
    for k in ["g_lt", "e_lt"]:
        m = min(ltcl, rem[k]); rem[k] -= m; ltcl -= m
    taxable_elt = max(0.0, rem["e_lt"] - 125000)
    tax = (rem["g_st"] * 0.30 + rem["e_st"] * 0.20 + rem["g_lt"] * 0.125 + taxable_elt * 0.125) * 1.04
    return dict(gross=gross, net_after_setoff=rem, exempt_used=min(rem["e_lt"], 125000), unused_exemption=max(0, 125000 - rem["e_lt"]),
                taxable_ltcg=taxable_elt, tax=tax, cf_stcl=stcl, cf_ltcl=ltcl)

def sell_fifo(sym, qty, sale_date):
    out = []; lt_cut = sale_date
    L = LOTS[LOTS.sym == sym].sort_values("date")
    for _, l in L.iterrows():
        if qty <= 1e-9: break
        m = min(qty, l.qty); qty -= m
        px = port.set_index("sym").px[sym]
        out.append(dict(sym=sym, qty=m, gain=(px - l.px) * m, lt=(l.matures <= sale_date), cls=l.cls, buy=l.date, matures=l.matures))
    return out

# ---------------- current allocation ----------------
alloc = H.groupby("cls").value.sum() / V * 100
top10 = H.value.sort_values(ascending=False).head(10)
sect = (H[H.cls == "Stock"].groupby("sector").value.sum() / V * 100).sort_values(ascending=False)

# ---------------- example target ----------------
T = dict(core=0.60, sat=0.15, debt=0.15, gold=0.10)
cand = H[(H.cls == "Stock") & (~H.decision.isin(["SELL", "VERIFY DATA"]))].copy()
cand = cand.sort_values(["conv", "value"], ascending=[False, False]).head(8)
cap, budget, sat = 0.05 * V, T["sat"] * V, {}
for s, r in cand.iterrows():
    keep = min(r.value, cap, budget - sum(sat.values()))
    if keep >= min(r.value, 10000): sat[s] = keep   # skip partial fills below Rs10k (min trade size)
px = port.set_index("sym").px
plan_sell = {}  # sym -> qty
for s, r in H.iterrows():
    if r.cls == "Stock":
        keepq = r.qty if sat.get(s, 0) >= r.value - 1e-6 else int(sat.get(s, 0) // px[s]); plan_sell[s] = r.qty - keepq
    elif r.cls == "Equity ETF (sector)":
        plan_sell[s] = r.qty
gold_val = H.loc[list(GOLD)].value.sum(); excess = gold_val - T["gold"] * V
plan_sell["ICIPSE"] = int(max(0, excess) // px["ICIPSE"]) + 1 if excess > 0 else 0
plan_sell = {k: v for k, v in plan_sell.items() if v > 0}

def realise(plan, sale_date):
    out = []
    for s, q in plan.items(): out += sell_fifo(s, q, sale_date)
    return out

STT = lambda s, val: val * (0.001 if cls(s) == "Stock" else (0.00001 if cls(s).startswith("Equity ETF") else 0.0))
def stt_of(plan): return sum(STT(s, q * px[s]) for s, q in plan.items())

# Scenario A: immediate full switch (all plan sales on ASOF)
A = realise(plan_sell, ASOF); taxA = tax_of(A)
# Scenario A2: liquidate everything immediately (cash out 100%)
ALL = {s: r.qty for s, r in H.iterrows()}; A2 = realise(ALL, ASOF); taxA2 = tax_of(A2)

# Staged: for each symbol, defer sale to the latest maturity date among its to-be-sold ST *gain* lots, if that is <= FY1_END -> FY1 at that date;
# if maturity is after FY1_END and those ST gains are not covered, push to FY2. Loss lots/LT lots sold now.
staged = []
for s, q in plan_sell.items():
    parts = sell_fifo(s, q, ASOF)
    stgain = [p for p in parts if not p["lt"] and p["gain"] > 0]
    if not stgain:
        staged.append((s, q, ASOF, "now")); continue
    mat = max(p["matures"] for p in stgain)
    staged.append((s, q, mat, "FY26-27 after maturity" if mat <= FY1_END else "FY27-28 after maturity"))
fy1 = [(s, q, d, why) for s, q, d, why in staged if d <= FY1_END]
fy2 = [(s, q, d, why) for s, q, d, why in staged if d > FY1_END]
R1 = sum((sell_fifo(s, q, d) for s, q, d, _ in fy1), []); tax1 = tax_of(R1)
R2 = sum((sell_fifo(s, q, d) for s, q, d, _ in fy2), []); tax2 = tax_of(R2, b_f_ltcl=tax1["cf_ltcl"])

# maturing lots within next 3 months (and to FY end)
LOTS["days_to_LT"] = [(m - ASOF).days for m in LOTS.matures]
mat3 = LOTS[(LOTS.days_to_LT > 0) & (LOTS.matures <= date(2027, 1, 16))]
matfy = LOTS[(LOTS.matures > date(2027, 1, 16)) & (LOTS.matures <= FY1_END)]

# monthly contributions to reach targets without selling
S_now = H[H.cls == "Stock"].value.sum(); biggest = H[H.cls == "Stock"].value.max()
nstocks = (H.cls == "Stock").sum()
def months_needed(monthly, g_annual=0.0):
    gm = (1 + g_annual) ** (1 / 12) - 1
    S, tot = S_now, V
    for n in range(1, 1200):
        S *= 1 + gm; tot = tot * (1 + gm) + monthly
        if S / tot <= T["sat"]: return n, tot
    return None, None
def months_cap(monthly, g_annual=0.0):
    gm = (1 + g_annual) ** (1 / 12) - 1; B, tot = biggest, V
    for n in range(1, 2400):
        B *= 1 + gm; tot = tot * (1 + gm) + monthly
        if B / tot <= 0.05: return n
    return None

def fmt(x): return f"{x:,.0f}"
out = dict(V=V, alloc=alloc.to_dict(), top10=(top10 / V * 100).to_dict(), top10_sum=top10.sum() / V * 100,
           sect=sect.to_dict(), sat=sat, plan_sell=plan_sell, nstocks=int(nstocks), S_now=S_now, biggest=biggest)
print(json.dumps(out, indent=1, default=str))
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30); pd.set_option("display.max_rows", 300)
print(H[["cls", "sector", "qty", "value", "broker_gain", "broker_pct", "lot_gain", "LT", "ST", "UNK", "status", "note", "decision", "conv"]].round(1).to_string())
print("\nTOTALS lot-based: LT gains", fmt(H.LT.clip(lower=0).sum()))
lt_pos = LOTS[(LOTS["lt"] == True) & (LOTS.gain > 0)].gain.sum(); lt_neg = LOTS[(LOTS["lt"] == True) & (LOTS.gain < 0)].gain.sum()
st_pos = LOTS[(LOTS["lt"] == False) & (LOTS.gain > 0)].gain.sum(); st_neg = LOTS[(LOTS["lt"] == False) & (LOTS.gain < 0)].gain.sum()
unk = LOTS[LOTS["lt"].isna()].gain.sum()
print(f"lot-level: LTCG+ {fmt(lt_pos)} LTCL {fmt(lt_neg)} STCG+ {fmt(st_pos)} STCL {fmt(st_neg)} unknown {fmt(unk)}; broker total {fmt(H.broker_gain.sum())}; lot total {fmt(H.lot_gain.sum())}")
for c in ["Stock", "Equity ETF (broad)", "Equity ETF (sector)", "Gold/silver ETF"]:
    sub = LOTS[LOTS.cls == c]
    print(c, "LT+", fmt(sub[(sub["lt"] == True) & (sub.gain > 0)].gain.sum()), "LT-", fmt(sub[(sub["lt"] == True) & (sub.gain < 0)].gain.sum()),
          "ST+", fmt(sub[(sub["lt"] == False) & (sub.gain > 0)].gain.sum()), "ST-", fmt(sub[(sub["lt"] == False) & (sub.gain < 0)].gain.sum()))
print("\nPer-symbol net by term (sym-level net LT / ST):")
g = LOTS.groupby(["sym", "lt"], dropna=False).gain.sum().unstack(); print(g.round(0).to_string())
print("\nLOSS LOTS:"); print(LOTS[LOTS.gain < 0][["sym", "date", "qty", "px", "src", "lt", "matures", "gain"]].round(1).to_string())
print("\nMATURING <=2027-01-16:"); print(mat3[["sym", "date", "qty", "px", "src", "matures", "gain"]].round(1).to_string())
print("\nMATURING 2027-01-17..2027-03-31:"); print(matfy[["sym", "date", "qty", "px", "src", "matures", "gain"]].round(1).to_string())
print("\nOTHER ST lots maturing after FY1:"); print(LOTS[(LOTS["lt"] == False) & (LOTS.matures > FY1_END)].groupby("sym").agg(qty=("qty", "sum"), gain=("gain", "sum"), first=("matures", "min"), last=("matures", "max")).round(0).to_string())
print("\nSCENARIO A immediate plan switch:", json.dumps(taxA, default=float, indent=0), "STT", fmt(stt_of(plan_sell)), "sale value", fmt(sum(q * px[s] for s, q in plan_sell.items())))
print("\nSCENARIO A2 liquidate all:", json.dumps(taxA2, default=float, indent=0), "STT", fmt(stt_of(ALL)))
print("\nSTAGED FY1:"); [print(" ", s, q, d, why, fmt(q * px[s])) for s, q, d, why in sorted(fy1, key=lambda x: x[2])]
print(json.dumps(tax1, default=float, indent=0), "STT", fmt(stt_of({s: q for s, q, _, _ in fy1})))
print("\nSTAGED FY2:"); [print(" ", s, q, d, why, fmt(q * px[s])) for s, q, d, why in fy2]
print(json.dumps(tax2, default=float, indent=0), "STT", fmt(stt_of({s: q for s, q, _, _ in fy2})))
print("\nPer-sale realised detail (scenario A):")
dA = pd.DataFrame(A); print(dA.groupby(["sym", "lt"]).gain.sum().unstack().round(0).to_string())
print("\nMONTHLY: stocks", fmt(S_now), "share", S_now / V)
for m in [10000, 25000]:
    for gr in [0.0, 0.10]:
        n, tot = months_needed(m, gr); print(f" {m}/mo growth {gr}: sat<=15% in {n} months ({(n or 0)/12:.1f}y) total {fmt(tot or 0)}; biggest<=5% in {months_cap(m, gr)} months")
print(" required total for stocks<=15% (no growth):", fmt(S_now / 0.15), "new money", fmt(S_now / 0.15 - V))
print(" required total for biggest<=5%:", fmt(biggest / 0.05))
# post-plan buckets
proceeds = sum(q * px[s] for s, q in plan_sell.items())
core_now = H[H.cls == "Equity ETF (broad)"].value.sum()
print("\nPOST-PLAN: proceeds", fmt(proceeds), "core_now", fmt(core_now), "core target", fmt(T["core"] * V), "buy core", fmt(T["core"] * V - core_now),
      "buy debt", fmt(T["debt"] * V), "sat kept", fmt(sum(sat.values())), "gold after", fmt(gold_val - plan_sell.get("ICIPSE", 0) * px["ICIPSE"]))

# ---------- Option S1: gains-first FY26-27, losses FY27-28 ----------
print("\n=== OPTION S1 ===")
net = {}
for sym, q in plan_sell.items():
    net[sym] = sum(p["gain"] for p in sell_fifo(sym, q, FY1_END))
gainers = {k: plan_sell[k] for k, v in net.items() if v > 0}; losers = {k: plan_sell[k] for k, v in net.items() if v <= 0}
for k in sorted(net, key=lambda k: -net[k]): print(f"  {k:11s} sell {plan_sell[k]:>5} value {fmt(plan_sell[k]*px[k]):>8} net {fmt(net[k]):>8} {'GAIN' if net[k]>0 else 'LOSS'}")
# FY1 gainers: sale date = max(now, latest maturity of any ST-gain lot among sold lots) if <= FY1_END
def best_date(sym, q, start, end):
    parts = sell_fifo(sym, q, start); stg = [p for p in parts if not p["lt"] and p["gain"] > 0]
    d = max([start] + [p["matures"] for p in stg]); return d if d <= end else end
G = []; 
for k, q in gainers.items():
    d = best_date(k, q, ASOF, FY1_END); G += sell_fifo(k, q, d); print(f"  FY1 {k} on/after {d}")
tG = tax_of(G); print("FY1 gainers tax:", json.dumps(tG, default=float))
L = []
for k, q in losers.items(): L += sell_fifo(k, q, date(2027, 4, 1))
tL = tax_of(L); print("FY2 losers:", json.dumps(tL, default=float))
print("gainer sale value", fmt(sum(q*px[k] for k,q in gainers.items())), "loser sale value", fmt(sum(q*px[k] for k,q in losers.items())))
print("STT gainers", fmt(stt_of(gainers)), "losers", fmt(stt_of(losers)))
# losers sold now (Option S2 = everything in FY26-27) -> loss consumption
print("Losses consumed if all in one FY:", fmt(tax_of(A)["gross"]["ltcl"] + tax_of(A)["gross"]["stcl"]))
print("Value of preserved losses if later used against fully taxable LTCG: LTCL x 13% =", fmt(tL["cf_ltcl"]*0.13), " STCL x 20.8% =", fmt(tL["cf_stcl"]*0.208))

H["weight"] = H.value / V * 100
H.to_csv(f"holdings_{PRICE_MODE}.csv"); LOTS.to_csv(f"lots_{PRICE_MODE}.csv")
print("\nMD TABLE")
for s, r in H.sort_values("value", ascending=False).iterrows():
    st = r.status.replace("UNRECONCILED - ", "UNREC: ")
    print(f"| {s} | {r.cls} | {r.sector} | {fmt(r.value)} | {r.weight:.1f} | {fmt(r.broker_gain)} | {r.broker_pct:+.1f}% | {fmt(r.LT)} | {fmt(r.ST)} | {st} | {r.decision} |")
