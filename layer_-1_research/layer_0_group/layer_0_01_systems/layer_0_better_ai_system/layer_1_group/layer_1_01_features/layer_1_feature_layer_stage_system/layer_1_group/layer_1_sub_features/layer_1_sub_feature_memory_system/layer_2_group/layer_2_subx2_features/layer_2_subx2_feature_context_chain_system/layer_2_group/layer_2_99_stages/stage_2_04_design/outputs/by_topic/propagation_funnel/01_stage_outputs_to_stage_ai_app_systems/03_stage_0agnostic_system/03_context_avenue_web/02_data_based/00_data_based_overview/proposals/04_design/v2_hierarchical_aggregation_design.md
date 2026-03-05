---
resource_id: "a94b8fd2-35b8-40fb-986b-46a7f1e3ea6b"
resource_type: "output"
resource_name: "v2_hierarchical_aggregation_design"
---
# Context Avenue Database Schema — Proposal v2

## Improved Design: Hierarchical Aggregation with Flat Tables

This proposal refines the avenues.db schema to support:
1. **Hierarchical operations** (Query with sub-operations: Retrieval, Read)
2. **Composite metrics** (Overall Query Speed = function of Retrieval Speed + Read Speed)
3. **Flat SQL structure** (consistent columns, proper normalization)
4. **Expanded capabilities** (16 total metrics for comprehensive analysis)

---

## Core Design Principle

Operations are organized hierarchically but stored in a **flat table structure** using `parent_operation_id` foreign keys. This allows:
- Component operations (query_retrieval, query_read) with individual metrics
- Aggregate operations (query overall) with composite metrics
- SQL tables with consistent schema across all rows

---

## Database Schema

### 1. AVENUES (Top-level container)

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

**Data:**
- AALang (JSON-LD)
- Integration Summaries (File-based)
- Skills (File-based)
- Auto Memory (File-based)

---

### 2. AVENUE_TYPES (Organization)

```sql
CREATE TABLE avenue_types (
  id INTEGER PRIMARY KEY,
  avenue_id INTEGER,
  type_name TEXT,                -- "knowledge_graph", "shimi", "relational_tables", "vector_databases"
  category TEXT,                 -- "file_based" or "data_based"
  description TEXT,
  FOREIGN KEY (avenue_id) REFERENCES avenues(id)
);
```

**Data-based types:**
- Knowledge Graph
- SHIMI (Semantic Hierarchical Memory Index)
- Relational Tables
- Vector Databases

---

### 3. OPERATIONS (Hierarchical with flat structure)

```sql
CREATE TABLE operations (
  id INTEGER PRIMARY KEY,
  avenue_type_id INTEGER,
  operation_name TEXT,           -- "query", "query_retrieval", "query_read", "insert_write", etc.
  operation_type TEXT,           -- "aggregate" or "specific"
  parent_operation_id INTEGER,   -- NULL for top-level, points to parent for sub-ops
  category TEXT,                 -- "read" or "write"
  FOREIGN KEY (avenue_type_id) REFERENCES avenue_types(id),
  FOREIGN KEY (parent_operation_id) REFERENCES operations(id)
);
```

**Hierarchy Example:**
```
query (aggregate)
├── query_retrieval (specific)
├── query_read (specific)

insert (aggregate)
└── insert_write (specific)

update (aggregate)
└── update_write (specific)

delete (aggregate)
└── delete_write (specific)
```

---

### 4. OPERATION_SPEEDS (Performance metrics)

```sql
CREATE TABLE operation_speeds (
  id INTEGER PRIMARY KEY,
  operation_id INTEGER,
  speed_metric_name TEXT,        -- "retrieval_speed", "read_speed", "write_speed", "overall_query_speed"
  speed_value REAL,              -- numeric value
  unit TEXT,                     -- "ms", "ops/sec", "MB/s"
  calculation_rule TEXT,         -- NULL for measured, "sum(child1,child2)" for aggregates
  FOREIGN KEY (operation_id) REFERENCES operations(id)
);
```

**Metrics:**
- retrieval_speed (ms)
- read_speed (ms)
- write_speed (ms)
- overall_query_speed (composite: retrieval + read)
- overall_insert_speed (composite: write latency)

---

### 5. OPERATION_QUALITIES (Quality aspects)

```sql
CREATE TABLE operation_qualities (
  id INTEGER PRIMARY KEY,
  operation_id INTEGER,
  quality_metric_name TEXT,      -- application-specific quality measures
  quality_value REAL,
  scale TEXT,                    -- "1-5", "0-100", "yes/no"
  FOREIGN KEY (operation_id) REFERENCES operations(id)
);
```

---

### 6. CAPABILITIES (Expanded from 8 to 16)

```sql
CREATE TABLE capabilities (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE,
  description TEXT,
  category TEXT,                 -- "performance", "usability", "maintainability", "industry", etc.
  lower_is_better BOOLEAN        -- TRUE if lower values are better (e.g., cost, setup_difficulty)
);
```

**Original capabilities (8):**
- Speed (retrieval/read/write performance)
- Coverage (% information available)
- Readability (ease of parsing, 1-5)
- Redundancy (backup availability)
- Updateability (ease to modify, minutes)
- Searchability (quick content discovery)
- Dependency (tool integration required)
- Freshness (auto-sync frequency, days)

**New capabilities (8):**
- Interpretability (how easy to understand/reason about)
- Setup Difficulty (effort to implement, 1-5 scale)
- Maintenance Difficulty (effort to maintain, 1-5 scale)
- Reasoning Capability (quality of logical inference, 1-5)
- Comprehensiveness (depth and breadth of coverage, %)
- Cost (implementation/operational cost, $ or 1-5)
- Scalability (ability to grow/expand, 1-5)
- Use Frequency in Industry (how widely adopted, %)

---

### 7. RANKINGS (Maps avenues to capabilities)

```sql
CREATE TABLE rankings (
  id INTEGER PRIMARY KEY,
  avenue_type_id INTEGER,
  capability_id INTEGER,
  rank_place INTEGER,            -- 1st, 2nd, 3rd, 4th place
  score REAL,                    -- optional numeric score
  notes TEXT,
  FOREIGN KEY (avenue_type_id) REFERENCES avenue_types(id),
  FOREIGN KEY (capability_id) REFERENCES capabilities(id)
);
```

---

## Views for Different Perspectives

### View 1: By Reasoning Capability (highest → lowest)

```sql
CREATE VIEW avenues_by_reasoning AS
SELECT
  at.type_name,
  c.name as capability,
  r.rank_place,
  r.score
FROM rankings r
JOIN avenue_types at ON r.avenue_type_id = at.id
JOIN capabilities c ON r.capability_id = c.id
WHERE c.name = 'Reasoning Capability'
ORDER BY r.rank_place ASC;
```

### View 2: By Usage Frequency in Industry (highest → lowest)

```sql
CREATE VIEW avenues_by_industry_usage AS
SELECT
  at.type_name,
  c.name as capability,
  r.rank_place,
  r.score
FROM rankings r
JOIN avenue_types at ON r.avenue_type_id = at.id
JOIN capabilities c ON r.capability_id = c.id
WHERE c.name = 'Use Frequency in Industry'
ORDER BY r.rank_place ASC;
```

### View 3: By Cost (lowest → highest)

```sql
CREATE VIEW avenues_by_cost AS
SELECT
  at.type_name,
  c.name as capability,
  r.rank_place,
  r.score
FROM rankings r
JOIN avenue_types at ON r.avenue_type_id = at.id
JOIN capabilities c ON r.capability_id = c.id
WHERE c.name = 'Cost'
ORDER BY r.rank_place ASC;
```

### View 4: By Scalability (highest → lowest)

```sql
CREATE VIEW avenues_by_scalability AS
SELECT
  at.type_name,
  c.name as capability,
  r.rank_place,
  r.score
FROM rankings r
JOIN avenue_types at ON r.avenue_type_id = at.id
JOIN capabilities c ON r.capability_id = c.id
WHERE c.name = 'Scalability'
ORDER BY r.rank_place ASC;
```

---

## Query Examples

### Get overall query speed for Knowledge Graph

```sql
SELECT os.speed_value, os.unit
FROM operation_speeds os
JOIN operations o ON os.operation_id = o.id
WHERE o.operation_name = 'query'
  AND os.speed_metric_name = 'overall_query_speed'
  AND o.avenue_type_id = (
    SELECT id FROM avenue_types WHERE type_name = 'knowledge_graph'
  );
```

### Get component speeds that make up Query

```sql
SELECT os.speed_metric_name, os.speed_value, os.unit
FROM operation_speeds os
JOIN operations o ON os.operation_id = o.id
WHERE o.parent_operation_id = (
  SELECT id FROM operations WHERE operation_name = 'query'
);
```

### Compare all avenue types on Reasoning Capability

```sql
SELECT
  at.type_name,
  c.name as capability,
  r.rank_place,
  r.score
FROM rankings r
JOIN avenue_types at ON r.avenue_type_id = at.id
JOIN capabilities c ON r.capability_id = c.id
WHERE c.name = 'Reasoning Capability'
ORDER BY r.rank_place;
```

### Find fastest Query operations across all avenues

```sql
SELECT
  at.type_name,
  o.operation_name,
  os.speed_value,
  os.unit
FROM operation_speeds os
JOIN operations o ON os.operation_id = o.id
JOIN avenue_types at ON o.avenue_type_id = at.id
WHERE o.operation_name LIKE '%query%'
  AND os.speed_metric_name LIKE '%speed%'
ORDER BY os.speed_value ASC;
```

---

## Key Design Benefits

1. **Flat SQL structure** — all rows have consistent columns (SQL normalization)
2. **Hierarchical relationships** — parent_operation_id enables tree structure
3. **Composite metrics** — aggregate operations show how components combine
4. **Comprehensive capability coverage** — 16 metrics for deep analysis
5. **Multiple perspectives** — views for different sorting/ranking needs
6. **Queryable and extensible** — easy to add new metrics, operations, or capabilities
7. **Normalized and efficient** — proper foreign keys, no data redundancy

---

## Migration Path

From current avenues.db:
1. Create new tables (avenues, avenue_types, operations, operation_speeds, operation_qualities, capabilities, rankings)
2. Migrate existing data:
   - Current `avenues` → new `avenues` table
   - Create `avenue_types` entries (knowledge_graph, shimi, relational_tables, vector_databases)
   - Create `operations` with hierarchy (query + query_retrieval, query_read, etc.)
   - Migrate/enhance `capabilities` with new 8 metrics
   - Migrate/enhance `rankings` to new structure
3. Create views for different perspectives
4. Test queries

---

## Next Steps

Ready for:
1. SQL implementation
2. Data migration from current avenues.db
3. SQLite Viewer testing (v2 schema + views)
4. Validation of hierarchical aggregation calculations
