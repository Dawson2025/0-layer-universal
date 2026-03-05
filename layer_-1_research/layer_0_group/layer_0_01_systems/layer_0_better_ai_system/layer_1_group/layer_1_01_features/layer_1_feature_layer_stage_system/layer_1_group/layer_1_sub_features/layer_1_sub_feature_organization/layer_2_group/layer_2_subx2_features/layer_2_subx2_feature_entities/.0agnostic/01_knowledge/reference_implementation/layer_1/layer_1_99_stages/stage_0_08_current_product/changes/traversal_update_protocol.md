---
resource_id: "f09dd337-23f3-492a-868c-2e5d985b81d1"
resource_type: "knowledge"
resource_name: "traversal_update_protocol"
---
# Traversal Update Protocol

**Purpose:** Ensure AI agents can navigate to the correct context after ANY system change.

**Last Updated:** 2026-01-15

---

## The Problem

When changing the system (renaming folders, restructuring, adding features), it's easy to:
1. Update the actual folders/files
2. Forget to update path references in documentation
3. Leave agents unable to navigate to what they need

**Result:** Agents follow broken paths, can't find context, and fail their tasks.

---

## Key Principle

> **Every structural change requires traversal verification.**
>
> If you change a path, you must update every document that references it.

---

## Critical Navigation Documents

These documents are the **entry points** for AI agent navigation. They MUST be updated when paths change:

| Document | Location | Purpose |
|----------|----------|---------|
| `universal_init_prompt.md` | `layer_0_group/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/` | Primary entry point for all sessions |
| `MASTER_DOCUMENTATION_INDEX.md` | `0_context/` | Master reference for all docs |
| `SYSTEM_OVERVIEW.md` | `0_context/` | System architecture overview |
| `instantiation_guide.md` | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/setup/` | How to create entities |
| Framework `README.md` | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/` | Layer/stage system explanation |

---

## Traversal Update Checklist

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

### When Restructuring (Moving Content)

1. **Before moving:** Document current paths in a temp file
2. **After moving:** Update ALL navigation documents
3. **Verify:** Run path verification (see below)

### When Adding New Layers/Stages

1. Update `SYSTEM_OVERVIEW.md` with new layer/stage info
2. Update `instantiation_guide.md` if entity creation changes
3. Update `universal_init_prompt.md` Quick Reference table
4. Update any status.json templates

---

## Path Verification Script

Run this after ANY structural change:

```bash
#!/bin/bash
# verify_paths.sh - Check that documented paths exist

CONTEXT_ROOT="/home/dawson/dawson-workspace/code/0_layer_universal/0_context"

echo "=== Verifying Documented Paths ==="

# Extract paths from universal_init_prompt.md and check they exist
INIT_PROMPT="$CONTEXT_ROOT/layer_0_group/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/universal_init_prompt.md"

# Check critical paths mentioned in init prompt
CRITICAL_PATHS=(
  "$CONTEXT_ROOT/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md"
  "$CONTEXT_ROOT/MASTER_DOCUMENTATION_INDEX.md"
  "$CONTEXT_ROOT/SYSTEM_OVERVIEW.md"
  "$CONTEXT_ROOT/layer_1/layer_1_features/layer_1_feature_layer_stage_system/setup/instantiation_guide.md"
  "$CONTEXT_ROOT/layer_0_group/0.99_stages/"
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

## Navigation Verification Tests

After changes, manually verify an agent can:

### Test 1: Entry Point → Framework Docs
```
universal_init_prompt.md
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md (should exist)
  → MASTER_DOCUMENTATION_INDEX.md (should exist)
  → SYSTEM_OVERVIEW.md (should exist)
```

### Test 2: Find Layer-Specific Context
```
From init prompt:
  → layer_1_project/ (should have 1.02_sub_layers/, 1.99_stages/)
  → layer_2_features/ (should have structure)
  → Find status.json in any layer
```

### Test 3: Find Setup/Creation Guides
```
From init prompt:
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/setup/instantiation_guide.md
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/1_project_template/
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template/
```

### Test 4: Find Current Work Stage
```
For any entity:
  → layer_N/layer_N_99_stages/stage_N.08_current_product/
  → Should contain README.md at minimum
```

---

## Common Path-Breaking Changes

| Change Type | What Breaks | Update Required |
|-------------|-------------|-----------------|
| Rename `N_folder` → `N_layer_folder` | All hardcoded paths | Batch sed replacement |
| Consolidate sub_layers | Individual sub_layer refs | Update init prompt Quick Reference |
| Add new stage | Stage number references | Update SYSTEM_OVERVIEW, framework README |
| Move files between layers | Direct path links | Update all linking docs |
| Rename MCP/tool folders | Setup documentation | Update all setup guides |

---

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

## Integration with Other Protocols

This protocol works alongside:

- `restructuring_migration_protocol.md` - Add traversal check to step 6
- `../setup/instantiation_guide.md` - When creating entities, paths are correct
- `../README.md` - System management overview

**Rule:** No structural change PR is complete without traversal verification.

---

## Related Documents

- `restructuring_migration_protocol.md` - Content migration checklist
- `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md` - Layer structure reference
- `../../SYSTEM_OVERVIEW.md` - Current system architecture
