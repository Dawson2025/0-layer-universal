---
resource_id: "f8a2b4c6-d0e1-4f3a-5b7c-9d1e3f5a7b8c"
resource_type: "output"
resource_name: "uuid_graph_and_query_design"
---
# Design: UUID Graph Traversal & Query CLI

<!-- section_id: "a1b3c5d7-e9f0-4a2b-6c8d-0e2f4a6b8c9d" -->
## Status: IMPLEMENTED
<!-- section_id: "b2c4d6e8-f0a1-4b3c-7d9e-1f3a5b7c9d0e" -->
## Date: 2026-03-06
<!-- section_id: "c3d5e7f9-a0b1-4c2d-8e0f-2a4b6c8d0e1f" -->
## Author: AI Agent (stage_3_04_design)
<!-- section_id: "d4e6f8a0-b1c2-4d3e-9f0a-3b5c7d9e1f2a" -->
## Related Design: `uuid_identity_system_design.md` (Sections 4, 12)

---

<!-- section_id: "e5f7a9b1-c2d3-4e4f-0a1b-4c6d8e0f2a3b" -->
## 1. Problem Statement

The UUID identity system (design doc Sections 1-14) established UUIDs for entities, stages, and resources with a flat index for lookup. However, agents need to:

1. **Navigate hierarchy**: Given an entity, find its parent and children without reading 0AGNOSTIC.md files
2. **Query flexibly**: Filter the index by type, name pattern, resource type, parent, path — like a database SELECT
3. **Access resource catalogs**: Find all resources within an entity without scanning the filesystem

These capabilities transform the UUID index from a simple key-value store into a filesystem-backed document database (design doc Section 12).

---

<!-- section_id: "f6a8b0c2-d3e4-4f5a-1b2c-5d7e9f1a3b4c" -->
## 2. Parent/Children Graph Design

<!-- section_id: "a7b9c1d3-e4f5-4a6b-2c3d-6e8f0a2b4c5d" -->
### 2.1 Data Source

Parent references are extracted from `**Parent**: \`../path/0AGNOSTIC.md\`` lines in each entity's 0AGNOSTIC.md Identity section. This is already the canonical parent declaration — no new data source needed.

<!-- section_id: "b8c0d2e4-f5a6-4b7c-3d4e-7f9a1b3c5d6e" -->
### 2.2 Resolution Algorithm

```
For each entity with 0AGNOSTIC.md:
  1. Read first 8KB of file
  2. Search for pattern: **Parent**: `<relative_path>`
  3. Resolve relative path from entity directory to get absolute parent path
  4. Read parent's 0AGNOSTIC.md, extract entity_id
  5. Store: entity.parent_id = parent.entity_id
  6. After all entities processed, invert to compute children[]:
     For each entity with parent_id:
       parent.children.append(entity.entity_id)
```

<!-- section_id: "c9d1e3f5-a6b7-4c8d-4e5f-8a0b2c4d6e7f" -->
### 2.3 Index Schema Extension

Entity entries in `.uuid-index.json` gain two new fields:

```json
{
  "a79b61a7-...": {
    "type": "entity",
    "name": "layer_2_subx2_feature_context_chain_system",
    "path": "layer_-1_research/.../layer_2_subx2_feature_context_chain_system",
    "parent_id": "f62dcffc-...",
    "children": ["5d5be68b-...", "7a74444f-...", "ae555d77-..."]
  }
}
```

- `parent_id`: UUID of the parent entity, or absent/null for root entities
- `children`: Array of child entity UUIDs (computed, not stored in source files)

<!-- section_id: "d0e2f4a6-b7c8-4d9e-5f6a-9b1c3d5e7f8a" -->
### 2.4 Edge Cases

| Scenario | Handling |
|----------|----------|
| Entity has no `**Parent**:` reference | No `parent_id` field (true root) |
| Parent path doesn't resolve to existing file | Warning to stderr, no `parent_id` (61 cases) |
| Parent file exists but has no `entity_id` | Warning, no `parent_id` (154 cases) |
| Circular parent references | Would create cycles — detected by --parent --verbose chain walk |
| Multiple `**Parent**:` lines | First match used |

<!-- section_id: "e1f3a5b7-c8d9-4e0f-6a7b-0c2d4e6f8a9b" -->
### 2.5 Statistics (Current)

| Metric | Count |
|--------|-------|
| Total entities | 351 |
| Entities with resolved parent_id | 122 |
| Entities with children | 34 |
| Root entities (no parent) | 229 |
| Roots with fixable parent refs | 215 (parent exists but lacks entity_id or path is wrong) |
| True roots | 14 (layer_-1_research, layer_0, layer_1, etc.) |

---

<!-- section_id: "f2a4b6c8-d9e0-4f1a-7b8c-1d3e5f7a9b0c" -->
## 3. Query CLI Design

<!-- section_id: "a3b5c7d9-e0f1-4a2b-8c9d-2e4f6a8b0c1d" -->
### 3.1 Interface

```bash
pointer-sync.sh --query [key=value ...]
```

Multiple key=value pairs are AND-combined. Values support fnmatch glob patterns.

<!-- section_id: "b4c6d8e0-f1a2-4b3c-9d0e-3f5a7b9c1d2e" -->
### 3.2 Supported Filter Keys

| Key | Applies To | Example | Description |
|-----|-----------|---------|-------------|
| `type` | All entries | `type=entity` | Filter by entry type (entity, stage, resource) |
| `name` | All entries | `name=*research*` | Glob match on entry name |
| `path` | All entries | `path=*layer_1*` | Glob match on entry path |
| `resource_type` | Resources | `resource_type=script` | Filter resources by type |
| `entity_id` | Stages, Resources | `entity_id=a79b...` | Find entries belonging to an entity |
| `parent_id` | Entities | `parent_id=f62d...` | Find children of a specific parent |
| `has_children` | Entities | `has_children=true` | Find entities that have/lack children |

<!-- section_id: "c5d7e9f1-a2b3-4c4d-0e1f-4a6b8c0d2e3f" -->
### 3.3 Implementation

The query engine is implemented as an embedded Python script that:
1. Loads `.uuid-index.json` (O(1) file read, ~3ms for 2.6MB)
2. Parses key=value pairs from arguments
3. Iterates all entries, applying `fnmatch.fnmatch()` for glob patterns
4. Prints matching entries as formatted table

Performance: <100ms for full scan of 5,313 entries.

<!-- section_id: "d6e8f0a2-b3c4-4d5e-1f2a-5b7c9d1e3f4a" -->
### 3.4 Output Format

```
UUID                                  TYPE      NAME                    PATH
a79b61a7-c4ab-4c93-bed5-bbcc8af0f1a9  entity    layer_2_subx2...        layer_-1_research/...
5d5be68b-1234-4abc-9def-567890abcdef  entity    layer_3_subx3...        layer_-1_research/...
```

---

<!-- section_id: "e7f9a1b3-c4d5-4e6f-2a3b-6c8d0e2f4a5b" -->
## 4. Per-Entity Resource Indexes

<!-- section_id: "f8a0b2c4-d5e6-4f7a-3b4c-7d9e1f3a5b6c" -->
### 4.1 Purpose

Resource indexes enable agents to discover all UUID-bearing files within an entity without filesystem scanning. They sit at `.0agnostic/resource_index.json` and serve as the entity-local component of the three-tier index architecture (local → root).

<!-- section_id: "a9b1c3d5-e6f7-4a8b-4c5d-8e0f2a4b6c7d" -->
### 4.2 Schema

```json
{
  "file_id": "uuid-of-this-index-file",
  "generated": "2026-03-06T10:30:00Z",
  "entity_id": "parent-entity-uuid",
  "entity_name": "entity_directory_name",
  "entity_path": "relative/path/from/repo/root",
  "resources": [
    {
      "resource_id": "uuid-of-resource",
      "id_field": "resource_id|file_id",
      "resource_type": "knowledge|rule|protocol|script|data|output|...",
      "resource_name": "human_readable_name",
      "path": "relative/path/from/entity/root"
    }
  ]
}
```

<!-- section_id: "b0c2d4e6-f7a8-4b9c-5d6e-9f1a3b5c7d8e" -->
### 4.3 Generation

`create-resource-indexes.sh` generates indexes by:
1. Discovering entities (directories with both `0AGNOSTIC.md` and `.0agnostic/`)
2. Using `git ls-files` to find tracked files within each entity
3. Reading file headers (first 8KB) for UUID fields
4. Excluding derived files (CLAUDE.md, .integration.md, etc.)
5. Inferring resource types from paths and explicit fields
6. Writing atomic JSON output

<!-- section_id: "c1d3e5f7-a8b9-4c0d-6e7f-0a2b4c6d8e9f" -->
### 4.4 Aggregation into Root Index

The root `build_uuid_index()` function (Phase 3 of the rebuild process) reads all `resource_index.json` files and aggregates their entries into `.uuid-index.json`. Duplicate UUIDs (from overlapping git ls-files scopes) are deduplicated with first-seen-wins.

---

<!-- section_id: "d2e4f6a8-b9c0-4d1e-7f8a-1b3c5d7e9f0a" -->
## 5. Architectural Context

This design extends the UUID identity system design (Sections 4 and 12) by adding:

| Concept | Document DB Parallel | Implementation |
|---------|---------------------|----------------|
| Parent/children graph | Document references + denormalized children | `parent_id` + `children[]` in index |
| Query CLI | Collection query with filters | `--query` with fnmatch patterns |
| Resource indexes | Per-document embedded indexes | `.0agnostic/resource_index.json` |
| Three-phase rebuild | Index aggregation pipeline | entities → stages → resources |

The system now supports all four primary database operations:
- **Create**: `uuidgen` + insert into frontmatter/header
- **Read**: `--lookup`, `--parent`, `--children`, `--query`
- **Update**: Edit source files, `--rebuild-index` to refresh
- **Delete**: Remove files, `--gc` to clean index (via design doc Section 13)
