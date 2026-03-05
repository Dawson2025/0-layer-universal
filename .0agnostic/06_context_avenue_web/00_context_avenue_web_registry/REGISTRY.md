---
resource_id: "4226db59-a43a-426d-8f0c-a7df7acabd96"
resource_type: "document"
resource_name: "REGISTRY"
---
# Context Avenue Web Registry

<!-- section_id: "8293a83e-eee0-4700-9363-ced4bd283ab0" -->
## Overview

The context avenue web delivers content to AI agents through multiple complementary avenues. Avenues are ordered by **comprehensiveness** — how complete a picture each avenue provides.

The web is divided into two categories:
- **File-based avenues (01-08)**: Deterministic transforms, human-readable, zero-dependency, version-controlled
- **Data-based avenues (09-13)**: Derived indexes, queryable, regenerable from file-based content

<!-- section_id: "07fb7329-78d1-4d01-a0ec-f31a1b856562" -->
## Physical Structure

```
06_context_avenue_web/
├── 00_context_avenue_web_registry/   # This registry + sync-registry.json
├── 01_file_based/                        # Deterministic, zero-dependency
│   ├── 01_aalang/
│   ├── 02_aalang_markdown_integration/
│   ├── 03_auto_memory/
│   ├── 04_@import_references/
│   ├── 05_skills/
│   ├── 06_agents/
│   ├── 07_path_specific_rules/
│   └── 08_hooks/
└── 02_data_based/                        # Derived, queryable, optional
    ├── 09_knowledge_graph/
    ├── 10_relational_index/
    ├── 11_vector_embeddings/
    ├── 12_temporal_index/
    └── 13_shimi_structures/
```

<!-- section_id: "a9fd7c5a-4276-4988-b30e-ac2ab8106e4e" -->
## Avenue Inventory

| # | Name | Category | Content | Comprehensiveness | Sync Script | Status |
|---|------|----------|---------|-------------------|-------------|--------|
| 00 | Registry | — | Avenue metadata, sync mappings | — | — | Active |
| 01 | AALang | File-based | Full .gab.jsonld agent graphs | Most comprehensive | jsonld-to-md.sh (partial) | Active |
| 02 | AALang Markdown Integration | File-based | .integration.md summaries | High | jsonld-to-md.sh | Active |
| 03 | Auto Memory | File-based | Persistent memory files | Medium | episodic-sync.sh | Active |
| 04 | @import References | File-based | Curated reference collections | Medium | — (manual) | Active |
| 05 | Skills | File-based | SKILL.md procedural files | Medium | — (manual) | Active |
| 06 | Agents | File-based | .agent.jsonld stubs | Medium-Low | — (manual) | Active |
| 07 | Path-Specific Rules | File-based | Directory-scoped rules | Low | — (manual) | Active |
| 08 | Hooks | File-based | Event-triggered scripts | Lowest (file) | — (manual) | Active |
| 09 | Knowledge Graph | Data-based | Structural model with typed relationships | Most comprehensive | build-graph.sh | Scaffolded |
| 10 | Relational Index | Data-based | Tabular metadata across entities | High | build-index.sh | Scaffolded |
| 11 | Vector Embeddings | Data-based | Semantic similarity fingerprints | Medium | build-embeddings.sh | Scaffolded |
| 12 | Temporal Index | Data-based | Time-series of events and changes | Low | build-temporal.sh | Scaffolded |
| 13 | SHIMI Structures | Data-based | Per-node optimization primitives | Lowest (data) | build-shimi.sh | Scaffolded |

<!-- section_id: "f49762df-6702-4dc0-bd12-fd357127d0e7" -->
## Key Properties

**Single direction of authority**: Source of truth (01-05) -> Avenues (06). Never the reverse.

**Graceful degradation**: If data-based avenues are down, file-based avenues still work. Zero-dependency operation is always preserved.

**Regenerability**: Every data-based avenue can be rebuilt from file-based content. Delete the database, rerun the sync, everything comes back.

**Comprehensiveness ordering**: Both file-based and data-based avenues follow the same principle — most comprehensive first (01/09), most fragmented last (08/13).

<!-- section_id: "d6c48a36-ff78-4d1f-90fb-6d4b491913ee" -->
## Sync Pipeline

See `sync-registry.json` for the machine-readable mapping.

```
sync-main.sh --all --recursive
    │
    ├── 1. agnostic-sync.sh (per entity)      ← foundational
    ├── 2. jsonld-to-md.sh (per .gab.jsonld)   ← depends on agent files
    ├── 3. episodic-sync.sh (global)           ← depends on episodic files
    └── 4. Data avenue scripts (parallel)      ← depends on all file content
        ├── build-graph.sh      (09)
        ├── build-index.sh      (10)
        ├── build-embeddings.sh (11)
        ├── build-temporal.sh   (12)
        └── build-shimi.sh      (13)
```
