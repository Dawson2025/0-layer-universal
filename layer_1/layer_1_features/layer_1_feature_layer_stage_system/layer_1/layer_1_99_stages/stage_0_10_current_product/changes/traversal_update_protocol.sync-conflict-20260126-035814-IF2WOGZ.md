---
resource_id: "1719724a-2979-4be8-97d8-391092dbc63c"
resource_type: "document"
resource_name: "traversal_update_protocol.sync-conflict-20260126-035814-IF2WOGZ"
---
# Traversal Update Protocol

**Purpose:** Ensure AI agents can navigate to the correct context after ANY system change.

**Last Updated:** 2026-01-15

---

<!-- section_id: "7d66943b-7076-41a1-9b30-84f54aff528d" -->
## The Problem

When changing the system (renaming folders, restructuring, adding features), it's easy to:
1. Update the actual folders/files
2. Forget to update path references in documentation
3. Leave agents unable to navigate to what they need

**Result:** Agents follow broken paths, can't find context, and fail their tasks.

---

<!-- section_id: "0feda91a-a25f-448a-bb72-3f6691c2ea78" -->
## Key Principle

> **Every structural change requires traversal verification.**
>
> If you change a path, you must update every document that references it.

---

<!-- section_id: "843e4f6f-a073-42dd-9e57-f99b3d331c77" -->
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

<!-- section_id: "5afa9bef-916f-4576-abae-04b9920b1f97" -->
## Traversal Update Checklist

<!-- section_id: "edf40a13-1b37-45e7-9d2d-099bad595408" -->
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

<!-- section_id: "aaed91f6-e9bd-4d5e-a3d3-b8217a53411c" -->
### When Restructuring (Moving Content)

1. **Before moving:** Document current paths in a temp file
2. **After moving:** Update ALL navigation documents
3. **Verify:** Run path verification (see below)

<!-- section_id: "5f9f131c-518e-44a4-b76d-24135529db0e" -->
### When Adding New Layers/Stages

1. Update `SYSTEM_OVERVIEW.md` with new layer/stage info
2. Update `instantiation_guide.md` if entity creation changes
3. Update `universal_init_prompt.md` Quick Reference table
4. Update any status.json templates

---

<!-- section_id: "21acf92b-e9bf-434e-87b7-606896fece1c" -->
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

<!-- section_id: "ac6a75e6-d37d-4065-b360-cf525191b3b7" -->
## Navigation Verification Tests

After changes, manually verify an agent can:

<!-- section_id: "9c11b121-205a-456a-8c93-a5ca53e1ff28" -->
### Test 1: Entry Point → Framework Docs
```
universal_init_prompt.md
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md (should exist)
  → MASTER_DOCUMENTATION_INDEX.md (should exist)
  → SYSTEM_OVERVIEW.md (should exist)
```

<!-- section_id: "278df480-3e39-4098-9172-852d883a6b8f" -->
### Test 2: Find Layer-Specific Context
```
From init prompt:
  → layer_1_project/ (should have 1.02_sub_layers/, 1.99_stages/)
  → layer_2_features/ (should have structure)
  → Find status.json in any layer
```

<!-- section_id: "c9fa5ab3-edc3-4cba-9568-64439c6b40d1" -->
### Test 3: Find Setup/Creation Guides
```
From init prompt:
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/setup/instantiation_guide.md
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/1_project_template/
  → layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template/
```

<!-- section_id: "9790fad1-387a-44d2-b6c5-63c7cc18c04f" -->
### Test 4: Find Current Work Stage
```
For any entity:
  → layer_N/layer_N_99_stages/stage_N.08_current_product/
  → Should contain README.md at minimum
```

---

<!-- section_id: "95c90b9a-9849-4284-8c61-450b84b5e39c" -->
## Common Path-Breaking Changes

| Change Type | What Breaks | Update Required |
|-------------|-------------|-----------------|
| Rename `N_folder` → `N_layer_folder` | All hardcoded paths | Batch sed replacement |
| Consolidate sub_layers | Individual sub_layer refs | Update init prompt Quick Reference |
| Add new stage | Stage number references | Update SYSTEM_OVERVIEW, framework README |
| Move files between layers | Direct path links | Update all linking docs |
| Rename MCP/tool folders | Setup documentation | Update all setup guides |

---

<!-- section_id: "0cf9377e-058d-4ca5-ac8c-2bb68e9dbe42" -->
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

<!-- section_id: "a629ae7c-c61c-4669-ab94-9ae89db0e946" -->
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

<!-- section_id: "635d8651-8881-46e8-a2bd-b90b33ecddfd" -->
## Integration with Other Protocols

This protocol works alongside:

- `restructuring_migration_protocol.md` - Add traversal check to step 6
- `../setup/instantiation_guide.md` - When creating entities, paths are correct
- `../README.md` - System management overview

**Rule:** No structural change PR is complete without traversal verification.

---

<!-- section_id: "ee4178f6-0df0-4949-8588-743d972a2f14" -->
## Related Documents

- `restructuring_migration_protocol.md` - Content migration checklist
- `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md` - Layer structure reference
- `../../SYSTEM_OVERVIEW.md` - Current system architecture
