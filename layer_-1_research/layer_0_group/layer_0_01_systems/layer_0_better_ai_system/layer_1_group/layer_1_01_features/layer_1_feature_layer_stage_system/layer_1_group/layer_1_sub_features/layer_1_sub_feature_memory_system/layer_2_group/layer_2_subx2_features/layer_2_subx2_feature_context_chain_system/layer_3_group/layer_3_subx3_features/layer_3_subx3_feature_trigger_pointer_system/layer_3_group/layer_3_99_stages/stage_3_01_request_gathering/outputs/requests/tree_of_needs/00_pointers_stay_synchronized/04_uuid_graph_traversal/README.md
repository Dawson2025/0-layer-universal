---
resource_id: "d4a1b7c3-8e2f-4d5a-9b6c-1e3f5a7d9c2b"
resource_type: "output"
resource_name: "uuid_graph_traversal_needs"
---
# Branch 04: UUID Graph Traversal & Query

**The UUID system must support navigating the entity hierarchy as a graph and querying across all indexed entries.**

---

<!-- section_id: "e7f2a8b4-5c1d-4e3f-9a6b-2d4f6c8e0a1b" -->
## Definition

> Agents can traverse the entity hierarchy via parent/children relationships embedded in the UUID index, query for entries using flexible filters, and access per-entity resource indexes for O(1) file lookup. The system functions as a filesystem-backed document database.

---

<!-- section_id: "a3b5c7d9-1e2f-4a6b-8c0d-3e5f7a9b1c2d" -->
## The Problem

After entity UUIDs, stage UUIDs, and resource UUIDs were assigned (Phases 1-2), the UUID index was a flat lookup table. Agents could find an entity by UUID but could not:
- Navigate from a child to its parent or from a parent to its children
- Query across entries (e.g., "find all entities of type stage with name containing 'research'")
- Access per-entity resource catalogs without scanning all files
- Use the system as a database for understanding hierarchy structure

---

<!-- section_id: "b4c6d8e0-2f3a-4b7c-9d1e-4f6a8c0b2d3e" -->
## Three Needs

### Need 01: Parent/Children Entity Graph

**Status**: IMPLEMENTED (2026-03-06)

The `.uuid-index.json` must include `parent_id` and `children[]` fields for every entity entry, computed from `**Parent**: \`../path/0AGNOSTIC.md\`` references in each entity's 0AGNOSTIC.md.

**Requirements**:
- [x] Each entity entry in the index includes `parent_id` (UUID of parent entity, or `null` for roots)
- [x] Each entity entry includes `children` array (list of child entity UUIDs)
- [x] Parent resolution works by reading the `**Parent**:` reference, resolving the relative path, and extracting the parent's `entity_id`
- [x] Children are computed by inverting the parent map (no redundant storage in source files)
- [x] `--parent <uuid>` CLI command shows the parent entity
- [x] `--parent <uuid> --verbose` walks the full parent chain to root
- [x] `--children <uuid>` CLI command lists all direct children with UUIDs and paths

**Acceptance Criteria**:
- 122 entities have resolved parent links
- 34 entities have children
- Parent chain traversal reaches root in all cases where parents have entity_ids

---

### Need 02: Query CLI

**Status**: IMPLEMENTED (2026-03-06)

The `pointer-sync.sh` must support a `--query` command that enables flexible filtering across all UUID index entries using key=value pairs with glob pattern support.

**Requirements**:
- [x] `--query type=entity` filters by entry type (entity, stage, resource)
- [x] `--query name=*pattern*` filters by name with glob/fnmatch matching
- [x] `--query resource_type=script` filters resources by type
- [x] `--query parent_id=<uuid>` finds all entries with a specific parent
- [x] `--query has_children=true` finds entities that have children
- [x] `--query path=*pattern*` filters by path pattern
- [x] Multiple filters combine with AND logic
- [x] Results show UUID, type, name, and path for each match

**Acceptance Criteria**:
- Queries execute in <100ms on the full 5,313-entry index
- All filter combinations work correctly
- Output is human-readable and parseable

---

### Need 03: Per-Entity Resource Indexes

**Status**: IMPLEMENTED (2026-03-06)

Every entity with a `.0agnostic/` directory must have a `resource_index.json` that catalogs all UUID-bearing files within that entity, enabling O(1) resource lookup.

**Requirements**:
- [x] `create-resource-indexes.sh` generates `resource_index.json` for all entities
- [x] Each resource entry includes `resource_id`, `resource_type`, `resource_name`, `path`
- [x] Paths are relative to the entity root
- [x] Derived files (CLAUDE.md, .integration.md, etc.) are excluded
- [x] Resource types are inferred from path patterns and explicit `resource_type:` fields
- [x] Script supports `--entity <path>`, `--dry-run`, `--verbose` flags
- [x] Entities without `entity_id` are skipped gracefully

**Acceptance Criteria**:
- 50 entities have resource indexes
- 4,566 resource entries aggregated into root `.uuid-index.json`
- Total index: 5,313 entries (351 entity + 396 stage + 4,566 resource)

---

<!-- section_id: "c5d7e9f1-3a4b-5c6d-0e1f-5a7b9c1d3e4f" -->
## Remaining Gaps

| Gap | Priority | Description |
|-----|----------|-------------|
| Incremental index updates | Medium | Rebuild only changed entities instead of full rescan |
| Short-name resolution | Medium | Fuzzy/partial matching for entity names (e.g., `context_chain` matches `layer_2_subx2_feature_context_chain_system`) |
| Entity creation skill integration | Medium | Auto-generate UUIDs and resource indexes when creating new entities |
| Write-through operations | Low | Modify files via UUID reference (update frontmatter, rename, etc.) |
| 229 root entities without parents | Low | 154 have parents without entity_id, 61 have broken relative paths |
