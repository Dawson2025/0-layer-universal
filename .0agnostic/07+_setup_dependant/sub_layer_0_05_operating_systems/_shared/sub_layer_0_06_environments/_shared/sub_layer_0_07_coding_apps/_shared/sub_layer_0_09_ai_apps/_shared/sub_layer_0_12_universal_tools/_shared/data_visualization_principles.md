---
resource_id: "61b5a128-52f0-44f9-b754-75d123e84739"
resource_type: "document"
resource_name: "data_visualization_principles"
---
# Data Visualization and Analysis Principles

**Level**: Universal Tools (0.75)
**Applies To**: All data analysis and visualization work
**Last Updated**: November 13, 2025
**Derived From**: Unit 3 DS250 lessons learned

---

<!-- section_id: "37cd3b9a-254b-494f-aa58-0f417be4fa44" -->
## Purpose

This document establishes universal principles for data visualization, data cleaning, and analysis consistency that apply across all projects involving data analysis and visualization.

**Key Lesson**: The order of operations in data preparation and the technical details of chart rendering significantly impact data quality and visual accuracy.

---

<!-- section_id: "b9d94c0b-1a9c-4a29-9988-6139d7a213c7" -->
## 1. Data Cleaning Order of Operations

<!-- section_id: "f4c656a2-63f8-4c1b-8099-009bd744bca9" -->
### The Golden Rule

**ALWAYS clean data BEFORE performing calculations on it.**

<!-- section_id: "53fbfac7-16d4-4c46-9db9-7808a0e884f0" -->
### Standard Sequence

Follow this order for all data cleaning tasks:

```
1. Replace sentinel values (-999, -1, 999, etc.) → NaN
2. Handle missing value indicators ("n/a", "N/A", "", blanks, "NA") → NaN
3. Fix typos and standardization (e.g., "Febuary" → "February")
4. Convert data types (strings → numeric, dates → datetime)
5. Fill missing values (mean, median, mode, forward-fill, backward-fill)
6. ONLY THEN: Perform calculations (multiplications, divisions, derived columns)
```

<!-- section_id: "9fa971ca-b24a-4fa0-80d3-b3cc4a3c9b43" -->
### Why Order Matters

**Bad Example** (calculation before cleaning):
```python
# ❌ WRONG
df['derived'] = df['value'] * 0.30  # If value = -999, result = -299.7!
df['value'] = df['value'].replace(-999, np.nan)  # Too late!
```

**Good Example** (clean then calculate):
```python
# ✅ CORRECT
df['value'] = df['value'].replace(-999, np.nan)
df['value'] = df['value'].fillna(df['value'].mean())
df['derived'] = df['value'] * 0.30  # Now using clean data
```

<!-- section_id: "719f0df2-1737-4eb0-8233-f91ede00639c" -->
### Red Flags to Watch For

- Unexpected negative values in results
- Values in the range of sentinel values (e.g., -299.7 ≈ -999 × 0.3)
- NaN appearing after calculations instead of before
- Results that don't make logical sense (negative percentages, etc.)

---

<!-- section_id: "3e1e18d5-741d-442a-ab58-07894dbfa396" -->
## 2. Chart Rendering Best Practices

<!-- section_id: "448536f3-b12f-4105-99dd-7c0535b72297" -->
### Pre-calculated Values in Bar Charts

When using visualization libraries with bar charts and pre-calculated values:

**Problem**: Default behavior often counts occurrences rather than using actual values.

**Solution**: Explicitly specify to use the actual values.

#### lets-plot (Python)

```python
# ❌ WRONG: Will count occurrences, not use values
ggplot(data) + geom_bar(aes(x="category", y="percentage"))

# ✅ CORRECT: Use actual values with stat="identity"
ggplot(data) + geom_bar(
    aes(x="category", y="percentage"),
    stat="identity"  # Use the actual y values
) + ylim(0, 100)  # Set explicit range for percentages
```

#### ggplot2 (R)

```r
# ✅ CORRECT
ggplot(data, aes(x=category, y=percentage)) +
  geom_bar(stat="identity") +
  ylim(0, 100)
```

<!-- section_id: "777c81e8-7118-4c39-b13f-2b776203a847" -->
### Percentage Data Display

**Best Practice**: Create both decimal and percentage versions of percentage columns.

```python
df = df.assign(
    rate_decimal=lambda d: d['count'] / d['total'],      # 0.0 to 1.0
    rate_percent=lambda d: d['count'] / d['total'] * 100 # 0 to 100
)

# For tables: use decimal with percentage formatting
df.style.format({"rate_decimal": "{:.1%}"})  # Shows as "67.0%"

# For charts: use percent with explicit limits
ggplot(...) + geom_bar(aes(y="rate_percent"), stat="identity") + ylim(0, 100)
```

**Why Both**:
- Decimal (0-1): Better for formatted table display
- Percent (0-100): Better for explicit chart axis control

<!-- section_id: "df6f17ff-245d-428f-8f46-0c3cecb8aa1f" -->
### Chart Verification Checklist

Before publishing any visualization:

- [ ] Chart scale makes sense (0-3 for percentages = BUG)
- [ ] Pre-calculated values use `stat="identity"` (or equivalent)
- [ ] Percentage charts have explicit y-limits (0-100)
- [ ] Axis labels are clear and include units
- [ ] Legend is present and understandable
- [ ] Colors are distinguishable and accessible

---

<!-- section_id: "dc0ed626-4c9d-4784-b4bb-67fa0b8f0985" -->
## 3. Analysis-Visual Consistency

<!-- section_id: "23ffdb3e-758c-47ce-861d-c36b75b9163e" -->
### The Principle

**Written analysis must precisely match what visualizations show.**

<!-- section_id: "408d8dfb-04d4-48f6-aaed-bb2d60832388" -->
### Process

```
1. Clean data
2. Generate the visualization
3. Examine the actual sorted data values
4. Write analysis based on what you actually see
5. Include specific numbers/percentages from the data
6. Verify once more before publishing
```

<!-- section_id: "1faa4b8a-1178-4d31-8598-4a8186d47289" -->
### Common Mistakes

**Mistake 1**: Writing analysis before looking at the actual data.

```markdown
❌ WRONG: "April and October are the best months"
(Written without checking which months actually rank 2nd and 3rd)

✅ CORRECT: "November (16.7%) and October (18.1%) are the next-best options"
(Written after sorting data and seeing actual values)
```

**Mistake 2**: Assuming analysis from a draft is still accurate after data updates.

```
Data changes → Chart updates → Analysis becomes outdated
Solution: Always re-verify analysis after any data changes
```

**Mistake 3**: Not including specific values in the analysis.

```markdown
❌ VAGUE: "San Francisco has the highest delay rate"

✅ SPECIFIC: "San Francisco has the highest delay rate (26.1%),
              meaning more than one in four flights experiences a delay"
```

<!-- section_id: "1715b764-30de-4e8f-be0f-26c619f870de" -->
### Verification Steps

```python
# Step 1: Sort to see actual rankings
data.sort_values('metric').head(5)

# Step 2: Note specific values
# Top: A (26.1%), B (24.3%), C (22.1%)

# Step 3: Write analysis matching these exact values
# "A leads with 26.1%, followed by B (24.3%) and C (22.1%)"

# Step 4: Verify chart shows same ranking and values
```

---

<!-- section_id: "229f3dbd-3dc9-4f5a-b011-9320abc87291" -->
## 4. Metric Justification

<!-- section_id: "a4894e41-807e-4e0d-9f6e-fa69a18191fe" -->
### The Requirement

**Always explain WHY you chose a metric, not just WHAT it shows.**

<!-- section_id: "6ef0cdda-b199-47ca-91b6-5a610fd7d83c" -->
### Complete Justification Structure

```markdown
1. State the metric chosen (e.g., "delay rate" vs "total delays")
2. Explain why it's appropriate for the question
3. Explain why it's better than alternatives
4. Show how it helps answer the specific question
5. Present the results using that metric
```

<!-- section_id: "e4fe2aeb-0391-46ba-b35f-6bfc803e54d3" -->
### Example

**Incomplete** ❌:
```markdown
San Francisco has the worst delays with a 26.1% delay rate.
```

**Complete** ✅:
```markdown
To determine the "worst" airport, I chose **delay rate (proportion of
delayed flights)** as the primary metric because it represents a traveler's
probability of experiencing a delay regardless of airport size. An airport
with 100,000 flights and 30,000 delays (30% rate) is worse for travelers
than one with 50,000 flights and 10,000 delays (20% rate), even though the
second has fewer total delays. This proportion-based metric ensures fair
comparison across airports of different sizes.

San Francisco International (SFO) stands out as the most delay-prone airport
with the highest delay rate (26.1%), meaning more than one in four flights
experiences a delay.
```

<!-- section_id: "7fd7ac55-4b9b-4575-86e0-327d5522f724" -->
### Common Metrics and Their Use Cases

| Metric | When to Use | When NOT to Use |
|--------|-------------|-----------------|
| **Proportion/Rate** | Comparing entities of different sizes | When absolute counts matter more |
| **Total Count** | Understanding overall impact/volume | Comparing different-sized groups |
| **Average** | Understanding typical experience | When outliers are important |
| **Median** | Data with outliers/skewed distribution | When mean is more meaningful |

---

<!-- section_id: "25146a51-e35c-4555-a747-9c45c6615d57" -->
## 5. Sequential Development Impact

<!-- section_id: "8532dd00-6c25-45ab-88a3-da29d90f31d3" -->
### Connection to Data Quality

These visualization principles reinforce sequential workflow methodology:

**Sequential Approach**:
```
Task 1: Discover -999 must be cleaned BEFORE calculations
Task 2: Inherit correct cleaning order → No negative values
Task 3: Apply established pattern → Clean from start
```

**Parallel Approach** (problematic):
```
Task 1: ✅ Discover issue, fix it
Task 2: ❌ Doesn't have fix, duplicates bug
Task 3: ❌ Duplicates bug independently

Result: Must fix multiple tasks after the fact
```

**Principle**: Data cleaning discoveries in early tasks must propagate to all subsequent tasks. Sequential development ensures this happens naturally.

---

<!-- section_id: "792545d6-89b4-4382-9156-3a93718eb0a8" -->
## 6. Technology-Specific Notes

<!-- section_id: "c9dfa009-69fa-4ade-8b0e-3d46342e3725" -->
### Python (pandas + lets-plot)

```python
# Data cleaning
df['column'] = df['column'].replace(sentinel_value, np.nan)
df['column'] = df['column'].fillna(df['column'].mean())

# Visualization
from lets_plot import *
ggplot(df) + geom_bar(aes(x="cat", y="val"), stat="identity") + ylim(0, 100)
```

<!-- section_id: "22112b35-d6a6-41aa-9606-6a695ed46bf8" -->
### R (dplyr + ggplot2)

```r
# Data cleaning
df <- df %>%
  mutate(column = na_if(column, sentinel_value)) %>%
  mutate(column = replace_na(column, mean(column, na.rm=TRUE)))

# Visualization
ggplot(df, aes(x=cat, y=val)) +
  geom_bar(stat="identity") +
  ylim(0, 100)
```

<!-- section_id: "0050c3b2-451f-4174-91d9-ecd77ef95666" -->
### JavaScript (D3.js, Observable)

```javascript
// Pre-calculate and verify data structure
const data = rawData
  .filter(d => d.value !== -999)  // Remove sentinel
  .map(d => ({
    category: d.cat,
    percentage: d.count / d.total * 100
  }));

// Explicit scale for percentages
const yScale = d3.scaleLinear()
  .domain([0, 100])
  .range([height, 0]);
```

---

<!-- section_id: "4c71eb84-5484-48e7-ac8a-de1167ea1012" -->
## 7. Red Flags and Debugging

<!-- section_id: "9f4ea3a5-ba84-4d4f-bca8-ace1f1276612" -->
### Data Red Flags

- Negative values where they shouldn't exist
- Values suspiciously close to sentinel values (-299.7 ≈ -999 × 0.3)
- Percentages over 100% or under 0%
- Means/medians that don't make logical sense

<!-- section_id: "330e019a-f363-4480-9a68-cb37ee39eff5" -->
### Visualization Red Flags

- Chart scale doesn't match data range (0-3 for percentages)
- Bar heights don't visually match the data values
- Missing or incorrect axis labels/units
- Legend categories don't match the data

<!-- section_id: "f12d1758-9765-47e1-884b-c7e15ff068d4" -->
### Analysis Red Flags

- Analysis mentions values not in the top/bottom N of actual data
- Rankings in text don't match rankings in chart
- No specific numbers/percentages cited
- Metric choice not justified

---

<!-- section_id: "31d6574c-e10b-44f6-a7c6-4dcf3496b9d0" -->
## 8. Quality Checklist

Before publishing any data analysis with visualizations:

<!-- section_id: "9d1a28e1-b109-4ff4-9dd3-6a7c016e9be2" -->
### Data Quality
- [ ] All sentinel values cleaned BEFORE calculations
- [ ] All missing value indicators standardized
- [ ] Data types converted appropriately
- [ ] No unexpected negative values
- [ ] No values suspiciously near sentinel values

<!-- section_id: "2fb15152-acd0-4028-aca9-038002b6ca1b" -->
### Visualization Quality
- [ ] Charts with pre-calculated values use `stat="identity"` (or equivalent)
- [ ] Percentage charts have explicit 0-100 limits
- [ ] Chart scales make logical sense
- [ ] All axes labeled with units
- [ ] Legends present and clear

<!-- section_id: "c4aa7383-19a0-4adc-ac79-5741451b1f39" -->
### Analysis Quality
- [ ] Written analysis checked against actual sorted data
- [ ] Specific values/percentages cited in text
- [ ] Rankings in text match rankings in chart
- [ ] Metric choice explained (WHY not just WHAT)
- [ ] Analysis makes logical sense given the data

---

<!-- section_id: "fc880cbc-dc7a-48d3-baf4-8af6be18253e" -->
## 9. Case Study: Unit 3 DS250

This guidance originated from issues found in Unit 3 flight delay analysis:

**Issues Found**:
1. Negative values (-299.7) from calculating before cleaning -999
2. Chart scale 0-3 instead of 0-100% from missing `stat="identity"`
3. Analysis mentioned "April" when data showed "November"
4. Metric choice (delay rate) not justified

**Root Cause**: Parallel development + insufficient verification

**Resolution**:
- Fixed data cleaning order
- Added `stat="identity"` to charts
- Updated analysis to match actual data
- Added metric justifications
- Created this documentation

**Lesson**: These issues are preventable with proper process and checklists.

---

<!-- section_id: "95faa8ff-75f3-4353-bd56-ac7fbe757575" -->
## 10. Summary

**Core Principles**:

1. **Clean BEFORE Calculate** - Sentinel values must be removed before math
2. **stat="identity" for Pre-calculated Values** - Tell the library to use your values
3. **Analysis Matches Visuals** - Always verify text against actual sorted data
4. **Justify Metrics** - Explain WHY you chose a metric, not just WHAT it shows
5. **Sequential Development** - Lessons from early tasks propagate to later ones

**Remember**: These aren't just best practices—they're necessary for data quality and analytical credibility.

---

**Created**: November 13, 2025
**Source**: DS250 Unit 3 flight delay analysis lessons learned
**Status**: Active guidance for all data visualization work
**Related**: Sequential Workflow Guidelines, Data Quality Standards
