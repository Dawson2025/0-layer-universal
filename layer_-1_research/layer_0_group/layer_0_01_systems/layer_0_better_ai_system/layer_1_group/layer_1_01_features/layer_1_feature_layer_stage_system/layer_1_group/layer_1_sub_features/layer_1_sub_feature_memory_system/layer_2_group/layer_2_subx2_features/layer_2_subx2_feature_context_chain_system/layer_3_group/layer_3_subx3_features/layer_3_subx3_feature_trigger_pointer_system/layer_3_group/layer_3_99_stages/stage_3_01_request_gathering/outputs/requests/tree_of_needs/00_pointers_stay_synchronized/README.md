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

**The reference fragility problem spans two layers:**

### Layer 1: Pointer Files (Branches 01-04)
Current pointer files use hardcoded relative paths. When directories move:
- Paths break silently
- No agent is warned about the stale reference
- Manual path computation is error-prone and tedious
- No way to validate all pointers at once

### Layer 2: All References Across the Entire Codebase (Branch 05)
The broader and more fundamental problem: **every reference in the system uses hardcoded filesystem paths**. This affects not just pointer files but everything — scripts calling scripts, documentation referencing resources, context files pointing to tools, hooks calling scripts, knowledge docs citing other docs. When anything moves (a file, directory, entity, stage, or subtree), dozens to hundreds of references break simultaneously. The script protocol migration (2026-03-07) proved this: moving 12 scripts required manually updating 81+ files. This is slow, error-prone, and the exact inefficiency that a UUID-based system should eliminate.

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
## Five Branches

| Branch | Question | Description |
|--------|----------|-------------|
| [**01_pointer_format**](./01_pointer_format/) | "How are pointers structured?" | YAML frontmatter format, required fields, body conventions |
| [**02_path_resolution**](./02_path_resolution/) | "How are canonical paths found?" | Entity search, stage navigation, subpath resolution |
| [**03_trigger_automation**](./03_trigger_automation/) | "How are pointers validated automatically?" | Hooks, agnostic-sync integration, CI-ready validation |
| [**04_uuid_graph_traversal**](./04_uuid_graph_traversal/) | "How does the UUID system support graph traversal and queries?" | Parent/children graph, query CLI, resource indexes, efficient agent lookups |
| [**05_uuid_based_reference_resolution**](./05_uuid_based_reference_resolution/) | "How do we eliminate path-based references so moves don't break things?" | resolve-uuid function, placeholder syntax, self-healing context files, trivial move workflow |

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
|   +-- need_01_hook_triggers            Automated notification on pointer edits
|   +-- need_02_sync_integration         agnostic-sync.sh end-of-run validation
|
+-- 04_uuid_graph_traversal/             How the UUID system supports graph traversal
|   +-- need_01_parent_children_graph    Entity hierarchy as navigable graph
|   +-- need_02_query_cli                Flexible filtering and search across all UUIDs
|   +-- need_03_resource_indexes         Per-entity resource indexes for O(1) lookup
|
+-- 05_uuid_based_reference_resolution/  How ALL references use UUID instead of paths
    +-- need_01_resolve_uuid_function    Shell function: UUID → current path (~5ms)
    +-- need_02_placeholder_syntax       {{resolve:UUID}} in 0AGNOSTIC.md source files
    +-- need_03_self_healing_contexts    AI apps resolve UUIDs at moment of use
    +-- need_04_move_workflow            mv + rebuild-index = done (no grep-replace)
```

---

<!-- section_id: "7e72ed0d-f80f-4dfc-955e-dafa04f3fa71" -->
## Success Criteria

The root need is satisfied when:
- [x] All pointer files use YAML frontmatter with `pointer_to:` and `canonical_entity:`
- [x] `pointer-sync.sh` resolves all pointers correctly
- [x] `pointer-sync.sh --validate` exits 0 when all pointers are valid, 1 when any are broken
- [x] Editing agent is notified when pointer files are modified
- [x] `agnostic-sync.sh` reports pointer validation at end of run
- [x] Creating a new pointer takes <1 minute (fill frontmatter, run script)
- [x] UUID index supports parent/children graph traversal (`--parent`, `--children`)
- [x] Query CLI enables flexible filtering across all UUID entries (`--query`)
- [x] Per-entity `resource_index.json` rolled out to all entities (50 entities)
- [x] Root `.uuid-index.json` aggregates entities, stages, and resources (5,313 entries)
- [ ] Incremental index updates (rebuild only changed entities)
- [ ] Short-name resolution for entities (fuzzy/partial matching)
- [ ] Auto-UUID assignment on entity creation (entity-creation skill integration)
- [ ] `resolve-uuid` function exists and resolves any UUID → current path in <10ms
- [ ] Scripts use `resolve-uuid` for cross-protocol calls instead of hardcoded paths
- [ ] 0AGNOSTIC.md files use `{{resolve:UUID}}` placeholders for resource references
- [ ] `agnostic-sync.sh` resolves `{{resolve:UUID}}` placeholders during generation
- [ ] Generated context files include UUID references with resolve-uuid instructions (self-healing)
- [ ] Moving a file/directory/entity requires only `mv` + `rebuild-index` (no grep-replace)
- [ ] Pre-commit hook validates all UUID references resolve to existing paths
- [ ] Auto-rebuild of UUID index via git hooks (post-checkout, post-merge)

---

<!-- section_id: "3f4a5b6c-7d8e-4f9a-0b1c-2d3e4f5a6b7c" -->
## Operations View

The needs above translate into three categories of operations:

| Category | Description | Examples |
|----------|-------------|---------|
| **Fully Automated** | Deterministic, no judgment — runs without agent | Index rebuilds, pointer validation, UUID assignment, git hooks |
| **Agent-Assisted** | Requires search, discovery, or creative decisions — agent does it with system-provided interfaces | Entity lookup, UUID resolution, hierarchy navigation, pointer creation |
| **Hybrid** | Automated trigger, but agent needs to see or act on results | Edit notifications, stale pointer reports, move impact summaries |

> **Design details**: See `stage_3_04_design/outputs/operations_and_interface_design.md` for the full operations inventory, automation decision framework, and agent interface design.
>
> **Situational analysis**: See `stage_3_02_research/outputs/operational_situations_analysis.md` for detailed documentation of when, why, and under what conditions each operation is triggered.
