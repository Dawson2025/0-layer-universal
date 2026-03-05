# UUID Identity System — Implementation Plan

## Date: 2026-03-02
## Design Reference: `../../stage_3_04_design/outputs/uuid_identity_system_design.md`
## Test Design: `../../stage_3_07_testing/outputs/uuid_test_design.md`

---

## Overview

This plan breaks the UUID identity system implementation into **8 phases** across **6 agent roles**. Each phase produces testable artifacts. Phases are ordered by dependency — later phases depend on earlier ones. Some phases can run in parallel.

---

## Agent Roles

| Agent | Type | Responsibility |
|-------|------|----------------|
| **Coordinator** | Manager (you) | Sequence phases, review outputs, handle cross-phase issues |
| **Script Agent** | general-purpose | Write bash scripts (assign-uuids.sh, migrate-pointers.sh) |
| **Pointer-Sync Agent** | general-purpose | Modify pointer-sync.sh for UUID resolution |
| **Skill Agent** | general-purpose | Update entity-creation skill for UUID generation |
| **Docs Agent** | general-purpose | Update entity_structure.md, pointer conventions, protocols |
| **Test Agent** | general-purpose | Write and run test suites for each phase |

---

## Phase Dependency Graph

```
Phase 1 (assign-uuids.sh) ──┬──> Phase 3 (pointer-sync.sh update)
                             │
Phase 2 (stage registries) ──┤──> Phase 5 (migrate pointers)
                             │
Phase 1b (resource IDs) ─────┘

Phase 4 (entity-creation skill) — independent, can run parallel with 3

Phase 6 (docs update) — after phases 1-5

Phase 7 (full integration test) — after all phases

Phase 8 (run agnostic-sync.sh) — final
```

---

## Phase 1: Assign Entity UUIDs

**Agent**: Script Agent
**Input**: All `0AGNOSTIC.md` files in the repo
**Output**: `assign-entity-uuids.sh` script at `.0agnostic/`

### Task

Write a script that:
1. Finds all `0AGNOSTIC.md` files under `0_layer_universal/`
2. For each, checks if `entity_id:` already exists in the Identity section
3. If missing, generates UUID v4 via `uuidgen`
4. Inserts `entity_id: "uuid"` on the line after `## Identity`
5. Reports: `Added entity_id <uuid> to <path>`
6. Supports `--dry-run` (show what would change)

### Acceptance Criteria
- Every `0AGNOSTIC.md` with an `## Identity` section gets an `entity_id`
- Idempotent — running twice doesn't duplicate IDs
- `--dry-run` shows changes without modifying files

### Estimated Effort: 2-3 hours

---

## Phase 1b: Assign Resource UUIDs

**Agent**: Script Agent
**Input**: All knowledge docs, rules, protocols, skills, and output files in `.0agnostic/` and `outputs/` directories
**Output**: `assign-resource-uuids.sh` script at `.0agnostic/`

### Task

Write a script that:
1. Finds all `.md` files in `.0agnostic/01_knowledge/`, `.0agnostic/02_rules/`, `.0agnostic/03_protocols/`
2. Finds all `.md` files in `outputs/` directories within stages (`stage_*_*/outputs/`)
3. Skips: `README.md`, `0INDEX.md`, `index.md`, auto-generated files (`CLAUDE.md`, `.integration.md`), `.1merge/` files, `stage_index.json`, `.gab.jsonld`
4. For each, checks if `resource_id:` exists in YAML frontmatter
5. If missing:
   a. If file has no YAML frontmatter (`---`), adds one
   b. Generates UUID v4
   c. Determines `resource_type` from path (`01_knowledge/` → "knowledge", `02_rules/` → "rule", `outputs/` → "output", etc.)
   d. Inserts frontmatter with `resource_id`, `resource_type`, `resource_name`
6. Also finds `SKILL.md` files and adds `resource_id` to their frontmatter
7. Supports `--dry-run`

### Acceptance Criteria
- All knowledge docs, rules, protocols, skills, and output files get `resource_id`
- YAML frontmatter is valid after insertion
- Idempotent
- Skips files that shouldn't have IDs (auto-generated files, indexes, registries, JSON-LD)

### Estimated Effort: 4-5 hours

### Can Run Parallel With: Phase 1

---

## Phase 2: Create Stage Registries

**Agent**: Script Agent
**Input**: All `stage_N_00_stage_registry/` directories, stage `0AGNOSTIC.md` files
**Output**: `create-stage-indexes.sh` script at `.0agnostic/`

### Task

Write a script that:
1. Finds all `layer_N_99_stages/` directories
2. For each, finds the `stage_N_00_stage_registry/` directory
3. Lists all `stage_N_XX_*` sibling directories
4. For each stage:
   a. If the stage has `0AGNOSTIC.md`, check for `stage_id:`
   b. If missing, generate UUID v4 and insert into stage's `0AGNOSTIC.md`
   c. If stage has no `0AGNOSTIC.md`, generate UUID for registry only
5. Creates/updates `stage_index.json` in `stage_N_00_stage_registry/` with all stage UUIDs
6. Supports `--dry-run`

### Registry Format
```json
{
  "entity_id": "from-parent-0AGNOSTIC.md",
  "entity_name": "entity_directory_name",
  "stages": [
    {
      "stage_id": "uuid",
      "stage_number": "00",
      "stage_name": "stage_registry",
      "directory": "stage_3_00_stage_registry"
    }
  ]
}
```

### Acceptance Criteria
- Every entity with stages gets a `stage_index.json`
- Every stage gets a UUID (in 0AGNOSTIC.md if it exists, always in registry)
- Entity UUID in registry matches the entity's `0AGNOSTIC.md` entity_id
- Idempotent

### Estimated Effort: 4-5 hours
### Depends On: Phase 1 (needs entity_id to populate registry)

---

## Phase 3: Update pointer-sync.sh for UUID Resolution

**Agent**: Pointer-Sync Agent
**Input**: Current `pointer-sync.sh` (253 lines), design doc Section 4
**Output**: Modified `pointer-sync.sh` at `.0agnostic/pointer-sync.sh`

### Task

Modify pointer-sync.sh to:

1. **Add new field extraction**: `canonical_entity_id`, `canonical_stage_id`, `canonical_resource_id`

2. **UUID-first entity resolution**:
   ```
   if canonical_entity_id is present:
     search .uuid-index.json for UUID → path
     if not in index: scan all 0AGNOSTIC.md files for entity_id match
     if found: use as entity directory
     if not found: BROKEN
   else (legacy):
     use current find -type d -name logic
     emit deprecation warning
   ```

3. **UUID-first stage resolution**:
   ```
   if canonical_stage_id is present:
     read stage_index.json in entity's stage_N_00_stage_registry/
     look up stage_id → directory name
     if found: use as stage directory
   else (legacy):
     use current find within entity logic
     emit deprecation warning
   ```

4. **Resource ID resolution** (new):
   ```
   if canonical_resource_id is present:
     search resource_index.json files for UUID → path
     if found: use as full canonical path (skip entity/stage resolution)
   ```

5. **Add `--rebuild-index` flag**: Scans all 0AGNOSTIC.md files, builds `.uuid-index.json`

6. **Index auto-rebuild**: If UUID not found in index, rebuild index once and retry

### Acceptance Criteria
- All 108 existing tests still pass (backward compat)
- UUID-based pointers resolve correctly
- Name-based pointers still work with deprecation warning
- `--rebuild-index` builds valid index
- Index miss triggers auto-rebuild

### Estimated Effort: 6-8 hours
### Depends On: Phase 1, Phase 2 (needs UUIDs to exist for testing)

---

## Phase 4: Update Entity Creation Skill

**Agent**: Skill Agent
**Input**: Current `/entity-creation` SKILL.md, entity_structure.md
**Output**: Modified skill files

### Task

Update the entity-creation skill to:

1. **Auto-generate entity_id**: When creating `0AGNOSTIC.md`, include `entity_id: "uuid"` in Identity section
2. **Auto-generate stage_ids**: When creating all 12 stages, generate UUIDs for each
3. **Create stage_index.json**: In `stage_N_00_stage_registry/` with all stage UUIDs
4. **Insert stage_id in stage 0AGNOSTIC.md**: If the skill creates stage-level `0AGNOSTIC.md` files

### Acceptance Criteria
- New entities created via skill have `entity_id` in `0AGNOSTIC.md`
- New entities have `stage_index.json` with all 12 stage UUIDs
- Stage `0AGNOSTIC.md` files (if created) have `stage_id`

### Estimated Effort: 3-4 hours
### Can Run Parallel With: Phase 3

---

## Phase 5: Migrate Existing Pointers

**Agent**: Script Agent
**Input**: All pointer files, UUID index
**Output**: `migrate-pointers.sh` script at `.0agnostic/`

### Task

Write a script that:
1. Finds all pointer files (YAML frontmatter with `pointer_to:`)
2. For each pointer with `canonical_entity:` but no `canonical_entity_id:`:
   a. Look up entity name in `.uuid-index.json` or scan 0AGNOSTIC.md files
   b. Add `canonical_entity_id:` field
   c. Rename `canonical_entity:` to `canonical_entity_name:` (display only)
3. For each pointer with `canonical_stage:` but no `canonical_stage_id:`:
   a. Look up stage name in the entity's `stage_index.json`
   b. Add `canonical_stage_id:` field
   c. Rename `canonical_stage:` to `canonical_stage_name:` (display only)
4. Supports `--dry-run`

### Acceptance Criteria
- All existing pointer files get UUID fields added
- Old name fields are kept as display-only (renamed to `_name` suffix)
- `pointer-sync.sh --validate` passes after migration
- `--dry-run` shows changes without modifying

### Estimated Effort: 3-4 hours
### Depends On: Phase 1, 2, 3 (needs UUIDs and updated pointer-sync.sh)

---

## Phase 6: Update Documentation

**Agent**: Docs Agent
**Input**: entity_structure.md, pointer_sync_protocol.md, pointer_file_convention.md
**Output**: Updated docs

### Task

Update these canonical documents:

1. **entity_structure.md** — Add `entity_id` as required field in `0AGNOSTIC.md`, document `stage_index.json` format, document `resource_id` frontmatter
2. **pointer_sync_protocol.md** — Add UUID resolution steps, document `--rebuild-index`, update pointer format spec
3. **pointer_file_convention.md** — Add `canonical_entity_id`, `canonical_stage_id`, `canonical_resource_id` fields
4. **pointer_sync_knowledge.md** — Add UUID identity system to architecture overview

### Acceptance Criteria
- All docs reflect new UUID fields
- New pointer format is documented with examples
- Migration guide included

### Estimated Effort: 2-3 hours
### Depends On: Phase 3 (needs final pointer-sync.sh behavior)

---

## Phase 7: Full Integration Test

**Agent**: Test Agent
**Input**: Test design from `stage_3_07_testing/outputs/uuid_test_design.md`
**Output**: Updated `test_pointer_sync.sh` + new `test_uuid_system.sh`

### Task

1. Extend `test_pointer_sync.sh` with UUID-specific test categories (see test design doc)
2. Create `test_uuid_system.sh` for migration script testing
3. Run full test suite
4. Iterate: fix failures, re-run until 0 FAIL

### Acceptance Criteria
- All existing 108 tests still pass
- All new UUID tests pass
- Migration scripts tested end-to-end
- Index rebuild tested

### Estimated Effort: 4-6 hours
### Depends On: Phase 1-5 (needs everything implemented to test)

---

## Phase 8: Final Sync

**Agent**: Coordinator
**Input**: All modified files
**Output**: Regenerated tool files, committed repo

### Task

1. Run `agnostic-sync.sh` at repo root — regenerates all CLAUDE.md files (now with `entity_id`)
2. Run `pointer-sync.sh --rebuild-index` — builds initial UUID index
3. Run `pointer-sync.sh --validate` — verify all pointers resolve
4. Commit all changes with `[AI Context]` prefix
5. Push to remote

### Acceptance Criteria
- All CLAUDE.md files include `entity_id` from their `0AGNOSTIC.md`
- `.uuid-index.json` exists and is valid
- `pointer-sync.sh --validate` exits 0
- All changes committed and pushed

### Estimated Effort: 1-2 hours

---

## Execution Timeline

```
Session 1 (Scripts):
  [Coordinator] Review plan → delegate
  [Script Agent] Phase 1: assign-entity-uuids.sh     (2-3h)
  [Script Agent] Phase 1b: assign-resource-uuids.sh   (3-4h, parallel)
  [Script Agent] Phase 2: create-stage-indexes.sh   (4-5h, after Phase 1)
  [Test Agent] Verify Phase 1-2 outputs

Session 2 (Core Changes):
  [Pointer-Sync Agent] Phase 3: Update pointer-sync.sh  (6-8h)
  [Skill Agent] Phase 4: Update entity-creation skill   (3-4h, parallel)
  [Test Agent] Run existing tests + new UUID tests

Session 3 (Migration + Polish):
  [Script Agent] Phase 5: migrate-pointers.sh           (3-4h)
  [Docs Agent] Phase 6: Update documentation             (2-3h, parallel)
  [Test Agent] Phase 7: Full integration test            (4-6h)
  [Coordinator] Phase 8: Final sync + commit             (1-2h)
```

**Total estimated effort**: ~30-40 hours across 3 sessions

---

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Migration breaks existing pointers | High | `--dry-run` on all scripts, run `--validate` after each phase |
| UUID index becomes stale | Medium | Auto-rebuild on index miss, `--rebuild-index` flag |
| Entity creation skill regressions | Medium | Test new entities with skill after changes |
| Long paths cause ENAMETOOLONG | Low | Work directly (no subagents for deep paths), use git -C |
| Partial migration (some pointers migrated, some not) | Low | Name-based fallback ensures backward compat |

---

## Verification Checklist

After all phases complete:

- [ ] Every `0AGNOSTIC.md` with Identity section has `entity_id`
- [ ] Every stage's `0AGNOSTIC.md` has `stage_id`
- [ ] Every entity with stages has `stage_index.json`
- [ ] All knowledge docs, rules, protocols, output files have `resource_id` frontmatter
- [ ] `pointer-sync.sh` resolves by UUID-first, name fallback
- [ ] All 108 existing tests pass
- [ ] All new UUID tests pass
- [ ] `pointer-sync.sh --validate` exits 0 on real repo
- [ ] Entity creation skill generates UUIDs for new entities
- [ ] Documentation updated (entity_structure.md, protocol, convention)
- [ ] All changes committed with `[AI Context]` prefix
