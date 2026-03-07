---
resource_id: "a3b4c5d6-e7f8-4a9b-0c1d-2e3f4a5b6c7d"
resource_type: "output"
resource_name: "entity_find_implementation"
---
# Entity Find — Implementation

> **Production script**: Root `.0agnostic/entity-find.sh`
> **Data file**: Root `.entity-lookup.tsv` (generated, in .gitignore)

<!-- section_id: "b4c5d6e7-f8a9-4b0c-1d2e-3f4a5b6c7d8f" -->
## Production Artifacts

| Artifact | Canonical Location | Status |
|----------|-------------------|--------|
| `entity-find.sh` | `.0agnostic/entity-find.sh` (~55 lines) | Production |
| `.entity-lookup.tsv` | `.entity-lookup.tsv` (353 entities) | Production (generated) |
| TSV generation | `.0agnostic/pointer-sync.sh` `do_rebuild_index()` | Production (integrated) |

<!-- section_id: "c5d6e7f8-a9b0-4c1d-2e3f-4a5b6c7d8e90" -->
## How TSV Generation Works

TSV is generated inside `do_rebuild_index()` in pointer-sync.sh, right after the JSON index is written. A small Python snippet reads `.uuid-index.json`, filters for `type == "entity"`, and writes the TSV with `atomic_write()`.

**TSV format**: `name\tuuid\tpath\tparent_uuid` (header + one line per entity)

<!-- section_id: "d6e7f8a9-b0c1-4d2e-3f4a-5b6c7d8e9f01" -->
## How entity-find.sh Works

Pure bash + grep. No Python. Steps:
1. Locate `.entity-lookup.tsv` relative to script location
2. If TSV missing → auto-rebuild via `pointer-sync.sh --rebuild-index`
3. Skip header, grep case-insensitive on the full line
4. Parse matched TSV lines and output in selected mode

**Modes**: `--path` (paths only), `--uuid` (UUIDs only), default (full name/uuid/path/parent)

<!-- section_id: "e7f8a9b0-c1d2-4e3f-4a5b-6c7d8e9f0a12" -->
## Propagation Chain

```
stage_3_06_development (this doc)
  ↓ copy
root .0agnostic/entity-find.sh (production script)
  ↓ referenced in
root .0agnostic/01_knowledge/pointer_sync/ (knowledge)
root .claude/rules/uuid-identity-system.md (rule)
  ↓ referenced in
root 0AGNOSTIC.md (UUID section + triggers + resources)
  ↓ agnostic-sync.sh
root CLAUDE.md (auto-generated, agents read this)
```
