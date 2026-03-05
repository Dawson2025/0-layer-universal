---
resource_id: "58cbcedb-b09b-492d-95a1-ce0ac32250bb"
resource_type: "knowledge"
resource_name: "restructuring_migration_protocol"
---
# Restructuring & Migration Protocol

**Purpose:** Ensure that when restructuring projects, actual content is migrated alongside structural changes.

**Last Updated:** 2026-01-15

---

<!-- section_id: "5ce6ba5b-942d-47b4-b5f4-910f63df7aea" -->
## The Problem

When restructuring a project's layer/stage organization, it's easy to:
1. Create new folder structures (layer_4/, layer_5/, sub_layers, stages)
2. Forget to migrate actual content from legacy locations
3. End up with empty new structures and orphaned legacy folders

**Result:** New structure has placeholder files, while valuable content remains in `0_context/`, `legacy_*/`, or old `N.xx` folders.

---

<!-- section_id: "0164422e-3f7c-4456-85e6-bdc642541ab2" -->
## Key Principle

> **Structural migration ≠ Content migration**
>
> Both must happen together. Creating folders is not the same as moving content.

---

<!-- section_id: "1033e341-57fc-4975-b378-29743e66a807" -->
## Restructuring Checklist

When restructuring any project or layer:

<!-- section_id: "00a634c0-6f6e-46fa-b486-3b18eff6f452" -->
### 1. Identify Legacy Content

```bash
# Find legacy folders
find <project_path> -type d \( -name "legacy*" -o -name "0_context" -o -name "[0-9].[0-9][0-9]_*" \) 2>/dev/null
```

Look for:
- `0_context/` folders
- `legacy_content/`, `legacy_context/`, `legacy_import/`
- Old numbered structures (`1.xx`, `2.xx` at wrong layer level)
- `layer_N_*` folders at wrong nesting level

<!-- section_id: "4622cb2a-3a8b-40be-8d84-72e18cdd0f3b" -->
### 2. Create New Structure

Use templates from `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/` to create:
- `layer_N/` grouping folder
- `layer_N_00_ai_manager_system/`
- `layer_N_01_manager_handoff_documents/`
- `layer_N_02_sub_layers/`
- `layer_N_99_stages/`
- `layer_N+1/` for nested content

<!-- section_id: "2fc28f85-49e7-44be-a681-c1c21bd9f776" -->
### 3. Migrate Content (Critical Step)

**Do not skip this step.** For each legacy location:

```bash
# Example: Migrate sub_layer content
cp -r <legacy>/layer_1_project/1.02_sub_layers/sub_layer_1.01_*/* \
      <new>/layer_4/layer_4_02_sub_layers/sub_layer_4.01_*/

# Example: Migrate stage content
cp -r <legacy>/layer_1_project/1.99_stages/stage_1.01_*/* \
      <new>/layer_4/layer_4_99_stages/stage_4.01_*/

# Example: Migrate features
cp -r <legacy>/layer_2_features/layer_2_feature_* \
      <new>/layer_5/layer_5_features/layer_5_feature_*
```

**Content to migrate:**
- Project init prompts and course overviews
- Stage archives and handoff documents
- Status JSON files
- Feature-specific documentation
- Any actual work artifacts

<!-- section_id: "fedf831d-c873-43d0-a80c-ef3a7404a12c" -->
### 4. Verify Migration

```bash
# Check new structure has files (not just .gitkeep)
find <new>/layer_N -type f ! -name ".gitkeep" | head -20

# Compare file counts
echo "Legacy:" && find <legacy> -type f | wc -l
echo "New:" && find <new>/layer_N -type f | wc -l
```

<!-- section_id: "5336342a-7438-453e-9d96-9ed102366f49" -->
### 5. Remove Legacy Folders

**Only after verification:**

```bash
rm -rf <project>/0_context
rm -rf <project>/legacy_content
rm -rf <project>/legacy_context
# Remove old N.xx folders if they existed at root
```

<!-- section_id: "6d07ac60-95d4-40e4-8f9a-cd7e6223aa13" -->
### 6. Update Traversal Documentation (Critical)

**Do not skip this step.** After restructuring, paths have changed. Update:

```bash
# Find all references to old paths
grep -r "old_path_or_name" --include="*.md" <0_context_root>/

# Update navigation documents:
# - universal_init_prompt.md (Quick Reference table)
# - MASTER_DOCUMENTATION_INDEX.md
# - SYSTEM_OVERVIEW.md
# - Any layer-specific init prompts
```

**Verify navigation works:**
- Follow paths from `universal_init_prompt.md` to new locations
- Ensure agents can find the restructured content

See `traversal_update_protocol.md` for full verification checklist.

<!-- section_id: "e8e9d5d2-ea3f-4f37-8d89-3d809ab876b6" -->
### 7. Commit and Push

```bash
git add -A
git commit -m "Restructure to layer system and migrate content from legacy

- Created layer_N/ and layer_N+1/ structure
- Migrated content from 0_context/legacy_* to proper locations
- Updated traversal documentation with new paths
- Removed legacy folders after verification

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

---

<!-- section_id: "94571b8c-1238-41d4-8857-de8be1081359" -->
## Common Mistakes

| Mistake | Consequence | Prevention |
|---------|-------------|------------|
| Create structure without migrating content | Empty folders, orphaned content | Always run migration step |
| Delete legacy before verifying | Lost content | Check file counts first |
| Migrate structure but not status.json | Lost progress tracking | Include status files |
| Forget nested features | Features stuck in old naming | Check layer_N+1 content |
| **Skip traversal doc updates** | **Agents can't find content** | **Always update navigation docs** |
| Hardcode paths without verification | Broken links after moves | Use relative paths, verify |

---

<!-- section_id: "443305f9-2295-4446-b1aa-7619b5c1a1cb" -->
## Migration Patterns

<!-- section_id: "7ec53c60-2304-4ec2-a57e-ddd029f25141" -->
### Pattern A: 0_context to layer_N

```
FROM: project/0_context/layer_1_project/1.02_sub_layers/
TO:   project/layer_4/layer_4_02_sub_layers/

FROM: project/0_context/layer_1_project/1.99_stages/
TO:   project/layer_4/layer_4_99_stages/

FROM: project/0_context/layer_2_features/
TO:   project/layer_5/layer_5_features/
```

<!-- section_id: "c1d31a5a-3940-4054-81a5-1be946124da9" -->
### Pattern B: Old N.xx at root to layer_N/

```
FROM: project/2.02_sub_layers/sub_layer_2.01_*/
TO:   project/layer_4/layer_4_02_sub_layers/sub_layer_4.01_*/

FROM: project/2.99_stages/stage_2.01_*/
TO:   project/layer_4/layer_4_99_stages/stage_4.01_*/
```

<!-- section_id: "b80af094-1a22-4578-899d-fb9ad1671868" -->
### Pattern C: Renaming features/components

```
FROM: layer_2_feature_* or layer_3_feature_*
TO:   layer_5_feature_* (at proper nesting level)

FROM: layer_3_subx3_feature_*
TO:   layer_5_feature_* (remove "sub_" if not same-type nesting)
```

---

<!-- section_id: "211f1c0a-c0ca-4724-8128-e33232e83f23" -->
## Verification Commands

```bash
# List all files in new structure (should have actual content)
find <project>/layer_4 -type f ! -name ".gitkeep" -name "*.md"

# Check for remaining legacy folders (should be empty after cleanup)
find <project> -type d \( -name "legacy*" -o -name "0_context" \) 2>/dev/null

# Verify status files exist
find <project> -name "status_*.json"
```

---

<!-- section_id: "6e045dde-681a-47e8-90de-f5be0cff87a0" -->
## Related Documents

- `traversal_update_protocol.md` - **Path verification after changes** (read this!)
- `../README.md` - Structural change checklist (which docs to update)
- `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/FLEXIBLE_LAYERING_SYSTEM.md` - Layer structure reference
- `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/` - Templates for new structures
