---
resource_id: "1f40a5c5-cebc-42b1-a3f2-56c9cbd91c2d"
resource_type: "output"
resource_name: "uuid_identity_system_design"
---
# Design Proposal: UUID Identity System for Layer-Stage Entities

<!-- section_id: "954bade0-48e4-46cf-9d58-493f6771bed5" -->
## Status: IMPLEMENTED (core phases complete, see Addendum 15 for graph + query extensions)
<!-- section_id: "8f196934-70c1-4cab-a2be-3328663704d4" -->
## Date: 2026-03-02
<!-- section_id: "0c009ec6-14a4-4a2a-a1a1-817c94690c49" -->
## Author: AI Agent (stage_3_04_design)
<!-- section_id: "9c557305-6dc4-4408-aeea-a91bb135de37" -->
## Related Research: `../../../stage_3_02_research/outputs/rename_propagation_research.md`

---

<!-- section_id: "2e31bc9d-ad98-4785-a06a-17fddc22fe62" -->
## 1. Problem Statement

<!-- section_id: "b5e892df-d58d-4846-b951-dd39ed60aa96" -->
### Current Behavior

The pointer-sync.sh system resolves pointer files using **name-based lookup**:

```yaml
canonical_entity: "layer_1_feature_context_chain"
canonical_stage: "stage_2_04_design"
```

Resolution uses `find -type d -name "$CANONICAL_ENTITY"` to locate the entity directory. This works when entities are **moved** (same name, new location) but **breaks completely** when entities are **renamed**.

<!-- section_id: "3da26aa2-dfbe-4020-aaa1-480fa20691fc" -->
### Impact of Renames

When `layer_1_feature_old_name` is renamed to `layer_1_feature_new_name`:
- Every pointer file referencing `canonical_entity: "layer_1_feature_old_name"` becomes BROKEN
- No warning at rename time — breakage is silent
- Discovery happens later when pointer-sync.sh runs and reports BROKEN pointers
- Manual find-and-replace across all pointer files is required

<!-- section_id: "a4ff7559-19ca-4cca-b4a2-b711270ba866" -->
### Why This Matters

- Entity names change as understanding evolves (e.g., renaming a feature to better reflect scope)
- Stage names may be adjusted (e.g., splitting or merging stages)
- The system will grow — more entities means more pointers means more breakage risk
- Cross-layer references are especially fragile (a layer 0 rename affects all layer 1+ pointers)

---

<!-- section_id: "04a31a02-2a5f-42ba-95b6-21f914b788e8" -->
## 2. Proposed Solution: UUID-Based Identity

<!-- section_id: "bb532a6f-945d-45c8-a2a6-c994b1bbd11d" -->
### Core Idea

Assign every entity and every stage a **UUID v4** (random, 128-bit) that:
- Is generated once at creation time
- Never changes, regardless of renames, moves, or restructuring
- Serves as the **primary** resolution key for pointer-sync.sh
- Coexists with human-readable names (which become display-only)

<!-- section_id: "38d541ed-f154-4969-a1a7-af34f2cc89b9" -->
### Why UUID v4 (Random)

| Version | Method | Why Not |
|---------|--------|---------|
| v1 | Timestamp + MAC | Leaks creation time, requires MAC address |
| v3 | MD5 hash of namespace+name | **Breaks on rename** — hash changes when name changes |
| v4 | Random | **Best fit** — no dependency on name, path, or time |
| v5 | SHA-1 hash of namespace+name | Same problem as v3 — deterministic from name |

UUID v4 is the only version where the identifier is completely decoupled from the entity's name or path.

<!-- section_id: "5f468613-5c04-4cd3-92bb-d1953d426976" -->
### Generation

```bash
# Option 1: uuidgen (available on most Linux/macOS)
uuidgen

# Option 2: /proc/sys/kernel/random/uuid (Linux only)
cat /proc/sys/kernel/random/uuid

# Option 3: Python fallback
python3 -c "import uuid; print(uuid.uuid4())"
```

Output format: `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx` (36 chars with hyphens)

---

<!-- section_id: "c945fdff-9fe7-45ee-9884-34125f8a2be1" -->
## 3. Where UUIDs Live

**Fundamental rule**: Every file, every directory, every entity, and every stage within `/home/dawson/dawson-workspace/code/0_layer_universal/` MUST have a universally unique identifier (UUID v4). No exceptions for any file type or directory — only binary files (`.png`, `.woff`, `.wav`, `.db`) are exempt. Empty `.gitkeep` files are replaced by `.dir-id` files (see Section 3.6).

**Scope includes submodules and nested repos**: The UUID requirement extends to ALL content under `0_layer_universal/`, including files and directories inside git submodules (registered in `.gitmodules`) and unregistered nested git repositories. These are separate git repos that require commits within each repo individually, but they are still part of the `0_layer_universal` system and must have full UUID coverage.

| Nested Repo Type | Count | UUID Responsibility |
|-------------------|-------|---------------------|
| Registered submodules (`.gitmodules`) | 9 | Commit inside submodule, update parent pointer |
| Unregistered nested git repos | 8 | Commit inside nested repo (parent tracks as gitlink) |
| **Total nested repos** | **17** | Each gets full file UUID + section UUID coverage |

<!-- section_id: "20a1f739-0100-4145-8762-d5baa7619f7d" -->
### 3.1 Entity UUID — in 0AGNOSTIC.md Identity Section

```yaml
## Identity

entity_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d"

You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: Context Chain System.
- **Role**: ...
- **Scope**: ...
```

The `entity_id` field is added to the **Identity** section of every entity's `0AGNOSTIC.md`. It is:
- Set once at entity creation
- Never modified
- Survives all renames and moves
- Propagated to `CLAUDE.md` (and other tool files) via `agnostic-sync.sh`

<!-- section_id: "e52c7320-fbc4-41c9-9f0e-2c212bf6de65" -->
### 3.2 Stage UUID — in Stage's 0AGNOSTIC.md

Each stage directory that has a `0AGNOSTIC.md` gets its own UUID:

```yaml
## Identity

stage_id: "f7e8d9c0-b1a2-4c3d-e4f5-6a7b8c9d0e1f"

You are the **Stage 04 (Design)** agent for the Context Chain System.
- **Stage Number**: 04
- **Stage Name**: design
```

For stages that don't yet have a `0AGNOSTIC.md` (scaffolded stages), the UUID is assigned when the stage's `0AGNOSTIC.md` is first created.

<!-- section_id: "00bc9e33-6dd1-4437-9651-d0522a024110" -->
### 3.3 Stage Registry — Machine-Readable Index

The existing `stage_N_00_stage_registry/` directory gets a `stage_index.json` mapping all stage UUIDs:

```json
{
  "entity_id": "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
  "entity_name": "layer_2_subx2_feature_context_chain_system",
  "stages": [
    {
      "stage_id": "11111111-aaaa-4bbb-cccc-dddddddddddd",
      "stage_number": "00",
      "stage_name": "stage_registry",
      "directory": "stage_2_00_stage_registry"
    },
    {
      "stage_id": "22222222-aaaa-4bbb-cccc-dddddddddddd",
      "stage_number": "01",
      "stage_name": "request_gathering",
      "directory": "stage_2_01_request_gathering"
    },
    {
      "stage_id": "33333333-aaaa-4bbb-cccc-dddddddddddd",
      "stage_number": "02",
      "stage_name": "research",
      "directory": "stage_2_02_research"
    }
  ]
}
```

This registry is the single source of truth for stage identity within an entity. It enables:
- Fast lookup without scanning the filesystem
- Stage rename tracking (update `stage_name` and `directory`, `stage_id` stays the same)
- Validation that all 12 stages (00-11) exist and have IDs

<!-- section_id: "97ca01dd-47a4-4d62-8590-21935611031b" -->
### 3.4 Pointer Files — Updated YAML Frontmatter

Pointer files reference entities and stages by UUID:

```yaml
---
pointer_to: "Context Chain System Design"
canonical_entity_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d"
canonical_entity_name: "layer_2_subx2_feature_context_chain_system"
canonical_stage_id: "33333333-aaaa-4bbb-cccc-dddddddddddd"
canonical_stage_name: "stage_2_02_research"
canonical_subpath: "outputs/by_topic/architecture/context_chain_architecture.md"
---
```

**Key rules**:
- `canonical_entity_id` is the **primary** resolution field (machine reads this)
- `canonical_entity_name` is **display only** (human reads this, not used for resolution)
- `canonical_stage_id` is the **primary** stage resolution field
- `canonical_stage_name` is **display only**
- `canonical_subpath` remains name-based (file paths within a stage don't get UUIDs in pointer references)
- Old format (`canonical_entity` without `_id`) still works as fallback

<!-- section_id: "b04b8a05-022d-4800-9b3e-05d96c7bca10" -->
### 3.5 File-Level UUIDs — Every File Gets an ID

Every non-binary, non-empty file in `0_layer_universal/` gets a UUID, stored using the comment syntax appropriate to its file type:

| File Type | UUID Field | Storage Method |
|-----------|-----------|----------------|
| `.md`, `.qmd` | `resource_id` | YAML frontmatter |
| `.sh`, `.py`, `.yaml`, `.yml`, `.txt`, `.ini`, `.rules`, `.env`, `.gitignore`, `.csv`, `.template`, `.jq`, `.dot` | `resource_id` | `# comment` header |
| `.js`, `.mjs`, `.jsx`, `.cjs`, `.jsonc`, `.jsonl` | `resource_id` | `// comment` header |
| `.css` | `resource_id` | `/* comment */` header |
| `.html`, `.svg`, `.mermaid` | `resource_id` | `<!-- comment -->` header |
| `.json`, `.jsonld` | `file_id` | JSON root object field |
| `.ps1` | `resource_id` | `# comment` header |
| Auto-generated (CLAUDE.md, AGENTS.md, etc.) | `derived_from` | HTML comment referencing source entity_id |
| Binary (`.png`, `.woff`, `.wav`, `.db`, `.pdf`) | N/A | Exempt — cannot embed text |
| Empty `.gitkeep` files | N/A | Exempt — 0 bytes |

**Coverage achieved**:
- Core repo: 17,340/17,340 text files = 100%
- Submodules + nested repos: ~29,000 files (Phase 1e — see Section 3.8)
- **Total**: ~46,340 text files with UUIDs

**Script**: `assign-file-uuids.sh` handles all types. For edge cases, a Python catch-all script processes remaining files.

<!-- section_id: "f1b87d69-3cbf-4c4b-a169-778871b94129" -->
### 3.6 Directory UUIDs — Every Directory Gets an ID

Every directory within `0_layer_universal/` gets a UUID via a `.dir-id` file placed inside it.

#### Why `.dir-id` Files (Not a Central Registry)

| Approach | Rename Resilience | Move Resilience | Git Clone Survives | Complexity |
|----------|-------------------|-----------------|--------------------|-----------|
| **`.dir-id` file per directory** | **Yes** — file travels with directory | **Yes** — file travels with directory | **Yes** — regular file | Low |
| Central path-based registry | **No** — path key breaks on rename | **No** — path key breaks on move | Yes | Medium |
| Extended attributes (xattr) | Yes | Yes | **No** — not preserved by git | Low |
| Git tree object hashing | N/A (changes on any content change) | N/A | Yes | High |
| Symlink-based tracking | Fragile | Fragile | Partial | High |

**`.dir-id` is the most robust approach** because:
1. The UUID physically **travels with the directory** on rename/move — no external system needed
2. Survives git clone, checkout, merge — it's a regular tracked file
3. A central path-keyed registry has the **same rename-breakage problem** UUIDs were designed to solve
4. `xattr` is eliminated — not preserved by `git clone` or `git checkout`
5. `git diff` does NOT support directory rename detection (only merge/cherry-pick context)

#### `.dir-id` File Format

```
a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d
```

Single line containing only the UUID. No YAML, no comments, no metadata. This keeps the file as simple and robust as possible — any tool can read it with `cat .dir-id`.

#### Replacing `.gitkeep` Files

There are ~39,432 empty `.gitkeep` files in the repo. The `.dir-id` file replaces `.gitkeep` because:
- Git tracks directories only if they contain files. `.gitkeep` exists solely to keep empty dirs in git.
- `.dir-id` serves the same purpose (non-empty file → git tracks the directory) PLUS provides identity.
- Migration: For each directory with an empty `.gitkeep`, remove `.gitkeep` and create `.dir-id` with a UUID.
- For directories that already have files (non-empty), `.dir-id` is added alongside existing content.

#### Directory UUID Index (`.dir-uuid-index.json`)

While `.dir-id` files are the **source of truth**, a central index provides O(1) lookup performance:

```json
{
  "generated": "2026-03-02T10:30:00Z",
  "directories": {
    "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d": {
      "path": "layer_-1_research/layer_0_group/layer_0_01_systems/",
      "name": "layer_0_01_systems"
    }
  }
}
```

**Index is a cache, not a source of truth**:
- Built by scanning all `.dir-id` files: `find . -name .dir-id -exec ...`
- Rebuilt on demand via `pointer-sync.sh --rebuild-dir-index`
- Stale entries are harmless — if a path doesn't exist, skip it and find the `.dir-id` via scan

#### Lazy Resolution (Zero-Intervention Rename Handling)

When a directory UUID lookup fails (UUID not in index, or indexed path doesn't exist):

```
1. Check index for UUID → path
2. If path exists → return path (cache hit)
3. If path doesn't exist OR UUID not in index:
   a. Scan filesystem: find . -name .dir-id -exec grep -l "UUID" {} \;
   b. If found → update index entry with new path, return new path
   c. If not found → directory was deleted, return BROKEN
```

This means **renames and moves are handled automatically** with no hooks, no scripts, no manual intervention. The first lookup after a rename is slower (filesystem scan), but subsequent lookups use the updated cache.

#### Coverage

| Category | Count | Has UUID |
|----------|-------|----------|
| Entity directories (have 0AGNOSTIC.md) | ~366 | Yes (entity_id) |
| Stage registry directories | ~33 | Yes (in stage_index.json) |
| All other directories | ~98,876 | **Pending** (need `.dir-id`) |
| **Total directories** | **~99,275** | Target: 100% |

#### Edge Cases

**Nested `.dir-id` on move**: When a directory containing subdirectories is moved, ALL `.dir-id` files in the subtree travel together. The index becomes stale for all of them, but lazy resolution fixes each on first access.

**`.dir-id` in `.gitignore`?**: NO. `.dir-id` files MUST be tracked by git. They are source-of-truth identity files.

**Merge conflicts in `.dir-id`**: Impossible — each `.dir-id` contains only a UUID unique to that directory. Two branches can't independently create the same directory with different UUIDs unless the directory was created on both branches (in which case, keep either UUID).

<!-- section_id: "3f35fa5b-b1b1-45e7-8b1c-1c3b894fae44" -->
### 3.7 Section-Level UUIDs — Every Section Gets an ID

Section-level UUIDs enable stable references to specific headings within files. When a heading is renamed or sections are reordered, the UUID stays the same.

#### Scope: Which Headings Get UUIDs

| Heading Level | Gets UUID | Rationale |
|--------------|-----------|-----------|
| `#` (h1) | No | File title — file-level `resource_id` already covers this |
| `##` (h2) | **Yes** | Primary structural divisions — most commonly referenced |
| `###` (h3) | **Yes** | Sub-sections within h2 — frequently referenced in design/research docs |
| `####` (h4+) | No | Too granular — diminishing returns, adds noise |

#### Format: HTML Comment Before Heading

```markdown
## Section Heading

### Sub-Section Heading
```

**Why HTML comment above the heading** (not inline or below):
- Stays paired with the heading even when content below changes
- HTML comments are invisible in rendered markdown
- Does not affect heading anchor links (`#section-heading`)
- Easy to parse: line matching `<!-- section_id: "..." -->` followed by `## ` or `### `

#### Pointer Reference Format

Pointers can reference sections by UUID:

```yaml
---
pointer_to: "Migration Plan section of UUID Design"
canonical_entity_id: "a1b2c3d4-..."
canonical_resource_id: "f47ac10b-..."
canonical_section_id: "e5f6a7b8-..."
canonical_section_name: "Migration Plan"
---
```

**Resolution**: `canonical_section_id` resolves to a specific heading within the file identified by `canonical_resource_id`. The section name is display-only.

#### Coverage

| File Type | h2+h3 Sections | Gets Section UUIDs |
|-----------|----------------|-------------------|
| `.md` files (AI context) | ~458,000+ | Yes |
| `.py`, `.js`, `.sh` (code) | N/A (no markdown headings) | No — functions/classes use different patterns |
| `.json`, `.yaml` | N/A | No |

#### Section UUID Index

Section UUIDs are NOT indexed in `.uuid-index.json` (too many entries, would bloat the index). Instead:
- Section UUIDs are resolved by scanning the target file directly
- Since `canonical_resource_id` or `canonical_entity_id` + path already narrows to one file, finding a section within that file is a simple `grep`
- No separate index needed — O(1) file lookup + O(n) line scan within file

#### Edge Cases

**Section deleted**: Pointer references a `canonical_section_id` that no longer exists in the file → BROKEN at section level (file still resolves, but the specific section is gone).

**Section moved to different file**: The section_id travels with the text if copy-pasted, but the `canonical_resource_id` still points to the old file. This is a manual fix — section IDs don't have cross-file tracking.

**Duplicate section_ids within a file**: Should not happen (each section gets a unique UUID). Detection: `assign-section-uuids.sh --validate` checks for duplicates.

**Auto-generated files (CLAUDE.md)**: Do NOT get section UUIDs. They are derived files — sections come from 0AGNOSTIC.md which has the authoritative section IDs.

<!-- section_id: "c7a21e33-4f8b-49d2-b6e1-9a0d3c5f7e82" -->
### 3.8 Submodule & Nested Repo UUIDs

The `0_layer_universal/` system contains 17 nested git repositories (9 registered submodules + 8 unregistered). These are separate repos but part of the same system — they MUST have full UUID coverage.

#### Nested Repo Inventory

| Type | Repository | Approx Files |
|------|-----------|-------------|
| Submodule | `layer_1_project_school` | ~23,700 |
| Submodule | `layer_1_project_physics_simulation` | ~700 |
| Submodule | `layer_1_project_portfolio` | ~80 |
| Submodule | `layer_1_project_parallelism` | ~230 |
| Submodule | `layer_1_project_ds250_course` | ~120 |
| Submodule | `layer_1_project_buying_list` | ~13 |
| Submodule | `layer_1_project_life_administration` | ~23 |
| Submodule | `layer_1_component_setup_hub` | ~14 |
| Submodule | `layer_1_component_dotfiles` | ~9 |
| Nested | `layer_1_project_lang_trak` | ~3,700 |
| Nested | `layer_1_project_central_website` | ~2 |
| Nested | `layer_1_project_internship_prep` | ~74 |
| Nested | `layer_1_project_language_tracker` | ~115 |
| Nested | `layer_1_project_machine_learning` | ~104 |
| Nested | `layer_1_project_web_app` | ~23 |
| Nested | `langtrak_original` | ~461 |
| Nested | `professor` (AALang fork) | ~42 |

#### What Gets Assigned

Each nested repo receives:
1. **File UUIDs** — Same comment-syntax-per-file-type approach as the core repo
2. **Section UUIDs** — `<!-- section_id -->` for h2/h3 headings in .md files (fill gaps)
3. **Directory UUIDs** — Already complete (`.dir-id` files were assigned repo-wide)

#### Commit Strategy

Each nested repo requires its own commit:
1. Process the nested repo (assign file + section UUIDs)
2. Commit inside the nested repo with `[AI Context]` prefix
3. Push the nested repo (if it has a remote)
4. In the parent repo, the submodule pointer automatically updates
5. Commit the parent's updated submodule pointer

#### Edge Cases

**Gitignored files**: Files like `.env`, `firebase-service-account*.json` may be gitignored in the nested repo. UUID assignment still happens on disk, but changes won't be committed.

**Nested repos without remotes**: Some unregistered nested repos may not have a remote. Changes are committed locally only.

**Binary-heavy repos** (e.g., `layer_1_project_school` with ~92K .jpg files): Binary files are exempt. Only text files get UUIDs.

---

<!-- section_id: "a3ac7ef8-c08e-43af-9c9d-bae84578f83e" -->
## 4. Updated Resolution Algorithm

<!-- section_id: "21c7e6d6-56a0-4082-bcb8-4e5166fe6418" -->
### Current Algorithm (Name-Based)

```
1. Extract canonical_entity from frontmatter
2. find -type d -name "$canonical_entity" → entity directory
3. Extract canonical_stage → find within entity directory
4. Append canonical_subpath → full path
5. Compute relative path from pointer to target
```

<!-- section_id: "f75f1145-4a9d-44c9-8d09-f18da3dd5238" -->
### Proposed Algorithm (UUID-First with Name Fallback)

```
1. Extract canonical_entity_id from frontmatter
2. If UUID present:
   a. Search all 0AGNOSTIC.md files for matching entity_id
   b. Cache results in .uuid-index.json for performance
   c. → entity directory
3. If UUID absent (legacy pointer):
   a. Extract canonical_entity (name-based)
   b. find -type d -name "$canonical_entity" → entity directory
   c. Emit deprecation warning: "Pointer uses name-based resolution. Add canonical_entity_id for rename safety."
4. Extract canonical_stage_id from frontmatter
5. If stage UUID present:
   a. Read stage_index.json in entity's stage_N_00_stage_registry/
   b. Look up stage_id → get directory name
   c. → stage directory
6. If stage UUID absent (legacy):
   a. Extract canonical_stage (name-based)
   b. find within entity directory
   c. Emit deprecation warning
7. Append canonical_subpath → full path
8. Compute relative path from pointer to target
```

<!-- section_id: "12e9a4d3-ac64-4dda-925f-ca84d7e283f9" -->
### Performance: Hybrid Index Architecture

Scanning all `0AGNOSTIC.md` files for UUIDs on every run would be slow. Solution: a **hybrid index architecture** — local authoritative indexes per entity, aggregated into a global root index.

#### Root Index (`.uuid-index.json` at ROOT level)

Contains ALL UUIDs across the entire system — entities, stages, and resources:

```json
{
  "generated": "2026-03-02T10:30:00Z",
  "checksum": "sha256:a1b2c3d4...",
  "uuids": {
    "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d": {
      "type": "entity",
      "name": "layer_2_subx2_feature_context_chain_system",
      "path": "/full/path/to/entity"
    },
    "33333333-aaaa-4bbb-cccc-dddddddddddd": {
      "type": "stage",
      "name": "research",
      "entity_id": "a1b2c3d4-...",
      "path": "/full/path/to/entity/layer_2_group/layer_2_99_stages/stage_2_02_research"
    },
    "f47ac10b-58cc-4372-a567-0e02b2c3d479": {
      "type": "resource",
      "name": "pointer_sync_knowledge",
      "entity_id": "a1b2c3d4-...",
      "path": ".0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md"
    }
  },
  "names": {
    "layer_2_subx2_feature_context_chain_system": "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
    "pointer_sync_knowledge": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
  }
}
```

**Key design choices**:
- **Flat `uuids` map**: Any UUID in, one path out — no need to know the type beforehand
- **`names` reverse map**: Name→UUID for fast name-based fallback (O(1) instead of O(n) scanning)
- **`checksum`**: SHA256 of index content for corruption detection on load
- **`type` field**: Distinguishes entity/stage/resource after lookup if needed

#### Local Indexes (per entity)

- `stage_index.json` in `stage_N_00_stage_registry/` — authoritative source for that entity's stages
- `resource_index.json` in `.0agnostic/` — authoritative source for that entity's resources

#### How They Relate

```
Local (authoritative)          Root (aggregated)
─────────────────────          ──────────────────
entity/stage_index.json  ──┐
entity/resource_index.json ──┼──> .uuid-index.json
entity_2/stage_index.json ──┘
```

Root index is **rebuilt from local indexes** — `--rebuild-index` reads all local `stage_index.json` and `resource_index.json` files to produce the global `.uuid-index.json`. This mirrors how databases work: local data files are authoritative, global indexes are derived.

#### Index Behavior

- Rebuilt on `pointer-sync.sh --rebuild-index` or when index is missing
- Auto-rebuilt if a UUID lookup fails (entity may have been created since last index build)
- Optionally rebuilt as part of `agnostic-sync.sh`
- Future: incremental updates instead of full rebuilds (update only changed entities)

#### Index Safety

- **Atomic writes**: Write to temp file → fsync → atomic rename. Never write directly to index files
- **Checksum validation**: On load, compute SHA256 of content and compare to stored `checksum` field. If mismatch → auto-rebuild from local indexes
- **File locking**: Use lockfile (`<index>.lock`) around index mutations to prevent concurrent write corruption
- **Idempotent rebuilds**: Running `--rebuild-index` twice produces identical output — safe to re-run after any suspected corruption

---

<!-- section_id: "09f40e54-a242-4d9c-ad3f-b7a0f964aaa0" -->
## 5. Migration Plan

<!-- section_id: "8441115f-e0a5-4210-8a36-fc4889343bb0" -->
### Phase 1: Assign UUIDs to All Existing Entities (Script)

Create `assign-uuids.sh` that:

1. Finds all `0AGNOSTIC.md` files in the repo
2. Checks if `entity_id:` already exists
3. If missing, generates a UUID v4 and inserts `entity_id: "uuid"` into the Identity section
4. Reports what was added

```bash
#!/bin/bash
# assign-uuids.sh — one-time migration: add entity_id to all 0AGNOSTIC.md files
find "$ROOT" -name "0AGNOSTIC.md" -path "*/layer_*" | while read -r file; do
    if ! grep -q "^entity_id:" "$file"; then
        uuid=$(uuidgen)
        # Insert after "## Identity" line
        sed -i "/^## Identity/a entity_id: \"$uuid\"" "$file"
        echo "Added entity_id $uuid to $file"
    fi
done
```

<!-- section_id: "1168c3b7-1a06-40f8-a70a-53db7244191b" -->
### Phase 2: Assign Stage UUIDs and Create Registries

For each entity with stages:

1. Find all `stage_N_XX_*` directories
2. Generate a UUID for each stage
3. If the stage has a `0AGNOSTIC.md`, insert `stage_id:` into its Identity section
4. Create/update `stage_index.json` in `stage_N_00_stage_registry/`

<!-- section_id: "5c57ef4d-3cd0-4c14-8340-e1b5ab8854b3" -->
### Phase 3: Update pointer-sync.sh

Modify the resolution algorithm to:
1. Try UUID-first resolution (read `canonical_entity_id`, search cache/0AGNOSTIC.md files)
2. Fall back to name-based resolution if no UUID
3. Emit deprecation warnings for name-based pointers
4. Add `--rebuild-index` flag

<!-- section_id: "2237e979-10c0-4137-b4e3-13a2ee1ee452" -->
### Phase 4: Update Entity Creation Skill

Modify `/entity-creation` to:
1. Auto-generate `entity_id` UUID when creating `0AGNOSTIC.md`
2. Auto-generate `stage_id` UUIDs for all 12 stages
3. Create `stage_index.json` in `stage_N_00_stage_registry/`

<!-- section_id: "6e1715d8-a8b3-4b21-91f3-144c4e326705" -->
### Phase 5: Migrate Existing Pointers

Create `migrate-pointers.sh` that:
1. Finds all pointer files (YAML frontmatter with `pointer_to:`)
2. For each pointer with `canonical_entity:` but no `canonical_entity_id:`:
   a. Look up the entity name in the UUID cache
   b. Add `canonical_entity_id:` and `canonical_entity_name:` fields
   c. Optionally remove the old `canonical_entity:` field (or keep for readability)
3. Same for `canonical_stage:` → `canonical_stage_id:` + `canonical_stage_name:`

<!-- section_id: "a18f60bb-666b-4826-9f6f-52d07d7f6557" -->
### Phase 6: Run agnostic-sync.sh

Regenerate all CLAUDE.md files so they include the `entity_id` from 0AGNOSTIC.md.

---

<!-- section_id: "6aefb236-5df6-464c-847c-8ea07b672542" -->
## 6. Impact on Existing Tools

<!-- section_id: "541f4984-5e96-4de6-9659-78efd356b9a0" -->
### pointer-sync.sh

| Component | Change |
|-----------|--------|
| `extract_fm()` | Add extraction of `canonical_entity_id`, `canonical_stage_id` |
| Entity resolution | UUID-first lookup (cache → scan), name fallback |
| Stage resolution | Registry lookup by `stage_id`, then name fallback |
| New flag: `--rebuild-index` | Rebuild `.uuid-index.json` |
| Output | Show UUID in verbose mode, deprecation warnings for name-based |

<!-- section_id: "1c1e560c-df18-40ad-a3e7-ec20139aa4dd" -->
### entity-creation skill (SKILL.md)

| Component | Change |
|-----------|--------|
| 0AGNOSTIC.md template | Add `entity_id: "UUID"` to Identity section |
| Stage creation loop | Generate UUID per stage, insert into stage 0AGNOSTIC.md |
| Stage registry | Create `stage_index.json` with all stage UUIDs |

<!-- section_id: "5b2dca89-dc85-4eea-8a46-174ab061e7f6" -->
### agnostic-sync.sh

| Component | Change |
|-----------|--------|
| CLAUDE.md generation | Pass through `entity_id` from 0AGNOSTIC.md to generated files |
| No other changes needed | entity_id is just another field in the Identity section |

<!-- section_id: "4d3414a0-f5e0-4785-b535-add370af60f1" -->
### entity_structure.md (canonical reference)

| Component | Change |
|-----------|--------|
| 0AGNOSTIC.md spec | Document `entity_id` as required field |
| Stage 0AGNOSTIC.md | Document `stage_id` as required field |
| stage_N_00_stage_registry | Document `stage_index.json` format |
| Pointer file spec | Document `canonical_entity_id` and `canonical_stage_id` fields |

---

<!-- section_id: "9f7c0248-cc5d-46ae-93d9-e9b290114b4d" -->
## 7. Edge Cases

<!-- section_id: "cc1c4cde-6971-43da-887e-92f96c7ce775" -->
### 7.1 Duplicate Entity Names

**Problem**: Two entities named `layer_1_feature_auth` in different locations.
**Before (name-based)**: `find -type d -name` returns first match — ambiguous.
**After (UUID-based)**: Each has a unique UUID. No ambiguity. Pointers reference the exact entity they intend.

<!-- section_id: "f2512263-3a4c-42e2-a83b-f25589d0bc47" -->
### 7.2 Cross-Layer References

**Problem**: A layer 1 pointer references a layer 0 entity. Layer 0 entity gets renamed.
**Before**: Pointer breaks silently.
**After**: UUID doesn't change. Pointer still resolves.

<!-- section_id: "a4d0a655-89de-4d56-b815-3f6521ca2be2" -->
### 7.3 Orphaned UUIDs

**Problem**: An entity is deleted but pointers still reference its UUID.
**Behavior**: Same as today — pointer reports BROKEN. The UUID just makes it clearer which entity was intended (the UUID can be searched in git history).
**Mitigation**: `pointer-sync.sh --validate` already catches broken pointers.

<!-- section_id: "b6e8c7f8-a4f7-461c-b4c6-11015a6db41b" -->
### 7.4 Subpath Changes

**Problem**: Files within a stage are renamed/moved.
**Behavior**: Every `.md` file that could be a pointer target gets a `resource_id` in its YAML frontmatter — including output files. When `canonical_resource_id` is present in a pointer, the file can be renamed freely and the pointer still resolves via UUID.
**Fallback**: `canonical_subpath` is kept as a display-only field (like `canonical_entity_name`). If no `canonical_resource_id` is present, subpath resolution falls back to name-based.
**Principle**: Every referenceable thing gets an ID — same as primary keys in a database. This eliminates the entire class of rename-breaks-reference problems.

<!-- section_id: "4d78ae91-d6a9-491b-99c9-3b8857917ef5" -->
### 7.5 UUID Collision

**Probability**: UUID v4 has 122 random bits. Collision probability with 1000 entities: ~2.7 × 10^-31. Negligible.

<!-- section_id: "e0f8689a-a31c-4b55-9e5e-d33f380d1e8e" -->
### 7.6 Merging Entities

**Problem**: Two entities are merged into one. Which UUID survives?
**Decision**: The absorbing entity keeps its UUID. The absorbed entity's UUID is added to a `previous_ids` list for backward compatibility:

```yaml
entity_id: "surviving-uuid"
previous_ids:
  - "absorbed-uuid-1"
  - "absorbed-uuid-2"
```

<!-- section_id: "ada77794-1c84-41c6-a452-f714212fc867" -->
### 7.7 Stage Without 0AGNOSTIC.md

**Problem**: Scaffolded stages don't have `0AGNOSTIC.md` yet.
**Solution**: The stage's UUID still exists in `stage_index.json`. When the stage's `0AGNOSTIC.md` is eventually created, the UUID from the registry is inserted into it. The registry is the source of truth for stage identity, the stage's `0AGNOSTIC.md` mirrors it.

---

<!-- section_id: "62ff95cb-e568-4bdb-9277-934e4008b5e3" -->
## 8. Before/After Examples

<!-- section_id: "f99c9b15-d9d3-412e-b7c8-b97ed6f07385" -->
### Example 1: Simple Entity Pointer

**Before (name-based)**:
```yaml
---
pointer_to: "Context Chain Architecture"
canonical_entity: "layer_2_subx2_feature_context_chain_system"
canonical_stage: "stage_2_02_research"
canonical_subpath: "outputs/by_topic/architecture/context_chain_architecture.md"
---
```

**After (UUID-based)**:
```yaml
---
pointer_to: "Context Chain Architecture"
canonical_entity_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d"
canonical_entity_name: "layer_2_subx2_feature_context_chain_system"
canonical_stage_id: "33333333-aaaa-4bbb-cccc-dddddddddddd"
canonical_stage_name: "stage_2_02_research"
canonical_subpath: "outputs/by_topic/architecture/context_chain_architecture.md"
---
```

**What happens on rename**: Entity renamed to `layer_2_subx2_feature_chain_system`. The `canonical_entity_name` becomes stale but `canonical_entity_id` still resolves correctly. A future `pointer-sync.sh` run can optionally update the display name.

<!-- section_id: "48c356f6-abeb-45af-b08b-ca76e5299de3" -->
### Example 2: Entity 0AGNOSTIC.md Identity Section

**Before**:
```markdown
## Identity

You are the **Context Chain System Manager** at **Layer 2** (Sub-Feature).
- **Role**: Manager of the context chain system
- **Scope**: ...
- **Parent**: `../../../0AGNOSTIC.md`
```

**After**:
```markdown
## Identity

entity_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d"

You are the **Context Chain System Manager** at **Layer 2** (Sub-Feature).
- **Role**: Manager of the context chain system
- **Scope**: ...
- **Parent**: `../../../0AGNOSTIC.md`
```

<!-- section_id: "5d6f0175-b3e8-463b-8b56-22d850f3e031" -->
### Example 3: Stage 0AGNOSTIC.md Identity Section

**Before**:
```markdown
## Identity

You are the **Stage 04 (Design)** agent for the Context Chain System.
```

**After**:
```markdown
## Identity

stage_id: "44444444-aaaa-4bbb-cccc-dddddddddddd"

You are the **Stage 04 (Design)** agent for the Context Chain System.
```

<!-- section_id: "14aa0d1a-a78f-4f14-a9a6-78e289df2e60" -->
### Example 4: Stage Registry (stage_index.json)

**New file** at `stage_2_00_stage_registry/stage_index.json`:
```json
{
  "entity_id": "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
  "entity_name": "layer_2_subx2_feature_context_chain_system",
  "stages": [
    {
      "stage_id": "11111111-aaaa-4bbb-cccc-dddddddddddd",
      "stage_number": "00",
      "stage_name": "stage_registry",
      "directory": "stage_2_00_stage_registry"
    },
    {
      "stage_id": "22222222-aaaa-4bbb-cccc-dddddddddddd",
      "stage_number": "01",
      "stage_name": "request_gathering",
      "directory": "stage_2_01_request_gathering"
    }
  ]
}
```

---

<!-- section_id: "95a97c2e-5ce7-4456-b7e1-5cdaf1bb4a6a" -->
## 9. Implementation Priority

| Phase | What | Effort | Risk | Prerequisite |
|-------|------|--------|------|--------------|
| 1 | `assign-uuids.sh` — add entity_id to all 0AGNOSTIC.md | 2-3 hours | Low | None |
| 2 | Stage UUIDs + stage_index.json | 3-4 hours | Low | Phase 1 |
| 3 | Update pointer-sync.sh for UUID resolution | 4-6 hours | Medium | Phase 1-2 |
| 4 | Update entity-creation skill | 2-3 hours | Low | Phase 1-2 |
| 5 | Migrate existing pointers | 2-3 hours | Low | Phase 3 |
| 6 | Update entity_structure.md canonical reference | 1 hour | Low | Phase 1-4 |

**Total estimated effort**: ~15-20 hours across phases.

**Recommended order**: Phase 1 → 2 → 4 → 3 → 5 → 6. Entity creation skill (Phase 4) can be done in parallel with pointer-sync.sh updates (Phase 3).

---

<!-- section_id: "17d0c1fa-1b74-4122-a07d-54dccb785f5c" -->
## 10. Open Questions

1. **Should `canonical_entity` (old field) be removed or kept?** Recommendation: keep during migration, remove after all pointers are migrated.
2. **Should the cache be git-tracked or .gitignored?** Recommendation: .gitignored (it's a build artifact).
3. **Should `previous_ids` be supported from day 1?** Recommendation: defer until an actual merge occurs.
4. **~~Should subpaths eventually get IDs too?~~** RESOLVED: Yes — every referenceable `.md` file gets a `resource_id` in YAML frontmatter (see Section 11). This includes output files, knowledge docs, rules, protocols, and skills.

---

---

<!-- section_id: "9c30a471-4b85-4162-a432-0147b7aa33ca" -->
## 11. Addendum: Universal Resource IDs (Expanded Scope)

<!-- section_id: "8343d6aa-0968-4b0c-912d-2fd969a3d2a0" -->
### Rationale

The original design covers entities and stages. However, **anything that can be pointed to or referenced** should have a stable ID. This includes `.0agnostic/` resources that participate in the deduplication pattern (pointer files redirect to canonical locations). When a knowledge doc, rule, or protocol is renamed, pointers to it break — the same problem as entity renames.

<!-- section_id: "0a56d48e-cbf5-4e51-bed0-ad4d5d6ae6c0" -->
### Resource Types That Get IDs

| Resource Type | ID Field | Where It Lives | Example |
|---------------|----------|----------------|---------|
| **Entity** | `entity_id` | `0AGNOSTIC.md` Identity section | `entity_id: "a1b2c3d4-..."` |
| **Stage** | `stage_id` | Stage's `0AGNOSTIC.md` + `stage_index.json` | `stage_id: "e5f6a7b8-..."` |
| **Knowledge doc** | `resource_id` | YAML frontmatter at top of `.md` file | `resource_id: "k1k2k3k4-..."` |
| **Rule** | `resource_id` | YAML frontmatter at top of rule `.md` | `resource_id: "r1r2r3r4-..."` |
| **Protocol** | `resource_id` | YAML frontmatter at top of protocol `.md` | `resource_id: "p1p2p3p4-..."` |
| **Skill** | `resource_id` | YAML frontmatter in `SKILL.md` | `resource_id: "s1s2s3s4-..."` |
| **Output file** | `resource_id` | YAML frontmatter at top of output `.md` | `resource_id: "o1o2o3o4-..."` |

<!-- section_id: "c28e91e4-a7a3-414e-b17f-9f38348ab676" -->
### Resource ID Format

All resources use the same `resource_id` field name (unified, not type-specific) with UUID v4:

```yaml
---
resource_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
resource_type: "knowledge"
resource_name: "pointer_sync_knowledge"
---
# Pointer Sync Knowledge
...
```

<!-- section_id: "68a2de07-52f6-4946-808e-86cf1b8a408a" -->
### Updated Pointer Format (Full)

Pointers can now reference any resource by ID:

```yaml
---
pointer_to: "Pointer Sync Knowledge"
canonical_entity_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d"
canonical_entity_name: "layer_3_subx3_feature_trigger_pointer_system"
canonical_stage_id: "33333333-aaaa-4bbb-cccc-dddddddddddd"
canonical_stage_name: "stage_3_02_research"
canonical_subpath: "outputs/by_topic/architecture.md"
canonical_resource_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
canonical_resource_name: "pointer_sync_knowledge"
---
```

**Resolution order**: `canonical_resource_id` (if present, resolves directly to the file) → `canonical_entity_id` + `canonical_stage_id` + `canonical_subpath` (composed path) → name-based fallback.

<!-- section_id: "335339bf-a6aa-47d0-b2cd-cdffb7561396" -->
### Where Files Get IDs — Every File

```
.0agnostic/
├── 01_knowledge/
│   ├── pointer_sync/
│   │   └── pointer_sync_knowledge.md    ← resource_id in YAML frontmatter
│   ├── deduplication_pattern.md          ← resource_id in YAML frontmatter
│   └── layer_stage_system/
│       └── LAYERS_EXPLAINED.md           ← resource_id in YAML frontmatter
├── 02_rules/
│   ├── static/
│   │   └── pointer_sync_rule/
│   │       └── pointer_sync_rule.md      ← resource_id in YAML frontmatter
│   └── dynamic/
│       └── auto_trigger_rule/
│           └── auto_trigger_rule.md      ← resource_id in YAML frontmatter
├── 03_protocols/
│   └── pointer_sync_protocol.md          ← resource_id in YAML frontmatter
├── pointer-sync.sh                       ← resource_id in comment header
├── resource_index.json                   ← file_id in JSON root
└── agnostic-sync.sh                      ← resource_id in comment header

# Root level
├── 0AGNOSTIC.md                          ← entity_id in Identity section
├── 0INDEX.md                             ← resource_id in YAML frontmatter
├── README.md                             ← resource_id in YAML frontmatter
├── CLAUDE.md                             ← derived_from (source entity_id)
├── layer_2_orchestrator.gab.jsonld       ← file_id in JSON
└── layer_2_orchestrator.integration.md   ← derived_from (source file_id)
```

<!-- section_id: "36824e47-b789-4aa2-ab08-428aba346ad5" -->
### Resource Registry

Each entity's `.0agnostic/` gets a `resource_index.json`:

```json
{
  "entity_id": "a1b2c3d4-...",
  "resources": [
    {
      "resource_id": "f47ac10b-...",
      "resource_type": "knowledge",
      "resource_name": "pointer_sync_knowledge",
      "path": "01_knowledge/pointer_sync/pointer_sync_knowledge.md"
    },
    {
      "resource_id": "b2c3d4e5-...",
      "resource_type": "rule",
      "resource_name": "pointer_sync_rule",
      "path": "02_rules/static/pointer_sync_rule/pointer_sync_rule.md"
    }
  ]
}
```

<!-- section_id: "50fdf838-d34d-4db6-9e69-3e0737e56b36" -->
### Universal File IDs — Every File Gets a UUID

**Design principle**: Every file in the AI system gets an ID. No exceptions. This eliminates ambiguity ("does this file have an ID?"), future-proofs against any file becoming a reference target, and enables stable cross-tool addressing.

#### ID Storage by File Type

| File Type | ID Field | Storage Method | Example |
|-----------|----------|---------------|---------|
| `.md` files | `resource_id` | YAML frontmatter (`---`) | `resource_id: "uuid"` |
| `.sh` scripts | `resource_id` | Comment header | `# resource_id: "uuid"` |
| `.json` files | `file_id` | JSON field | `"file_id": "uuid"` |
| `.jsonld` files | `file_id` | JSON field | `"file_id": "uuid"` |
| Auto-generated files | `derived_from` | Reference to source file's UUID | `derived_from: "source-uuid"` |

#### Previously Excluded Files — Now Included

| File Type | ID Field | Notes |
|-----------|----------|-------|
| Scripts (`.sh`) | `resource_id` in comment header | `# resource_id: "uuid"` after shebang |
| `CLAUDE.md`, `.integration.md` | `derived_from` | Points to source file's UUID — not an independent ID |
| `.1merge/` files | `resource_id` | Independent ID per override file |
| `0INDEX.md` | `resource_id` | YAML frontmatter |
| `README.md` | `resource_id` | YAML frontmatter |
| `.gab.jsonld` files | `file_id` | JSON field in the top-level object |
| `stage_index.json` | `file_id` | JSON field in the root object |
| `resource_index.json` | `file_id` | JSON field in the root object |

#### Auto-Generated Files: Derived Identity

Auto-generated files (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `OPENAI.md`, `.integration.md`) do NOT get independent UUIDs. Instead, they carry a `derived_from` field pointing to their source file's UUID:

```markdown
<!-- derived_from: "a1b2c3d4-..." -->
<!-- This file is auto-generated from 0AGNOSTIC.md. Do not edit directly. -->
```

This means:
- The source file (`0AGNOSTIC.md`) has the authoritative `entity_id`
- Generated files reference the source's ID
- If the source is deleted, generated files are also deleted (they have no independent identity)

#### Script ID Format

Scripts get their UUID in a comment immediately after the shebang:

```bash
#!/bin/bash
# resource_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
# resource_type: "script"
# resource_name: "pointer-sync"

# pointer-sync.sh — ...
```

#### JSON File ID Format

JSON files get a `file_id` at the root level:

```json
{
  "file_id": "99999999-aaaa-4bbb-cccc-dddddddddddd",
  "entity_id": "a1b2c3d4-...",
  "stages": [...]
}
```

<!-- section_id: "547b2643-a42a-4f97-af75-b4e868d420a5" -->
### Migration Impact

The Phase 1-6 migration plan expands to include:
- **Phase 1b**: Assign `resource_id` to ALL `.md` files (knowledge, rules, protocols, outputs, README, 0INDEX)
- **Phase 1c**: Assign `resource_id` to ALL `.sh` scripts (comment header format)
- **Phase 1d**: Assign `file_id` to ALL `.json` and `.jsonld` files
- **Phase 1e**: Add `derived_from` to ALL auto-generated files
- **Phase 2b**: Assign `resource_id` to resources in entity-level `.0agnostic/` dirs
- **Phase 5b**: Migrate pointer files that reference resources (add `canonical_resource_id`)

---

<!-- section_id: "8c3ee180-d1cd-4f03-80f9-51d7483d2444" -->
## 12. Database Paradigm Analysis

The layer-stage hierarchy is functionally a **filesystem-backed database**. Comparing against all major database paradigms reveals which patterns we're using and validates the UUID design.

<!-- section_id: "e18766d5-c1d4-4efb-84a8-f9013b4dfa1c" -->
### Similarity Ranking

| Rank | Database Type | Overlap | Why |
|------|--------------|---------|-----|
| 1 | **Document DB** (MongoDB, CouchDB) | Highest | Self-contained entities with embedded resources, materialized views, two-level indexes |
| 2 | **Hierarchical DB** (IBM IMS) | Very high | Tree structure, parent-child ownership, path-based traversal |
| 3 | **Graph DB** (Neo4j) | Moderate | Pointer files create a reference graph across entities |
| 4 | **Object DB** | Moderate | Encapsulated entities with identity and state |
| 5 | **Key-Value** (Redis) | Low | UUID index is a key-value lookup (one component) |
| 6 | **Relational DB** (PostgreSQL) | Lowest | Normalization would destroy self-contained design |

<!-- section_id: "5084e850-9e93-4a74-af4e-e9fabde179f9" -->
### Key Document DB Parallels

| Document DB Concept | Layer-Stage Equivalent |
|---|---|
| **Document** | Entity directory + `0AGNOSTIC.md` |
| **Document ID** (`_id`) | `entity_id` UUID |
| **Embedded subdocument** | `.0agnostic/` resources |
| **Collection** | `layer_N_group/` directory |
| **Per-collection index** | Local `stage_index.json`, `resource_index.json` |
| **Global index** | Root `.uuid-index.json` (aggregated from locals) |
| **Schema / validation** | `entity_structure.md` |
| **Materialized view** | `CLAUDE.md` (auto-generated from `0AGNOSTIC.md`) |

<!-- section_id: "fe4a9344-718d-4f4c-8963-296267250694" -->
### Why Document DB Wins Over Hierarchical DB

Both have high overlap, but the **self-contained entity** pattern is the most defining characteristic. Hierarchical DBs organize by tree structure (which we also do) but don't emphasize data locality — each entity carrying its own resources, indexes, and identity is fundamentally document-oriented. Hierarchical DBs also lack cross-tree references (our pointer files link across branches).

Full research: `../../../stage_3_02_research/outputs/uuid_and_database_patterns_research.md`

---

<!-- section_id: "d87fd77e-a2c1-4183-8ddd-c49027313d50" -->
## 13. Reference Integrity

<!-- section_id: "72c170a0-823b-42dc-b421-5474253f359a" -->
### 13.1 Dangling References

A **dangling reference** occurs when a pointer file references a UUID that no longer exists (entity deleted, resource removed).

**Detection**: `pointer-sync.sh --validate` scans all pointer files and checks each `canonical_entity_id`, `canonical_stage_id`, and `canonical_resource_id` against the UUID index. Any UUID not found → BROKEN.

**Prevention**:
- Before deleting an entity, run `pointer-sync.sh --find-references <uuid>` to find all pointers referencing it
- Display warning: "N pointer files reference this entity. Delete anyway?"
- After deletion, re-run `--validate` to confirm no new BROKEN pointers

**Recovery**:
- BROKEN pointers fall back to name-based resolution (if `canonical_entity_name` still matches)
- If name-based also fails → pointer is truly broken, requires manual fix

<!-- section_id: "80f550db-7d71-4743-beca-91fe8d159ee4" -->
### 13.2 Cascading Operations

**Policy**: No automatic cascading deletes. Deleting an entity does NOT automatically delete pointers to it.

**Rationale**: Cascading deletes are dangerous in a filesystem — accidental deletion of a widely-referenced entity could destroy dozens of pointer files. Better to leave dangling references and fix them explicitly.

**Soft delete pattern** (recommended):
1. Mark entity as deleted by adding `deleted: true` to its `0AGNOSTIC.md` Identity section
2. `--validate` flags pointers to soft-deleted entities as WARN (not BROKEN)
3. After grace period (or explicit confirmation), physically delete the entity directory
4. Run `--rebuild-index` to remove from UUID index

<!-- section_id: "6ed07f38-747f-45c0-b695-cec76251aca2" -->
### 13.3 Circular References

**Policy**: Circular references are **allowed** but detectable.

**Rationale**: In a context hierarchy, circular references can be legitimate (entity A references entity B's research, entity B references entity A's design). Forbidding them would be too restrictive.

**Detection**: `pointer-sync.sh --detect-cycles` builds a directed graph from all pointer files and reports any cycles found. This is informational — cycles are logged but not treated as errors.

**When cycles matter**: If a future tool needs to traverse references recursively (e.g., "find all transitive dependencies"), it must implement cycle detection with a visited set to avoid infinite loops.

<!-- section_id: "86ebb16e-72c7-4260-9c97-fc407537a4df" -->
### 13.4 Orphaned UUIDs

An **orphaned UUID** is an entry in the UUID index that points to a path that no longer exists.

**Detection**: `pointer-sync.sh --gc` (garbage collection) scans the UUID index and checks that every path still exists on the filesystem. Missing paths → remove from index.

**Causes**:
- Entity directory deleted without running `--rebuild-index`
- File moved or renamed without updating its `resource_id`
- Git branch merge where one branch deleted an entity

**Recovery**: `--gc` removes orphaned entries. `--rebuild-index` is the nuclear option — rebuilds from scratch.

<!-- section_id: "82be01e7-0632-423e-a319-e23db40b829b" -->
### 13.5 Duplicate UUIDs

Two entities/resources should never share the same UUID. UUID v4 collision probability is near-zero, but copy-paste errors can create duplicates.

**Detection**: `--rebuild-index` checks for duplicate UUIDs during aggregation. If two entities have the same `entity_id`, it reports an error and keeps the first one found (alphabetically by path).

**Prevention**: UUID assignment scripts check for existing UUIDs before inserting a new one.

---

<!-- section_id: "ef591e6b-01cc-464e-a9c8-1d9a2307efc0" -->
## 14. Failure Modes & Recovery

<!-- section_id: "42a8aa8d-3184-46d7-a523-1d0ce15ebd2d" -->
### 14.1 Index Corruption

| Failure | Cause | Detection | Recovery |
|---------|-------|-----------|----------|
| Partial JSON | Crash during index write | JSON parse fails on load | Auto-rebuild from local indexes |
| Stale entries | Entity moved, index not updated | UUID lookup succeeds but path doesn't exist | Remove stale entry, re-scan for UUID |
| Missing index file | Accidental deletion, new clone | File not found on first lookup | Auto-rebuild triggered |
| Checksum mismatch | Bit rot, manual edit, partial write | SHA256 doesn't match on load | Auto-rebuild from local indexes |

**Recovery priority**: Always rebuild from local indexes (authoritative) → root index (derived). Never rebuild local from root.

<!-- section_id: "a257e4ec-e5ad-4f9a-ae3a-cde5b3ba06d1" -->
### 14.2 Atomic Write Protocol

All index file writes MUST follow this protocol:

```bash
# 1. Write to temp file
temp_file="${index_file}.tmp.$$"
echo "$new_content" > "$temp_file"

# 2. Sync to disk
sync "$temp_file"

# 3. Atomic rename (overwrites old file)
mv "$temp_file" "$index_file"
```

This ensures the index file is always either the old version or the new version — never a partial write.

<!-- section_id: "2644220a-ee32-4ddb-8cef-c6af6d76991e" -->
### 14.3 Concurrent Access

**Problem**: Multiple AI agents may run `pointer-sync.sh` or `--rebuild-index` simultaneously.

**Solution**: File-based locking.

```bash
lockfile="${index_file}.lock"

# Acquire lock (wait up to 30 seconds)
if ! mkdir "$lockfile" 2>/dev/null; then
    # Lock exists — check if stale (older than 5 minutes)
    if [[ $(find "$lockfile" -maxdepth 0 -mmin +5 2>/dev/null) ]]; then
        rm -rf "$lockfile"
        mkdir "$lockfile"
    else
        echo "Index locked by another process. Waiting..."
        # Retry loop with timeout
    fi
fi

# ... do index work ...

# Release lock
rm -rf "$lockfile"
```

**Why `mkdir`**: `mkdir` is atomic on all filesystems — it either succeeds or fails, never creates a partial lock.

<!-- section_id: "001da772-75c1-4314-94fe-8ab4cc59f431" -->
### 14.4 Materialized View Staleness

**Problem**: `0AGNOSTIC.md` is edited but `agnostic-sync.sh` is not run → `CLAUDE.md` is stale.

**Detection**: Store hash of source file in the generated view:
```
<!-- source-hash: sha256:abc123... -->
```

A validation tool can compare the stored hash against the current `0AGNOSTIC.md` hash. Mismatch → view is stale.

**Prevention**: Git hooks can run `agnostic-sync.sh` on commit if any `0AGNOSTIC.md` file changed.

<!-- section_id: "11db3a39-11bd-42a7-b9a8-fab733ca7ea6" -->
### 14.5 Git Branch Merge Conflicts

**Scenario**: Branch A adds entity X with UUID `aaa`. Branch B deletes entity Y with UUID `bbb`. Branch A has a pointer to entity Y. On merge:
- Entity Y is gone (deleted in B)
- Pointer to `bbb` is dangling (added in A)

**Solution**: Post-merge validation.

```bash
# After any git merge
pointer-sync.sh --validate
pointer-sync.sh --gc
```

Add to `.git/hooks/post-merge`:
```bash
#!/bin/bash
pointer-sync.sh --rebuild-index
pointer-sync.sh --validate
```

<!-- section_id: "79b1cf09-0c80-4309-8305-d8dea1b672d4" -->
### 14.6 Performance at Scale

| Scale | Entity Count | UUID Count | Index Size | Rebuild Time |
|-------|-------------|-----------|------------|-------------|
| Small | <100 | <1,000 | <100KB | <1 second |
| Medium | 100-1,000 | 1K-10K | 100KB-1MB | 1-10 seconds |
| Large | 1,000-10,000 | 10K-100K | 1-10MB | 10-60 seconds |
| Very Large | 10,000+ | 100K+ | 10MB+ | Minutes |

**Mitigation strategies**:
- **Incremental index updates** (Phase 2): Only rebuild portions where local indexes changed
- **Name→UUID reverse map** in root index: Eliminates O(n) scanning for name-based fallback
- **Binary index format** (future): msgpack or protobuf instead of JSON if parsing becomes bottleneck
- **Parallel scanning**: Scan multiple entity directories concurrently during rebuild

<!-- section_id: "11e67891-17da-46d6-80d7-2b9c862a4090" -->
### 14.7 Observability

All UUID operations should produce structured log output:

```
[pointer-sync] RESOLVE entity_id=a1b2c3d4 → path=/full/path result=OK
[pointer-sync] RESOLVE entity_id=deadbeef → result=BROKEN (not in index)
[pointer-sync] REBUILD index entries=1234 duration=2.3s
[pointer-sync] GC removed=5 orphaned_uuids
[pointer-sync] VALIDATE total=89 ok=87 broken=1 warn=1
```

This enables:
- Debugging reference resolution failures
- Tracking index rebuild frequency and duration
- Detecting patterns (frequently broken pointers → systemic issue)

<!-- section_id: "d7a762ed-828a-41f6-92b5-c3aa2494f1d1" -->
### 14.8 Chaos Testing

Recommended chaos tests for the UUID system:

| Test | What It Does | Expected Result |
|------|-------------|-----------------|
| Delete random entity, run `--validate` | Simulates accidental deletion | Pointers to it flagged BROKEN, no crash |
| Corrupt `.uuid-index.json` (truncate), run any UUID operation | Simulates crash during write | Auto-rebuild, operation succeeds |
| Run `--rebuild-index` from two processes simultaneously | Simulates concurrent access | Lock prevents corruption, both complete |
| Delete `.uuid-index.json` entirely | Simulates fresh clone | Auto-rebuild on first UUID lookup |
| Create two entities with same UUID (manual) | Simulates copy-paste error | `--rebuild-index` reports duplicate, keeps first |
| Rename entity directory, run `--validate` | Simulates rename without migration | UUID resolves to old path (stale), name fallback finds new path |

---

<!-- section_id: "3fe8772e-1285-4d36-8d52-2c42396ebf03" -->
## 15. Addendum: Parent/Children Graph & Query CLI (2026-03-06)

The core UUID identity system design (Sections 1-14) has been extended with graph traversal and query capabilities. These are documented in a separate design doc:

**Full design**: `uuid_graph_and_query_design.md` (same directory)

### Summary of Extensions

| Extension | Section in New Doc | Status |
|-----------|-------------------|--------|
| Parent/children entity graph | Section 2 | IMPLEMENTED |
| Query CLI with flexible filters | Section 3 | IMPLEMENTED |
| Per-entity resource indexes | Section 4 | IMPLEMENTED (50 entities) |
| Index as document database | Section 5 | Architectural analysis |

### Key Metrics After Extensions

| Metric | Value |
|--------|-------|
| Total UUID index entries | 5,313 |
| Entities with parent links | 122 / 351 |
| Entities with children | 34 |
| Resource indexes generated | 50 |
| Index load time | ~3ms |
| Query execution | <100ms |

---

<!-- section_id: "4ae9f3b7-c0d2-4e5f-8a1b-3c5d7e9f1a2b" -->
## 16. Addendum: Agent Interaction Layer & Concurrency Architecture (2026-03-06)

The UUID system's value depends on how effectively agents can use it. This addendum documents the design decision for agent-facing interfaces and future concurrency architecture.

### Agent Interface Decision

**Decision**: Agents interact via **bash + Claude Code skills**, not SQL or custom MCP tools.

**Evidence**: Vercel's production experiment showed filesystem+bash agents are 3.5x faster, use 37% fewer tokens, and achieve 100% success rates compared to custom-tooled equivalents. This aligns with the harness engineering principle: agents perform best with interfaces they were pretrained on.

**Implementation**: A `/uuid-query` skill teaches agents the pointer-sync.sh CLI commands. Zero prompt overhead until invoked. See `uuid_graph_and_query_design.md` Section 6 for full design.

### Concurrency Upgrade Path

**Current**: JSON file + mkdir locking (sufficient for single-agent, read-heavy workload)

**Future**: SQLite backend behind the same CLI interface (virtual filesystem pattern). Triggers: 50K+ entries, 3+ concurrent write agents, or >500ms query latency. See `uuid_graph_and_query_design.md` Section 7 for schema design.

**Full research**: `../../../stage_3_02_research/outputs/uuid_and_database_patterns_research.md` Sections 8-10

---

<!-- section_id: "5bf9a3c1-d2e4-4f6a-8b7c-9d0e1f2a3b4c" -->
## 17. Addendum: Advanced Infrastructure Layer & Hybrid Knowledge Architecture (2026-03-06)

The UUID identity system's infrastructure layer can be extended with sophisticated knowledge representations without changing the agent-facing interface (Addendum 16).

### Two-Layer Architecture Principle

**Interface layer** (Addendum 16): Bash + skills + virtual filesystem. Agent performance depends on this layer (3.5x speed improvement, 37% fewer tokens). MUST use familiar tools. NEVER changes.

**Infrastructure layer** (this addendum): Backend data stores. Agent performance is NOT affected by this layer (LLM computation is 87-99.9% of execution time). Choose based on functionality needs, not agent performance.

### Hybrid Knowledge Capabilities

The infrastructure layer can combine four data representation types, all behind the unchanged pointer-sync.sh CLI:

| Capability | Technology | Query Example | When Needed |
|-----------|-----------|---------------|-------------|
| Structured queries | SQLite | `--query type=entity parent=X` | Phase 1 (multi-agent writes) |
| Semantic search | sqlite-vec | `--query "entities related to memory"` | When natural language queries needed |
| Graph traversal | JSON-LD @graph / recursive CTEs | `--query "ancestors of entity X"` | When complex relationship queries needed |
| Temporal history | SQLite history table | `--query "parent history of X"` | When evolution tracking needed |

### AALang/GAB Integration

AALang's JSON-LD `@graph` format is inherently a knowledge graph. Our existing `.gab.jsonld` files define typed nodes (LLMAgent, Actor, Mode) with explicit relationship edges (containedBy, contains, canMessage). This creates a natural integration path: the UUID index could cross-reference entity UUIDs with JSON-LD `@id` values, enabling graph queries across both systems.

Future capability: `pointer-sync.sh --export-graph` generates a unified JSON-LD knowledge graph queryable with SPARQL or loadable into graph databases.

### SHIMI Alignment

SHIMI (Semantic Hierarchical Memory Index, arXiv:2504.06135) validates our hierarchical approach — its semantic node hierarchy mirrors our layer-stage tree. Key gaps identified: CRDT-based conflict resolution for multi-agent writes, and embedding-based similarity search. Both are addressed in the hybrid schema design.

### Cross-References

- **Full research**: `../../../stage_3_02_research/outputs/uuid_and_database_patterns_research.md` Sections 11-16
- **Infrastructure design**: `uuid_graph_and_query_design.md` Sections 8-9
- **Interface design**: `uuid_graph_and_query_design.md` Sections 6-7 (Addendum 16)

---

## Sources

- Research: `../../../stage_3_02_research/outputs/rename_propagation_research.md` — evaluation of 7 rename propagation approaches
- Research: `../../../stage_3_02_research/outputs/uuid_and_database_patterns_research.md` — UUID universality, document database analogy, agent interaction research, concurrency patterns
- IETF UUID Specification: RFC 4122
- Current system: `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/pointer-sync.sh`
- [Vercel: We Removed 80% of Our Agent's Tools](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)
- [Vercel: How to Build Agents with Filesystems and Bash](https://vercel.com/blog/how-to-build-agents-with-filesystems-and-bash)
- [Anthropic: Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [NxCode: Harness Engineering Complete Guide](https://www.nxcode.io/resources/news/harness-engineering-complete-guide-ai-agent-codex-2026)
- [Hugo Bowne: Harness Engineering — Why Agent Context Matters](https://hugobowne.substack.com/p/harness-engineering-why-agent-context)
- [Microsoft: Collaborating Agents — Chatting with Your Database the Right Way](https://devblogs.microsoft.com/azure-sql/a-story-of-collaborating-agents-chatting-with-your-database-the-right-way/)
- [SHIMI: Semantic Hierarchical Memory Index (arXiv:2504.06135)](https://arxiv.org/abs/2504.06135)
- [Microsoft GraphRAG](https://microsoft.github.io/graphrag/)
- [HybridRAG: Knowledge Graph + Vector Retrieval (arXiv:2408.04948)](https://arxiv.org/abs/2408.04948)
- [Zep/Graphiti: Temporal Knowledge Graphs](https://www.getzep.com/graphiti)
- [MemWeaver: Multi-Type Agent Memory (arXiv:2503.15917)](https://arxiv.org/abs/2503.15917)
- [sqlite-vec: Vector Search for SQLite](https://github.com/asg017/sqlite-vec)
- [AALang and GAB (Brother Barney)](https://github.com/yenrab/AALang-Gab)
- [JSON-LD W3C Specification](https://www.w3.org/TR/json-ld11/)
