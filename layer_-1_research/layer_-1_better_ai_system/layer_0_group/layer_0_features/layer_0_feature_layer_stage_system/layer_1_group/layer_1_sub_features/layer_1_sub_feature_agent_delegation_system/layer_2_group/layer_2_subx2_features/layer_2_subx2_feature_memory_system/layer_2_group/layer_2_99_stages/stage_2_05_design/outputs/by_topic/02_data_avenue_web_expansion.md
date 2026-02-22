# Data-Based Avenue Web Expansion (Avenues 09-13)

## Overview

The context avenue web currently has 8 file-based avenues (01-08) ordered from most comprehensive to most fragmented. This document designs 5 data-based avenues (09-13) that extend the web with derived indexes — queryable databases built FROM file-based content.

## Design Principle

**File-based avenues** answer: "What IS the context?" (source of truth, human-editable, version-controlled)

**Data-based avenues** answer: "How do I FIND the right context?" (search, query, filter, rank)

Data-based avenues are:
- **Derived**: Always regenerable from files. Delete the database, rebuild from source.
- **Optional**: The system works without them. They are accelerators, not requirements.
- **Additive**: They never modify files. Information flows one way: files → databases.

## Comprehensiveness Ordering

| Avenue | Name | What It Models | Why This Position |
|--------|------|----------------|-------------------|
| **09** | Knowledge Graph | Full structural model — entities, relationships, dependencies, typed edges | Most comprehensive: captures the entire system topology with explicit relationship types |
| **10** | Relational Index | Tabular metadata — entity status, stage reports, skill inventory, rule inventory | Broad coverage but flat: every entity gets a row, but no relationship depth |
| **11** | Vector Embeddings | Semantic fingerprints — meaning compressed to dimensional space | Broad but lossy: covers all text content but reduces to similarity scores |
| **12** | Temporal Index | Time-series — sessions, events, changes ordered chronologically | Partial scope: only models the WHEN dimension, not WHAT or WHY |
| **13** | SHIMI Structures | Per-node optimization primitives — Bloom filters, Merkle hashes, CRDTs | Most fragmented: individual artifacts per entity for specific operations |

The ordering mirrors file-based: avenue 01 (full agent graphs) is the most comprehensive file-based avenue, avenue 08 (hooks) is the most fragmented. Avenue 09 (knowledge graph) is the most comprehensive data-based avenue, avenue 13 (SHIMI) is the most fragmented.

## Avenue 09: Knowledge Graph

### Purpose
Explicit typed relationships between all system entities — enables structural queries, impact analysis, and dependency visualization.

### Data Source
- Entity hierarchy (directories with 0AGNOSTIC.md)
- JSON-LD agent definitions (.gab.jsonld)
- Cross-references in 0AGNOSTIC.md (Parent, Children, Inputs, Outputs)
- Skill WHEN conditions (maps skills to entity types)
- Rule scoping (which rules apply where)

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

### Implementation
- **Phase 1** (scaffold): Directory + README
- **Phase 2** (build): Extract relationships from 0AGNOSTIC.md + JSON-LD via script
- **Phase 3** (query): SQL adjacency lists in SQLite (portable, zero-server) or PostgreSQL for production

### Research Basis
Research docs 34 (agent delegation patterns), 35 (data structures comparison), 37 (avenue web vs commercial)

## Avenue 10: Relational Index

### Purpose
Structured SQL tables of queryable metadata across all entities — enables dashboards, status queries, and inventory reports.

### Data Source
- 0AGNOSTIC.md Identity sections (entity name, layer, role, scope, status)
- Stage reports (stage_report.md: status, last_updated, summary, open_items)
- Episodic memory sessions (date, duration, topics, files_changed)
- Skill inventory (name, WHEN conditions, last_used, success_rate)
- Rule inventory (name, importance, scope, trigger_conditions)

### Schema (SQL Tables)

```sql
entities (id, name, layer, parent_id, role, scope, status, agnostic_path, last_updated)
stage_reports (id, entity_id, stage_number, stage_name, status, summary, last_updated)
sessions (id, entity_id, session_date, agent_type, topics, files_changed, decisions)
skills (id, name, description, when_conditions, last_used, invocation_count, success_rate)
rules (id, name, importance_level, scope, trigger_conditions, content_hash)
```

### Implementation
- **Phase 1** (scaffold): Directory + README
- **Phase 2** (build): Parse markdown files via awk/grep into SQL INSERT statements
- **Phase 3** (query): SQLite for local use, PostgreSQL for multi-agent shared access

### Research Basis
Research doc 36 (technology integration roadmap — PostgreSQL entity registry, stage reports, sessions tables)

## Avenue 11: Vector Embeddings

### Purpose
Semantic similarity search across all text content — enables "find everything about X" queries without knowing file paths.

### Data Source
- All `.0agnostic/01_knowledge/` documents
- All 0AGNOSTIC.md sections (STATIC content)
- Skill SKILL.md descriptions
- Research documents in `outputs/by_topic/`
- Stage reports
- Episodic memory session files

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

### Key Feature: Avenue-Weighted Search

When searching, results are weighted by the source avenue's comprehensiveness:
```
effective_score = cosine_similarity × avenue_weight

Avenue weights: 01=1.0, 02=0.9, 03=0.8, ..., 08=0.3
```

This ensures that a match in AALang (avenue 01) ranks higher than the same cosine similarity in hooks (avenue 08).

### Implementation
- **Phase 1** (scaffold): Directory + README
- **Phase 2** (build): Chunk documents, call embedding API, store in pgvector
- **Phase 3** (query): Semantic search CLI + integration into context-gathering skill

### Research Basis
Research docs 32 (context chain vs commercial — semantic search gap), 35 (data structures — vector overlay), 36 (pgvector integration), 37 (avenue web — intra/cross-avenue search)

## Avenue 12: Temporal Index

### Purpose
Time-series views of system activity — enables "what happened this week?", decay/reinforcement, and temporal range queries.

### Data Source
- `.0agnostic/04_episodic_memory/` session files (timestamps, topics, changes)
- Stage reports (status transitions with dates)
- Git commit history (file changes over time)
- Skill trajectory stores (invocation timestamps)

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

### Key Feature: Cognitive Dynamics

Inspired by MongoDB AI Memory (research doc 29):
- **Decay**: `effective_importance = importance × decay_factor^(days_since_event)`
- **Reinforcement**: When a session references an old event, its importance increases
- **Consolidation**: Old events with similar topics merge into summary events

### Implementation
- **Phase 1** (scaffold): Directory + README
- **Phase 2** (build): Parse episodic files + git log into events table
- **Phase 3** (query): Temporal range queries, decay-weighted retrieval

### Research Basis
Research docs 24 (biological data structures — TCM temporal context), 25 (AI implementations — TimescaleDB), 33 (episodic memory approaches)

## Avenue 13: SHIMI Structures

### Purpose
Per-node optimization primitives for intelligent context navigation and multi-device sync — Bloom filters, Merkle-DAG, CRDTs.

### Data Source
- Context chain (hierarchy of 0AGNOSTIC.md files)
- Entity content hashes
- Sync state across devices (Syncthing)

### Components

**Bloom Filters**: Per-entity probabilistic filter of content keywords. Before loading an ancestor's DYNAMIC context, check: `bloom_filter.might_contain("memory decay")`. If false, skip loading entirely. Estimated token savings: 2000+ tokens per skipped ancestor.

**Merkle-DAG**: Hash tree where each entity's hash = SHA256(own_content + children_hashes). Detect which subtrees changed since last sync by comparing root hashes. Enables efficient `agnostic-sync.sh --recursive` — only process changed subtrees.

**CRDTs**: Conflict-free Replicated Data Types for multi-device editing via Syncthing:
- LWW-Register for scalar values (status, last_updated)
- G-Counter for monotonic values (stage_number, invocation_count)
- OR-Set for collections (file lists, tag sets)

### Implementation
- **Phase 1** (scaffold): Directory + README
- **Phase 2** (build): Bloom filter generator + Merkle hash calculator
- **Phase 3** (query): Pre-check integration into context-gathering skill
- **Phase 4** (CRDT): Conflict resolution layer for Syncthing

### Research Basis
Research doc 23 (9-tier AI memory — SHIMI T3.5), research doc 36 (SHIMI integration points), SHIMI paper (arXiv:2504.06135)

## Phase Rollout

| Phase | What | When | Risk |
|-------|------|------|------|
| **Scaffold** | Directories + READMEs for 09-13 | Now (design stage) | Zero — no functional changes |
| **Build Scripts** | Extract/parse/embed pipeline per avenue | Stage 06 (development) | Low — additive only |
| **Query Interfaces** | CLI tools for each avenue | Stage 06 (development) | Low — read-only |
| **Integration** | Hook into context-gathering skill, sync-main.sh | Stage 06 (development) | Medium — changes agent behavior |
| **Production** | Default-on for data-based avenues | After stage 07 (testing) | Medium — performance dependency |

## Sources

- Research docs 23, 24, 25, 29, 32-37 (memory system research stage 02)
- SHIMI paper: arXiv:2504.06135
- Mem0 documentation: https://docs.mem0.ai/
- pgvector documentation: https://github.com/pgvector/pgvector
- TimescaleDB documentation: https://docs.timescale.com/
