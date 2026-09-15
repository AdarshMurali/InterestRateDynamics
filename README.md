# Interest Rate Dynamics Dashboard

## Project Overview

A comprehensive BI dashboard visualizing interest rate dynamics and macroeconomic indicators across US financial markets. Built with Python (data pipeline) and Tableau (8 interactive dashboards), showcasing end-to-end analytics: data integration → correlation analysis → visual storytelling.

**Purpose:** Showcase BI/Analytics portfolio experience (primary goal)  
**Status:** In Development  
**Timeline:** 6-8 weeks  

---

## Project Goals

### Primary Objectives
- ✅ Build 8 comprehensive interactive Tableau dashboards
- ✅ Collect 12-15 financial metrics from authoritative sources
- ✅ Analyze correlations and market dynamics
- ✅ Create professional data visualizations
- ✅ Document financial insights and findings

### Success Criteria
- All dashboards published and functional
- Clear narrative on each dashboard
- Professional portfolio-ready presentation
- GitHub repo with clean documentation
- 12-15 key financial metrics tracked

---

## Quick Start

```bash
# 1. Clone repo
cd interest-rate-dynamics

# 2. Set up environment
pip install -r python/requirements.txt

# 3. Fetch data
python python/fetch_market_data.py

# 4. Open in Tableau Desktop
# Connect to data/interest_rates_data.csv

# 5. Build dashboards
# Follow DASHBOARD_DESIGN.md for specifications
```

---

## Project Structure

```
interest-rate-dynamics/
├── README.md                              # Overview (this file)
├── PROJECT_PLAN.md                        # Detailed roadmap & timeline
├── STATUS.md                              # Progress tracking
├── ROADMAP.md                             # Future enhancements
├── DEVELOPMENT_LOG.md                     # Development notes
│
├── docs/
│   ├── DATA_SOURCES.md                   # Data specifications
│   ├── DASHBOARD_DESIGN.md               # Design system
│   ├── CHARTS_SPECIFICATION.md           # Chart details
│   ├── TECHNICAL_SETUP.md                # Setup guide
│   └── METHODOLOGY.md                    # Analysis approach
│
├── data/
│   ├── interest_rates_data.csv           # Main dataset
│   ├── raw/
│   │   ├── fred_raw.csv
│   │   ├── bls_raw.csv
│   │   └── other_sources.csv
│   └── processed/
│       └── metrics_with_calculations.csv
│
├── python/
│   ├── fetch_market_data.py              # Data fetching
│   ├── data_processor.py                 # Cleaning & transformation
│   ├── calculate_metrics.py              # Derived metrics
│   ├── requirements.txt                  # Dependencies
│   └── config.py                         # Configuration
│
├── tableau/
│   ├── interest_rate_dynamics.twbx       # Main workbook
│   ├── dashboards/
│   │   ├── 01_executive_summary.twb
│   │   ├── 02_rate_dynamics.twb
│   │   ├── 03_inflation_analysis.twb
│   │   ├── 04_correlations.twb
│   │   ├── 05_real_yields.twb
│   │   ├── 06_year_over_year.twb
│   │   ├── 07_recession_signals.twb
│   │   └── 08_consumer_impact.twb
│   ├── docs/
│   │   ├── dashboard_guide.md
│   │   └── design_notes.md
│   └── assets/
│       ├── color_palette.json
│       └── font_guidelines.txt
│
├── assets/
│   ├── color_palette.md                  # Color scheme
│   └── screenshots/                      # Dashboard screenshots
│
└── .gitignore
```

---

## Dashboard Summary

| # | Dashboard | Focus | Status |
|---|-----------|-------|--------|
| 1 | Executive Summary | KPIs & current state | Planned |
| 2 | Rate Dynamics | Interest rate movements | Planned |
| 3 | Inflation Analysis | Policy effectiveness | Planned |
| 4 | Correlations | Market relationships | Planned |
| 5 | Real Yields | Investor perspective | Planned |
| 6 | Year-over-Year | Historical changes | Planned |
| 7 | Recession Signals | Risk indicators | Planned |
| 8 | Consumer Impact | Everyday effects | Planned |

---

## Key Metrics

**Interest Rates:** Fed Funds Rate, SOFR, Repo Rate, Prime Rate, Treasury Yields (2Y/5Y/10Y), Mortgage Rates  
**Inflation:** CPI, PPI, Inflation Expectations  
**Economy:** Unemployment, Jobless Claims, M2 Money Supply  
**Markets:** Gold, Dollar Index, VIX, Credit Spreads, Yield Curve  

**Total: 15 key metrics**

---

## Technology Stack

- **Data:** Python (pandas), CSV
- **Visualization:** Tableau Desktop
- **Publication:** Tableau Public (future)
- **Version Control:** Git + GitHub

---

## Documentation Guide

- **PROJECT_PLAN.md** → Detailed timeline & tasks
- **STATUS.md** → What's done, what's pending
- **DASHBOARD_DESIGN.md** → Visual design & specifications
- **CHARTS_SPECIFICATION.md** → Exact chart requirements
- **DATA_SOURCES.md** → Data collection details
- **TECHNICAL_SETUP.md** → Environment setup

---

**Last Updated:** Sept 15, 2026  
**Project Lead:** Adarsh Murali
