---
resource_id: "50e10df8-5daa-4a4d-883e-4fe474502b30"
resource_type: "output"
resource_name: "current_product"
---
# Pointer Sync System — Current Product

> **Canonical location**: Root `.0agnostic/pointer-sync.sh`

The current working product is the `pointer-sync.sh` script at the root `.0agnostic/` level. It is production-ready and integrated into the agnostic-sync workflow.

<!-- section_id: "2187b9e6-ab3e-4583-878f-983b66b5d8ee" -->
## What's Shipped

| Component | Status | Location |
|-----------|--------|----------|
| `pointer-sync.sh` | Production | `.0agnostic/pointer-sync.sh` (~1150 lines) |
| `entity-find.sh` | Production | `.0agnostic/entity-find.sh` (~55 lines) |
| Entity lookup TSV | Production | `.entity-lookup.tsv` (353 entities, generated) |
| `create-resource-indexes.sh` | Production | `.0agnostic/create-resource-indexes.sh` (~345 lines) |
| Root UUID index | Production | `.uuid-index.json` (5,313 entries) |
| Per-entity resource indexes | Production | `<entity>/.0agnostic/resource_index.json` (50 entities) |
| Pointer sync protocol | Production | `.0agnostic/03_protocols/pointer_sync_protocol.md` |
| Pointer sync knowledge | Production | `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md` |
| Pointer sync rule | Production | `.0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md` |
| Pointer edit guard hook | Production | `.0agnostic/06_.../08_hooks/scripts/pointer-edit-guard.sh` |
| agnostic-sync integration | Production | `.0agnostic/agnostic-sync.sh` (validation section) |

<!-- section_id: "f51874ea-40be-4ce2-a8ec-9bde37e0778d" -->
## Usage

```bash
# Fast entity lookup (~5ms, no Python)
.0agnostic/entity-find.sh memory          # Find entities by name
.0agnostic/entity-find.sh --path chain    # Just show paths
.0agnostic/entity-find.sh --uuid memory   # Just show UUIDs

# Sync all pointers (fix stale paths)
.0agnostic/pointer-sync.sh

# Validate only (check without modifying)
.0agnostic/pointer-sync.sh --validate

# Verbose output
.0agnostic/pointer-sync.sh --verbose

# Dry run (show what would change)
.0agnostic/pointer-sync.sh --dry-run

# Rebuild UUID index from source files
.0agnostic/pointer-sync.sh --rebuild-index

# Look up a UUID or entity name
.0agnostic/pointer-sync.sh --lookup <uuid-or-name>

# Navigate parent chain
.0agnostic/pointer-sync.sh --parent <uuid>
.0agnostic/pointer-sync.sh --parent <uuid> --verbose  # full chain to root

# List children of an entity
.0agnostic/pointer-sync.sh --children <uuid>

# Query with flexible filters
.0agnostic/pointer-sync.sh --query type=entity name=*research*
.0agnostic/pointer-sync.sh --query type=resource resource_type=script
.0agnostic/pointer-sync.sh --query has_children=true
.0agnostic/pointer-sync.sh --query parent_id=<uuid>

# Find references to a UUID
.0agnostic/pointer-sync.sh --find-references <uuid>

# Generate resource indexes for all entities
.0agnostic/create-resource-indexes.sh
.0agnostic/create-resource-indexes.sh --entity <path>
.0agnostic/create-resource-indexes.sh --dry-run
```

<!-- section_id: "c3d5e7f9-a0b2-4c1d-8e3f-6a7b9c0d2e4f" -->
## Index Statistics (2026-03-06)

| Metric | Count |
|--------|-------|
| Total UUID entries | 5,313 |
| Entity entries | 351 |
| Stage entries | 396 |
| Resource entries | 4,566 |
| Entities with parent links | 122 |
| Entities with children | 34 |
| Entities with resource indexes | 50 |
| Index file size | ~2.6 MB |
| Index load time | ~3ms |
| Single lookup time | <0.03ms |
