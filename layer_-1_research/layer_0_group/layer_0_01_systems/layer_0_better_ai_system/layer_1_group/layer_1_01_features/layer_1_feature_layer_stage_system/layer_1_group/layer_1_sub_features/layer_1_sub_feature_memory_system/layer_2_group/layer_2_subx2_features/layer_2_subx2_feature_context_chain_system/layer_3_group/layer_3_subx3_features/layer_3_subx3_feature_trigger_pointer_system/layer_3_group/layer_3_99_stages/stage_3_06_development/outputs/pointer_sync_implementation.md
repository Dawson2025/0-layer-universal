---
resource_id: "24b87bb5-c981-40b3-94dc-c0b052db0997"
resource_type: "output"
resource_name: "pointer_sync_implementation"
---
# Pointer Sync System — Implementation

> **Canonical location**: Root `.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh`

The implementation artifacts live at the root `.0agnostic/` level. This pointer connects stage_3_06_development to the canonical script and hook.

<!-- section_id: "5001571b-8242-46c8-9417-fb7f0d150133" -->
## Production Artifacts

| Artifact | Canonical Location | Status |
|----------|-------------------|--------|
| Main script | `.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh` | Production (~1050 lines) |
| Resource index script | `.0agnostic/03_protocols/pointer_sync_protocol/tools/create-resource-indexes.sh` | Production (~345 lines) |
| Claude Code hook | `.0agnostic/06_context_avenue_web/01_file_based/08_hooks/scripts/pointer-edit-guard.sh` | Production |
| Hook registration | `.claude/settings.json` (PostToolUse entry) | Production |
| agnostic-sync integration | `.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh` (pointer validation section) | Production |
| Root UUID index | `.uuid-index.json` | Production (5,313 entries, ~2.6MB) |
| Resource indexes | `<entity>/.0agnostic/resource_index.json` (50 entities) | Production |

<!-- section_id: "a2b4c6d8-e0f1-4a3b-5c7d-9e1f3a5b7c8d" -->
## Capabilities Added (2026-03-06)

### pointer-sync.sh Enhancements

| Feature | CLI Command | Description |
|---------|-------------|-------------|
| Parent lookup | `--parent <uuid>` | Shows parent entity of a given entity |
| Parent chain | `--parent <uuid> --verbose` | Walks full parent chain to root |
| Children listing | `--children <uuid>` | Lists all direct children of an entity |
| Query engine | `--query key=value [...]` | Flexible filtering with glob patterns |
| Entity lookup | `--lookup <uuid-or-name>` | Now shows parent_id and children info |

### Query Filter Keys

| Key | Example | Description |
|-----|---------|-------------|
| `type` | `type=entity` | Filter by entry type |
| `name` | `name=*research*` | Glob match on name |
| `path` | `path=*layer_1*` | Glob match on path |
| `resource_type` | `resource_type=script` | Filter resources by type |
| `parent_id` | `parent_id=<uuid>` | Find children of specific parent |
| `has_children` | `has_children=true` | Find entities with/without children |

### Implementation Details

- `build_uuid_index()` rewritten from bash string-building to embedded Python for reliability
- Three-phase index rebuild: entities (with parent resolution) → stages → resources
- Parent resolution parses `**Parent**: \`path\`` from 0AGNOSTIC.md, resolves relative path, reads parent entity_id
- Children computed by inverting the parent map (no redundant data in source files)
- Query engine uses `fnmatch.fnmatch()` for glob pattern matching
- All warnings go to stderr, clean JSON to stdout (fixes previous output corruption)

### create-resource-indexes.sh Enhancements

- Gracefully skips entities without `entity_id` (instead of erroring)
- Bulk rollout: 50 entities received resource indexes in one run
- 4,566 resource entries aggregated into root index
