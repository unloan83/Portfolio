"""
ingest_pdf_statements.py

Parses ICICI Direct / broker Annual Global Transaction Statement (AGTS) PDF files from reports/,
extracts transaction entries (Date, Stock Symbol, Action BUY/SELL, Qty, Price),
converts them into trades.csv format, and reconciles against portfolio.csv.
"""

import os
import re
import sys
from pathlib import Path
import pandas as pd
import pypdf

from ingest_trades import reconcile, PORTFOLIO_FILE, OUTPUT_FILE

REPORTS_DIR = Path("reports")

ISIN_MAP = {
    'INE208A01029': 'ASHLEY', 'INE976I01016': 'TATCAP', 'INE171A01029': 'FEDBAN',
    'INE040A01034': 'HDFBAN', 'INE324D01010': 'LGELEC', 'INF179KC1FB2': 'HDF250',
    'INF109KC1NT3': 'ICIGOL', 'INF109K012R6': 'ICINIF', 'INF109KC1Y56': 'ICIPSE',
    'INF204KB15V2': 'NIPNIT', 'INE263A01024': 'BHAELE', 'INE192A01025': 'TATGLO',
    'INE758E01017': 'JIOFIN', 'INE075A01022': 'WIPRO',  'INE510A01028': 'ENGIND',
    'INE0J1Y01017': 'LIC',    'INF769K01IC9': 'MIR150', 'INE089A01031': 'DRREDD',
    'INE807F01027': 'SEQSCI', 'INE121E01018': 'JSWENE', 'INE848E01016': 'NHPC',
    'INE733E01010': 'NTPC',   'INE0ONG01011': 'NTPGRE', 'INE002L01015': 'SJVLIM',
    'INE245A01021': 'TATPOW', 'INE129A01019': 'GAIL',   'INE844O01030': 'GUJGA',
    'INE094A01015': 'HINPET', 'INE213A01029': 'ONGC',   'INE347G01014': 'PETLNG',
    'INE002A01018': 'RELIND', 'INE517F01014': 'GUJPPL', 'INE669E01016': 'IDECEL'
}


def parse_agts_pdf(pdf_path: str) -> tuple[str, list[dict]]:
    reader = pypdf.PdfReader(pdf_path)
    full_text = '\n'.join([p.extract_text() for p in reader.pages])
    file_name = Path(pdf_path).name

    period_match = re.search(r'Annual Global Transaction Statement from (.*?) to (.*?)\s', full_text)
    end_date = period_match.group(2) if period_match else '2026-03-31'
    period_str = f"{period_match.group(1)} to {end_date}" if period_match else "Unknown"
    
    try:
        date_str = pd.to_datetime(end_date).strftime('%Y-%m-%d')
    except Exception:
        date_str = '2026-03-31'

    isin_pattern = re.compile(r'([A-Z0-9\.\s\&\(\)\-\']+?)\s*-\s*([A-Z0-9]{12})')
    matches = list(isin_pattern.finditer(full_text))

    trades = []
    for idx, match in enumerate(matches):
        c_name = match.group(1).strip()
        isin = match.group(2)
        symbol = ISIN_MAP.get(isin, c_name)

        start_pos = match.end()
        end_pos = matches[idx+1].start() if idx+1 < len(matches) else len(full_text)
        block = full_text[start_pos:end_pos]

        pattern = re.compile(r'(\d+)\s+[\d\.]*(BSE|NSE)\s*[\d\.]*?([\d]+\.\d{2,4})\s')
        for m in pattern.finditer(block):
            qty = int(m.group(1))
            val = float(m.group(3))
            price = round(val / qty, 2) if qty > 0 else 0.0

            action = 'BUY'
            if 'Sale' in block[:m.start()] and 'Purchase' not in block[:m.start()]:
                action = 'SELL'

            if qty > 0 and price > 0:
                trades.append({
                    'Date': date_str,
                    'Stock Symbol': symbol,
                    'Action': action,
                    'Qty': qty,
                    'Price': price,
                    'Notes': f'icici direct agts: {file_name}'
                })

    return period_str, trades


def process_reports_pdf_directory(reports_dir: Path = REPORTS_DIR) -> tuple[dict, pd.DataFrame]:
    pdf_files = sorted(list(reports_dir.glob("*.pdf")) + list(reports_dir.glob("*.PDF")))
    if len(sys.argv) > 1:
        extra_paths = [Path(p) for p in sys.argv[1:] if p.lower().endswith(".pdf")]
        pdf_files.extend(extra_paths)

    file_summary = {}
    all_trades = []
    for pdf in pdf_files:
        period_str, extracted = parse_agts_pdf(str(pdf))
        file_summary[pdf.name] = {
            'period': period_str,
            'rows': len(extracted)
        }
        all_trades.extend(extracted)

    if not all_trades:
        df = pd.DataFrame(columns=["Date", "Stock Symbol", "Action", "Qty", "Price", "Notes"])
    else:
        df = pd.DataFrame(all_trades).drop_duplicates()
        df = df.sort_values(["Stock Symbol", "Date"])

    return file_summary, df


def main():
    print("=== PDF STATEMENT TRADE INGESTION ENGINE ===")
    file_summary, trades_df = process_reports_pdf_directory()

    print("\n--- PER PDF FILE EXTRACTION REPORT ---")
    for fname, info in file_summary.items():
        print(f"File: {fname}")
        print(f"  Period Covered: {info['period']}")
        print(f"  Rows Extracted: {info['rows']}")

    if not trades_df.empty:
        trades_df.to_csv(OUTPUT_FILE, index=False)
        print(f"\n[success] Wrote {len(trades_df)} trade entries to {OUTPUT_FILE}")

        # Run reconciliation against portfolio.csv
        reconciled_trades, report = reconcile(trades_df, PORTFOLIO_FILE)
        print("\n=== RECONCILIATION REPORT (portfolio.csv vs PDF Statements) ===")
        print(report.to_string(index=False))
    else:
        print("\n[warn] 0 transaction rows extracted across all PDF files.")


if __name__ == "__main__":
    main()
