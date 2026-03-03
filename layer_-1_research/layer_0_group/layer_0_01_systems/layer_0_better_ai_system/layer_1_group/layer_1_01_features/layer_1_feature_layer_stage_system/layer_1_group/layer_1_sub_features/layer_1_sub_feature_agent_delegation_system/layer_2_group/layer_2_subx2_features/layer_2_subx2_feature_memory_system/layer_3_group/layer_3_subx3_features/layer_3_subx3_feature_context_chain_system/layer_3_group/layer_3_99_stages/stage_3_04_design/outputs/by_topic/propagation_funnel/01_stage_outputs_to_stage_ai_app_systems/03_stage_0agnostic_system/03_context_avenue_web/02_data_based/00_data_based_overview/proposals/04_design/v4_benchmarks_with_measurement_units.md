# Context Avenue Database Schema — Proposal v4

## Benchmarks with Measurement Units & Methodology

This proposal adds **measurable units** and **methodology** to every capability, enabling benchmarks to be data-driven, traceable, and updateable.

---

## Core Concept

**Benchmarks are only meaningful with units.** Each capability needs:
- **Unit of measurement** — what scale/metric is used
- **Measurement methodology** — how the benchmark is obtained
- **Raw value** — the actual measured data
- **Normalized score** — conversion to 0-100 for comparison

Example:
```
Capability: Speed
Unit: milliseconds (ms)
Raw Value: Knowledge Graph = 450ms, Vector DB = 15ms
Normalized: Knowledge Graph = 33/100, Vector DB = 100/100
```

---

## Database Schema

### 1. CAPABILITY_METRICS (Defines how each capability is measured)

```sql
CREATE TABLE capability_metrics (
  id INTEGER PRIMARY KEY,
  capability_id INTEGER,
  unit_of_measurement TEXT,        -- "milliseconds", "1-5 scale", "$", "%", "hours", etc.
  measurement_methodology TEXT,    -- HOW it's measured (can reference external docs)
  measurement_scale_min REAL,      -- minimum value on scale
  measurement_scale_max REAL,      -- maximum value on scale
  lower_is_better BOOLEAN,         -- TRUE if lower values are better (cost, difficulty)
  baseline_reference TEXT,         -- what "good" looks like
  example_measurement TEXT,        -- example of how to measure
  FOREIGN KEY (capability_id) REFERENCES capabilities(id),
  UNIQUE(capability_id)
);
```

### 2. CAPABILITY_BENCHMARKS (Actual measured values)

```sql
CREATE TABLE capability_benchmarks (
  id INTEGER PRIMARY KEY,
  avenue_type_id INTEGER,
  capability_id INTEGER,
  raw_value REAL,                  -- measured value in native units
  raw_unit TEXT,                   -- the unit (ms, $, 1-5, %, etc.)
  normalized_score REAL,           -- 0-100 normalized score
  measurement_date TEXT,           -- ISO 8601 date when measured
  measurement_source TEXT,         -- "research", "vendor_spec", "benchmark_test", etc.
  notes TEXT,
  FOREIGN KEY (avenue_type_id) REFERENCES avenue_types(id),
  FOREIGN KEY (capability_id) REFERENCES capabilities(id)
);
```

---

## Capability Measurement Definitions

### Performance Metrics

#### 1. Speed (Retrieval/Read/Write Performance)
| Property | Value |
|----------|-------|
| **Unit** | milliseconds (ms) |
| **Methodology** | Measure response time for standard query on 1 million record dataset |
| **Scale** | 10ms (best) to 10,000ms (worst) |
| **Lower is Better** | TRUE |
| **Baseline "Good"** | <100ms |
| **Example** | Knowledge Graph: 450ms, Vector DB: 15ms |

#### 2. Scalability (Ability to Grow)
| Property | Value |
|----------|-------|
| **Unit** | number of records (millions) |
| **Methodology** | Maximum dataset size efficiently indexable and queryable |
| **Scale** | 1M (minimum) to 10,000M (10 billion, maximum) |
| **Lower is Better** | FALSE (higher = better) |
| **Baseline "Good"** | >1,000M (1 billion records) |
| **Example** | Knowledge Graph: 500M, Vector DB: 10,000M |

#### 3. Freshness (Auto-sync Frequency)
| Property | Value |
|----------|-------|
| **Unit** | hours |
| **Methodology** | Maximum time lag before updates propagate from source to all replicas |
| **Scale** | <1 hour (best) to 24+ hours (worst) |
| **Lower is Better** | TRUE |
| **Baseline "Good"** | <4 hours |
| **Example** | SHIMI: 0.5 hours, Knowledge Graph: 8 hours |

---

### Usability & Comprehensibility

#### 4. Readability (Ease of Parsing)
| Property | Value |
|----------|-------|
| **Unit** | 1-5 scale |
| **Methodology** | Expert panel rates how easy to understand output format (1=very difficult, 5=trivial) |
| **Scale** | 1 to 5 |
| **Lower is Better** | FALSE (higher = more readable) |
| **Baseline "Good"** | >3.5/5.0 |
| **Example** | Relational Tables: 4.8/5, Vector Databases: 2.1/5 |

#### 5. Interpretability (Understanding & Reasoning)
| Property | Value |
|----------|-------|
| **Unit** | 1-5 scale |
| **Methodology** | Rate how easily stakeholders can understand WHY a result was returned (1=black box, 5=fully transparent) |
| **Scale** | 1 to 5 |
| **Lower is Better** | FALSE |
| **Baseline "Good"** | >3.5/5.0 |
| **Example** | Knowledge Graph: 4.5/5, Vector DB: 2.0/5 |

#### 6. Reasoning Capability (Quality of Inference)
| Property | Value |
|----------|-------|
| **Unit** | 1-5 scale |
| **Methodology** | Rate capability to perform logical inference: 1=none, 5=perfect reasoning chains |
| **Scale** | 1 to 5 |
| **Lower is Better** | FALSE |
| **Baseline "Good"** | >4.0/5.0 |
| **Example** | Knowledge Graph: 4.8/5, Vector DB: 2.2/5 |

---

### Coverage & Completeness

#### 7. Coverage (Information Available)
| Property | Value |
|----------|-------|
| **Unit** | percentage (%) |
| **Methodology** | What % of potential data types can be represented and indexed |
| **Scale** | 20% (minimum) to 100% (perfect) |
| **Lower is Better** | FALSE |
| **Baseline "Good"** | >85% |
| **Example** | Knowledge Graph: 95%, Vector DB: 70% |

#### 8. Comprehensiveness (Depth & Breadth)
| Property | Value |
|----------|-------|
| **Unit** | percentage (%) |
| **Methodology** | Breadth (data types covered) × Depth (relationship complexity) as % of ideal |
| **Scale** | 20% to 100% |
| **Lower is Better** | FALSE |
| **Baseline "Good"** | >80% |
| **Example** | Knowledge Graph: 92%, Relational Tables: 85% |

---

### Maintainability & Deployment

#### 9. Setup Difficulty (Implementation Effort)
| Property | Value |
|----------|-------|
| **Unit** | 1-5 scale |
| **Methodology** | Expert estimate: days to production-ready deployment (1=<1 day, 5=>2 weeks) |
| **Scale** | 1 to 5 |
| **Lower is Better** | TRUE |
| **Baseline "Good"** | <2.5/5.0 |
| **Example** | Relational Tables: 1.2/5, Knowledge Graph: 3.8/5 |

#### 10. Maintenance Difficulty (Ongoing Effort)
| Property | Value |
|----------|-------|
| **Unit** | hours per year |
| **Methodology** | Annual maintenance person-hours for typical medium deployment |
| **Scale** | 10 hours/year (best) to 1,000+ hours/year (worst) |
| **Lower is Better** | TRUE |
| **Baseline "Good"** | <100 hours/year |
| **Example** | Relational Tables: 40 hrs/year, Knowledge Graph: 250 hrs/year |

#### 11. Updateability (Ease to Modify)
| Property | Value |
|----------|-------|
| **Unit** | 1-5 scale |
| **Methodology** | Rate ease of schema changes, updates, extensions (1=very difficult, 5=trivial) |
| **Scale** | 1 to 5 |
| **Lower is Better** | TRUE |
| **Baseline "Good"** | <2.5/5.0 |
| **Example** | Relational Tables: 1.5/5, Knowledge Graph: 3.2/5 |

---

### Integration & Discoverability

#### 12. Searchability (Content Discovery)
| Property | Value |
|----------|-------|
| **Unit** | 1-5 scale |
| **Methodology** | Rate ability to quickly find content (full-text, semantic, similarity search available) |
| **Scale** | 1 to 5 |
| **Lower is Better** | FALSE |
| **Baseline "Good"** | >4.0/5.0 |
| **Example** | Vector Databases: 4.9/5, Relational Tables: 4.2/5 |

#### 13. Dependency (Tool Integration Required)
| Property | Value |
|----------|-------|
| **Unit** | 1-5 scale |
| **Methodology** | Count of external dependencies (1=minimal/universal, 5=many specialized tools) |
| **Scale** | 1 to 5 |
| **Lower is Better** | TRUE |
| **Baseline "Good"** | <2.5/5.0 |
| **Example** | Relational Tables: 1.1/5, Knowledge Graph: 3.5/5 |

#### 14. Redundancy (Backup & Failover)
| Property | Value |
|----------|-------|
| **Unit** | 1-5 scale |
| **Methodology** | Maturity of replication, backup, and failover mechanisms (1=manual only, 5=fully automated) |
| **Scale** | 1 to 5 |
| **Lower is Better** | FALSE |
| **Baseline "Good"** | >3.5/5.0 |
| **Example** | Relational Tables: 4.8/5, Vector DB: 4.1/5 |

---

### Economics & Industry Adoption

#### 15. Cost (Implementation & Operational)
| Property | Value |
|----------|-------|
| **Unit** | $/month (Total Cost of Ownership) |
| **Methodology** | Annual all-in cost (software, hardware, personnel, support) ÷ 12 for medium deployment |
| **Scale** | $0/month (open source) to $50,000+/month (enterprise) |
| **Lower is Better** | TRUE |
| **Baseline "Good"** | <$5,000/month |
| **Example** | Relational Tables: $800/mo, Knowledge Graph: $12,000/mo |

#### 16. Use Frequency in Industry (Adoption & Maturity)
| Property | Value |
|----------|-------|
| **Unit** | percentage (%) |
| **Methodology** | % of relevant industry segment actively using this approach |
| **Scale** | 1% (emerging) to 100% (ubiquitous) |
| **Lower is Better** | FALSE |
| **Baseline "Good"** | >30% |
| **Example** | Relational Tables: 95%, Vector DB: 65%, Knowledge Graph: 40%, SHIMI: 5% |

---

## Normalization: Raw Units → 0-100 Scores

Each raw benchmark is converted to a 0-100 normalized score for comparison.

### Normalization Formula

For **higher-is-better** capabilities:
```
score = (raw_value - min_value) / (max_value - min_value) * 100
```

For **lower-is-better** capabilities:
```
score = (max_value - raw_value) / (max_value - min_value) * 100
```

### Example Conversions

**Speed (lower is better)**
- Scale: 10ms to 10,000ms
- Vector DB: 15ms → score = (10000-15)/(10000-10) × 100 = 99.85 ≈ 100
- Knowledge Graph: 450ms → score = (10000-450)/(10000-10) × 100 = 95.6 ≈ 96
- Relational Tables: 200ms → score = (10000-200)/(10000-10) × 100 = 98.0

**Scalability (higher is better)**
- Scale: 1M to 10,000M
- Vector DB: 10,000M → score = 100
- SHIMI: 5,000M → score = (5000-1)/(10000-1) × 100 ≈ 50
- Knowledge Graph: 500M → score = (500-1)/(10000-1) × 100 ≈ 5

**Reasoning Capability (higher is better, 1-5 scale)**
- Scale: 1 to 5
- Knowledge Graph: 4.8/5 → score = (4.8-1)/(5-1) × 100 = 95
- SHIMI: 3.5/5 → score = (3.5-1)/(5-1) × 100 = 62.5
- Vector DB: 2.2/5 → score = (2.2-1)/(5-1) × 100 = 30

---

## SQL Implementation

### Insert Capability Metrics

```sql
INSERT INTO capability_metrics (capability_id, unit_of_measurement, measurement_methodology,
                                measurement_scale_min, measurement_scale_max, lower_is_better,
                                baseline_reference, example_measurement)
VALUES
((SELECT id FROM capabilities WHERE name = 'Speed'),
 'milliseconds',
 'Query response time for standard search on 1M record dataset',
 10, 10000, 1,
 '<100ms for acceptable performance',
 'Run 100 sequential queries, record average response time'),

((SELECT id FROM capabilities WHERE name = 'Scalability'),
 'millions of records',
 'Maximum dataset size efficiently indexed and queryable',
 1, 10000, 0,
 '>1,000M (1 billion) for strong scalability',
 'Test with datasets of increasing size, find breaking point'),

((SELECT id FROM capabilities WHERE name = 'Cost'),
 '$/month TCO',
 'Annual all-in cost (software, hardware, personnel, support) ÷ 12',
 0, 50000, 1,
 '<$5,000/month for cost efficiency',
 'Calculate total 3-year cost, divide by 36 months'),

((SELECT id FROM capabilities WHERE name = 'Reasoning Capability'),
 '1-5 scale',
 'Expert panel rates logical inference capability (1=none, 5=perfect)',
 1, 5, 0,
 '>4.0/5.0 for strong reasoning',
 'Have domain experts rate inference quality'),

-- ... continue for all 16 capabilities
```

### Insert Benchmark Data

```sql
INSERT INTO capability_benchmarks (avenue_type_id, capability_id, raw_value, raw_unit,
                                   normalized_score, measurement_date, measurement_source, notes)
VALUES
-- Vector Database benchmarks
((SELECT id FROM avenue_types WHERE type_name = 'vector_databases'),
 (SELECT id FROM capabilities WHERE name = 'Speed'),
 15, 'milliseconds', 99.85, '2026-03-02', 'benchmark_test',
 'Average from 100 sequential queries on 1M vector embeddings'),

((SELECT id FROM avenue_types WHERE type_name = 'vector_databases'),
 (SELECT id FROM capabilities WHERE name = 'Scalability'),
 10000, 'millions of records', 100, '2026-03-02', 'vendor_spec',
 'Official capacity specification for distributed deployment'),

-- Knowledge Graph benchmarks
((SELECT id FROM avenue_types WHERE type_name = 'knowledge_graph'),
 (SELECT id FROM capabilities WHERE name = 'Speed'),
 450, 'milliseconds', 95.6, '2026-03-02', 'benchmark_test',
 'Complex relationship traversal queries'),

((SELECT id FROM avenue_types WHERE type_name = 'knowledge_graph'),
 (SELECT id FROM capabilities WHERE name = 'Reasoning Capability'),
 4.8, '1-5 scale', 95, '2026-03-02', 'expert_panel',
 'Expert consensus on inference quality'),

-- ... continue for all avenues × capabilities
```

---

## Query Examples

### Get Actual Measurements (Raw Values)

```sql
-- Show actual measured values for each avenue
SELECT
  at.type_name,
  c.name as capability,
  cb.raw_value,
  cb.raw_unit,
  cm.baseline_reference,
  cb.measurement_source
FROM capability_benchmarks cb
JOIN avenue_types at ON cb.avenue_type_id = at.id
JOIN capabilities c ON cb.capability_id = c.id
JOIN capability_metrics cm ON c.id = cm.capability_id
ORDER BY at.type_name, c.name;
```

### Convert and Compare Scores

```sql
-- Show normalized scores for comparison
SELECT
  at.type_name,
  c.name as capability,
  cb.raw_value,
  cb.raw_unit,
  cb.normalized_score,
  CASE
    WHEN cb.normalized_score >= 85 THEN 'Excellent'
    WHEN cb.normalized_score >= 70 THEN 'Good'
    WHEN cb.normalized_score >= 50 THEN 'Fair'
    ELSE 'Poor'
  END as rating
FROM capability_benchmarks cb
JOIN avenue_types at ON cb.avenue_type_id = at.id
JOIN capabilities c ON cb.capability_id = c.id
ORDER BY at.type_name, cb.normalized_score DESC;
```

### Threshold-Based Decisions

```sql
-- Find avenues that meet minimum requirements
-- (e.g., Speed <200ms AND Cost <$5000/month AND Reasoning >3.5/5)

SELECT at.type_name, c.name, cb.raw_value, cb.raw_unit
FROM capability_benchmarks cb
JOIN avenue_types at ON cb.avenue_type_id = at.id
JOIN capabilities c ON cb.capability_id = c.id
WHERE
  (c.name = 'Speed' AND cb.raw_value < 200) OR
  (c.name = 'Cost' AND cb.raw_value < 5000) OR
  (c.name = 'Reasoning Capability' AND cb.raw_value > 3.5)
ORDER BY at.type_name;
```

### Tradeoff Analysis

```sql
-- Show Speed vs Cost tradeoff
SELECT
  at.type_name,
  CASE WHEN c.name = 'Speed' THEN cb.raw_value END as speed_ms,
  CASE WHEN c.name = 'Cost' THEN cb.raw_value END as cost_month
FROM capability_benchmarks cb
JOIN avenue_types at ON cb.avenue_type_id = at.id
JOIN capabilities c ON cb.capability_id = c.id
WHERE c.name IN ('Speed', 'Cost')
PIVOT (MAX(value) FOR capability IN (...))
ORDER BY speed_ms;
```

---

## Benefits of Measurement Units

✅ **Measurable** — every benchmark has a clear unit and methodology
✅ **Traceable** — you can verify how scores were calculated
✅ **Comparable** — normalize raw values to 0-100 for fair comparison
✅ **Updateable** — new measurements update scores automatically
✅ **Decision-supportive** — threshold queries answer real questions
✅ **Defensible** — backed by measurable data, not opinion

---

## Next Steps

1. **Populate CAPABILITY_METRICS** — insert all 16 capability definitions
2. **Populate CAPABILITY_BENCHMARKS** — insert all raw measurement data (4 avenues × 16 capabilities)
3. **Create views** — derive rankings from normalized scores
4. **Test threshold queries** — verify decision-support queries work
5. **Validate with SQLite Viewer** — visually inspect the complete matrix

---

## Summary

This v4 proposal:
- ✅ Adds **CAPABILITY_METRICS table** defining how each capability is measured
- ✅ Refines **CAPABILITY_BENCHMARKS table** to track raw values and normalized scores
- ✅ Provides **16 measurement definitions** with units, methodology, and baselines
- ✅ Shows **normalization formula** for converting raw units → 0-100 scores
- ✅ Includes **SQL implementation** for storing and querying benchmarks
- ✅ Enables **threshold-based decision queries** ("find avenues with Speed <200ms AND Cost <$5000")

Raw measurements drive everything. Rankings are derived. Decisions are data-backed.
