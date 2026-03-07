---
resource_id: "f3a4b5c6-d7e8-4f9a-0b1c-2d3e4f5a6b7c"
resource_type: "document"
resource_name: "uuid-identity-system"
---
# UUID Identity System

Every entity, stage, file, and directory in this repository has a stable UUID. These UUIDs survive renames, moves, and restructuring.

<!-- section_id: "e2f3a4b5-c6d7-4e8f-9a0b-1c2d3e4f5a6b" -->
## Fast Entity Lookup

To find any entity by name, use entity-find.sh (fastest option, ~5ms, no Python):

```bash
.0agnostic/entity-find.sh <pattern>     # Find entity by name
.0agnostic/entity-find.sh memory        # Example: find memory-related entities
.0agnostic/entity-find.sh --path chain  # Just show paths
.0agnostic/entity-find.sh --uuid memory # Just show UUIDs
```

Use this BEFORE grep/glob when looking for entities. It searches a pre-built index and is faster than scanning the codebase.

<!-- section_id: "a8b9c0d1-e2f3-4a5b-6c7d-8e9f0a1b2c3d" -->
## What Agents Should Know

- Every `0AGNOSTIC.md` has an `entity_id:` field — this is the entity's permanent identity
- Every file header has `resource_id:` — this is the file's permanent identity
- `.entity-lookup.tsv` at repo root lists all entities (name/uuid/path) for instant grep
- `.uuid-index.json` at repo root indexes 5,313 entries (entities, stages, resources)
- Per-entity `resource_index.json` files catalog resources within each entity's `.0agnostic/`

<!-- section_id: "b9c0d1e2-f3a4-4b5c-6d7e-8f9a0b1c2d3e" -->
## When to Use Which Tool

- **Finding where an entity lives** → `.0agnostic/entity-find.sh <name>` (fast, simple)
- **Navigating hierarchy** (parent, children, chain to root) → `pointer-sync.sh --parent/--children`
- **Pre-rename check** → `pointer-sync.sh --find-references <uuid>`
- **Resource discovery** → `pointer-sync.sh --query type=resource entity_id=<uuid>`
- **Pointer validation** → `pointer-sync.sh --validate`

<!-- section_id: "c0d1e2f3-a4b5-4c6d-7e8f-9a0b1c2d3e4f" -->
## Quick Reference

| Task | Command |
|------|---------|
| Find entity by name (fast) | `.0agnostic/entity-find.sh <pattern>` |
| Find entity path only | `.0agnostic/entity-find.sh --path <pattern>` |
| Look up any UUID | `pointer-sync.sh --lookup <uuid>` |
| Get parent entity | `pointer-sync.sh --parent <uuid>` |
| List children | `pointer-sync.sh --children <uuid>` |
| Check references | `pointer-sync.sh --find-references <uuid>` |
| Find resources | `pointer-sync.sh --query type=resource entity_id=<uuid>` |
| Validate all pointers | `pointer-sync.sh --validate` |

All commands run from repo root. Scripts at `.0agnostic/`.

<!-- section_id: "d1e2f3a4-b5c6-4d7e-8f9a-0b1c2d3e4f5a" -->
## Full Reference

For complete command documentation, examples, and advanced queries: load the `/uuid-query` skill.

Key resources:
- Knowledge: `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md`
- Rule: `.0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md`
- Protocol: `.0agnostic/03_protocols/pointer_sync_protocol.md`
