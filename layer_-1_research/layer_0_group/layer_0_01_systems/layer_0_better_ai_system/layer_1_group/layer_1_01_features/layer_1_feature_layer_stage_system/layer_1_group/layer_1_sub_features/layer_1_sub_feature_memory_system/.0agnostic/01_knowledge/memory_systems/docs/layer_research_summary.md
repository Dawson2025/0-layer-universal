---
resource_id: "95228e50-d96e-4571-b9ad-a546065fb3ea"
resource_type: "knowledge"
resource_name: "layer_research_summary"
---
# Layer Research Summary: Memory System

<!-- section_id: "0741069e-1239-49eb-ba81-fe7998146ab6" -->
## Overview

Stage 02 (research) produced a comprehensive investigation into AI agent memory systems. The research spans 24 documents totaling approximately 350KB of distilled knowledge, covering biological foundations, cognitive science mappings, implementation architectures, data structures, commercial platforms, and performance benchmarks.

The research is substantially complete and ready to inform downstream stages (03_instructions, 04_planning, 05_design).

---

<!-- section_id: "c6984d40-fccb-4267-bdd7-09c6a92ec491" -->
## Research Scope

<!-- section_id: "6b3c883e-d446-4565-9143-29e194360ad2" -->
### Documents Produced

24 research documents (`outputs/by_topic/00-23`) organized by topic:

| Range | Focus Area |
|-------|-----------|
| 00-04 | Foundations: taxonomy, cognitive science, duration-based memory, content-based memory, memory dynamics |
| 05-08 | Implementations: frameworks (LangChain, LlamaIndex), dedicated platforms (Mem0, Zep, MemGPT), commercial AI (ChatGPT, Claude, Gemini), multi-agent architectures |
| 09-12 | Techniques: RAG and knowledge graphs, reflection and learning, key papers, benchmarks and performance |
| 13-17 | Guides: practitioner's guide, memory type selection guide, vectors vs graphs vs neurology, traceability, learning path |
| 18-20 | Architecture: underlying data structures, prototype specification, three-tier knowledge architecture |
| 21-23 | Core syntheses: memory structure hierarchy, data structure hierarchy, core AI memory systems |

<!-- section_id: "bfe5b312-bb6d-43dc-9cc9-e2e6d1cdb683" -->
### Distilled Knowledge

Stage-level knowledge summary: `stage_1_02_research/.0agnostic/01_knowledge/memory_systems/docs/core_ai_memory_architecture.md`

---

<!-- section_id: "8d3cd832-bf8b-406d-99e8-d9beca5ac2af" -->
## Key Architectural Findings

<!-- section_id: "7649b71e-e641-4652-bc54-356dd9a7d768" -->
### 1. Biological Memory Hierarchy (6 Levels)

Memory types form a strict dependency chain where each level requires the levels below:

| Level | Memory Type | Design Implication |
|-------|-------------|-------------------|
| L1 | Sensory Memory | Raw input processing |
| L2 | Reflexes & Conditioning | Simple stimulus-response |
| L3 | Motor Memory | Coordinated patterns |
| L4 | Core Systems (4 parallel) | Semantic, time-based, spatial, emotional |
| L5 | Complex Integrations (3) | Procedural, episodic, predictive |
| L6 | Autobiographical | Integrates all below into personal narrative |

**Build order**: L4 (semantic + time-based) first, then L5 (episodic + procedural), then L6.

<!-- section_id: "c2e9e151-4d64-437f-9b88-ccf7dcb2737f" -->
### 2. Data Structure Hierarchy (10 Levels)

Every AI memory system is built on layered data structures:

- L0-L1: Hardware primitives and fundamentals (arrays, linked lists, hash tables)
- L2-L3: Hierarchical and sorted structures (B-trees, heaps, skip lists)
- L4-L5: Core AI structures and indexes (SQL tables, vectors, HNSW, IVFFlat)
- L6-L7: Temporal and caching layers (hypertables, ring buffers, LRU/LFU)
- L8-L9: Flexible and composite stores (JSONB, episodic/semantic/procedural stores)

**Key insight**: Vector databases are actually graphs (HNSW). Everything reduces to arrays, trees, graphs, and hash tables.

<!-- section_id: "84036446-4350-441f-9c28-24472a73cf9d" -->
### 3. Core AI Memory Systems (9 Tiers)

AI memory structures ranked by foundational importance:

| Tier | System | Substitutable? |
|------|--------|---------------|
| T1 | Vector Embeddings | NO |
| T2 | Relational Tables (SQL) | NO |
| T3 | Knowledge Graphs | MAYBE |
| T3.5 | SHIMI (Hierarchical Tree) | YES |
| T4 | Time-Series Stores | MAYBE |
| T5 | Working Memory Buffers | NO |
| T6 | Procedural / Skill Stores | YES |
| T7 | Document Stores (JSONB) | YES |
| T8 | Vector Indexes (HNSW) | YES |
| T9 | Event Stores / Audit Logs | YES |

**Minimal core**: Vectors (T1) + SQL (T2) + Working Memory (T5) = absolute minimum for any AI agent.

<!-- section_id: "b5855cdf-d63b-49cb-8eae-b837b86c3a12" -->
### 4. SHIMI (Semantic Hierarchical Memory Index)

Positioned at T3.5, SHIMI provides meaning-driven retrieval superior to flat vector search:

- Hierarchical tree structure: abstract concepts at top, specific entities at bottom
- Meaning-driven retrieval (not just cosine similarity)
- Explainable paths through the hierarchy
- Decentralized sync via Merkle-DAG + Bloom filters + CRDTs

<!-- section_id: "e66b80bc-719a-4a51-ae1f-ef600c446b47" -->
### 5. Unified PostgreSQL Architecture

Modern production systems consolidate ALL memory types in PostgreSQL:

- `pgvector` for semantic similarity search
- `TimescaleDB` hypertables for episodic time-series data
- `JSONB` for flexible procedural trajectories
- Foreign keys for knowledge graph edges
- **Result**: 66% cost reduction, single ACID transactions across all memory types

<!-- section_id: "cc35bb84-7198-4611-87a0-32018f2b932f" -->
### 6. Memory Consolidation Pipeline (4 Stages)

The standard architecture for memory processing:

1. **Extraction** -- identify what is worth remembering from interactions
2. **Consolidation** -- merge related information, resolve conflicts
3. **Storage** -- persist to appropriate tier (vector, relational, time-series)
4. **Retrieval** -- hybrid search combining semantic, temporal, and relational queries

---

<!-- section_id: "d8f90995-0017-4924-bed0-809f6df3bd58" -->
## Key Performance Benchmarks

| System | Metric | Value |
|--------|--------|-------|
| Mem0 | p95 latency reduction | 91% lower vs full-context |
| Mem0 | Token reduction | 90% |
| pgvector (DiskANN) | QPS at 99% recall (50M vectors) | 471 |
| Mem^p (procedural) | Success rate improvement | +8 points (71.9% to 79.9%) |
| Mem^p | Step reduction | 18% fewer steps |

---

<!-- section_id: "fbf56047-ff8f-4eec-8ec0-d56143266a3d" -->
## Phase Recommendations

<!-- section_id: "4fcd166d-999f-4e62-86d2-fe14678f70aa" -->
### Phase 1: Minimal Core
- Vector Embeddings (T1) for semantic similarity
- SQL/Relational (T2) for structured data
- Working Memory Buffers (T5) for active context
- Unified PostgreSQL as the storage backend

<!-- section_id: "5631b8fc-f573-4601-b194-4164af0dccb9" -->
### Phase 2: Enhanced Memory
- SHIMI (T3.5) for meaning-driven hierarchical retrieval
- Procedural Memory (T6) for learning from task trajectories
- Time-Series Stores (T4) for episodic memory
- 4-stage consolidation pipeline

---

<!-- section_id: "9725d1d8-2f8a-4c91-8df0-a24f5be06533" -->
## Cross-References

| Resource | Location |
|----------|----------|
| Stage report | `layer_1_group/layer_1_99_stages/stage_1_02_research/.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` |
| Stage knowledge summary | `layer_1_group/layer_1_99_stages/stage_1_02_research/.0agnostic/01_knowledge/memory_systems/docs/core_ai_memory_architecture.md` |
| Research documents | `layer_1_group/layer_1_99_stages/stage_1_02_research/outputs/by_topic/` (24 documents, 00-23) |
| Stage 02 0AGNOSTIC.md | `layer_1_group/layer_1_99_stages/stage_1_02_research/0AGNOSTIC.md` |
