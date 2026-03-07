---
resource_id: "c8d88e83-ee42-43c7-baf6-b9913b549aa0"
resource_type: "output"
resource_name: "uuid_test_design"
---
# UUID Identity System — Test Design

<!-- section_id: "0f2ded3e-3058-4f2e-89fe-3bd2b4500507" -->
## Date: 2026-03-02
<!-- section_id: "12bd7cc6-f8dd-4318-8e05-e77edaa245ea" -->
## Design Reference: `../../stage_3_04_design/outputs/uuid_identity_system_design.md`
<!-- section_id: "72ca1ebf-9095-4219-abf5-3f92a67e0c6b" -->
## Implementation Plan: `../../stage_3_05_planning/outputs/uuid_implementation_plan.md`
<!-- section_id: "4653a9bb-5b59-4799-887f-b6347c4ecfe3" -->
## Existing Test Suite: `test_pointer_sync.sh` (108 tests, same directory)

---

<!-- section_id: "79c476ee-84b3-4092-9634-6f3b7f0aad9b" -->
## Test Strategy

<!-- section_id: "b044f71f-b6fe-4ddf-b16e-9262f995766e" -->
### Approach

1. **Extend existing test suite** (`test_pointer_sync.sh`) with UUID-specific categories (20-25)
2. **Create new test suite** (`test_uuid_scripts.sh`) for migration/assignment scripts
3. **All tests use temp directories** — no modification of real repo
4. **Mock hierarchy** mirrors the real repo structure with entities, stages, resources

<!-- section_id: "0e2e9982-5e46-44ae-a41e-7028004566c0" -->
### Test Environments

| Suite | Tests | What It Validates |
|-------|-------|-------------------|
| `test_pointer_sync.sh` (extended) | 108 existing + ~50 new | pointer-sync.sh UUID resolution, backward compat |
| `test_uuid_scripts.sh` (new) | ~60 tests | assign-uuids.sh, create-stage-indexes.sh, migrate-pointers.sh |

---

<!-- section_id: "984fbba0-b82f-4597-a5cc-dd62a6a14c3b" -->
## Test Category 20: UUID-Based Entity Resolution

**Tests pointer-sync.sh resolves entities by UUID when `canonical_entity_id` is present.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 20.1 | UUID resolves to correct entity | Pointer with `canonical_entity_id` pointing to entity with matching `entity_id` in 0AGNOSTIC.md | UPDATED with correct path |
| 20.2 | UUID not found → BROKEN | Pointer with `canonical_entity_id` that doesn't match any entity | BROKEN |
| 20.3 | UUID takes priority over name | Pointer with both `canonical_entity_id` and `canonical_entity_name`, name points to wrong entity | Resolves via UUID, not name |
| 20.4 | Renamed entity still resolves by UUID | Entity directory renamed after UUID assigned; pointer uses UUID | Resolves to new path |
| 20.5 | Legacy pointer (name only, no UUID) | Pointer with `canonical_entity` but no `_id` | Resolves via name (backward compat) |
| 20.6 | Legacy pointer emits deprecation warning | Same as 20.5 | Output contains "deprecation" or "legacy" |

---

<!-- section_id: "0fd382f7-4a28-419d-b073-e6cb31b5b2c4" -->
## Test Category 21: UUID-Based Stage Resolution

**Tests pointer-sync.sh resolves stages by UUID via stage_index.json.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 21.1 | Stage UUID resolves via registry | Pointer with `canonical_stage_id`, entity has `stage_index.json` | Stage directory found |
| 21.2 | Stage UUID not in registry → BROKEN | Pointer with `canonical_stage_id` that's not in `stage_index.json` | BROKEN |
| 21.3 | Stage renamed, UUID still resolves | Stage directory renamed, stage_index.json updated with new directory name, UUID stays | Resolves via UUID |
| 21.4 | Legacy stage (name only) | Pointer with `canonical_stage` but no `_id` | Resolves via name (backward compat) |
| 21.5 | Missing stage_index.json falls back to name | Entity has no `stage_index.json`, pointer has `canonical_stage_id` | Falls back to name resolution |

---

<!-- section_id: "f6ac694d-31b2-49f0-8e60-82c142e772ba" -->
## Test Category 22: Resource ID Resolution

**Tests pointer-sync.sh resolves resources by `canonical_resource_id`.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 22.1 | Resource UUID resolves directly | Pointer with `canonical_resource_id`, resource has matching `resource_id` in frontmatter | Full path resolved |
| 22.2 | Resource UUID not found → BROKEN | Pointer with `canonical_resource_id` that matches nothing | BROKEN |
| 22.3 | Resource UUID skips entity/stage resolution | Pointer has `canonical_resource_id` AND `canonical_entity_id`; resource_id resolves directly | Uses resource path, not entity+stage+subpath |
| 22.4 | Resource renamed, UUID still resolves | Resource file renamed, `resource_id` in frontmatter unchanged | Resolves to new filename |

---

<!-- section_id: "41c1a96d-c825-490b-a297-fe45617e98ba" -->
## Test Category 23: Index Behavior

**Tests `.uuid-index.json` creation, usage, and rebuild.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 23.1 | `--rebuild-index` creates index file | Run pointer-sync.sh --rebuild-index | `.uuid-index.json` exists with entity mappings |
| 23.2 | Index used for resolution | Index exists, pointer uses UUID | Resolves without scanning all 0AGNOSTIC.md |
| 23.3 | Index miss triggers auto-rebuild | Index missing, pointer uses UUID | Rebuilds index, then resolves |
| 23.4 | Stale index (entity moved) | Index has old path, entity moved | Auto-rebuild finds new path |
| 23.5 | Index file format valid JSON | Run --rebuild-index | Valid JSON with "entities" key |

---

<!-- section_id: "0a29d780-6e9e-4e11-986e-4471711af5bb" -->
## Test Category 24: Backward Compatibility

**Ensures all 108 existing tests pass unchanged.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 24.1 | All legacy pointer files still resolve | No UUIDs in any pointer or entity | Same behavior as before UUID changes |
| 24.2 | Mixed pointers (some UUID, some name) | Repo with both UUID and name-based pointers | Both resolve correctly |
| 24.3 | Empty UUID fields treated as absent | `canonical_entity_id: ""` | Falls back to name resolution |
| 24.4 | Original CLI flags unchanged | --dry-run, --validate, --verbose, --help | Same behavior |

---

<!-- section_id: "58af3f0a-7bba-4031-b063-a37c0439ec24" -->
## Test Category 25: assign-entity-uuids.sh

**Tests the UUID assignment script for entities.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 25.1 | Assigns UUID to entity without one | 0AGNOSTIC.md with `## Identity` but no `entity_id` | `entity_id: "uuid"` inserted after `## Identity` |
| 25.2 | Skips entity that already has UUID | 0AGNOSTIC.md already has `entity_id` | File unchanged |
| 25.3 | Idempotent (run twice) | Run script twice on same entity | Only one `entity_id` line, same UUID |
| 25.4 | `--dry-run` doesn't modify | Run with --dry-run | File unchanged, output shows what would change |
| 25.5 | Valid UUID v4 format | Run script | UUID matches `[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}` |
| 25.6 | Handles multiple entities | 5 0AGNOSTIC.md files | All 5 get unique UUIDs |
| 25.7 | Skips 0AGNOSTIC.md without Identity section | File exists but no `## Identity` | File unchanged |

---

<!-- section_id: "e8452379-d3d7-43fd-a65f-87333ab14220" -->
## Test Category 26: create-stage-indexes.sh

**Tests stage UUID assignment and registry creation.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 26.1 | Creates stage_index.json | Entity with stage dirs, no registry yet | `stage_index.json` in `stage_N_00_stage_registry/` |
| 26.2 | All stages in registry | Entity with 12 stage dirs | stage_index.json has 12 entries |
| 26.3 | Stage 0AGNOSTIC.md gets stage_id | Stage dir with 0AGNOSTIC.md | `stage_id:` inserted |
| 26.4 | Stage without 0AGNOSTIC.md | Scaffolded stage (no 0AGNOSTIC.md) | UUID only in registry, no file modified |
| 26.5 | entity_id in registry matches entity | Entity has `entity_id: "X"` | stage_index.json `entity_id` = "X" |
| 26.6 | Idempotent | Run twice | Same UUIDs, no duplicates |
| 26.7 | `--dry-run` | Run with --dry-run | No files modified |
| 26.8 | Valid JSON output | Create registry | `jq .` succeeds on stage_index.json |

---

<!-- section_id: "1f2b4e59-84f4-4849-b56d-38aa8bc1d985" -->
## Test Category 27: assign-resource-uuids.sh

**Tests resource UUID assignment to knowledge, rules, protocols, skills, and output files.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 27.1 | Knowledge doc gets resource_id | `.0agnostic/01_knowledge/topic/doc.md` without frontmatter | YAML frontmatter with `resource_id`, `resource_type: "knowledge"` |
| 27.2 | Rule gets resource_id | `.0agnostic/02_rules/static/rule/rule.md` | `resource_type: "rule"` |
| 27.3 | Protocol gets resource_id | `.0agnostic/03_protocols/protocol.md` | `resource_type: "protocol"` |
| 27.4 | SKILL.md gets resource_id | `.0agnostic/.../05_skills/skill/SKILL.md` | `resource_type: "skill"` |
| 27.5 | Output file gets resource_id | `stage_3_04_design/outputs/design_doc.md` without frontmatter | YAML frontmatter with `resource_id`, `resource_type: "output"` |
| 27.6 | Nested output file gets resource_id | `stage_3_02_research/outputs/by_topic/arch/doc.md` | `resource_type: "output"` |
| 27.7 | Existing frontmatter preserved | File already has `---` frontmatter with other fields | `resource_id` added, other fields kept |
| 27.8 | Skips README.md | `01_knowledge/README.md` | File unchanged |
| 27.9 | Skips 0INDEX.md | `01_knowledge/0INDEX.md` | File unchanged |
| 27.10 | Skips auto-generated files | `CLAUDE.md`, `.integration.md` | File unchanged |
| 27.11 | Skips .1merge/ files | `.1merge/claude/overrides/file.md` | File unchanged |
| 27.12 | Skips stage_index.json | `stage_3_00_stage_registry/stage_index.json` | File unchanged |
| 27.13 | Idempotent | Run twice | Same IDs, no duplicates |
| 27.14 | `--dry-run` | Run with --dry-run | No files modified |

---

<!-- section_id: "efc249df-de15-4eeb-9cf1-8e031e5d507d" -->
## Test Category 28: migrate-pointers.sh

**Tests migration of existing name-based pointers to UUID-based.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 28.1 | Adds entity UUID to pointer | Pointer with `canonical_entity: "name"`, entity has `entity_id` | `canonical_entity_id` added |
| 28.2 | Renames entity field | Same as 28.1 | `canonical_entity` → `canonical_entity_name` |
| 28.3 | Adds stage UUID to pointer | Pointer with `canonical_stage: "name"`, stage in registry | `canonical_stage_id` added |
| 28.4 | Renames stage field | Same as 28.3 | `canonical_stage` → `canonical_stage_name` |
| 28.5 | Skips already-migrated pointer | Pointer already has `canonical_entity_id` | File unchanged |
| 28.6 | Entity not found → skip with warning | Pointer references entity with no UUID | Warning emitted, file unchanged |
| 28.7 | Multiple pointers migrated | 5 pointer files | All 5 migrated correctly |
| 28.8 | `--dry-run` | Run with --dry-run | No files modified |
| 28.9 | pointer-sync.sh validates after migration | Run migrate, then pointer-sync.sh --validate | Exit 0 |

---

<!-- section_id: "52e78fab-dc71-49c4-9d7d-b12014a0bee5" -->
## Test Category 29: Resource Index

**Tests resource_index.json creation and usage.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 29.1 | Registry created with all resources | Entity with knowledge docs, rules, protocols | `resource_index.json` has entries for each |
| 29.2 | Registry valid JSON | Create registry | `jq .` succeeds |
| 29.3 | Resource paths in registry are relative | Registry entries | Paths relative to `.0agnostic/` |
| 29.4 | Registry matches frontmatter IDs | Create registry, check vs file frontmatter | All IDs match |

---

<!-- section_id: "5c3cc0d8-b64f-4582-be9a-ed7678143be6" -->
## Test Category 30: Edge Cases

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 30.1 | Entity with no stages (leaf) | Entity that has 0AGNOSTIC.md but no layer_N_group/ | `entity_id` assigned, no registry created |
| 30.2 | Very deep nesting (5+ layers) | Entity at layer 5+ depth | UUID resolution works at any depth |
| 30.3 | UUID with special characters in surrounding YAML | Adjacent YAML fields with quotes, colons | Correct extraction |
| 30.4 | Two entities, same name, different UUIDs | `layer_1_feature_auth` in two locations | UUID resolves to correct one |
| 30.5 | Entity deleted but pointer remains | Pointer with UUID, entity directory removed | BROKEN (not crash) |
| 30.6 | Registry.json corrupted (invalid JSON) | Malformed stage_index.json | Graceful fallback to name resolution |
| 30.7 | Index file corrupted | Malformed .uuid-index.json | Auto-rebuild, then resolve |
| 30.8 | 0AGNOSTIC.md with entity_id but no ## Identity | entity_id at file top, no section header | Still extracted correctly |

---

<!-- section_id: "ecb9223e-7caa-483f-a286-53c676d33a48" -->
## Test Category 31: Reference Integrity

**Tests `--find-references`, `--detect-cycles`, `--gc`, and duplicate UUID detection.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 31.1 | `--find-references` finds all pointers to UUID | 3 pointers reference entity UUID X | Output lists all 3 pointer files |
| 31.2 | `--find-references` returns empty for unreferenced UUID | Entity with UUID that no pointer references | Output: "0 references found" |
| 31.3 | `--detect-cycles` finds simple cycle | Pointer A→B and B→A | Reports cycle: A → B → A |
| 31.4 | `--detect-cycles` finds no cycles | Linear pointer chain A→B→C | Exit 0, no cycles reported |
| 31.5 | `--detect-cycles` handles 3-node cycle | A→B, B→C, C→A | Reports cycle: A → B → C → A |
| 31.6 | `--gc` removes orphaned entry | Index has entry for deleted entity | Entry removed, other entries preserved |
| 31.7 | `--gc` keeps valid entries | Index has only valid entries | Index unchanged |
| 31.8 | Duplicate UUID detected during rebuild | Two entities with same `entity_id` | Error reported, first kept |
| 31.9 | `--find-references` works with stage UUIDs | Pointer references stage UUID | Found correctly |
| 31.10 | `--find-references` works with resource UUIDs | Pointer references resource UUID | Found correctly |

---

<!-- section_id: "5722f122-3f94-4a10-896d-3de2c4e1dd29" -->
## Test Category 32: Index Safety & Concurrency

**Tests atomic writes, file locking, checksum validation.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 32.1 | Atomic write produces valid JSON | Interrupt index write mid-stream | Old or new file — never partial |
| 32.2 | Lock prevents concurrent writes | Run `--rebuild-index` from two processes | Both complete, no corruption |
| 32.3 | Stale lock removed after timeout | Lock dir older than 5 minutes | Lock removed, operation proceeds |
| 32.4 | Checksum mismatch triggers rebuild | Manually edit index content (change a path) | Auto-rebuild from local indexes |
| 32.5 | Valid checksum passes | Unmodified index | No rebuild triggered |
| 32.6 | Lock dir cleaned up after operation | Run any index mutation | No `.lock` directory remains |

---

<!-- section_id: "f5c62d78-8ece-4063-b737-be57729a79f8" -->
## Test Category 33: Universal File IDs

**Tests `assign-file-uuids.sh` across all file types.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 33.1 | `.sh` script gets comment-header UUID | Script without resource_id | `# resource_id: "uuid"` after shebang |
| 33.2 | `.sh` with existing resource_id skipped | Script already has UUID | File unchanged |
| 33.3 | `.json` file gets file_id | JSON file without file_id | `"file_id": "uuid"` in root |
| 33.4 | `.jsonld` file gets file_id | JSONLD without file_id | `"file_id": "uuid"` in root |
| 33.5 | Auto-generated `.md` gets derived_from | `CLAUDE.md` without derived_from | `<!-- derived_from: "source-uuid" -->` |
| 33.6 | `README.md` gets resource_id | README without frontmatter | YAML frontmatter with `resource_id` |
| 33.7 | `0INDEX.md` gets resource_id | 0INDEX without frontmatter | YAML frontmatter with `resource_id` |
| 33.8 | `.1merge/` file gets resource_id | .1merge override file | YAML frontmatter with `resource_id` |
| 33.9 | `--type=sh` only processes scripts | Run with --type=sh | Only .sh files modified |
| 33.10 | Idempotent across all types | Run twice on all types | Same UUIDs, no duplicates |

---

<!-- section_id: "dc571b9b-f697-4ea9-9cb6-3e39d6be6e60" -->
## Test Category 34: Git Hooks & Validation

**Tests post-merge hooks, materialized view staleness detection.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 34.1 | Post-merge hook runs `--validate` | Simulate merge that deletes entity | BROKEN pointers reported |
| 34.2 | Post-merge hook runs `--rebuild-index` | Simulate merge that adds entity | New entity in index |
| 34.3 | Materialized view staleness detected | Edit 0AGNOSTIC.md, don't run sync | Validation reports stale CLAUDE.md |
| 34.4 | Fresh materialized view passes | Run agnostic-sync.sh after edit | Validation passes |

---

<!-- section_id: "3e4782e8-78ee-4b5d-aa0a-769820337056" -->
## Summary

| Suite | Categories | Estimated Tests |
|-------|-----------|-----------------|
| test_pointer_sync.sh (extended) | 20-24, 30-32 | ~60 new tests |
| test_uuid_scripts.sh (new) | 25-29, 33 | ~58 tests |
| test_hooks.sh (new) | 34 | ~4 tests |
| **Total new** | **15 categories** | **~122 tests** |
| **Grand total (with existing 108)** | **34 categories** | **~230 tests** |

<!-- section_id: "18cf9b7d-61e6-4df2-b513-6a4f6c87596f" -->
### Test Execution Order

1. Run existing 108 tests first (regression gate)
2. Run UUID resolution tests (cat 20-24) after pointer-sync.sh is updated
3. Run script tests (cat 25-29, 33) after each script is written
4. Run reference integrity tests (cat 31-32) after Phase 3b
5. Run edge cases (cat 30) after all core phases
6. Run hook tests (cat 34) after Phase 9
7. Full suite run as final gate before commit

<!-- section_id: "a1173c1c-7f37-4cad-a98a-9f7d7c6c1190" -->
### Pass Criteria

- **All 108 existing tests**: PASS (zero regressions)
- **All new UUID tests**: PASS
- **pointer-sync.sh --validate on real repo**: exit 0
- **No BROKEN pointers introduced by migration**
- **Index locking prevents concurrent corruption**
- **Checksum validation catches corrupted indexes**

---

<!-- section_id: "a4b6c8d0-e2f3-4a5b-7c9d-1e3f5a7b9c0d" -->
## Test Category 35: Parent/Children Graph

**Tests `--parent` and `--children` CLI commands and graph data in the index.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 35.1 | `--parent` returns correct parent | Entity with known parent link | Shows parent UUID, name, path |
| 35.2 | `--parent` on root entity | Entity with no parent_id | Reports "no parent" or root status |
| 35.3 | `--parent --verbose` walks full chain | Entity 3 levels deep | Shows chain: entity → parent → grandparent → root |
| 35.4 | `--children` lists direct children | Entity with 3 known children | Lists all 3 children with UUIDs and paths |
| 35.5 | `--children` on leaf entity | Entity with no children | Reports "no children" |
| 35.6 | Parent/children consistency | Build index, check graph | Every entity in parent.children also has parent_id = parent |
| 35.7 | Broken parent path | Entity with `**Parent**:` pointing to nonexistent file | Warning emitted, no parent_id in index |
| 35.8 | Parent without entity_id | Entity referencing parent whose 0AGNOSTIC.md lacks entity_id | Warning emitted, no parent_id in index |

---

<!-- section_id: "b5c7d9e1-f3a4-4b6c-8d0e-2f4a6b8c0d1e" -->
## Test Category 36: Query CLI

**Tests `--query` command with various filter combinations.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 36.1 | Query by type=entity | Index with mixed types | Returns only entity entries |
| 36.2 | Query by type=stage | Index with mixed types | Returns only stage entries |
| 36.3 | Query by type=resource | Index with mixed types | Returns only resource entries |
| 36.4 | Query by name=*pattern* | Index with various names | Returns entries matching glob pattern |
| 36.5 | Query by resource_type=script | Index with resources | Returns only script-type resources |
| 36.6 | Query with multiple filters (AND) | type=entity name=*research* | Returns entities with "research" in name |
| 36.7 | Query by has_children=true | Index with graph data | Returns only entities with children |
| 36.8 | Query by parent_id=<uuid> | Index with graph data | Returns children of specific parent |
| 36.9 | Query by path=*pattern* | Index entries | Returns entries with matching paths |
| 36.10 | Query with no matches | Specific filter that matches nothing | Empty result, no error |
| 36.11 | Query with no filters | No key=value args | Returns all entries (or error) |

---

<!-- section_id: "c6d8e0f2-a4b5-4c7d-9e1f-3a5b7c9d1e2f" -->
## Test Category 37: Resource Index Generation

**Tests `create-resource-indexes.sh` bulk and per-entity generation.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 37.1 | Creates resource_index.json for entity | Entity with .0agnostic/ and UUID-bearing files | Valid JSON index at .0agnostic/resource_index.json |
| 37.2 | Skips entity without entity_id | Entity with 0AGNOSTIC.md but no entity_id | Skipped with verbose message, no error |
| 37.3 | Skips derived files | Entity with CLAUDE.md, .integration.md | Derived files not in resource index |
| 37.4 | Resource types inferred correctly | Entity with script, knowledge, rule files | Correct resource_type for each |
| 37.5 | Paths relative to entity root | Entity with nested resources | All paths are relative, not absolute |
| 37.6 | Duplicate UUID detection | Two files with same resource_id in entity | Error reported |
| 37.7 | --dry-run shows without creating | Entity without index | No file created, output shows what would change |
| 37.8 | --entity flag processes single entity | Specific entity path | Only that entity processed |
| 37.9 | Idempotent (run twice) | Run script twice | Same output, file_id preserved |
| 37.10 | Valid JSON output | Create index | `jq .` succeeds on resource_index.json |

---

<!-- section_id: "d7e9f1a3-b5c6-4d8e-0f2a-4b6c8d0e2f3a" -->
## Updated Summary

| Suite | Categories | Estimated Tests |
|-------|-----------|-----------------|
| test_pointer_sync.sh (extended) | 20-24, 30-32, 35-36 | ~80 new tests |
| test_uuid_scripts.sh (new) | 25-29, 33, 37 | ~68 tests |
| test_hooks.sh (new) | 34 | ~4 tests |
| **Total new** | **18 categories** | **~152 tests** |
| **Grand total (with existing 108)** | **37 categories** | **~260 tests** |
