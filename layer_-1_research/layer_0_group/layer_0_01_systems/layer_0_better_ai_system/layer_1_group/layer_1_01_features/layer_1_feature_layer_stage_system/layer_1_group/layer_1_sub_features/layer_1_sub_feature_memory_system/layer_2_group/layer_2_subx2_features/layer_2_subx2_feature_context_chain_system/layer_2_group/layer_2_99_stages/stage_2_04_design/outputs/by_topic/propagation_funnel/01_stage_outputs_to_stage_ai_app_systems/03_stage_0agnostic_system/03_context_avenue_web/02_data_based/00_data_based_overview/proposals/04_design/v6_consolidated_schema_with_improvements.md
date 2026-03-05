---
resource_id: "24ccdb73-21e6-41e0-bde3-daacd3001898"
resource_type: "output"
resource_name: "v6_consolidated_schema_with_improvements"
---
# Context Avenue Database Schema — Proposal v6

<!-- section_id: "ede0e42c-a696-4dd4-941e-d4b05eacec86" -->
## Consolidated Schema with All Improvements

This proposal merges v1-v5 into a single unified schema and adds new capabilities: file-based avenues, combination recommendations, benchmark history, and decision matrix.

---

<!-- section_id: "67abc3c9-a361-4264-b910-db640bcf2f6d" -->
## Complete Table Index

| # | Table | Purpose | Source |
|---|-------|---------|--------|
| 1 | avenues | Top-level avenue container | v1 |
| 2 | avenue_types | Data-based + file-based subtypes | v1 (enhanced) |
| 3 | capabilities | 16 evaluation metrics | v3 (enhanced) |
| 4 | capability_metrics | Measurement units and methodology | v4 |
| 5 | capability_benchmarks | Raw + normalized benchmark scores | v4 |
| 6 | operations | 24 operations with hierarchy | v2, v5 |
| 7 | operation_metrics | Measurement units for operations | v5 |
| 8 | operation_benchmarks | Raw + normalized operation performance | v5 |
| 9 | operation_qualities | Quality metrics per operation | v2 |
| 10 | importance_metrics | 8 dimensions for measuring importance | v5 |
| 11 | operation_importance_general | Base importance for all projects | v5 |
| 12 | project_contexts | Project definitions and priorities | v5 |
| 13 | project_operation_importance | Project-specific importance overrides | v5 |
| 14 | avenue_combinations | Hybrid avenue pairings | NEW |
| 15 | combination_benchmarks | Performance of avenue pairs | NEW |
| 16 | benchmark_history | Version tracking for benchmarks | NEW |
| 17 | rankings | Derived rankings (from benchmarks) | v3 (enhanced) |

**Views:**
| # | View | Purpose |
|---|------|---------|
| V1 | weighted_operation_scores | Project-specific weighted performance |
| V2 | ranking_by_capability | Avenues ranked per capability |
| V3 | decision_matrix | Final recommendation per project |
| V4 | avenue_comparison_cross_category | File-based vs data-based comparison |
| V5 | hybrid_recommendations | Best avenue combinations |
| V6 | benchmark_trends | How benchmarks change over time |

---

<!-- section_id: "082e9637-aaf0-4a81-a329-58f75e39abbe" -->
## 1. AVENUES (Top-level container)

```sql
CREATE TABLE avenues (
  id INTEGER PRIMARY KEY,
  avenue_number INTEGER UNIQUE,
  name TEXT,
  format TEXT,
  purpose TEXT,
  status TEXT
);
```

---

<!-- section_id: "5058fa59-c6ff-4f74-a4eb-46a62530df81" -->
## 2. AVENUE_TYPES (Data-based + File-based)

```sql
CREATE TABLE avenue_types (
  id INTEGER PRIMARY KEY,
  avenue_id INTEGER,
  type_name TEXT UNIQUE,
  category TEXT,                    -- "file_based" or "data_based"
  description TEXT,
  FOREIGN KEY (avenue_id) REFERENCES avenues(id)
);
```

**Data-based types:**
| type_name | description |
|---|---|
| knowledge_graph | Semantic relationships, inference engines, ontology-based |
| shimi | Semantic Hierarchical Memory Index structures |
| relational_tables | Traditional SQL, normalized schema, ACID compliance |
| vector_databases | Embedding-based similarity search, high-dimensional vectors |

**File-based types:**
| type_name | description |
|---|---|
| aalang_jsonld | JSON-LD graphs with modes, actors, personas (AALang) |
| integration_summaries | Markdown summaries of AALang files |
| skills | Claude Code skills with WHEN/WHEN NOT conditions |
| auto_memory | Auto-loaded memory files in ~/.claude/ |
| agnostic_system | .0agnostic/ numbered directories with rules, knowledge, protocols |
| parent_chain | CLAUDE.md chain from root to working directory |
| path_rules | .claude/rules/ directory with path-scoped context |
| episodic_memory | Session records, work history, continuity files |

---

<!-- section_id: "a862c06d-2611-44bd-9933-a3924b751aee" -->
## 3. CAPABILITIES (16 metrics)

```sql
CREATE TABLE capabilities (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE,
  description TEXT,
  category TEXT,
  lower_is_better BOOLEAN
);
```

*Already populated with 16 capabilities in the database.*

---

<!-- section_id: "b917b6ff-ea3e-427f-a193-5782515b2a3f" -->
## 4. CAPABILITY_METRICS (Measurement definitions)

```sql
CREATE TABLE capability_metrics (
  id INTEGER PRIMARY KEY,
  capability_id INTEGER,
  unit_of_measurement TEXT,
  measurement_methodology TEXT,
  measurement_scale_min REAL,
  measurement_scale_max REAL,
  lower_is_better BOOLEAN,
  baseline_reference TEXT,
  example_measurement TEXT,
  FOREIGN KEY (capability_id) REFERENCES capabilities(id),
  UNIQUE(capability_id)
);
```

---

<!-- section_id: "af22cda6-bc55-407c-a8d1-d20c3fbc04db" -->
## 5. CAPABILITY_BENCHMARKS (Raw + normalized scores)

```sql
CREATE TABLE capability_benchmarks (
  id INTEGER PRIMARY KEY,
  avenue_type_id INTEGER,
  capability_id INTEGER,
  raw_value REAL,
  raw_unit TEXT,
  normalized_score REAL,
  measurement_date TEXT,
  measurement_source TEXT,
  notes TEXT,
  FOREIGN KEY (avenue_type_id) REFERENCES avenue_types(id),
  FOREIGN KEY (capability_id) REFERENCES capabilities(id)
);
```

---

<!-- section_id: "0490754b-4f9a-456a-8707-3e864b12bd38" -->
## 6. OPERATIONS (24 comprehensive operations)

```sql
CREATE TABLE operations (
  id INTEGER PRIMARY KEY,
  operation_name TEXT UNIQUE,
  operation_category TEXT,
  parent_operation_id INTEGER,
  description TEXT,
  use_case TEXT,
  FOREIGN KEY (parent_operation_id) REFERENCES operations(id)
);
```

**Complete Operation List (24):**

| # | Name | Category | Parent |
|---|------|----------|--------|
| 1 | query | read | NULL (aggregate) |
| 2 | query_point_lookup | read | query |
| 3 | query_range | read | query |
| 4 | query_fuzzy_search | read | query |
| 5 | query_semantic_search | read | query |
| 6 | query_full_text_search | read | query |
| 7 | query_graph_traversal | read | query |
| 8 | insert | write | NULL (aggregate) |
| 9 | insert_single | write | insert |
| 10 | insert_bulk | write | insert |
| 11 | update | write | NULL (aggregate) |
| 12 | update_single | write | update |
| 13 | update_bulk | write | update |
| 14 | delete | write | NULL (aggregate) |
| 15 | delete_single | write | delete |
| 16 | delete_bulk | write | delete |
| 17 | index_rebuild | maintenance | NULL |
| 18 | index_optimize | maintenance | NULL |
| 19 | rebalancing | maintenance | NULL |
| 20 | schema_migration | maintenance | NULL |
| 21 | transaction_commit | consistency | NULL |
| 22 | rollback | consistency | NULL |
| 23 | replication_sync | consistency | NULL |
| 24 | conflict_resolution | consistency | NULL |
| 25 | backup_recovery | consistency | NULL |
| 26 | aggregation | analytics | NULL |
| 27 | join_multi_source | analytics | NULL |
| 28 | grouping | analytics | NULL |

---

<!-- section_id: "b662e87c-3a3e-4b11-bcae-a69a4f1eba0d" -->
## 7. OPERATION_METRICS (How to measure operations)

```sql
CREATE TABLE operation_metrics (
  id INTEGER PRIMARY KEY,
  operation_id INTEGER,
  unit_of_measurement TEXT,
  measurement_methodology TEXT,
  measurement_scale_min REAL,
  measurement_scale_max REAL,
  lower_is_better BOOLEAN,
  baseline_reference TEXT,
  FOREIGN KEY (operation_id) REFERENCES operations(id),
  UNIQUE(operation_id)
);
```

---

<!-- section_id: "dc61fe5e-e6a3-4898-a348-7fed1ceb966d" -->
## 8. OPERATION_BENCHMARKS (Operation performance data)

```sql
CREATE TABLE operation_benchmarks (
  id INTEGER PRIMARY KEY,
  avenue_type_id INTEGER,
  operation_id INTEGER,
  raw_value REAL,
  raw_unit TEXT,
  normalized_score REAL,
  calculation_rule TEXT,
  measurement_date TEXT,
  measurement_source TEXT,
  notes TEXT,
  FOREIGN KEY (avenue_type_id) REFERENCES avenue_types(id),
  FOREIGN KEY (operation_id) REFERENCES operations(id)
);
```

---

<!-- section_id: "fd062364-384f-44dd-9a34-dc682ad1f53d" -->
## 9. OPERATION_QUALITIES (Quality aspects)

```sql
CREATE TABLE operation_qualities (
  id INTEGER PRIMARY KEY,
  operation_id INTEGER,
  avenue_type_id INTEGER,
  quality_metric_name TEXT,
  quality_value REAL,
  scale TEXT,
  FOREIGN KEY (operation_id) REFERENCES operations(id),
  FOREIGN KEY (avenue_type_id) REFERENCES avenue_types(id)
);
```

---

<!-- section_id: "3b92348a-395f-47b8-8bcd-0a5f84efa4ea" -->
## 10. IMPORTANCE_METRICS (How to measure importance)

```sql
CREATE TABLE importance_metrics (
  id INTEGER PRIMARY KEY,
  metric_name TEXT UNIQUE,
  unit_of_measurement TEXT,
  measurement_methodology TEXT,
  measurement_scale_min REAL,
  measurement_scale_max REAL,
  lower_is_better BOOLEAN,
  context_type TEXT,
  description TEXT
);
```

**8 Importance Dimensions:**

| # | Metric | Unit | Methodology |
|---|--------|------|-------------|
| 1 | Frequency | % of use | % of deployments using this operation |
| 2 | Criticality | 1-5 scale | Expert rating: impact if broken (1=minor, 5=system down) |
| 3 | Cost Impact | $/query or $/month | Financial cost per operation + failure cost |
| 4 | Risk Score | 1-10 scale | (Criticality x Frequency x Cost) normalized |
| 5 | User Impact | 1-5 scale | How directly it affects end-users (1=backend, 5=direct) |
| 6 | SLA Requirement | milliseconds | Required response time (p99 or average) |
| 7 | Competitive Advantage | 1-5 scale | Strategic value if optimized (1=none, 5=major edge) |
| 8 | Technical Debt | 1-5 scale | Complexity if not optimized (1=none, 5=severe debt) |

---

<!-- section_id: "3e831a80-a5aa-484d-9bd7-c684071abf67" -->
## 11. OPERATION_IMPORTANCE_GENERAL (Base importance)

```sql
CREATE TABLE operation_importance_general (
  id INTEGER PRIMARY KEY,
  operation_id INTEGER,
  importance_metric_id INTEGER,
  raw_value REAL,
  raw_unit TEXT,
  normalized_importance REAL,
  rationale TEXT,
  FOREIGN KEY (operation_id) REFERENCES operations(id),
  FOREIGN KEY (importance_metric_id) REFERENCES importance_metrics(id)
);
```

---

<!-- section_id: "d65467d8-acf2-4bb8-9037-1525c54ed32b" -->
## 12. PROJECT_CONTEXTS (Project definitions)

```sql
CREATE TABLE project_contexts (
  id INTEGER PRIMARY KEY,
  project_name TEXT UNIQUE,
  description TEXT,
  project_type TEXT,
  priority_focus TEXT,
  created_date TEXT
);
```

---

<!-- section_id: "9e6a0bbd-2d3a-4a9b-818f-4ce5720c82ae" -->
## 13. PROJECT_OPERATION_IMPORTANCE (Project-specific overrides)

```sql
CREATE TABLE project_operation_importance (
  id INTEGER PRIMARY KEY,
  project_id INTEGER,
  operation_id INTEGER,
  importance_metric_id INTEGER,
  raw_value REAL,
  raw_unit TEXT,
  normalized_importance REAL,
  rationale TEXT,
  override_general BOOLEAN,
  FOREIGN KEY (project_id) REFERENCES project_contexts(id),
  FOREIGN KEY (operation_id) REFERENCES operations(id),
  FOREIGN KEY (importance_metric_id) REFERENCES importance_metrics(id)
);
```

---

<!-- section_id: "a7ce1885-35c1-4175-843e-77cfe61c227d" -->
## 14. AVENUE_COMBINATIONS (NEW - Hybrid pairings)

```sql
CREATE TABLE avenue_combinations (
  id INTEGER PRIMARY KEY,
  primary_avenue_type_id INTEGER,
  secondary_avenue_type_id INTEGER,
  combination_name TEXT,
  rationale TEXT,
  synergy_description TEXT,
  FOREIGN KEY (primary_avenue_type_id) REFERENCES avenue_types(id),
  FOREIGN KEY (secondary_avenue_type_id) REFERENCES avenue_types(id)
);
```

**Example Combinations:**
| Primary | Secondary | Rationale |
|---|---|---|
| vector_databases | knowledge_graph | Vector for speed + KG for reasoning |
| relational_tables | vector_databases | Relational for ACID + Vector for search |
| knowledge_graph | relational_tables | KG for relationships + Relational for structured data |
| shimi | vector_databases | SHIMI for hierarchy + Vector for similarity |

---

<!-- section_id: "90fca74e-3906-4169-b6b1-f9c402738fc5" -->
## 15. COMBINATION_BENCHMARKS (NEW - Hybrid performance)

```sql
CREATE TABLE combination_benchmarks (
  id INTEGER PRIMARY KEY,
  combination_id INTEGER,
  capability_id INTEGER,
  combined_score REAL,
  improvement_over_primary REAL,
  improvement_over_secondary REAL,
  notes TEXT,
  FOREIGN KEY (combination_id) REFERENCES avenue_combinations(id),
  FOREIGN KEY (capability_id) REFERENCES capabilities(id)
);
```

---

<!-- section_id: "f7e974f5-e510-4fc9-bbb5-609f4d957ca6" -->
## 16. BENCHMARK_HISTORY (NEW - Version tracking)

```sql
CREATE TABLE benchmark_history (
  id INTEGER PRIMARY KEY,
  benchmark_type TEXT,             -- "capability" or "operation"
  benchmark_id INTEGER,
  old_value REAL,
  new_value REAL,
  old_normalized REAL,
  new_normalized REAL,
  changed_date TEXT,
  reason TEXT,
  changed_by TEXT
);
```

---

<!-- section_id: "8d354470-d9e3-482e-9fd6-1085430b878d" -->
## 17. RANKINGS (Derived from benchmarks)

```sql
CREATE TABLE rankings (
  id INTEGER PRIMARY KEY,
  avenue_type_id INTEGER,
  capability_id INTEGER,
  rank_place INTEGER,
  score REAL,
  notes TEXT,
  FOREIGN KEY (avenue_type_id) REFERENCES avenue_types(id),
  FOREIGN KEY (capability_id) REFERENCES capabilities(id)
);
```

*Rankings are computed from capability_benchmarks.normalized_score ORDER BY DESC.*

---

<!-- section_id: "b18965ec-8d9e-462c-acfb-61c11ecc9089" -->
## Views

<!-- section_id: "edb542ae-797a-4101-aac0-6024a50c1a36" -->
### V1: Weighted Operation Scores (Project-specific)

```sql
CREATE VIEW weighted_operation_scores AS
SELECT
  p.project_name,
  at.type_name as avenue_type,
  o.operation_name,
  ob.normalized_score as performance_score,
  COALESCE(poi.normalized_importance, oig.normalized_importance) as importance_score,
  (ob.normalized_score * COALESCE(poi.normalized_importance, oig.normalized_importance) / 100) as weighted_score
FROM project_contexts p
CROSS JOIN avenue_types at
CROSS JOIN operations o
LEFT JOIN operation_benchmarks ob ON at.id = ob.avenue_type_id AND o.id = ob.operation_id
LEFT JOIN operation_importance_general oig ON o.id = oig.operation_id
LEFT JOIN project_operation_importance poi ON p.id = poi.project_id AND o.id = poi.operation_id
WHERE ob.normalized_score IS NOT NULL
ORDER BY p.project_name, weighted_score DESC;
```

<!-- section_id: "b75fbc0b-cd52-4dc8-909f-40f2ef1e7366" -->
### V2: Ranking by Capability

```sql
CREATE VIEW ranking_by_capability AS
SELECT
  c.name as capability,
  at.type_name as avenue_type,
  cb.raw_value,
  cb.raw_unit,
  cb.normalized_score,
  RANK() OVER (PARTITION BY c.id ORDER BY
    CASE WHEN c.lower_is_better THEN -cb.normalized_score ELSE cb.normalized_score END DESC
  ) as rank_place
FROM capability_benchmarks cb
JOIN avenue_types at ON cb.avenue_type_id = at.id
JOIN capabilities c ON cb.capability_id = c.id
ORDER BY c.name, rank_place;
```

<!-- section_id: "e15a21cf-d780-473a-8944-32aed621d8d6" -->
### V3: Decision Matrix (Final recommendation per project)

```sql
CREATE VIEW decision_matrix AS
SELECT
  project_name,
  avenue_type,
  ROUND(AVG(weighted_score), 2) as avg_weighted_score,
  RANK() OVER (PARTITION BY project_name ORDER BY AVG(weighted_score) DESC) as recommendation_rank
FROM weighted_operation_scores
GROUP BY project_name, avenue_type
ORDER BY project_name, recommendation_rank;
```

**Example Output:**
```
| project_name       | avenue_type        | avg_weighted_score | recommendation_rank |
|--------------------|--------------------|-------------------|---------------------|
| HighThroughputAPI  | vector_databases   | 87.3              | 1                   |
| HighThroughputAPI  | relational_tables  | 78.1              | 2                   |
| FinancialLedger    | relational_tables  | 92.4              | 1                   |
| FinancialLedger    | knowledge_graph    | 71.2              | 2                   |
| GraphAISystem      | knowledge_graph    | 89.1              | 1                   |
| GraphAISystem      | shimi              | 76.5              | 2                   |
```

<!-- section_id: "b1240743-dc45-4cd5-9a19-3a725d8c3382" -->
### V4: Cross-Category Comparison (File vs Data)

```sql
CREATE VIEW avenue_comparison_cross_category AS
SELECT
  at.category,
  at.type_name,
  c.name as capability,
  cb.normalized_score,
  RANK() OVER (PARTITION BY c.id ORDER BY cb.normalized_score DESC) as overall_rank
FROM capability_benchmarks cb
JOIN avenue_types at ON cb.avenue_type_id = at.id
JOIN capabilities c ON cb.capability_id = c.id
ORDER BY c.name, overall_rank;
```

<!-- section_id: "2b99263b-9798-441a-9b58-70a8373a6616" -->
### V5: Hybrid Recommendations

```sql
CREATE VIEW hybrid_recommendations AS
SELECT
  ac.combination_name,
  c.name as capability,
  cb.combined_score,
  cb.improvement_over_primary,
  cb.improvement_over_secondary,
  p_at.type_name as primary_avenue,
  s_at.type_name as secondary_avenue
FROM combination_benchmarks cb
JOIN avenue_combinations ac ON cb.combination_id = ac.id
JOIN capabilities c ON cb.capability_id = c.id
JOIN avenue_types p_at ON ac.primary_avenue_type_id = p_at.id
JOIN avenue_types s_at ON ac.secondary_avenue_type_id = s_at.id
ORDER BY cb.combined_score DESC;
```

<!-- section_id: "7aed34b1-a429-4458-9815-3df066f4b6ab" -->
### V6: Benchmark Trends

```sql
CREATE VIEW benchmark_trends AS
SELECT
  benchmark_type,
  benchmark_id,
  old_value,
  new_value,
  ROUND((new_value - old_value) / old_value * 100, 2) as percent_change,
  changed_date,
  reason
FROM benchmark_history
ORDER BY changed_date DESC;
```

---

<!-- section_id: "2d03839c-61ff-449e-a50c-a685490d8223" -->
## Entity Relationship Diagram

```
avenues (1) ──< avenue_types (M)
avenue_types (1) ──< capability_benchmarks (M) >── capabilities (1)
avenue_types (1) ──< operation_benchmarks (M) >── operations (1)
avenue_types (1) ──< operation_qualities (M) >── operations (1)
avenue_types (1) ──< rankings (M) >── capabilities (1)
capabilities (1) ──< capability_metrics (1)
operations (1) ──< operation_metrics (1)
operations (1) ──< operation_importance_general (M) >── importance_metrics (1)
project_contexts (1) ──< project_operation_importance (M) >── operations (1)
avenue_types (1) ──< avenue_combinations (M as primary)
avenue_types (1) ──< avenue_combinations (M as secondary)
avenue_combinations (1) ──< combination_benchmarks (M) >── capabilities (1)
```

---

<!-- section_id: "41c4f1fb-8e70-47e3-a3d7-aa25af233dea" -->
## Implementation Order

1. Create tables 1-3 (avenues, avenue_types, capabilities) — foundation
2. Create tables 4-5 (capability_metrics, capability_benchmarks) — measurement layer
3. Create table 6 (operations) — operation taxonomy
4. Create tables 7-9 (operation_metrics, operation_benchmarks, operation_qualities) — operation measurement
5. Create tables 10-13 (importance system) — weighting layer
6. Create tables 14-16 (combinations, history) — advanced features
7. Create table 17 (rankings) — derived data
8. Create views V1-V6 — query perspectives
9. Populate base data — avenues, capabilities, operations
10. Populate benchmarks — capability and operation benchmarks
11. Populate importance — general and project-specific weights
12. Test queries — validate all views return correct results

---

<!-- section_id: "f5462cec-7d6b-4ad6-8a2e-eb817829458f" -->
## Summary

This v6 consolidates all previous proposals into a single implementable schema:
- **17 tables** covering avenues, capabilities, operations, importance, combinations, history
- **6 views** for different analysis perspectives
- **12 avenue types** (4 data-based + 8 file-based)
- **16 capabilities** with measurement units
- **28 operations** with hierarchical aggregation
- **8 importance dimensions** with project customization
- **Hybrid recommendations** for combined avenue strategies
- **Benchmark history** for version tracking
- **Decision matrix** for project-specific final recommendations
