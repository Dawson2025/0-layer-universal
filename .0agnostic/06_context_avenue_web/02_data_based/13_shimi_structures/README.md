---
resource_id: "0ac601a9-362e-4e33-8423-ca205489bff9"
resource_type: "readme
document"
resource_name: "README"
---
# Avenue 13: SHIMI Structures

## Purpose

Per-node optimization primitives for intelligent context navigation and multi-device sync — Bloom filters, Merkle-DAG, CRDTs.

## Comprehensiveness Level

**Most fragmented** data-based avenue — individual artifacts per entity for specific operations.

## Data Source

- Context chain (hierarchy of 0AGNOSTIC.md files)
- Entity content hashes
- Sync state across devices (Syncthing)

## Components

**Bloom Filters**: Per-entity probabilistic filter of content keywords. Before loading an ancestor's DYNAMIC context, check: `bloom_filter.might_contain("topic")`. If false, skip loading entirely. Estimated token savings: 2000+ tokens per skipped ancestor.

**Merkle-DAG**: Hash tree where each entity's hash = SHA256(own_content + children_hashes). Detect which subtrees changed since last sync. Enables efficient `agnostic-sync.sh --recursive` — only process changed subtrees.

**CRDTs**: Conflict-free Replicated Data Types for multi-device editing via Syncthing:
- LWW-Register for scalar values (status, last_updated)
- G-Counter for monotonic values (stage_number, invocation_count)
- OR-Set for collections (file lists, tag sets)

## Build Command

```bash
sync-main.sh --avenue 13
# or: build-shimi.sh <directory>
```

## Query Interface

Pre-check integration into context-gathering skill.

## Dependencies

- Python or Bash (Bloom filter generator)
- SHA256 (Merkle hash calculator)
- CRDT library (for multi-device sync — Phase 4)

## Status

**Scaffolded** — directory exists, no scripts or data yet. Implementation in stage 06 (development).

## Design Reference

- `stage_2_05_design/outputs/by_topic/02_data_avenue_web_expansion.md`
- SHIMI paper: arXiv:2504.06135
