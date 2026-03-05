---
resource_id: "4374b67d-f26d-4529-a411-19d6a90c44da"
resource_type: "document"
resource_name: "data_visualization_principles"
---
# Data Visualization and Analysis Principles

**Level**: Universal Tools (0.75)
**Applies To**: All data analysis and visualization work
**Last Updated**: November 13, 2025
**Derived From**: Unit 3 DS250 lessons learned

---

<!-- section_id: "1ba762f8-46d5-450e-adfc-c49d1f149f7a" -->
## Purpose

This document establishes universal principles for data visualization, data cleaning, and analysis consistency that apply across all projects involving data analysis and visualization.

**Key Lesson**: The order of operations in data preparation and the technical details of chart rendering significantly impact data quality and visual accuracy.

---

<!-- section_id: "f8f84e73-4abd-4814-829e-cfcc2ccc9e34" -->
## 1. Data Cleaning Order of Operations

<!-- section_id: "60cb110e-c8b3-452e-a682-f1f57a83ad9d" -->
### The Golden Rule

**ALWAYS clean data BEFORE performing calculations on it.**

<!-- section_id: "cb48ea5c-0c94-48db-9072-23b20c32dea2" -->
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

<!-- section_id: "6d465cde-8171-4f4e-a80e-81430c6a94ec" -->
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

<!-- section_id: "b875a55d-8f59-42dd-80fe-a240ea5ce16d" -->
### Red Flags to Watch For

- Unexpected negative values in results
- Values in the range of sentinel values (e.g., -299.7 ≈ -999 × 0.3)
- NaN appearing after calculations instead of before
- Results that don't make logical sense (negative percentages, etc.)

---

<!-- section_id: "2e553807-5744-4a54-ba5d-92e798b64675" -->
## 2. Chart Rendering Best Practices

<!-- section_id: "53b57de7-682b-487e-a13e-07199d583bc9" -->
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

<!-- section_id: "c5002b42-52d3-4248-b3d8-1946c0ee61ef" -->
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

<!-- section_id: "0b975a62-f9f1-47ef-ac03-7b0c9bd32f61" -->
### Chart Verification Checklist

Before publishing any visualization:

- [ ] Chart scale makes sense (0-3 for percentages = BUG)
- [ ] Pre-calculated values use `stat="identity"` (or equivalent)
- [ ] Percentage charts have explicit y-limits (0-100)
- [ ] Axis labels are clear and include units
- [ ] Legend is present and understandable
- [ ] Colors are distinguishable and accessible

---

<!-- section_id: "92aaace8-b214-4885-9d64-7595983ba24d" -->
## 3. Analysis-Visual Consistency

<!-- section_id: "0c14ba3e-b607-49c7-83e2-83c594f0f754" -->
### The Principle

**Written analysis must precisely match what visualizations show.**

<!-- section_id: "f3960d9f-0774-42e9-b58f-72dadf4f1518" -->
### Process

```
1. Clean data
2. Generate the visualization
3. Examine the actual sorted data values
4. Write analysis based on what you actually see
5. Include specific numbers/percentages from the data
6. Verify once more before publishing
```

<!-- section_id: "e58a767c-c559-4262-b017-6b677a00ebfc" -->
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

<!-- section_id: "84779df7-4343-4743-9511-4fe409c7ac6a" -->
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

<!-- section_id: "ca7cf64e-d76b-482c-86d8-372e43652094" -->
## 4. Metric Justification

<!-- section_id: "9cb3b898-53ed-4713-93dc-2cd4dd363700" -->
### The Requirement

**Always explain WHY you chose a metric, not just WHAT it shows.**

<!-- section_id: "a1281194-7a86-47ec-837d-dc2b7267d9e8" -->
### Complete Justification Structure

```markdown
1. State the metric chosen (e.g., "delay rate" vs "total delays")
2. Explain why it's appropriate for the question
3. Explain why it's better than alternatives
4. Show how it helps answer the specific question
5. Present the results using that metric
```

<!-- section_id: "643e9b59-72b2-4e00-9613-16c9e65fa060" -->
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

<!-- section_id: "2a193237-9dc4-4e89-84cc-8b62c74dc7dd" -->
### Common Metrics and Their Use Cases

| Metric | When to Use | When NOT to Use |
|--------|-------------|-----------------|
| **Proportion/Rate** | Comparing entities of different sizes | When absolute counts matter more |
| **Total Count** | Understanding overall impact/volume | Comparing different-sized groups |
| **Average** | Understanding typical experience | When outliers are important |
| **Median** | Data with outliers/skewed distribution | When mean is more meaningful |

---

<!-- section_id: "a6dbd7c8-957e-44ba-a353-049fc6d0d242" -->
## 5. Sequential Development Impact

<!-- section_id: "4ce74ebe-4360-4d91-ac92-05353e5aceb6" -->
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

<!-- section_id: "604bd87b-6c78-4120-a3fc-5e61f3724736" -->
## 6. Technology-Specific Notes

<!-- section_id: "474577ab-2063-4359-948a-4fece4ef5124" -->
### Python (pandas + lets-plot)

```python
# Data cleaning
df['column'] = df['column'].replace(sentinel_value, np.nan)
df['column'] = df['column'].fillna(df['column'].mean())

# Visualization
from lets_plot import *
ggplot(df) + geom_bar(aes(x="cat", y="val"), stat="identity") + ylim(0, 100)
```

<!-- section_id: "72fc6a2f-4845-4866-a4d0-931535aecea5" -->
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

<!-- section_id: "a0ae120b-8128-4ea5-ae30-9e7420711edc" -->
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

<!-- section_id: "eb38cce0-8918-4438-9b4d-df2a55cc4393" -->
## 7. Red Flags and Debugging

<!-- section_id: "aa941219-1e54-4dc6-8619-ff435d81b806" -->
### Data Red Flags

- Negative values where they shouldn't exist
- Values suspiciously close to sentinel values (-299.7 ≈ -999 × 0.3)
- Percentages over 100% or under 0%
- Means/medians that don't make logical sense

<!-- section_id: "1cb6a372-6901-4b60-93f6-10b28fd7453e" -->
### Visualization Red Flags

- Chart scale doesn't match data range (0-3 for percentages)
- Bar heights don't visually match the data values
- Missing or incorrect axis labels/units
- Legend categories don't match the data

<!-- section_id: "a892c347-ab17-44c2-bb02-417cb9a4cb30" -->
### Analysis Red Flags

- Analysis mentions values not in the top/bottom N of actual data
- Rankings in text don't match rankings in chart
- No specific numbers/percentages cited
- Metric choice not justified

---

<!-- section_id: "b23b7b93-ba48-4934-bd34-1c06bd7c5fd1" -->
## 8. Quality Checklist

Before publishing any data analysis with visualizations:

<!-- section_id: "0c96648f-6561-4cb8-aeb9-5e49c81851ca" -->
### Data Quality
- [ ] All sentinel values cleaned BEFORE calculations
- [ ] All missing value indicators standardized
- [ ] Data types converted appropriately
- [ ] No unexpected negative values
- [ ] No values suspiciously near sentinel values

<!-- section_id: "c6352631-3a99-4af0-ab12-4a7f86878ea3" -->
### Visualization Quality
- [ ] Charts with pre-calculated values use `stat="identity"` (or equivalent)
- [ ] Percentage charts have explicit 0-100 limits
- [ ] Chart scales make logical sense
- [ ] All axes labeled with units
- [ ] Legends present and clear

<!-- section_id: "e6ffb1c7-793b-4d0b-a3c7-75a35cf7a0a2" -->
### Analysis Quality
- [ ] Written analysis checked against actual sorted data
- [ ] Specific values/percentages cited in text
- [ ] Rankings in text match rankings in chart
- [ ] Metric choice explained (WHY not just WHAT)
- [ ] Analysis makes logical sense given the data

---

<!-- section_id: "e04e40c8-cf67-4913-97d4-c949424f14c7" -->
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

<!-- section_id: "10a8b3f6-76ce-4d39-aad0-57ae41cab2c8" -->
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
