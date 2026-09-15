# Data Sources Specification

Complete guide to collecting all 15 financial metrics for the Interest Rate Dynamics Dashboard.

---

## Overview

**Total Metrics:** 15  
**Time Period:** Last 12 months (Sept 2024 - Sept 2025)  
**Update Frequency:** Monthly (for portfolio project)  
**Total Data Size:** ~250-300 rows × 18 columns  

---

## Data Source 1: Federal Reserve (FRED API)

**Official Name:** Federal Reserve Economic Data (FRED)  
**API:** REST API  
**Cost:** Free  
**Rate Limit:** 120 requests per minute  

### Setup
```
Website: https://fred.stlouisfed.org/docs/api/
1. Create free account
2. Get API key (immediate)
3. Keep key in config.py (don't commit to GitHub)
```

### Metrics from FRED (10 metrics)

| Metric | FRED Series ID | Type | Frequency | Use Case |
|--------|---------------|------|-----------|----------|
| **Fed Funds Rate** | FEDFUNDS | Daily | Daily | Primary policy rate |
| **SOFR (Overnight)** | SOFR | Daily | Daily | LIBOR replacement |
| **Repo Rate (Overnight)** | TGCRRATE | Daily | Daily | Funding market health |
| **Prime Loan Rate** | DPRIME | Daily | Daily | Consumer rate anchor |
| **Treasury 2-Year** | DGS2 | Daily | Daily | Short-term yields |
| **Treasury 5-Year** | DGS5 | Daily | Daily | Medium yields |
| **Treasury 10-Year** | DGS10 | Daily | Daily | Long-term yields |
| **Gold Spot Price** | *(Yahoo Finance, GC=F)* | Daily | Daily | Risk-off indicator |
| **Dollar Index (Broad)** | DTWEXBGS | Daily | Daily | USD strength |
| **Credit Spreads (HY OAS)** | BAMLH0A0HYM2 | Daily | Daily | Corporate stress |

> **Corrected 2026-09-15:** `SOFRCMPD` and `GOLDAMND` don't exist on FRED (404). `MMNRNJ` exists but is a discontinued money-market deposit rate, not the prime rate. `DEXUSEU` is the USD/EUR exchange rate, not a broad dollar index. `M2` (below) is discontinued in favor of `M2SL`. FRED also discontinued its daily LBMA gold series in 2022, so gold is now fetched from Yahoo Finance instead. See `python/fetch_fred_data.py` for the verified IDs actually used.

### Additional FRED Series

| Metric | Series ID | Type | Frequency |
|--------|-----------|------|-----------|
| M2 Money Supply | M2SL | Monthly | Monthly |
| VIX (via other source, but FRED has historical) | VIXCLS | Daily | Daily |
| Mortgage Rate (30Y) | MORTGAGE30US | Weekly | Weekly |
| Initial Jobless Claims | ICSA | Weekly | Weekly |
| Real Yields (calculated) | DGS10 - INFLATION (calculated) | Derived | Daily |
| Yield Curve Spread (calculated) | DGS10 - DGS2 (calculated) | Derived | Daily |

> **Note:** Mortgage rate and Initial Jobless Claims are fetched here via FRED (`python/fetch_fred_data.py`), not via BLS as the table below originally suggested for jobless claims -- `ICSA` is a FRED/Dept. of Labor series with no BLS timeseries equivalent.

### FRED API Example Call

```python
import requests
import pandas as pd

API_KEY = "your_api_key_here"
BASE_URL = "https://api.stlouisfed.org/fred/series/data"

def fetch_fred(series_id, start_date="2024-09-01", end_date="2025-09-15"):
    params = {
        'series_id': series_id,
        'api_key': API_KEY,
        'file_type': 'json',
        'observation_start': start_date,
        'observation_end': end_date
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    df = pd.DataFrame(data['observations'])
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    return df[['date', 'value']].rename(columns={'value': series_id})

# Example
fed_funds = fetch_fred('FEDFUNDS')
print(fed_funds.head())
```

---

## Data Source 2: Bureau of Labor Statistics (BLS API)

**Official Name:** Bureau of Labor Statistics Data Tools  
**API:** REST API  
**Cost:** Free  
**Rate Limit:** 500 requests per IP per day  

### Setup
```
Website: https://www.bls.gov/developers/
1. Register for API key (free)
2. Add key to config.py
3. Can make queries without key but limited
```

### Metrics from BLS (3 metrics)

| Metric | Series ID | Type | Frequency | Use Case |
|--------|-----------|------|-----------|----------|
| **CPI - Headline (US, All Urban)** | CUUR0000SA0 | Monthly | Monthly | Main inflation measure |
| **CPI - Core (Ex. Food & Energy)** | CUUR0000SA0L1E | Monthly | Monthly | Underlying inflation |
| **Unemployment Rate (US, Total)** | LNS14000000 | Monthly | Monthly | Labor market |

**Initial Jobless Claims (ICSA)** is fetched via FRED instead -- see the "Additional FRED Series" table above.

### BLS API Example Call

```python
import requests
import json

API_KEY = "your_bls_api_key"
BASE_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

def fetch_bls(series_id_list, start_year=2024, end_year=2025):
    data = {
        'seriesid': series_id_list,
        'startyear': start_year,
        'endyear': end_year,
        'registrationkey': API_KEY
    }
    
    response = requests.post(BASE_URL, json=data)
    results = response.json()
    
    dfs = []
    for series in results['Results']['series']:
        series_id = series['seriesID']
        df_temp = pd.DataFrame(series['data'])
        df_temp['date'] = pd.to_datetime(
            df_temp['year'].astype(str) + '-' + 
            df_temp['period'].str.replace('M', '').astype(str) + 
            '-01'
        )
        df_temp['value'] = pd.to_numeric(df_temp['value'])
        dfs.append(df_temp[['date', 'value']].rename(columns={'value': series_id}))
    
    return pd.concat(dfs, axis=1)

# Example
series_list = ['CUUR0000SA0', 'LNS14000000']
cpi_data = fetch_bls(series_list)
```

---

## Data Source 3: Federal Reserve (Non-API Sources)

**Source:** Federal Reserve website (direct download)  
**Cost:** Free  

### Metrics Collected (3 metrics)

| Metric | Source | Type | Frequency | Notes |
|--------|--------|------|-----------|-------|
| **Mortgage Rates (30Y)** | Federal Reserve H.15 Release | Weekly | Weekly | Published Thursdays |
| **Repo Rate (Term)** | Fed OMO data | Daily | Daily | Open Market Operations |
| **Fed Balance Sheet (Assets)** | Fed's H.41 Release | Weekly | Weekly | QE/QT indicator |

### Collection Method

1. **Mortgage Rates:**
   - URL: https://www.federalreserve.gov/datadownload/
   - Data: H.15 Economic Report of the President
   - Frequency: Weekly (updated Thursdays)
   - Manual download or via FRED (MORTGAGE30US)

2. **Repo Rates:**
   - URL: https://www.federalreserve.gov/data.htm
   - Data: Reverse Repurchase Agreement Rates
   - Frequency: Daily
   - Can be found on Fed's Open Market Operations page

3. **Fed Balance Sheet:**
   - URL: https://www.federalreserve.gov/releases/h41/
   - Data: Monetary Authority Balance Sheet
   - Frequency: Weekly
   - Download as CSV

---

## Data Source 4: World Bank / OECD (Commodities)

**Source:** World Bank Commodity Price Data  
**Cost:** Free  

### Metrics (Already covered by FRED but alternative)

| Metric | Source | Frequency |
|--------|--------|-----------|
| Gold prices | World Bank Commodity Data | Monthly |
| Oil prices | World Bank | Monthly |

**Note:** FRED has more complete daily data for gold, so prioritize FRED.

---

## Data Source 5: NY Federal Reserve (SOFR & Repo)

**Official Source:** ny.frb.org  
**Cost:** Free  

### Reference Data

| Metric | Release | Frequency | URL |
|--------|---------|-----------|-----|
| SOFR | Daily SOFR | Daily | https://www.newyorkfed.org/markets/reference_rates/sofr |
| Repo Rates | Daily Repo | Daily | https://www.newyorkfed.org/markets/reference_rates/repo |

**Note:** FRED mirrors this data, so fetching from FRED is sufficient.

---

## Data Transformation & Calculation

### Derived Metrics (Calculated in Pipeline)

1. **Real Yields**
   ```
   Real Yield = Nominal Treasury Yield - CPI (inflation)
   Example: 10Y = 4.50% (Treasury) - 3.42% (CPI) = 1.08% (Real)
   ```

2. **Yield Curve Spread**
   ```
   Spread = 10-Year Treasury - 2-Year Treasury
   Example: 3.50% - 3.15% = 0.35%
   Negative = Inversion (recession risk)
   ```

3. **YoY Inflation Change**
   ```
   YoY Change = (Current Month CPI - Same Month Last Year CPI) / Last Year * 100
   Captures annual inflation rate
   ```

4. **Rate Changes (Monthly)**
   ```
   Change = Current Rate - Previous Month Rate
   Measured in basis points (1 bps = 0.01%)
   ```

5. **Rolling 30-Day Correlations**
   ```
   Calculate Pearson correlation between metrics
   Using 30-day rolling window
   Updated daily
   ```

### Data Alignment & Standardization

**Frequency Alignment:**
```
Daily data:         Fed Funds, SOFR, Treasury yields, Gold, VIX, Dollar Index
Weekly data:        Mortgage rates, Repo rates (some), Jobless claims
Monthly data:       CPI, PPI, Unemployment rate, Fed Balance Sheet
Interpolation:      Forward-fill for missing values (especially monthly → daily)
```

**Data Quality Checks:**

```python
def validate_data(df):
    # Check 1: No null values in key metrics
    assert df[['FEDFUNDS', 'CPIAUCSL']].isnull().sum().sum() == 0
    
    # Check 2: Values in reasonable ranges
    assert (df['FEDFUNDS'] >= 0) & (df['FEDFUNDS'] <= 10)
    assert (df['GOLDAMND'] >= 1000) & (df['GOLDAMND'] <= 3000)
    
    # Check 3: No outliers (>3 std deviations)
    for col in df.columns:
        z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
        assert (z_scores < 3).all()
    
    # Check 4: Date range correct (12 months)
    assert (df['date'].max() - df['date'].min()).days >= 360
    
    return "✓ Data validation passed"
```

---

## Final Master Dataset Structure

**File:** `data/interest_rates_data.csv`  
**Format:** CSV with headers  
**Columns:** ~18 (15 metrics + date + calculated fields)

### Column Names & Order

```
Date                          (YYYY-MM-DD)
Fed_Funds_Rate                (%)
SOFR_Rate                      (%)
Repo_Rate_Overnight            (%)
Prime_Loan_Rate                (%)
Treasury_2Y_Yield              (%)
Treasury_5Y_Yield              (%)
Treasury_10Y_Yield             (%)
Mortgage_30Y_Rate              (%)
CPI_Headline_YoY               (%) - annualized
CPI_Core_YoY                   (%) - annualized
Gold_Spot_Price                (USD/oz)
Dollar_Index                   (Index value)
VIX                            (Index 0-100)
Credit_Spreads_HY_OAS          (basis points)
Unemployment_Rate              (%)
M2_Money_Supply                (Billions USD)
Yield_Curve_Spread             (%) - CALCULATED: 10Y - 2Y
Real_Yield_10Y                 (%) - CALCULATED: 10Y Nominal - CPI
```

### Sample Row

```
2025-09-15,4.50,4.80,4.65,8.00,3.15,3.50,3.50,6.85,3.42,3.10,2450,104.5,18.5,350,4.0,20500,0.85,1.08
```

---

## Update Schedule (For Automation Later)

**Frequency:** Monthly (1st of month)  
**Time:** 2:00 AM UTC (during market hours off-time)

**Order of Updates:**
```
1. FRED API pull (all daily metrics) - happens automatically
2. BLS API pull (monthly CPI, unemployment) - on release dates
3. Manual inputs (mortgage rates, if not on FRED) - download from Fed
4. Validation checks - ensure no gaps
5. Calculations (derived metrics) - real yields, spreads, etc.
6. Data merge - combine all sources
7. Push to Google Sheets/local CSV
8. Tableau auto-refresh
```

---

## Data Lineage & Audit Trail

**Keep record of:**

```
Data Source Log (CSV file):
├─ Date pulled
├─ Source
├─ Series ID
├─ Data points received
├─ Any data corrections applied
└─ Status (Success/Failed)
```

**Example:**

```
Date,Source,SeriesID,Records,Status,Notes
2025-09-15,FRED,FEDFUNDS,250,Success,No issues
2025-09-15,BLS,CUUR0000SA0,12,Success,Sept 2024 - Sept 2025
2025-09-15,Federal_Reserve,Mortgage_30Y,52,Success,Manual download
```

---

## API Credentials & Security

**DO NOT commit to GitHub:**
- FRED API keys
- BLS API keys
- Any credentials

**Setup:**
1. Create `python/config.py` (NOT in Git):
   ```python
   FRED_API_KEY = "your_actual_key"
   BLS_API_KEY = "your_actual_key"
   ```

2. Add to `.gitignore`:
   ```
   python/config.py
   python/.env
   *.pyc
   __pycache__/
   ```

3. Reference in scripts:
   ```python
   from config import FRED_API_KEY, BLS_API_KEY
   ```

---

## Data Refresh Checklist

Before considering data "ready for Tableau":

- [ ] All 15 metrics present
- [ ] Date range: Sept 2024 - Sept 2025
- [ ] No null values in critical columns
- [ ] Values in realistic ranges (no outliers)
- [ ] 250+ rows (daily ≈ 250 business days)
- [ ] CSV headers correct & aligned with Tableau
- [ ] Calculated metrics validated
- [ ] Data source attribution documented
- [ ] Last update timestamp recorded
- [ ] Backup copy saved

---

## Troubleshooting

### Issue: FRED API Rate Limit
**Solution:** Add delays between requests, batch requests efficiently
```python
import time
for series in series_list:
    fetch_fred(series)
    time.sleep(1)  # 1 second delay
```

### Issue: BLS Data Not Available on Expected Release Date
**Solution:** BLS sometimes delays; use previous data, will update when available
```python
try:
    bls_data = fetch_bls(series_list)
except:
    print("Data not yet available, using last update")
    bls_data = load_previous_csv()
```

### Issue: Missing Data for Specific Date
**Solution:** Forward-fill missing values (common for monthly → daily conversion)
```python
df = df.fillna(method='ffill')  # Forward fill
```

### Issue: Data Looks Wrong (Outlier)
**Solution:** Check source, verify calculation, investigate anomaly
```python
# Example: Gold price spike
if gold_price > gold_price.rolling(30).mean() * 1.5:
    print("ALERT: Potential data error or market event")
```

---

## References

- Federal Reserve FRED: https://fred.stlouisfed.org
- BLS Data Tools: https://www.bls.gov/developers/
- NY Federal Reserve: https://www.newyorkfed.org/markets/
- Tableau Data Connection Guide: https://help.tableau.com/current/pro/desktop/en-us/examples_data_connections.htm

---

**Last Updated:** Sept 15, 2026  
**Next Review:** Upon first data pull completion
