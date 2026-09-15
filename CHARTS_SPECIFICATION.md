# Charts Specification & Requirements

Complete specifications for every chart across all 8 dashboards.

---

## Dashboard 1: Executive Summary

**Purpose:** At-a-glance financial snapshot  
**Layout Type:** KPI-focused  
**Chart Count:** 7 elements

### Chart 1.1: KPI Card - Fed Funds Rate (Current)

```
Type:               KPI Card / Gauge
Data Source:        fed_funds_rate (latest)
Dimensions:         Single value
Metrics:            Current Fed Funds Rate %

Layout:
├─ Top-left position
├─ Width: 23% of dashboard
├─ Height: 120px

Visual:
├─ Large number: 32px bold, blue (#1F77B4)
├─ Label: "Fed Funds Rate" (14px)
├─ Icon: Federal Reserve logo (small, 40×40px)
├─ Background: White with subtle shadow
├─ Border: 1px light gray

Display:
├─ Current value: "4.50%"
├─ Previous value: "4.50%" (reference)
├─ Change indicator: ↑0.25% (red if up, green if down)
├─ Unit: Large, clear "%"

Interaction:
└─ Hover: Show "Updated Sept 15, 2025"
```

### Chart 1.2: KPI Card - CPI (Headline)

```
Type:               KPI Card
Data Source:        cpi_headline (latest YoY)
Dimensions:         Single value
Metrics:            Inflation %

Layout:
├─ Position: Next to Fed Rate card
├─ Width: 23%
├─ Height: 120px

Visual:
├─ Large number: 32px bold, red (#D62728)
├─ Label: "Inflation (Headline CPI YoY)"
├─ Icon: Inflation symbol (40×40px)
├─ Background: White with subtle shadow

Display:
├─ Value: "3.42%"
├─ Change from 3 months ago: ↓0.15%
├─ Trend: "Moderating" (green text)

Interaction:
└─ Hover: "Latest data: Aug 2025"
```

### Chart 1.3: KPI Card - SOFR Current

```
Type:               KPI Card
Data Source:        sofr_rate (latest)

Layout:
├─ Position: Third card
├─ Width: 23%
├─ Height: 120px

Visual:
├─ Number: 32px bold, blue
├─ Label: "SOFR Rate"
├─ Icon: Bank symbol

Display:
├─ Value: "4.80%"
├─ Context: "Overnight financing rate"
```

### Chart 1.4: KPI Card - Gold Price

```
Type:               KPI Card
Data Source:        gold_price (latest USD/oz)

Layout:
├─ Position: Fourth card
├─ Width: 23%
├─ Height: 120px

Visual:
├─ Number: 32px bold, gold (#FFD700)
├─ Label: "Gold Price"
├─ Icon: Gold bar symbol (40×40px)

Display:
├─ Value: "$2,450/oz"
├─ Change YTD: ↑12.5% (green)
```

### Chart 1.5: Large Line Chart - Fed Rate + CPI Trend

```
Type:               Dual-Axis Line Chart
Data Source:        fed_funds_rate, cpi_headline
Time Period:        Last 12 months
Dimensions:         Date (X-axis), Two Y-axes

Layout:
├─ Position: Full width, below KPI cards
├─ Width: 100%
├─ Height: 250px

Metrics:
├─ Left axis: Fed Funds Rate (%) - blue line
├─ Right axis: CPI Headline YoY (%) - red line

Visual:
├─ Fed Rate line: Blue (#1F77B4), 2px width
├─ CPI line: Red (#D62728), 2px width
├─ Grid: Light gray, subtle
├─ Points: Visible on hover (4px)
├─ Annotations: Mark Fed rate hikes with vertical lines

Labels:
├─ Title: "Fed Rate vs Inflation (Last 12 Months)"
├─ X-axis: Monthly intervals (Jan, Feb, Mar...)
├─ Left Y-axis: "Fed Rate (%)" in blue
├─ Right Y-axis: "Inflation (%)" in red
├─ Legend: Top-right corner

Interaction:
├─ Hover: Show both values, date
├─ Tooltip format:
│  └─ "Jan 15, 2025 | Fed: 4.50% | CPI: 3.42%"
├─ Zoom: Allow date range selection
└─ Pan: Allow scrolling through time
```

### Chart 1.6: Gauge Chart - Yield Curve Status

```
Type:               Gauge Chart
Data Source:        yield_curve_spread (10Y - 2Y)
Dimensions:         Single current value

Layout:
├─ Bottom-left
├─ Width: 48%
├─ Height: 120px

Visual:
├─ Gauge range: -1% (left, red) to +2% (right, green)
├─ Needle: Current spread value (black, 2px)
├─ Zones:
│  ├─ Red zone: < 0% (inverted = recession risk)
│  ├─ Yellow zone: 0% - 0.5%
│  └─ Green zone: > 0.5% (normal)

Display:
├─ Current value: "0.85%" (green zone)
├─ Label: "Yield Curve (10Y-2Y Spread)"
├─ Status: "Normal" (green text)

Interpretation:
└─ "Positive spread indicates normal conditions"
```

### Chart 1.7: Gauge Chart - Recession Probability

```
Type:               Gauge Chart / Risk Meter
Data Source:        Composite: yield curve, spreads, vix
Dimensions:         Single composite score

Layout:
├─ Bottom-right
├─ Width: 48%
├─ Height: 120px

Visual:
├─ Gauge: 0 (green, low risk) to 100 (red, high risk)
├─ Needle: Current position (35 = medium-low risk)
├─ Color zones:
│  ├─ Green: 0-25 (Low recession risk)
│  ├─ Yellow: 25-50 (Medium risk)
│  ├─ Orange: 50-75 (High risk)
│  └─ Red: 75-100 (Very high risk)

Display:
├─ Value: "35/100" (green)
├─ Label: "Recession Risk Indicator"
├─ Status: "Low Risk"

Note:
└─ "Based on yield curve, spreads, volatility"
```

---

## Dashboard 2: Rate Dynamics

**Purpose:** Show how different rates move together/apart  
**Layout Type:** Analytical  
**Chart Count:** 4

### Chart 2.1: Multi-Line Chart - All Interest Rates

```
Type:               Multi-Line Chart
Data Source:        fed_funds_rate, sofr, repo_rate, prime_rate
Time Period:        Last 12 months
Dimensions:         Date (X), Rate % (Y)

Layout:
├─ Position: Large, top portion
├─ Width: 70%
├─ Height: 350px

Metrics Shown:
├─ Fed Funds Rate (blue #1F77B4, 2px)
├─ SOFR Rate (light blue #3498DB, 2px)
├─ Repo Rate (green #2CA02C, 2px)
├─ Prime Loan Rate (orange #FF7F0E, 2px)

X-Axis:
├─ Monthly ticks (Jan, Feb, Mar...)
├─ Labels: 12px regular
├─ Grid: Light vertical lines, subtle

Y-Axis:
├─ Range: Auto (based on data min/max)
├─ Label: "Interest Rate (%)"
├─ Grid: Horizontal lines, light gray

Title:
├─ "Interest Rate Transmission (Last 12 Months)"
├─ Subtitle: "How Fed policy flows through the financial system"

Legend:
├─ Position: Top-right
├─ Colors: Matching line colors
├─ Interactive: Click to toggle lines

Annotations:
├─ Mark Fed FOMC meeting dates with vertical dashed lines
├─ Label major policy changes ("Rate hike", "Rate cut")

Interaction:
├─ Hover: Tooltip showing all 4 rates on that date
├─ Zoom: Click & drag to zoom into date range
├─ Filter: Dropdown to show/hide specific rates
└─ Format: "Jan 15, 2025 | Fed: 4.50% | SOFR: 4.80% | Repo: 4.65% | Prime: 8.00%"
```

### Chart 2.2: Multi-Line Chart - Treasury Yields

```
Type:               Multi-Line Chart
Data Source:        treasury_2y, treasury_5y, treasury_10y
Time Period:        Last 12 months

Layout:
├─ Position: Top-right
├─ Width: 30%
├─ Height: 350px

Metrics Shown:
├─ 2-Year Treasury (dashed line, blue)
├─ 5-Year Treasury (solid line, light blue)
├─ 10-Year Treasury (solid line, dark blue)

Visual:
├─ Different styles to distinguish (solid vs dashed)
├─ Colors: Shades of blue
├─ Grid: Subtle, light gray

Title:
├─ "Treasury Yield Curve"
├─ Subtitle: "2Y, 5Y, 10Y trends"

Interaction:
└─ Hover: Show all three values for selected date
```

### Chart 2.3: Area Chart - Fed vs Repo Spread

```
Type:               Area Chart
Data Source:        fed_funds_rate - repo_rate
Time Period:        Last 12 months
Dimensions:         Date (X), Spread in bps (Y)

Layout:
├─ Position: Bottom-left
├─ Width: 48%
├─ Height: 250px

Visual:
├─ Area fill: Light blue (#87CEEB), 60% opacity
├─ Line: Blue (#1F77B4), 2px
├─ Grid: Light gray

Metrics:
├─ Spread = Fed Funds Rate - Repo Rate
├─ Positive spread = Fed policy higher than money market
├─ Negative spread = Stress in funding market

Title:
├─ "Fed Funds vs Repo Rate Spread"
├─ Story: "Funding market health indicator"

Y-Axis:
├─ Label: "Spread (basis points)"
├─ Range: -50 to +200

Annotations:
├─ Red zone highlight if spread goes negative
├─ Label: "Funding stress"

Interaction:
└─ Hover: "Spread: +125 bps (healthy)"
```

### Chart 2.4: Bar Chart - Prime Rate vs Fed Rate Alignment

```
Type:               Bar Chart (Grouped)
Data Source:        fed_funds_rate, prime_rate, difference
Time Period:        Last 12 months (quarterly snapshots)

Layout:
├─ Position: Bottom-right
├─ Width: 48%
├─ Height: 250px

Metrics:
├─ Fed Funds Rate (blue bars)
├─ Prime Loan Rate (orange bars)
├─ Expected difference: ~3.25%

Visual:
├─ Bars side-by-side
├─ Width: 20px
├─ Spacing: 5px between groups
├─ Colors: Blue & Orange

Title:
├─ "Prime Rate Premium Over Fed Rate"
├─ Expected spread: 3.25%

X-Axis:
├─ Quarterly labels (Q1, Q2, Q3, Q4)
├─ Grid: None

Y-Axis:
├─ "Rate (%)"
├─ Range: 0-12%

Annotations:
├─ Horizontal dashed line at 3.25%
├─ Label: "Expected difference"
├─ Highlight if difference deviates > 0.5%

Interaction:
└─ Hover: Show exact values & difference
```

---

## Dashboard 3: Inflation Analysis

**Purpose:** Connect rates to inflation outcomes  
**Chart Count:** 4

### Chart 3.1: Dual-Axis Chart - Fed Rate Impact on CPI (Main)

```
Type:               Dual-Axis Line Chart
Data Source:        fed_funds_rate (lagged), cpi_headline
Time Period:        Last 12 months
Dimensions:         Date (X), Fed Rate % (Left Y), CPI % (Right Y)

Layout:
├─ Position: Full width, top half
├─ Width: 100%
├─ Height: 300px

Metrics:
├─ Fed Funds Rate: Shown at current date (blue, left axis)
├─ CPI: Shown with 2-3 month lag (red, right axis)
│  └─ "Shifted back to show policy lag effect"

Visual:
├─ Fed Rate line: Blue (#1F77B4), 2px, solid
├─ CPI line: Red (#D62728), 2px, solid
├─ Grid: Subtle horizontal lines

Title:
├─ "Monetary Policy Lag: Fed Rate Impact on Inflation"
├─ Subtitle: "CPI lagged 2-3 months to show policy transmission"

Left Y-Axis:
├─ Label: "Fed Funds Rate (%)" - blue color
├─ Range: 0-8%

Right Y-Axis:
├─ Label: "Inflation (CPI % YoY)" - red color
├─ Range: 0-5%

Annotations:
├─ Vertical lines marking major Fed rate changes
├─ Labels: "Rate hike cycle begins", "Pauses", "Rate cuts"
├─ Shaded region: "Peak inflation period"

Legend:
├─ Fed Funds Rate (blue)
├─ Inflation (red, lagged 2-3 months)

Interaction:
├─ Hover: "Jan 15, 2025 | Fed Rate: 4.50% | CPI (Mar 2025): 3.42%"
├─ Zoom: Date range selection
└─ Annotation click: Show context on Fed decisions

Insight Box:
└─ "Fed rate increases take 12-18 months to fully impact inflation"
```

### Chart 3.2: Line Chart - Headline vs Core CPI

```
Type:               Multi-Line Chart
Data Source:        cpi_headline, cpi_core
Time Period:        Last 12 months

Layout:
├─ Position: Top-right
├─ Width: 48%
├─ Height: 250px

Metrics:
├─ Headline CPI (red, solid)
├─ Core CPI (orange, dashed, to show it's without food/energy)

Visual:
├─ Clear line distinction (solid vs dashed)
├─ Grid: Subtle

Title:
├─ "Inflation Components"
├─ "Headline vs Core CPI"

Story:
├─ Headline: All items (volatile due to energy)
├─ Core: Excludes food & energy (more stable)

Interaction:
└─ Hover: Show difference between headline & core
```

### Chart 3.3: Bar Chart - Monthly CPI Changes

```
Type:               Bar Chart
Data Source:        cpi_monthly_change
Time Period:        Last 12 months (12 bars, monthly)

Layout:
├─ Position: Bottom-left
├─ Width: 48%
├─ Height: 250px

Visual:
├─ Bars: Each month's MoM change
├─ Color: Green if < 0.2%, Yellow if 0.2%-0.5%, Red if > 0.5%
├─ Width: 20px, spacing: 3px

Title:
├─ "Month-over-Month CPI Changes"

X-Axis:
├─ Monthly labels (Sep, Oct, Nov...)

Y-Axis:
├─ "Monthly Change (%)"
├─ Range: -0.5% to +1.0%

Annotations:
├─ Horizontal reference line at 0.4% (high)
├─ Label: "Elevated monthly inflation"

Interaction:
└─ Hover: "Oct 2024: +0.32% MoM"
```

### Chart 3.4: Line Chart - YoY Inflation Trend

```
Type:               Line Chart with Area
Data Source:        cpi_yoy_change
Time Period:        Last 12 months

Layout:
├─ Position: Bottom-right
├─ Width: 48%
├─ Height: 250px

Visual:
├─ Area: Light red (#FFB6C1), 50% opacity
├─ Line: Red (#D62728), 2px
├─ Target line: Horizontal dashed at 2% (Fed target)

Title:
├─ "Year-over-Year Inflation Trend"
├─ Subtitle: "Progress toward Fed's 2% target"

Y-Axis:
├─ Label: "YoY Change (%)"
├─ Range: 0-5%

Annotations:
├─ Red zone: > 3.5% (high inflation)
├─ Yellow zone: 2.5%-3.5% (above target but moderating)
├─ Green zone: < 2.5% (near target)

Status Indicator:
├─ Current: "3.42% (Moderating ↓)"
├─ Color: Yellow (above target)

Interaction:
└─ Hover: Show exact monthly rates
```

---

## Dashboard 4: Correlations

**Purpose:** Show market relationships  
**Chart Count:** 3

### Chart 4.1: Correlation Heatmap (Main)

```
Type:               Heatmap
Data Source:        Correlation matrix of all 15 metrics
Dimensions:         15 × 15 matrix (all metrics)

Layout:
├─ Position: Center, large
├─ Width: 100%
├─ Height: 400px

Metrics Included (15 total):
├─ Fed Funds Rate, SOFR, Repo Rate
├─ Treasury 2Y, 5Y, 10Y
├─ CPI, Inflation Expectation
├─ Gold Price, Dollar Index, VIX
├─ Credit Spreads, Unemployment
├─ M2 Money Supply
└─ Yield Curve Spread

Visual:
├─ Color scale: Red (-1.0) → White (0.0) → Green (+1.0)
├─ Cell size: 40×40px (readable)
├─ Cell borders: 1px light gray
├─ Values: Correlation coefficient displayed (2 decimals)
├─ Font: 11px bold, dark text

Title:
├─ "Correlation Matrix: All Financial Metrics"
├─ Subtitle: "Green = moves together, Red = moves opposite"

Interaction:
├─ Hover over cell: Highlight row & column
├─ Show: "Fed Funds ↔ Gold: -0.65 (strong negative)"
├─ Click cell: Show scatter plot of those two variables
└─ Zoom: Allow matrix zoom for legibility

Legend:
├─ Position: Right side
├─ Scale: -1.0 (Red) → 0.0 (White) → +1.0 (Green)
├─ Label: "Pearson Correlation Coefficient"

Insight Box:
├─ "Strong correlations (>0.7 or <-0.7):"
├─ "- Interest rates move together (0.95)"
├─ "- Gold inversely with real yields (-0.68)"
└─ "- Credit spreads with unemployment (0.72)"
```

### Chart 4.2: Scatter Plot - Interest Rates vs Inflation

```
Type:               Scatter Plot with Trend Line
Data Source:        fed_funds_rate, cpi
Time Period:        Last 12 months (12 points, 1 per month)

Layout:
├─ Position: Bottom-left
├─ Width: 48%
├─ Height: 250px

Visual:
├─ Points: 6px, blue (#1F77B4), 70% opacity
├─ Trend line: 2px, slightly darker blue, dashed
├─ Grid: Light, subtle

Title:
├─ "Relationship: Fed Rate vs Inflation"

X-Axis:
├─ Label: "Fed Funds Rate (%)"
├─ Range: 4.0-5.0%

Y-Axis:
├─ Label: "CPI Inflation (%)"
├─ Range: 2.5-4.0%

Quadrants:
├─ Upper-right: High rates, high inflation (policy lag)
├─ Lower-left: Low rates, low inflation (target achieved)

Statistics:
├─ Correlation coefficient: Shown
├─ R-squared: Shown (fit quality)
├─ Interpretation: "Positive relationship: rates raised to combat inflation"

Interaction:
└─ Hover over point: Show date & both values
```

### Chart 4.3: Scatter Plot - Interest Rates vs Gold

```
Type:               Scatter Plot with Trend Line
Data Source:        fed_funds_rate, gold_price
Time Period:        Last 12 months

Layout:
├─ Position: Bottom-right
├─ Width: 48%
├─ Height: 250px

Visual:
├─ Points: 6px, gold (#FFD700), 70% opacity
├─ Trend line: 2px, darker gold, dashed
├─ Grid: Light

Title:
├─ "Relationship: Interest Rates vs Gold Price"

X-Axis:
├─ Label: "Fed Funds Rate (%)"

Y-Axis:
├─ Label: "Gold Price (USD/oz)"
├─ Range: $2,200-$2,600

Story:
├─ "Gold historically inversely related to real rates"
├─ "Higher rates = lower gold prices (opportunity cost)"

Statistics:
├─ Correlation: Strong negative (-0.68)
├─ Interpretation: "When rates rise, gold becomes less attractive"

Interaction:
└─ Hover: Show date & both values
```

---

## Dashboard 5: Real Yields & Asset Prices

**Purpose:** Investor perspective  
**Chart Count:** 4

### Chart 5.1: Multi-Line Chart - Real vs Nominal Yields

```
Type:               Multi-Line Chart
Data Source:        treasury_10y, cpi, calculated_real_yield
Time Period:        Last 12 months

Layout:
├─ Position: Top half, full width
├─ Width: 100%
├─ Height: 300px

Metrics:
├─ Nominal 10Y Yield (blue, solid, 2px)
├─ Inflation (CPI) (red, dashed, 2px)
├─ Real Yield = Nominal - Inflation (green, solid, 2px)

Title:
├─ "Real Yields Drive Investment Decisions"
├─ Subtitle: "What investors actually earn after inflation"

Y-Axis:
├─ Label: "Yield / Rate (%)"
├─ Range: -2% to +6%

Color Zones:
├─ Red zone: Real yields < 0 (negative, investors losing purchasing power)
├─ Yellow zone: Real yields 0-1%
├─ Green zone: Real yields > 1% (attractive)

Annotations:
├─ Highlight periods of negative real yields
├─ Label: "Negative real rates - inflation > yields"

Key Insight:
├─ "Real yields turned positive in late 2024"
├─ "Attracting capital back to bonds"

Interaction:
├─ Hover: Show all three values
├─ Toggle: Show/hide individual lines
└─ Insight: "Current real yield: +1.12% (attractive)"
```

### Chart 5.2: Dual-Axis Chart - Gold Prices vs Real Yields

```
Type:               Dual-Axis Line Chart
Data Source:        gold_price, real_yield
Time Period:        Last 12 months
Dimensions:         Date (X), Price (Left Y), Yield (Right Y)

Layout:
├─ Position: Top-right
├─ Width: 48%
├─ Height: 250px

Visual:
├─ Gold line: Gold (#FFD700), 2px (Left axis)
├─ Real yield: Green (#2CA02C), 2px (Right axis)
├─ Story: "Inverse relationship"

Title:
├─ "Gold as Inflation Hedge"
├─ "Inverse to Real Yields"

Left Y-Axis:
├─ Label: "Gold Price (USD/oz)"
├─ Range: $2,200-$2,600

Right Y-Axis:
├─ Label: "Real Yield (%)"
├─ Range: -2% to +3%

Insight:
├─ "When real yields rise, gold loses appeal"
├─ "When real yields fall, gold rises"

Interaction:
└─ Hover: "Sept 1, 2025 | Gold: $2,450/oz | Real Yield: +1.05%"
```

### Chart 5.3: Line Chart - Equity Index vs Interest Rates

```
Type:               Dual-Axis Line Chart
Data Source:        sp500_returns (or normalized index), fed_funds_rate
Time Period:        Last 12 months

Layout:
├─ Position: Bottom-left
├─ Width: 48%
├─ Height: 250px

Visual:
├─ S&P 500: Dark blue (#1F77B4), left axis
├─ Fed Rate: Red (#D62728), right axis

Title:
├─ "Equities Sensitive to Interest Rates"

Left Y-Axis:
├─ Label: "S&P 500 (Indexed to 100)"
├─ Range: 90-110

Right Y-Axis:
├─ Label: "Fed Funds Rate (%)"

Story:
├─ "Higher rates → lower equity valuations"
├─ "Inversely correlated"

Interaction:
└─ Hover: Show both index and rate
```

### Chart 5.4: KPI Cards - Real Yield Status

```
Type:               KPI Cards (3 cards)
Data Source:        real_yields (2Y, 5Y, 10Y)

Layout:
├─ Position: Bottom, three cards
├─ Width: 30% each
├─ Height: 100px

Cards:
├─ Real Yield (2Y): Calculated value, color-coded
├─ Real Yield (5Y): Calculated value
├─ Real Yield (10Y): Calculated value

Visual:
├─ Large number: 28px bold
├─ Label: "Real 10Y Yield"
├─ Color: Green if > 1%, Yellow if 0-1%, Red if < 0

Current Values:
├─ 2Y: +0.45%
├─ 5Y: +0.78%
├─ 10Y: +1.12%

Interpretation:
├─ "Positive across curve"
├─ "Attractive for investors"
├─ "Supports bond buying"

Interaction:
└─ Click: Show calculation (10Y Yield - CPI)
```

---

## Dashboard 6: Year-over-Year Comparisons

**Purpose:** Historical change narrative  
**Chart Count:** 4

### Chart 6.1: Bar Chart - YoY Rate Comparisons

```
Type:               Grouped Bar Chart
Data Source:        fed_funds_rate, repo_rate, prime_rate (current vs 1 year ago)
Time Period:        Current month vs same month last year

Layout:
├─ Position: Top half, full width
├─ Width: 100%
├─ Height: 280px

Metrics Shown (3 groups):
├─ Fed Funds Rate: 1 year ago (blue, lighter)
├─ Fed Funds Rate: Current (blue, darker)
├─ Similar for Repo & Prime rates

Visual:
├─ Grouped bars: 3 metrics, 2 bars each
├─ Colors: Light & dark shades
├─ Width: 25px bars, 8px spacing
├─ Data labels on bars

Title:
├─ "Year-over-Year Rate Changes"
├─ "Sept 2024 vs Sept 2025"

Y-Axis:
├─ Label: "Rate (%)"
├─ Range: 0-10%

X-Axis:
├─ Categories: "Fed Funds", "Repo Rate", "Prime Rate"

Statistics:
├─ Show % change for each
├─ "Fed Funds: No change (4.50% → 4.50%)"
├─ "Repo: -0.15% (down)"
├─ "Prime: No change (8.00%)"

Interaction:
└─ Hover: Show exact current & prior year values
```

### Chart 6.2: Bar Chart - YoY Inflation & Employment

```
Type:               Grouped Bar Chart
Data Source:        cpi, unemployment_rate (current vs 1 year ago)

Layout:
├─ Position: Top-right
├─ Width: 48%
├─ Height: 250px

Metrics:
├─ CPI (inflation): Current vs 1 year ago
├─ Unemployment: Current vs 1 year ago

Visual:
├─ CPI bars: Red shades
├─ Unemployment bars: Orange shades
├─ Clear comparison

Title:
├─ "Economic Progress: Inflation & Jobs"

Changes:
├─ Inflation: 4.15% (Sep 2024) → 3.42% (Sep 2025) = ↓0.73%
├─ Unemployment: 3.8% → 4.0% = ↑0.2%
├─ Story: "Inflation down, slight job market softening"

Interaction:
└─ Hover: Show exact values
```

### Chart 6.3: Bar Chart - Treasury Yields YoY

```
Type:               Grouped Bar Chart
Data Source:        treasury_2y, treasury_5y, treasury_10y (current vs 1 year ago)

Layout:
├─ Position: Bottom-left
├─ Width: 48%
├─ Height: 250px

Metrics:
├─ 2Y Treasury (light green)
├─ 5Y Treasury (medium green)
├─ 10Y Treasury (dark green)

Title:
├─ "Treasury Yield Curve Changes"

Story:
├─ Steeper? Flatter? Same?
├─ Implications for economy

Interaction:
└─ Hover: Show change in basis points
```

### Chart 6.4: Waterfall Chart - Fed Rate Changes This Year

```
Type:               Waterfall Chart
Data Source:        Individual Fed rate decisions (hikes/cuts)
Time Period:        Sept 2024 - Sept 2025

Layout:
├─ Position: Bottom-right
├─ Width: 48%
├─ Height: 250px

Visual:
├─ Starting point: "Sept 2024: 5.00%"
├─ Each change: Green bar (cut) or Red bar (hike)
├─ Connectors: Gray dashed lines
├─ Ending point: "Sept 2025: 4.50%"

Title:
├─ "Fed Rate Movement Timeline"
├─ "How we got from 5.00% to 4.50%"

Example Waterfall:
├─ Start: 5.00%
├─ December cut: -0.25% → 4.75%
├─ March cut: -0.25% → 4.50%
├─ End: 4.50%
├─ Net change: -0.50% (5 rate cuts total in year)

X-Axis:
├─ Dates of FOMC decisions

Y-Axis:
├─ "Rate (%)"

Labels:
├─ Each bar labeled with meeting date
├─ Amount of change

Insight:
├─ "Total: 5 cuts (-0.50%)"
├─ "Strategy: Pausing inflation fight, supporting growth"

Interaction:
└─ Hover: "March 19, 2025 | Rate Cut: -0.25%"
```

---

## Dashboard 7: Recession Signals

**Purpose:** Risk indicators  
**Chart Count:** 4

### Chart 7.1: Yield Curve Spread Line Chart (Main)

```
Type:               Line Chart with Threshold
Data Source:        yield_curve_spread (10Y - 2Y)
Time Period:        Last 12 months

Layout:
├─ Position: Top half, full width
├─ Width: 100%
├─ Height: 280px

Visual:
├─ Main line: Blue (#1F77B4), 3px (thick for importance)
├─ Zero line: Red (#D62728), dashed (recession threshold)
├─ Grid: Subtle gray
├─ Area above zero: Light green fill
├─ Area below zero: Light red fill

Title:
├─ "RECESSION SIGNAL: Yield Curve Inversion"
├─ Subtitle: "When 10Y yields drop below 2Y, recession usually follows"

Y-Axis:
├─ Label: "Spread (10Y - 2Y) in %"
├─ Range: -1% to +3%

Key Threshold:
├─ Zero line: Red dashed
├─ > 0.5%: Green zone (normal)
├─ 0% to +0.5%: Yellow zone (flattening)
├─ < 0%: Red zone (INVERTED - recession risk!)

Current Status:
├─ "Current spread: +0.85%"
├─ "Status: Normal ✓"
├─ "Recession probability: LOW"

Historical Context:
├─ Mark previous inversions (if any in past 12 months)
├─ Show: "Previous inversion in March 2022"
├─ Note: "Recession followed in 2023"

Interaction:
├─ Hover: Show exact spread on that date
├─ Click on inversion: Show forward returns (how long until recession)
└─ Annotation: "Data leads recession by 6-12 months on average"
```

### Chart 7.2: VIX (Volatility Index) Line Chart

```
Type:               Line Chart with Zones
Data Source:        vix
Time Period:        Last 12 months

Layout:
├─ Position: Top-right
├─ Width: 48%
├─ Height: 250px

Visual:
├─ Line: Red (#D62728), 2px
├─ Area: Light red fill, 50% opacity
├─ Grid: Subtle

Title:
├─ "VIX: Market Fear Gauge"
├─ Subtitle: "Volatility of S&P 500 implied by options"

Y-Axis:
├─ Label: "VIX Level"
├─ Range: 10-50

Zones:
├─ Green zone: 10-20 (Low volatility, calm)
├─ Yellow zone: 20-30 (Elevated volatility)
├─ Red zone: 30+ (High fear, market stress)

Current Level:
├─ "Current: 18.5"
├─ "Status: Low volatility ✓"
├─ "Investor sentiment: Calm"

Interpretation:
├─ "Elevated VIX = market expects turbulence"
├─ "Low VIX = confidence, but complacency risk"

Interaction:
└─ Hover: Show VIX level & market fear intensity
```

### Chart 7.3: Line Chart - Credit Spreads (HY OAS)

```
Type:               Line Chart with Threshold
Data Source:        high_yield_oas (Option-Adjusted Spread)
Time Period:        Last 12 months

Layout:
├─ Position: Bottom-left
├─ Width: 48%
├─ Height: 250px

Visual:
├─ Line: Orange (#FF7F0E), 2px
├─ Normal range: 300-400 bps (green zone)
├─ Stress range: 400-600 bps (yellow)
├─ Crisis range: 600+ bps (red)

Title:
├─ "Corporate Stress: High Yield Spreads"
├─ Subtitle: "Risk premium demanded by credit investors"

Y-Axis:
├─ Label: "OAS (basis points)"
├─ Range: 200-1000

Threshold Lines:
├─ 300 bps: Normal (dashed green)
├─ 500 bps: Elevated (dashed orange)
├─ 700 bps: Crisis (dashed red)

Current:
├─ "Current: 350 bps"
├─ "Status: Normal ✓"
├─ "Corporate fundamentals: Healthy"

Story:
├─ "Widening spreads = companies struggling to refinance"
├─ "Credit stress can trigger broader market downturn"

Interaction:
└─ Hover: Show OAS level & interpretation
```

### Chart 7.4: Line Chart - Jobless Claims Trend

```
Type:               Area Chart
Data Source:        initial_jobless_claims_weekly
Time Period:        Last 12 months

Layout:
├─ Position: Bottom-right
├─ Width: 48%
├─ Height: 250px

Visual:
├─ Area: Light blue fill
├─ Line: Blue (#1F77B4), 2px
├─ Smooth trend line: Dark blue, dashed

Title:
├─ "Labor Market Health: Initial Jobless Claims"
├─ Subtitle: "Rising claims signal economic stress"

Y-Axis:
├─ Label: "Weekly Claims (thousands)"
├─ Range: 150-500k

Zones:
├─ Green: < 250k (healthy labor market)
├─ Yellow: 250-350k (weakening)
├─ Red: > 350k (significant stress)

Current:
├─ "Latest: 210k claims"
├─ "Trend: Stable"
├─ "Labor market: Holding up"

Recession Signal:
├─ "Sharp spike in claims often precedes recession"
├─ "Watch for trend breaks"

Interaction:
└─ Hover: Show weekly claims
```

---

## Dashboard 8: Consumer Impact

**Purpose:** Everyday effects  
**Chart Count:** 4

### Chart 8.1: Mortgage Rates Line Chart

```
Type:               Line Chart
Data Source:        mortgage_30yr
Time Period:        Last 12 months

Layout:
├─ Position: Top half, full width
├─ Width: 100%
├─ Height: 280px

Visual:
├─ Line: Orange (#FF7F0E), 3px (important for consumers)
├─ Area: Light orange fill
├─ Grid: Subtle

Title:
├─ "Home Affordability: 30-Year Mortgage Rates"
├─ Subtitle: "How borrowing costs impact housing market"

Y-Axis:
├─ Label: "Mortgage Rate (%)"
├─ Range: 6.0-8.0%

Zones:
├─ Green zone: < 6.5% (more affordable)
├─ Yellow zone: 6.5-7.5% (moderate)
├─ Red zone: > 7.5% (expensive)

Current:
├─ "Current: 6.85%"
├─ "Status: Moderate affordability"

Context:
├─ "Followed Fed rate hikes with lag"
├─ "Monthly payment example:"
├─ "  $300k home @ 6.85% = $1,987/month (principal+interest)"
├─ "  Same home @ 7.50% = $2,100/month (+$113)"

Comparison:
├─ "1 year ago: 7.15%"
├─ "Change: -0.30% (slight improvement)"

Interaction:
└─ Hover: Show rate & estimated monthly payment
```

### Chart 8.2: Dual-Axis - Fed Rate vs Mortgage Rates

```
Type:               Dual-Axis Line Chart
Data Source:        fed_funds_rate, mortgage_30yr
Time Period:        Last 12 months

Layout:
├─ Position: Top-right
├─ Width: 48%
├─ Height: 250px

Visual:
├─ Fed Rate: Blue, left axis
├─ Mortgage: Orange, right axis
├─ Lines aligned to show lag

Title:
├─ "Policy to Consumer: Rate Transmission"

Story:
├─ "Fed rate changes take 2-6 months to reach mortgages"
├─ "Commercial rates slower to change than Fed rate"

Interaction:
└─ Hover: Show both rates on same date
```

### Chart 8.3: Bar Chart - Unemployment by Sector

```
Type:               Bar Chart
Data Source:        unemployment_by_sector (if available)
Time Period:        Current month

Layout:
├─ Position: Bottom-left
├─ Width: 48%
├─ Height: 250px

Sectors:
├─ Overall unemployment
├─ Tech sector
├─ Finance
├─ Manufacturing
├─ Services
├─ Construction

Visual:
├─ Colors: Different shade per sector
├─ Sorted: Highest to lowest

Title:
├─ "Job Market by Sector"
├─ "Where are jobs being lost/gained?"

Current:
├─ Overall: 4.0%
├─ Tech: 3.2% (strong)
├─ Finance: 4.5% (weaker)
├─ Services: 4.2%

Interpretation:
├─ "Some sectors resilient, others weakening"
├─ "Signals uneven economic health"

Interaction:
└─ Hover: Show exact rate per sector
```

### Chart 8.4: KPI Cards - Cost of Living Impact

```
Type:               KPI Cards (3 cards)
Data Source:        Calculated from inflation data

Layout:
├─ Position: Bottom-right
├─ Width: 48%
├─ Height: 100px (3 cards stacked)

Card 1: Real Wage Growth
├─ Calculation: Wage growth rate - inflation rate
├─ Value: "-0.8%"
├─ Interpretation: "Wages losing purchasing power"
├─ Color: Red (warning)

Card 2: Annual Cost Increase
├─ Example: 3.42% inflation on $60k salary
├─ Annual increase needed: $2,052
├─ Value: "+$2,052/year"
├─ Color: Orange (caution)

Card 3: Cumulative 12-Month Cost
├─ Total cumulative inflation over past 12 months
├─ Value: "+3.42% from 12 months ago"
├─ Equivalent: "$2,052 more per $60k earned"

Title:
├─ "Real Impact on Your Wallet"

Narrative:
├─ "Despite moderating inflation, real wages still pressured"
├─ "Workers need wage increases to maintain purchasing power"
```

---

## Summary Table: All Charts

| Dashboard | Chart # | Type | Key Data | Focus |
|-----------|---------|------|----------|-------|
| 1 | 1.1-1.4 | KPI Cards | 4 key metrics | Current snapshot |
| 1 | 1.5 | Dual-Axis | Fed vs CPI | Policy vs outcome |
| 1 | 1.6-1.7 | Gauges | Spreads, risk | Status indicators |
| 2 | 2.1 | Multi-line | 4 rates | Rate transmission |
| 2 | 2.2 | Multi-line | Treasury yields | Curve shape |
| 2 | 2.3 | Area | Fed-Repo spread | Funding health |
| 2 | 2.4 | Bar | Prime vs Fed | Rate alignment |
| 3 | 3.1 | Dual-Axis | Fed (lagged) vs CPI | Policy lag |
| 3 | 3.2 | Multi-line | Headline vs Core | Inflation components |
| 3 | 3.3 | Bar | Monthly CPI | Monthly changes |
| 3 | 3.4 | Area | YoY inflation | Trend to target |
| 4 | 4.1 | Heatmap | 15×15 correlation | All relationships |
| 4 | 4.2 | Scatter | Rates vs inflation | Policy effectiveness |
| 4 | 4.3 | Scatter | Rates vs gold | Asset correlations |
| 5 | 5.1 | Multi-line | Nominal, inflation, real | Real returns |
| 5 | 5.2 | Dual-Axis | Gold vs real yields | Inverse relationship |
| 5 | 5.3 | Dual-Axis | Equities vs rates | Market sensitivity |
| 5 | 5.4 | KPI Cards | Real yields (2Y/5Y/10Y) | Attractiveness |
| 6 | 6.1 | Grouped bars | YoY rates | Rate comparison |
| 6 | 6.2 | Grouped bars | YoY inflation/jobs | Economic progress |
| 6 | 6.3 | Grouped bars | YoY Treasury yields | Curve changes |
| 6 | 6.4 | Waterfall | Fed rate decisions | Decision sequence |
| 7 | 7.1 | Line+threshold | Yield curve spread | Recession risk |
| 7 | 7.2 | Area | VIX | Market fear |
| 7 | 7.3 | Line+zones | Credit spreads | Corporate stress |
| 7 | 7.4 | Area | Jobless claims | Labor market |
| 8 | 8.1 | Line | Mortgage rates | Housing affordability |
| 8 | 8.2 | Dual-Axis | Fed rate vs mortgages | Rate transmission to consumer |
| 8 | 8.3 | Bar | Unemployment by sector | Sector strength |
| 8 | 8.4 | KPI Cards | Real wages, costs | Wallet impact |

**Total: 30 distinct charts across 8 dashboards**

---

**Reference Document:** Use this while building each dashboard in Tableau  
**Last Updated:** Sept 15, 2026
