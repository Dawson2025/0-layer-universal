---
resource_id: "b4c5d6e7-f8a9-4b0c-1d2e-3f4a5b6c7d8e"
resource_type: "output"
resource_name: "entity_find_design"
---
# Entity Find — Lightweight Lookup Design

<!-- section_id: "c5d6e7f8-a9b0-4c1d-2e3f-4a5b6c7d8e9f" -->
## Problem

Agents tasked with "find entity X" default to Grep/Glob (~50ms, 13+ tool calls) rather than pointer-sync.sh (~500ms, loads Python + 2.6MB JSON). Neither is optimal. We need a tool fast enough that agents prefer it over grep.

<!-- section_id: "d6e7f8a9-b0c1-4d2e-3f4a-5b6c7d8e9f0a" -->
## Solution

Two components:

### .entity-lookup.tsv (Data)

Flat tab-separated file at repo root. One entity per line. ~350 lines, ~15KB.

**Format**: `name\tuuid\tpath\tparent_uuid`

Generated as a side-effect of `pointer-sync.sh --rebuild-index`. Listed in `.gitignore` as a build artifact (same as `.dir-uuid-index.json`).

### entity-find.sh (Script)

Lightweight bash script at `.0agnostic/entity-find.sh`. Pure bash + grep. No Python dependency. ~55 lines.

**Modes**:
- `entity-find.sh <pattern>` — full output (name/uuid/path/parent)
- `entity-find.sh --path <pattern>` — paths only
- `entity-find.sh --uuid <pattern>` — UUIDs only
- Auto-rebuilds TSV if missing (calls pointer-sync.sh)

<!-- section_id: "e7f8a9b0-c1d2-4e3f-4a5b-6c7d8e9f0a1b" -->
## Performance Comparison

| Tool | Time | Dependencies | Use Case |
|------|------|-------------|----------|
| `entity-find.sh` | ~5ms | bash + grep | Find entity by name |
| Grep on codebase | ~50ms | grep + multiple calls | Ad-hoc text search |
| `pointer-sync.sh` | ~500ms | Python + 2.6MB JSON | Hierarchy, references, validation |

<!-- section_id: "f8a9b0c1-d2e3-4f4a-5b6c-7d8e9f0a1b2c" -->
## Propagation Path

1. **Source**: `stage_3_06_development/outputs/entity-find.sh` (this entity)
2. **Production copy**: Root `.0agnostic/entity-find.sh`
3. **Knowledge**: Root `.0agnostic/01_knowledge/pointer_sync/` (updated)
4. **Rules**: Root `.0agnostic/02_rules/` (pointer_sync_rule covers this)
5. **Context avenues**: Root `.claude/rules/uuid-identity-system.md`
6. **AI systems**: `0AGNOSTIC.md` → `CLAUDE.md` (via agnostic-sync.sh)
