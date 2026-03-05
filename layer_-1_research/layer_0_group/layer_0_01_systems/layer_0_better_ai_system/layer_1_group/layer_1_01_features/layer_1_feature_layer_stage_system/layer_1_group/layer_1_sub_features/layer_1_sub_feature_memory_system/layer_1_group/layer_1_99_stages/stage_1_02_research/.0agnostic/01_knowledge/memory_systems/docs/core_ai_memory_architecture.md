---
resource_id: "d2d6a5f3-1519-4c8c-a34f-5368d8b48dd7"
resource_type: "knowledge"
resource_name: "core_ai_memory_architecture"
---
# Core AI Memory Architecture — Knowledge Summary

<!-- section_id: "0127db62-8446-4b2f-bb3b-85f89a5b4ae7" -->
## Overview

This document summarizes the key architectural findings from Stage 02 Research on AI agent memory systems. It serves as the distilled knowledge reference for this stage.

---

<!-- section_id: "66bfb529-2a3b-422e-82a6-f3e681440951" -->
## 1. Memory Structure Hierarchy (Biological Buildup)

Memory types form a strict 6-level dependency chain, where each level requires the levels below:

| Level | Memory Type | Key Insight |
|-------|-------------|-------------|
| L1 | Sensory Memory | Raw inputs — the absolute foundation |
| L2 | Reflexes & Conditioning | Simple stimulus-response (Pavlovian) |
| L3 | Motor Memory | Coordinated movement patterns |
| L4 | Core Systems (4 parallel) | Semantic, Time-based, Spatial, Emotional |
| L5 | Complex Integrations (3) | Procedural, Episodic, Predictive |
| L6 | Autobiographical | Integrates ALL below into personal narrative |

**Design implication**: Build L4 (semantic + time-based) first, then L5 (episodic + procedural), then L6.

**Full detail**: `outputs/by_topic/21_core_memory_structure_hierarchy.md`, `outputs/by_topic/24_biological_data_structures_per_memory_type.md`

---

<!-- section_id: "3b2d6df7-3eba-4d25-815f-bff39dfe30c0" -->
## 2. Core Long-Term Memory Types — Emphasis Areas

The four critical long-term memory types for AI agents, ordered by dependency:

<!-- section_id: "10e9a901-d82d-4495-a042-86776230780f" -->
### 2.1 Semantic Memory (L4 — Foundation)

**What it stores**: Facts, concepts, relationships — the "what" of knowledge.

| Aspect | Biological | AI Implementation |
|--------|-----------|-------------------|
| **Structure** | Hub-and-spoke cortical networks | pgvector + knowledge graphs |
| **Storage** | Distributed across temporal lobes | `CREATE TABLE semantic_memory (embedding vector(1536), content text, ...)` with DiskANN index |
| **Retrieval** | Spreading activation | Cosine similarity `<=>` operator + recursive CTE graph traversal |
| **Key insight** | Concepts linked by typed relationships | Knowledge graphs as SQL adjacency lists (entities + relationships tables) |

**AI systems**: pgvector (471 QPS at 99% recall), Neo4j, hybrid PostgreSQL (pgvector column + foreign-key edges). Mem0 uses vector-first with optional Neo4j graph overlay. SHIMI adds hierarchical tree retrieval for meaning-driven access.

<!-- section_id: "e9f714d9-710f-4ae3-9abe-dbf0293ce96a" -->
### 2.2 Time-Based Memory (L4 — Foundation)

**What it stores**: Temporal sequences, chronological ordering, "when" and "in what order."

| Aspect | Biological | AI Implementation |
|--------|-----------|-------------------|
| **Structure** | Temporal Context Model (TCM) — drifting context vectors | Sliding window buffers + temporal context vectors |
| **Storage** | Hippocampal time cells, entorhinal cortex | TimescaleDB hypertables: `SELECT create_hypertable('temporal_events', 'event_time')` |
| **Retrieval** | Sequential replay, context reinstatement | Time-range queries + temporal validity tracking (`valid_from`/`valid_until`) |
| **Key insight** | Different decay rates encode different timescales | Hierarchical time buckets (seconds → minutes → hours → days) |

**AI systems**: TimescaleDB hypertables, InfluxDB, ring buffers (O(1) fixed-size windows), skip lists (Redis sorted sets for time-ordered retrieval). Temporal validity tracking ensures facts are time-scoped.

<!-- section_id: "a159932a-85d9-454a-a052-bbf164e62cff" -->
### 2.3 Episodic Memory (L5 — Builds on Semantic + Time-Based)

**What it stores**: Specific experiences — the "what happened" with full context (who, where, when, emotional valence).

| Aspect | Biological | AI Implementation |
|--------|-----------|-------------------|
| **Structure** | Event-segmented, context-bound episodes | Vector DB + time-indexed logs + key-value context |
| **Storage** | Hippocampus (binding), distributed cortex (consolidation) | Hypertable episodes with embeddings: `episodes(embedding vector(1536), event_time timestamptz, context jsonb)` |
| **Retrieval** | Cue-dependent, context reinstatement | Hybrid: semantic similarity + temporal range + metadata filters |
| **Key insight** | Event boundaries at prediction error spikes | Scene-based grouping, significance filtering (selective/sparse storage) |

**AI systems**: FAISS, Pinecone, ChromaDB for vector episodes. AWS Bedrock two-stage extraction (extract → consolidate). MongoDB AI Memory Service adds cognitive dynamics (importance scoring, temporal decay, reinforcement on access, memory merging). Mem^p stores distilled trajectories.

<!-- section_id: "e3968ea2-ec45-4c9a-aa4c-956baab1931a" -->
### 2.4 Procedural Memory (L5 — Builds on Semantic + Motor)

**What it stores**: Skills, routines, how-to knowledge — the "how" of doing things.

| Aspect | Biological | AI Implementation |
|--------|-----------|-------------------|
| **Structure** | Production rules (IF-THEN), motor sequences, chunk hierarchies | Skill registries + JSONB trajectory stores + procedural embeddings |
| **Storage** | Basal ganglia, cerebellum, supplementary motor area | `procedures(trajectory jsonb, embedding vector(1536), success_rate float)` + `skill_invocations` table |
| **Retrieval** | Automatic activation by context match | Vector similarity on procedural embeddings + invocation history |
| **Key insight** | Chunking: low→mid→high level skill composition | Mem^p framework: fine-grained + coarse-grained trajectory stores + proceduralization |

**AI systems**: Mem^p framework (+8 points success, 18% fewer steps, transfers across tasks). LangMem for persistent tool-use memory. Skill libraries/tool registries with invocation tracking. Production rules encode IF-THEN action sequences.

<!-- section_id: "773218cc-fce5-47f8-822d-b32f036805bf" -->
### 2.5 Memory Consolidation Pipeline (Cross-Type)

All four types feed through a shared consolidation pipeline:

```
Working Memory → [Extract] → [Consolidate] → [Store] → [Retrieve]
   (~20-40s)       (LLM)      (PostgreSQL)    (~200ms hybrid)
```

**Unified PostgreSQL**: All four types coexist in one database — pgvector for semantic, hypertables for temporal, JSONB for procedural, foreign keys for relationships. Cross-type JOIN queries enable holistic retrieval.

**Full detail**: `outputs/by_topic/25_ai_agent_implementations_per_memory_type.md`, `outputs/by_topic/26_long_term_storage_sql_schemas.md`

---

<!-- section_id: "2eff6f4a-a829-4b50-aaa7-0536456fa12f" -->
## 3. Core AI Memory Systems (9-Tier Ranking)

AI memory structures ranked from most to least foundational (T1-T3 support semantic+time-based, T4-T6 support episodic+procedural):

| Tier | System | Substitutable? | Used By |
|------|--------|---------------|---------|
| **T1** | Vector Embeddings | NO | All memory types |
| **T2** | Relational Tables (SQL) | NO | All memory types |
| **T3** | Knowledge Graphs | MAYBE | Semantic, some episodic |
| **T3.5** | SHIMI (Hierarchical Tree) | YES | Semantic |
| **T4** | Time-Series Stores | MAYBE | Episodic, temporal |
| **T5** | Working Memory Buffers | NO | All (staging area) |
| **T6** | Procedural / Skill Stores | YES | Procedural only |
| **T7** | Document Stores (JSONB) | YES | Flexible metadata |
| **T8** | Vector Indexes (HNSW) | YES | Search optimization |
| **T9** | Event Stores / Audit Logs | YES | Debugging/compliance |

**Minimal core**: Vectors + SQL + Working Memory = absolute minimum for any AI agent.

**Full detail**: `outputs/by_topic/23_core_ai_memory_systems.md`

---

<!-- section_id: "6fcd4e6c-7cd7-4257-8365-d49ff366e1da" -->
## 4. Data Structure Hierarchy (10 Levels)

Every AI memory system is built on layered data structures:

```
L0: Hardware (RAM, pointers)
L1: Fundamentals (arrays, linked lists, hash tables)
L2: Hierarchical (B-trees, heaps, tries)
L3: Sorted (skip lists, sorted arrays)
L4: Core AI (SQL tables, vectors, knowledge graphs)
L5: AI Indexes (HNSW, IVFFlat, inverted indexes)
L6: Temporal (hypertables, ring buffers)
L7: Caching (LRU, LFU, bloom filters)
L8: Flexible (JSONB, GIN)
L9: Composites (episodic store, semantic store, procedural store)
```

**Key insight**: Vector databases are actually graphs (HNSW). Everything reduces to arrays, trees, graphs, and hash tables.

**Full detail**: `outputs/by_topic/22_core_data_structure_hierarchy.md`, `outputs/by_topic/27_core_structures_nesting_analysis.md`, `outputs/by_topic/28_supporting_data_structures_deep_dive.md`

---

<!-- section_id: "bdecb5c1-06ab-4834-8cb1-1a68c5720cdd" -->
## 5. Technology × Memory Type Mapping

How each core technology serves each long-term memory type — and WHY that pairing works:

<!-- section_id: "dc43523e-a0c6-4690-a9dd-7277b0c60704" -->
### 5.1 Vector Embeddings (pgvector)

| Memory Type | How Used | Why It Works |
|-------------|----------|-------------|
| **Semantic** | Embed concepts/facts as vectors; cosine similarity retrieval | Captures meaning — "dog" is near "animal" in vector space. Primary retrieval mechanism for factual knowledge |
| **Time-based** | Embed temporal context vectors (TCM-inspired) | Drifting context vectors encode "what was happening around this time" — temporal similarity, not just exact timestamps |
| **Episodic** | Embed whole episodes for similarity search | Find "experiences like this one" — useful when exact time/place isn't known but the situation was similar |
| **Procedural** | Embed skill descriptions and tool-use trajectories | Match current task to previously successful procedures by semantic similarity, not just keyword matching |

**Why vectors are T1 (most foundational)**: Every memory type benefits from "find similar things" — it's the universal retrieval primitive. Without vectors, retrieval is limited to exact match or keyword search.

<!-- section_id: "e88f29b0-4a2e-43d9-8004-38952a291776" -->
### 5.2 Relational Tables (SQL / PostgreSQL)

| Memory Type | How Used | Why It Works |
|-------------|----------|-------------|
| **Semantic** | `semantic_memory` table with structured columns + pgvector column | ACID guarantees, JOINs across concepts, SQL querying for exact lookups ("get all facts about X") |
| **Time-based** | `temporal_events` hypertable with `event_time`, `valid_from`, `valid_until` | Time-range queries are what SQL does best. TimescaleDB optimizes for time-series. Temporal validity tracking (facts that expire) |
| **Episodic** | `episodes` hypertable with embeddings + timestamps + context JSONB | Combines time-ordering (hypertable) with semantic search (vector column) and rich metadata (JSONB). Cross-type JOINs link episodes to semantic facts |
| **Procedural** | `procedures` table with JSONB trajectories + `skill_invocations` tracking | Stores full execution traces as JSONB, tracks success rates per skill, enables performance analysis. Foreign keys link procedures to the knowledge they use |

**Why SQL is T2**: Provides structure, transactions, JOINs, constraints. Vectors find similar things; SQL organizes and relates them. Together they form the irreducible core.

<!-- section_id: "02c64059-cb3d-4930-acd2-6e8785e462db" -->
### 5.3 Knowledge Graphs (Neo4j or SQL Adjacency Lists)

| Memory Type | How Used | Why It Works |
|-------------|----------|-------------|
| **Semantic** | Entities + typed relationships (IS_A, HAS_PART, CAUSES) | Knowledge IS a graph — concepts connected by relationships. Graph traversal finds multi-hop connections that flat search misses |
| **Time-based** | Causal chains (event A → caused → event B) | Temporal causality is naturally a directed graph. Graph queries find "what led to what" |
| **Episodic** | Episode-to-entity links, participant graphs | "Who was involved in this episode?" — graph traversal connects episodes to people, places, concepts |
| **Procedural** | Skill dependency graphs, prerequisite chains | "Skill A requires Skill B" — DAG structure for skill composition and planning |

**Why KGs are T3 (MAYBE substitutable)**: KGs add explicit relationship modeling that vectors miss. A vector knows "dog" and "bone" are related but not HOW. A KG says `dog -[EATS]-> bone`. Critical for semantic memory, useful for others. Can be implemented as SQL adjacency lists (entities + relationships tables with recursive CTEs) — no need for separate Neo4j.

<!-- section_id: "03676579-58e3-4ff8-bb5a-a21792ebea46" -->
### 5.4 SHIMI (Semantic Hierarchical Memory Index)

| Memory Type | How Used | Why It Works |
|-------------|----------|-------------|
| **Semantic** | Hierarchical tree: abstract concepts at top, specific entities at bottom | Meaning-driven retrieval — traverse from abstract to specific. Explainable paths through the hierarchy. Superior to flat vector search for structured knowledge |
| **Time-based** | Temporal hierarchy: era → year → month → day → event | Natural time hierarchies map to tree structure. Drill-down from broad time period to specific moment |
| **Episodic** | Episode categorization: life phase → project → session → event | Autobiographical memory IS hierarchical — SHIMI mirrors this naturally |
| **Procedural** | Skill taxonomy: domain → capability → specific skill → variant | Hierarchical skill organization enables compositional reasoning about capabilities |

**Why SHIMI is T3.5**: Adds hierarchy and explainability that flat vectors and even KGs lack. Merkle-DAG sync enables decentralized multi-agent memory sharing. Bloom filter protocol speeds up relevance checks. CRDTs handle concurrent updates. Most impactful for semantic memory but applicable to all types.

<!-- section_id: "91d5594f-c5db-4f86-9ee7-36dfcb8d3403" -->
### 5.5 Summary Matrix

| Technology | Semantic | Time-Based | Episodic | Procedural | Primary Strength |
|------------|----------|------------|----------|------------|-----------------|
| **Vectors** | Find similar concepts | Temporal context similarity | Find similar experiences | Match tasks to skills | Universal "find similar" |
| **SQL** | Structured fact storage | Time-range queries, validity | Time-ordered episodes + JOINs | Trajectory storage, tracking | Structure + transactions |
| **Knowledge Graphs** | Typed relationships | Causal chains | Entity-episode links | Skill dependencies | Explicit relationships |
| **SHIMI** | Hierarchical meaning | Temporal drill-down | Episode categorization | Skill taxonomy | Hierarchy + explainability |

**Full detail**: `outputs/by_topic/23_core_ai_memory_systems.md`, `outputs/by_topic/27_core_structures_nesting_analysis.md`, `outputs/by_topic/36_technology_integration_roadmap.md`

---

<!-- section_id: "cef28c15-4450-45e7-83cc-d64ed5be6bf7" -->
## 6. Key Implementation Patterns

<!-- section_id: "6f1279fb-ed15-40a0-8fc1-02cb02d39aae" -->
### Unified PostgreSQL Architecture
Modern systems consolidate ALL memory in PostgreSQL:
- `pgvector` for semantic similarity
- `TimescaleDB` hypertables for episodic time-series
- `JSONB` for flexible procedural trajectories
- Foreign keys for knowledge graph edges
- **Result**: 66% cost reduction, single ACID transactions across all memory types

<!-- section_id: "6bf26767-214c-4f76-956d-e9f367589965" -->
### SHIMI (Semantic Hierarchical Memory Index)
- Hierarchical tree: abstract concepts at top, specific entities at bottom
- Meaning-driven retrieval (not just similarity)
- Explainable paths through hierarchy
- Decentralized sync via Merkle-DAG + Bloom filters + CRDTs

<!-- section_id: "a6397f01-5fa8-4471-90b6-c56b50b394ed" -->
### Memory Consolidation Pipeline
1. **Extraction** — identify what's worth remembering
2. **Consolidation** — merge related info, resolve conflicts
3. **Storage** — persist to appropriate tier
4. **Retrieval** — hybrid search (semantic + temporal + relational)

---

<!-- section_id: "a652517c-1a2a-41d6-8986-00a81e44a079" -->
## 7. Key Performance Benchmarks

| System | Metric | Value |
|--------|--------|-------|
| Mem0 | p95 latency reduction | 91% lower vs full-context |
| Mem0 | Token reduction | 90% |
| pgvector (DiskANN) | QPS at 99% recall (50M vectors) | 471 |
| Mem^p (procedural) | Success rate improvement | +8 points (71.9% → 79.9%) |
| Mem^p | Step reduction | 18% fewer steps |

---

<!-- section_id: "7d1faf74-ba8f-4c3f-be84-aa61926e0ae0" -->
## Research Document Index

<!-- section_id: "6de291f6-afdb-4a75-93dc-971a3fc3041d" -->
### Foundation (00-20)

| # | Document | Focus Area |
|---|----------|-----------|
| 00 | overview_and_taxonomy | Master taxonomy (Liu et al. 3D model) |
| 01 | cognitive_science_foundations | Human memory types, cognitive architectures |
| 02 | memory_by_duration | Sensory, short-term, long-term |
| 03 | memory_by_content_type | Semantic, episodic, procedural, entity |
| 04 | memory_dynamics_and_operations | How memory systems work |
| 05 | framework_implementations | LangChain, LlamaIndex, etc. |
| 06 | dedicated_memory_platforms | Mem0, Zep, MemGPT |
| 07 | commercial_ai_memory | ChatGPT, Claude, Gemini |
| 08 | multi_agent_memory | Multi-agent architectures |
| 09 | rag_and_knowledge_graphs | Retrieval systems |
| 10 | reflection_and_learning | Meta-learning |
| 11 | key_papers_and_references | Academic literature |
| 12 | benchmarks_and_performance | Evaluation metrics |
| 13 | practitioners_complete_guide | Comprehensive practical guide |
| 14 | memory_types_best_for_guide | When to use which type |
| 15 | vectors_graphs_and_neurology | Deep technical comparison |
| 16 | answer_traceability_log | Traceability and provenance |
| 17 | learning_path | Learning roadmap |
| 18 | underlying_data_structures | Individual structures (flat listing) |
| 19 | prototype_specification | Prototype design |
| 20 | three_tier_knowledge_architecture | 3-tier architecture |

<!-- section_id: "2722198b-a41e-44b4-b2e5-c813e1fcd126" -->
### Hierarchies & Core Systems (21-23)

| # | Document | Focus Area |
|---|----------|-----------|
| **21** | **core_memory_structure_hierarchy** | **Biological buildup (6 levels)** |
| **22** | **core_data_structure_hierarchy** | **Data structure layers (10 levels)** |
| **23** | **core_ai_memory_systems** | **AI system tiers (9 tiers + SHIMI)** |

<!-- section_id: "00947e7c-0bb1-4e02-8be6-a4028ff7f4ef" -->
### Deep Dives — Biology, Implementations, Schemas (24-28)

| # | Document | Focus Area |
|---|----------|-----------|
| **24** | **biological_data_structures_per_memory_type** | **Neuroscience structures: TCM, event segmentation, production rules** |
| **25** | **ai_agent_implementations_per_memory_type** | **AI implementations: episodic, time-based, procedural (Mem^p, LangMem)** |
| **26** | **long_term_storage_sql_schemas** | **Full SQL schemas: pgvector, hypertables, JSONB trajectories, consolidation pipeline** |
| **27** | **core_structures_nesting_analysis** | **How vectors/graphs/SQL nest inside PostgreSQL** |
| **28** | **supporting_data_structures_deep_dive** | **Bloom filters, skip lists, tries, ring buffers, LRU/LFU, heaps** |

<!-- section_id: "d9e5dbc1-abc0-45d1-aaa4-a7a80e9859f5" -->
### Real-World Systems & Implementations (29-31)

| # | Document | Focus Area |
|---|----------|-----------|
| **29** | **open_source_memory_implementations** | **Mem0, Eion, MemOS, MongoDB cognitive dynamics, Hindsight** |
| **30** | **complete_ai_agent_systems_with_memory** | **OASIS, CrewAI, LangGraph+LangMem, AutoGen, GenAI_Agents** |
| **31** | **personal_ai_tutor_systems** | **ATLAS, Mem0 Tutor, ChromaDB Tutor, AITutorAgent, ReMe** |

<!-- section_id: "2da2cb3c-ab2c-4af6-b9f6-d490cfc56321" -->
### Comparisons with Layer-Stage System (32-37)

| # | Document | Focus Area |
|---|----------|-----------|
| **32** | **comparison_context_chain_vs_commercial_memory** | **Context chain vs Mem0, LangMem, CrewAI, MongoDB** |
| **33** | **comparison_episodic_memory_approaches** | **User's episodic memory vs vector DB, time-indexed, cognitive dynamics** |
| **34** | **comparison_agent_delegation_patterns** | **Stage delegation vs AutoGen, CrewAI, LangGraph, OASIS** |
| **35** | **comparison_data_structures_user_vs_ideal** | **File-based system vs PostgreSQL/vectors/graphs ideal** |
| **36** | **technology_integration_roadmap** | **WHERE and HOW to integrate vectors, SQL, KGs, SHIMI into layer-stage** |
| **37** | **comparison_context_avenue_web_vs_commercial** | **8-avenue web vs Mem0, LangChain, CrewAI, RAG systems** |
