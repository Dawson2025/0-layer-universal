---
resource_id: "82b7faea-7e1c-4928-b66d-bf0da25ffc02"
resource_type: "document"
resource_name: "traversal_update_protocol"
---
# Traversal Update Protocol

**Purpose:** Ensure AI agents can navigate to the correct context after ANY system change.

**Last Updated:** 2026-01-15

---

<!-- section_id: "d5ffd057-769b-4147-8ec3-c76170ae969d" -->
## The Problem

When changing the system (renaming folders, restructuring, adding features), it's easy to:
1. Update the actual folders/files
2. Forget to update path references in documentation
3. Leave agents unable to navigate to what they need

**Result:** Agents follow broken paths, can't find context, and fail their tasks.

---

<!-- section_id: "bfe58881-0cf4-4fdd-aa96-b0eed2a5dfa9" -->
## Key Principle

> **Every structural change requires traversal verification.**
>
> If you change a path, you must update every document that references it.

---

<!-- section_id: "1a48bda5-9857-490d-8809-ff61cf772ec9" -->
## Critical Navigation Documents

These documents are the **entry points** for AI agent navigation. They MUST be updated when paths change:

| Document | Location | Purpose |
|----------|----------|---------|
| `universal_init_prompt.md` | `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/` | Primary entry point for all sessions |
| `MASTER_DOCUMENTATION_INDEX.md` | `0_context/` | Master reference for all docs |
| `SYSTEM_OVERVIEW.md` | `0_context/` | System architecture overview |
| `instantiation_guide.md` | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/setup/` | How to create entities |
| Framework `README.md` | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/` | Layer/stage system explanation |

---

<!-- section_id: "08cd500f-ee55-445c-ac26-6c2d54db5251" -->
## Traversal Update Checklist

<!-- section_id: "b3abdea7-2d03-4b0b-ab34-64b03edb0f10" -->
### When Renaming Folders

```bash
# 1. Find all references to the old name
grep -r "old_folder_name" --include="*.md" /path/to/0_context/

# 2. Update each reference
# Use sed for batch updates:
find /path/to/0_context -name "*.md" -exec sed -i 's|old_folder_name|new_folder_name|g' {} \;

# 3. Verify no old references remain
grep -r "old_folder_name" --include="*.md" /path/to/0_context/
# Should return empty
```

<!-- section_id: "0852367a-3cd1-4d33-9c0e-4936f43db7e7" -->
### When Restructuring (Moving Content)

1. **Before moving:** Document current paths in a temp file
2. **After moving:** Update ALL navigation documents
3. **Verify:** Run path verification (see below)

<!-- section_id: "f47e0b8b-9e19-4938-9d7c-e98f6f12c11a" -->
### When Adding New Layers/Stages

1. Update `SYSTEM_OVERVIEW.md` with new layer/stage info
2. Update `instantiation_guide.md` if entity creation changes
3. Update `universal_init_prompt.md` Quick Reference table
4. Update any status.json templates

---

<!-- section_id: "e53f81f7-9375-4355-b92d-c48723dfe057" -->
## Path Verification Script

Run this after ANY structural change:

```bash
#!/bin/bash
# verify_paths.sh - Check that documented paths exist

CONTEXT_ROOT="/home/dawson/dawson-workspace/code/0_layer_universal/0_context"

echo "=== Verifying Documented Paths ==="

# Extract paths from universal_init_prompt.md and check they exist
INIT_PROMPT="$CONTEXT_ROOT/layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/universal_init_prompt.md"

# Check critical paths mentioned in init prompt
CRITICAL_PATHS=(
  "$CONTEXT_ROOT/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md"
  "$CONTEXT_ROOT/MASTER_DOCUMENTATION_INDEX.md"
  "$CONTEXT_ROOT/SYSTEM_OVERVIEW.md"
  "$CONTEXT_ROOT/layer_1/layer_1_features/layer_1_feature_layer_stage_system/setup/instantiation_guide.md"
  "$CONTEXT_ROOT/layer_0/layer_0_99_stages/"
  "$CONTEXT_ROOT/layer_1_project/1.99_stages/"
)

FAILED=0
for path in "${CRITICAL_PATHS[@]}"; do
  if [ -e "$path" ]; then
    echo "✓ $path"
  else
    echo "✗ MISSING: $path"
    FAILED=$((FAILED + 1))
  fi
done

echo ""
echo "=== Results ==="
if [ $FAILED -eq 0 ]; then
  echo "All critical paths verified."
else
  echo "WARNING: $FAILED paths are broken!"
  exit 1
fi
```

---

<!-- section_id: "51003ea9-1bb1-41d9-a04a-6756538881fe" -->
## Navigation Verification Tests

After changes, manually verify an agent can:

<!-- section_id: "8f1fd9ee-9d2c-4663-8244-a1418c3e0698" -->
### Test 1: Entry Point → Framework Docs
```
universal_init_prompt.md
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md (should exist)
  → MASTER_DOCUMENTATION_INDEX.md (should exist)
  → SYSTEM_OVERVIEW.md (should exist)
```

<!-- section_id: "6d3df9d3-69db-46a4-8a52-5af4dc0268c7" -->
### Test 2: Find Layer-Specific Context
```
From init prompt:
  → layer_1_project/ (should have 1.02_sub_layers/, 1.99_stages/)
  → layer_2_features/ (should have structure)
  → Find status.json in any layer
```

<!-- section_id: "2896534b-7754-4cf9-b32c-9ef900190278" -->
### Test 3: Find Setup/Creation Guides
```
From init prompt:
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/setup/instantiation_guide.md
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/1_project_template/
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template/
```

<!-- section_id: "de8a09b8-23b6-490d-8b1c-b07d73707891" -->
### Test 4: Find Current Work Stage
```
For any entity:
  → layer_N/layer_N_99_stages/stage_N.08_current_product/
  → Should contain README.md at minimum
```

---

<!-- section_id: "bec8aaea-239d-45a9-9ad5-a4c570a3da95" -->
## Common Path-Breaking Changes

| Change Type | What Breaks | Update Required |
|-------------|-------------|-----------------|
| Rename `N_folder` → `N_layer_folder` | All hardcoded paths | Batch sed replacement |
| Consolidate sub_layers | Individual sub_layer refs | Update init prompt Quick Reference |
| Add new stage | Stage number references | Update SYSTEM_OVERVIEW, framework README |
| Move files between layers | Direct path links | Update all linking docs |
| Rename MCP/tool folders | Setup documentation | Update all setup guides |

---

<!-- section_id: "e8cc767e-491c-47d0-9344-bbe6ebf5fd19" -->
## Post-Change Verification Checklist

After ANY structural change:

- [ ] Run `grep -r "old_name"` to find remaining references
- [ ] Run path verification script
- [ ] Test navigation from `universal_init_prompt.md`
- [ ] Verify Quick Reference table paths in init prompt
- [ ] Check MASTER_DOCUMENTATION_INDEX links
- [ ] Verify at least one entity has working stage navigation
- [ ] Commit with message describing path updates

---

<!-- section_id: "db99a895-ab18-4ca9-974c-6de183a12742" -->
## Emergency Recovery

If agents report broken navigation:

1. **Identify the broken path:**
   ```bash
   # What path is the agent trying?
   # Check if it exists:
   ls -la "<reported_path>"
   ```

2. **Find the correct path:**
   ```bash
   # Search for the file/folder name:
   find /path/to/0_context -name "*<partial_name>*" -type d
   ```

3. **Update documentation:**
   - Fix the specific reference in the navigation doc
   - Search for other occurrences of the same wrong path

4. **Add to verification script:**
   - Add the corrected path to CRITICAL_PATHS

---

<!-- section_id: "08d3785c-9e1f-4446-8ff3-1aa2b20f2624" -->
## Integration with Other Protocols

This protocol works alongside:

- `restructuring_migration_protocol.md` - Add traversal check to step 6
- `../setup/instantiation_guide.md` - When creating entities, paths are correct
- `../README.md` - System management overview

**Rule:** No structural change PR is complete without traversal verification.

---

<!-- section_id: "8e1ffce6-f432-4b43-834b-5f1e03362564" -->
## Related Documents

- `restructuring_migration_protocol.md` - Content migration checklist
- `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md` - Layer structure reference
- `../../SYSTEM_OVERVIEW.md` - Current system architecture
