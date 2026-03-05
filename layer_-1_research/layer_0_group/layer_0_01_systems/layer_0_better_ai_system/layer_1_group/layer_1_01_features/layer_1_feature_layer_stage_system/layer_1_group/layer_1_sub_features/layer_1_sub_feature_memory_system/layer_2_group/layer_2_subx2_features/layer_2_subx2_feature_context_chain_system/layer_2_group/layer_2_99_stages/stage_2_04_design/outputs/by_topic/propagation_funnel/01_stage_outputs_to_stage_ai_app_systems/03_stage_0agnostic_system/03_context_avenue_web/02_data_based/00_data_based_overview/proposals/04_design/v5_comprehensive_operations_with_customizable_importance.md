---
resource_id: "aaff36a4-9c4e-4fcf-b0ac-2d877d246c28"
resource_type: "output"
resource_name: "v5_comprehensive_operations_with_customizable_importance"
---
# Context Avenue Database Schema — Proposal v5

## Comprehensive Operations with Customizable Importance Weighting

This proposal adds **all 20+ database operations** with comprehensive **importance measurement** at both general and project-specific levels, enabling projects to customize what matters to their needs.

---

## Core Concept

**Every operation has two dimensions:**
1. **Performance benchmark** — how GOOD is each avenue at this operation (0-100 score)
2. **Importance weight** — how IMPORTANT is this operation (0-100 score, customizable per project)

**Project-specific value = Performance × Importance**

Different projects get different answers from the same data by adjusting importance weights.

Example:
```
Operation: Bulk Insert
- Performance: Vector DB = 85, Relational = 75, Knowledge Graph = 40
- General Importance: 60 (medium priority)
- HighThroughput Project: Importance = 95 (critical)
- FinancialSystem Project: Importance = 30 (not critical)
- Result: HighThroughput favors Vector DB, Financial favors Relational
```

---

## Database Schema

### 1. OPERATIONS (Comprehensive List)

```sql
CREATE TABLE operations (
  id INTEGER PRIMARY KEY,
  operation_name TEXT UNIQUE,           -- "query_point_lookup", "bulk_insert", etc.
  operation_category TEXT,              -- "read", "write", "maintenance", "consistency", "analytics"
  parent_operation_id INTEGER,          -- NULL for top-level (Query, Insert, Update, Delete)
  description TEXT,
  use_case TEXT,                        -- when/why this operation matters
  FOREIGN KEY (parent_operation_id) REFERENCES operations(id)
);
```

**Operation Hierarchy:**
```
CRUD Operations (Top-level)
├── Query (Read)
│   ├── Query - Point Lookup (exact match)
│   ├── Query - Range Query (between X and Y)
│   ├── Query - Fuzzy Search (approximate match)
│   ├── Query - Semantic Search (similarity/concept-based)
│   ├── Query - Full-Text Search (keyword-based)
│   └── Query - Graph Traversal (follow relationships)
├── Insert (Create)
│   ├── Insert - Single Record
│   └── Insert - Bulk (batch insert)
├── Update
│   ├── Update - Single Record
│   └── Update - Bulk (batch update)
└── Delete
    ├── Delete - Single Record
    └── Delete - Bulk (batch delete)

Structural Operations
├── Index - Create/Rebuild
├── Index - Optimize/Defragment
├── Rebalancing (tree/hierarchy rebalancing)
└── Schema Migration

Consistency Operations
├── Transaction - Begin/Commit
├── Rollback - Undo Changes
├── Replication - Sync Updates
├── Conflict Resolution - Merge Data
└── Backup/Recovery

Analytics Operations
├── Aggregation (SUM, AVG, COUNT)
├── Join - Multi-source Data
└── Grouping - GROUP BY Operations
```

---

### 2. OPERATION_METRICS (How to measure operation performance)

```sql
CREATE TABLE operation_metrics (
  id INTEGER PRIMARY KEY,
  operation_id INTEGER,
  unit_of_measurement TEXT,            -- "milliseconds", "ops/sec", "1-5 scale", "%", etc.
  measurement_methodology TEXT,        -- HOW it's measured
  measurement_scale_min REAL,
  measurement_scale_max REAL,
  lower_is_better BOOLEAN,
  baseline_reference TEXT,
  FOREIGN KEY (operation_id) REFERENCES operations(id),
  UNIQUE(operation_id)
);
```

---

### 3. OPERATION_BENCHMARKS (Performance data)

```sql
CREATE TABLE operation_benchmarks (
  id INTEGER PRIMARY KEY,
  avenue_type_id INTEGER,
  operation_id INTEGER,
  raw_value REAL,                      -- measured value
  raw_unit TEXT,
  normalized_score REAL,               -- 0-100 score
  measurement_date TEXT,
  measurement_source TEXT,
  notes TEXT,
  FOREIGN KEY (avenue_type_id) REFERENCES avenue_types(id),
  FOREIGN KEY (operation_id) REFERENCES operations(id)
);
```

---

### 4. IMPORTANCE_METRICS (How to measure importance)

```sql
CREATE TABLE importance_metrics (
  id INTEGER PRIMARY KEY,
  metric_name TEXT UNIQUE,             -- "frequency", "criticality", "cost_impact", "risk_score"
  unit_of_measurement TEXT,            -- "% of use", "1-5 scale", "$", "1-10 scale"
  measurement_methodology TEXT,        -- how importance is assessed
  measurement_scale_min REAL,
  measurement_scale_max REAL,
  lower_is_better BOOLEAN,
  context_type TEXT,                   -- "general", "project_specific", or "both"
  description TEXT,
  UNIQUE(metric_name)
);
```

**Standard Importance Metrics:**
```
1. Frequency: How often operation is used (% of deployments or % of operations)
2. Criticality: How critical to system success (1-5 scale)
3. Cost Impact: Financial impact if operation fails ($, or cost/query)
4. Risk Score: Risk if operation is slow/fails (1-10 scale)
5. User Impact: Direct user-facing importance (1-5 scale)
6. SLA Requirement: Service level agreement requirement (ms target)
7. Competitive Advantage: Strategic advantage if optimized (1-5 scale)
8. Technical Debt: Technical complexity if not optimized (1-5 scale)
```

---

### 5. OPERATION_IMPORTANCE_GENERAL (Base importance for all projects)

```sql
CREATE TABLE operation_importance_general (
  id INTEGER PRIMARY KEY,
  operation_id INTEGER,
  importance_metric_id INTEGER,
  raw_value REAL,                      -- measured value
  raw_unit TEXT,
  normalized_importance REAL,          -- 0-100 score
  rationale TEXT,                      -- why this importance level
  FOREIGN KEY (operation_id) REFERENCES operations(id),
  FOREIGN KEY (importance_metric_id) REFERENCES importance_metrics(id)
);
```

**Example General Importance:**
```
Query - Point Lookup:
  - Frequency: 95% (used in almost all deployments)
  - Criticality: 5/5 (core functionality)
  - Cost Impact: High (slow queries = user delay)
  - Risk Score: 9/10 (system unusable if broken)
  - Combined: ~90/100 importance

Delete - Bulk:
  - Frequency: 20% (rare operation)
  - Criticality: 2/5 (maintenance task)
  - Cost Impact: Low
  - Risk Score: 3/10 (can be done offline)
  - Combined: ~25/100 importance
```

---

### 6. PROJECT_CONTEXTS (Define projects and their priorities)

```sql
CREATE TABLE project_contexts (
  id INTEGER PRIMARY KEY,
  project_name TEXT UNIQUE,
  description TEXT,
  project_type TEXT,                   -- "web_app", "financial_system", "analytics", "real_time", etc.
  priority_focus TEXT,                 -- what matters most for THIS project
  created_date TEXT
);
```

**Example Project Types:**
- `high_throughput` — volume matters most (bulk operations, query speed)
- `financial_system` — consistency matters most (transactions, rollback, conflict resolution)
- `real_time_analytics` — query variants and aggregation matter (semantic search, joins, grouping)
- `graph_based_ai` — relationships matter (graph traversal, semantic search)
- `low_cost_archive` — cost matters (cheap storage, infrequent access)
- `high_availability` — consistency matters (replication, backup/recovery, transactions)

---

### 7. PROJECT_OPERATION_IMPORTANCE (Customized importance per project)

```sql
CREATE TABLE project_operation_importance (
  id INTEGER PRIMARY KEY,
  project_id INTEGER,
  operation_id INTEGER,
  importance_metric_id INTEGER,
  raw_value REAL,                      -- project-specific value
  raw_unit TEXT,
  normalized_importance REAL,          -- 0-100 score for THIS project
  rationale TEXT,                      -- why this importance for this project
  override_general BOOLEAN,            -- TRUE if different from general
  FOREIGN KEY (project_id) REFERENCES project_contexts(id),
  FOREIGN KEY (operation_id) REFERENCES operations(id),
  FOREIGN KEY (importance_metric_id) REFERENCES importance_metrics(id)
);
```

**Example Project-Specific Importance:**
```
HighThroughputProject:
  - Bulk Insert: Frequency 95% (vs general 20%) → normalized 95/100
  - Query Point Lookup: Frequency 70% (vs general 95%) → normalized 70/100
  - Transaction: Frequency 10% (vs general 60%) → normalized 10/100

FinancialSystemProject:
  - Transaction: Criticality 5/5 (vs general 3/5) → normalized 100/100
  - Rollback: Criticality 5/5 (vs general 2/5) → normalized 100/100
  - Conflict Resolution: Criticality 5/5 (vs general 2/5) → normalized 100/100
  - Query Speed: Criticality 2/5 (vs general 5/5) → normalized 40/100
```

---

### 8. WEIGHTED_OPERATION_SCORES (Project-specific recommendations)

```sql
CREATE VIEW weighted_operation_scores AS
SELECT
  p.project_name,
  at.type_name as avenue_type,
  o.operation_name,
  ob.normalized_score as performance_score,
  COALESCE(poi.normalized_importance, oig.normalized_importance) as importance_score,
  (ob.normalized_score * COALESCE(poi.normalized_importance, oig.normalized_importance) / 100) as weighted_score,
  RANK() OVER (PARTITION BY p.project_name, o.operation_name ORDER BY weighted_score DESC) as rank_for_operation
FROM project_contexts p
CROSS JOIN avenue_types at
CROSS JOIN operations o
LEFT JOIN operation_benchmarks ob ON at.id = ob.avenue_type_id AND o.id = ob.operation_id
LEFT JOIN operation_importance_general oig ON o.id = oig.operation_id
LEFT JOIN project_operation_importance poi ON p.id = poi.project_id AND o.id = poi.operation_id
WHERE ob.normalized_score IS NOT NULL
ORDER BY p.project_name, weighted_score DESC;
```

---

## Importance Measurement Definitions

### 1. Frequency (How Often Used)

| Property | Value |
|----------|-------|
| **Unit** | percentage (%) |
| **Methodology** | % of deployments/systems that use this operation |
| **Scale** | 5% (rarely used) to 100% (universal) |
| **Lower is Better** | FALSE |
| **Baseline "Critical"** | >70% (used in most deployments) |
| **General Examples** | Query Point: 95%, Bulk Delete: 15%, Graph Traversal: 20% |

### 2. Criticality (Impact if Broken)

| Property | Value |
|----------|-------|
| **Unit** | 1-5 scale |
| **Methodology** | Expert rating: if this operation fails, how bad? (1=minor, 5=system unusable) |
| **Scale** | 1 to 5 |
| **Lower is Better** | FALSE |
| **Baseline "Critical"** | >4/5 (system seriously impaired if broken) |
| **General Examples** | Query: 5/5, Bulk Insert: 3/5, Rebalancing: 1/5 |

### 3. Cost Impact (Financial Consequence)

| Property | Value |
|----------|-------|
| **Unit** | $/query or $/month |
| **Methodology** | Cost per operation execution + cost of failures |
| **Scale** | $0.001/query (minimal) to $100+/query (expensive) |
| **Lower is Better** | TRUE |
| **Baseline "High Impact"** | >$1/query |
| **General Examples** | Query: $0.01, Bulk Insert: $5, Replication: $100/month |

### 4. Risk Score (Failure Impact)

| Property | Value |
|----------|-------|
| **Unit** | 1-10 scale |
| **Methodology** | (Criticality × Frequency × Cost Impact) normalized to 1-10 |
| **Scale** | 1 (low risk) to 10 (severe risk) |
| **Lower is Better** | TRUE |
| **Baseline "High Risk"** | >7/10 (major risk) |
| **General Examples** | Query: 9/10, Bulk Delete: 4/10, Index Rebuild: 2/10 |

### 5. User Impact (Direct User-Facing)

| Property | Value |
|----------|-------|
| **Unit** | 1-5 scale |
| **Methodology** | How directly does this operation affect end-users? (1=backend, 5=direct user impact) |
| **Scale** | 1 to 5 |
| **Lower is Better** | FALSE |
| **Baseline "High Impact"** | >3.5/5 |
| **General Examples** | Query: 5/5, Transaction: 4/5, Backup: 1/5 |

### 6. SLA Requirement (Service Level Target)

| Property | Value |
|----------|-------|
| **Unit** | milliseconds (ms) or percentile |
| **Methodology** | Required response time for this operation (p99 or average) |
| **Scale** | 1ms (strict) to 10,000ms (relaxed) |
| **Lower is Better** | TRUE |
| **Baseline "Strict"** | <100ms |
| **General Examples** | Query: 50ms p99, Bulk Insert: 5000ms, Rebalance: no SLA |

---

## SQL Implementation

### Insert Operations

```sql
INSERT INTO operations (operation_name, operation_category, parent_operation_id, description, use_case)
VALUES
('query_point_lookup', 'read', NULL, 'Find single record by exact key match', 'User lookups, cache misses'),
('query_range_query', 'read', NULL, 'Find records where value is between X and Y', 'Filtering, time ranges'),
('query_semantic_search', 'read', NULL, 'Find similar concepts/embeddings', 'AI search, recommendations'),
('insert_single', 'write', NULL, 'Insert one record', 'User creates single item'),
('insert_bulk', 'write', NULL, 'Insert thousands of records at once', 'Data migration, batch loading'),
('index_rebuild', 'maintenance', NULL, 'Rebuild indexes for optimal performance', 'Maintenance task'),
('transaction_commit', 'consistency', NULL, 'Commit multi-step transaction atomically', 'Financial transactions'),
('replication_sync', 'consistency', NULL, 'Synchronize updates across replicas', 'Keep copies in sync'),
('aggregation', 'analytics', NULL, 'Calculate SUM, AVG, COUNT, etc.', 'Analytics, reporting');
-- ... continue for all 20+ operations
```

### Insert General Importance

```sql
INSERT INTO operation_importance_general (operation_id, importance_metric_id, raw_value, raw_unit, normalized_importance, rationale)
VALUES
((SELECT id FROM operations WHERE operation_name = 'query_point_lookup'),
 (SELECT id FROM importance_metrics WHERE metric_name = 'frequency'),
 95, '%', 95,
 'Used in 95% of deployments - nearly universal'),

((SELECT id FROM operations WHERE operation_name = 'query_point_lookup'),
 (SELECT id FROM importance_metrics WHERE metric_name = 'criticality'),
 5, '1-5 scale', 100,
 'System unusable if queries fail'),

((SELECT id FROM operations WHERE operation_name = 'insert_bulk'),
 (SELECT id FROM importance_metrics WHERE metric_name = 'frequency'),
 20, '%', 20,
 'Used in only 20% of deployments'),

((SELECT id FROM operations WHERE operation_name = 'transaction_commit'),
 (SELECT id FROM importance_metrics WHERE metric_name = 'criticality'),
 4.5, '1-5 scale', 90,
 'Very critical for data integrity');
-- ... continue for all operations × metrics
```

### Insert Project Context and Overrides

```sql
INSERT INTO project_contexts (project_name, description, project_type, priority_focus)
VALUES
('HighThroughputAPI', 'High-volume API serving millions of queries/sec', 'high_throughput', 'Speed and bulk operations'),
('FinancialLedger', 'Financial transaction processing system', 'financial_system', 'Consistency and data integrity'),
('RealTimeAnalytics', 'Real-time analytics and aggregations', 'real_time_analytics', 'Query variants and aggregations'),
('GraphAISystem', 'AI system using knowledge graphs', 'graph_based_ai', 'Semantic search and graph traversal');

-- Project-specific overrides
INSERT INTO project_operation_importance (project_id, operation_id, importance_metric_id, raw_value, normalized_importance, override_general, rationale)
VALUES
((SELECT id FROM project_contexts WHERE project_name = 'HighThroughputAPI'),
 (SELECT id FROM operations WHERE operation_name = 'insert_bulk'),
 (SELECT id FROM importance_metrics WHERE metric_name = 'frequency'),
 95, 95, 1,
 'Critical for this project - bulk inserts are 95% of workload'),

((SELECT id FROM project_contexts WHERE project_name = 'FinancialLedger'),
 (SELECT id FROM operations WHERE operation_name = 'transaction_commit'),
 (SELECT id FROM importance_metrics WHERE metric_name = 'criticality'),
 5, 100, 1,
 'Absolute requirement - cannot skip or delay transactions');
```

---

## Query Examples

### Get Weighted Scores for a Project

```sql
-- What's the best avenue for HighThroughputAPI?
SELECT
  avenue_type,
  operation_name,
  performance_score,
  importance_score,
  weighted_score,
  rank_for_operation
FROM weighted_operation_scores
WHERE project_name = 'HighThroughputAPI'
ORDER BY weighted_score DESC
LIMIT 20;
```

### Compare Projects' Priorities

```sql
-- How does importance differ between projects for same operation?
SELECT
  p.project_name,
  o.operation_name,
  poi.normalized_importance as project_importance,
  oig.normalized_importance as general_importance,
  (poi.normalized_importance - oig.normalized_importance) as difference
FROM project_operation_importance poi
JOIN project_contexts p ON poi.project_id = p.id
JOIN operations o ON poi.operation_id = o.id
JOIN operation_importance_general oig ON o.id = oig.operation_id
WHERE o.operation_name = 'insert_bulk'
ORDER BY poi.normalized_importance DESC;
```

### Find Best Avenue for Project's Top Priorities

```sql
-- For FinancialLedger, what avenue is best at critical operations?
SELECT
  at.type_name,
  o.operation_name,
  ob.normalized_score as performance,
  poi.normalized_importance as importance,
  (ob.normalized_score * poi.normalized_importance / 100) as weighted_score
FROM avenue_types at
JOIN operation_benchmarks ob ON at.id = ob.avenue_type_id
JOIN operations o ON ob.operation_id = o.id
JOIN project_operation_importance poi ON o.id = poi.operation_id
JOIN project_contexts p ON poi.project_id = p.id
WHERE p.project_name = 'FinancialLedger'
  AND poi.normalized_importance > 70  -- only critical operations
ORDER BY weighted_score DESC;
```

### Create Custom Project Instance

```sql
-- New project: E-CommerceSearch
INSERT INTO project_contexts VALUES
(NULL, 'E-CommerceSearch', 'E-commerce search and discovery', 'search_platform', 'Fast search, semantic relevance');

-- Define its importance profile (overrides for key operations)
INSERT INTO project_operation_importance
SELECT
  (SELECT id FROM project_contexts WHERE project_name = 'E-CommerceSearch'),
  operation_id,
  importance_metric_id,
  raw_value * 1.2 as raw_value,  -- boost all importance by 20%
  (normalized_importance * 1.2) OVER (...) as normalized_importance,
  1 as override_general,
  'Customized for E-CommerceSearch priorities'
FROM operation_importance_general;
```

---

## Benefits of This Comprehensive Architecture

✅ **Universal Base Layer** — all operations measured the same way
✅ **Importance Dimension** — importance measured systematically, not arbitrarily
✅ **Project Customization** — each project defines what matters to them
✅ **Weighted Recommendations** — different projects get different "best" avenue from same data
✅ **Decision Support** — answers questions like "What avenue is best for FinancialLedger?"
✅ **Scenario Planning** — what if we change project priorities?
✅ **Extensible** — new operations, new projects, new importance metrics all supported
✅ **Traceable** — every recommendation backed by measurable data
✅ **Comparable** — see how projects differ in their priorities

---

## Complete Operation Taxonomy (20+ Operations)

### Read Operations (6)
- Query - Point Lookup
- Query - Range Query
- Query - Fuzzy Search
- Query - Semantic Search
- Query - Full-Text Search
- Query - Graph Traversal

### Write Operations (6)
- Insert - Single Record
- Insert - Bulk
- Update - Single Record
- Update - Bulk
- Delete - Single Record
- Delete - Bulk

### Structural Operations (4)
- Index - Create/Rebuild
- Index - Optimize/Defragment
- Rebalancing (tree/hierarchy)
- Schema Migration

### Consistency Operations (5)
- Transaction - Begin/Commit
- Rollback - Undo
- Replication - Sync
- Conflict Resolution - Merge
- Backup/Recovery

### Analytics Operations (3)
- Aggregation (SUM, AVG, COUNT)
- Join - Multi-source
- Grouping - GROUP BY

---

## Next Steps

1. **Populate OPERATIONS** — add all 20+ operations with hierarchy
2. **Define IMPORTANCE_METRICS** — all 8 importance dimensions
3. **Insert OPERATION_IMPORTANCE_GENERAL** — base importance for all projects
4. **Create PROJECT_CONTEXTS** — sample projects (HighThroughput, Financial, Analytics, GraphAI)
5. **Define PROJECT_OPERATION_IMPORTANCE** — customizations per project
6. **Create WEIGHTED_OPERATION_SCORES view** — enable project-specific recommendations
7. **Test queries** — verify customization works correctly
8. **Extend for future projects** — add new project contexts as needed

---

## Summary

This v5 proposal creates a **fully parameterizable database** where:
- **Base layer** = comprehensive operations + metrics + benchmarks (universal)
- **Customization layer** = project-specific importance weights (flexible)
- **Recommendation layer** = weighted scores that change per project (dynamic)

Different projects, different needs, same data. Projects can be added anytime with custom importance profiles, and the database automatically computes which avenue is best for that project.
