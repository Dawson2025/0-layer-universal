---
resource_id: "d3e0054a-c1cf-4257-859d-4951cd354700"
resource_type: "document"
resource_name: "data_visualization_principles"
---
# Data Visualization and Analysis Principles

**Level**: Universal Tools (0.75)
**Applies To**: All data analysis and visualization work
**Last Updated**: November 13, 2025
**Derived From**: Unit 3 DS250 lessons learned

---

<!-- section_id: "0dd6e9e3-6277-437f-a738-2db440dfaf40" -->
## Purpose

This document establishes universal principles for data visualization, data cleaning, and analysis consistency that apply across all projects involving data analysis and visualization.

**Key Lesson**: The order of operations in data preparation and the technical details of chart rendering significantly impact data quality and visual accuracy.

---

<!-- section_id: "8ade45b7-72c6-4daa-83e8-5f221f20e2ab" -->
## 1. Data Cleaning Order of Operations

<!-- section_id: "8bb0b467-cde7-4a3b-9eb3-746188166407" -->
### The Golden Rule

**ALWAYS clean data BEFORE performing calculations on it.**

<!-- section_id: "7bfed74b-5453-44ff-80e1-55c157c32d09" -->
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

<!-- section_id: "f4ae8c2e-429c-4166-a775-948fa886ee2f" -->
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

<!-- section_id: "a1271098-a294-49ce-90ac-2e587db2cfe0" -->
### Red Flags to Watch For

- Unexpected negative values in results
- Values in the range of sentinel values (e.g., -299.7 ≈ -999 × 0.3)
- NaN appearing after calculations instead of before
- Results that don't make logical sense (negative percentages, etc.)

---

<!-- section_id: "814a2e09-9000-40ff-b36b-cebd1c3c1b01" -->
## 2. Chart Rendering Best Practices

<!-- section_id: "3b0b1a2a-9d62-4054-8322-ce57d49c7e84" -->
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

<!-- section_id: "36656a78-b32e-4096-8da5-e6410262ec0b" -->
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

<!-- section_id: "246d453b-1b1e-491a-8ac1-16f01926bc6e" -->
### Chart Verification Checklist

Before publishing any visualization:

- [ ] Chart scale makes sense (0-3 for percentages = BUG)
- [ ] Pre-calculated values use `stat="identity"` (or equivalent)
- [ ] Percentage charts have explicit y-limits (0-100)
- [ ] Axis labels are clear and include units
- [ ] Legend is present and understandable
- [ ] Colors are distinguishable and accessible

---

<!-- section_id: "54803a3b-74ca-4c0e-a9e1-25f47db9e200" -->
## 3. Analysis-Visual Consistency

<!-- section_id: "27745c86-bf16-4078-8c8b-7c621d266199" -->
### The Principle

**Written analysis must precisely match what visualizations show.**

<!-- section_id: "3561241a-3a94-42b8-8d4e-d4d938ffa108" -->
### Process

```
1. Clean data
2. Generate the visualization
3. Examine the actual sorted data values
4. Write analysis based on what you actually see
5. Include specific numbers/percentages from the data
6. Verify once more before publishing
```

<!-- section_id: "b56d3110-bb3e-48bc-bbfe-c1650073e115" -->
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

<!-- section_id: "8fb8963f-ac89-48b9-a113-256708ebd6f8" -->
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

<!-- section_id: "2124f5cc-d8be-4cd4-b082-a1b6c082e95f" -->
## 4. Metric Justification

<!-- section_id: "707af471-4301-455b-bf17-e732ba1f34a5" -->
### The Requirement

**Always explain WHY you chose a metric, not just WHAT it shows.**

<!-- section_id: "d8346ce7-1589-4183-8180-f7e5819d57e7" -->
### Complete Justification Structure

```markdown
1. State the metric chosen (e.g., "delay rate" vs "total delays")
2. Explain why it's appropriate for the question
3. Explain why it's better than alternatives
4. Show how it helps answer the specific question
5. Present the results using that metric
```

<!-- section_id: "24bb35e1-2b04-411e-90fc-fabbd16ee956" -->
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

<!-- section_id: "35ee6080-dfdb-4a97-ae0c-cb6fcb2c3e88" -->
### Common Metrics and Their Use Cases

| Metric | When to Use | When NOT to Use |
|--------|-------------|-----------------|
| **Proportion/Rate** | Comparing entities of different sizes | When absolute counts matter more |
| **Total Count** | Understanding overall impact/volume | Comparing different-sized groups |
| **Average** | Understanding typical experience | When outliers are important |
| **Median** | Data with outliers/skewed distribution | When mean is more meaningful |

---

<!-- section_id: "e49affaf-4efd-4ca9-ad4b-2086cd209a56" -->
## 5. Sequential Development Impact

<!-- section_id: "d5dd9310-6fd3-47e4-9c41-02440c042806" -->
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

<!-- section_id: "769211a1-99a4-4468-8832-e9140c8945b0" -->
## 6. Technology-Specific Notes

<!-- section_id: "e2a363d9-20a9-481f-90f3-1456a4080e92" -->
### Python (pandas + lets-plot)

```python
# Data cleaning
df['column'] = df['column'].replace(sentinel_value, np.nan)
df['column'] = df['column'].fillna(df['column'].mean())

# Visualization
from lets_plot import *
ggplot(df) + geom_bar(aes(x="cat", y="val"), stat="identity") + ylim(0, 100)
```

<!-- section_id: "012434d3-6ba5-4497-8e3c-c7fa66792be9" -->
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

<!-- section_id: "02e6559e-d87b-48e0-aa2d-50e895641027" -->
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

<!-- section_id: "f59e4bbf-62c8-465e-aafb-4d5225de3a36" -->
## 7. Red Flags and Debugging

<!-- section_id: "108c9b10-1a50-4162-9f51-beb7597c3f1f" -->
### Data Red Flags

- Negative values where they shouldn't exist
- Values suspiciously close to sentinel values (-299.7 ≈ -999 × 0.3)
- Percentages over 100% or under 0%
- Means/medians that don't make logical sense

<!-- section_id: "4e6ddf47-cee4-4d9f-b7dc-b503e4cd3400" -->
### Visualization Red Flags

- Chart scale doesn't match data range (0-3 for percentages)
- Bar heights don't visually match the data values
- Missing or incorrect axis labels/units
- Legend categories don't match the data

<!-- section_id: "51cbb856-6a19-47c1-ab4a-b89d9cc2a982" -->
### Analysis Red Flags

- Analysis mentions values not in the top/bottom N of actual data
- Rankings in text don't match rankings in chart
- No specific numbers/percentages cited
- Metric choice not justified

---

<!-- section_id: "c240623d-d9ce-4d83-a81f-3ebc0073cd26" -->
## 8. Quality Checklist

Before publishing any data analysis with visualizations:

<!-- section_id: "f9230677-2cff-4d9f-b0ce-2e1ba3f74bbc" -->
### Data Quality
- [ ] All sentinel values cleaned BEFORE calculations
- [ ] All missing value indicators standardized
- [ ] Data types converted appropriately
- [ ] No unexpected negative values
- [ ] No values suspiciously near sentinel values

<!-- section_id: "8025a134-8d7e-4bea-a95c-b2c1b249c768" -->
### Visualization Quality
- [ ] Charts with pre-calculated values use `stat="identity"` (or equivalent)
- [ ] Percentage charts have explicit 0-100 limits
- [ ] Chart scales make logical sense
- [ ] All axes labeled with units
- [ ] Legends present and clear

<!-- section_id: "98cb65ff-da44-4848-a873-725b83c97d16" -->
### Analysis Quality
- [ ] Written analysis checked against actual sorted data
- [ ] Specific values/percentages cited in text
- [ ] Rankings in text match rankings in chart
- [ ] Metric choice explained (WHY not just WHAT)
- [ ] Analysis makes logical sense given the data

---

<!-- section_id: "73696fb5-5349-4fcd-8ecb-139505945a92" -->
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

<!-- section_id: "3598e283-aa7a-423d-9a82-18cf7c064c92" -->
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
