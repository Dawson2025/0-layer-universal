# UUID Identity System — Test Design

## Date: 2026-03-02
## Design Reference: `../../stage_3_04_design/outputs/uuid_identity_system_design.md`
## Implementation Plan: `../../stage_3_05_planning/outputs/uuid_implementation_plan.md`
## Existing Test Suite: `test_pointer_sync.sh` (108 tests, same directory)

---

## Test Strategy

### Approach

1. **Extend existing test suite** (`test_pointer_sync.sh`) with UUID-specific categories (20-25)
2. **Create new test suite** (`test_uuid_scripts.sh`) for migration/assignment scripts
3. **All tests use temp directories** — no modification of real repo
4. **Mock hierarchy** mirrors the real repo structure with entities, stages, resources

### Test Environments

| Suite | Tests | What It Validates |
|-------|-------|-------------------|
| `test_pointer_sync.sh` (extended) | 108 existing + ~50 new | pointer-sync.sh UUID resolution, backward compat |
| `test_uuid_scripts.sh` (new) | ~60 tests | assign-uuids.sh, create-stage-indexes.sh, migrate-pointers.sh |

---

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

## Test Category 22: Resource ID Resolution

**Tests pointer-sync.sh resolves resources by `canonical_resource_id`.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 22.1 | Resource UUID resolves directly | Pointer with `canonical_resource_id`, resource has matching `resource_id` in frontmatter | Full path resolved |
| 22.2 | Resource UUID not found → BROKEN | Pointer with `canonical_resource_id` that matches nothing | BROKEN |
| 22.3 | Resource UUID skips entity/stage resolution | Pointer has `canonical_resource_id` AND `canonical_entity_id`; resource_id resolves directly | Uses resource path, not entity+stage+subpath |
| 22.4 | Resource renamed, UUID still resolves | Resource file renamed, `resource_id` in frontmatter unchanged | Resolves to new filename |

---

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

## Test Category 24: Backward Compatibility

**Ensures all 108 existing tests pass unchanged.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 24.1 | All legacy pointer files still resolve | No UUIDs in any pointer or entity | Same behavior as before UUID changes |
| 24.2 | Mixed pointers (some UUID, some name) | Repo with both UUID and name-based pointers | Both resolve correctly |
| 24.3 | Empty UUID fields treated as absent | `canonical_entity_id: ""` | Falls back to name resolution |
| 24.4 | Original CLI flags unchanged | --dry-run, --validate, --verbose, --help | Same behavior |

---

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

## Test Category 29: Resource Index

**Tests resource_index.json creation and usage.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 29.1 | Registry created with all resources | Entity with knowledge docs, rules, protocols | `resource_index.json` has entries for each |
| 29.2 | Registry valid JSON | Create registry | `jq .` succeeds |
| 29.3 | Resource paths in registry are relative | Registry entries | Paths relative to `.0agnostic/` |
| 29.4 | Registry matches frontmatter IDs | Create registry, check vs file frontmatter | All IDs match |

---

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

## Test Category 34: Git Hooks & Validation

**Tests post-merge hooks, materialized view staleness detection.**

| # | Test | Setup | Expected |
|---|------|-------|----------|
| 34.1 | Post-merge hook runs `--validate` | Simulate merge that deletes entity | BROKEN pointers reported |
| 34.2 | Post-merge hook runs `--rebuild-index` | Simulate merge that adds entity | New entity in index |
| 34.3 | Materialized view staleness detected | Edit 0AGNOSTIC.md, don't run sync | Validation reports stale CLAUDE.md |
| 34.4 | Fresh materialized view passes | Run agnostic-sync.sh after edit | Validation passes |

---

## Summary

| Suite | Categories | Estimated Tests |
|-------|-----------|-----------------|
| test_pointer_sync.sh (extended) | 20-24, 30-32 | ~60 new tests |
| test_uuid_scripts.sh (new) | 25-29, 33 | ~58 tests |
| test_hooks.sh (new) | 34 | ~4 tests |
| **Total new** | **15 categories** | **~122 tests** |
| **Grand total (with existing 108)** | **34 categories** | **~230 tests** |

### Test Execution Order

1. Run existing 108 tests first (regression gate)
2. Run UUID resolution tests (cat 20-24) after pointer-sync.sh is updated
3. Run script tests (cat 25-29, 33) after each script is written
4. Run reference integrity tests (cat 31-32) after Phase 3b
5. Run edge cases (cat 30) after all core phases
6. Run hook tests (cat 34) after Phase 9
7. Full suite run as final gate before commit

### Pass Criteria

- **All 108 existing tests**: PASS (zero regressions)
- **All new UUID tests**: PASS
- **pointer-sync.sh --validate on real repo**: exit 0
- **No BROKEN pointers introduced by migration**
- **Index locking prevents concurrent corruption**
- **Checksum validation catches corrupted indexes**
