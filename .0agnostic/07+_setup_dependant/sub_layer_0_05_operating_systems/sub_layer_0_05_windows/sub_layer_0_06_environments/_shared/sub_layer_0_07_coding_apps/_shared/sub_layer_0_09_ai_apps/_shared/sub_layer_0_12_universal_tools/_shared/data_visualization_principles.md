---
resource_id: "2cc35b65-c719-4d81-8357-6a924039afdf"
resource_type: "document"
resource_name: "data_visualization_principles"
---
# Data Visualization and Analysis Principles

**Level**: Universal Tools (0.75)
**Applies To**: All data analysis and visualization work
**Last Updated**: November 13, 2025
**Derived From**: Unit 3 DS250 lessons learned

---

<!-- section_id: "bd7d9aab-03ff-442c-a079-d295a3b26efe" -->
## Purpose

This document establishes universal principles for data visualization, data cleaning, and analysis consistency that apply across all projects involving data analysis and visualization.

**Key Lesson**: The order of operations in data preparation and the technical details of chart rendering significantly impact data quality and visual accuracy.

---

<!-- section_id: "acb09bf9-0db9-4b03-b14f-9fb17a23418b" -->
## 1. Data Cleaning Order of Operations

<!-- section_id: "8d476500-87df-4448-8eaa-7074c1d89f07" -->
### The Golden Rule

**ALWAYS clean data BEFORE performing calculations on it.**

<!-- section_id: "ea0c3080-97dd-49c9-818d-503e5e58d61d" -->
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

<!-- section_id: "2061a7f8-bfd2-4b4e-b130-157d73b94eb3" -->
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

<!-- section_id: "92c82460-2a9a-4eec-9084-f916157c0f1e" -->
### Red Flags to Watch For

- Unexpected negative values in results
- Values in the range of sentinel values (e.g., -299.7 ≈ -999 × 0.3)
- NaN appearing after calculations instead of before
- Results that don't make logical sense (negative percentages, etc.)

---

<!-- section_id: "891e70ac-efa6-498c-9f8e-d1f46380c430" -->
## 2. Chart Rendering Best Practices

<!-- section_id: "84ad2698-9bae-41d1-beb5-86fae8a2acea" -->
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

<!-- section_id: "16daf359-4e25-4453-85f8-c37f822e30db" -->
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

<!-- section_id: "d18f6ac2-a08c-42df-bb20-dc630bb19ae5" -->
### Chart Verification Checklist

Before publishing any visualization:

- [ ] Chart scale makes sense (0-3 for percentages = BUG)
- [ ] Pre-calculated values use `stat="identity"` (or equivalent)
- [ ] Percentage charts have explicit y-limits (0-100)
- [ ] Axis labels are clear and include units
- [ ] Legend is present and understandable
- [ ] Colors are distinguishable and accessible

---

<!-- section_id: "baf45675-c6c9-44b6-b548-78d235cdcec8" -->
## 3. Analysis-Visual Consistency

<!-- section_id: "ed0d10cc-0cc7-446d-b8d9-1af71883da68" -->
### The Principle

**Written analysis must precisely match what visualizations show.**

<!-- section_id: "386a524c-ea9a-4fb1-ba32-d18dc5446c8b" -->
### Process

```
1. Clean data
2. Generate the visualization
3. Examine the actual sorted data values
4. Write analysis based on what you actually see
5. Include specific numbers/percentages from the data
6. Verify once more before publishing
```

<!-- section_id: "12916cb4-6bca-4c74-aa32-c720047b0961" -->
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

<!-- section_id: "299f4ae5-8f24-4d97-8181-789b3dcd40ce" -->
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

<!-- section_id: "6052e6f4-b9a1-4fcc-8242-d86fc813f4c4" -->
## 4. Metric Justification

<!-- section_id: "8611c2bb-e4cf-4808-815d-598585522f97" -->
### The Requirement

**Always explain WHY you chose a metric, not just WHAT it shows.**

<!-- section_id: "8b86213c-bd2e-494f-9dbb-be132e186226" -->
### Complete Justification Structure

```markdown
1. State the metric chosen (e.g., "delay rate" vs "total delays")
2. Explain why it's appropriate for the question
3. Explain why it's better than alternatives
4. Show how it helps answer the specific question
5. Present the results using that metric
```

<!-- section_id: "430a35f8-9449-4882-b609-3714e24c1892" -->
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

<!-- section_id: "c686616f-53aa-4eee-b4af-152064d9d47c" -->
### Common Metrics and Their Use Cases

| Metric | When to Use | When NOT to Use |
|--------|-------------|-----------------|
| **Proportion/Rate** | Comparing entities of different sizes | When absolute counts matter more |
| **Total Count** | Understanding overall impact/volume | Comparing different-sized groups |
| **Average** | Understanding typical experience | When outliers are important |
| **Median** | Data with outliers/skewed distribution | When mean is more meaningful |

---

<!-- section_id: "0242b595-d178-4f9d-842c-d3b3940b426a" -->
## 5. Sequential Development Impact

<!-- section_id: "87352ae4-a3dc-40df-97c5-7f515c7361b5" -->
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

<!-- section_id: "3bacec4a-51e6-4f0f-ab96-d926af1b33c8" -->
## 6. Technology-Specific Notes

<!-- section_id: "6bd5f849-dbb0-435b-9f9f-c34acc492bbb" -->
### Python (pandas + lets-plot)

```python
# Data cleaning
df['column'] = df['column'].replace(sentinel_value, np.nan)
df['column'] = df['column'].fillna(df['column'].mean())

# Visualization
from lets_plot import *
ggplot(df) + geom_bar(aes(x="cat", y="val"), stat="identity") + ylim(0, 100)
```

<!-- section_id: "39fb702c-ef21-4665-8be4-5c4ea421104e" -->
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

<!-- section_id: "11fb86ca-a1a2-4bec-8c1e-9185a493828b" -->
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

<!-- section_id: "435995c6-dc66-4865-8a39-87d2a2a8a3ef" -->
## 7. Red Flags and Debugging

<!-- section_id: "c0516fee-c2d3-4c09-951e-dd0fe7adf032" -->
### Data Red Flags

- Negative values where they shouldn't exist
- Values suspiciously close to sentinel values (-299.7 ≈ -999 × 0.3)
- Percentages over 100% or under 0%
- Means/medians that don't make logical sense

<!-- section_id: "797ee0e4-c3a3-4f3b-9523-21d3d7816319" -->
### Visualization Red Flags

- Chart scale doesn't match data range (0-3 for percentages)
- Bar heights don't visually match the data values
- Missing or incorrect axis labels/units
- Legend categories don't match the data

<!-- section_id: "41425148-d83b-40f4-9ed8-595ce2b87558" -->
### Analysis Red Flags

- Analysis mentions values not in the top/bottom N of actual data
- Rankings in text don't match rankings in chart
- No specific numbers/percentages cited
- Metric choice not justified

---

<!-- section_id: "682d6c04-6744-48b5-b83b-5a6356bd5d6b" -->
## 8. Quality Checklist

Before publishing any data analysis with visualizations:

<!-- section_id: "705bd3f0-d4e4-4e4d-898f-73f8a0efd979" -->
### Data Quality
- [ ] All sentinel values cleaned BEFORE calculations
- [ ] All missing value indicators standardized
- [ ] Data types converted appropriately
- [ ] No unexpected negative values
- [ ] No values suspiciously near sentinel values

<!-- section_id: "bb0aa4bf-f5f0-4006-9c38-d38cdfd3974c" -->
### Visualization Quality
- [ ] Charts with pre-calculated values use `stat="identity"` (or equivalent)
- [ ] Percentage charts have explicit 0-100 limits
- [ ] Chart scales make logical sense
- [ ] All axes labeled with units
- [ ] Legends present and clear

<!-- section_id: "e79b7ef0-49f3-4334-90a8-ff3da72c3132" -->
### Analysis Quality
- [ ] Written analysis checked against actual sorted data
- [ ] Specific values/percentages cited in text
- [ ] Rankings in text match rankings in chart
- [ ] Metric choice explained (WHY not just WHAT)
- [ ] Analysis makes logical sense given the data

---

<!-- section_id: "37184675-e25b-47f3-8395-654eaa2e15c9" -->
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

<!-- section_id: "933ec22c-d774-4d17-bfe1-c2c722734f97" -->
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
