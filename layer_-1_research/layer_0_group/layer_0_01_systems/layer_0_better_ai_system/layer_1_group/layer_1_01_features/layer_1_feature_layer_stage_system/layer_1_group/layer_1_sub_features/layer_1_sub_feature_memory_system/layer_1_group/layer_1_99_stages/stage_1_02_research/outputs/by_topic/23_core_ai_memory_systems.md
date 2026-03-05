---
resource_id: "625d40e9-0801-4140-a025-48e731f164d4"
resource_type: "output"
resource_name: "23_core_ai_memory_systems"
---
# Core AI Memory Systems: Tiered Architecture from Most to Least Foundational

<!-- section_id: "0e217ef3-fb9e-4f6a-a29a-bbb39d87cbd6" -->
## Purpose

This document presents a **9-tier ranking** of AI memory system structures, ordered from most foundational (cannot build anything without it) to least foundational (optional optimization). It answers: "If I'm building an AI agent memory system, what do I need first, and what can I add later?"

This complements the flat comparison in `15_vectors_graphs_and_neurology.md` by adding the **dependency ordering**, **substitutability analysis**, and **SHIMI** (Semantic Hierarchical Memory Index) placement.

---

<!-- section_id: "660feca8-73e1-4ae6-8c30-9b661a281785" -->
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

<!-- section_id: "7aad99f3-3aaf-4840-9a25-5c4d4531c699" -->
## 2. Tier 1: Vector Embeddings (Most Foundational)

<!-- section_id: "9dd0edbf-d803-4864-97b8-55909d530c23" -->
### Why Most Foundational
- **Everything** in modern AI memory uses embeddings
- Semantic memory, episodic memory, procedural memory ALL store vector representations
- Without embeddings, you have no semantic similarity, no retrieval, no intelligence
- 1536-4096 dimensional float arrays that encode meaning

<!-- section_id: "0cb84f11-f43b-4faf-a88e-6bed60cfcfe5" -->
### What They Store
Semantic meaning of text, images, or any data in high-dimensional space.

<!-- section_id: "e593f839-b6e0-4d49-8cfc-0fd4906b7c20" -->
### Structure
Fixed-length arrays of floats (e.g., `VECTOR(1536)` in pgvector).

<!-- section_id: "18652490-74f2-426f-bdb7-f56cb7c31903" -->
### Used By
Literally every memory type — it's the universal representation layer.

<!-- section_id: "67158ac8-7159-44b1-8f59-daf2c52afd24" -->
### Substitutability
**NO** — Cannot do AI memory without embeddings.

---

<!-- section_id: "2faded27-fc95-4c18-9a55-53d7eaa6cd9b" -->
## 3. Tier 2: Relational Tables (SQL / PostgreSQL)

<!-- section_id: "76296d0f-0606-404b-ae71-7067b5abcca5" -->
### Why Second Most Foundational
- Provides ACID guarantees for data consistency
- Foundation for structured queries, joins, transactions
- **Hosts** vectors, graphs, and time-series data in production systems
- Every other structure can be built on top of or inside relational tables

<!-- section_id: "42da44ed-b42d-4662-9c53-9929ce73d99b" -->
### What They Store
Structured facts, user data, metadata, preferences, entities.

<!-- section_id: "0264fda0-eff3-43a6-92b9-2926b026cd2a" -->
### Structure
Rows and columns with typed fields, primary keys, foreign keys. Under the hood: B-trees (indexes) + heap files (data) + hash indexes.

<!-- section_id: "013d7c8c-e504-4759-aade-abc34706e7eb" -->
### Used By
All memory types for structured data — user profiles, facts, configuration.

<!-- section_id: "65cd06e0-c088-4074-b6f1-a72b7cb22860" -->
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

<!-- section_id: "faec06c3-8d67-462a-9802-b70f000e265a" -->
### Substitutability
**NO** — Need persistent structured storage.

---

<!-- section_id: "6af3044f-7beb-46f2-83b1-bb34f7a256e1" -->
## 4. Tier 3: Knowledge Graphs

<!-- section_id: "793fcc18-75eb-46a4-b3a4-fcd5d25de304" -->
### Why Third
- Explicitly represents **entity relationships** (who knows whom, what belongs to what)
- Can be built on top of relational tables (foreign keys) or native graph DBs (Neo4j)
- Critical for semantic memory but optional for episodic/procedural
- Enables multi-hop reasoning: "If A relates to B, and B relates to C, then..."

<!-- section_id: "392e7e17-f653-4a7b-b798-b4dce31ebf20" -->
### What They Store
Entities as nodes, relationships as edges, properties on both.

<!-- section_id: "a754c685-fcba-45fa-b5e5-b97d0b070dba" -->
### Structure
Adjacency lists (SQL foreign keys), adjacency matrices, or native graph storage (Neo4j index-free adjacency).

<!-- section_id: "b787bef6-d630-4169-a48d-079fa10b4456" -->
### Used By
Primarily semantic memory, some episodic memory (event relationships).

<!-- section_id: "fb3d8249-2996-4206-9c2d-7902c209c8d3" -->
### Substitutability
**MAYBE** — Can use just vectors for similarity-based connections, but loses explicit relationships.

---

<!-- section_id: "41de1a5c-ca04-4f4b-979a-c7bb7bec2384" -->
## 5. Tier 3.5: SHIMI (Semantic Hierarchical Memory Index)

<!-- section_id: "6da1fd9c-0bc6-4edf-96a4-7198d56cefd2" -->
### What It Is
SHIMI is a **hierarchical tree structure** specifically designed for semantic memory. It models knowledge as a dynamically structured hierarchy of concepts, enabling meaning-driven retrieval rather than surface similarity.

<!-- section_id: "bfa7e2ff-a9ca-4ac0-bffd-cdbfcf46f10c" -->
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

<!-- section_id: "5be7ae87-582c-495a-a978-1cf722243b81" -->
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

<!-- section_id: "3b658f91-9c81-4d97-8fe6-65bf9ca81f0f" -->
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

<!-- section_id: "733894ba-0c14-4480-8057-29fd23136f4d" -->
### Built On
- **Tier 1 (Vectors)**: Each node has a semantic summary/embedding for similarity matching
- **Tier 2 (SQL)**: Can be stored as adjacency list in PostgreSQL
- **Tier 3 (Graphs)**: Is a specialized graph — specifically a directed tree/DAG

<!-- section_id: "21d6c0da-2db8-4616-8caf-1b671d87db8f" -->
### Additional Structures Used
- **Merkle-DAG** for synchronization across agents (only send changed subtrees)
- **Bloom Filters** for efficient sync protocol ("do you have node X?")
- **CRDTs** (Conflict-free Replicated Data Types) for distributed consistency

<!-- section_id: "1e8f29ee-8848-4abf-b735-56e494c9a29b" -->
### Key Properties

| Property | Description |
|----------|-------------|
| **Hierarchical Abstraction** | Top = abstract ("Transportation"), Bottom = specific ("Tesla Model 3"). Enforces compression: each level has fewer words. |
| **Meaning-Based Retrieval** | Query: "I need to get to the airport" -> Transportation -> Ground -> Cars -> [ride services]. Not just similarity — semantic reasoning through hierarchy. |
| **Explainable Paths** | Shows explicit reasoning: Abstract -> Mid-level -> Specific. Unlike vector search black box. |
| **Decentralized Sync** | Agents maintain local SHIMI trees, sync via Merkle-DAG summaries + Bloom filters + CRDT merge. |
| **Dynamic Growth** | New entities find best-matching subtrees; intermediate abstraction nodes created when needed. |

<!-- section_id: "5585cf09-9e62-4f7e-a802-d696df8d1c11" -->
### Comparison to Other Structures

| Structure | Retrieval Method | Explainability | Scalability | Best For |
|-----------|-----------------|----------------|-------------|----------|
| Vector DB (Tier 1) | Brute-force k-NN or HNSW | Black box | O(n) -> O(log n) | Raw similarity |
| Knowledge Graph (Tier 3) | Graph traversal | Explicit edges | O(edges) | Relationships |
| **SHIMI (Tier 3.5)** | Hierarchical traversal | Abstraction paths | O(log n) tree depth | Semantic memory |
| Time-Series (Tier 4) | Time range filtering | Temporal order | O(log n) | Events over time |

<!-- section_id: "0d137344-1214-47fe-9a0c-f6377c089f48" -->
### Performance
SHIMI outperforms flat vector retrieval in semantic retrieval accuracy, traversal efficiency, synchronization cost, and scalability — especially in decentralized AI ecosystems.

<!-- section_id: "7fd3e5f1-d587-44b3-b6d1-b7ef93c9a409" -->
### Substitutability
**OPTIONAL** — Can use flat vector search + knowledge graphs instead. SHIMI provides better semantic organization and explainability.

---

<!-- section_id: "35a894e7-b09c-4b16-9244-1d9c7a1c2b36" -->
## 6. Tier 4: Time-Series Stores (Hypertables)

<!-- section_id: "266975c7-e54e-4564-9a1a-5cb83ba14cb9" -->
### Why Fourth
- Specialized for **temporal ordering** — "what happened when"
- Essential for episodic memory, less critical for semantic/procedural
- Built on relational tables with time-based partitioning

<!-- section_id: "79d06499-a462-48f2-b182-78dea4ddf1e7" -->
### What They Store
Events ordered by timestamp with automatic chunking.

<!-- section_id: "ef2bda9e-2d9a-426b-84a8-8bf22f811680" -->
### Structure
Relational tables with timestamp column + automatic time partitioning (TimescaleDB hypertables).

<!-- section_id: "e9d31ac3-f507-4dc4-b33d-a272d53a7dff" -->
### Used By
Episodic memory (events), time-based memory (sequences), temporal facts.

<!-- section_id: "ef488df8-93a9-4400-af7a-1d5d74c7c102" -->
### Substitutability
**MAYBE** — Can use regular SQL with timestamp columns, but loses time-optimized partitioning and queries.

---

<!-- section_id: "2359893c-cb25-42b8-9309-853ee816afd3" -->
## 7. Tier 5: Working Memory Buffers

<!-- section_id: "2bfe4f50-419f-4538-8dc8-9d8b73df2649" -->
### Why Fifth
- Stores **immediate context** — the agent's "attention span"
- Maps to LLM context window (last N tokens/messages)
- Temporary — doesn't persist across sessions

<!-- section_id: "21a6e73c-51c8-4dee-9176-c45fb7460adc" -->
### What They Store
Recent conversation turns, current task state, active reasoning.

<!-- section_id: "caeaab23-d472-4dea-934c-465ad53b7aaa" -->
### Structure
Fixed-size array or ring buffer of recent interactions.

<!-- section_id: "520c2da4-5a1a-4569-a396-884c54670f2f" -->
### Used By
All memory types as the "staging area" before consolidation to long-term storage.

<!-- section_id: "34094d56-4cfa-4650-9059-47a5f31579e8" -->
### Substitutability
**NO** — Need immediate context somewhere (even if it's just the LLM's context window).

---

<!-- section_id: "7947b592-21dd-4ca7-a4fc-12a09ff91557" -->
## 8. Tier 6: Procedural / Skill Stores

<!-- section_id: "7a256ec4-f9ca-456b-9623-a9ad8a3de5e1" -->
### Why Sixth
- Stores **executable procedures** and skills — "how to do things"
- Less foundational because not all agents need procedural memory
- Most actively learned and refined memory type

<!-- section_id: "b3235467-75d0-420a-9e11-7ef37d242e1b" -->
### What They Store
Step-by-step action sequences, learned skills, tool usage patterns.

<!-- section_id: "bc6934bb-02dd-464a-b58a-7385149f66b6" -->
### Structure
Trajectories (JSONB arrays) + embeddings + success metrics. Two granularities: fine-grained (full trajectory) and coarse-grained (abstracted scripts).

<!-- section_id: "9f1ef058-fada-49ba-8c52-dd28e57956cd" -->
### Key Implementation: Mem^p Framework
- **Without procedural memory**: 71.93% success, 17.84 steps average
- **With procedural memory**: 79.94% success (+8 points), 14.62 steps (18% reduction)
- Transfer learning: procedures from GPT-4o boost smaller models by 5% without retraining

<!-- section_id: "44c53351-b3d6-45e5-bc5e-33c1a9ea3438" -->
### Used By
Procedural memory exclusively — "how to do X."

<!-- section_id: "5eb14930-e496-49d9-9b8f-8c2dbcef01be" -->
### Substitutability
**YES** — Many agents function without procedural memory. High value when present.

---

<!-- section_id: "753788cc-8574-4204-892c-4db9ab65d694" -->
## 9. Tier 7: Document Stores (JSONB)

<!-- section_id: "5321dc57-aa32-43cc-8bd6-96c34ebfbd92" -->
### Why Seventh
- Handles **variable schema** data — properties that differ per record
- Convenience layer for flexibility — can model everything in strict relational tables instead

<!-- section_id: "abc0551d-61b9-49b1-bfa2-7a174311d7ab" -->
### What They Store
Episode metadata, arbitrary properties, nested structures.

<!-- section_id: "51fee2fe-a30e-44be-afcb-49f47c184c4a" -->
### Structure
Binary-encoded JSON with indexable paths (PostgreSQL JSONB).

<!-- section_id: "b4ece000-966a-4170-bcbb-2f518c9c1fb2" -->
### Used By
All memory types for flexible metadata that doesn't fit clean schemas.

<!-- section_id: "fca6c097-4d49-490e-a521-f4021a3da63a" -->
### Substitutability
**YES** — Can use strict relational schemas. JSONB adds developer convenience.

---

<!-- section_id: "1aa17dbd-d463-45b4-84f9-5002c36938dd" -->
## 10. Tier 8: Vector Indexes (HNSW / IVFFlat)

<!-- section_id: "aa4f3454-8877-40c3-a65c-13bf08577bdf" -->
### Why Eighth
- **Not storage structures** — they're indexes for fast vector retrieval
- Built ON TOP of vectors to make search faster
- Could use brute-force search instead (slower but functional)

<!-- section_id: "b0e821b0-9e5b-4c1a-813c-7847caa36c5f" -->
### What They Store
Nothing — they index existing vectors for fast k-NN search.

<!-- section_id: "3c4add20-2cfe-41a1-b982-3de7c601a086" -->
### Structure
Graphs (HNSW — multi-layer proximity graph) or clustered buckets (IVFFlat — k-means clustering).

<!-- section_id: "51f837c7-5cca-4ecb-bb4c-de12821a83ce" -->
### Performance
- HNSW: O(log n) approximate nearest neighbor
- DiskANN: 471 QPS at 99% recall on 50M vectors
- IVFFlat: search only relevant buckets

<!-- section_id: "a80a05a4-aaca-4994-9c87-90c93c4b2158" -->
### Used By
Vector search optimization across all memory types.

<!-- section_id: "a755fcc2-bbf2-4ca9-838f-7983b81ac9da" -->
### Substitutability
**YES** — Can brute-force search vectors (but slow at scale).

---

<!-- section_id: "4a58f375-23ab-4e6f-9b58-20d34aa3abd9" -->
## 11. Tier 9: Event Stores / Audit Logs

<!-- section_id: "e6f945d1-ede9-4689-b3e1-3984de235249" -->
### Why Ninth (Least Foundational)
- Specialized **append-only logs** of all interactions
- Can be derived from other structures
- Useful for debugging and replay but not core to memory function

<!-- section_id: "617d922c-0eb1-4c7d-9bcb-809715d2498c" -->
### What They Store
Immutable record of every agent action/observation.

<!-- section_id: "a275f533-44ec-4b52-abf4-4219d4599bc5" -->
### Structure
Append-only log with timestamps.

<!-- section_id: "7ad2c2fc-f4f1-4db3-8ca6-0c46284c1e93" -->
### Used By
System monitoring, episodic memory source, debugging, compliance.

<!-- section_id: "8e33a0b7-e139-4750-bd7f-a8b53df515e2" -->
### Substitutability
**YES** — Nice to have, not required.

---

<!-- section_id: "3cebc67e-0191-4ec4-b410-77be2478c05d" -->
## 12. Three Analysis Dimensions

<!-- section_id: "a98cd4f6-4e09-41b6-a485-08be68da4360" -->
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

<!-- section_id: "c736326d-5084-4a52-b757-ac37ccb7f4fe" -->
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

<!-- section_id: "15abb7de-8f9c-48be-a0ab-8e2aeee9c663" -->
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

<!-- section_id: "3add0cfd-efa0-41a8-9cb8-3fa3f4890d5d" -->
## 13. The Minimal Core

**The absolute minimum for AI agent memory:**

1. **Vector Embeddings** (semantic similarity)
2. **Relational Tables** (persistent storage)
3. **Working Memory Buffer** (immediate context)

Everything else can be built on top of or derived from these three. Production systems add Tiers 3-9 for performance, specialized use cases, and developer experience.

---

<!-- section_id: "08874200-23eb-4e2b-8a67-d3ab10ee04cf" -->
## 14. Memory Consolidation Pipeline

Production systems implement a four-stage pipeline across these tiers:

<!-- section_id: "1d63902e-8c03-44e5-a939-b58be0653908" -->
### Stage 1: Extraction
Identify what's worth remembering from raw interactions. Uses Working Memory (Tier 5) as source.

<!-- section_id: "f32b8623-ffe7-447a-afcd-a8d98b92dd9c" -->
### Stage 2: Consolidation
Merge related information and resolve conflicts. LLM determines: merge, update, or keep separate.

<!-- section_id: "7ac0cada-cea6-4cd0-8846-9dfe59041eff" -->
### Stage 3: Storage
Persist to appropriate tier: semantic facts to Tier 2+3, episodes to Tier 2+4, procedures to Tier 2+6.

<!-- section_id: "075b1cc9-734e-4994-b2cd-db2bca651823" -->
### Stage 4: Retrieval
Hybrid retrieval combining: semantic similarity (Tier 1), temporal filtering (Tier 4), relational constraints (Tier 2), graph traversal (Tier 3).

**Performance benchmarks:**
- Mem0: 91% lower p95 latency vs full-context, 90% token reduction
- pgvector: 471 QPS at 99% recall on 50M vectors
- Retrieval latency: ~200ms for semantic search

---

<!-- section_id: "391f3caa-7ab6-483a-be8c-14eda6e2663c" -->
## Cross-References

- **Biological memory hierarchy these implement**: `21_core_memory_structure_hierarchy.md`
- **Data structures underlying these tiers**: `22_core_data_structure_hierarchy.md`
- **Vectors vs graphs deep comparison**: `15_vectors_graphs_and_neurology.md`
- **Individual data structure details**: `18_underlying_data_structures.md`
- **Master taxonomy**: `00_overview_and_taxonomy.md`

---

<!-- section_id: "edbf039d-4e24-4296-87b4-742902c38a80" -->
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
