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
