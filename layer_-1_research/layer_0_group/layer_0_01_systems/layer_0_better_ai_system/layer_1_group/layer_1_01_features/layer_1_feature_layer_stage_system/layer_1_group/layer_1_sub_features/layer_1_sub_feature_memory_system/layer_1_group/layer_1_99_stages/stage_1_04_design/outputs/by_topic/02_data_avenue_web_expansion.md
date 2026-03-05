---
resource_id: "a5080c10-e719-450f-bdf9-3a225d70d5be"
resource_type: "output"
resource_name: "02_data_avenue_web_expansion"
---
# Data-Based Avenue Web Expansion (Avenues 09-13)

<!-- section_id: "5bda27f7-c920-422d-8c96-9c45a92eb75b" -->
## Overview

The context avenue web currently has 8 file-based avenues (01-08) ordered from most comprehensive to most fragmented. This document designs 5 data-based avenues (09-13) that extend the web with derived indexes — queryable databases built FROM file-based content.

<!-- section_id: "b774cab6-ce65-4293-a9ad-ff0b485095e0" -->
## Design Principle

**File-based avenues** answer: "What IS the context?" (source of truth, human-editable, version-controlled)

**Data-based avenues** answer: "How do I FIND the right context?" (search, query, filter, rank)

Data-based avenues are:
- **Derived**: Always regenerable from files. Delete the database, rebuild from source.
- **Optional**: The system works without them. They are accelerators, not requirements.
- **Additive**: They never modify files. Information flows one way: files → databases.

<!-- section_id: "ec74cb2d-f822-4b7e-b563-713a68a550a6" -->
## Comprehensiveness Ordering

| Avenue | Name | What It Models | Why This Position |
|--------|------|----------------|-------------------|
| **09** | Knowledge Graph | Full structural model — entities, relationships, dependencies, typed edges | Most comprehensive: captures the entire system topology with explicit relationship types |
| **10** | Relational Index | Tabular metadata — entity status, stage reports, skill inventory, rule inventory | Broad coverage but flat: every entity gets a row, but no relationship depth |
| **11** | Vector Embeddings | Semantic fingerprints — meaning compressed to dimensional space | Broad but lossy: covers all text content but reduces to similarity scores |
| **12** | Temporal Index | Time-series — sessions, events, changes ordered chronologically | Partial scope: only models the WHEN dimension, not WHAT or WHY |
| **13** | SHIMI Structures | Per-node optimization primitives — Bloom filters, Merkle hashes, CRDTs | Most fragmented: individual artifacts per entity for specific operations |

The ordering mirrors file-based: avenue 01 (full agent graphs) is the most comprehensive file-based avenue, avenue 08 (hooks) is the most fragmented. Avenue 09 (knowledge graph) is the most comprehensive data-based avenue, avenue 13 (SHIMI) is the most fragmented.

<!-- section_id: "3b625aa0-374a-43b0-9ab9-ad15e2c7f678" -->
## Avenue 09: Knowledge Graph

<!-- section_id: "e4edfa8d-487f-4b71-9529-7ef66df75f83" -->
### Purpose
Explicit typed relationships between all system entities — enables structural queries, impact analysis, and dependency visualization.

<!-- section_id: "3886d0b5-dbe7-45ad-9974-28840b75dd10" -->
### Data Source
- Entity hierarchy (directories with 0AGNOSTIC.md)
- JSON-LD agent definitions (.gab.jsonld)
- Cross-references in 0AGNOSTIC.md (Parent, Children, Inputs, Outputs)
- Skill WHEN conditions (maps skills to entity types)
- Rule scoping (which rules apply where)

<!-- section_id: "ab796096-2cc2-4615-855c-0053ce3186e2" -->
### Schema (Graph Nodes and Edges)

**Node types**: Entity, Stage, Skill, Rule, Protocol, Knowledge_Doc, Agent_Definition

**Edge types**:
- `CHILD_OF` (entity → parent entity)
- `HAS_STAGE` (entity → stage)
- `PRODUCES` (stage → output document)
- `DEPENDS_ON` (entity → entity)
- `APPLIES_TO` (rule → entity scope)
- `MATCHES` (skill → entity type)
- `DELEGATES_TO` (manager → stage agent)
- `REFERENCES` (document → document)

<!-- section_id: "8d7e425d-ef88-4e4a-8c0c-9322e9dd0fa5" -->
### Implementation
- **Phase 1** (scaffold): Directory + README
- **Phase 2** (build): Extract relationships from 0AGNOSTIC.md + JSON-LD via script
- **Phase 3** (query): SQL adjacency lists in SQLite (portable, zero-server) or PostgreSQL for production

<!-- section_id: "1376beb4-cdca-42aa-b5be-73ba57faea45" -->
### Research Basis
Research docs 34 (agent delegation patterns), 35 (data structures comparison), 37 (avenue web vs commercial)

<!-- section_id: "ba0cca07-33cf-48e9-aae7-8609f386d53e" -->
## Avenue 10: Relational Index

<!-- section_id: "d8b8d812-78e4-4cfb-8e23-2f4aa0b9477e" -->
### Purpose
Structured SQL tables of queryable metadata across all entities — enables dashboards, status queries, and inventory reports.

<!-- section_id: "7d571fee-0451-4cdd-94f0-815969f1139f" -->
### Data Source
- 0AGNOSTIC.md Identity sections (entity name, layer, role, scope, status)
- Stage reports (stage_report.md: status, last_updated, summary, open_items)
- Episodic memory sessions (date, duration, topics, files_changed)
- Skill inventory (name, WHEN conditions, last_used, success_rate)
- Rule inventory (name, importance, scope, trigger_conditions)

<!-- section_id: "cf502060-60b9-498f-b5ee-3b44e2d987b6" -->
### Schema (SQL Tables)

```sql
entities (id, name, layer, parent_id, role, scope, status, agnostic_path, last_updated)
stage_reports (id, entity_id, stage_number, stage_name, status, summary, last_updated)
sessions (id, entity_id, session_date, agent_type, topics, files_changed, decisions)
skills (id, name, description, when_conditions, last_used, invocation_count, success_rate)
rules (id, name, importance_level, scope, trigger_conditions, content_hash)
```

<!-- section_id: "20f490df-bc78-409b-be5d-ba2aa4022661" -->
### Implementation
- **Phase 1** (scaffold): Directory + README
- **Phase 2** (build): Parse markdown files via awk/grep into SQL INSERT statements
- **Phase 3** (query): SQLite for local use, PostgreSQL for multi-agent shared access

<!-- section_id: "e5335259-ac9a-4156-8b30-e65c33d57058" -->
### Research Basis
Research doc 36 (technology integration roadmap — PostgreSQL entity registry, stage reports, sessions tables)

<!-- section_id: "9c101561-9918-4c09-8c1e-b5bc37149d90" -->
## Avenue 11: Vector Embeddings

<!-- section_id: "5dadadac-db7f-405d-b03a-1f6ab165e794" -->
### Purpose
Semantic similarity search across all text content — enables "find everything about X" queries without knowing file paths.

<!-- section_id: "aa5c5ee3-5e00-4d9d-a9af-9eeb6945f651" -->
### Data Source
- All `.0agnostic/01_knowledge/` documents
- All 0AGNOSTIC.md sections (STATIC content)
- Skill SKILL.md descriptions
- Research documents in `outputs/by_topic/`
- Stage reports
- Episodic memory session files

<!-- section_id: "5243b0ce-c579-43ec-ad50-6c7e6622e58b" -->
### Schema (Embedding Tables)

```sql
content_embeddings (
  id, source_path, source_section, chunk_text,
  embedding vector(1536),  -- or 3072 for newer models
  avenue_type,             -- which avenue the source belongs to
  entity_path,             -- which entity this content is in
  last_updated
)
```

<!-- section_id: "d7bff61f-0a24-4324-bd5f-1ed22b49b687" -->
### Key Feature: Avenue-Weighted Search

When searching, results are weighted by the source avenue's comprehensiveness:
```
effective_score = cosine_similarity × avenue_weight

Avenue weights: 01=1.0, 02=0.9, 03=0.8, ..., 08=0.3
```

This ensures that a match in AALang (avenue 01) ranks higher than the same cosine similarity in hooks (avenue 08).

<!-- section_id: "752afeb7-0808-4f78-9216-139ce989caec" -->
### Implementation
- **Phase 1** (scaffold): Directory + README
- **Phase 2** (build): Chunk documents, call embedding API, store in pgvector
- **Phase 3** (query): Semantic search CLI + integration into context-gathering skill

<!-- section_id: "1f7eb354-b077-4b54-8351-c7ca294a1fc3" -->
### Research Basis
Research docs 32 (context chain vs commercial — semantic search gap), 35 (data structures — vector overlay), 36 (pgvector integration), 37 (avenue web — intra/cross-avenue search)

<!-- section_id: "161eb024-89e7-46e4-992f-5dc02daf9255" -->
## Avenue 12: Temporal Index

<!-- section_id: "807e29f1-4b4e-429d-b51d-3261f176a68f" -->
### Purpose
Time-series views of system activity — enables "what happened this week?", decay/reinforcement, and temporal range queries.

<!-- section_id: "742ce450-d410-45a4-b5e7-bd30e30a1f67" -->
### Data Source
- `.0agnostic/04_episodic_memory/` session files (timestamps, topics, changes)
- Stage reports (status transitions with dates)
- Git commit history (file changes over time)
- Skill trajectory stores (invocation timestamps)

<!-- section_id: "465ec4b7-194c-47ad-b257-2d7eba04631e" -->
### Schema (Hypertable)

```sql
-- TimescaleDB hypertable (or regular SQL with timestamp indexes)
events (
  id, entity_path, event_type,
  timestamp TIMESTAMPTZ,
  agent_type, summary, details_json,
  importance FLOAT DEFAULT 0.5,
  decay_factor FLOAT DEFAULT 1.0
)

-- Materialized view for time buckets
events_daily AS (
  SELECT time_bucket('1 day', timestamp) AS day,
         entity_path, event_type, COUNT(*), AVG(importance)
  FROM events GROUP BY 1, 2, 3
)
```

<!-- section_id: "a979a737-b97d-4f88-b031-e35a39583c0a" -->
### Key Feature: Cognitive Dynamics

Inspired by MongoDB AI Memory (research doc 29):
- **Decay**: `effective_importance = importance × decay_factor^(days_since_event)`
- **Reinforcement**: When a session references an old event, its importance increases
- **Consolidation**: Old events with similar topics merge into summary events

<!-- section_id: "821676c6-49bc-4d36-a0e3-b18f47635557" -->
### Implementation
- **Phase 1** (scaffold): Directory + README
- **Phase 2** (build): Parse episodic files + git log into events table
- **Phase 3** (query): Temporal range queries, decay-weighted retrieval

<!-- section_id: "f9dca9b3-e401-4caa-bbd2-537ec699ab49" -->
### Research Basis
Research docs 24 (biological data structures — TCM temporal context), 25 (AI implementations — TimescaleDB), 33 (episodic memory approaches)

<!-- section_id: "1b1513a7-8c2c-4322-a858-9209d275bee2" -->
## Avenue 13: SHIMI Structures

<!-- section_id: "930b73f7-e213-4464-8348-403e430fff75" -->
### Purpose
Per-node optimization primitives for intelligent context navigation and multi-device sync — Bloom filters, Merkle-DAG, CRDTs.

<!-- section_id: "cfdb9fd8-73da-47fc-bc4f-55ded99ae79a" -->
### Data Source
- Context chain (hierarchy of 0AGNOSTIC.md files)
- Entity content hashes
- Sync state across devices (Syncthing)

<!-- section_id: "666320b8-4062-4078-9395-39bb32d884ec" -->
### Components

**Bloom Filters**: Per-entity probabilistic filter of content keywords. Before loading an ancestor's DYNAMIC context, check: `bloom_filter.might_contain("memory decay")`. If false, skip loading entirely. Estimated token savings: 2000+ tokens per skipped ancestor.

**Merkle-DAG**: Hash tree where each entity's hash = SHA256(own_content + children_hashes). Detect which subtrees changed since last sync by comparing root hashes. Enables efficient `agnostic-sync.sh --recursive` — only process changed subtrees.

**CRDTs**: Conflict-free Replicated Data Types for multi-device editing via Syncthing:
- LWW-Register for scalar values (status, last_updated)
- G-Counter for monotonic values (stage_number, invocation_count)
- OR-Set for collections (file lists, tag sets)

<!-- section_id: "d81e2298-c7b3-4ce4-8c07-6ab613132151" -->
### Implementation
- **Phase 1** (scaffold): Directory + README
- **Phase 2** (build): Bloom filter generator + Merkle hash calculator
- **Phase 3** (query): Pre-check integration into context-gathering skill
- **Phase 4** (CRDT): Conflict resolution layer for Syncthing

<!-- section_id: "1d5d0aa8-fbd0-4fcb-bc93-ed18b39a6b65" -->
### Research Basis
Research doc 23 (9-tier AI memory — SHIMI T3.5), research doc 36 (SHIMI integration points), SHIMI paper (arXiv:2504.06135)

<!-- section_id: "a3e9983d-3077-401b-ac77-dd26e6d55151" -->
## Phase Rollout

| Phase | What | When | Risk |
|-------|------|------|------|
| **Scaffold** | Directories + READMEs for 09-13 | Now (design stage) | Zero — no functional changes |
| **Build Scripts** | Extract/parse/embed pipeline per avenue | Stage 06 (development) | Low — additive only |
| **Query Interfaces** | CLI tools for each avenue | Stage 06 (development) | Low — read-only |
| **Integration** | Hook into context-gathering skill, sync-main.sh | Stage 06 (development) | Medium — changes agent behavior |
| **Production** | Default-on for data-based avenues | After stage 07 (testing) | Medium — performance dependency |

<!-- section_id: "b631e69d-6ece-4c96-ac60-0760636fe76d" -->
## Sources

- Research docs 23, 24, 25, 29, 32-37 (memory system research stage 02)
- SHIMI paper: arXiv:2504.06135
- Mem0 documentation: https://docs.mem0.ai/
- pgvector documentation: https://github.com/pgvector/pgvector
- TimescaleDB documentation: https://docs.timescale.com/
