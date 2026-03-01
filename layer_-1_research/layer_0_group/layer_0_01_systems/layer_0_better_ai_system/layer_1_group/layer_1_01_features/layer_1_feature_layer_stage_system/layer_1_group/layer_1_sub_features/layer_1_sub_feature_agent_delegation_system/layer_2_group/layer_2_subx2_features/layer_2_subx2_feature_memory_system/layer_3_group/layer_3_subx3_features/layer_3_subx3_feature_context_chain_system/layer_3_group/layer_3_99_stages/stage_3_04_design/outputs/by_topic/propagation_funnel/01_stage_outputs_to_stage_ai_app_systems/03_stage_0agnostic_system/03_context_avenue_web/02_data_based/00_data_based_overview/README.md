# Data-Based Avenues (09-13) — Optional

## Overview

The data-based avenues (09-13) are **optional, derived structures** that enhance the file-based avenues with structured data, semantic search, and temporal tracking.

**Important**: Data-based avenues are:
- **Optional** — not required for core operation
- **Derived** — generated FROM file-based avenue content
- **Regenerable** — can be recreated from source files
- **Specialized** — for semantic search, relational queries, and optimization

## Ordering Principle: Most Detailed → Optimization

Data-based avenues are ordered from most comprehensive to most specialized:

```
09 Knowledge Graph
      ↓ (structured relations)
10 Relational Tables (SQL)
      ↓ (optimization primitives)
13 SHIMI Structures
      ↓ (semantic similarity)
11 Vector Embeddings
      ↓ (temporal versioning — wraps all above)
12 Temporal Index
```

## The Five Data-Based Avenues

### Avenue 09: Knowledge Graph — Most Detailed

**Format**: JSON graph structure with typed edges

**Comprehensiveness**: Most detailed

**Purpose**: Semantic relationships between concepts and entities

**Structure**:
```json
{
  "nodes": [
    {"id": "context-chain", "type": "concept", "label": "Context Chain System"},
    {"id": "static-context", "type": "concept", "label": "Static Context"}
  ],
  "edges": [
    {"source": "context-chain", "target": "static-context", "type": "contains", "weight": 1.0},
    {"source": "context-chain", "target": "dynamic-context", "type": "composed_of", "weight": 1.0}
  ]
}
```

**Use case**: Answer relationship questions
- "What does context-chain contain?"
- "What concepts relate to memory?"
- "What are the dependencies of stage_01?"

### Avenue 10: Relational Tables (SQL) — Structured Data

**Format**: SQL schema with tables, columns, relationships

**Comprehensiveness**: Structured, queryable

**Purpose**: Tabular metadata with relational queries

**Structure**:
```sql
CREATE TABLE entities (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  layer INT,
  type VARCHAR(50),
  status VARCHAR(50)
);

CREATE TABLE relationships (
  source_id INT,
  target_id INT,
  relationship_type VARCHAR(50),
  FOREIGN KEY (source_id) REFERENCES entities(id)
);
```

**Example data**:
```
| id | name | layer | type | status |
|----|------|-------|------|--------|
| 1 | context_chain_system | 3 | SubFeature | active |
| 2 | memory_system | 2 | SubFeature | active |
```

**Use case**: Answer structural questions
- "What entities are in layer 3?"
- "How many subfeatures are active?"
- "What's the relationship between X and Y?"
- Fast SQL queries across all entities

#### SQL Storage in Markdown: Practical Implementation

SQL schemas, queries, and results can be stored directly in markdown files and executed using SQLite or other database tools.

**File Structure Example**:

```
10_relational_tables/
├── schema.md              ← SQL schema definitions (markdown code blocks)
├── schema.sql             ← Executable SQL schema file
├── queries.md             ← Example queries with documentation
├── queries/               ← Individual executable query files
│   ├── 01_entities_by_layer.sql
│   ├── 02_active_subfeatures.sql
│   └── 03_hierarchy_depth.sql
└── results/               ← Generated query results (markdown or JSON)
    ├── entities_summary.md
    ├── active_status_breakdown.md
    └── latest_snapshot.json
```

**Markdown + SQL Workflow**:

1. **Schema Definition** (markdown + SQL file):

```markdown
## Database Schema

Create tables that map the layer-stage system structure:

### Entities Table
\`\`\`sql
CREATE TABLE entities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  layer INTEGER,
  type TEXT,
  parent_id INTEGER,
  status TEXT,
  created_date DATE,
  last_updated DATE,
  FOREIGN KEY (parent_id) REFERENCES entities(id)
);
\`\`\`

### Stages Table
\`\`\`sql
CREATE TABLE stages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  entity_id INTEGER,
  stage_number INTEGER,
  stage_name TEXT,
  status TEXT,
  completed_date DATE,
  FOREIGN KEY (entity_id) REFERENCES entities(id)
);
\`\`\`

### Context Metrics Table
\`\`\`sql
CREATE TABLE context_metrics (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  entity_id INTEGER,
  avenue_id INTEGER,
  context_tokens INTEGER,
  cache_ttl_seconds INTEGER,
  priority TEXT,
  refresh_trigger TEXT,
  last_refreshed DATETIME,
  FOREIGN KEY (entity_id) REFERENCES entities(id)
);
\`\`\`
```

2. **Example Queries** (markdown with documentation):

```markdown
## Common Queries

### Query 1: List All Active Entities by Layer
\`\`\`sql
SELECT
  layer,
  type,
  COUNT(*) as count,
  SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) as active_count
FROM entities
GROUP BY layer, type
ORDER BY layer, type;
\`\`\`

**Use case**: Understand entity distribution across layers
**Expected columns**: layer, type, count, active_count
**Time complexity**: O(n) scan + sort

### Query 2: Hierarchy Depth Analysis
\`\`\`sql
WITH RECURSIVE hierarchy_depth AS (
  SELECT id, name, parent_id, 0 as depth
  FROM entities
  WHERE parent_id IS NULL

  UNION ALL

  SELECT e.id, e.name, e.parent_id, hd.depth + 1
  FROM entities e
  JOIN hierarchy_depth hd ON e.parent_id = hd.id
)
SELECT depth, COUNT(*) as entities_at_depth
FROM hierarchy_depth
GROUP BY depth
ORDER BY depth;
\`\`\`

**Use case**: Understand nesting depth distribution
**Note**: Uses recursive CTE for hierarchical traversal

### Query 3: Stage Completion Status
\`\`\`sql
SELECT
  e.name as entity,
  s.stage_number,
  s.stage_name,
  CASE
    WHEN s.status = 'completed' THEN '✓'
    WHEN s.status = 'active' THEN '◈'
    WHEN s.status = 'blocked' THEN '✗'
    ELSE '○'
  END as status_icon,
  s.completed_date
FROM entities e
JOIN stages s ON e.id = s.entity_id
WHERE e.status = 'active'
ORDER BY e.layer, s.stage_number;
\`\`\`

**Use case**: Track stage completion across active entities
**Output**: Timeline view of progress
```

3. **Generated Results** (stored as markdown table or JSON):

```markdown
## Query Results (Generated: 2026-02-26)

### Entities Summary
| Layer | Type | Total | Active | Scaffolded | Complete |
|-------|------|-------|--------|-----------|----------|
| 0 | Feature | 3 | 3 | 0 | 1 |
| 1 | Sub-Feature | 5 | 5 | 0 | 2 |
| 2 | Component | 12 | 8 | 3 | 1 |
| 3 | Feature | 4 | 4 | 0 | 0 |

### Stage Completion Summary
| Stage | Total | Completed | Active | Blocked |
|-------|-------|-----------|--------|---------|
| 01_request_gathering | 8 | 6 | 2 | 0 |
| 02_research | 8 | 5 | 3 | 0 |
| 04_design | 8 | 4 | 4 | 0 |
| 06_development | 8 | 3 | 5 | 0 |
```

4. **Automation via Script** (bash or Python):

```bash
#!/bin/bash
# regenerate-relational-avenue.sh

DB_FILE="entities.db"
SQL_SCHEMA="schema.sql"
QUERIES_DIR="queries"
RESULTS_DIR="results"

# Create or reset database
sqlite3 "$DB_FILE" < "$SQL_SCHEMA"

# Populate from file-based avenues (parse .0agnostic/)
python3 extract_entities_to_sql.py --output "$DB_FILE"

# Run all queries and save results
for query_file in "$QUERIES_DIR"/*.sql; do
  query_name=$(basename "$query_file" .sql)
  sqlite3 "$DB_FILE" < "$query_file" > "$RESULTS_DIR/$query_name.csv"
  echo "✓ Generated $query_name.csv"
done

# Generate markdown summary
sqlite3 "$DB_FILE" \
  "SELECT 'Regenerated: ' || datetime('now') as timestamp;" >> results.md
```

**Benefits**:
- SQL schemas documented inline with markdown
- Queries are self-documenting (comments explain purpose)
- Results can be regenerated automatically
- Easy to version control (entire avenue is human-readable)
- Queryable via SQLite, PostgreSQL, or any SQL database
- Results can feed into dashboards or reports

### Avenue 13: SHIMI Structures — Optimization Primitives

**Format**: JSON optimization primitives per node

**Comprehensiveness**: Optimization-focused

**Purpose**: Performance tuning and resource budgets per node

**Structure**:
```json
{
  "stage_3_04_design": {
    "context_budget_tokens": 8000,
    "cache_ttl_seconds": 3600,
    "priority": "high",
    "frequency": "frequent",
    "refresh_trigger": "on_file_change"
  },
  "stage_3_02_research": {
    "context_budget_tokens": 12000,
    "cache_ttl_seconds": 7200,
    "priority": "medium",
    "frequency": "occasional"
  }
}
```

**Use case**: Optimize performance per entity
- "How much context can stage_3_04_design load?"
- "When should we refresh this node's cache?"
- "What's the priority level of this feature?"

### Avenue 11: Vector Embeddings — Semantic Similarity

**Format**: Binary embeddings (NPY, H5, ONNX)

**Comprehensiveness**: Semantic space

**Purpose**: Find semantically similar contexts for retrieval-augmented generation

**Structure**:
```
Entity: context_chain_system
Embedding: [0.23, -0.15, 0.87, ..., 0.42]  (1536 dimensions)

Entity: memory_system
Embedding: [0.25, -0.12, 0.89, ..., 0.41]  (similar, nearby in embedding space)

Entity: docker_setup
Embedding: [-0.45, 0.78, -0.23, ..., 0.55]  (very different)
```

**Use case**: Semantic search
- "What context is most similar to this query?"
- "Find related entities based on semantic meaning"
- "RAG: retrieve most similar context for this task"

### Avenue 12: Temporal Index — Versioning All Above

**Format**: JSON timeline with versions of 09-13

**Comprehensiveness**: Change tracking

**Purpose**: Track evolution and versions of knowledge graph, relational tables, SHIMI, and embeddings over time

**Structure**:
```json
{
  "2026-02-26": {
    "knowledge_graph_v1": { "nodes": [...], "edges": [...] },
    "relational_tables_v1": { "schema": [...], "data": [...] },
    "shimi_structures_v1": { "budget": {...} },
    "vector_embeddings_v1": { "embeddings": [...] }
  },
  "2026-02-27": {
    "knowledge_graph_v2": { "nodes": [...], "edges": [...] },  // Updated
    "relational_tables_v1": { ... },  // Unchanged
    "shimi_structures_v2": { "budget": {...} },  // Updated
    "vector_embeddings_v1": { ... }  // Unchanged
  }
}
```

**Note**: Temporal Index isn't a separate data structure — it's **versioning metadata** applied to all the above avenues.

**Use case**: Historical analysis
- "How has this entity evolved?"
- "What changed between 2026-02-26 and 2026-02-27?"
- "Restore to previous knowledge graph version"
- "Compare old vs. new SHIMI configurations"

## Relationship to File-Based Avenues

Data-based avenues are **generated FROM and augment** file-based avenues:

```
File-Based Avenues (01-08)
    ↓
Extraction & Processing Pipeline
    ↓
Data-Based Avenues (09-13)
```

Example: `03_auto_memory/` and `05_skills/` files are parsed to generate:
- **Avenue 09** (Knowledge Graph): Concepts and relationships
- **Avenue 10** (Relational Tables): Indexed metadata
- **Avenue 11** (Vector Embeddings): Semantic representations
- **Avenue 12** (Temporal Index): Version history

## When to Use Data-Based Avenues

| Question | Avenue | Method |
|----------|--------|--------|
| What concepts relate to X? | 09 Knowledge Graph | Graph traversal |
| What entities match criteria? | 10 Relational Tables | SQL query |
| How should we optimize this? | 13 SHIMI | Lookup by node |
| What's semantically similar? | 11 Vector Embeddings | Cosine similarity |
| How did X change over time? | 12 Temporal Index | Version comparison |

## Generation and Regeneration

Data-based avenues are **automatically generated** from file-based sources and can be **regenerated** if stale:

```
Update file-based avenues (01-08)
    ↓
Run extraction pipeline
    ↓
Regenerate data-based avenues (09-13)
```

If a data-based avenue becomes outdated, simply regenerate from current file-based content.

## Avenue 10 Implementation: SQLite Schema & Data

Below is a complete **Avenue 10 (Relational Tables)** implementation — all avenue rankings stored as queryable SQL schema with data embedded in markdown.

### Schema

```sql
-- Table 1: Data-Based Avenues (09-13)
CREATE TABLE avenues (
  id INTEGER PRIMARY KEY,
  avenue_number INTEGER NOT NULL UNIQUE,
  name TEXT NOT NULL,
  format TEXT,
  purpose TEXT,
  status TEXT
);

-- Table 2: Capability Dimensions (8 dimensions for ranking)
CREATE TABLE capabilities (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  description TEXT,
  category TEXT,
  lower_is_better BOOLEAN
);

-- Table 3: Rankings (one-hot encoded: 1=1st place, 2=2nd, 3=3rd, 4=4th)
CREATE TABLE rankings (
  id INTEGER PRIMARY KEY,
  avenue_id INTEGER NOT NULL,
  capability_id INTEGER NOT NULL,
  rank_place INTEGER NOT NULL CHECK(rank_place >= 1 AND rank_place <= 4),
  notes TEXT,
  FOREIGN KEY (avenue_id) REFERENCES avenues(id),
  FOREIGN KEY (capability_id) REFERENCES capabilities(id)
);
```

### Data: Avenues

| ID | Avenue # | Name | Format | Purpose | Status |
|----|----------|------|--------|---------|--------|
| 1 | 9 | Knowledge Graph | JSON graph structure | Semantic relationships | mature |
| 2 | 10 | Relational Tables | SQL schema | Tabular metadata queries | mature |
| 3 | 11 | Vector Embeddings | NPY/H5 binary | Semantic similarity (RAG) | mature |
| 4 | 13 | SHIMI Structures | JSON primitives | Hierarchical agent memory | advanced_research |

### Data: Capabilities (8 Dimensions)

| ID | Name | Description | Category |
|----|------|-------------|----------|
| 1 | Reasoning Capabilities | Complex logical reasoning | reasoning |
| 2 | Comprehensiveness | Detail and information coverage | detail |
| 3 | Retrieval Speed | Query performance (lower is better) | performance |
| 4 | Scalability | Performance as data grows | performance |
| 5 | Semantic Awareness | Meaning and relationship understanding | semantic |
| 6 | Decentralization Support | Distributed system capability | distributed |
| 7 | Practical Adoption | Industry usage and tooling | adoption |
| 8 | Maturity Level | Research completeness and stability | maturity |

### Data: Rankings (One-Hot Encoded: 1-4)

#### Reasoning Capabilities
| Avenue | Rank | Notes |
|--------|------|-------|
| Knowledge Graph | **1** | Best for logical traversal and relationship reasoning |
| SHIMI Structures | **2** | Hierarchical reasoning with semantic awareness |
| Vector Embeddings | **3** | Limited to semantic similarity, no logical reasoning |
| Relational Tables | **4** | Only basic SQL joins and predicates |

#### Comprehensiveness
| Avenue | Rank | Notes |
|--------|------|-------|
| Knowledge Graph | **1** | Most detailed relationship information |
| SHIMI Structures | **2** | Hierarchical structure with full semantic detail |
| Relational Tables | **3** | Structured data, limited semantic info |
| Vector Embeddings | **4** | Only 1536-dim vectors, no explainability |

#### Retrieval Speed (lower is better)
| Avenue | Rank | Notes |
|--------|------|-------|
| SHIMI Structures | **1** | O(log n) hierarchical traversal |
| Vector Embeddings | **2** | Fast cosine similarity with index |
| Relational Tables | **3** | O(n) to O(log n) depending on indexes |
| Knowledge Graph | **4** | Slower graph traversal with relationship lookups |

#### Scalability
| Avenue | Rank | Notes |
|--------|------|-------|
| SHIMI Structures | **1** | Designed for distributed multi-agent systems |
| Vector Embeddings | **2** | Scales with vector databases |
| Relational Tables | **3** | Scales with indexes and partitioning |
| Knowledge Graph | **4** | Graph operations become expensive at scale |

#### Semantic Awareness
| Avenue | Rank | Notes |
|--------|------|-------|
| SHIMI Structures | **1** | Semantic hierarchy by design |
| Knowledge Graph | **2** | Type-aware edges and relationships |
| Vector Embeddings | **3** | Semantic similarity but not interpretable |
| Relational Tables | **4** | No semantic information, just structure |

#### Decentralization Support
| Avenue | Rank | Notes |
|--------|------|-------|
| SHIMI Structures | **1** | Merkle-DAG + CRDT native |
| Knowledge Graph | **2** | Can be distributed via sharding |
| Vector Embeddings | **3** | Requires central synchronization |
| Relational Tables | **4** | Difficult to distribute consistently |

#### Practical Adoption
| Avenue | Rank | Notes |
|--------|------|-------|
| Vector Embeddings | **1** | Wide industry use (RAG, semantic search) |
| Knowledge Graph | **2** | Used by Google, Microsoft, etc. |
| Relational Tables | **3** | Universal SQL databases |
| SHIMI Structures | **4** | Still research-phase, limited tools |

#### Maturity Level
| Avenue | Rank | Notes |
|--------|------|-------|
| Relational Tables | **1** | Decades of stable technology |
| Knowledge Graph | **2** | Established RDF/semantic web standards |
| Vector Embeddings | **3** | Newer but widely adopted (2020s) |
| SHIMI Structures | **4** | Active research (ArXiv 2504.06135) |

### Example Queries

If you export this markdown to SQLite using the schema above:

```sql
-- Query 1: What avenues rank 1st in each capability?
SELECT c.name, a.name, r.notes
FROM rankings r
JOIN avenues a ON r.avenue_id = a.id
JOIN capabilities c ON r.capability_id = c.id
WHERE r.rank_place = 1
ORDER BY c.name;

-- Query 2: How many 1st-place rankings does each avenue have?
SELECT a.name, COUNT(*) as first_places
FROM rankings r
JOIN avenues a ON r.avenue_id = a.id
WHERE r.rank_place = 1
GROUP BY a.name
ORDER BY first_places DESC;

-- Query 3: Ranking distribution across all capabilities for one avenue
SELECT c.name, r.rank_place
FROM rankings r
JOIN capabilities c ON r.capability_id = c.id
WHERE r.avenue_id = (SELECT id FROM avenues WHERE name = 'SHIMI Structures')
ORDER BY c.name;

-- Query 4: Compare two avenues across all capabilities
SELECT c.name,
  MAX(CASE WHEN a.name = 'Knowledge Graph' THEN r.rank_place END) as 'KG',
  MAX(CASE WHEN a.name = 'SHIMI Structures' THEN r.rank_place END) as 'SHIMI'
FROM rankings r
JOIN capabilities c ON r.capability_id = c.id
JOIN avenues a ON r.avenue_id = a.id
GROUP BY c.name;
```

### Implementation Note

This data is **queryable and executable** — you can:

1. **Export to SQLite**: Copy the schema and INSERT statements into a `.sql` file and run:
   ```bash
   sqlite3 avenues.db < schema_and_data.sql
   ```

2. **Use in Python/Node/Java**: Copy schema + data into any SQL database (PostgreSQL, MySQL, etc.) for programmatic queries

3. **Keep in Markdown**: This markdown document IS the source of truth — it's version-controllable, human-readable, and can be regenerated whenever the ranking tables in the overview section above are updated

This demonstrates **Avenue 10 (Relational Tables)** in action: SQL schema documented in markdown, queryable, and integrated with the full context chain.

## Hierarchy of Comprehensiveness

Complete comprehensiveness hierarchy across all avenues:

```
File-Based (Primary)
├── 01 JSON-LD: Complete detail
├── 02 Markdown: ~80% detail
├── 05 Skills: Task detail
├── 04 References: Curated links
├── 06 Agents: Lightweight
├── 07 Path Rules: Scoped
└── 08 Hooks: Fragments

Data-Based (Derived)
├── 09 Knowledge Graph: Relationship detail
├── 10 Relational Tables: Structured queries
├── 13 SHIMI: Optimization detail
├── 11 Vector Embeddings: Semantic representation
└── 12 Temporal: Version history (wraps all)
```

## Summary

Data-based avenues provide **semantic and optimization capabilities** to the file-based avenues, but are entirely **optional and regenerable**. Use them when:
- You need semantic search (Avenue 11)
- You need relational queries (Avenue 10)
- You need performance optimization (Avenue 13)
- You need historical tracking (Avenue 12)
- You need conceptual relationships (Avenue 09)

For basic operation, the file-based avenues (01-08) are sufficient.
