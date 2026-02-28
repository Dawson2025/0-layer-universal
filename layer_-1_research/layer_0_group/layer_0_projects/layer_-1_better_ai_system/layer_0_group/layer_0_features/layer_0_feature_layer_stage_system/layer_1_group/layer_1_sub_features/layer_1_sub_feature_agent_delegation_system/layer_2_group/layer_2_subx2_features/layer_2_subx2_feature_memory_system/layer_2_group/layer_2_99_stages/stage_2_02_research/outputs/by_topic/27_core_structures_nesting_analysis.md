# Core Structures Nesting Analysis: Vectors, Relations, and Graphs in PostgreSQL

## Purpose

This document analyzes how the three core data structures of AI agent memory -- vectors, relational tables, and knowledge graphs -- nest inside a single PostgreSQL instance, what underlying CS data structures power each one, and why this unified approach works as a single backend for all memory types.

---

## 1. The Three Core Structures

Modern AI long-term memory systems fundamentally use three data structures:

1. **Vector databases** -- for semantic similarity search
2. **Relational tables** -- for structured data and relationships
3. **Knowledge graphs** -- for explicit entity relationships

The dominant trend is nesting vectors and graphs inside PostgreSQL/SQL rather than running separate specialized databases.

---

## 2. Vectors Inside SQL: pgvector

The pgvector extension allows storing vectors as a native PostgreSQL column type, making embeddings first-class citizens alongside regular columns:

```sql
CREATE TABLE memories (
    id UUID PRIMARY KEY,
    content TEXT,              -- Regular SQL column
    embedding VECTOR(1536),    -- Vector column (special type)
    timestamp TIMESTAMPTZ,     -- Regular SQL column
    user_id UUID               -- Regular SQL column
);

-- Vector similarity search in pure SQL
SELECT content FROM memories
WHERE user_id = '123'
ORDER BY embedding <=> query_vector  -- <=> is cosine distance operator
LIMIT 5;
```

What is actually happening:
- Vectors are stored as fixed-length arrays of floats within PostgreSQL
- The `<=>` operator computes cosine distance between two vectors
- Specialized indexes (IVFFlat, HNSW, DiskANN) enable fast approximate nearest-neighbor search
- The table remains a standard relational table -- it just has a special column type for embeddings

The key insight is that pgvector does not create a separate database. It adds a column type and index type to the existing relational engine.

---

## 3. Knowledge Graphs Inside SQL

### Adjacency List Representation

Knowledge graphs are stored as pairs of relational tables -- one for nodes, one for edges:

```sql
-- Graph nodes
CREATE TABLE entities (
    id UUID PRIMARY KEY,
    name TEXT,
    type VARCHAR(50)
);

-- Graph edges (adjacency list)
CREATE TABLE relationships (
    source_id UUID REFERENCES entities(id),
    target_id UUID REFERENCES entities(id),
    relationship_type VARCHAR(100),
    properties JSONB
);
```

### Graph Traversal via Recursive CTEs

SQL provides recursive Common Table Expressions for graph traversal, eliminating the need for a dedicated graph database for most use cases:

```sql
WITH RECURSIVE paths AS (
    SELECT source_id, target_id, 1 as depth
    FROM relationships
    WHERE source_id = 'start_node'

    UNION ALL

    SELECT r.source_id, r.target_id, p.depth + 1
    FROM relationships r
    JOIN paths p ON r.source_id = p.target_id
    WHERE p.depth < 3
)
SELECT * FROM paths;
```

### Hybrid with Neo4j

Some systems store graph structure in PostgreSQL for ACID guarantees but use Neo4j for complex graph queries (multi-hop traversals, shortest paths), syncing between them. However, for most AI memory use cases, PostgreSQL recursive CTEs are sufficient.

---

## 4. Under the Hood: What Each Structure Really Is

### Vector Indexes

Vector databases are built on graph and tree structures internally:

| Index Type | Underlying Structure | Characteristics |
|-----------|---------------------|-----------------|
| **Flat** | Arrays | Brute force O(n) scan. Only viable for small datasets |
| **IVFFlat** | Clustered arrays + tree | K-means clusters vectors into buckets. Search only relevant buckets |
| **HNSW** | Multi-layer graph | Hierarchical proximity graph. Upper layers for coarse navigation, lower for precision. **This is a graph data structure** |
| **DiskANN** | Disk-optimized graph | Vamana graph algorithm. Achieves 471 QPS at 99% recall on 50M vectors |

The critical realization: vector databases are actually graphs. The "vectors" are node values -- the index structure uses graph traversal to find nearest neighbors.

### Relational Tables

SQL tables use classic data structures internally:

| Component | Underlying Structure | Purpose |
|-----------|---------------------|---------|
| **Primary indexes** | B-trees | Balanced tree, O(log n) lookups on keys and indexed columns |
| **Table data** | Heap files | Unsorted collection of records in 8KB pages |
| **Hash indexes** | Hash tables | O(1) equality lookups (less common than B-trees) |

### Knowledge Graphs

Graph databases use various representations:

| Representation | Structure | When Used |
|---------------|-----------|-----------|
| **Adjacency lists** | Per-node edge lists | Sparse graphs (what SQL foreign keys create) |
| **Adjacency matrices** | 2D matrix | Dense graphs (wasteful for sparse) |
| **Edge lists** | List of (source, target) pairs | What the SQL `relationships` table is |
| **Index-free adjacency** (Neo4j) | Direct node-to-neighbor pointers | O(1) traversal, no index lookups |

---

## 5. The Unified PostgreSQL Architecture

```
+-----------------------------------------+
|         PostgreSQL (Foundation)          |
|                                         |
|  +----------------+  +----------------+ |
|  | Vector columns |  | JSONB columns  | |
|  | (pgvector)     |  | (semi-struct)  | |
|  +----------------+  +----------------+ |
|           |                   |          |
|  +--------v-------------------v--------+ |
|  |   Relational tables with indexes    | |
|  |   (B-trees, hash tables)           | |
|  +-------------------------------------+ |
|           |                              |
|  +--------v----------------------------+ |
|  |  Graph relationships (foreign keys) | |
|  |  (adjacency lists)                  | |
|  +-------------------------------------+ |
+-----------------------------------------+
```

This diagram shows the layering:
- **Bottom**: Foreign key relationships form adjacency lists (graph structure)
- **Middle**: Relational tables with B-tree and hash indexes provide structured storage
- **Top**: pgvector columns and JSONB columns add specialized data types on top of the relational foundation

---

## 6. The Actual Data Structures in Play

Everything reduces to five classic CS data structures:

| Data Structure | Where It Appears | Role |
|---------------|-----------------|------|
| **Arrays** | Vector embeddings (VECTOR type) | Store 1536-dimensional float arrays for semantic content |
| **B-trees** | Indexes on timestamps, IDs, attributes | O(log n) lookups for structured queries |
| **Graphs** | HNSW/DiskANN indexes + knowledge graph edges | Similarity search traversal + entity relationships |
| **Hash tables** | Hash indexes for equality checks | O(1) lookups on exact matches |
| **Heaps** | Raw table storage (heap files) | Unsorted record storage in 8KB pages |

The key insight: there is no magic. Every sophisticated memory system decomposes into arrays, trees, graphs, and hash tables -- the same structures from any data structures course.

---

## 7. Why PostgreSQL Works as a Single Unified Backend

### Cost and Operational Benefits

The 66% cost reduction from unification comes from:
1. **One connection pool** instead of 3-4 separate databases
2. **Single transaction** -- ACID across all memory types simultaneously
3. **Cross-type JOINs** -- combine semantic + episodic + procedural in one query
4. **One backup strategy** -- no multi-database coordination
5. **Native integration** -- no network hops between databases

### Unified Cross-Type Query

A single query can leverage all data structures simultaneously:

```sql
SELECT
    s.content as semantic_fact,
    e.context as recent_episode,
    p.trajectory as procedure
FROM semantic_memory s
JOIN episodes e ON e.embedding <=> s.embedding < 0.3  -- Vector similarity
JOIN procedures p ON p.task_embedding <=> s.embedding < 0.4
WHERE s.user_id = ?
  AND e.timestamp > NOW() - INTERVAL '7 days'  -- Time-based filter
  AND p.success_rate > 0.8  -- Procedural filter
ORDER BY s.embedding <=> query_vector
LIMIT 10;
```

This single query uses:
- **Vectors** (semantic similarity via `<=>` operator)
- **Time-series** (temporal filtering on `timestamp`)
- **Relational** (JOINs, user_id filtering)
- **B-tree indexes** (on user_id, timestamp columns)
- **Graph indexes** (HNSW for vector nearest-neighbor search)

### Why Not Specialized Databases?

Specialized databases (Pinecone for vectors, Neo4j for graphs, TimescaleDB standalone) excel in isolation. But AI memory requires cross-type queries -- finding semantically similar facts from recent episodes that match known procedures. Running these across separate databases means multiple network round-trips, no shared transactions, and complex synchronization. PostgreSQL with extensions provides "good enough" performance (471 QPS at 99% recall) with dramatically simpler operations.

---

## Cross-References

- **Core data structure hierarchy (what implements each memory type)**: `22_core_data_structure_hierarchy.md`
- **AI memory system tiers (how systems compose)**: `23_core_ai_memory_systems.md`
- **Full SQL schemas for all memory types**: `26_long_term_storage_sql_schemas.md`
- **Memory type hierarchy (biological buildup)**: `21_core_memory_structure_hierarchy.md`

---

## Sources

- [TigerData: Building AI Agents with Persistent Memory -- A Unified Database Approach](https://www.tigerdata.com/learn/building-ai-agents-with-persistent-memory-a-unified-database-approach)
- [Redis: AI Agent Memory for Stateful Systems](https://redis.io/blog/ai-agent-memory-stateful-systems/)
- [Reddit: How Do You Store Long-Term Memory for AI Agents](https://www.reddit.com/r/ArtificialInteligence/comments/1ptwrfu/how_do_you_store_longterm_memory_for_ai_agents/)
- [Memory in the Age of AI Agents (arXiv:2512.13564)](https://arxiv.org/abs/2512.13564)
