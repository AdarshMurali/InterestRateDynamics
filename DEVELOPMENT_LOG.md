# Development Log

**Project:** Interest Rate Dynamics Dashboard  
**Purpose:** Track progress, learnings, decisions, and blockers  
**Updated:** Weekly (or as needed)

---

## Week 1: Sept 15-21, 2026 - Foundation

### Tasks Planned
- [ ] Setup Python environment
- [ ] Get FRED API credentials
- [ ] Get BLS API credentials  
- [ ] Write data fetching script
- [ ] Test first data pull

### Progress Log

**Sept 15 - Project Kickoff**
- Created project structure
- Wrote documentation templates (README, PROJECT_PLAN, STATUS, DASHBOARD_DESIGN, CHARTS_SPEC)
- Established 8-dashboard architecture with 30 distinct charts
- Defined color palette and design system
- **Hours:** 6 hours (documentation & planning)
- **Status:** 📋 Documentation complete, ready to code

**Sept 16-17 - API Setup**
- [ ] Get FRED API key
- [ ] Get BLS API key
- [ ] Create config.py for credentials
- **Notes:** TBD

**Sept 18-20 - Data Fetching**
- [ ] Write fetch_fred_data.py
- [ ] Write fetch_bls_data.py
- [ ] Write fetch_other_data.py (gold, mortgage rates, etc.)
- [ ] Test API calls
- **Notes:** TBD

**Sept 21 - End of Week Review**
- [ ] All 3 raw CSV files created
- [ ] Data validated
- [ ] Commit to GitHub
- **Hours:** TBD
- **Notes:** TBD

### Learnings This Week
- TBD

### Blockers/Issues
- None yet

### Decisions Made
- None this week (already made in kickoff)

---

## Week 2: Sept 22-28 - Data Processing

### Tasks Planned
- [ ] Write data_processor.py
- [ ] Write calculate_metrics.py
- [ ] Create final master CSV
- [ ] Data quality validation

### Progress Log

**Sept 22 - Data Cleaning**
- [ ] TBD

**Sept 23-24 - Metrics Calculation**
- [ ] Real yields = 10Y Treasury - CPI
- [ ] Yield curve spread = 10Y - 2Y
- [ ] Rolling correlations
- [ ] YoY changes
- [ ] TBD

**Sept 25 - Final Dataset**
- [ ] Master CSV ready
- [ ] All 15 metrics complete
- [ ] No nulls, validated
- [ ] TBD

**Sept 28 - Week Review**
- [ ] Commit Phase 1 to GitHub
- [ ] Document any issues
- **Hours:** TBD

### Learnings This Week
- TBD

### Blockers/Issues
- TBD

### Decisions Made
- TBD

---

## Week 3: Sept 29-Oct 5 - Dashboards 1-2

### Tasks Planned
- [ ] Build Dashboard 1: Executive Summary
- [ ] Build Dashboard 2: Rate Dynamics
- [ ] Apply design system
- [ ] Test all charts

### Progress Log

**Sept 29 - Dashboard 1 Kickoff**
- [ ] KPI cards setup (Fed Rate, CPI, SOFR, Gold)
- [ ] Large dual-axis chart
- [ ] Gauge charts
- **Notes:** TBD

**Oct 1-3 - Dashboard 2**
- [ ] Multi-line: Interest rates
- [ ] Multi-line: Treasury yields
- [ ] Area chart: Spreads
- [ ] Bar chart: Prime rate alignment
- **Notes:** TBD

**Oct 4-5 - Design & Testing**
- [ ] Apply color palette
- [ ] Check interactivity
- [ ] Screenshots for portfolio
- [ ] Test date filters
- **Notes:** TBD

### Learnings This Week
- TBD

### Blockers/Issues
- TBD

### Decisions Made
- TBD

---

## Week 4: Oct 6-12 - Dashboard 3

### Tasks Planned
- [ ] Build Dashboard 3: Inflation Analysis
- [ ] Dual-axis chart (Fed rate lagged vs CPI)
- [ ] Narrative text
- [ ] Phase 2 commit

### Progress Log

**Oct 6-7 - Main Chart**
- [ ] Dual-axis setup
- [ ] Lag implementation (2-3 months)
- [ ] Annotations for Fed meetings
- **Notes:** TBD

**Oct 8-9 - Supporting Charts**
- [ ] Headline vs Core CPI
- [ ] Monthly CPI changes
- [ ] YoY inflation trend
- **Notes:** TBD

**Oct 10-12 - Finalization**
- [ ] Narrative boxes added
- [ ] Insights documented
- [ ] Phase 2 commit
- [ ] Screenshots
- **Notes:** TBD

### Learnings This Week
- TBD

### Blockers/Issues
- TBD

### Decisions Made
- TBD

---

## Week 5: Oct 13-19 - Dashboards 4-5

### Tasks Planned
- [ ] Build Dashboard 4: Correlations
- [ ] Build Dashboard 5: Real Yields
- [ ] Advanced analytics

### Progress Log

**Oct 13-15 - Dashboard 4**
- [ ] Correlation heatmap (15×15 matrix)
- [ ] Scatter plots
- [ ] Interaction setup
- **Notes:** TBD

**Oct 16-19 - Dashboard 5**
- [ ] Real vs nominal yields
- [ ] Gold inverse relationship
- [ ] Equity sensitivity
- [ ] KPI cards for real yields
- **Notes:** TBD

### Learnings This Week
- TBD

### Blockers/Issues
- TBD

### Decisions Made
- TBD

---

## Week 6: Oct 20-26 - Dashboards 6-8

### Tasks Planned
- [ ] Build Dashboard 6: Year-over-Year
- [ ] Build Dashboard 7: Recession Signals
- [ ] Build Dashboard 8: Consumer Impact
- [ ] Master workbook finalized

### Progress Log

**Oct 20-22 - Dashboard 6**
- [ ] YoY comparisons (bars)
- [ ] Waterfall (Fed rate changes)
- [ ] Narrative
- **Notes:** TBD

**Oct 23-24 - Dashboard 7**
- [ ] Yield curve inversion chart
- [ ] VIX gauge
- [ ] Credit spreads
- [ ] Jobless claims
- **Notes:** TBD

**Oct 25-26 - Dashboard 8**
- [ ] Mortgage rates trend
- [ ] Unemployment
- [ ] Cost of living impact
- [ ] KPI cards
- [ ] Master workbook created
- **Notes:** TBD

### Learnings This Week
- TBD

### Blockers/Issues
- TBD

### Decisions Made
- TBD

---

## Week 7: Oct 27-Nov 2 - Polish

### Tasks Planned
- [ ] Visual audit
- [ ] Consistency check
- [ ] Design refinements
- [ ] Accessibility review

### Progress Log

**Oct 27-28 - Audit**
- [ ] Color consistency across all 8 dashboards
- [ ] Font sizes and hierarchy
- [ ] Alignment and spacing
- **Notes:** TBD

**Oct 29-31 - Refinements**
- [ ] Fix any inconsistencies
- [ ] Optimize tooltips
- [ ] Test color-blind accessibility
- **Notes:** TBD

**Nov 1-2 - Final Polish**
- [ ] Remove clutter
- [ ] Ensure white space usage
- [ ] Final QA pass
- **Notes:** TBD

### Learnings This Week
- TBD

### Blockers/Issues
- TBD

### Decisions Made
- TBD

---

## Week 8: Nov 3-9 - Documentation & Publish

### Tasks Planned
- [ ] Complete all documentation
- [ ] GitHub final polish
- [ ] Case study writing
- [ ] Portfolio prep

### Progress Log

**Nov 3-4 - Documentation**
- [ ] Dashboard guides written
- [ ] Methodology documented
- [ ] All .md files finalized
- **Notes:** TBD

**Nov 5-6 - GitHub**
- [ ] Final repo organization
- [ ] README polish
- [ ] Screenshots organized
- [ ] .gitignore clean
- **Notes:** TBD

**Nov 7-9 - Portfolio**
- [ ] Case study written
- [ ] LinkedIn post drafted
- [ ] Project summary created
- [ ] Ready to share
- **Notes:** TBD

### Learnings This Week
- TBD

### Blockers/Issues
- TBD

### Decisions Made
- TBD

---

## Key Learnings & Insights

### Data Insights
(To be filled as project progresses)

- Interest rate transmission: How Fed rates flow through to consumer rates
- Gold correlation: Strong inverse to real yields
- Yield curve: Leading indicator for recessions
- Inflation lag: CPI responds to rate changes 2-3 months later

### Technical Learnings
(To be filled)

- Tableau best practices for financial dashboards
- Date handling and timezone considerations
- Correlation calculations and heatmap visualization
- Color accessibility for colorblind users

### Design Learnings
(To be filled)

- Effective use of dual-axis charts for comparing different scales
- Annotation techniques for marking important dates
- KPI card design for quick scanning
- Storytelling through dashboards

---

## Design Decisions Made

### Decision 1: 8 Dashboards
**Date:** Sept 15, 2026  
**Rationale:** Shows breadth of analytics skills, strong portfolio piece  
**Status:** ✅ Confirmed

### Decision 2: Color Palette
**Date:** Sept 15, 2026  
**Choices:** Blue (rates), Red (inflation), Gold (gold), Green (yields)  
**Rationale:** Semantically aligned with meanings, colorblind accessible  
**Status:** ✅ Confirmed

### Decision 3: 15 Metrics vs 6
**Date:** Sept 15, 2026  
**Rationale:** Richer analysis, more impressive, still manageable  
**Status:** ✅ Confirmed

### Decision 4: Local CSV (vs automated)
**Date:** Sept 15, 2026  
**Rationale:** Focus on BI work first, can automate later  
**Status:** ✅ Confirmed

---

## Risks & Mitigations

### Risk: Scope Creep
**Status:** 🟢 Low  
**Mitigation:** Fixed 8 dashboards, 30 charts, 15 metrics  
**Owner:** Adarsh  

### Risk: Data Quality Issues
**Status:** 🟢 Low  
**Mitigation:** Built validation checks into pipeline  
**Owner:** Adarsh

### Risk: Tableau Skills Gap
**Status:** 🟡 Medium  
**Mitigation:** Reference CHARTS_SPECIFICATION.md for each chart  
**Owner:** Adarsh

### Risk: Time Overrun
**Status:** 🟡 Medium  
**Mitigation:** Prioritize dashboards 1-3 first, 4-8 can be simplified if needed  
**Owner:** Adarsh

---

## Questions & Open Items

1. Should auto-refresh be added post-launch?
2. Will Tableau Public be used or stick with local workbook?
3. Any additional metrics to track?

---

## Resources & References

- Tableau Chart Types: https://help.tableau.com/current/pro/desktop/en-us/viewparts_charts_chartypes.htm
- Federal Reserve FRED API: https://fred.stlouisfed.org/docs/api/
- BLS API Documentation: https://www.bls.gov/developers/api_python.htm
- Design System Template: See DASHBOARD_DESIGN.md

---

**Last Updated:** Sept 15, 2026  
**Next Update:** Sept 21, 2026 (End of Week 1)
