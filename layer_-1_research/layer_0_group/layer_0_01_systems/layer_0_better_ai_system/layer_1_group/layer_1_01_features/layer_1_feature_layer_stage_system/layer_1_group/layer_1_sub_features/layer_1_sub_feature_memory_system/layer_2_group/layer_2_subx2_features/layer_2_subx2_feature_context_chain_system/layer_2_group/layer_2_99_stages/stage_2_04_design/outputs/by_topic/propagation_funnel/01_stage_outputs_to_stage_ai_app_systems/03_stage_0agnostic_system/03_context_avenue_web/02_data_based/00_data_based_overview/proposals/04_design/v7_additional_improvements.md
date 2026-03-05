---
resource_id: "1989d867-e591-486b-86d5-6a2e194391dd"
resource_type: "output"
resource_name: "v7_additional_improvements"
---
# Context Avenue Database Schema — Proposal v7

## Additional Improvements (5 New Tables)

This proposal extends v6 with 5 additional tables that strengthen decision-making without restructuring the existing schema. These can be added incrementally after v6 is implemented.

---

## New Table Index

| # | Table | Purpose | Priority |
|---|-------|---------|----------|
| 18 | capability_tradeoffs | Model tensions between capabilities | Medium |
| 19 | avenue_maturity | Track readiness level of each avenue type | High |
| 20 | data_type_compatibility | Which data types work well with which avenue | High |
| 21 | migration_paths | Difficulty of migrating between avenue pairs | Medium |
| 22 | implementation_examples | Real-world tools implementing each avenue type | Low |

---

## 18. CAPABILITY_TRADEOFFS (Capability Dependencies/Conflicts)

Some capabilities have natural tension. Optimizing for one may degrade another.

```sql
CREATE TABLE capability_tradeoffs (
  id INTEGER PRIMARY KEY,
  capability_a_id INTEGER,
  capability_b_id INTEGER,
  relationship_type TEXT,          -- "tension", "synergy", "independent"
  strength REAL,                    -- -1.0 (strong tension) to +1.0 (strong synergy)
  description TEXT,
  example TEXT,
  FOREIGN KEY (capability_a_id) REFERENCES capabilities(id),
  FOREIGN KEY (capability_b_id) REFERENCES capabilities(id),
  UNIQUE(capability_a_id, capability_b_id)
);
```

**Example Data:**

| Capability A | Capability B | Type | Strength | Example |
|---|---|---|---|---|
| speed | comprehensiveness | tension | -0.7 | Faster retrieval often means less thorough results |
| cost | scalability | tension | -0.6 | Scaling up increases infrastructure cost |
| readability | speed | tension | -0.4 | Human-readable formats are slower to parse |
| coverage | comprehensiveness | synergy | +0.8 | Broader coverage usually means more comprehensive results |
| interpretability | reasoning | synergy | +0.6 | Interpretable structures support better reasoning |
| searchability | speed | synergy | +0.5 | Well-indexed data is both searchable and fast |

**View: Tradeoff Warnings**

```sql
CREATE VIEW tradeoff_warnings AS
SELECT
  ca.name as capability_optimized,
  cb.name as capability_affected,
  ct.relationship_type,
  ct.strength,
  ct.description
FROM capability_tradeoffs ct
JOIN capabilities ca ON ct.capability_a_id = ca.id
JOIN capabilities cb ON ct.capability_b_id = cb.id
WHERE ct.relationship_type = 'tension'
ORDER BY ct.strength ASC;
```

**Use case**: When a project says "optimize for speed", the system warns: "Expect comprehensiveness to drop (strength: -0.7) and readability to decrease (strength: -0.4)."

---

## 19. AVENUE_MATURITY (Readiness Levels)

Tracks how mature/production-ready each avenue type is, beyond just industry usage frequency.

```sql
CREATE TABLE avenue_maturity (
  id INTEGER PRIMARY KEY,
  avenue_type_id INTEGER,
  maturity_stage TEXT,              -- "emerging", "growing", "mature", "legacy"
  years_in_production INTEGER,
  ecosystem_size TEXT,              -- "small", "medium", "large", "massive"
  community_support TEXT,           -- "minimal", "growing", "strong", "extensive"
  documentation_quality TEXT,       -- "sparse", "adequate", "good", "excellent"
  enterprise_adoption TEXT,         -- "experimental", "early_adopter", "mainstream", "universal"
  risk_level TEXT,                  -- "high", "medium", "low", "minimal"
  notes TEXT,
  last_assessed TEXT,
  FOREIGN KEY (avenue_type_id) REFERENCES avenue_types(id),
  UNIQUE(avenue_type_id)
);
```

**Example Data:**

| Avenue Type | Stage | Years | Ecosystem | Enterprise | Risk |
|---|---|---|---|---|---|
| knowledge_graph | mature | 15+ | large | mainstream | low |
| shimi | emerging | <1 | small | experimental | high |
| relational_tables | mature | 40+ | massive | universal | minimal |
| vector_databases | growing | 5+ | medium | early_adopter | medium |

**Maturity Lifecycle:**
```
emerging → growing → mature → legacy
  (SHIMI)   (Vector)   (KG, SQL)   (flat files?)
```

---

## 20. DATA_TYPE_COMPATIBILITY (Data Type Matrix)

Not all avenues handle all data types equally well.

```sql
CREATE TABLE data_type_compatibility (
  id INTEGER PRIMARY KEY,
  avenue_type_id INTEGER,
  data_type TEXT,                   -- "relationships", "embeddings", "structured_records", "hierarchical", "temporal", "binary", "text", "graph"
  compatibility_level TEXT,         -- "excellent", "good", "fair", "poor", "unsupported"
  compatibility_score INTEGER,      -- 1-5 (1=poor, 5=excellent)
  notes TEXT,
  FOREIGN KEY (avenue_type_id) REFERENCES avenue_types(id)
);
```

**Example Data:**

| Avenue | Relationships | Embeddings | Structured Records | Hierarchical | Temporal | Text |
|---|---|---|---|---|---|---|
| knowledge_graph | excellent (5) | poor (1) | fair (3) | excellent (5) | fair (3) | good (4) |
| shimi | good (4) | fair (3) | fair (3) | excellent (5) | good (4) | good (4) |
| relational_tables | fair (3) | poor (1) | excellent (5) | fair (3) | good (4) | fair (3) |
| vector_databases | poor (1) | excellent (5) | poor (1) | poor (1) | fair (3) | good (4) |

**View: Best Avenue for Data Type**

```sql
CREATE VIEW best_avenue_for_data_type AS
SELECT
  dtc.data_type,
  at.type_name as avenue_type,
  dtc.compatibility_score,
  dtc.compatibility_level,
  RANK() OVER (PARTITION BY dtc.data_type ORDER BY dtc.compatibility_score DESC) as rank_for_type
FROM data_type_compatibility dtc
JOIN avenue_types at ON dtc.avenue_type_id = at.id
ORDER BY dtc.data_type, rank_for_type;
```

**Use case**: "My data is mostly relationships and hierarchical structures" -> "Knowledge Graph is your best fit (score 5+5=10), SHIMI is second (4+5=9)."

---

## 21. MIGRATION_PATHS (Migration Difficulty Between Avenues)

If a project starts with one avenue and needs to migrate to another, how hard is that?

```sql
CREATE TABLE migration_paths (
  id INTEGER PRIMARY KEY,
  source_avenue_type_id INTEGER,
  target_avenue_type_id INTEGER,
  difficulty_level TEXT,            -- "trivial", "easy", "moderate", "hard", "very_hard"
  difficulty_score INTEGER,         -- 1-5 (1=trivial, 5=very_hard)
  estimated_effort TEXT,            -- "hours", "days", "weeks", "months"
  data_loss_risk TEXT,              -- "none", "minimal", "some", "significant"
  tooling_available BOOLEAN,
  migration_strategy TEXT,
  key_challenges TEXT,
  FOREIGN KEY (source_avenue_type_id) REFERENCES avenue_types(id),
  FOREIGN KEY (target_avenue_type_id) REFERENCES avenue_types(id),
  UNIQUE(source_avenue_type_id, target_avenue_type_id)
);
```

**Example Data:**

| From | To | Difficulty | Effort | Data Loss Risk | Strategy |
|---|---|---|---|---|---|
| relational_tables | vector_databases | moderate (3) | weeks | minimal | Generate embeddings from structured fields, batch import |
| relational_tables | knowledge_graph | hard (4) | weeks | some | Extract relationships from foreign keys, map to ontology |
| knowledge_graph | relational_tables | moderate (3) | days | some | Flatten graph to tables, lose implicit relationships |
| vector_databases | knowledge_graph | hard (4) | weeks | significant | Reverse embeddings to entities, manually define relationships |
| knowledge_graph | shimi | easy (2) | days | none | Map ontology to hierarchical structure |
| relational_tables | shimi | moderate (3) | days | minimal | Transform normalized tables to hierarchical indices |

**View: Easiest Migration Options**

```sql
CREATE VIEW migration_options AS
SELECT
  s_at.type_name as from_avenue,
  t_at.type_name as to_avenue,
  mp.difficulty_level,
  mp.difficulty_score,
  mp.estimated_effort,
  mp.data_loss_risk,
  mp.tooling_available
FROM migration_paths mp
JOIN avenue_types s_at ON mp.source_avenue_type_id = s_at.id
JOIN avenue_types t_at ON mp.target_avenue_type_id = t_at.id
ORDER BY mp.difficulty_score ASC;
```

---

## 22. IMPLEMENTATION_EXAMPLES (Real-World Tools)

Ground abstract avenue types in concrete implementations.

```sql
CREATE TABLE implementation_examples (
  id INTEGER PRIMARY KEY,
  avenue_type_id INTEGER,
  tool_name TEXT,
  vendor TEXT,
  license_type TEXT,                -- "open_source", "commercial", "freemium", "managed_service"
  primary_language TEXT,
  notable_users TEXT,
  url TEXT,
  notes TEXT,
  FOREIGN KEY (avenue_type_id) REFERENCES avenue_types(id)
);
```

**Example Data:**

| Avenue Type | Tool | Vendor | License | Language |
|---|---|---|---|---|
| knowledge_graph | Neo4j | Neo4j Inc | freemium | Java |
| knowledge_graph | Amazon Neptune | AWS | managed_service | - |
| knowledge_graph | Apache Jena | Apache | open_source | Java |
| knowledge_graph | Stardog | Stardog | commercial | Java |
| shimi | (custom) | - | open_source | Python |
| relational_tables | PostgreSQL | Community | open_source | C |
| relational_tables | MySQL | Oracle | open_source | C/C++ |
| relational_tables | SQLite | Community | open_source | C |
| vector_databases | Pinecone | Pinecone | managed_service | - |
| vector_databases | Weaviate | Weaviate | open_source | Go |
| vector_databases | Milvus | Zilliz | open_source | Go/C++ |
| vector_databases | Chroma | Chroma | open_source | Python |
| vector_databases | pgvector | Community | open_source | C |

---

## Updated Entity Relationship Diagram (v6 + v7)

```
avenues (1) ──< avenue_types (M)
avenue_types (1) ──< capability_benchmarks (M) >── capabilities (1)
avenue_types (1) ──< operation_benchmarks (M) >── operations (1)
avenue_types (1) ──< operation_qualities (M) >── operations (1)
avenue_types (1) ──< rankings (M) >── capabilities (1)
avenue_types (1) ──< avenue_maturity (1)                          [NEW v7]
avenue_types (1) ──< data_type_compatibility (M)                  [NEW v7]
avenue_types (1) ──< migration_paths (M as source)                [NEW v7]
avenue_types (1) ──< migration_paths (M as target)                [NEW v7]
avenue_types (1) ──< implementation_examples (M)                  [NEW v7]
capabilities (1) ──< capability_metrics (1)
capabilities (1) ──< capability_tradeoffs (M as A or B)           [NEW v7]
operations (1) ──< operation_metrics (1)
operations (1) ──< operation_importance_general (M) >── importance_metrics (1)
project_contexts (1) ──< project_operation_importance (M) >── operations (1)
avenue_types (1) ──< avenue_combinations (M as primary)
avenue_types (1) ──< avenue_combinations (M as secondary)
avenue_combinations (1) ──< combination_benchmarks (M) >── capabilities (1)
```

---

## Updated Implementation Order (v7 additions)

After completing v6 steps 1-12:

13. Create table 18 (capability_tradeoffs) -- model capability tensions
14. Create table 19 (avenue_maturity) -- classify readiness levels
15. Create table 20 (data_type_compatibility) -- data type matrix
16. Create table 21 (migration_paths) -- migration difficulty between avenues
17. Create table 22 (implementation_examples) -- real-world tools
18. Create views V7-V9 (tradeoff_warnings, best_avenue_for_data_type, migration_options)
19. Populate tradeoff data -- capability tension/synergy pairs
20. Populate maturity data -- readiness level per avenue
21. Populate compatibility data -- data type scores per avenue
22. Populate migration data -- difficulty between all avenue pairs
23. Populate implementation data -- real-world tools per avenue

---

## Summary

v7 adds **5 new tables** and **3 new views** to the v6 schema:
- **capability_tradeoffs**: Model tensions/synergies between capabilities (speed vs comprehensiveness)
- **avenue_maturity**: Classify each avenue's production readiness (emerging/growing/mature/legacy)
- **data_type_compatibility**: Score each avenue's fit for different data types
- **migration_paths**: Rate migration difficulty between avenue pairs
- **implementation_examples**: Link abstract avenues to concrete tools (Neo4j, Pinecone, etc.)

**Total schema**: 22 tables + 9 views (v6's 17+6 plus v7's 5+3)
