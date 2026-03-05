# Design Proposal: UUID Identity System for Layer-Stage Entities

## Status: PROPOSED
## Date: 2026-03-02
## Author: AI Agent (stage_3_04_design)
## Related Research: `../../../stage_3_02_research/outputs/rename_propagation_research.md`

---

## 1. Problem Statement

### Current Behavior

The pointer-sync.sh system resolves pointer files using **name-based lookup**:

```yaml
canonical_entity: "layer_1_feature_context_chain"
canonical_stage: "stage_2_04_design"
```

Resolution uses `find -type d -name "$CANONICAL_ENTITY"` to locate the entity directory. This works when entities are **moved** (same name, new location) but **breaks completely** when entities are **renamed**.

### Impact of Renames

When `layer_1_feature_old_name` is renamed to `layer_1_feature_new_name`:
- Every pointer file referencing `canonical_entity: "layer_1_feature_old_name"` becomes BROKEN
- No warning at rename time — breakage is silent
- Discovery happens later when pointer-sync.sh runs and reports BROKEN pointers
- Manual find-and-replace across all pointer files is required

### Why This Matters

- Entity names change as understanding evolves (e.g., renaming a feature to better reflect scope)
- Stage names may be adjusted (e.g., splitting or merging stages)
- The system will grow — more entities means more pointers means more breakage risk
- Cross-layer references are especially fragile (a layer 0 rename affects all layer 1+ pointers)

---

## 2. Proposed Solution: UUID-Based Identity

### Core Idea

Assign every entity and every stage a **UUID v4** (random, 128-bit) that:
- Is generated once at creation time
- Never changes, regardless of renames, moves, or restructuring
- Serves as the **primary** resolution key for pointer-sync.sh
- Coexists with human-readable names (which become display-only)

### Why UUID v4 (Random)

| Version | Method | Why Not |
|---------|--------|---------|
| v1 | Timestamp + MAC | Leaks creation time, requires MAC address |
| v3 | MD5 hash of namespace+name | **Breaks on rename** — hash changes when name changes |
| v4 | Random | **Best fit** — no dependency on name, path, or time |
| v5 | SHA-1 hash of namespace+name | Same problem as v3 — deterministic from name |

UUID v4 is the only version where the identifier is completely decoupled from the entity's name or path.

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

## 3. Where UUIDs Live

Every level of the hierarchy gets a UUID, stored in its own `0AGNOSTIC.md`:

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

### 3.3 Stage Registry — Machine-Readable Index

The existing `stage_N_00_stage_registry/` directory gets a `registry.json` mapping all stage UUIDs:

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
- `canonical_subpath` remains name-based (file paths within a stage don't get UUIDs)
- Old format (`canonical_entity` without `_id`) still works as fallback

---

## 4. Updated Resolution Algorithm

### Current Algorithm (Name-Based)

```
1. Extract canonical_entity from frontmatter
2. find -type d -name "$canonical_entity" → entity directory
3. Extract canonical_stage → find within entity directory
4. Append canonical_subpath → full path
5. Compute relative path from pointer to target
```

### Proposed Algorithm (UUID-First with Name Fallback)

```
1. Extract canonical_entity_id from frontmatter
2. If UUID present:
   a. Search all 0AGNOSTIC.md files for matching entity_id
   b. Cache results in .pointer-cache.json for performance
   c. → entity directory
3. If UUID absent (legacy pointer):
   a. Extract canonical_entity (name-based)
   b. find -type d -name "$canonical_entity" → entity directory
   c. Emit deprecation warning: "Pointer uses name-based resolution. Add canonical_entity_id for rename safety."
4. Extract canonical_stage_id from frontmatter
5. If stage UUID present:
   a. Read registry.json in entity's stage_N_00_stage_registry/
   b. Look up stage_id → get directory name
   c. → stage directory
6. If stage UUID absent (legacy):
   a. Extract canonical_stage (name-based)
   b. find within entity directory
   c. Emit deprecation warning
7. Append canonical_subpath → full path
8. Compute relative path from pointer to target
```

### Performance: UUID Index Cache

Scanning all `0AGNOSTIC.md` files for UUIDs on every run would be slow. Solution: a cache file.

```json
// .pointer-cache.json (at ROOT level, auto-generated)
{
  "generated": "2026-03-02T10:30:00Z",
  "entities": {
    "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d": {
      "name": "layer_2_subx2_feature_context_chain_system",
      "path": "/full/path/to/entity"
    }
  }
}
```

Cache behavior:
- Rebuilt on `pointer-sync.sh --rebuild-cache` or when cache is missing
- Auto-rebuilt if a UUID lookup fails (entity may have been created since last cache)
- Optionally rebuilt as part of `agnostic-sync.sh`

---

## 5. Migration Plan

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

### Phase 2: Assign Stage UUIDs and Create Registries

For each entity with stages:

1. Find all `stage_N_XX_*` directories
2. Generate a UUID for each stage
3. If the stage has a `0AGNOSTIC.md`, insert `stage_id:` into its Identity section
4. Create/update `registry.json` in `stage_N_00_stage_registry/`

### Phase 3: Update pointer-sync.sh

Modify the resolution algorithm to:
1. Try UUID-first resolution (read `canonical_entity_id`, search cache/0AGNOSTIC.md files)
2. Fall back to name-based resolution if no UUID
3. Emit deprecation warnings for name-based pointers
4. Add `--rebuild-cache` flag

### Phase 4: Update Entity Creation Skill

Modify `/entity-creation` to:
1. Auto-generate `entity_id` UUID when creating `0AGNOSTIC.md`
2. Auto-generate `stage_id` UUIDs for all 12 stages
3. Create `registry.json` in `stage_N_00_stage_registry/`

### Phase 5: Migrate Existing Pointers

Create `migrate-pointers.sh` that:
1. Finds all pointer files (YAML frontmatter with `pointer_to:`)
2. For each pointer with `canonical_entity:` but no `canonical_entity_id:`:
   a. Look up the entity name in the UUID cache
   b. Add `canonical_entity_id:` and `canonical_entity_name:` fields
   c. Optionally remove the old `canonical_entity:` field (or keep for readability)
3. Same for `canonical_stage:` → `canonical_stage_id:` + `canonical_stage_name:`

### Phase 6: Run agnostic-sync.sh

Regenerate all CLAUDE.md files so they include the `entity_id` from 0AGNOSTIC.md.

---

## 6. Impact on Existing Tools

### pointer-sync.sh

| Component | Change |
|-----------|--------|
| `extract_fm()` | Add extraction of `canonical_entity_id`, `canonical_stage_id` |
| Entity resolution | UUID-first lookup (cache → scan), name fallback |
| Stage resolution | Registry lookup by `stage_id`, then name fallback |
| New flag: `--rebuild-cache` | Rebuild `.pointer-cache.json` |
| Output | Show UUID in verbose mode, deprecation warnings for name-based |

### entity-creation skill (SKILL.md)

| Component | Change |
|-----------|--------|
| 0AGNOSTIC.md template | Add `entity_id: "UUID"` to Identity section |
| Stage creation loop | Generate UUID per stage, insert into stage 0AGNOSTIC.md |
| Stage registry | Create `registry.json` with all stage UUIDs |

### agnostic-sync.sh

| Component | Change |
|-----------|--------|
| CLAUDE.md generation | Pass through `entity_id` from 0AGNOSTIC.md to generated files |
| No other changes needed | entity_id is just another field in the Identity section |

### entity_structure.md (canonical reference)

| Component | Change |
|-----------|--------|
| 0AGNOSTIC.md spec | Document `entity_id` as required field |
| Stage 0AGNOSTIC.md | Document `stage_id` as required field |
| stage_N_00_stage_registry | Document `registry.json` format |
| Pointer file spec | Document `canonical_entity_id` and `canonical_stage_id` fields |

---

## 7. Edge Cases

### 7.1 Duplicate Entity Names

**Problem**: Two entities named `layer_1_feature_auth` in different locations.
**Before (name-based)**: `find -type d -name` returns first match — ambiguous.
**After (UUID-based)**: Each has a unique UUID. No ambiguity. Pointers reference the exact entity they intend.

### 7.2 Cross-Layer References

**Problem**: A layer 1 pointer references a layer 0 entity. Layer 0 entity gets renamed.
**Before**: Pointer breaks silently.
**After**: UUID doesn't change. Pointer still resolves.

### 7.3 Orphaned UUIDs

**Problem**: An entity is deleted but pointers still reference its UUID.
**Behavior**: Same as today — pointer reports BROKEN. The UUID just makes it clearer which entity was intended (the UUID can be searched in git history).
**Mitigation**: `pointer-sync.sh --validate` already catches broken pointers.

### 7.4 Subpath Changes

**Problem**: Files within a stage are renamed/moved.
**Behavior**: Every `.md` file that could be a pointer target gets a `resource_id` in its YAML frontmatter — including output files. When `canonical_resource_id` is present in a pointer, the file can be renamed freely and the pointer still resolves via UUID.
**Fallback**: `canonical_subpath` is kept as a display-only field (like `canonical_entity_name`). If no `canonical_resource_id` is present, subpath resolution falls back to name-based.
**Principle**: Every referenceable thing gets an ID — same as primary keys in a database. This eliminates the entire class of rename-breaks-reference problems.

### 7.5 UUID Collision

**Probability**: UUID v4 has 122 random bits. Collision probability with 1000 entities: ~2.7 × 10^-31. Negligible.

### 7.6 Merging Entities

**Problem**: Two entities are merged into one. Which UUID survives?
**Decision**: The absorbing entity keeps its UUID. The absorbed entity's UUID is added to a `previous_ids` list for backward compatibility:

```yaml
entity_id: "surviving-uuid"
previous_ids:
  - "absorbed-uuid-1"
  - "absorbed-uuid-2"
```

### 7.7 Stage Without 0AGNOSTIC.md

**Problem**: Scaffolded stages don't have `0AGNOSTIC.md` yet.
**Solution**: The stage's UUID still exists in `registry.json`. When the stage's `0AGNOSTIC.md` is eventually created, the UUID from the registry is inserted into it. The registry is the source of truth for stage identity, the stage's `0AGNOSTIC.md` mirrors it.

---

## 8. Before/After Examples

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

### Example 4: Stage Registry (registry.json)

**New file** at `stage_2_00_stage_registry/registry.json`:
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

## 9. Implementation Priority

| Phase | What | Effort | Risk | Prerequisite |
|-------|------|--------|------|--------------|
| 1 | `assign-uuids.sh` — add entity_id to all 0AGNOSTIC.md | 2-3 hours | Low | None |
| 2 | Stage UUIDs + registry.json | 3-4 hours | Low | Phase 1 |
| 3 | Update pointer-sync.sh for UUID resolution | 4-6 hours | Medium | Phase 1-2 |
| 4 | Update entity-creation skill | 2-3 hours | Low | Phase 1-2 |
| 5 | Migrate existing pointers | 2-3 hours | Low | Phase 3 |
| 6 | Update entity_structure.md canonical reference | 1 hour | Low | Phase 1-4 |

**Total estimated effort**: ~15-20 hours across phases.

**Recommended order**: Phase 1 → 2 → 4 → 3 → 5 → 6. Entity creation skill (Phase 4) can be done in parallel with pointer-sync.sh updates (Phase 3).

---

## 10. Open Questions

1. **Should `canonical_entity` (old field) be removed or kept?** Recommendation: keep during migration, remove after all pointers are migrated.
2. **Should the cache be git-tracked or .gitignored?** Recommendation: .gitignored (it's a build artifact).
3. **Should `previous_ids` be supported from day 1?** Recommendation: defer until an actual merge occurs.
4. **~~Should subpaths eventually get IDs too?~~** RESOLVED: Yes — every referenceable `.md` file gets a `resource_id` in YAML frontmatter (see Section 11). This includes output files, knowledge docs, rules, protocols, and skills.

---

---

## 11. Addendum: Universal Resource IDs (Expanded Scope)

### Rationale

The original design covers entities and stages. However, **anything that can be pointed to or referenced** should have a stable ID. This includes `.0agnostic/` resources that participate in the deduplication pattern (pointer files redirect to canonical locations). When a knowledge doc, rule, or protocol is renamed, pointers to it break — the same problem as entity renames.

### Resource Types That Get IDs

| Resource Type | ID Field | Where It Lives | Example |
|---------------|----------|----------------|---------|
| **Entity** | `entity_id` | `0AGNOSTIC.md` Identity section | `entity_id: "a1b2c3d4-..."` |
| **Stage** | `stage_id` | Stage's `0AGNOSTIC.md` + `registry.json` | `stage_id: "e5f6a7b8-..."` |
| **Knowledge doc** | `resource_id` | YAML frontmatter at top of `.md` file | `resource_id: "k1k2k3k4-..."` |
| **Rule** | `resource_id` | YAML frontmatter at top of rule `.md` | `resource_id: "r1r2r3r4-..."` |
| **Protocol** | `resource_id` | YAML frontmatter at top of protocol `.md` | `resource_id: "p1p2p3p4-..."` |
| **Skill** | `resource_id` | YAML frontmatter in `SKILL.md` | `resource_id: "s1s2s3s4-..."` |
| **Output file** | `resource_id` | YAML frontmatter at top of output `.md` | `resource_id: "o1o2o3o4-..."` |

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

### Where Resources Get IDs

```
.0agnostic/
├── 01_knowledge/
│   ├── pointer_sync/
│   │   └── pointer_sync_knowledge.md    ← resource_id in frontmatter
│   ├── deduplication_pattern.md          ← resource_id in frontmatter
│   └── layer_stage_system/
│       └── LAYERS_EXPLAINED.md           ← resource_id in frontmatter
├── 02_rules/
│   ├── static/
│   │   └── pointer_sync_rule/
│   │       └── pointer_sync_rule.md      ← resource_id in frontmatter
│   └── dynamic/
│       └── auto_trigger_rule/
│           └── auto_trigger_rule.md      ← resource_id in frontmatter
├── 03_protocols/
│   └── pointer_sync_protocol.md          ← resource_id in frontmatter
└── pointer-sync.sh                       ← NO ID (scripts are invoked, not referenced by pointers)
```

### Resource Registry

Each entity's `.0agnostic/` gets a `resource_registry.json`:

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

### What Does NOT Get an ID

| Thing | Why Not |
|-------|---------|
| Scripts (`.sh`) | Invoked by path/name, not referenced by pointers |
| Auto-generated files (`CLAUDE.md`, `.integration.md`) | Derivative — identity comes from source (`0AGNOSTIC.md`) |
| `.1merge/` files | Override mechanism — identity comes from target |
| `0INDEX.md` | Dashboard — not a referenceable resource |
| `README.md` | Human-readable overview — not a pointer target |
| JSON-LD files (`.gab.jsonld`) | Agent definitions — referenced by agent type, not by ID |
| `registry.json` | Machine registry — not a pointer target itself |

**Note**: Episodic memory files and handoff documents DO get `resource_id` if they are pointer targets. The criterion is: **if something can be the target of a pointer file's `canonical_*` fields, it gets an ID.**

### Migration Impact

The Phase 1-6 migration plan expands to include:
- **Phase 1b**: Assign `resource_id` to all knowledge docs, rules, protocols at root `.0agnostic/`
- **Phase 2b**: Assign `resource_id` to resources in entity-level `.0agnostic/` dirs
- **Phase 5b**: Migrate pointer files that reference resources (add `canonical_resource_id`)

---

## Sources

- Research: `../../../stage_3_02_research/outputs/rename_propagation_research.md` — evaluation of 7 rename propagation approaches
- IETF UUID Specification: RFC 4122
- Current system: `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/pointer-sync.sh`
