---
resource_id: "0ac601a9-362e-4e33-8423-ca205489bff9"
resource_type: "readme
document"
resource_name: "README"
---
# Avenue 13: SHIMI Structures

<!-- section_id: "d367954b-2af1-4f7c-9f04-ef74b695bb18" -->
## Purpose

Per-node optimization primitives for intelligent context navigation and multi-device sync — Bloom filters, Merkle-DAG, CRDTs.

<!-- section_id: "d41c470b-8c1b-4083-9914-4c1757ca14fc" -->
## Comprehensiveness Level

**Most fragmented** data-based avenue — individual artifacts per entity for specific operations.

<!-- section_id: "d45dff87-b418-4d42-806f-a5e0a387287c" -->
## Data Source

- Context chain (hierarchy of 0AGNOSTIC.md files)
- Entity content hashes
- Sync state across devices (Syncthing)

<!-- section_id: "4d919afe-b36e-488f-a7c8-d1d713760f24" -->
## Components

**Bloom Filters**: Per-entity probabilistic filter of content keywords. Before loading an ancestor's DYNAMIC context, check: `bloom_filter.might_contain("topic")`. If false, skip loading entirely. Estimated token savings: 2000+ tokens per skipped ancestor.

**Merkle-DAG**: Hash tree where each entity's hash = SHA256(own_content + children_hashes). Detect which subtrees changed since last sync. Enables efficient `agnostic-sync.sh --recursive` — only process changed subtrees.

**CRDTs**: Conflict-free Replicated Data Types for multi-device editing via Syncthing:
- LWW-Register for scalar values (status, last_updated)
- G-Counter for monotonic values (stage_number, invocation_count)
- OR-Set for collections (file lists, tag sets)

<!-- section_id: "c0298cdf-20bd-494a-aca5-9924fdd22fa2" -->
## Build Command

```bash
sync-main.sh --avenue 13
# or: build-shimi.sh <directory>
```

<!-- section_id: "6387ed38-a89a-463d-974d-93b7e6c73726" -->
## Query Interface

Pre-check integration into context-gathering skill.

<!-- section_id: "6c72b8ab-1735-435d-b5ae-7bacafe41093" -->
## Dependencies

- Python or Bash (Bloom filter generator)
- SHA256 (Merkle hash calculator)
- CRDT library (for multi-device sync — Phase 4)

<!-- section_id: "cf7de393-afcf-4d91-b274-d8314cfb5f73" -->
## Status

**Scaffolded** — directory exists, no scripts or data yet. Implementation in stage 06 (development).

<!-- section_id: "c7b570e8-f5c0-464f-8f7d-f45baac6acce" -->
## Design Reference

- `stage_2_05_design/outputs/by_topic/02_data_avenue_web_expansion.md`
- SHIMI paper: arXiv:2504.06135
