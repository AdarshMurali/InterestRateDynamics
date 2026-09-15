# Dashboard Design System

## Visual Identity

This document defines the complete visual design system for all 8 dashboards in the Interest Rate Dynamics project.

---

## Color Palette

### Primary Colors

```
Fed Funds Rate / Policy:           #1F77B4 (Blue)
Inflation / Risk:                   #D62728 (Red)
Gold / Safe Assets:                 #FFD700 (Gold)
Treasury Yields / Growth:           #2CA02C (Green)
Unemployment / Caution:             #FF7F0E (Orange)
Technical / Background:             #FFFFFF (White)
Text / Neutral:                     #2B2D42 (Dark Blue-Gray)
Subtle / Dividers:                  #CCCCCC (Light Gray)
```

### Secondary Colors (For Contrasts)

```
Negative/Warning:                   #E74C3C (Dark Red)
Positive/Good:                      #27AE60 (Dark Green)
Neutral:                            #95A5A6 (Gray)
Accent:                             #3498DB (Light Blue)
```

### Usage Rules

| Color | Use Case | Examples |
|-------|----------|----------|
| Blue (#1F77B4) | Fed Funds Rate, policy rates | Line charts for Fed Funds |
| Red (#D62728) | Inflation, negative signals | CPI bars, recession warnings |
| Gold (#FFD700) | Gold prices, commodity prices | Gold price trends |
| Green (#2CA02C) | Treasury yields, positive | Yield curves, growing metrics |
| Orange (#FF7F0E) | Unemployment, caution signals | Jobless claims, warnings |

**Important:** Never use red and green together without patterns for colorblind accessibility.

---

## Typography

### Fonts

```
Headings:       Arial, Helvetica, Sans-serif (Bold)
Labels:         Arial, Helvetica, Sans-serif (Regular)
Values/Numbers: Monaco, Courier, Monospace (for precision)
Body Text:      Arial, Helvetica, Sans-serif (Regular)
```

### Font Sizes

```
Dashboard Title:              24px Bold
Section Heading:              18px Bold
Chart Title:                  16px Bold
Axis Labels:                  12px Regular
Tooltip Values:               11px Regular
KPI Card Value:               32px Bold (numbers)
KPI Card Label:               14px Regular
Annotations:                  10px Italic
```

### Font Weights & Emphasis

```
Regular:    400 weight
Bold:       700 weight (for titles, KPIs)
Italic:     For annotations, sources
```

---

## Layout Grid & Spacing

### Dashboard Dimensions

All dashboards: **1200px wide × 800px tall** (Tableau standard)

### Grid System

```
12-column grid, 20px gutter

[████] [████] [████] [████]  (4 columns)
[██████] [██████]            (2 columns)
[████████████]               (1 column)
```

### Spacing Rules

```
Padding (outer):        20px from edge
Padding (inner):        10px between elements
Margin (between sections): 15px
Margin (between charts): 20px
```

### Dashboard Zones

```
┌─────────────────────────────────────────┐
│  HEADER ZONE (100px)                    │
│  [Logo] Dashboard Title    [Refresh]    │
├─────────────────────────────────────────┤
│         MAIN CONTENT ZONE (600px)       │
│  [Chart] [Chart] [Chart]                │
│  [Chart] [Chart]                        │
├─────────────────────────────────────────┤
│  FOOTER ZONE (50px)                     │
│  Data Source: ... | Last Updated: ...   │
└─────────────────────────────────────────┘
```

---

## Dashboard Layouts

### Layout Type A: Analytical (Dashboards 2, 3, 4, 5)

**For charts requiring detail & precision**

```
┌──────────────────────────────────────────┐
│  Dashboard Title                         │
├──────────────────┬───────────────────────┤
│                  │                       │
│   Large Chart 1  │   Chart 2 (smaller)   │
│   (70%)          │   (30%)               │
│                  │                       │
├──────────────────┼───────────────────────┤
│      Chart 3     │      Chart 4          │
│      (50%)       │      (50%)            │
├──────────────────┴───────────────────────┤
│ Data Source | Annotations               │
└──────────────────────────────────────────┘
```

### Layout Type B: KPI-Focused (Dashboard 1)

**For executive summary**

```
┌──────────────────────────────────────────┐
│  Executive Summary                       │
├──────────────────────────────────────────┤
│ [KPI 1] [KPI 2] [KPI 3] [KPI 4]         │
├──────────────────────────────────────────┤
│              Large Chart 1                │
│          (Main narrative)                 │
├──────────────────┬───────────────────────┤
│   Chart 2        │   Chart 3             │
└──────────────────┴───────────────────────┘
```

### Layout Type C: Comparison (Dashboard 6)

**For side-by-side comparisons**

```
┌──────────────────────────────────────────┐
│  Year-over-Year Analysis                 │
├──────────────────┬───────────────────────┤
│   Bar Chart 1    │   Bar Chart 2         │
│   Comparisons    │   Comparisons         │
├──────────────────┼───────────────────────┤
│   Bar Chart 3    │   Bar Chart 4         │
├──────────────────┴───────────────────────┤
│          Waterfall Chart                  │
└──────────────────────────────────────────┘
```

---

## Chart Specifications

### Chart Type: Line Chart
**When:** Trends over time  
**Examples:** Fed Funds Rate, Treasury yields, unemployment trend

**Styling:**
```
Line width:        2px
Point size:        4px (visible on hover)
Color:             Per color palette
Background:        None (white/transparent)
Grid:              Light gray (#CCCCCC), subtle
Axis labels:       12px, left-aligned
Annotations:       Mark key events with vertical lines
```

### Chart Type: Bar Chart
**When:** Comparisons, YoY changes  
**Examples:** CPI monthly changes, rate comparisons

**Styling:**
```
Bar width:         20px
Bar spacing:       5px between bars
Color:             Solid per palette
Borders:           1px, slightly darker than fill
Data labels:       On hover, or inside if space allows
Gradient:          Subtle gradient (optional enhancement)
```

### Chart Type: Dual-Axis Chart
**When:** Comparing different scales  
**Examples:** Fed Rate (axis 1) vs CPI % (axis 2)

**Styling:**
```
Left axis:         #1F77B4 (Blue) - rates
Right axis:        #D62728 (Red) - inflation
Line width:        2px each
Clearly label:     Which metric on which axis
Legend:            Positioned top-right
```

### Chart Type: Heatmap
**When:** Correlation matrix  
**Example:** Dashboard 4 correlation analysis

**Styling:**
```
Color scale:       Red (-1.0) → White (0.0) → Green (+1.0)
Cell size:         40px × 40px
Cell borders:      Light gray, 1px
Values:            Show correlation coefficient (2 decimals)
Font:              11px, bold for emphasis
Interaction:       Highlight row/column on hover
```

### Chart Type: Scatter Plot
**When:** Relationship analysis  
**Example:** Interest rates vs gold prices

**Styling:**
```
Point size:        6px-8px
Point color:       Per relationship
Opacity:           70% (allows overlapping)
Trend line:        Yes, dashed, 2px
Color of trend:    Slightly darker than points
Grid:              Light, subtle
Quadrant labels:   If applicable (positive/negative regions)
```

### Chart Type: Gauge Chart
**When:** Current value vs range  
**Example:** Current Fed Funds Rate in context of historical range

**Styling:**
```
Background:        Light gray
Gauge color:       Blue (#1F77B4)
Range colors:      Green (low) → Yellow (med) → Red (high)
Needle:            Black, 2px
Center value:      Large, bold number
Min/Max labels:    Small, subtle
```

### Chart Type: KPI Card
**When:** Key performance indicators  
**Example:** Current CPI %, Fed Rate, Gold Price

**Styling:**
```
Background:        White with subtle shadow
Border:            1px light gray
Icon/Color:        Top-left, 40×40px, colored
Title:             14px regular, dark gray
Value:             32px bold, dark blue
Change indicator:  Arrow up/down (green/red)
Unit:              12px, gray
```

### Chart Type: Waterfall Chart
**When:** Showing cumulative changes  
**Example:** How Fed rates changed over year (sequence of hikes)

**Styling:**
```
Increase bars:     Green (#2CA02C)
Decrease bars:     Red (#D62728)
Total bar:         Blue (#1F77B4)
Connector lines:   Dashed, light gray
Data labels:       On each bar
X-axis:            Chronological (date or quarter)
```

---

## Interactivity Standards

### Filters (All Dashboards)

```
Date Range Filter:
├─ Default: Last 12 months
├─ Style: Dropdown or date picker
├─ Position: Top-right of dashboard
└─ Apply immediately on change

Metric Toggle (where applicable):
├─ Multi-select checkbox
├─ Default: All metrics shown
├─ Position: Dashboard left sidebar
└─ Allow showing/hiding specific lines
```

### Hover Interactions

```
On hover over any data point:
├─ Show tooltip with value
├─ Highlight that data point
├─ Slightly dim other data
├─ Format: 
│  └─ Date: "Jan 15, 2025"
│  └─ Metric: "Fed Funds Rate"
│  └─ Value: "4.50%"
└─ Font: 11px, dark background, white text
```

### Tooltips Format

```
[Date] [Value] [Change]
Jan 15, 2025 | 4.50% | ↑0.25% (up from prev)
```

---

## Narrative & Annotations

### Dashboard Annotations

**Every dashboard should have:**

1. **Title** (24px bold)
   - Clear, descriptive
   - Example: "Interest Rate Dynamics & Market Impacts"

2. **Subtitle** (14px regular)
   - One-line summary
   - Example: "12-month historical trends with key events"

3. **Key Insight Cards** (optional, on some dashboards)
   - Callout boxes highlighting key findings
   - Example: "Yield curve inversion signals potential recession"
   - Styling: Light background (#F5F5F5), bold text

4. **Source Attribution** (footer)
   - "Data Sources: Federal Reserve FRED API, BLS API"
   - "Last Updated: Sept 15, 2025"
   - Font: 10px, light gray

5. **Event Annotations**
   - Mark important dates with vertical lines
   - Example: Fed rate hike dates
   - Label: 10px italic
   - Color: Light gray dashed lines

### Text on Dashboards

```
Title:                  Narrative Dashboard Name
Subtitle:               1-line summary of what it shows
Left annotation:        "What this means for investors..."
Center annotation:      Key insights & findings
Footer:                 Data sources & refresh date
```

---

## Aesthetic Best Practices

### Do ✅

- ✅ Use consistent colors across related metrics
- ✅ Apply 20px spacing margins consistently
- ✅ Use 12pt minimum font for readability
- ✅ Include data source citations
- ✅ Align chart elements to grid
- ✅ Keep color-blind accessibility in mind
- ✅ Limit charts per dashboard to 4-5 max
- ✅ Use white space to reduce clutter
- ✅ Label axes clearly
- ✅ Include last update timestamp

### Don't ❌

- ❌ Mix colors without reason
- ❌ Use fancy 3D effects or decorations
- ❌ Crowd dashboards with too many charts
- ❌ Use small fonts (< 11px)
- ❌ Apply gradients that reduce readability
- ❌ Mix multiple visualization styles randomly
- ❌ Forget to cite data sources
- ❌ Use bright/neon colors
- ❌ Leave axes unlabeled
- ❌ Create unnecessary clutter

---

## Accessibility Standards

### Color Contrast

```
Text on background:     4.5:1 minimum contrast ratio
Large text:             3:1 minimum
Interactive elements:   3:1 minimum
```

### Color-Blind Friendly

```
Don't rely on red/green alone:
├─ Add patterns (stripes, dots)
├─ Use shape variation
└─ Include text labels

Safe color combinations:
├─ Blue + Orange
├─ Blue + Yellow
├─ Black + White
└─ Dark Blue + Gold
```

### Typography Accessibility

```
Minimum font size:      11px
Line height:            1.5× font size
Letter spacing:         Normal (don't squeeze)
Font weight:            Regular (400) or Bold (700), no weights between
```

---

## Dashboard-Specific Design Notes

### Dashboard 1: Executive Summary
- **Style:** Bright, modern, professional
- **Color Focus:** Blue for Fed, Red for inflation
- **Layout:** KPI cards prominently, then key charts
- **Tone:** "What's happening NOW?"

### Dashboard 2: Rate Dynamics
- **Style:** Technical, detailed
- **Color Focus:** Multiple blues, greens
- **Layout:** Large multi-line chart, supporting details
- **Tone:** "How are rates moving?"

### Dashboard 3: Inflation Analysis
- **Style:** Policy-focused
- **Color Focus:** Blue (rates) + Red (inflation)
- **Layout:** Dual-axis prominently
- **Tone:** "Is the Fed winning?"

### Dashboard 4: Correlations
- **Style:** Academic, data-rich
- **Color Focus:** Heatmap (red/white/green)
- **Layout:** Heatmap center, scatter plots supporting
- **Tone:** "What moves together?"

### Dashboard 5: Real Yields & Assets
- **Style:** Investment-focused
- **Color Focus:** Blue (rates) + Gold
- **Layout:** Multi-line with supporting charts
- **Tone:** "What do investors care about?"

### Dashboard 6: Year-over-Year
- **Style:** Narrative-driven
- **Color Focus:** Green (up) + Red (down)
- **Layout:** Comparison bars + waterfall
- **Tone:** "How have we changed?"

### Dashboard 7: Recession Signals
- **Style:** Alert/warning style
- **Color Focus:** Red (warnings), Blue (normal)
- **Layout:** Key signals prominent, supporting detail
- **Tone:** "What's the recession risk?"

### Dashboard 8: Consumer Impact
- **Style:** Relatable, personal
- **Color Focus:** Orange (caution), Green (good)
- **Layout:** Simple, clear charts
- **Tone:** "How does this affect you?"

---

## Implementation Checklist

**Before finalizing each dashboard:**

- [ ] Colors consistent with palette
- [ ] Fonts: Title 24px, heading 18px, labels 12px
- [ ] Grid spacing: 20px margins, 10px inner padding
- [ ] Charts: 4-5 max per dashboard
- [ ] Axes labeled clearly
- [ ] Data sources cited in footer
- [ ] Last update timestamp visible
- [ ] Tooltips working & informative
- [ ] Colors accessible (color-blind friendly)
- [ ] White space used effectively
- [ ] Mobile/responsive (if applicable)
- [ ] No typos or formatting errors

---

**Design System Version:** 1.0  
**Last Updated:** Sept 15, 2026  
**Reference:** Use this while building each dashboard
