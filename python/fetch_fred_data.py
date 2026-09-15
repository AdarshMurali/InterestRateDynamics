"""
Fetch the FRED-sourced metrics for the Interest Rate Dynamics dashboard
and write a merged CSV to data/raw/fred_raw.csv.

Usage:
    python fetch_fred_data.py

Requires FRED_API_KEY, either as an environment variable or in
python/config.py (see config.py.example).

Note on series IDs vs. DATA_SOURCES.md:
Several IDs in that doc don't resolve on FRED (SOFRCMPD, GOLDAMND are
invalid; MMNRNJ is a discontinued, unrelated series; DEXUSEU is USD/EUR,
not a broad dollar index; M2 is discontinued). It also lists Initial
Jobless Claims (ICSA) as a BLS series, but ICSA is a FRED/DOL series with
no BLS equivalent. This script uses the verified replacements below:
  - Repo rate       -> TGCRRATE (NY Fed Tri-Party General Collateral Rate)
  - Prime rate      -> DPRIME   (Bank Prime Loan Rate)
  - Dollar index    -> DTWEXBGS (Nominal Broad U.S. Dollar Index)
  - M2 money supply -> M2SL (M2 replacement series)
  - Jobless claims  -> ICSA, fetched here instead of via BLS
  - Gold spot price -> fetched from Yahoo Finance (GC=F), since FRED
    discontinued its daily LBMA gold series in 2022.
"""

import os
import sys
import time
from pathlib import Path

import pandas as pd
import requests
import yfinance as yf

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from config import FRED_API_KEY
except ImportError:
    FRED_API_KEY = os.environ.get("FRED_API_KEY")

if not FRED_API_KEY:
    sys.exit(
        "FRED_API_KEY not found. Set it as an environment variable, or copy "
        "python/config.py.example to python/config.py and fill it in."
    )

START_DATE = "2024-09-01"
END_DATE = "2026-09-15"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "fred_raw.csv"
BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

# output_column -> FRED series ID
FRED_SERIES = {
    "Fed_Funds_Rate": "FEDFUNDS",
    "SOFR_Rate": "SOFR",
    "Repo_Rate_Overnight": "TGCRRATE",
    "Prime_Loan_Rate": "DPRIME",
    "Treasury_2Y_Yield": "DGS2",
    "Treasury_5Y_Yield": "DGS5",
    "Treasury_10Y_Yield": "DGS10",
    "Mortgage_30Y_Rate": "MORTGAGE30US",
    "Dollar_Index": "DTWEXBGS",
    "VIX": "VIXCLS",
    "Credit_Spreads_HY_OAS": "BAMLH0A0HYM2",
    "M2_Money_Supply": "M2SL",
    "Initial_Jobless_Claims": "ICSA",
}


def fetch_fred_series(series_id, start_date=START_DATE, end_date=END_DATE):
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": start_date,
        "observation_end": end_date,
    }
    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    payload = response.json()
    if "observations" not in payload:
        raise ValueError(f"Unexpected FRED response for {series_id}: {payload}")

    df = pd.DataFrame(payload["observations"])
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df.set_index("date")["value"]


def fetch_gold_price(start_date=START_DATE, end_date=END_DATE):
    end_inclusive = (pd.Timestamp(end_date) + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    gold = yf.download(
        "GC=F", start=start_date, end=end_inclusive, progress=False, auto_adjust=False
    )
    if gold.empty:
        raise ValueError("No gold price data returned from Yahoo Finance")
    close = gold["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
    close.index = close.index.tz_localize(None)
    return close


def main():
    business_days = pd.bdate_range(START_DATE, END_DATE)
    series_frames = {}

    for column, series_id in FRED_SERIES.items():
        print(f"Fetching {column} ({series_id})...")
        try:
            raw = fetch_fred_series(series_id)
            aligned = raw.reindex(business_days, method="ffill").bfill()
            series_frames[column] = aligned
            print(f"  OK - {raw.notna().sum()} observations, "
                  f"{aligned.isna().sum()} still missing after fill")
        except Exception as exc:
            print(f"  FAILED: {exc}")
            series_frames[column] = pd.Series(index=business_days, dtype=float)
        time.sleep(0.5)  # stay well under the 120 req/min FRED rate limit

    print("Fetching Gold_Spot_Price (Yahoo Finance: GC=F)...")
    try:
        gold_raw = fetch_gold_price()
        series_frames["Gold_Spot_Price"] = gold_raw.reindex(business_days, method="ffill").bfill()
        print(f"  OK - {gold_raw.notna().sum()} observations")
    except Exception as exc:
        print(f"  FAILED: {exc}")
        series_frames["Gold_Spot_Price"] = pd.Series(index=business_days, dtype=float)

    df = pd.DataFrame(series_frames)
    df.index.name = "Date"

    ordered_columns = [
        "Fed_Funds_Rate", "SOFR_Rate", "Repo_Rate_Overnight", "Prime_Loan_Rate",
        "Treasury_2Y_Yield", "Treasury_5Y_Yield", "Treasury_10Y_Yield",
        "Mortgage_30Y_Rate", "Gold_Spot_Price", "Dollar_Index", "VIX",
        "Credit_Spreads_HY_OAS", "M2_Money_Supply", "Initial_Jobless_Claims",
    ]
    df = df[ordered_columns]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH)

    missing_total = df.isna().sum().sum()
    print(f"\nSaved {len(df)} rows x {len(df.columns)} columns to {OUTPUT_PATH}")
    if missing_total:
        print(f"WARNING: {missing_total} missing values remain (columns with no "
              f"data at all can't be filled):")
        print(df.isna().sum()[df.isna().sum() > 0])
    else:
        print("No missing values remain.")


if __name__ == "__main__":
    main()
