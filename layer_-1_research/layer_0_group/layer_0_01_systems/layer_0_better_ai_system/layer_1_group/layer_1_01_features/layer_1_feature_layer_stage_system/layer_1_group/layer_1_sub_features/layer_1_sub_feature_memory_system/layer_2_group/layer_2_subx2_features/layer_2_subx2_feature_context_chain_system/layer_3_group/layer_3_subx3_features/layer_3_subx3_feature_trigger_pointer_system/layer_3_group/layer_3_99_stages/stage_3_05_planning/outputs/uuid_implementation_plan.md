---
resource_id: "6baf4700-3026-43e9-ae26-72b11d9c8b31"
resource_type: "output"
resource_name: "uuid_implementation_plan"
---
# UUID Identity System — Implementation Plan

<!-- section_id: "ab79cddc-01a6-4f2f-984b-4201f8569c65" -->
## Date: 2026-03-02
<!-- section_id: "74afa248-ad19-4c98-a6dc-ffaeabeaf692" -->
## Design Reference: `../../stage_3_04_design/outputs/uuid_identity_system_design.md`
<!-- section_id: "9e65ccdf-71ff-45e9-8aa5-d5902d6229ee" -->
## Test Design: `../../stage_3_07_testing/outputs/uuid_test_design.md`

---

<!-- section_id: "b4b9c0b6-1b6b-44d7-87aa-e744ed5d86da" -->
## Overview

This plan breaks the UUID identity system implementation into **14 phases** across **6 agent roles**, plus **4 additional phases** (11-14) added after the initial implementation for graph traversal, query capabilities, and skill context avenue delivery, plus **Phase 15** for lightweight entity lookup, **Phase 16** for script protocol migration, and **Phases 17-24** for the UUID resolution system — making UUID the primary reference mechanism so paths become derived artifacts resolved at runtime. Each phase produces testable artifacts. Phases are ordered by dependency — later phases depend on earlier ones. Some phases can run in parallel.

<!-- section_id: "f1a2b3c4-d5e6-4f7a-8b9c-0d1e2f3a4b5c" -->
## Implementation Status (2026-03-07)

| Phase | Status | Notes |
|-------|--------|-------|
| 1 (entity UUIDs) | COMPLETE | All entities have entity_id in 0AGNOSTIC.md |
| 1b (file UUIDs) | COMPLETE | 17,340 core text files have resource_id/file_id |
| 1c (directory UUIDs) | COMPLETE | ~99,275 directories have .dir-id files |
| 1d (section UUIDs) | COMPLETE | h2/h3 headings have section_id comments |
| 1e (submodule UUIDs) | COMPLETE | 17 nested repos have file + section UUIDs |
| 2 (stage indexes) | COMPLETE | stage_index.json in all stage registries |
| 3 (pointer-sync.sh UUID resolution) | COMPLETE | UUID-first resolution with name fallback |
| 3b (reference integrity) | COMPLETE | --find-references, --validate, --detect-cycles, --gc all implemented |
| 4 (entity-creation skill) | COMPLETE | Canonical + Claude port updated with UUID generation steps |
| 5 (migrate pointers) | COMPLETE | All 4 real pointer files already have canonical_entity_id + canonical_stage_id |
| 6 (docs update) | COMPLETE | All 4 docs have UUID fields, format, resolution, examples |
| 7 (integration test) | COMPLETE | 160 tests pass (29 categories), 0 FAIL — includes UUID resolution, graph, query, dir-index |
| 8 (final sync) | COMPLETE | agnostic-sync.sh run, index rebuilt |
| 9 (git hooks) | COMPLETE | Pre-commit + post-merge hooks installed and symlinked |
| 10 (dir UUID index) | COMPLETE | --rebuild-dir-index implemented, 100,520 dirs indexed, post-merge hook, .gitignore |
| **11 (parent/children graph)** | **COMPLETE** | **Added 2026-03-06** |
| **12 (query CLI)** | **COMPLETE** | **Added 2026-03-06** |
| **13 (bulk resource indexes)** | **COMPLETE** | **Added 2026-03-06** |
| **14 (UUID query skill avenue)** | **COMPLETE** | **Added 2026-03-06, implemented 2026-03-07** |
| **15 (entity-find.sh lightweight lookup)** | **COMPLETE** | **Added 2026-03-07** — `.entity-lookup.tsv` + `entity-find.sh`, design at `stage_3_04_design/outputs/entity_find_design.md` |
| **16 (script protocol migration)** | **COMPLETE** | **Added 2026-03-07** — All 12 scripts moved from `.0agnostic/` root into `03_protocols/{protocol}/tools/`, 81+ files updated, design at `stage_3_04_design/outputs/script_protocol_migration_design.md` |
| **17 (resolve-uuid function)** | **COMPLETE** | **Added 2026-03-07** — `resolve-uuid.sh` at `pointer_sync_protocol/tools/`, Python3-based JSON lookup, error-safe pattern |
| **18 (scripts use resolve-uuid)** | **COMPLETE** | **Added 2026-03-07** — agnostic-sync.sh, post-merge, post-checkout use UUID-based script discovery with fallback |
| **19 ({{resolve:UUID}} placeholder syntax)** | **COMPLETE** | **Added 2026-03-07** — Root 0AGNOSTIC.md uses `{{resolve:UUID}}` for script paths in code blocks, triggers, resources |
| **20 (agnostic-sync.sh UUID integration)** | **COMPLETE** | **Added 2026-03-07** — Placeholder resolution step added, resolves all `{{resolve:UUID}}` before generation |
| **21 (git hooks: auto-rebuild + UUID validation)** | **COMPLETE** | **Added 2026-03-07** — post-checkout rebuilds index on branch switch, pre-commit validates UUID refs in staged files |
| **22 (UUID short-form prefix matching)** | **COMPLETE** | **Added 2026-03-07** — Built into resolve-uuid, 8-char prefix (16^8 = 4.3B combinations vs 5.3K entries) |
| **23 (logical names: resolve-name)** | **COMPLETE** | **Added 2026-03-07** — `.uuid-aliases.tsv` with 13 script aliases, `resolve-name` function in resolve-uuid.sh |
| **24 (end-to-end validation)** | **COMPLETE** | **Added 2026-03-07** — All 13 scripts resolve by name/UUID/prefix, hooks work, agnostic-sync resolves placeholders |

---

<!-- section_id: "63ca82ff-3bbd-4bef-8f75-9d1862ebfc5d" -->
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

<!-- section_id: "7c0e0c2a-ba8a-4d6d-bb4a-f8fca3fb9163" -->
## Phase Dependency Graph

```
Phase 1 (entity UUIDs) ─────┬──> Phase 3 (pointer-sync.sh update)
                              │
Phase 2 (stage indexes) ─────┤──> Phase 5 (migrate pointers)
                              │
Phase 1b (all file UUIDs) ───┘

Phase 1c (directory UUIDs) — independent, can run parallel with 1b

Phase 1d (section UUIDs) — after Phase 1b (needs file UUIDs to exist)

Phase 1e (submodule/nested repo UUIDs) — after Phase 1b, 1d (reuses same scripts)

Phase 3b (reference integrity) — after Phase 3

Phase 4 (entity-creation skill) — independent, can run parallel with 3

Phase 6 (docs update) — after phases 1-5, 1c, 1e

Phase 7 (full integration test) — after all phases

Phase 8 (run agnostic-sync.sh) — final

Phase 9 (git hooks + validation) — after Phase 8

Phase 10 (directory UUID index + lazy resolution) — after Phase 1c

Phase 14 (UUID query skill context avenue) — after Phase 12, 13

Phase 16 (script protocol migration) — after Phase 15 (uses entity-find.sh)

--- UUID Resolution System (Phases 17-24) ---

Phase 17 (resolve-uuid function) — after Phase 13 (needs .uuid-index.json), Phase 16 (scripts organized)
                                  ├──> Phase 18 (scripts use resolve-uuid)
                                  ├──> Phase 19 (placeholder syntax)
                                  ├──> Phase 21 (git hooks UUID validation)
                                  ├──> Phase 22 (UUID short-form)
                                  └──> Phase 23 (logical names)

Phase 18 (scripts use resolve-uuid) — after Phase 17

Phase 19 ({{resolve:UUID}} syntax) — after Phase 17
  └──> Phase 20 (agnostic-sync.sh UUID integration)

Phase 20 (agnostic-sync.sh UUID integration) — after Phase 19

Phase 21 (git hooks: auto-rebuild + UUID validation) — after Phase 17, Phase 18

Phase 22 (UUID short-form prefix matching) — after Phase 17, can run parallel with 18-21

Phase 23 (logical names: resolve-name) — after Phase 17, can run parallel with 18-22

Phase 24 (end-to-end validation) — after Phases 17-23 (all must be complete)
```

---

<!-- section_id: "2e4c1dae-1700-4adf-98dc-0467082614d1" -->
## Phase 1: Assign Entity UUIDs

**Agent**: Script Agent
**Input**: All `0AGNOSTIC.md` files in the repo
**Output**: `assign-entity-uuids.sh` script at `.0agnostic/`

<!-- section_id: "0b077d8b-9e46-498f-9425-f593b72745db" -->
### Task

Write a script that:
1. Finds all `0AGNOSTIC.md` files under `0_layer_universal/`
2. For each, checks if `entity_id:` already exists in the Identity section
3. If missing, generates UUID v4 via `uuidgen`
4. Inserts `entity_id: "uuid"` on the line after `## Identity`
5. Reports: `Added entity_id <uuid> to <path>`
6. Supports `--dry-run` (show what would change)

<!-- section_id: "61f8b229-4e46-4a71-aac1-e93833b50a65" -->
### Acceptance Criteria
- Every `0AGNOSTIC.md` with an `## Identity` section gets an `entity_id`
- Idempotent — running twice doesn't duplicate IDs
- `--dry-run` shows changes without modifying files

<!-- section_id: "a8677c91-9f7c-46c9-aac5-bee97df2fc7e" -->
### Estimated Effort: 2-3 hours

---

<!-- section_id: "e2742f52-abcf-49da-a842-dd2bfb6bcedb" -->
## Phase 1b: Assign Universal File UUIDs

**Agent**: Script Agent
**Input**: ALL files in the AI system — every file type, every directory, every subdirectory under `0_layer_universal/`
**Output**: `assign-file-uuids.sh` script at `.0agnostic/`

**Fundamental rule**: Every file that has `0_layer_universal/` as an ancestor in its path MUST have a UUID. No file type exceptions — only binary files and empty `.gitkeep` placeholders are exempt.

<!-- section_id: "a71f92a1-395d-4930-8953-3fb199516e07" -->
### Task

Write a script that assigns UUIDs to **every file** in the system, using the appropriate comment syntax per file type:

1. **`.md`/`.qmd` files** — `resource_id` in YAML frontmatter
2. **`# comment` files** (`.sh`, `.py`, `.yaml`, `.yml`, `.txt`, `.ini`, `.rules`, `.env`, `.gitignore`, `.csv`, `.template`, `.jq`, `.dot`, `.Rproj`, `.replit`) — `# resource_id:` header
3. **`// comment` files** (`.js`, `.mjs`, `.jsx`, `.cjs`, `.jsonc`, `.jsonl`) — `// resource_id:` header
4. **`/* */` comment files** (`.css`) — `/* resource_id: */` header
5. **`<!-- -->` comment files** (`.html`, `.svg`, `.mermaid`) — `<!-- resource_id: -->` header
6. **`.ps1` files** — `# resource_id:` header
7. **`.json`/`.jsonld` files** — `"file_id"` in JSON root object
8. **Auto-generated files** (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `OPENAI.md`, `.integration.md`, `.cursorrules`, `copilot-instructions.md`) — `derived_from` referencing source entity_id
9. **Extensionless text files** — `# resource_id:` header as default
10. **Binary files** (`.png`, `.woff`, `.wav`, `.db`, `.pdf`, `.pid`) — EXEMPT (cannot embed text)
11. **Empty `.gitkeep` files** — EXEMPT (0 bytes)

<!-- section_id: "12f4bfef-b037-4501-8b7e-528384640554" -->
### Acceptance Criteria
- Every non-binary, non-empty file has `resource_id` or `file_id` or `derived_from`
- Coverage: 17,340/17,340 core text files = 100% (submodules covered in Phase 1e)
- YAML/JSON remains valid after insertion
- Idempotent — running twice doesn't duplicate IDs
- `--dry-run` shows changes without modifying
- Firebase service account JSON files are excluded from UUID insertion (GitHub push protection blocks credential file changes)

<!-- section_id: "dde30f06-2b95-4dc5-9d27-2d90b8b49f66" -->
### Estimated Effort: 6-8 hours

<!-- section_id: "d556fca0-510e-4a69-9621-65d5a791d912" -->
### Can Run Parallel With: Phase 1

---

<!-- section_id: "54d0d3bc-9c38-44bc-825b-c3559c7cb687" -->
## Phase 1c: Assign Directory UUIDs

**Agent**: Script Agent
**Input**: ALL directories under `0_layer_universal/`
**Output**: `assign-dir-uuids.sh` script at `.0agnostic/`

**Fundamental rule**: Every directory within `0_layer_universal/` MUST have a UUID via a `.dir-id` file. This replaces empty `.gitkeep` files and ensures every directory has stable identity.

<!-- section_id: "e791bbad-0ffc-436f-85e5-8cf0f2be4a3e" -->
### Task

Write a script that:
1. Finds all directories under `0_layer_universal/`
2. For each directory, checks if `.dir-id` already exists
3. If missing, generates UUID v4 and creates `.dir-id` containing only the UUID (single line, no metadata)
4. If directory has an empty `.gitkeep`, removes it (`.dir-id` replaces its git-tracking purpose)
5. Reports: `Added .dir-id <uuid> to <path>`
6. Supports `--dry-run` (show what would change)

<!-- section_id: "a97e0650-618f-41ef-8c6a-b30a1bce9619" -->
### `.dir-id` File Format

```
a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d
```

Single line. No comments, no YAML, no metadata. Maximum simplicity.

<!-- section_id: "d25f9a5d-0a54-422f-a266-2af23d40cb91" -->
### `.gitkeep` Replacement Rules

| Scenario | Action |
|----------|--------|
| Directory has empty `.gitkeep` only | Remove `.gitkeep`, create `.dir-id` |
| Directory has `.gitkeep` with content | Keep `.gitkeep` (it has data), also create `.dir-id` |
| Directory has files but no `.dir-id` | Create `.dir-id` |
| Directory already has `.dir-id` | Skip (idempotent) |

<!-- section_id: "3667abd8-778c-4d0f-a06c-0b42c7ef6740" -->
### Acceptance Criteria
- Every directory under `0_layer_universal/` has a `.dir-id` file
- All empty `.gitkeep` files are replaced by `.dir-id`
- `.gitkeep` files with content are preserved
- Idempotent — running twice doesn't create duplicate `.dir-id` files
- `--dry-run` shows changes without modifying
- Coverage target: ~99,275 directories = 100%

<!-- section_id: "48e2c232-b8e9-44cb-8115-b297fca66551" -->
### Estimated Effort: 4-6 hours
<!-- section_id: "534d737f-ab6d-43d5-9d1f-58a4c133379d" -->
### Can Run Parallel With: Phase 1, Phase 1b

---

<!-- section_id: "45cc5b7e-2aa8-46b0-8d0c-5daf4cce2659" -->
## Phase 1d: Assign Section-Level UUIDs

**Agent**: Script Agent
**Input**: ALL `.md` files under `0_layer_universal/` (excluding auto-generated files)
**Output**: `assign-section-uuids.sh` script at `.0agnostic/`

<!-- section_id: "d7dda006-08f0-4a26-b62a-10105407c7a3" -->
### Task

Write a script that assigns UUIDs to every `##` (h2) and `###` (h3) heading in markdown files:

1. Finds all `.md` files under `0_layer_universal/`
2. Skips auto-generated files (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `OPENAI.md`, `.integration.md`, `.cursorrules`, `copilot-instructions.md`)
3. For each file, scans for lines matching `^## ` or `^### `
4. If the line above is already `<!-- section_id: "..." -->`, skip (idempotent)
5. If no section_id exists, generates UUID v4 and inserts `<!-- section_id: "uuid" -->` on the line above the heading
6. Reports per-file counts
7. Supports `--dry-run`

<!-- section_id: "df820637-7d7d-433a-b9c7-b164b4d8c1e5" -->
### Section ID Format

```markdown
## Section Heading
```

<!-- section_id: "71948a1b-e140-426f-9e6f-7efc99e3554c" -->
### Heading Levels

| Level | Gets UUID | Rationale |
|-------|-----------|-----------|
| `#` (h1) | No | File title — covered by file-level `resource_id` |
| `##` (h2) | Yes | Primary structural divisions |
| `###` (h3) | Yes | Sub-sections frequently referenced |
| `####`+ | No | Too granular |

<!-- section_id: "e0a1fbd6-ec06-48d1-8657-91434d29174b" -->
### Exclusions

- Auto-generated files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .integration.md, .cursorrules, copilot-instructions.md)
- Files in `node_modules/`, `venv/`, `.venv/`, `__pycache__/`
- Binary/non-text files

<!-- section_id: "e6129d95-8fe2-4e1a-8aa2-e5a7c130eeb0" -->
### Acceptance Criteria
- Every h2 and h3 heading in non-auto-generated `.md` files has a `<!-- section_id: "uuid" -->` comment above it
- Auto-generated files are untouched
- Idempotent — running twice doesn't duplicate IDs
- `--dry-run` shows changes without modifying
- Valid markdown after insertion (heading still renders correctly)

<!-- section_id: "20d82775-02fd-4c46-ba73-74cb47068332" -->
### Estimated Effort: 4-6 hours
<!-- section_id: "9e3f24a1-f91b-4881-84d2-d75529e85fe2" -->
### Depends On: Phase 1b (file UUIDs should exist first)

---

<!-- section_id: "c4e91b3a-7f2d-4e8c-a1d5-9b3f6e8c2d7a" -->
## Phase 1e: Assign UUIDs to Submodule & Nested Repo Content

**Agent**: Script Agent
**Input**: All 17 nested repos/submodules under `0_layer_universal/`
**Output**: File UUIDs and section UUIDs assigned inside each nested repo

**Fundamental rule**: The UUID requirement extends to ALL content under `0_layer_universal/`, including files inside git submodules and unregistered nested git repos. Directory UUIDs (`.dir-id`) are already 100% complete across all nested repos from Phase 1c.

<!-- section_id: "d8f42e1c-3a9b-4c6d-b5e7-1f8a2d4c6e9b" -->
### Nested Repo Inventory

| Repo | Type | Approx Files | Dir UUIDs | File UUIDs | Section UUIDs |
|------|------|-------------|-----------|------------|---------------|
| layer_1_project_school | Submodule | ~23,731 | 100% | 0% | 78% |
| layer_1_project_physics_simulation | Submodule | ~713 | 100% | 0% | 7% |
| layer_1_project_portfolio | Submodule | ~36 | 100% | 0% | 38% |
| layer_1_project_parallelism | Submodule | ~21 | 100% | 0% | 36% |
| layer_1_project_ds250_course | Submodule | ~19 | 100% | 0% | 0% |
| layer_1_project_buying_list | Submodule | ~9 | 100% | 0% | 27% |
| layer_1_project_life_administration | Submodule | ~9 | 100% | 0% | 100% |
| layer_1_component_setup_hub | Submodule | ~15 | 100% | 0% | 42% |
| layer_1_component_dotfiles | Submodule | ~30 | 100% | 0% | 0% |
| layer_1_project_lang_trak | Nested | ~3,741 | 100% | 0% | 75% |
| layer_1_project_central_website | Nested | ~10 | 100% | 0% | 33% |
| layer_1_project_internship_prep | Nested | ~27 | 100% | 0% | 69% |
| layer_1_project_language_tracker | Nested | ~57 | 100% | 0% | 15% |
| layer_1_project_machine_learning | Nested | ~84 | 100% | 0% | 0% |
| layer_1_project_web_app | Nested | ~20 | 100% | 0% | 0% |
| langtrak_original | Nested | ~461 | 100% | 97% | 88% |
| professor | Nested | ~42 | 100% | 0% | 95% |

<!-- section_id: "a2b7c5d9-4e1f-3c8a-b6d4-7f9e1a3c5d8b" -->
### Task

For each of the 17 nested repos:

1. **File UUIDs**: Run the same file UUID assignment logic from Phase 1b:
   - Use appropriate comment syntax per file type
   - Skip binary files and empty `.gitkeep` files
   - Skip files that already have UUIDs (idempotent)
   - Skip Firebase service account JSON files (GitHub push protection)
2. **Section UUIDs**: Run the same section UUID assignment logic from Phase 1d:
   - Add `<!-- section_id: "uuid" -->` above every h2/h3 heading in `.md` files
   - Skip auto-generated files (CLAUDE.md, AGENTS.md, etc.)
   - Skip headings that already have section_id
3. **Commit inside each repo**: Use `[AI Context]` prefix
4. **Push each repo** if it has a remote
5. **Update parent submodule pointers**: After all nested repos are processed, commit updated gitlinks in `0_layer_universal`

<!-- section_id: "e5c8d2f4-1a3b-4d6e-9c7f-2b5a8d0e3f6c" -->
### Commit Strategy

```
For each nested repo (deepest first):
  1. cd into nested repo
  2. git add [modified files]
  3. git commit -m "[AI Context] Assign file + section UUIDs for full coverage"
  4. git push (if remote exists)

Then in parent 0_layer_universal:
  5. git add [submodule paths]
  6. git commit -m "[AI Context] Update submodule pointers after UUID assignment"
  7. git push
```

<!-- section_id: "f7a9b1c3-2d4e-5f6a-8b7c-9d0e1f2a3b4c" -->
### Edge Cases

| Scenario | Handling |
|----------|----------|
| Gitignored files (e.g., `.env`) | Skip — not tracked, no UUID needed |
| Repos without remotes | Commit locally only, no push |
| Binary-heavy repos (physics_simulation) | Skip binaries, only process text files |
| Deeply nested submodules (school has nested repos inside) | Process recursively, commit bottom-up |
| Files with `\r` in path | Skip — pre-existing path corruption issue |

<!-- section_id: "a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d" -->
### Acceptance Criteria
- All ~29,000 text files across 17 nested repos have file UUIDs
- All h2/h3 headings in `.md` files across nested repos have section UUIDs
- Directory UUIDs remain at 100% (no regression)
- Each nested repo has its own commit with `[AI Context]` prefix
- Parent `0_layer_universal` has updated submodule pointers committed
- No binary files modified
- No Firebase service account files modified

<!-- section_id: "b3c4d5e6-7f8a-9b0c-1d2e-3f4a5b6c7d8e" -->
### Estimated Effort: 8-12 hours (largest phase — 17 repos, ~29,000 files)
<!-- section_id: "c5d6e7f8-9a0b-1c2d-3e4f-5a6b7c8d9e0f" -->
### Depends On: Phase 1b (file UUID scripts), Phase 1d (section UUID scripts)

---

<!-- section_id: "159c43a8-82c2-452d-8888-e4dcbd91e1e8" -->
## Phase 2: Create Stage Registries

**Agent**: Script Agent
**Input**: All `stage_N_00_stage_registry/` directories, stage `0AGNOSTIC.md` files
**Output**: `create-stage-indexes.sh` script at `.0agnostic/`

<!-- section_id: "5d238f69-fc1c-42b0-b3ff-c054a7a74aea" -->
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

<!-- section_id: "b6297f77-011d-4307-b353-fe61db9c4824" -->
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

<!-- section_id: "1e92d65d-d469-4617-bb5a-bc11c9e464d8" -->
### Acceptance Criteria
- Every entity with stages gets a `stage_index.json`
- Every stage gets a UUID (in 0AGNOSTIC.md if it exists, always in registry)
- Entity UUID in registry matches the entity's `0AGNOSTIC.md` entity_id
- Idempotent

<!-- section_id: "bdb37fd1-d628-4360-9b72-1585ab27a1af" -->
### Estimated Effort: 4-5 hours
<!-- section_id: "87f45142-c9d9-44d0-a028-0d26aa15b46d" -->
### Depends On: Phase 1 (needs entity_id to populate registry)

---

<!-- section_id: "c6963199-bac8-457a-960f-abdfa87aad9e" -->
## Phase 3: Update pointer-sync.sh for UUID Resolution

**Agent**: Pointer-Sync Agent
**Input**: Current `pointer-sync.sh` (253 lines), design doc Section 4
**Output**: Modified `pointer-sync.sh` at `.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh`

<!-- section_id: "76279962-632d-4017-a481-52a26e53f0eb" -->
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

<!-- section_id: "59d6e1a6-1495-44f4-b5fe-a51ceaff80f7" -->
### Acceptance Criteria
- All 108 existing tests still pass (backward compat)
- UUID-based pointers resolve correctly
- Name-based pointers still work with deprecation warning
- `--rebuild-index` builds valid index
- Index miss triggers auto-rebuild

<!-- section_id: "909de9fd-584c-4c2d-b279-95ad725ee1fe" -->
### Estimated Effort: 6-8 hours
<!-- section_id: "70b5fdba-bf92-4906-bcc9-04fed97ba721" -->
### Depends On: Phase 1, Phase 2 (needs UUIDs to exist for testing)

---

<!-- section_id: "e57bb209-6753-4f58-a296-3858f3c1bfe7" -->
## Phase 4: Update Entity Creation Skill

**Agent**: Skill Agent
**Input**: Current `/entity-creation` SKILL.md, entity_structure.md
**Output**: Modified skill files

<!-- section_id: "9283c570-b66b-4749-8b6e-30a1371d1e2f" -->
### Task

Update the entity-creation skill to:

1. **Auto-generate entity_id**: When creating `0AGNOSTIC.md`, include `entity_id: "uuid"` in Identity section
2. **Auto-generate stage_ids**: When creating all 12 stages, generate UUIDs for each
3. **Create stage_index.json**: In `stage_N_00_stage_registry/` with all stage UUIDs
4. **Insert stage_id in stage 0AGNOSTIC.md**: If the skill creates stage-level `0AGNOSTIC.md` files

<!-- section_id: "4e2206f5-8550-40a5-8d93-764f4b536b63" -->
### Acceptance Criteria
- New entities created via skill have `entity_id` in `0AGNOSTIC.md`
- New entities have `stage_index.json` with all 12 stage UUIDs
- Stage `0AGNOSTIC.md` files (if created) have `stage_id`

<!-- section_id: "fc129451-2afd-4e40-b187-fa502b8cf203" -->
### Estimated Effort: 3-4 hours
<!-- section_id: "5cc79aa4-e96b-42b8-aa01-c9556fa32d56" -->
### Can Run Parallel With: Phase 3

---

<!-- section_id: "09139850-7d57-4ddd-bc49-52ac9991c36b" -->
## Phase 3b: Reference Integrity Tools

**Agent**: Pointer-Sync Agent
**Input**: Updated `pointer-sync.sh` from Phase 3
**Output**: New flags added to `pointer-sync.sh`

<!-- section_id: "6ec15571-b6c3-4eda-b501-0a7cff167eb6" -->
### Task

Add reference integrity features to pointer-sync.sh:

1. **`--find-references <uuid>`**: Find all pointer files that reference a given UUID (reverse lookup)
2. **`--detect-cycles`**: Build directed graph from all pointer files, report any cycles
3. **`--gc`**: Garbage collection — scan index, remove entries whose paths don't exist
4. **Atomic write protocol**: All index writes use temp → fsync → atomic rename
5. **File locking**: `mkdir`-based lock around index mutations (5-minute stale lock timeout)
6. **Checksum validation**: On index load, compute SHA256 and compare to stored checksum. Mismatch → auto-rebuild
7. **Duplicate UUID detection**: During `--rebuild-index`, report any duplicate UUIDs

<!-- section_id: "c9d318ab-31f2-485c-a746-191f0682a8e6" -->
### Acceptance Criteria
- `--find-references` returns all pointers referencing a given UUID
- `--detect-cycles` correctly identifies circular reference chains
- `--gc` removes orphaned index entries without affecting valid ones
- Concurrent `--rebuild-index` from two processes doesn't corrupt the index
- Checksum mismatch triggers rebuild, not crash

<!-- section_id: "f785fbf0-da6a-4faf-b905-5b60ac8121f9" -->
### Estimated Effort: 4-6 hours
<!-- section_id: "e999e186-13d2-4d2a-baac-05e0fcb07fb4" -->
### Depends On: Phase 3

---

<!-- section_id: "236a9d7f-a653-4696-8fc7-86a7d0351819" -->
## Phase 5: Migrate Existing Pointers

**Agent**: Script Agent
**Input**: All pointer files, UUID index
**Output**: `migrate-pointers.sh` script at `.0agnostic/`

<!-- section_id: "74211491-ce1e-4343-9e77-6ba133333ca8" -->
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

<!-- section_id: "427a71fe-c7bb-4fb6-8161-5f6d3b512e3e" -->
### Acceptance Criteria
- All existing pointer files get UUID fields added
- Old name fields are kept as display-only (renamed to `_name` suffix)
- `pointer-sync.sh --validate` passes after migration
- `--dry-run` shows changes without modifying

<!-- section_id: "a622d06f-9f9a-4ad3-811b-81ff11695fca" -->
### Estimated Effort: 3-4 hours
<!-- section_id: "bb729cd4-a8dc-456f-ad27-0d3e929b6726" -->
### Depends On: Phase 1, 2, 3 (needs UUIDs and updated pointer-sync.sh)

---

<!-- section_id: "1210e548-8676-4ae1-829c-2999e3806db6" -->
## Phase 6: Update Documentation

**Agent**: Docs Agent
**Input**: entity_structure.md, pointer_sync_protocol.md, pointer_file_convention.md
**Output**: Updated docs

<!-- section_id: "cb22a04b-212e-438e-817b-d86db324d340" -->
### Task

Update these canonical documents:

1. **entity_structure.md** — Add `entity_id` as required field in `0AGNOSTIC.md`, document `stage_index.json` format, document `resource_id` frontmatter
2. **pointer_sync_protocol.md** — Add UUID resolution steps, document `--rebuild-index`, update pointer format spec
3. **pointer_file_convention.md** — Add `canonical_entity_id`, `canonical_stage_id`, `canonical_resource_id` fields
4. **pointer_sync_knowledge.md** — Add UUID identity system to architecture overview

<!-- section_id: "adc3fabb-a42b-44af-a2c4-a458ab65e39c" -->
### Acceptance Criteria
- All docs reflect new UUID fields
- New pointer format is documented with examples
- Migration guide included

<!-- section_id: "f67363cf-316f-4884-a765-44a9a9915f67" -->
### Estimated Effort: 2-3 hours
<!-- section_id: "82e04292-c5c3-40c9-ad38-f5b6a86873e0" -->
### Depends On: Phase 3 (needs final pointer-sync.sh behavior)

---

<!-- section_id: "98032b32-ff60-4f74-acf3-906cc63249be" -->
## Phase 7: Full Integration Test

**Agent**: Test Agent
**Input**: Test design from `stage_3_07_testing/outputs/uuid_test_design.md`
**Output**: Updated `test_pointer_sync.sh` + new `test_uuid_system.sh`

<!-- section_id: "eafc5344-753b-4278-809b-d675d4a2d35a" -->
### Task

1. Extend `test_pointer_sync.sh` with UUID-specific test categories (see test design doc)
2. Create `test_uuid_system.sh` for migration script testing
3. Run full test suite
4. Iterate: fix failures, re-run until 0 FAIL

<!-- section_id: "b5db3649-3760-4e40-abf3-309bf3f1b1a1" -->
### Acceptance Criteria
- All existing 108 tests still pass
- All new UUID tests pass
- Migration scripts tested end-to-end
- Index rebuild tested

<!-- section_id: "0091e605-68bd-4bc3-87d8-2b28ae649ca8" -->
### Estimated Effort: 4-6 hours
<!-- section_id: "439d16ab-c837-4a2f-b7ea-c30a02a63167" -->
### Depends On: Phase 1-5 (needs everything implemented to test)

---

<!-- section_id: "f90157bd-4ff9-4af4-b7ff-e11c77f3fcb5" -->
## Phase 8: Final Sync

**Agent**: Coordinator
**Input**: All modified files
**Output**: Regenerated tool files, committed repo

<!-- section_id: "deb707ee-8916-494d-b817-eb572b975a08" -->
### Task

1. Run `agnostic-sync.sh` at repo root — regenerates all CLAUDE.md files (now with `entity_id`)
2. Run `pointer-sync.sh --rebuild-index` — builds initial UUID index
3. Run `pointer-sync.sh --validate` — verify all pointers resolve
4. Commit all changes with `[AI Context]` prefix
5. Push to remote

<!-- section_id: "10adec87-d447-444a-9f12-9076ac79ed55" -->
### Acceptance Criteria
- All CLAUDE.md files include `entity_id` from their `0AGNOSTIC.md`
- `.uuid-index.json` exists and is valid
- `pointer-sync.sh --validate` exits 0
- All changes committed and pushed

<!-- section_id: "1ecd0ed1-9bae-4462-b60c-8785e61b7bf1" -->
### Estimated Effort: 1-2 hours

---

<!-- section_id: "069a63ab-ef55-4090-b4bf-74b598b7a930" -->
## Phase 9: Git Hooks & Validation Infrastructure

**Agent**: Script Agent
**Input**: Updated pointer-sync.sh, agnostic-sync.sh
**Output**: Git hook scripts, validation runner

<!-- section_id: "122c4e54-14d7-449f-808d-50356a62eebf" -->
### Task

1. **Post-merge hook** (`.git/hooks/post-merge`):
   - Run `pointer-sync.sh --rebuild-index`
   - Run `pointer-sync.sh --validate`
   - Report any BROKEN pointers

2. **Pre-commit hook** (optional, `.git/hooks/pre-commit`):
   - If any `0AGNOSTIC.md` changed, warn if `agnostic-sync.sh` hasn't been run (stale CLAUDE.md)
   - If any pointer file changed, run `pointer-sync.sh --validate` on changed files

3. **Materialized view staleness detection**:
   - Add `<!-- source-hash: sha256:... -->` to generated CLAUDE.md files
   - Validation script compares stored hash vs current source hash

<!-- section_id: "0da36568-f7e5-4cf5-a35e-f1c879b05495" -->
### Acceptance Criteria
- Post-merge hook runs automatically and catches dangling references
- Pre-commit hook warns about stale materialized views
- Hooks don't block normal commits (warnings only, not errors)

<!-- section_id: "01ca3d78-c741-4ef4-84fb-16f65997656b" -->
### Estimated Effort: 2-3 hours
<!-- section_id: "7821c9b4-a25c-4d9f-b6c7-8abc260cb56d" -->
### Depends On: Phase 8

---

<!-- section_id: "6bc78a9b-b9d2-46cc-b51a-8c36c6366311" -->
## Phase 10: Directory UUID Index & Lazy Resolution

**Agent**: Pointer-Sync Agent
**Input**: All `.dir-id` files created in Phase 1c
**Output**: `.dir-uuid-index.json` at repo root, lazy resolution in pointer-sync.sh

<!-- section_id: "e3185755-d623-4d70-839c-64bf09abd574" -->
### Task

1. **Build `.dir-uuid-index.json`**: Scan all `.dir-id` files, create a JSON index mapping UUID → path
2. **Add `--rebuild-dir-index` flag** to pointer-sync.sh: Rebuilds `.dir-uuid-index.json` from filesystem scan
3. **Implement lazy resolution**: When a directory UUID lookup misses the index (UUID not found or path stale):
   - Scan filesystem: `find . -name .dir-id -exec grep -l "UUID" {} \;`
   - Update index with new path
   - Return resolved path
4. **Integrate with post-merge hook**: Add `.dir-uuid-index.json` rebuild to post-merge

<!-- section_id: "793af979-e2d3-489c-87bc-f21cc06e2d15" -->
### Index Format

```json
{
  "generated": "2026-03-02T10:30:00Z",
  "directories": {
    "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d": {
      "path": "layer_-1_research/layer_0_group/",
      "name": "layer_0_group"
    }
  }
}
```

<!-- section_id: "5167b821-fd99-4fc0-a5d3-5a6516f7fafa" -->
### Acceptance Criteria
- `.dir-uuid-index.json` is generated with all directory UUIDs
- `--rebuild-dir-index` rebuilds from `.dir-id` files
- Lazy resolution handles moved/renamed directories without manual intervention
- Index is `.gitignored` (build artifact, rebuilt from `.dir-id` source files)
- Post-merge hook triggers rebuild

<!-- section_id: "08abb438-7e62-4e08-810c-142f0cea30ab" -->
### Estimated Effort: 3-4 hours
<!-- section_id: "bca6d022-92bb-4b76-8f3b-fe1cf0887bc2" -->
### Depends On: Phase 1c

---

<!-- section_id: "3372992c-32c7-4088-bb49-f50ec42afa07" -->
## Execution Timeline

```
Session 1 (Scripts):
  [Coordinator] Review plan → delegate
  [Script Agent] Phase 1: assign-entity-uuids.sh      (2-3h)
  [Script Agent] Phase 1b: assign-file-uuids.sh       (6-8h, parallel)
  [Script Agent] Phase 1c: assign-dir-uuids.sh        (4-6h, parallel with 1b)
  [Script Agent] Phase 1d: assign-section-uuids.sh     (4-6h, after 1b)
  [Script Agent] Phase 2: create-stage-indexes.sh      (4-5h, after Phase 1)
  [Test Agent] Verify Phase 1-2 outputs

Session 1b (Submodule Coverage):
  [Script Agent] Phase 1e: Assign UUIDs to all 17 nested repos (8-12h)
    - File UUIDs for ~29,000 text files
    - Section UUIDs for remaining .md headings
    - Commit inside each repo, push if remote exists
    - Update parent submodule pointers

Session 2 (Core Changes):
  [Pointer-Sync Agent] Phase 3: Update pointer-sync.sh   (6-8h)
  [Pointer-Sync Agent] Phase 3b: Reference integrity     (4-6h, after Phase 3)
  [Skill Agent] Phase 4: Update entity-creation skill     (3-4h, parallel with 3)
  [Test Agent] Run existing tests + new UUID tests

Session 3 (Migration + Polish):
  [Script Agent] Phase 5: migrate-pointers.sh              (3-4h)
  [Docs Agent] Phase 6: Update documentation                (2-3h, parallel)
  [Test Agent] Phase 7: Full integration test               (4-6h)
  [Coordinator] Phase 8: Final sync + commit                (1-2h)
  [Script Agent] Phase 9: Git hooks + validation            (2-3h)
  [Pointer-Sync Agent] Phase 10: Dir UUID index + lazy res  (3-4h)
```

**Total estimated effort**: ~60-77 hours across 4 sessions

---

<!-- section_id: "5ffb3d34-fc14-4c17-81f2-0a0307eeb55a" -->
## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Migration breaks existing pointers | High | `--dry-run` on all scripts, run `--validate` after each phase |
| UUID index becomes stale | Medium | Auto-rebuild on index miss, `--rebuild-index` flag |
| Index corruption from concurrent access | Medium | File-based locking, atomic writes, checksum validation |
| Entity creation skill regressions | Medium | Test new entities with skill after changes |
| Long paths cause ENAMETOOLONG | Low | Work directly (no subagents for deep paths), use git -C |
| Partial migration (some pointers migrated, some not) | Low | Name-based fallback ensures backward compat |
| Dangling references after entity deletion | Low | `--find-references` before delete, `--validate` after |
| Git merge creates orphaned UUIDs | Low | Post-merge hook runs `--gc` and `--validate` |

---

<!-- section_id: "42f5e43c-be51-422e-b7c5-0072fc30f5ea" -->
## Phase 11: Parent/Children Entity Graph

**Agent**: Pointer-Sync Agent
**Status**: COMPLETE (2026-03-06)
**Input**: All `0AGNOSTIC.md` files with `**Parent**:` references
**Output**: Modified `pointer-sync.sh` with graph-aware `build_uuid_index()`

<!-- section_id: "a2b4c6d8-e0f2-4a1b-3c5d-7e9f1a3b5c7d" -->
### What Was Done

1. **Rewrote `build_uuid_index()`** from bash string-building to embedded Python (PYINDEX heredoc)
2. **Phase 1 of rebuild** now extracts parent references from 0AGNOSTIC.md, resolves relative paths, reads parent entity_id
3. **Computes `children[]`** by inverting the parent map after all entities are processed
4. **Added `--parent <uuid>` command** with `--verbose` for full chain walk
5. **Added `--children <uuid>` command** to list direct children
6. **Fixed stderr/stdout separation** so warnings don't corrupt JSON output

### Results

- 351 entities in index, 122 with resolved parent links, 34 with children
- Parent chain walks work correctly to root
- Children listings show all direct descendants

---

## Phase 12: Query CLI

**Agent**: Pointer-Sync Agent
**Status**: COMPLETE (2026-03-06)
**Input**: `.uuid-index.json` with 5,313 entries
**Output**: `--query` command in `pointer-sync.sh`

<!-- section_id: "b3c5d7e9-f0a1-4b2c-4d6e-8f0a2b4c6d8e" -->
### What Was Done

1. **Added `--query` CLI option** with key=value argument parsing
2. **Implemented Python query engine** (PYQUERY heredoc) with fnmatch-based filtering
3. **7 filter keys**: type, name, path, resource_type, entity_id, parent_id, has_children
4. **Multiple filters** combine with AND logic

### Results

- Queries execute in <100ms on full index
- All filter combinations tested and working

---

## Phase 13: Bulk Resource Index Rollout

**Agent**: Script Agent
**Status**: COMPLETE (2026-03-06)
**Input**: All entities with `.0agnostic/` directories
**Output**: 50 `resource_index.json` files, updated root index

<!-- section_id: "c4d6e8f0-a1b2-4c3d-5e7f-9a1b3c5d7e9f" -->
### What Was Done

1. **Fixed `create-resource-indexes.sh`** to skip entities without entity_id (graceful skip vs error)
2. **Ran bulk creation** across all eligible entities: 50 indexes created
3. **Rebuilt root index** to aggregate all resource entries
4. **Fixed stdout/stderr separation** in `do_rebuild_index()` to prevent JSON corruption

### Results

- 50 entities have resource indexes
- 4,566 resource entries aggregated into root index
- Total index: 5,313 entries (351 entity + 396 stage + 4,566 resource)
- Index size: ~2.6MB, load time: ~3ms

---

<!-- section_id: "d5e6f7a8-b9c0-4d1e-2f3a-4b5c6d7e8f9a" -->
## Phase 14: UUID Query Skill Context Avenue

**Agent**: Skill Agent + Docs Agent
**Status**: COMPLETE (designed 2026-03-06, implemented 2026-03-07)
**Input**: Design doc Section 6.2 (skill interface), Section 10 (skill context avenue design)
**Output**: Canonical skill, Claude Code port, 0AGNOSTIC.md references, regenerated context files
**Design Reference**: `../../stage_3_04_design/outputs/uuid_graph_and_query_design.md` Sections 6 and 10

<!-- section_id: "e6f7a8b9-c0d1-4e2f-3a4b-5c6d7e8f9a0b" -->
### Task

Create the `/uuid-query` skill that teaches agents how to use the UUID identity system for entity lookup, hierarchy navigation, and resource discovery. The skill exposes the existing `pointer-sync.sh` CLI through the standard skill context avenue.

#### Step 1: Create Canonical Skill

Create at `.0agnostic/06_context_avenue_web/01_file_based/05_skills/uuid-query/`:

```
uuid-query/
├── SKILL.md              ← Instructions: WHEN/WHEN NOT, commands, output format
└── references/           ← Pointers to existing resources
    ├── pointer_sync_knowledge.md  → ../../01_knowledge/pointer_sync/pointer_sync_knowledge.md
    ├── pointer_sync_rule.md       → ../../02_rules/static/pointer_sync_rule/pointer_sync_rule.md
    └── pointer_sync_protocol.md   → ../../03_protocols/pointer_sync_protocol/pointer_sync_protocol.md
```

SKILL.md content comes from design doc Section 10.3 (skill content design).

#### Step 2: Create Claude Code Port

Create at `.claude/skills/uuid-query/SKILL.md` with Claude-specific frontmatter:

```yaml
---
resource_id: "<generate-uuid-v4>"
resource_type: "skill"
resource_name: "uuid-query"
---
---
name: uuid-query
description: Query and navigate the UUID identity system for entity lookup, hierarchy traversal, and resource discovery
---
```

Body content matches canonical SKILL.md from Step 1, with Claude-specific adaptations (e.g., tool references like "Read tool" instead of generic "file read").

#### Step 3: Update SKILLS.md Index

Add row to `.0agnostic/06_context_avenue_web/01_file_based/05_skills/SKILLS.md`:

```markdown
| uuid-query | Querying UUID identity system, entity lookup, hierarchy navigation | `uuid-query/` |
```

#### Step 4: Update Root 0AGNOSTIC.md

Add to Triggers table:
```markdown
| Querying UUID identity system (entity lookup, hierarchy, resources) | Load skill: uuid-query |
```

Add to Resources table:
```markdown
| UUID Query Skill | `.0agnostic/06_context_avenue_web/01_file_based/05_skills/uuid-query/SKILL.md` | Agent interface for UUID system queries |
```

#### Step 5: Run agnostic-sync.sh

Regenerate all context files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, copilot-instructions.md) so the trigger and resource reference appear in all tool contexts.

#### Step 6: Verify Porting

| Tool | Verification |
|------|-------------|
| Claude Code | `.claude/skills/uuid-query/SKILL.md` exists, `/uuid-query` invocable |
| Cursor | `.cursorrules` contains uuid-query trigger text |
| Gemini | `GEMINI.md` contains uuid-query trigger text |
| Copilot | `.github/copilot-instructions.md` contains uuid-query trigger text |
| OpenAI | `OPENAI.md` contains uuid-query trigger text |

#### Step 7: Commit and Push

```bash
git add .0agnostic/06_context_avenue_web/01_file_based/05_skills/uuid-query/
git add .0agnostic/06_context_avenue_web/01_file_based/05_skills/SKILLS.md
git add .claude/skills/uuid-query/
git add 0AGNOSTIC.md CLAUDE.md AGENTS.md GEMINI.md OPENAI.md .cursorrules .github/copilot-instructions.md
git commit -m "[AI Context] Add /uuid-query skill context avenue with Claude Code port"
git push
```

<!-- section_id: "f7a8b9c0-d1e2-4f3a-4b5c-6d7e8f9a0b1c" -->
### Dependencies

| Dependency | Status | Why Needed |
|-----------|--------|-----------|
| Phase 11 (parent/children graph) | COMPLETE | Skill teaches `--parent`, `--children` commands |
| Phase 12 (query CLI) | COMPLETE | Skill teaches `--query` command |
| Phase 13 (resource indexes) | COMPLETE | Skill teaches resource catalog queries |
| Design doc Section 6.2 | COMPLETE | Defines skill interface (WHEN/WHEN NOT, commands) |
| Design doc Section 10 | COMPLETE | Defines skill context avenue architecture |

All dependencies are satisfied — this phase can be executed immediately.

<!-- section_id: "a8b9c0d1-e2f3-4a4b-5c6d-7e8f9a0b1c2d" -->
### Acceptance Criteria

- [ ] Canonical SKILL.md exists at `.0agnostic/06_context_avenue_web/01_file_based/05_skills/uuid-query/SKILL.md`
- [ ] `references/` directory has pointer files to knowledge, rule, and protocol
- [ ] Claude Code port exists at `.claude/skills/uuid-query/SKILL.md`
- [ ] SKILLS.md index includes uuid-query row
- [ ] Root `0AGNOSTIC.md` has trigger and resource entries
- [ ] `agnostic-sync.sh` regenerated all context files
- [ ] Trigger text appears in generated CLAUDE.md, GEMINI.md, OPENAI.md, .cursorrules, copilot-instructions.md
- [ ] All changes committed with `[AI Context]` prefix and pushed

<!-- section_id: "b9c0d1e2-f3a4-4b5c-6d7e-8f9a0b1c2d3e" -->
### Estimated Effort: 2-3 hours
### Depends On: Phase 12, Phase 13 (needs query CLI and resource indexes to be complete)
### Can Run Parallel With: Phase 3b, Phase 4, Phase 5

---

## Phase 16: Script Protocol Migration

**Agent**: Coordinator + Docs Agent
**Status**: COMPLETE (2026-03-07)
**Input**: 12 shell scripts loose at `.0agnostic/` root
**Output**: All scripts organized into protocol directories with UUID-based references
**Design Reference**: `../../stage_3_04_design/outputs/script_protocol_migration_design.md`

<!-- section_id: "a1c2d3e4-f5a6-4b7c-8d9e-0f1a2b3c4d5e" -->
### Problem

12 shell scripts sat loose at `.0agnostic/` root, violating the convention that everything in `.0agnostic/` belongs in numbered subdirectories (01_knowledge, 02_rules, 03_protocols, etc.). Additionally, all 65+ documentation references used hardcoded paths (`.0agnostic/pointer-sync.sh`) — exactly the brittleness that the UUID system was designed to eliminate.

**Core insight**: The UUID identity system exists precisely to solve this problem. Every script already had a `resource_id` (UUID). When we move scripts, the UUID stays stable — only the path changes. References should use UUID for stability with path as human-readable convenience.

### What Was Done

1. **Created protocol directory structure**: Three protocol directories under `.0agnostic/03_protocols/`, each with a `tools/` subdirectory
2. **Moved all 12 scripts** from `.0agnostic/` root into their protocol's `tools/` directory:
   - 4 scripts → `pointer_sync_protocol/tools/`
   - 5 scripts → `uuid_assignment_protocol/tools/`
   - 3 scripts → `agnostic_sync_protocol/tools/`
3. **Fixed internal ROOT/path references** in all scripts (scripts were now 4 levels deeper)
4. **Fixed cross-protocol references** (agnostic-sync.sh → pointer-sync.sh uses relative path traversal)
5. **Created protocol docs** for uuid_assignment_protocol and agnostic_sync_protocol (pointer_sync_protocol already existed)
6. **Updated 81+ files** with hardcoded path references to use new paths
7. **Updated git hooks** (pre-commit, post-merge) and pointer-edit-guard.sh
8. **Assigned resource_id** to entity-find.sh (only script missing one)

### Script Organization

| Protocol | Scripts | Count |
|----------|---------|-------|
| pointer_sync_protocol | pointer-sync.sh, entity-find.sh, create-resource-indexes.sh, migrate-pointers.sh | 4 |
| uuid_assignment_protocol | assign-entity-uuids.sh, assign-file-uuids.sh, assign-dir-uuids.sh, assign-section-uuids.sh, create-stage-indexes.sh | 5 |
| agnostic_sync_protocol | agnostic-sync.sh, agnostic-diagram-generator.sh, user-level-sync.sh | 3 |

### Key Design Decision: Path is Convenience, UUID is Truth

After this migration, references in documentation include both UUID and path:
```
| pointer-sync.sh | `.../pointer_sync_protocol/tools/` | resource_id: `08a4e9bc-...` |
```

If the path changes again in the future, the UUID remains stable. The `.uuid-index.json` resolves UUID → current path. This eliminates the "bajillion file changes" problem — future moves only require: (1) physically move the file, (2) rebuild the UUID index. All UUID-based lookups automatically resolve to the new path.

### Depends On: Phase 15 (entity-find.sh existed and needed a resource_id)

---

<!-- section_id: "a2b3c4d5-e6f7-4a8b-9c0d-1e2f3a4b5c6d" -->
## UUID Resolution System — Phases 17-24

**Design Reference**: `../../stage_3_04_design/outputs/uuid_resolution_system_design.md`
**Research Reference**: `../../stage_3_02_research/outputs/ai_app_bash_capability_research.md`
**Requirements Reference**: `../../stage_3_01_request_gathering/outputs/requests/tree_of_needs/00_pointers_stay_synchronized/05_uuid_based_reference_resolution/`

### Problem Being Solved

Phases 1-16 built a comprehensive UUID identity system — every entity, file, directory, section, and stage has a stable UUID. But **references throughout the codebase still use hardcoded filesystem paths**. When anything moves, all path references break (81+ files during the script protocol migration in Phase 16). UUIDs exist as metadata alongside paths, but nothing resolves via UUID at runtime.

### Goal

Make UUID the **primary reference mechanism**. Paths become derived artifacts, resolved at the moment of use from the UUID index. Moving anything requires only: `mv` + `rebuild-index` = done.

### Key Research Finding

All major AI coding apps (Claude Code, Codex CLI, Gemini CLI, Copilot, Cursor, Windsurf, Aider, Cline, Continue.dev, Amazon Q, JetBrains AI, Open Interpreter) can run bash. UUID references with `resolve-uuid` instructions can go in **all** ported context files. No app needs pre-resolved paths as its primary mechanism.

---

<!-- section_id: "b3c4d5e6-f7a8-4b9c-0d1e-2f3a4b5c6d7e" -->
## Phase 17: Create resolve-uuid Function

**Agent**: Script Agent
**Status**: PLANNED
**Input**: `.uuid-index.json` (5,313 entries from Phase 13), design doc resolve-uuid specification
**Output**: `resolve-uuid.sh` at `.0agnostic/03_protocols/pointer_sync_protocol/tools/`

<!-- section_id: "c4d5e6f7-a8b9-4c0d-1e2f-3a4b5c6d7e8f" -->
### Task

Create a standalone shell function/script that resolves any UUID to its current filesystem path:

1. **Core function**:
   ```bash
   resolve-uuid() {
     local uuid="$1"
     local root
     root="$(git rev-parse --show-toplevel 2>/dev/null || echo "$HOME/dawson-workspace/code/0_layer_universal")"
     local index="$root/.uuid-index.json"

     if [[ ! -f "$index" ]]; then
       echo "ERROR: UUID index not found at $index" >&2
       return 1
     fi

     local path
     path=$(jq -r --arg id "$uuid" '.[$id].path // empty' "$index")

     if [[ -z "$path" ]]; then
       echo "ERROR: UUID $uuid not found in index" >&2
       return 1
     fi

     echo "$root/$path"
   }
   ```

2. **Bootstrapping**: Uses `git rev-parse --show-toplevel` to find repo root. Index is always at `$ROOT/.uuid-index.json`. This is the one hardcoded path in the entire system.

3. **Distribution**: Two modes:
   - **Standalone script** at a well-known location (sourced by other scripts)
   - **Inline function** that scripts can copy into their preamble (for bootstrap independence)

4. **Assign `resource_id`** to the new script (UUID v4)

5. **Error handling**: Clear stderr messages for missing index, missing UUID, ambiguous prefix (Phase 22)

<!-- section_id: "d5e6f7a8-b9c0-4d1e-2f3a-4b5c6d7e8f9a" -->
### Acceptance Criteria
- `resolve-uuid <full-uuid>` returns the absolute path for any UUID in the index
- Resolution completes in <10ms (load + lookup)
- Works from any directory within the repo (uses `git rev-parse` for root)
- Works in sandboxed environments (only reads a local JSON file, no network)
- Clear error messages for: missing index, UUID not found, ambiguous prefix
- Script has `resource_id` in its header
- Script is executable and has correct shebang

### Estimated Effort: 2-3 hours
### Depends On: Phase 13 (`.uuid-index.json` must exist with 5,313+ entries), Phase 16 (scripts organized into protocols)

---

<!-- section_id: "e6f7a8b9-c0d1-4e2f-3a4b-5c6d7e8f9a0b" -->
## Phase 18: Update Scripts to Use resolve-uuid

**Agent**: Script Agent
**Status**: PLANNED
**Input**: All 12 scripts in `.0agnostic/03_protocols/*/tools/`, `resolve-uuid` from Phase 17
**Output**: Modified scripts using UUID-based cross-protocol references

<!-- section_id: "f7a8b9c0-d1e2-4f3a-4b5c-6d7e8f9a0b1c" -->
### Task

Replace hardcoded cross-protocol path references in scripts with `resolve-uuid` calls:

1. **Identify cross-protocol calls**: Scripts that call scripts in *different* protocol directories. Key examples:
   - `agnostic-sync.sh` calls `pointer-sync.sh` for validation → currently uses relative path traversal
   - `pointer-sync.sh` calls `entity-find.sh` → currently uses `$SCRIPT_DIR/entity-find.sh` (same directory, keep as-is)

2. **Replace cross-protocol references**:
   ```bash
   # Before (hardcoded relative path — breaks if either script moves):
   POINTER_SYNC="$ROOT/.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh"

   # After (UUID — doesn't matter where either script lives):
   POINTER_SYNC="$(resolve-uuid 08a4e9bc-8cc1-457e-b966-0a912ae6dff7)"
   ```

3. **Keep same-directory references**: Scripts in the same `tools/` directory can still use `$SCRIPT_DIR/` for efficiency (they'll always move together as a group)

4. **Source resolve-uuid**: Each script that needs cross-protocol resolution sources the function:
   ```bash
   source "$(git rev-parse --show-toplevel)/.0agnostic/03_protocols/pointer_sync_protocol/tools/resolve-uuid.sh"
   ```
   Or inline the function in scripts that need bootstrap independence.

5. **Update git hooks**: Hooks in `.git/hooks/` (pre-commit, post-merge) currently use hardcoded paths to scripts. Replace with `resolve-uuid` calls.

<!-- section_id: "a8b9c0d1-e2f3-4a4b-5c6d-7e8f9a0b1c2d" -->
### Scripts to Modify

| Script | Current Cross-Protocol Calls | Change |
|--------|------------------------------|--------|
| `agnostic-sync.sh` | calls `pointer-sync.sh` | Use `resolve-uuid 08a4e9bc` |
| `user-level-sync.sh` | calls `agnostic-sync.sh` | Use `resolve-uuid 781698fa` |
| `.git/hooks/pre-commit` | calls `pointer-sync.sh` | Use `resolve-uuid 08a4e9bc` |
| `.git/hooks/post-merge` | calls `pointer-sync.sh` | Use `resolve-uuid 08a4e9bc` |
| `pointer-edit-guard.sh` | calls `pointer-sync.sh` | Use `resolve-uuid 08a4e9bc` |

Scripts that only call within their own `tools/` directory (entity-find.sh, create-resource-indexes.sh, etc.) keep `$SCRIPT_DIR/` references — no change needed.

### Acceptance Criteria
- All cross-protocol script references use `resolve-uuid` instead of hardcoded paths
- Same-directory references (`$SCRIPT_DIR/`) are preserved (not changed)
- Git hooks use `resolve-uuid` for script discovery
- All scripts still execute correctly from their current locations
- Moving any single script to a new location + rebuilding index = cross-protocol calls still work

### Estimated Effort: 3-4 hours
### Depends On: Phase 17 (resolve-uuid must exist)

---

<!-- section_id: "b9c0d1e2-f3a4-4b5c-6d7e-8f9a0b1c2d3e" -->
## Phase 19: Add {{resolve:UUID}} Placeholder Syntax to 0AGNOSTIC.md

**Agent**: Docs Agent
**Status**: PLANNED
**Input**: Root `0AGNOSTIC.md` and all entity-level `0AGNOSTIC.md` files that reference scripts/resources by path
**Output**: 0AGNOSTIC.md files with `{{resolve:UUID}}` placeholders instead of hardcoded paths

<!-- section_id: "c0d1e2f3-a4b5-4c6d-7e8f-9a0b1c2d3e4f" -->
### Task

Define and deploy the `{{resolve:UUID}}` placeholder syntax in 0AGNOSTIC.md source files:

1. **Syntax definition**:
   ```markdown
   | pointer-sync.sh | `{{resolve:08a4e9bc-8cc1-457e-b966-0a912ae6dff7}}` | Sync all pointers |
   ```
   The `{{resolve:UUID}}` placeholder is:
   - **Human-scannable**: The UUID is visible, can be looked up manually
   - **Machine-resolvable**: `agnostic-sync.sh` replaces it with the current path during generation
   - **Stable**: Never needs updating when things move
   - **Grep-searchable**: `grep -r '{{resolve:' .` finds all UUID references

2. **Convert key references in root 0AGNOSTIC.md**: Replace hardcoded script paths in the Triggers table, Resources table, and any inline references with `{{resolve:UUID}}` placeholders

3. **Convert entity-level 0AGNOSTIC.md files**: The trigger_pointer_system's 0AGNOSTIC.md has a Production Artifacts table with hardcoded paths — convert to placeholders

4. **Document the syntax**: Add a brief section to the root 0AGNOSTIC.md explaining the placeholder convention

### Key Conversions

| Current Reference | Placeholder |
|-------------------|-------------|
| `.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh` | `{{resolve:08a4e9bc-8cc1-457e-b966-0a912ae6dff7}}` |
| `.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh` | `{{resolve:781698fa-f580-4606-80e4-dc73fb30e3f7}}` |
| `.0agnostic/03_protocols/pointer_sync_protocol/tools/entity-find.sh` | `{{resolve:f4a2b3c5-d6e7-4f89-a0b1-c2d3e4f5a6b7}}` |
| `.0agnostic/03_protocols/uuid_assignment_protocol/tools/assign-entity-uuids.sh` | `{{resolve:92ab3def-22d7-48cd-91be-6744c3466240}}` |
| (and all other scripts with resource_ids) | (corresponding `{{resolve:UUID}}`) |

### Acceptance Criteria
- `{{resolve:UUID}}` syntax is defined and documented
- Root `0AGNOSTIC.md` uses placeholders for all script/resource references
- Trigger_pointer_system `0AGNOSTIC.md` uses placeholders in Production Artifacts table
- Placeholders are valid markdown (render as code blocks with the UUID visible)
- `grep -r '{{resolve:' .` finds all placeholder references
- No `agnostic-sync.sh` changes yet (that's Phase 20) — placeholders are inert until Phase 20

### Estimated Effort: 3-4 hours
### Depends On: Phase 17 (resolve-uuid function exists to validate UUIDs)

---

<!-- section_id: "d1e2f3a4-b5c6-4d7e-8f9a-0b1c2d3e4f5a" -->
## Phase 20: Update agnostic-sync.sh for UUID Integration

**Agent**: Script Agent
**Status**: PLANNED
**Input**: `agnostic-sync.sh`, `{{resolve:UUID}}` syntax from Phase 19, `resolve-uuid` from Phase 17
**Output**: Modified `agnostic-sync.sh` that resolves placeholders and emits UUID references

<!-- section_id: "e2f3a4b5-c6d7-4e8f-9a0b-1c2d3e4f5a6b" -->
### Task

Enhance `agnostic-sync.sh` to handle UUID placeholders during context file generation:

1. **Placeholder resolution**: When processing 0AGNOSTIC.md content, detect `{{resolve:UUID}}` patterns and replace with:
   - **For all context files** (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, copilot-instructions.md): Emit the current path (resolved at generation time) plus the UUID and resolve-uuid instruction for self-healing:
     ```markdown
     | pointer-sync.sh | `.0agnostic/03_protocols/.../pointer-sync.sh` | UUID: `08a4e9bc` · `resolve-uuid 08a4e9bc` |
     ```
   - This gives both human-readable path AND UUID for runtime resolution

2. **Emit resolve-uuid instructions**: Add a section to generated context files explaining how to resolve UUID references:
   ```markdown
   ## UUID Resolution
   Scripts and resources are referenced by UUID for stability.
   To resolve any UUID to its current path: `resolve-uuid <UUID>`
   Or: `jq -r --arg id "<UUID>" '.[$id].path' .uuid-index.json`
   ```

3. **Self-healing property**: Even if `agnostic-sync.sh` hasn't been re-run after a move:
   - The UUID reference in the generated file is still valid
   - The AI app runs `resolve-uuid` and gets the current path from the rebuilt index
   - No stale window between move and context file regeneration

4. **Placeholder validation**: During generation, verify each `{{resolve:UUID}}` resolves in the current index. Warn if any UUID is not found (catches typos in 0AGNOSTIC.md).

### Acceptance Criteria
- `agnostic-sync.sh` detects and resolves `{{resolve:UUID}}` patterns in 0AGNOSTIC.md
- Generated context files contain both human-readable path and UUID reference
- Generated context files include resolve-uuid instructions section
- Unresolvable UUIDs produce a warning during generation (not a fatal error)
- All 6 context file formats updated: CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, copilot-instructions.md
- Existing non-placeholder content is unaffected

### Estimated Effort: 4-6 hours
### Depends On: Phase 17 (resolve-uuid function), Phase 19 (placeholders exist in 0AGNOSTIC.md)

---

<!-- section_id: "f3a4b5c6-d7e8-4f9a-0b1c-2d3e4f5a6b7c" -->
## Phase 21: Git Hooks — Auto-Rebuild + UUID Reference Validation

**Agent**: Script Agent
**Status**: PLANNED
**Input**: Existing git hooks (pre-commit, post-merge), `resolve-uuid` from Phase 17
**Output**: Enhanced git hooks with auto-rebuild and UUID validation

<!-- section_id: "a4b5c6d7-e8f9-4a0b-1c2d-3e4f5a6b7c8d" -->
### Task

Enhance git hooks to support the UUID resolution system:

1. **Post-checkout + post-merge auto-rebuild**:
   Add `pointer-sync.sh --rebuild-index` to post-checkout and post-merge hooks. After any `git checkout`, `git pull`, or `git merge`, the UUID index is automatically rebuilt. Combined with Phase 18 (scripts use resolve-uuid), the move workflow becomes: `mv` + `commit` — the index rebuilds automatically on the next checkout/merge.

   ```bash
   # Append to .git/hooks/post-checkout and post-merge:
   "$(resolve-uuid 08a4e9bc-8cc1-457e-b966-0a912ae6dff7)" --rebuild-index --quiet
   ```

2. **Pre-commit UUID reference validation**:
   Scan staged files for UUID references (`resolve-uuid` calls and `{{resolve:UUID}}` patterns) and verify each resolves in the current index. Catches broken UUID references before they're committed.

   ```bash
   # In pre-commit hook:
   for uuid in $(grep -rohP 'resolve[-_]uuid\s+([0-9a-f-]{8,36})' "$staged_files" | grep -oP '[0-9a-f-]{8,36}'); do
     if ! jq -e --arg id "$uuid" '.[$id]' "$ROOT/.uuid-index.json" >/dev/null 2>&1; then
       echo "WARNING: UUID $uuid not found in index" >&2
     fi
   done
   ```

3. **Post-checkout hook creation**: Currently only pre-commit and post-merge exist. Create post-checkout hook.

### Acceptance Criteria
- Post-checkout hook runs `--rebuild-index` automatically
- Post-merge hook runs `--rebuild-index` automatically (already has pointer-sync calls, add rebuild)
- Pre-commit hook validates UUID references in staged files
- UUID validation is a warning, not a blocking error (gradual adoption)
- Hooks use `resolve-uuid` to find pointer-sync.sh (not hardcoded paths) — bootstrapping via `git rev-parse`
- Moving a file + committing + checking out on another machine = index auto-rebuilds

### Estimated Effort: 2-3 hours
### Depends On: Phase 17 (resolve-uuid), Phase 18 (scripts using resolve-uuid, so hooks need it too)

---

<!-- section_id: "b5c6d7e8-f9a0-4b1c-2d3e-4f5a6b7c8d9e" -->
## Phase 22: UUID Short-Form Prefix Matching

**Agent**: Script Agent
**Status**: PLANNED
**Input**: `resolve-uuid` from Phase 17
**Output**: Enhanced `resolve-uuid` with prefix matching support

<!-- section_id: "c6d7e8f9-a0b1-4c2d-3e4f-5a6b7c8d9e0f" -->
### Task

Support 8-character UUID prefixes like git does with commit SHAs. With 5,300 entries, collisions at 8 hex characters are essentially impossible (16^8 = 4.3 billion possible prefixes).

1. **Enhance resolve-uuid**:
   ```bash
   resolve-uuid() {
     local uuid="$1"
     local root="$(git rev-parse --show-toplevel)"
     local index="$root/.uuid-index.json"

     # Try exact match first, then prefix match
     local path
     path=$(jq -r --arg id "$uuid" '
       if .[$id] then .[$id].path
       else [to_entries[] | select(.key | startswith($id))] |
         if length == 1 then .[0].value.path
         elif length == 0 then empty
         else "AMBIGUOUS"
         end
       end // empty' "$index")

     if [[ "$path" == "AMBIGUOUS" ]]; then
       echo "ERROR: UUID prefix $uuid is ambiguous (multiple matches)" >&2
       return 1
     elif [[ -z "$path" ]]; then
       echo "ERROR: UUID $uuid not found" >&2
       return 1
     fi

     echo "$root/$path"
   }
   ```

2. **Update all documentation** to show short-form examples alongside full UUIDs:
   ```markdown
   | pointer-sync.sh | `08a4e9bc` | `$(resolve-uuid 08a4e9bc)` |
   ```

3. **Performance**: Prefix matching requires scanning all keys, but with <6,000 entries and jq, this still completes in <50ms. Acceptable for interactive use.

### Acceptance Criteria
- `resolve-uuid 08a4e9bc` resolves the same as `resolve-uuid 08a4e9bc-8cc1-457e-b966-0a912ae6dff7`
- Ambiguous prefixes (multiple matches) produce a clear error with the matching UUIDs listed
- Non-matching prefixes produce a clear "not found" error
- Resolution with short-form still completes in <50ms
- Documentation updated to show short-form usage

### Estimated Effort: 1-2 hours
### Depends On: Phase 17 (resolve-uuid must exist to enhance)
### Can Run Parallel With: Phases 18, 19, 20, 21

---

<!-- section_id: "d7e8f9a0-b1c2-4d3e-4f5a-6b7c8d9e0f1a" -->
## Phase 23: Logical Names — resolve-name Aliases

**Agent**: Script Agent + Docs Agent
**Status**: PLANNED
**Input**: `resolve-uuid` from Phase 17, script inventory from Phase 16
**Output**: `.uuid-aliases.tsv`, `resolve-name` function

<!-- section_id: "e8f9a0b1-c2d3-4e4f-5a6b-7c8d9e0f1a2b" -->
### Task

Create a human-friendly alias layer for the most commonly referenced scripts and resources:

1. **Create `.uuid-aliases.tsv`** at repo root (manually curated, small file):
   ```tsv
   pointer-sync	08a4e9bc-8cc1-457e-b966-0a912ae6dff7
   entity-find	f4a2b3c5-d6e7-4f89-a0b1-c2d3e4f5a6b7
   agnostic-sync	781698fa-f580-4606-80e4-dc73fb30e3f7
   assign-entity-uuids	92ab3def-22d7-48cd-91be-6744c3466240
   assign-file-uuids	68c9cfcc-9915-47f6-be3a-2c75fbd7ef7e
   assign-dir-uuids	c7d8e9f0-1a2b-4c3d-e4f5-6a7b8c9d0e1f
   assign-section-uuids	d8e9f0a1-2b3c-4d5e-f6a7-8b9c0d1e2f3a
   create-stage-indexes	bcac347f-f4e3-4047-8171-ed9a20022624
   create-resource-indexes	9f294247-a227-4bf1-8a51-bdee7555115c
   migrate-pointers	7505b140-8772-43f1-abe5-996847e68657
   agnostic-diagram-generator	44f8f145-6ab5-44c0-8538-887e7c652052
   user-level-sync	5e3e7995-23d1-42e6-9a11-de1515e6367f
   ```

2. **Create `resolve-name` function** (in resolve-uuid.sh or separate):
   ```bash
   resolve-name() {
     local name="$1"
     local root="$(git rev-parse --show-toplevel)"
     local uuid=$(grep "^${name}	" "$root/.uuid-aliases.tsv" | cut -f2)
     if [[ -z "$uuid" ]]; then
       echo "ERROR: Name '$name' not found in .uuid-aliases.tsv" >&2
       return 1
     fi
     resolve-uuid "$uuid"
   }
   ```

3. **Usage in scripts**:
   ```bash
   # Human-friendly:
   bash "$(resolve-name pointer-sync)" --validate

   # Equivalent to:
   bash "$(resolve-uuid 08a4e9bc)" --validate
   ```

4. **Names are mutable convenience aliases**: The UUID underneath is the stable identity. If a name changes, update the aliases file (one line). If a file moves, rebuild the UUID index (automatic). Neither requires updating references in scripts.

### Acceptance Criteria
- `.uuid-aliases.tsv` exists at repo root with all 12 script aliases
- `resolve-name pointer-sync` returns the absolute path to pointer-sync.sh
- Unknown names produce a clear error
- Names are case-sensitive and exact-match
- Aliases file is git-tracked (manually curated, not generated)
- Documentation shows `resolve-name` usage alongside `resolve-uuid`

### Estimated Effort: 1-2 hours
### Depends On: Phase 17 (resolve-uuid must exist)
### Can Run Parallel With: Phases 18, 19, 20, 21, 22

---

<!-- section_id: "f9a0b1c2-d3e4-4f5a-6b7c-8d9e0f1a2b3c" -->
## Phase 24: End-to-End Validation

**Agent**: Test Agent + Coordinator
**Status**: PLANNED
**Input**: All outputs from Phases 17-23
**Output**: Validation report, updated test suite

<!-- section_id: "a0b1c2d3-e4f5-4a6b-7c8d-9e0f1a2b3c4d" -->
### Task

Comprehensive end-to-end validation that the UUID resolution system works correctly:

1. **Move test — script**:
   - Move `pointer-sync.sh` to a temporary location
   - Run `pointer-sync.sh --rebuild-index`
   - Verify `resolve-uuid 08a4e9bc` returns the new path
   - Verify `agnostic-sync.sh` still calls pointer-sync.sh correctly (via resolve-uuid)
   - Move pointer-sync.sh back, rebuild index

2. **Move test — entity directory**:
   - Rename an entity directory
   - Rebuild index
   - Verify all UUID references to that entity and its contents resolve correctly
   - Rename back, rebuild index

3. **Self-healing test**:
   - Move a script, rebuild index, but do NOT re-run agnostic-sync.sh
   - Verify that an AI app reading CLAUDE.md can still resolve the script via the UUID reference + resolve-uuid instruction
   - Confirms the self-healing property (no stale window)

4. **Git hook test**:
   - Move a script, commit, push to a branch
   - Checkout the branch on a fresh clone
   - Verify post-checkout hook rebuilds the index automatically
   - Verify all resolve-uuid calls work on the fresh clone

5. **Short-form test**: Verify all 12 scripts resolve via 8-char prefix

6. **Logical name test**: Verify all 12 scripts resolve via `resolve-name`

7. **Pre-commit validation test**: Stage a file with a bad UUID reference, verify pre-commit warns

8. **Placeholder test**: Verify `agnostic-sync.sh` correctly resolves `{{resolve:UUID}}` placeholders in generated files

9. **Performance test**: Time `resolve-uuid` for 100 random UUIDs, verify average <10ms

10. **Update test suite**: Add these tests to `test_pointer_sync.sh` or a new `test_uuid_resolution.sh`

### Acceptance Criteria
- All 9 test scenarios pass
- Moving a script + rebuilding index = all UUID references resolve automatically
- Self-healing property confirmed (CLAUDE.md not regenerated, UUID still resolves)
- Git hooks trigger automatic rebuild
- Short-form and logical name resolution both work
- Pre-commit catches bad UUID references
- Performance within budget (<10ms per resolution)
- Test suite committed and executable

### Estimated Effort: 4-6 hours
### Depends On: All of Phases 17-23

---

<!-- section_id: "b1c2d3e4-f5a6-4b7c-8d9e-0f1a2b3c4d5e" -->
## Execution Timeline (Phases 17-24)

```
Session 5 (UUID Resolution Core):
  [Script Agent] Phase 17: Create resolve-uuid function            (2-3h)
  [Script Agent] Phase 22: UUID short-form prefix matching         (1-2h, after 17)
  [Script Agent] Phase 23: Logical names / resolve-name            (1-2h, after 17, parallel with 22)
  [Script Agent] Phase 18: Update scripts to use resolve-uuid      (3-4h, after 17)

Session 6 (Placeholder System + Hooks):
  [Docs Agent] Phase 19: {{resolve:UUID}} syntax in 0AGNOSTIC.md   (3-4h, after 17)
  [Script Agent] Phase 20: agnostic-sync.sh UUID integration       (4-6h, after 19)
  [Script Agent] Phase 21: Git hooks auto-rebuild + validation     (2-3h, after 17, 18)

Session 7 (Validation):
  [Test Agent] Phase 24: End-to-end validation                     (4-6h, after all)
  [Coordinator] Final commit and push
```

**Total estimated effort (Phases 17-24)**: ~20-30 hours across 3 sessions

**Grand total (Phases 1-24)**: ~80-107 hours across 7 sessions

---

<!-- section_id: "c2d3e4f5-a6b7-4c8d-9e0f-1a2b3c4d5e6f" -->
## Risk Assessment (Phases 17-24)

| Risk | Impact | Mitigation |
|------|--------|------------|
| resolve-uuid adds latency to every script call | Medium | Performance budget: <10ms. jq on 2.6MB JSON is ~3ms load + <0.03ms lookup. Well within budget. |
| `{{resolve:UUID}}` placeholders break markdown rendering | Low | Placeholders render as inline code — visually acceptable. Test in all 6 context file formats. |
| agnostic-sync.sh changes break existing generation | High | Test thoroughly before deploying. Existing non-placeholder content must be unaffected. |
| Short-form prefix collisions | Very Low | 16^8 = 4.3B possible prefixes for ~5,300 entries. Collision probability ~0.000003%. Detect and warn if it occurs. |
| Developers forget to rebuild index after moves | Medium | Post-checkout/post-merge hooks auto-rebuild (Phase 21). Manual rebuilds become rarely needed. |
| Bootstrap problem (resolve-uuid finding itself) | Low | `git rev-parse --show-toplevel` is always available. One hardcoded relative path: `.uuid-index.json` from repo root. |
| Partial adoption (some refs UUID, some still hardcoded) | Medium | Gradual migration is acceptable. Hardcoded paths still work — UUID refs are additive, not replacing. Pre-commit validation warns about unresolvable UUIDs. |
| Index becomes stale in working tree | Medium | Auto-rebuild on checkout/merge. For in-session staleness, manual `--rebuild-index` is fast (~3s). |

---

## Verification Checklist

After all phases complete:

- [x] Every `0AGNOSTIC.md` with Identity section has `entity_id`
- [x] Every stage's `0AGNOSTIC.md` has `stage_id`
- [x] Every entity with stages has `stage_index.json`
- [x] **Every `.md` file** has `resource_id` in YAML frontmatter (core + submodules)
- [x] **Every `.sh` file** has `resource_id` in comment header (core + submodules)
- [x] **Every `.json`/`.jsonld` file** has `file_id` in root object (core + submodules)
- [x] **Every auto-generated file** has `derived_from` reference
- [x] **Every directory** has a `.dir-id` file with UUID (core + submodules — already 100%)
- [x] **All empty `.gitkeep` files** replaced by `.dir-id` files
- [x] **All 17 nested repos** have file UUIDs assigned (~29,000 files)
- [x] **All 17 nested repos** have section UUIDs for h2/h3 headings in `.md` files
- [x] **Each nested repo** has its own `[AI Context]` commit
- [x] **Parent submodule pointers** updated after nested repo UUID assignment
- [ ] `.dir-uuid-index.json` exists and is valid
- [ ] Lazy directory resolution handles renames/moves without manual intervention
- [x] `pointer-sync.sh` resolves by UUID-first, name fallback
- [x] `pointer-sync.sh --find-references` works (reverse UUID lookup)
- [ ] `pointer-sync.sh --detect-cycles` reports cycles correctly
- [ ] `pointer-sync.sh --gc` removes orphaned entries
- [ ] `pointer-sync.sh --rebuild-dir-index` rebuilds directory UUID index
- [x] Atomic write protocol in place for all index mutations
- [x] File locking prevents concurrent index corruption
- [ ] Checksum validation detects corrupt indexes
- [x] All 108 existing tests pass
- [ ] All new UUID tests pass
- [x] `pointer-sync.sh --validate` exits 0 on real repo
- [ ] Entity creation skill generates UUIDs for new entities
- [ ] Entity creation skill creates `.dir-id` for all new directories
- [ ] Documentation updated (entity_structure.md, protocol, convention)
- [x] Post-merge git hook installed and functional
- [x] All changes committed with `[AI Context]` prefix
- [x] Parent/children entity graph in UUID index (Phase 11)
- [x] `--parent`, `--children` CLI commands work (Phase 11)
- [x] `--query` CLI with flexible filtering works (Phase 12)
- [x] Per-entity resource indexes rolled out to 50 entities (Phase 13)
- [x] Root index aggregates 5,381 entries across entities, stages, resources (Phase 13+17)
- [x] Canonical `/uuid-query` skill exists at `.0agnostic/.../05_skills/uuid-query/SKILL.md` (Phase 14)
- [x] Claude Code port exists at `.claude/skills/uuid-query/SKILL.md` (Phase 14)
- [x] SKILLS.md index includes uuid-query (Phase 14)
- [x] Root `0AGNOSTIC.md` has uuid-query trigger and resource entries (Phase 14)
- [x] Trigger text propagated to all generated context files via agnostic-sync.sh (Phase 14)
- [x] All 12 scripts moved from `.0agnostic/` root into `03_protocols/` subdirectories (Phase 16)
- [x] No `.sh` files remain at `.0agnostic/` root (Phase 16)
- [x] All scripts have `resource_id` in their headers (Phase 16)
- [x] Internal ROOT path references updated for new depth (Phase 16)
- [x] Cross-protocol script references use relative path traversal (Phase 16)
- [x] Protocol docs created for uuid_assignment_protocol and agnostic_sync_protocol (Phase 16)
- [x] Git hooks updated with new script paths (Phase 16)
- [x] 81+ documentation files updated with new paths (Phase 16)
- [x] `resolve-uuid` function exists and resolves any UUID → current path in <10ms (Phase 17)
- [x] `resolve-uuid` works from any directory within the repo (Phase 17)
- [ ] `resolve-uuid` works in sandboxed environments (Phase 17)
- [x] Cross-protocol script calls use `resolve-uuid` instead of hardcoded paths (Phase 18)
- [x] Git hooks use `resolve-uuid` to find scripts (Phase 18)
- [x] Same-directory `$SCRIPT_DIR/` references preserved (Phase 18)
- [x] `{{resolve:UUID}}` syntax defined and documented (Phase 19)
- [x] Root `0AGNOSTIC.md` uses `{{resolve:UUID}}` placeholders (Phase 19)
- [ ] trigger_pointer_system `0AGNOSTIC.md` uses `{{resolve:UUID}}` placeholders (Phase 19)
- [x] `agnostic-sync.sh` resolves `{{resolve:UUID}}` placeholders during generation (Phase 20)
- [x] Generated context files contain resolved paths from UUID placeholders (Phase 20)
- [x] Generated context files include resolve-uuid instructions section (Phase 20)
- [x] Unresolvable UUIDs produce "UNRESOLVED:UUID" marker during generation (Phase 20)
- [x] Post-checkout hook runs `--rebuild-index` automatically (Phase 21)
- [x] Pre-commit hook validates UUID references in staged files (Phase 21)
- [x] UUID short-form (8-char prefix) resolves correctly (Phase 22)
- [x] Ambiguous prefixes produce clear error with candidates listed (Phase 22)
- [x] `.uuid-aliases.tsv` exists with all 13 script aliases (Phase 23)
- [x] `resolve-name` function resolves logical names → UUID → path (Phase 23)
- [ ] Move test passes: move script → rebuild → all UUID refs resolve (Phase 24)
- [ ] Self-healing test passes: CLAUDE.md not regenerated, UUID still resolves (Phase 24)
- [ ] Git hook auto-rebuild test passes on fresh checkout (Phase 24)
- [ ] Performance test: <10ms average for resolve-uuid (Phase 24)
