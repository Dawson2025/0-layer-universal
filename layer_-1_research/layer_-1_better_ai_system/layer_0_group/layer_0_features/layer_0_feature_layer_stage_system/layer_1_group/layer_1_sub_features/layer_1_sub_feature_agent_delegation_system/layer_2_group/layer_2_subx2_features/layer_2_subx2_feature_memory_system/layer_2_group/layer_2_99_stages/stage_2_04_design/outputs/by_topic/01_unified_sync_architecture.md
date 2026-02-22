# Unified Sync Architecture

## Overview

The layer-stage system uses a **source of truth → delivery** pattern. Content lives in `.0agnostic/` directories (01-05). Delivery happens through the context avenue web (06). This document defines the sync architecture that connects them.

## Core Principle

```
0AGNOSTIC.md (hub / entry point)
       │
       ▼
.0agnostic/ (source of truth)
├── 01_knowledge/          ─┐
├── 02_rules/              │  CONTENT
├── 03_protocols/          │  (what agents know)
├── 04_episodic_memory/    │
├── 05_handoff_documents/  ─┘
│
├── 06_context_avenue_web/ ─── DELIVERY (how agents receive it)
│   ├── 00_registry/           management hub
│   ├── 01_file_based/ (01-08)    deterministic transforms
│   └── 02_data_based/ (09-13)    derived indexes
│
└── 07+_setup_dependant/   ─── ENVIRONMENT (OS/tool-specific)
```

The numbering encodes the flow: lower numbers are more fundamental. 01-05 produce content. 06 delivers it. 07+ configures the environment.

## 0AGNOSTIC.md as Hub

Every entity has a `0AGNOSTIC.md` at its root. This file is:

1. **The starting point** — the first file any AI agent reads when entering an entity
2. **The identity document** — WHO this entity is, WHAT it does, WHERE things stand
3. **The pointer hub** — references into .0agnostic/ for detailed content
4. **The sync source** — agnostic-sync.sh transforms it into tool-specific files

```
                          0AGNOSTIC.md
                         /      |      \
                        /       |       \
              STATIC content  DYNAMIC content  Pointers to .0agnostic/
             (always loaded)  (on-demand)      (read when needed)
                    |
                    ▼
            agnostic-sync.sh
           /    |    |    |    \      \
      CLAUDE AGENTS GEMINI OPENAI .cursorrules copilot-instructions
        .md    .md    .md    .md
```

## Existing Sync Scripts

### 1. agnostic-sync.sh

| Property | Value |
|----------|-------|
| **Location** | `.0agnostic/agnostic-sync.sh` |
| **From** | `0AGNOSTIC.md` (STATIC content) + `.1merge/` overrides |
| **To** | CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, .github/copilot-instructions.md |
| **Scope** | Single entity (pass directory as argument) |
| **When** | After editing 0AGNOSTIC.md |
| **Avenues served** | Indirect — generates tool entry points that reference avenue content |

### 2. episodic-sync.sh

| Property | Value |
|----------|-------|
| **Location** | `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh` |
| **From** | All `.0agnostic/04_episodic_memory/index.md` files across the hierarchy |
| **To** | `~/.claude/projects/.../memory/episodic.md` (Claude Code auto-memory) |
| **Scope** | Global (scans entire repo) |
| **When** | After updating any episodic memory index.md |
| **Avenues served** | 03_auto_memory |

### 3. jsonld-to-md.sh

| Property | Value |
|----------|-------|
| **Location** | `.0agnostic/01_knowledge/layer_stage_system/resources/tools/jsonld-to-md.sh` |
| **From** | Any `.gab.jsonld` file |
| **To** | Matching `.integration.md` (same base name) |
| **Scope** | Single file |
| **When** | After editing a .gab.jsonld agent definition |
| **Avenues served** | 01_aalang, 02_aalang_markdown_integration |

## sync-main.sh — Orchestrator Specification

### Purpose

A single entry point that coordinates all sync operations. Like a `main.py` but for shell-based sync pipelines.

### Location

`.0agnostic/01_knowledge/layer_stage_system/resources/tools/sync-main.sh`

### CLI Interface

```bash
sync-main.sh [OPTIONS] [DIRECTORY]

Options:
  --all           Run all sync pipelines (default)
  --agnostic      Run only agnostic-sync (0AGNOSTIC→tool files)
  --episodic      Run only episodic-sync (episodic→auto-memory)
  --jsonld        Run only jsonld-to-md (all .gab.jsonld in scope)
  --avenues       Run only data-based avenue sync (09-13)
  --avenue N      Run specific avenue sync (e.g., --avenue 09)
  --recursive     Process all entities below DIRECTORY
  --dry-run       Show what would run without executing
  --verbose       Detailed output
  --help          Show usage

If no DIRECTORY specified, uses current directory.
If no OPTIONS specified, runs --all.
```

### Execution Order

Sync scripts have dependencies — they must run in this order:

```
1. agnostic-sync.sh     (updates tool files — foundational)
     ↓
2. jsonld-to-md.sh      (updates integration MDs — depends on agent definitions)
     ↓
3. episodic-sync.sh     (aggregates episodic memory — depends on index.md files)
     ↓
4. avenue-sync scripts   (data avenues — depend on all file content being current)
   ├── build-graph.sh    (09_knowledge_graph)
   ├── build-index.sh    (10_relational_index)
   ├── build-embeddings.sh (11_vector_embeddings)
   ├── build-temporal.sh (12_temporal_index)
   └── build-shimi.sh   (13_shimi_structures)
```

Data-based avenue scripts (step 4) are independent of each other and can run in parallel.

### Entity Discovery

When `--recursive` is used:
```bash
find "$DIRECTORY" -name "0AGNOSTIC.md" -type f | sort
```

Each discovered entity gets the selected sync pipelines run against it.

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All syncs succeeded |
| 1 | Some syncs failed (partial success) |
| 2 | Critical failure (no syncs completed) |

### Logging

Output to stdout by default. With `--verbose`, also writes to `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/sync.log`.

## Sync Registry

Machine-readable mapping at `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/sync-registry.json`.

See `sync-registry.json` for the full schema. Each entry maps a sync script to:
- `name`: Human-readable identifier
- `script`: Relative path to the script
- `scope`: `entity` (one dir), `file` (one file), `global` (entire repo)
- `inputs`: File patterns consumed
- `outputs`: File patterns produced
- `avenues`: Which avenues this sync serves
- `required`: Whether this sync is mandatory (file-based) or optional (data-based)
- `phase`: When this sync runs in the dependency chain

## Zero-Dependency Guarantee

The sync architecture is designed so that:

1. **File-based avenues (01-08) always work** — they require only bash, awk, jq (standard unix tools)
2. **Data-based avenues (09-13) are optional** — they require PostgreSQL, pgvector, etc. If unavailable, the system operates normally without them
3. **sync-main.sh gracefully skips** unavailable data-based syncs (checks for required tools before running)
4. **All data-based content is regenerable** — delete the database, rerun the sync, everything comes back from files

This means: the system works TODAY with zero infrastructure. Data-based avenues are future accelerators, not requirements.

## Sources

- Research docs 32-37 (layer-stage comparisons with commercial systems)
- Research doc 36 (technology integration roadmap)
- Existing sync scripts (agnostic-sync.sh, episodic-sync.sh, jsonld-to-md.sh)
