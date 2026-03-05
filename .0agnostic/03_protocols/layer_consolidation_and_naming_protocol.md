---
resource_id: "ba824b39-6669-433f-bd54-4862ee5f8925"
resource_type: "protocol"
resource_name: "layer_consolidation_and_naming_protocol"
---
# Layer Consolidation and Naming Protocol

**Last Updated**: 2026-02-27
**Confirmed Status**: ✅ Reliable (validated through layer_4 consolidation)

---

## What This Protocol Addresses

When a layer directory (e.g., `layer_3/`, `layer_4/`) uses old naming conventions and has duplicate `layer_N_group/` directories, this protocol provides the standardized workflow to:
1. **Consolidate** content from old and new structures
2. **Rename** layers to follow `layer_N_group` convention
3. **Validate** the final structure is correct

---

## Problem Pattern

**Symptoms**:
- Directory structure has both `layer_N/` and `layer_N_group/` existing simultaneously
- `layer_N/` uses old naming (layer_N_00_ai_manager_system, layer_N_01_*, layer_N_02_sub_layers, layer_N_99_stages)
- `layer_N_group/` uses new naming convention but only has partial content
- No `.0agnostic/` directory present in either location

**Root Cause**: Historical migration from old architecture to layer-stage system wasn't fully completed at all layers. Some layers got partially updated while others remained in old structure.

**Example**:
- `layer_4/` had all projects (ML, algorithms, erlang, etc.)
- `layer_4_group/` had only new projects (professional_readiness from CSE 300)
- This created a split where newer work went to layer_4_group but old work remained in layer_4

---

## Consolidation Workflow

### Step 1: Verify Content Distribution

```bash
# Check what's in each directory
ls -la layer_N/layer_N_subx3_projects/
ls -la layer_N_group/layer_N_subx3_projects/
```

**Outcome**: Know which directory has which projects.

### Step 2: Copy Missing Content

Copy projects from one location to the unified location:

```bash
cp -r layer_N_group/layer_N_subx3_projects/* layer_N/layer_N_subx3_projects/
```

**Precondition**: Ensure `layer_N/layer_N_subx3_projects/` exists and has space.

**Outcome**: All content now in `layer_N/` (source of truth).

### Step 3: Rename Layer (Handle mv Behavior)

```bash
mv layer_N layer_N_group
```

**Critical Note**: If `layer_N_group` already exists, the `mv` command will move `layer_N` INSIDE `layer_N_group` as a subdirectory, creating a nested structure. This is shell behavior, not an error.

**Result if nesting occurs**:
```
layer_N_group/
├── layer_N/          ← Nested (wrong)
│   └── layer_N_subx3_projects/
└── layer_N_subx3_projects/  ← Top-level (correct)
```

### Step 4: Flatten Nested Structure (If Needed)

If nesting occurred, merge the nested content up one level:

```bash
cd layer_N_group
cp -r layer_N/layer_N_subx3_projects/* layer_N_subx3_projects/
find . -maxdepth 1 -type d -name "layer_N" -exec rm -rf {} +
```

**Outcome**: Single `layer_N_subx3_projects/` at top level with all content.

### Step 5: Verify Final Structure

```bash
ls -1 layer_N_group/layer_N_subx3_projects/ | grep layer_N_subx3_project
```

**Expected**: All projects visible (old + new consolidated).

### Step 6: Handle Old Architecture Remnants

`layer_N` directory may contain old-style sub-structure:
- `layer_N_00_ai_manager_system/` → Deprecated (replaced by `.0agnostic/`)
- `layer_N_01_manager_handoff_documents/` → Deprecated (replaced by `.0agnostic/05_handoff_documents/`)
- `layer_N_02_sub_layers/` → Deprecated (consolidated into entity `.0agnostic/`)
- `layer_N_99_stages/` → Move to `layer_N_group/layer_N_99_stages/` if still needed

**Action for each**:
- `layer_N_00_*`, `layer_N_01_*`, `layer_N_02_*`: Can be deleted (content migrated to `.0agnostic/`)
- `layer_N_99_stages/`: Copy to new location if stages are still in use
- After copying, delete original `layer_N/` directory

---

## Naming Convention After Consolidation

**Correct structure**:
```
layer_N_group/                          ← Follows layer_N_group naming
├── 0AGNOSTIC.md                        ← Should exist (source of truth)
├── CLAUDE.md                           ← Auto-generated
├── layer_N_99_stages/                  ← Stages (if applicable)
│   ├── stage_00_universal/
│   ├── stage_01_request_gathering/
│   └── ... (stages 02-11)
└── layer_N_subx3_projects/             ← All projects consolidated here
    ├── layer_N_subx3_project_A/
    ├── layer_N_subx3_project_B/
    └── ... (all projects)
```

---

## Validation Checklist

- [ ] All projects from both old locations are in `layer_N_group/layer_N_subx3_projects/`
- [ ] No duplicate projects exist (no `layer_N/layer_N_subx3_project_X` AND `layer_N_group/layer_N_subx3_project_X`)
- [ ] `layer_N/` directory is completely removed (or moved out of the way)
- [ ] Only `layer_N_group/` exists (naming convention followed)
- [ ] `layer_N_group/` is a git-tracked directory ready for commit
- [ ] If projects have 0AGNOSTIC.md files, they reference correct parent paths

---

## Git Operations After Consolidation

```bash
# Stage all changes
git add layer_N_group/

# Commit with clear message
git commit -m "[AI Context] Consolidate layer_N structure and rename to layer_N_group

- Merged projects from old layer_N and layer_N_group
- Removed duplicate layer_N_group structure
- Renamed layer_N to layer_N_group (naming convention)
- Total projects consolidated: [count]"

# Push
git push
```

---

## Common Pitfalls

| Pitfall | Prevention |
|---------|-----------|
| `mv layer_N layer_N_group` nests instead of replacing | Check if `layer_N_group` exists first; if yes, flatten nested structure afterward |
| Deleting content before copying | Always verify content is in final location before deletion |
| Forgetting to remove old `layer_N_00_*` directories | Review what each old directory contained before deciding to delete |
| Not updating 0AGNOSTIC.md parent references | After moving projects into layer_N_group, verify parent path references are correct |

---

## Integration with .0agnostic/

After consolidation, `layer_N_group/` should have:
- **0AGNOSTIC.md**: Source of truth for layer identity and resources
- **.0agnostic/**: On-demand resources (rules, protocols, knowledge, skills, agents)
- **layer_N_99_stages/**: If stages are used
- **layer_N_subx3_projects/**: All child projects consolidated

If `.0agnostic/` is missing, create it following the unified numbering convention (01_knowledge/, 02_rules/, 03_protocols/, etc.).

---

## Session Notes

### 2026-02-27 — Initial Consolidation (layer_4)

- ✅ **Validated**: layer_4 had all base projects (ML, algorithms, erlang, pac20026, parallelism)
- ✅ **Validated**: layer_4_group had only professional_readiness (new CSE 300 project)
- ✅ **Merged**: Copied professional_readiness from layer_4_group into layer_4/layer_4_subx3_projects/
- ⚠️ **Issue**: `mv layer_4 layer_4_group` nested layer_4 inside layer_4_group (expected shell behavior)
- ✅ **Resolved**: Flattened structure using `cp -r` to move layer_4's projects up, then deleted nested layer_4
- ✅ **Result**: layer_4_group now has all 8 projects consolidated (7 old + 1 new professional_readiness)

### 2026-02-27 — Consolidation Planned (layer_3)

- layer_3 has old naming: layer_3_00_ai_manager_system, layer_3_01_manager_handoff_documents, layer_3_02_sub_layers, layer_3_99_stages
- No layer_3_group exists yet
- **Next step**: Rename layer_3 → layer_3_group and migrate old sub-structure to `.0agnostic/` convention

---

## References

- **Layer Stage System**: `.0agnostic/01_knowledge/layer_stage_system/`
- **Entity Structure**: `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`
- **Migration Guide**: `.0agnostic/03_protocols/MIGRATION_GUIDE.md` (old architecture transition details)
