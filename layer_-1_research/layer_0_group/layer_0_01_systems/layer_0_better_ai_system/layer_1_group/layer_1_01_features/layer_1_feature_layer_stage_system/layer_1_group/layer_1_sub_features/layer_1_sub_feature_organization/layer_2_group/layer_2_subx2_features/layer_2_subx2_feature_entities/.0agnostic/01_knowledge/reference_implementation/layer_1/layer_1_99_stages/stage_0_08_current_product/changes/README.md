---
resource_id: "588f2669-8d31-407e-8d6d-930e8191e1a5"
resource_type: "readme_knowledge"
resource_name: "README"
---
# Changes

Procedures and protocols for making changes to the layer/stage system.

**Last Updated:** 2026-01-15

<!-- section_id: "22d90d9b-5581-4ee5-832a-73c698d2826a" -->
## Purpose

This folder contains:
- Restructuring procedures
- Migration protocols
- Traversal/navigation updates
- Renaming conventions
- System modification checklists

<!-- section_id: "618a2dcb-3556-4b00-b79c-61feb0d5bd87" -->
## Contents

| Document | Purpose |
|----------|---------|
| `restructuring_migration_protocol.md` | How to restructure projects while ensuring content is migrated |
| `traversal_update_protocol.md` | **How to update navigation docs after ANY path change** |

<!-- section_id: "87d4a877-3da2-4d9b-88d1-17371c0d5433" -->
## Key Principles

<!-- section_id: "317ac403-830e-48f8-8346-dfc2569e9997" -->
### 1. Content Migration
**Structural changes and content migration must happen together.** Creating new folder structures without migrating the actual content leaves orphaned legacy folders.

<!-- section_id: "d3f33a70-b732-40b2-b670-8bf5f5c74202" -->
### 2. Traversal Updates
**Every path change requires navigation doc updates.** If agents can't navigate to the new paths, the restructuring is incomplete. Always:
- Update `universal_init_prompt.md` Quick Reference
- Update `MASTER_DOCUMENTATION_INDEX.md`
- Verify paths with grep/find before committing

<!-- section_id: "c163fdc7-916f-462c-b5bb-80da9c15ac70" -->
## Change Checklist (Quick Reference)

When making ANY structural change:

1. [ ] Make the structural change (rename, move, create)
2. [ ] Migrate content (if applicable)
3. [ ] `grep -r "old_path"` to find references
4. [ ] Update all navigation documents
5. [ ] Verify an agent can navigate from init prompt to new location
6. [ ] Commit with descriptive message

<!-- section_id: "f94c7445-abe5-478d-abdf-a983d6fb4157" -->
## Related

- `../README.md` - System management overview
- `../setup/` - Entity creation guides
- `../plans/` - Planning documents before making changes
- `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/` - Templates for new structures
