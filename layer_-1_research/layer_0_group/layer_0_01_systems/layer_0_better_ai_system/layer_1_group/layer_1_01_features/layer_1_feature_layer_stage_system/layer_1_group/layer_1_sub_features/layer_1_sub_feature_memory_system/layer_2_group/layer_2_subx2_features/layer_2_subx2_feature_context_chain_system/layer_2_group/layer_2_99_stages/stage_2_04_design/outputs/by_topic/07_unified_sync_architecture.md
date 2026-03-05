---
resource_id: "5cc603bf-2a08-41aa-9b9e-6ca520890152"
resource_type: "output"
resource_name: "07_unified_sync_architecture"
---
# Unified Sync Architecture

**Date**: 2026-02-23
**Status**: Partially implemented (file-based syncs working; orchestrator and data-based syncs designed)
**Scope**: How all sync scripts coordinate to propagate changes from source of truth through the avenue web

---

<!-- section_id: "3a81b8e6-f631-4029-b382-30712ce61900" -->
## Overview

The layer-stage system uses multiple sync scripts that transform source content into delivery formats. This document defines the orchestration architecture that coordinates them.

---

<!-- section_id: "4c44043c-e11c-4500-9fc1-beca50e77a01" -->
## Existing Sync Scripts

<!-- section_id: "5025dfa2-080f-4031-9f66-9690e76183ee" -->
### 1. agnostic-sync.sh

| Property | Value |
|----------|-------|
| **Location** | `.0agnostic/agnostic-sync.sh` (at repo root, cascades to all entities) |
| **From** | `0AGNOSTIC.md` STATIC content + `.1merge/` overrides + hot rule frontmatter |
| **To** | CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, .github/copilot-instructions.md |
| **Scope** | Single entity (pass directory as argument) |
| **When** | After editing 0AGNOSTIC.md or .0agnostic/ rules with `promote: hot` |
| **Features** | Format detection (new/old/minimal), .1merge 3-tier merge, hot rule promotion, content validation warnings |

<!-- section_id: "adb81907-ca6c-451f-ab37-c45f9f56b220" -->
### 2. episodic-sync.sh

| Property | Value |
|----------|-------|
| **Location** | `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh` |
| **From** | All `.0agnostic/04_episodic_memory/index.md` files across the hierarchy |
| **To** | `~/.claude/projects/.../memory/episodic.md` (Claude Code auto-memory) |
| **Scope** | Global (scans entire repo) |
| **When** | After updating any episodic memory index.md |
| **Avenues served** | 03_auto_memory |

<!-- section_id: "14adad55-cea6-4d6e-843c-f3cfb500ddb7" -->
### 3. jsonld-to-md.sh

| Property | Value |
|----------|-------|
| **Location** | `.0agnostic/01_knowledge/layer_stage_system/resources/tools/jsonld-to-md.sh` |
| **From** | Any `.gab.jsonld` file |
| **To** | Matching `.integration.md` (same base name) |
| **Scope** | Single file |
| **When** | After editing a .gab.jsonld agent definition |
| **Avenues served** | 01_aalang, 02_aalang_markdown_integration |

<!-- section_id: "4b8b769f-bb17-4719-9b70-e2f0aa367a40" -->
### 4. sync-handoffs.sh

| Property | Value |
|----------|-------|
| **Location** | `.0agnostic/01_knowledge/layer_stage_system/resources/tools/sync-handoffs.sh` |
| **From** | Stage reports, layer reports, manager instructions |
| **To** | Handoff document directories (from_above/, from_sides/, from_below/) |
| **Scope** | Single entity and its stages |
| **When** | After updating any stage or layer report |
| **Avenues served** | Indirect — populates handoff document structure |

<!-- section_id: "85d0a12f-1f70-4757-a58e-4c71e54adc87" -->
### 5. user-level-sync.sh

| Property | Value |
|----------|-------|
| **Location** | `.0agnostic/01_knowledge/layer_stage_system/resources/tools/user-level-sync.sh` |
| **From** | Root `.0agnostic/` (universal rules, protocols, knowledge) |
| **To** | `~/.0agnostic/` (user-level context beyond the repo) |
| **Scope** | Global (repo root → user home) |
| **When** | After updating universal artifacts |
| **Avenues served** | Extends chain beyond repo boundary |

---

<!-- section_id: "3940820d-d584-4703-821b-d7d18650e36e" -->
## sync-main.sh — Orchestrator Specification

<!-- section_id: "99686eda-66e1-4b49-baf1-f1f25a52b96f" -->
### Purpose

A single entry point that coordinates all sync operations. Ensures correct execution order, handles dependencies, and provides unified reporting.

<!-- section_id: "994d3a92-8407-4392-8a9b-fc7dc627cf30" -->
### Location

`.0agnostic/01_knowledge/layer_stage_system/resources/tools/sync-main.sh`

<!-- section_id: "d4f7177c-2aa9-483a-b76a-db535e3d0a90" -->
### CLI Interface

```bash
sync-main.sh [OPTIONS] [DIRECTORY]

Options:
  --all           Run all sync pipelines (default)
  --agnostic      Run only agnostic-sync (0AGNOSTIC→tool files)
  --episodic      Run only episodic-sync (episodic→auto-memory)
  --jsonld        Run only jsonld-to-md (all .gab.jsonld in scope)
  --handoffs      Run only sync-handoffs (distribute reports)
  --avenues       Run only data-based avenue sync (09-13)
  --avenue N      Run specific avenue sync (e.g., --avenue 09)
  --recursive     Process all entities below DIRECTORY
  --dry-run       Show what would run without executing
  --verbose       Detailed output
  --help          Show usage

If no DIRECTORY specified, uses current directory.
If no OPTIONS specified, runs --all.
```

<!-- section_id: "bdd231fe-e085-43a0-9ad4-b2d66a5e3628" -->
### Execution Order

Sync scripts have dependencies — they must run in this order:

```
Phase 1: Foundation (sequential)
├── 1. agnostic-sync.sh         Updates tool files from 0AGNOSTIC.md
│        ↓
├── 2. jsonld-to-md.sh          Updates integration MDs from agent definitions
│        ↓
└── 3. sync-handoffs.sh         Distributes reports through hierarchy

Phase 2: Aggregation (sequential)
└── 4. episodic-sync.sh         Aggregates episodic memory to auto-memory

Phase 3: Data avenues (parallel — independent of each other)
├── 5a. build-graph.sh          09_knowledge_graph
├── 5b. build-index.sh          10_relational_index
├── 5c. build-embeddings.sh     11_vector_embeddings
├── 5d. build-temporal.sh       12_temporal_index
└── 5e. build-shimi.sh          13_shimi_structures

Phase 4: Extension (sequential)
└── 6. user-level-sync.sh       Extends to ~/.0agnostic/
```

Phase 1 scripts depend on each other (tool files must exist before integration MDs reference them). Phase 3 scripts are independent and can run in parallel. Phase 4 runs last because it copies finalized content to user level.

<!-- section_id: "dcbb7e0d-c6a3-46a4-8c06-d0550acb2484" -->
### Entity Discovery

When `--recursive` is used:
```bash
find "$DIRECTORY" -name "0AGNOSTIC.md" -type f | sort
```

Each discovered entity gets the selected sync pipelines run against it.

<!-- section_id: "e5cf02f4-77d9-4509-b1d8-7a2cbe369bc4" -->
### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All syncs succeeded |
| 1 | Some syncs failed (partial success) |
| 2 | Critical failure (no syncs completed) |

<!-- section_id: "06a4e2ac-787b-4b72-a524-39bfe37ce5e3" -->
### Logging

Output to stdout by default. With `--verbose`, also writes to `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/sync.log`.

---

<!-- section_id: "455e9267-e884-41cb-ad49-73574d3b67bd" -->
## Sync Registry

Machine-readable mapping at `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/sync-registry.json`.

Each entry maps a sync script to:
- `name`: Human-readable identifier
- `script`: Relative path to the script
- `scope`: `entity` (one dir), `file` (one file), `global` (entire repo)
- `inputs`: File patterns consumed
- `outputs`: File patterns produced
- `avenues`: Which avenues this sync serves
- `required`: Whether this sync is mandatory (file-based) or optional (data-based)
- `phase`: When this sync runs in the dependency chain

---

<!-- section_id: "28223727-7cac-4c8b-ab45-bd2de1ee5b60" -->
## Zero-Dependency Guarantee

The sync architecture is designed so that:

1. **File-based syncs (1-4) always work** — they require only bash, awk, sed, jq (standard unix tools)
2. **Data-based syncs (5a-5e) are optional** — they require PostgreSQL, pgvector, etc. If unavailable, the system operates normally without them
3. **sync-main.sh gracefully skips** unavailable data-based syncs (checks for required tools before running)
4. **All data-based content is regenerable** — delete the database, rerun the sync, everything comes back from files

The system works TODAY with zero infrastructure. Data-based avenues are future accelerators, not requirements.

---

<!-- section_id: "7ad4d53c-b00f-4e7f-9e82-090d74c6b690" -->
## Implementation Status

| Script | Status | Notes |
|--------|--------|-------|
| agnostic-sync.sh | Implemented | v2 with format detection, .1merge, hot promotion, validation |
| jsonld-to-md.sh | Implemented | Generates .integration.md from .gab.jsonld |
| episodic-sync.sh | Implemented | Aggregates to Claude auto-memory |
| sync-handoffs.sh | Implemented | Distributes stage/layer reports |
| user-level-sync.sh | Implemented | Extends chain to ~/.0agnostic/ |
| sync-main.sh | **Not yet implemented** | Orchestrator spec defined, not built |
| build-graph.sh | **Not yet implemented** | Knowledge graph (avenue 09) |
| build-index.sh | **Not yet implemented** | Relational index (avenue 10) |
| build-embeddings.sh | **Not yet implemented** | Vector embeddings (avenue 11) |
| build-temporal.sh | **Not yet implemented** | Temporal index (avenue 12) |
| build-shimi.sh | **Not yet implemented** | SHIMI structures (avenue 13) |

---

<!-- section_id: "207beebc-a326-4d39-8e3d-b9c835c5c9d2" -->
## Related Documents

- **Source-to-avenue flow**: `06_source_of_truth_to_avenue_flow.md` (ordering and numbering)
- **Propagation chain**: `03_propagation_chain_architecture.md` (4-layer chain)
- **Discovery temperatures**: `08_discovery_temperature_model.md` (Hot/Warm/Cold)
- **Integration design**: `02_0agnostic_1merge_avenue_web_integration_design.md` (.1merge 3-tier)
