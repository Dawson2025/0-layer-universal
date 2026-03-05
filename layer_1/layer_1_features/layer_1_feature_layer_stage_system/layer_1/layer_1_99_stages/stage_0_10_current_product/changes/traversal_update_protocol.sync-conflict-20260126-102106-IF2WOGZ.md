---
resource_id: "445b48c9-6ac4-4997-a3a4-a2ff25d2fad9"
resource_type: "document"
resource_name: "traversal_update_protocol.sync-conflict-20260126-102106-IF2WOGZ"
---
# Traversal Update Protocol

**Purpose:** Ensure AI agents can navigate to the correct context after ANY system change.

**Last Updated:** 2026-01-15

---

<!-- section_id: "9e6b3666-530e-4256-9759-13870e581003" -->
## The Problem

When changing the system (renaming folders, restructuring, adding features), it's easy to:
1. Update the actual folders/files
2. Forget to update path references in documentation
3. Leave agents unable to navigate to what they need

**Result:** Agents follow broken paths, can't find context, and fail their tasks.

---

<!-- section_id: "5be454ff-6741-4571-b26f-01288f5bda1f" -->
## Key Principle

> **Every structural change requires traversal verification.**
>
> If you change a path, you must update every document that references it.

---

<!-- section_id: "6b9144cc-abf7-4c2d-9ac7-b01571ae8348" -->
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

<!-- section_id: "6a345b08-f806-4f46-a9e0-89494d3037c7" -->
## Traversal Update Checklist

<!-- section_id: "582c4cdf-c9f6-4aba-8113-82cbef526098" -->
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

<!-- section_id: "e33d59f1-d79f-4dc8-bc3c-a1190ee513c7" -->
### When Restructuring (Moving Content)

1. **Before moving:** Document current paths in a temp file
2. **After moving:** Update ALL navigation documents
3. **Verify:** Run path verification (see below)

<!-- section_id: "632491eb-42e9-4fbc-a869-d690cc2c59da" -->
### When Adding New Layers/Stages

1. Update `SYSTEM_OVERVIEW.md` with new layer/stage info
2. Update `instantiation_guide.md` if entity creation changes
3. Update `universal_init_prompt.md` Quick Reference table
4. Update any status.json templates

---

<!-- section_id: "de1b8ffb-a9d8-43d5-b269-55cd0129debb" -->
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

<!-- section_id: "7fddd292-2d22-4cc5-b662-5c94651cfecb" -->
## Navigation Verification Tests

After changes, manually verify an agent can:

<!-- section_id: "ec40bded-e530-4f1d-8c7a-97a472fa3b9d" -->
### Test 1: Entry Point → Framework Docs
```
universal_init_prompt.md
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md (should exist)
  → MASTER_DOCUMENTATION_INDEX.md (should exist)
  → SYSTEM_OVERVIEW.md (should exist)
```

<!-- section_id: "dd82ea1f-f101-4eda-ab7a-13734b1b9cbe" -->
### Test 2: Find Layer-Specific Context
```
From init prompt:
  → layer_1_project/ (should have 1.02_sub_layers/, 1.99_stages/)
  → layer_2_features/ (should have structure)
  → Find status.json in any layer
```

<!-- section_id: "d25c6d9c-fc6c-42f1-8826-293b6b4c7b02" -->
### Test 3: Find Setup/Creation Guides
```
From init prompt:
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/setup/instantiation_guide.md
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/1_project_template/
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template/
```

<!-- section_id: "83d6762d-d3d4-4e68-9f45-349b448b7c52" -->
### Test 4: Find Current Work Stage
```
For any entity:
  → layer_N/layer_N_99_stages/stage_N.08_current_product/
  → Should contain README.md at minimum
```

---

<!-- section_id: "c90189e3-c1f7-4d86-a1e3-eb66b108b35d" -->
## Common Path-Breaking Changes

| Change Type | What Breaks | Update Required |
|-------------|-------------|-----------------|
| Rename `N_folder` → `N_layer_folder` | All hardcoded paths | Batch sed replacement |
| Consolidate sub_layers | Individual sub_layer refs | Update init prompt Quick Reference |
| Add new stage | Stage number references | Update SYSTEM_OVERVIEW, framework README |
| Move files between layers | Direct path links | Update all linking docs |
| Rename MCP/tool folders | Setup documentation | Update all setup guides |

---

<!-- section_id: "04bce4e4-3e4c-400d-b721-c5550c28b678" -->
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

<!-- section_id: "2fd4da9e-ba65-43b6-ab5c-1972629d0e3d" -->
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

<!-- section_id: "ea73d8b8-0661-47c0-911b-7a898220b9da" -->
## Integration with Other Protocols

This protocol works alongside:

- `restructuring_migration_protocol.md` - Add traversal check to step 6
- `../setup/instantiation_guide.md` - When creating entities, paths are correct
- `../README.md` - System management overview

**Rule:** No structural change PR is complete without traversal verification.

---

<!-- section_id: "2b8f69b3-a247-4afd-94ef-fe4d021b9b78" -->
## Related Documents

- `restructuring_migration_protocol.md` - Content migration checklist
- `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md` - Layer structure reference
- `../../SYSTEM_OVERVIEW.md` - Current system architecture
