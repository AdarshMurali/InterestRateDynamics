"""
Fetch the BLS-sourced metrics for the Interest Rate Dynamics dashboard
and write a merged CSV to data/raw/bls_raw.csv.

Usage:
    python fetch_bls_data.py

BLS_API_KEY is optional (env var or python/config.py) -- the public BLS
API works unregistered at lower limits, which is enough for 3 series.

Note on series IDs vs. DATA_SOURCES.md:
The doc lists Initial Jobless Claims (ICSA) as a 4th BLS metric, but ICSA
is a FRED/Dept. of Labor series with no BLS timeseries equivalent -- it's
fetched by fetch_fred_data.py instead. Only the 3 genuine BLS series are
pulled here.

We pull one extra year of history (from Sept 2023) beyond the dashboard's
Sept 2024 start so that data_processor.py can compute trailing 12-month
CPI YoY inflation for every month in the actual date range.
"""

import os
import sys
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from config import BLS_API_KEY
except ImportError:
    BLS_API_KEY = os.environ.get("BLS_API_KEY")

HISTORY_START_YEAR = 2023  # covers the 12-month lookback needed for YoY calcs
HISTORY_END_YEAR = 2026
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "bls_raw.csv"
BASE_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

# output_column -> BLS series ID
BLS_SERIES = {
    "CPI_Headline_Index": "CUUR0000SA0",
    "CPI_Core_Index": "CUUR0000SA0L1E",
    "Unemployment_Rate": "LNS14000000",
}


def fetch_bls_series(series_ids, start_year=HISTORY_START_YEAR, end_year=HISTORY_END_YEAR):
    payload = {
        "seriesid": series_ids,
        "startyear": str(start_year),
        "endyear": str(end_year),
    }
    if BLS_API_KEY:
        payload["registrationkey"] = BLS_API_KEY

    response = requests.post(BASE_URL, json=payload, timeout=30)
    response.raise_for_status()
    result = response.json()

    if result.get("status") != "REQUEST_SUCCEEDED":
        raise ValueError(f"BLS request failed: {result.get('message')}")

    series_data = {}
    for series in result["Results"]["series"]:
        series_id = series["seriesID"]
        rows = series["data"]
        if not rows:
            series_data[series_id] = pd.Series(dtype=float)
            continue
        df = pd.DataFrame(rows)
        df = df[df["period"].str.startswith("M") & (df["period"] != "M13")]
        df["date"] = pd.to_datetime(
            df["year"] + "-" + df["period"].str.replace("M", "") + "-01"
        )
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
        series_data[series_id] = df.set_index("date")["value"].sort_index()

    return series_data


def main():
    print(f"Fetching {len(BLS_SERIES)} BLS series ({HISTORY_START_YEAR}-{HISTORY_END_YEAR})...")
    try:
        raw = fetch_bls_series(list(BLS_SERIES.values()))
    except Exception as exc:
        sys.exit(f"FAILED: {exc}")

    columns = {}
    for column, series_id in BLS_SERIES.items():
        series = raw.get(series_id, pd.Series(dtype=float))
        columns[column] = series
        print(f"  {column} ({series_id}): {series.notna().sum()} monthly observations")

    df = pd.DataFrame(columns)
    df.index.name = "Date"

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH)
    print(f"\nSaved {len(df)} rows x {len(df.columns)} columns to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
