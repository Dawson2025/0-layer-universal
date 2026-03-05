---
resource_id: "294ebc0c-1bcc-4f4f-ae50-43a515b7cfae"
resource_type: "document"
resource_name: "data_visualization_principles"
---
# Data Visualization and Analysis Principles

**Level**: Universal Tools (0.75)
**Applies To**: All data analysis and visualization work
**Last Updated**: November 13, 2025
**Derived From**: Unit 3 DS250 lessons learned

---

<!-- section_id: "909792c4-6e2f-4895-82ad-5d20c26815b9" -->
## Purpose

This document establishes universal principles for data visualization, data cleaning, and analysis consistency that apply across all projects involving data analysis and visualization.

**Key Lesson**: The order of operations in data preparation and the technical details of chart rendering significantly impact data quality and visual accuracy.

---

<!-- section_id: "b5fc5a56-982c-4b44-a5af-23303caa3838" -->
## 1. Data Cleaning Order of Operations

<!-- section_id: "784eb4ae-16a6-498d-9333-df5661b50a60" -->
### The Golden Rule

**ALWAYS clean data BEFORE performing calculations on it.**

<!-- section_id: "4aed9c36-2230-4b66-9bab-d2f993bb80ca" -->
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

<!-- section_id: "20417205-e885-49e5-b9e2-5068ffc30a9b" -->
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

<!-- section_id: "2e25f05a-3dfe-403e-8472-13aac2b062ba" -->
### Red Flags to Watch For

- Unexpected negative values in results
- Values in the range of sentinel values (e.g., -299.7 ≈ -999 × 0.3)
- NaN appearing after calculations instead of before
- Results that don't make logical sense (negative percentages, etc.)

---

<!-- section_id: "c2d5e01f-e3f2-4c9a-b3bc-5611614b43bb" -->
## 2. Chart Rendering Best Practices

<!-- section_id: "09b22044-9c84-4d6d-ae57-0297445e9341" -->
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

<!-- section_id: "31683605-728e-45de-826a-b87d50374b6f" -->
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

<!-- section_id: "6169457f-7a18-49f0-945b-cc6146381705" -->
### Chart Verification Checklist

Before publishing any visualization:

- [ ] Chart scale makes sense (0-3 for percentages = BUG)
- [ ] Pre-calculated values use `stat="identity"` (or equivalent)
- [ ] Percentage charts have explicit y-limits (0-100)
- [ ] Axis labels are clear and include units
- [ ] Legend is present and understandable
- [ ] Colors are distinguishable and accessible

---

<!-- section_id: "ab6cbf66-34cb-4e14-9844-26ab86b4499f" -->
## 3. Analysis-Visual Consistency

<!-- section_id: "0e893468-1921-4cd9-9898-c232176fb340" -->
### The Principle

**Written analysis must precisely match what visualizations show.**

<!-- section_id: "5d8859fc-02ff-4d58-9fb4-42c58300e0cf" -->
### Process

```
1. Clean data
2. Generate the visualization
3. Examine the actual sorted data values
4. Write analysis based on what you actually see
5. Include specific numbers/percentages from the data
6. Verify once more before publishing
```

<!-- section_id: "6a27036f-56bd-46ee-aa87-7f5b9312901a" -->
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

<!-- section_id: "6243a87e-b8f6-409d-98bb-24ab17c4ce9b" -->
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

<!-- section_id: "8ba72856-ddd2-4ff2-b7bc-47d495d0c07c" -->
## 4. Metric Justification

<!-- section_id: "4d9d67e4-96bb-4e5c-925c-8ab4965d56bc" -->
### The Requirement

**Always explain WHY you chose a metric, not just WHAT it shows.**

<!-- section_id: "dfe36991-62e3-4a9d-aa30-9a380f1b30c9" -->
### Complete Justification Structure

```markdown
1. State the metric chosen (e.g., "delay rate" vs "total delays")
2. Explain why it's appropriate for the question
3. Explain why it's better than alternatives
4. Show how it helps answer the specific question
5. Present the results using that metric
```

<!-- section_id: "31205c15-47ec-41f0-9101-1310e18ed05d" -->
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

<!-- section_id: "a328c830-1174-4096-a54e-6e2603372a0e" -->
### Common Metrics and Their Use Cases

| Metric | When to Use | When NOT to Use |
|--------|-------------|-----------------|
| **Proportion/Rate** | Comparing entities of different sizes | When absolute counts matter more |
| **Total Count** | Understanding overall impact/volume | Comparing different-sized groups |
| **Average** | Understanding typical experience | When outliers are important |
| **Median** | Data with outliers/skewed distribution | When mean is more meaningful |

---

<!-- section_id: "055722aa-869f-4bb2-ac4b-6b29a732f86a" -->
## 5. Sequential Development Impact

<!-- section_id: "974f9ad4-4c47-4d95-ac16-a781aca01224" -->
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

<!-- section_id: "8a416d67-1f3b-488a-bf84-d4563ec5164e" -->
## 6. Technology-Specific Notes

<!-- section_id: "659a91bd-627f-4603-983c-8ea98ff44a30" -->
### Python (pandas + lets-plot)

```python
# Data cleaning
df['column'] = df['column'].replace(sentinel_value, np.nan)
df['column'] = df['column'].fillna(df['column'].mean())

# Visualization
from lets_plot import *
ggplot(df) + geom_bar(aes(x="cat", y="val"), stat="identity") + ylim(0, 100)
```

<!-- section_id: "e5674579-aab6-420f-a194-215e0ede8223" -->
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

<!-- section_id: "3dce3984-df8c-4506-a8db-6882b6df8609" -->
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

<!-- section_id: "44fcf56b-7d0c-41dd-9ae9-13743b1257d7" -->
## 7. Red Flags and Debugging

<!-- section_id: "02c4cdcb-3486-4f38-a640-4dd167185c31" -->
### Data Red Flags

- Negative values where they shouldn't exist
- Values suspiciously close to sentinel values (-299.7 ≈ -999 × 0.3)
- Percentages over 100% or under 0%
- Means/medians that don't make logical sense

<!-- section_id: "f3c3e402-5e94-414f-beff-3437dc9c3dac" -->
### Visualization Red Flags

- Chart scale doesn't match data range (0-3 for percentages)
- Bar heights don't visually match the data values
- Missing or incorrect axis labels/units
- Legend categories don't match the data

<!-- section_id: "d5eb7ee8-097c-4aa2-ad62-9800e3e444b2" -->
### Analysis Red Flags

- Analysis mentions values not in the top/bottom N of actual data
- Rankings in text don't match rankings in chart
- No specific numbers/percentages cited
- Metric choice not justified

---

<!-- section_id: "bc3831ee-9d78-4109-9527-887f9b40298d" -->
## 8. Quality Checklist

Before publishing any data analysis with visualizations:

<!-- section_id: "120c6783-7a0b-4e53-8514-24906304f195" -->
### Data Quality
- [ ] All sentinel values cleaned BEFORE calculations
- [ ] All missing value indicators standardized
- [ ] Data types converted appropriately
- [ ] No unexpected negative values
- [ ] No values suspiciously near sentinel values

<!-- section_id: "df1fdbbd-da0e-447f-a435-ac7e923c62b1" -->
### Visualization Quality
- [ ] Charts with pre-calculated values use `stat="identity"` (or equivalent)
- [ ] Percentage charts have explicit 0-100 limits
- [ ] Chart scales make logical sense
- [ ] All axes labeled with units
- [ ] Legends present and clear

<!-- section_id: "db82b9fe-3a9e-48da-8009-d8d147184c14" -->
### Analysis Quality
- [ ] Written analysis checked against actual sorted data
- [ ] Specific values/percentages cited in text
- [ ] Rankings in text match rankings in chart
- [ ] Metric choice explained (WHY not just WHAT)
- [ ] Analysis makes logical sense given the data

---

<!-- section_id: "a52ceee6-6369-4548-9ca7-21e2d14492de" -->
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

<!-- section_id: "30042c98-8227-41a5-bc45-d61d661ef89f" -->
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
