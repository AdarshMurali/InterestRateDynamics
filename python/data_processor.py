"""
Merge data/raw/fred_raw.csv and data/raw/bls_raw.csv into the final master
dataset, computing the derived metrics from DATA_SOURCES.md.

Usage:
    python data_processor.py

Must be run after fetch_fred_data.py and fetch_bls_data.py.
"""

import sys
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
FRED_RAW_PATH = DATA_DIR / "raw" / "fred_raw.csv"
BLS_RAW_PATH = DATA_DIR / "raw" / "bls_raw.csv"
OUTPUT_PATH = DATA_DIR / "interest_rates_data.csv"

START_DATE = "2024-09-01"
END_DATE = "2026-09-15"

FINAL_COLUMNS = [
    "Fed_Funds_Rate", "SOFR_Rate", "Repo_Rate_Overnight", "Prime_Loan_Rate",
    "Treasury_2Y_Yield", "Treasury_5Y_Yield", "Treasury_10Y_Yield",
    "Mortgage_30Y_Rate", "CPI_Headline_YoY", "CPI_Core_YoY", "Gold_Spot_Price",
    "Dollar_Index", "VIX", "Credit_Spreads_HY_OAS", "Unemployment_Rate",
    "M2_Money_Supply", "Initial_Jobless_Claims", "Yield_Curve_Spread",
    "Real_Yield_10Y",
]


def load_fred():
    df = pd.read_csv(FRED_RAW_PATH, parse_dates=["Date"]).set_index("Date")
    if df.empty:
        sys.exit(f"{FRED_RAW_PATH} is empty. Run fetch_fred_data.py first.")
    return df


def load_bls_monthly():
    df = pd.read_csv(BLS_RAW_PATH, parse_dates=["Date"]).set_index("Date").sort_index()
    if df.empty:
        sys.exit(f"{BLS_RAW_PATH} is empty. Run fetch_bls_data.py first.")
    return df


def compute_cpi_yoy(bls_monthly):
    yoy = pd.DataFrame(index=bls_monthly.index)
    yoy["CPI_Headline_YoY"] = (
        bls_monthly["CPI_Headline_Index"] / bls_monthly["CPI_Headline_Index"].shift(12) - 1
    ) * 100
    yoy["CPI_Core_YoY"] = (
        bls_monthly["CPI_Core_Index"] / bls_monthly["CPI_Core_Index"].shift(12) - 1
    ) * 100
    yoy["Unemployment_Rate"] = bls_monthly["Unemployment_Rate"]
    return yoy


def align_to_business_days(monthly_df, business_days):
    return monthly_df.reindex(business_days, method="ffill").bfill()


def validate(df):
    issues = []
    if df.isna().sum().sum() > 0:
        issues.append(f"{int(df.isna().sum().sum())} missing values remain")
    if (df.index.max() - df.index.min()).days < 360:
        issues.append("date range spans less than 360 days")
    if len(df) < 250:
        issues.append(f"only {len(df)} rows (expected ~250 business days)")
    range_checks = {
        "Fed_Funds_Rate": (0, 10),
        "Gold_Spot_Price": (1000, 8000),
        "VIX": (5, 100),
        "Unemployment_Rate": (0, 20),
    }
    for col, (lo, hi) in range_checks.items():
        if col in df and not df[col].between(lo, hi).all():
            issues.append(f"{col} has values outside [{lo}, {hi}]")
    return issues


def main():
    fred = load_fred()
    bls_monthly = load_bls_monthly()
    business_days = pd.bdate_range(START_DATE, END_DATE)

    cpi_yoy_monthly = compute_cpi_yoy(bls_monthly)
    bls_aligned = align_to_business_days(cpi_yoy_monthly, business_days)

    df = fred.reindex(business_days).join(bls_aligned)

    df["Yield_Curve_Spread"] = df["Treasury_10Y_Yield"] - df["Treasury_2Y_Yield"]
    df["Real_Yield_10Y"] = df["Treasury_10Y_Yield"] - df["CPI_Headline_YoY"]

    df = df[FINAL_COLUMNS]
    df.index.name = "Date"

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH)
    print(f"Saved {len(df)} rows x {len(df.columns)} columns to {OUTPUT_PATH}")

    issues = validate(df)
    if issues:
        print("\nValidation warnings:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("Validation passed: no nulls, ranges sane, date span and row count OK.")


if __name__ == "__main__":
    main()
