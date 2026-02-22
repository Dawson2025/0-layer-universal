# Core AI Memory Systems: Tiered Architecture from Most to Least Foundational

## Purpose

This document presents a **9-tier ranking** of AI memory system structures, ordered from most foundational (cannot build anything without it) to least foundational (optional optimization). It answers: "If I'm building an AI agent memory system, what do I need first, and what can I add later?"

This complements the flat comparison in `15_vectors_graphs_and_neurology.md` by adding the **dependency ordering**, **substitutability analysis**, and **SHIMI** (Semantic Hierarchical Memory Index) placement.

---

## 1. Tier Ranking: Most to Least Foundational

```
+---------------------------------------------+
| 1. Vector Embeddings                        | <-- MOST FOUNDATIONAL
|    (Universal semantic representation)      |     Everything uses this
+---------------------------------------------+
                 | enables
+---------------------------------------------+
| 2. Relational Tables (SQL)                  | <-- Structural foundation
|    (Structured data + ACID)                 |     Hosts everything else
+---------------------------------------------+
                 | organizes
+---------------------------------------------+
| 3. Knowledge Graphs                         | <-- Semantic relationships
|    (Entity relationships)                   |     Explicit connections
+---------------------------------------------+
                 |
+---------------------------------------------+
| 3.5. SHIMI (Semantic Hierarchical Tree)     | <-- Specialized KG
|      (Hierarchical semantic memory)         |     Meaning-driven retrieval
+---------------------------------------------+
                 | +
+---------------------------------------------+
| 4. Time-Series Stores                       | <-- Temporal ordering
|    (Event sequences)                        |     "When" dimension
+---------------------------------------------+
                 | feeds
+---------------------------------------------+
| 5. Working Memory Buffers                   | <-- Active context
|    (Immediate recall)                       |     "Attention" span
+---------------------------------------------+
                 | consolidates to
+---------------------------------------------+
| 6. Procedural / Skill Stores               | <-- Behavioral memory
|    (How to do things)                       |     Action sequences
+---------------------------------------------+
                 | +
+---------------------------------------------+
| 7. Document Stores (JSONB)                  | <-- Flexible metadata
|    (Variable schema)                        |     Semi-structured
+---------------------------------------------+
                 | optimized by
+---------------------------------------------+
| 8. Vector Indexes (HNSW / IVFFlat)          | <-- Search optimization
|    (Fast retrieval)                         |     Not storage
+---------------------------------------------+
                 | +
+---------------------------------------------+
| 9. Event Stores / Audit Logs               | <-- LEAST FOUNDATIONAL
|    (Immutable history)                      |     Debugging/compliance
+---------------------------------------------+
```

---

## 2. Tier 1: Vector Embeddings (Most Foundational)

### Why Most Foundational
- **Everything** in modern AI memory uses embeddings
- Semantic memory, episodic memory, procedural memory ALL store vector representations
- Without embeddings, you have no semantic similarity, no retrieval, no intelligence
- 1536-4096 dimensional float arrays that encode meaning

### What They Store
Semantic meaning of text, images, or any data in high-dimensional space.

### Structure
Fixed-length arrays of floats (e.g., `VECTOR(1536)` in pgvector).

### Used By
Literally every memory type — it's the universal representation layer.

### Substitutability
**NO** — Cannot do AI memory without embeddings.

---

## 3. Tier 2: Relational Tables (SQL / PostgreSQL)

### Why Second Most Foundational
- Provides ACID guarantees for data consistency
- Foundation for structured queries, joins, transactions
- **Hosts** vectors, graphs, and time-series data in production systems
- Every other structure can be built on top of or inside relational tables

### What They Store
Structured facts, user data, metadata, preferences, entities.

### Structure
Rows and columns with typed fields, primary keys, foreign keys. Under the hood: B-trees (indexes) + heap files (data) + hash indexes.

### Used By
All memory types for structured data — user profiles, facts, configuration.

### The Unified PostgreSQL Approach

Modern production systems consolidate ALL memory types in PostgreSQL:

```sql
-- Semantic memory
CREATE TABLE semantic_facts (
    id UUID PRIMARY KEY,
    content TEXT,
    embedding VECTOR(1536),
    created_at TIMESTAMPTZ
);

-- Episodic memory (hypertable for time-series)
CREATE TABLE episodes (
    id UUID,
    timestamp TIMESTAMPTZ NOT NULL,
    content TEXT,
    embedding VECTOR(1536)
);

-- Procedural memory
CREATE TABLE procedures (
    id UUID PRIMARY KEY,
    task TEXT,
    trajectory JSONB,
    embedding VECTOR(1536),
    success_rate FLOAT
);
```

**Benefits**: Single transaction across all memory types, one backup strategy, 66% infrastructure cost reduction, no network hops between databases.

### Substitutability
**NO** — Need persistent structured storage.

---

## 4. Tier 3: Knowledge Graphs

### Why Third
- Explicitly represents **entity relationships** (who knows whom, what belongs to what)
- Can be built on top of relational tables (foreign keys) or native graph DBs (Neo4j)
- Critical for semantic memory but optional for episodic/procedural
- Enables multi-hop reasoning: "If A relates to B, and B relates to C, then..."

### What They Store
Entities as nodes, relationships as edges, properties on both.

### Structure
Adjacency lists (SQL foreign keys), adjacency matrices, or native graph storage (Neo4j index-free adjacency).

### Used By
Primarily semantic memory, some episodic memory (event relationships).

### Substitutability
**MAYBE** — Can use just vectors for similarity-based connections, but loses explicit relationships.

---

## 5. Tier 3.5: SHIMI (Semantic Hierarchical Memory Index)

### What It Is
SHIMI is a **hierarchical tree structure** specifically designed for semantic memory. It models knowledge as a dynamically structured hierarchy of concepts, enabling meaning-driven retrieval rather than surface similarity.

### Why Between Tier 3 and 4

**More specialized than Knowledge Graphs (Tier 3):**
- Structured as tree/DAG, not arbitrary graph
- Hierarchical abstraction: top = abstract, bottom = specific
- Semantic traversal: top-down from concept to entity
- Purpose-built for semantic memory

**More foundational than Time-Series (Tier 4):**
- Not specific to temporal data
- Core structure for organizing all semantic knowledge
- General-purpose hierarchy, not time-specific

### Structure

```
SHIMI Tree = T(V, E) where:
- V = semantic nodes (concepts/entities)
- E = parent-child relationships
- Each node v contains:
  - s(v) = semantic summary (text/embedding)
  - C(v) = list of children
  - E_v = set of entities at this node
  - p(v) = parent pointer
```

### Example Hierarchy

```
                    [Abstract Concepts]
                          |
        [Transportation]      [Communication]
            |                      |
    [Ground]  [Air]         [Digital]  [Physical]
       |        |              |           |
   [Cars] [Trains] [Planes] [Email] [Chat] [Mail]
     |
  [Tesla Model 3]
  [Honda Civic]
```

### Built On
- **Tier 1 (Vectors)**: Each node has a semantic summary/embedding for similarity matching
- **Tier 2 (SQL)**: Can be stored as adjacency list in PostgreSQL
- **Tier 3 (Graphs)**: Is a specialized graph — specifically a directed tree/DAG

### Additional Structures Used
- **Merkle-DAG** for synchronization across agents (only send changed subtrees)
- **Bloom Filters** for efficient sync protocol ("do you have node X?")
- **CRDTs** (Conflict-free Replicated Data Types) for distributed consistency

### Key Properties

| Property | Description |
|----------|-------------|
| **Hierarchical Abstraction** | Top = abstract ("Transportation"), Bottom = specific ("Tesla Model 3"). Enforces compression: each level has fewer words. |
| **Meaning-Based Retrieval** | Query: "I need to get to the airport" -> Transportation -> Ground -> Cars -> [ride services]. Not just similarity — semantic reasoning through hierarchy. |
| **Explainable Paths** | Shows explicit reasoning: Abstract -> Mid-level -> Specific. Unlike vector search black box. |
| **Decentralized Sync** | Agents maintain local SHIMI trees, sync via Merkle-DAG summaries + Bloom filters + CRDT merge. |
| **Dynamic Growth** | New entities find best-matching subtrees; intermediate abstraction nodes created when needed. |

### Comparison to Other Structures

| Structure | Retrieval Method | Explainability | Scalability | Best For |
|-----------|-----------------|----------------|-------------|----------|
| Vector DB (Tier 1) | Brute-force k-NN or HNSW | Black box | O(n) -> O(log n) | Raw similarity |
| Knowledge Graph (Tier 3) | Graph traversal | Explicit edges | O(edges) | Relationships |
| **SHIMI (Tier 3.5)** | Hierarchical traversal | Abstraction paths | O(log n) tree depth | Semantic memory |
| Time-Series (Tier 4) | Time range filtering | Temporal order | O(log n) | Events over time |

### Performance
SHIMI outperforms flat vector retrieval in semantic retrieval accuracy, traversal efficiency, synchronization cost, and scalability — especially in decentralized AI ecosystems.

### Substitutability
**OPTIONAL** — Can use flat vector search + knowledge graphs instead. SHIMI provides better semantic organization and explainability.

---

## 6. Tier 4: Time-Series Stores (Hypertables)

### Why Fourth
- Specialized for **temporal ordering** — "what happened when"
- Essential for episodic memory, less critical for semantic/procedural
- Built on relational tables with time-based partitioning

### What They Store
Events ordered by timestamp with automatic chunking.

### Structure
Relational tables with timestamp column + automatic time partitioning (TimescaleDB hypertables).

### Used By
Episodic memory (events), time-based memory (sequences), temporal facts.

### Substitutability
**MAYBE** — Can use regular SQL with timestamp columns, but loses time-optimized partitioning and queries.

---

## 7. Tier 5: Working Memory Buffers

### Why Fifth
- Stores **immediate context** — the agent's "attention span"
- Maps to LLM context window (last N tokens/messages)
- Temporary — doesn't persist across sessions

### What They Store
Recent conversation turns, current task state, active reasoning.

### Structure
Fixed-size array or ring buffer of recent interactions.

### Used By
All memory types as the "staging area" before consolidation to long-term storage.

### Substitutability
**NO** — Need immediate context somewhere (even if it's just the LLM's context window).

---

## 8. Tier 6: Procedural / Skill Stores

### Why Sixth
- Stores **executable procedures** and skills — "how to do things"
- Less foundational because not all agents need procedural memory
- Most actively learned and refined memory type

### What They Store
Step-by-step action sequences, learned skills, tool usage patterns.

### Structure
Trajectories (JSONB arrays) + embeddings + success metrics. Two granularities: fine-grained (full trajectory) and coarse-grained (abstracted scripts).

### Key Implementation: Mem^p Framework
- **Without procedural memory**: 71.93% success, 17.84 steps average
- **With procedural memory**: 79.94% success (+8 points), 14.62 steps (18% reduction)
- Transfer learning: procedures from GPT-4o boost smaller models by 5% without retraining

### Used By
Procedural memory exclusively — "how to do X."

### Substitutability
**YES** — Many agents function without procedural memory. High value when present.

---

## 9. Tier 7: Document Stores (JSONB)

### Why Seventh
- Handles **variable schema** data — properties that differ per record
- Convenience layer for flexibility — can model everything in strict relational tables instead

### What They Store
Episode metadata, arbitrary properties, nested structures.

### Structure
Binary-encoded JSON with indexable paths (PostgreSQL JSONB).

### Used By
All memory types for flexible metadata that doesn't fit clean schemas.

### Substitutability
**YES** — Can use strict relational schemas. JSONB adds developer convenience.

---

## 10. Tier 8: Vector Indexes (HNSW / IVFFlat)

### Why Eighth
- **Not storage structures** — they're indexes for fast vector retrieval
- Built ON TOP of vectors to make search faster
- Could use brute-force search instead (slower but functional)

### What They Store
Nothing — they index existing vectors for fast k-NN search.

### Structure
Graphs (HNSW — multi-layer proximity graph) or clustered buckets (IVFFlat — k-means clustering).

### Performance
- HNSW: O(log n) approximate nearest neighbor
- DiskANN: 471 QPS at 99% recall on 50M vectors
- IVFFlat: search only relevant buckets

### Used By
Vector search optimization across all memory types.

### Substitutability
**YES** — Can brute-force search vectors (but slow at scale).

---

## 11. Tier 9: Event Stores / Audit Logs

### Why Ninth (Least Foundational)
- Specialized **append-only logs** of all interactions
- Can be derived from other structures
- Useful for debugging and replay but not core to memory function

### What They Store
Immutable record of every agent action/observation.

### Structure
Append-only log with timestamps.

### Used By
System monitoring, episodic memory source, debugging, compliance.

### Substitutability
**YES** — Nice to have, not required.

---

## 12. Three Analysis Dimensions

### Dependencies (What requires what)

| Tier | Depends On |
|------|-----------|
| 1. Vectors | Arrays (Level 1 data structure) |
| 2. SQL Tables | B-trees, heaps, hash tables |
| 3. Knowledge Graphs | SQL (foreign keys) or vectors (similarity edges) |
| 3.5. SHIMI | Vectors + SQL + graphs |
| 4. Time-Series | SQL with time partitioning |
| 5. Working Memory | Simple buffer, references other structures |
| 6. Procedural | Vectors + SQL, specialized for one type |
| 7. JSONB | Convenience layer on SQL |
| 8. Indexes | Optimization layer on vectors |
| 9. Event Logs | Derived from other structures |

### Universality (How many memory types use it)

| Tier | Memory Types |
|------|-------------|
| 1. Vectors | ALL (semantic, episodic, procedural) |
| 2. SQL | ALL (stores metadata, structured facts) |
| 3. Knowledge Graphs | MOST (semantic primarily, some episodic) |
| 3.5. SHIMI | SOME (semantic primarily, potentially episodic/procedural) |
| 4. Time-Series | SOME (episodic, temporal) |
| 5. Working Memory | ALL (temporary context) |
| 6. Procedural | ONE (procedural memory only) |
| 7. JSONB | SOME (flexible use cases) |
| 8. Indexes | ALL (optimization) |
| 9. Event Logs | OPTIONAL (debugging) |

### Substitutability (Can you skip it?)

| Tier | Can Skip? | Alternative |
|------|----------|-------------|
| 1. Vectors | **NO** | No AI memory without embeddings |
| 2. SQL | **NO** | Need persistent structured storage |
| 3. Knowledge Graphs | **MAYBE** | Use vectors for similarity-based connections |
| 3.5. SHIMI | **YES** | Use flat vectors + KGs |
| 4. Time-Series | **MAYBE** | Use regular SQL with timestamps |
| 5. Working Memory | **NO** | Need immediate context |
| 6. Procedural | **YES** | Many agents lack procedural memory |
| 7. JSONB | **YES** | Use strict relational schemas |
| 8. Indexes | **YES** | Brute-force search (slow) |
| 9. Event Logs | **YES** | Nice to have |

---

## 13. The Minimal Core

**The absolute minimum for AI agent memory:**

1. **Vector Embeddings** (semantic similarity)
2. **Relational Tables** (persistent storage)
3. **Working Memory Buffer** (immediate context)

Everything else can be built on top of or derived from these three. Production systems add Tiers 3-9 for performance, specialized use cases, and developer experience.

---

## 14. Memory Consolidation Pipeline

Production systems implement a four-stage pipeline across these tiers:

### Stage 1: Extraction
Identify what's worth remembering from raw interactions. Uses Working Memory (Tier 5) as source.

### Stage 2: Consolidation
Merge related information and resolve conflicts. LLM determines: merge, update, or keep separate.

### Stage 3: Storage
Persist to appropriate tier: semantic facts to Tier 2+3, episodes to Tier 2+4, procedures to Tier 2+6.

### Stage 4: Retrieval
Hybrid retrieval combining: semantic similarity (Tier 1), temporal filtering (Tier 4), relational constraints (Tier 2), graph traversal (Tier 3).

**Performance benchmarks:**
- Mem0: 91% lower p95 latency vs full-context, 90% token reduction
- pgvector: 471 QPS at 99% recall on 50M vectors
- Retrieval latency: ~200ms for semantic search

---

## Cross-References

- **Biological memory hierarchy these implement**: `21_core_memory_structure_hierarchy.md`
- **Data structures underlying these tiers**: `22_core_data_structure_hierarchy.md`
- **Vectors vs graphs deep comparison**: `15_vectors_graphs_and_neurology.md`
- **Individual data structure details**: `18_underlying_data_structures.md`
- **Master taxonomy**: `00_overview_and_taxonomy.md`

---

## Sources

- Perplexity AI research conversation (Feb 2026) — synthesis of AI memory architecture literature
- [SHIMI: Semantic Hierarchical Memory Index (arXiv:2504.06135)](https://arxiv.org/abs/2504.06135) — SHIMI architecture and benchmarks
- [Building AI Agents with Persistent Memory (TigerData)](https://www.tigerdata.com/learn/building-ai-agents-with-persistent-memory-a-unified-database-approach) — unified PostgreSQL approach, 66% cost reduction, pgvector benchmarks
- [Mem0: Long-Term Memory for AI Agents](https://mem0.ai/blog/long-term-memory-ai-agents) — 91% latency reduction, 90% token reduction
- [AI Agent Memory (Redis)](https://redis.io/blog/ai-agent-memory-stateful-systems/) — stateful memory systems
- [Mem^p: Procedural Memory Framework (arXiv:2508.06433)](https://arxiv.org/html/2508.06433v2) — procedural memory benchmarks
- [AWS AgentCore Long-Term Memory](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/) — consolidation pipeline
- [Episodic Memory in AI (DigitalOcean)](https://www.digitalocean.com/community/tutorials/episodic-memory-in-ai) — episodic memory implementation patterns
- [IBM: AI Agent Memory](https://www.ibm.com/think/topics/ai-agent-memory) — knowledge graph memory
- [Vector Embeddings Technical Intro](https://www.shaped.ai/blog/a-technical-intro-to-embeddings) — embedding fundamentals
- [SHIMI: Hierarchical Memory Systems (EmergentMind)](https://www.emergentmind.com/topics/hierarchical-memory-systems) — SHIMI context
