# Interest Rate Dynamics Dashboard - Project Plan

## Executive Summary

Build a comprehensive financial analytics dashboard showcasing interest rate dynamics across US markets. **8 interactive dashboards**, **15 financial metrics**, **1-year historical data**. Timeline: **6-8 weeks**.

---

## Phase Overview

| Phase | Duration | Deliverables | Status |
|-------|----------|--------------|--------|
| **Phase 1: Foundation** | Weeks 1-2 | Data pipeline, ETL scripts, CSV ready | 📋 Not Started |
| **Phase 2: Core Dashboards** | Weeks 3-4 | Dashboards 1-3 built & functional | 📋 Not Started |
| **Phase 3: Advanced Analytics** | Weeks 5-6 | Dashboards 4-8, correlations, signals | 📋 Not Started |
| **Phase 4: Polish & Publish** | Weeks 7-8 | Documentation, final polish, GitHub ready | 📋 Not Started |

---

## Phase 1: Foundation (Weeks 1-2)

### Week 1: Setup & Data Architecture

**Goals:**
- [ ] API credentials obtained
- [ ] Python environment configured
- [ ] Data fetching script written & tested
- [ ] First dataset pulled

**Tasks:**

1. **Setup**
   - [ ] Create Python virtual environment
   - [ ] Install dependencies (pandas, requests, yfinance)
   - [ ] Create project structure locally

2. **Data Sources - FRED API**
   - [ ] Register for FRED API key (https://fred.stlouisfed.org/docs/api/)
   - [ ] Write `fetch_fred_data.py` to pull:
     - Fed Funds Rate
     - Treasury yields (2Y, 5Y, 10Y)
     - SOFR
     - Gold prices
     - Credit spreads (HY OAS)
     - Repo rates
     - Dollar Index
     - VIX
     - M2 Money Supply
   - [ ] Test API calls & data validation
   - [ ] Save to `data/raw/fred_raw.csv`

3. **Data Sources - BLS API**
   - [ ] Register for BLS API key
   - [ ] Write `fetch_bls_data.py` to pull:
     - CPI (headline & core)
     - PPI
     - Unemployment rate
     - Initial jobless claims
   - [ ] Test API calls & validation
   - [ ] Save to `data/raw/bls_raw.csv`

4. **Data Sources - Other**
   - [ ] Mortgage rates (Federal Reserve website)
   - [ ] Yield curve data
   - [ ] Save to `data/raw/other_sources.csv`

**Deliverables:**
- ✅ 3 CSV files with raw data
- ✅ Python scripts documented
- ✅ Data validation checks passing

---

### Week 2: Data Processing & Metrics

**Goals:**
- [ ] Data cleaned & standardized
- [ ] Derived metrics calculated
- [ ] Final master CSV ready
- [ ] Data quality validated

**Tasks:**

1. **Data Cleaning**
   - [ ] Write `data_processor.py`:
     - Align all data to daily frequency
     - Forward-fill missing values (weekly/monthly data)
     - Remove outliers/errors
     - Standardize date formats
     - Combine all sources into one DataFrame
   - [ ] Data quality checks:
     - No null values in key metrics
     - Date range: Sept 2024 - Sept 2025
     - ~250 rows total

2. **Derived Metrics Calculations**
   - [ ] Write `calculate_metrics.py`:
     - Real yields = 10Y Treasury - CPI
     - Yield curve spread = 10Y - 2Y
     - YoY inflation change
     - YoY rate change
     - Rolling 30-day correlation matrix
     - Unemployment trend

3. **Final Dataset**
   - [ ] Create `interest_rates_data.csv`:
     - Columns: Date, all 15 metrics, derived metrics
     - Clean, validated data
     - Ready for Tableau
   - [ ] Data dictionary created
   - [ ] Sample statistics documented

4. **Documentation**
   - [ ] DATA_SOURCES.md written
   - [ ] METHODOLOGY.md written
   - [ ] Data lineage documented

**Deliverables:**
- ✅ `data/interest_rates_data.csv` (250 rows × 18 columns)
- ✅ Python ETL scripts (fetch, process, calculate)
- ✅ Data documentation complete
- ✅ GitHub repo initialized & Phase 1 code committed

---

## Phase 2: Core Dashboards (Weeks 3-4)

### Week 3: Dashboards 1-2

**Goals:**
- [ ] Dashboard 1 (Executive Summary) complete
- [ ] Dashboard 2 (Rate Dynamics) complete
- [ ] Design system applied
- [ ] Interactivity tested

**Tasks:**

1. **Dashboard 1: Executive Summary**
   - [ ] KPI cards (Fed Rate, CPI %, SOFR, Gold Price)
   - [ ] Gauge charts (current vs historical range)
   - [ ] Trending arrows (up/down/neutral)
   - [ ] Last update timestamp
   - [ ] 4-5 key metrics prominently displayed
   - See CHARTS_SPECIFICATION.md for exact requirements

2. **Dashboard 2: Rate Dynamics**
   - [ ] Multi-line chart: Fed Funds, SOFR, Repo Rate (1-year trend)
   - [ ] Multi-line chart: Treasury yields (2Y, 5Y, 10Y)
   - [ ] Spread analysis: Fed Rate vs Repo Rate
   - [ ] Prime rate vs Fed Funds alignment
   - [ ] Interactive date filter
   - [ ] Hover tooltips enabled

3. **Design Application**
   - [ ] Apply color palette (blues for rates, greens for safe assets)
   - [ ] Typography: Consistent fonts & sizes
   - [ ] Grid layout & alignment
   - [ ] Tooltip formatting
   - [ ] Title & subtitle clear
   - [ ] Data source attribution

4. **Testing**
   - [ ] All charts pulling correct data
   - [ ] Filters working properly
   - [ ] No errors/warnings in Tableau
   - [ ] Performance acceptable

**Deliverables:**
- ✅ Dashboard 1 (.twb file)
- ✅ Dashboard 2 (.twb file)
- ✅ Design system implemented
- ✅ Screenshots saved to assets/

---

### Week 4: Dashboard 3

**Goals:**
- [ ] Dashboard 3 (Inflation Analysis) complete
- [ ] Dual-axis charts working
- [ ] Narrative explanations added
- [ ] Phase 2 complete & committed

**Tasks:**

1. **Dashboard 3: Inflation Analysis**
   - [ ] Dual-axis chart: Fed Funds Rate (line) vs CPI % (bars)
     - Show lag relationship (2-3 month offset)
   - [ ] Headline vs Core CPI comparison
   - [ ] Month-over-month inflation changes (bars)
   - [ ] YoY inflation rate trend
   - [ ] Annotations: Fed rate hike dates
   - [ ] Story: "Is rate hikes fighting inflation?"

2. **Narrative & Context**
   - [ ] Explanatory text on each dashboard
   - [ ] Key insights called out
   - [ ] Data source citations
   - [ ] Last refresh date shown

3. **Finalizations**
   - [ ] Save as `.twb` files
   - [ ] Screenshot each dashboard
   - [ ] Document design choices in dashboard_design.md
   - [ ] Quality assurance pass

**Deliverables:**
- ✅ Dashboard 3 (.twb file)
- ✅ All 3 dashboards with consistent design
- ✅ Screenshots for portfolio
- ✅ Phase 2 complete & GitHub committed

---

## Phase 3: Advanced Analytics Dashboards (Weeks 5-6)

### Week 5: Dashboards 4-5

**Goals:**
- [ ] Dashboard 4 (Correlations) complete with heatmap
- [ ] Dashboard 5 (Real Yields) complete
- [ ] Advanced analytics showcased

**Tasks:**

1. **Dashboard 4: Correlation Matrix**
   - [ ] Heatmap: All metrics correlation (15×15)
     - Color coded: Red (negative), white (neutral), green (positive)
   - [ ] Scatter plots: Select key correlations
     - Interest rates vs inflation
     - Interest rates vs gold
     - Real yields vs equity returns
   - [ ] Interpretation text: "What correlations tell us"
   - [ ] Interactive: Highlight row/column on hover

2. **Dashboard 5: Real Yields & Asset Prices**
   - [ ] Line chart: Nominal vs Real 10Y yields
   - [ ] Real yield trend (calculated metric)
   - [ ] Gold price vs real yields (inverse relationship)
   - [ ] Equity index (S&P 500) vs interest rates
   - [ ] Story: "Why real yields matter for investors"

3. **Technical Execution**
   - [ ] Correlation calculation validated
   - [ ] Chart formatting matches design system
   - [ ] Color palette applied consistently
   - [ ] Performance tested

**Deliverables:**
- ✅ Dashboard 4 (.twb)
- ✅ Dashboard 5 (.twb)
- ✅ Correlation matrix calculated & visualized
- ✅ Professional heatmap implementation

---

### Week 6: Dashboards 6-8

**Goals:**
- [ ] Dashboard 6 (Year-over-Year) complete
- [ ] Dashboard 7 (Recession Signals) complete
- [ ] Dashboard 8 (Consumer Impact) complete
- [ ] All 8 dashboards functional

**Tasks:**

1. **Dashboard 6: Year-over-Year Comparisons**
   - [ ] Bar charts: Current vs 1-year-ago
     - Fed rate, CPI, Treasury yields, gold
   - [ ] Waterfall chart: How we got here (rate hike sequence)
   - [ ] Percentage change indicators
   - [ ] Timeline annotation: Major events in past year

2. **Dashboard 7: Recession Signals**
   - [ ] Yield curve (2Y/10Y spread) - KEY metric
     - Highlight inversions (red)
   - [ ] VIX level & trend (volatility gauge)
   - [ ] Credit spreads (HY OAS) - corporate stress
   - [ ] Jobless claims trend
   - [ ] Interpretation: "Market recession probability"

3. **Dashboard 8: Consumer Impact**
   - [ ] Mortgage rates trend (30-year)
   - [ ] Fed rate vs mortgage rates alignment
   - [ ] Unemployment rate chart
   - [ ] Wage growth vs inflation (if data available)
   - [ ] Story: "How does this affect regular people?"

4. **Quality Assurance**
   - [ ] All 8 dashboards tested
   - [ ] Cross-dashboard consistency
   - [ ] Data accuracy verified
   - [ ] Performance acceptable
   - [ ] All filters working

**Deliverables:**
- ✅ Dashboard 6, 7, 8 (.twb files)
- ✅ All 8 dashboards complete & functional
- ✅ Master workbook: interest_rate_dynamics.twbx
- ✅ Screenshots of all dashboards

---

## Phase 4: Polish & Documentation (Weeks 7-8)

### Week 7: Aesthetics & Refinement

**Goals:**
- [ ] All dashboards visually polished
- [ ] Consistent branding throughout
- [ ] User experience optimized

**Tasks:**

1. **Visual Polish**
   - [ ] Color consistency audit across all 8 dashboards
   - [ ] Font sizing & hierarchy review
   - [ ] Alignment & spacing checks
   - [ ] Remove clutter, unnecessary elements
   - [ ] Ensure accessibility (color-blind friendly)

2. **Interactivity**
   - [ ] Date range filters working smoothly
   - [ ] Metric toggles functional
   - [ ] Hover tooltips informative
   - [ ] Drill-down capabilities where applicable

3. **Branding & Design Assets**
   - [ ] Logo/branding if applicable
   - [ ] Color palette standardized
   - [ ] Font guidelines documented
   - [ ] Asset library created

**Deliverables:**
- ✅ Polished master workbook
- ✅ Design assets folder complete
- ✅ Consistent visual identity

---

### Week 8: Documentation & Final Publish

**Goals:**
- [ ] Complete documentation
- [ ] GitHub repo publication ready
- [ ] Portfolio presentation ready

**Tasks:**

1. **Documentation Completion**
   - [ ] DASHBOARD_DESIGN.md - finalized
   - [ ] CHARTS_SPECIFICATION.md - finalized
   - [ ] Dashboard_guide.md - user guide for each dashboard
   - [ ] TECHNICAL_SETUP.md - complete environment setup
   - [ ] ROADMAP.md - future enhancements

2. **GitHub Repository**
   - [ ] All code committed & documented
   - [ ] README.md final version
   - [ ] .gitignore properly configured
   - [ ] Tableau workbooks saved
   - [ ] Screenshots added
   - [ ] Data files organized

3. **Portfolio Preparation**
   - [ ] Screenshots prepared (3-4 per dashboard)
   - [ ] Brief case study written
   - [ ] Key insights documented
   - [ ] LinkedIn post prepared
   - [ ] GitHub README showcase-ready

4. **Final QA**
   - [ ] End-to-end testing
   - [ ] Documentation review
   - [ ] Links/references working
   - [ ] No broken visualizations

**Deliverables:**
- ✅ Complete GitHub repository
- ✅ All documentation finalized
- ✅ Portfolio-ready project
- ✅ Case study & insights documented

---

## Success Metrics

### Must-Haves (Do Not Skip)
- ✅ All 8 dashboards created & functional
- ✅ 15 financial metrics tracked
- ✅ 1-year historical data
- ✅ Clean GitHub repository
- ✅ Professional documentation
- ✅ Data sources properly cited

### Nice-to-Haves (If Time Allows)
- ✅ Automated monthly data refresh (Cloud Run + Google Sheets)
- ✅ Interactive filters across all dashboards
- ✅ Drill-down capabilities
- ✅ Mobile-responsive design

---

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| API rate limits | High | Batch requests, cache data locally |
| Data quality issues | High | Validation checks in pipeline |
| Tableau skills gap | Medium | Follow templates, use resources |
| Time overrun | Medium | Prioritize core 6 dashboards first |
| Data source changes | Low | Document all sources, version control |

---

## Dependencies

- Python 3.8+
- Tableau Desktop (free edition)
- API keys: FRED, BLS
- Internet connection
- ~2GB local storage

---

## Sign-Off

**Project Lead:** Adarsh Murali  
**Start Date:** Sept 15, 2026  
**Planned End Date:** Oct 26, 2026  
**Last Updated:** Sept 15, 2026

---

**Track progress in STATUS.md**
