---
resource_id: "45aa82e3-bb13-469d-bb71-ee2769fc35f4"
resource_type: "readme_document"
resource_name: "README"
---
# Changes

Procedures and protocols for making changes to the layer/stage system.

**Last Updated:** 2026-01-15

<!-- section_id: "39fa31ba-70a7-4b28-aad7-f2715c0e8704" -->
## Purpose

This folder contains:
- Restructuring procedures
- Migration protocols
- Traversal/navigation updates
- Renaming conventions
- System modification checklists

<!-- section_id: "abc965b5-de58-4590-8d88-b277ede82faf" -->
## Contents

| Document | Purpose |
|----------|---------|
| `restructuring_migration_protocol.md` | How to restructure projects while ensuring content is migrated |
| `traversal_update_protocol.md` | **How to update navigation docs after ANY path change** |

<!-- section_id: "b6da2da0-8619-4988-b4b8-5a04b7e72684" -->
## Key Principles

<!-- section_id: "c6c1c382-25db-4e88-821c-d8109a3fb8b9" -->
### 1. Content Migration
**Structural changes and content migration must happen together.** Creating new folder structures without migrating the actual content leaves orphaned legacy folders.

<!-- section_id: "b8eb99c1-1e37-441a-acb9-5fbd321aff21" -->
### 2. Traversal Updates
**Every path change requires navigation doc updates.** If agents can't navigate to the new paths, the restructuring is incomplete. Always:
- Update `universal_init_prompt.md` Quick Reference
- Update `MASTER_DOCUMENTATION_INDEX.md`
- Verify paths with grep/find before committing

<!-- section_id: "d1ce34fd-7647-43dc-9bc5-3bb927c8ad1f" -->
## Change Checklist (Quick Reference)

When making ANY structural change:

1. [ ] Make the structural change (rename, move, create)
2. [ ] Migrate content (if applicable)
3. [ ] `grep -r "old_path"` to find references
4. [ ] Update all navigation documents
5. [ ] Verify an agent can navigate from init prompt to new location
6. [ ] Commit with descriptive message

<!-- section_id: "8749785b-1dcb-4ace-99ab-5b312e5f12a6" -->
## Related

- `../README.md` - System management overview
- `../setup/` - Entity creation guides
- `../plans/` - Planning documents before making changes
- `../../layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/` - Templates for new structures
