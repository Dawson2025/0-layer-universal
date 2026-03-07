---
resource_id: "2c3c89f6-6378-430a-aa2d-6c3278e00db7"
resource_type: "readme
output"
resource_name: "README"
---
# Root Need: Pointers Stay Synchronized

**The fundamental goal all pointer system requirements derive from.**

---

<!-- section_id: "98f8491b-8bf8-40b1-a37e-8a1ca725502e" -->
## Definition

> Pointer files always resolve to the correct canonical location, even after directories are moved or renamed. Stale pointers are detected automatically and agents are prompted to fix them.

---

<!-- section_id: "99ac2ac9-74be-4747-9f46-4edb324b2b3b" -->
## The Problem

Current pointer files use hardcoded relative paths. When directories move:
- Paths break silently
- No agent is warned about the stale reference
- Manual path computation is error-prone and tedious
- No way to validate all pointers at once

---

<!-- section_id: "42608161-36c9-41e6-8fff-93de1cebc943" -->
## The Vision

A system where:
- Pointer files self-declare their target via structured frontmatter
- A script resolves targets dynamically (by entity name, not by hardcoded path)
- Hooks trigger validation automatically after edits
- Stale pointers are caught during `agnostic-sync.sh` runs
- New pointers are trivial to create (fill in frontmatter, run script)

---

<!-- section_id: "abcfd27e-1598-479a-bb28-7543224467c6" -->
## Four Branches

| Branch | Question | Description |
|--------|----------|-------------|
| [**01_pointer_format**](./01_pointer_format/) | "How are pointers structured?" | YAML frontmatter format, required fields, body conventions |
| [**02_path_resolution**](./02_path_resolution/) | "How are canonical paths found?" | Entity search, stage navigation, subpath resolution |
| [**03_trigger_automation**](./03_trigger_automation/) | "How are pointers validated automatically?" | Hooks, agnostic-sync integration, CI-ready validation |
| [**04_uuid_graph_traversal**](./04_uuid_graph_traversal/) | "How does the UUID system support graph traversal and queries?" | Parent/children graph, query CLI, resource indexes, efficient agent lookups |

---

<!-- section_id: "2ceb0b4c-2ce5-467d-bb14-9c620a5cd75f" -->
## Branch Structure

```
00_pointers_stay_synchronized/           (this folder - the root)
|
+-- 01_pointer_format/                   How pointers are structured
|   +-- need_01_frontmatter_standard     YAML fields, required vs optional
|   +-- need_02_body_convention          Canonical location line, description
|
+-- 02_path_resolution/                  How canonical paths are found
|   +-- need_01_entity_search            Find entity dirs by name
|   +-- need_02_relative_path_compute    Compute portable relative paths
|
+-- 03_trigger_automation/               How pointers validate automatically
|   +-- need_01_hook_triggers            Claude Code PostToolUse hooks
|   +-- need_02_sync_integration         agnostic-sync.sh end-of-run validation
|
+-- 04_uuid_graph_traversal/             How the UUID system supports graph traversal
    +-- need_01_parent_children_graph    Entity hierarchy as navigable graph
    +-- need_02_query_cli                Flexible filtering and search across all UUIDs
    +-- need_03_resource_indexes         Per-entity resource indexes for O(1) lookup
```

---

<!-- section_id: "7e72ed0d-f80f-4dfc-955e-dafa04f3fa71" -->
## Success Criteria

The root need is satisfied when:
- [x] All pointer files use YAML frontmatter with `pointer_to:` and `canonical_entity:`
- [x] `pointer-sync.sh` resolves all pointers correctly
- [x] `pointer-sync.sh --validate` exits 0 when all pointers are valid, 1 when any are broken
- [x] Claude Code hook fires after editing pointer files
- [x] `agnostic-sync.sh` reports pointer validation at end of run
- [x] Creating a new pointer takes <1 minute (fill frontmatter, run script)
- [x] UUID index supports parent/children graph traversal (`--parent`, `--children`)
- [x] Query CLI enables flexible filtering across all UUID entries (`--query`)
- [x] Per-entity `resource_index.json` rolled out to all entities (50 entities)
- [x] Root `.uuid-index.json` aggregates entities, stages, and resources (5,313 entries)
- [ ] Incremental index updates (rebuild only changed entities)
- [ ] Short-name resolution for entities (fuzzy/partial matching)
- [ ] Auto-UUID assignment on entity creation (entity-creation skill integration)
