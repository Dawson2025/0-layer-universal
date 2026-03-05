---
resource_id: "e72c7ddc-b94f-45c8-b75d-b882442dff20"
resource_type: "document"
resource_name: "APPLYING_SUB_FEATURE_PATTERN"
---
# Applying Sub-Feature Pattern Across All Features

<!-- section_id: "34d6acb9-18d2-4a55-ae8f-dcd2e2284f63" -->
## Strategy

Based on the routes analysis, here's how to apply the sub-feature pattern to each major feature:

<!-- section_id: "a69c6156-3d01-411b-98e6-272b939dbedb" -->
## 1. Projects Feature

**Routes Found (10 routes):**
- `/projects` - List projects
- `/projects/group/<group_id>` - Group projects
- `/projects/create` - Create project
- `/projects/<id>/migrate-to-cloud` - Cloud migration
- `/projects/<id>/fork-to-local` - Fork to local
- `/projects/<id>/sync-to-cloud` - Sync to cloud
- `/projects/<id>/sync-from-cloud` - Sync from cloud
- `/projects/<id>/enter` - Enter project context
- `/projects/exit` - Exit project context
- `/projects/<id>/edit` - Edit project

**Proposed Sub-Modules:**
```
features/projects/
├── display.py          # List, view projects
├── creation.py         # Create new projects
├── editing.py          # Edit project metadata
├── storage_ops.py      # Cloud migration, sync, fork
├── context.py          # Enter/exit project context
└── api.py              # API endpoints
```

**Concerns Separated:**
- Display (1 route)
- Creation (1 route)
- Editing (1 route)
- Storage operations (4 routes) - migrate, fork, sync
- Context management (2 routes) - enter, exit
- Already have: metadata.py

**Parallel Capacity:** 5 agents

<!-- section_id: "88a0a7b2-5ce5-4edf-b482-70eb43844e85" -->
## 2. Phonemes Feature

**Routes Found (4 routes):**
- `/phonemes` - Overview/menu
- `/phonemes/flat` - Flat view
- `/phonemes/nested` - Nested view
- `/phonemes/full` - Full hierarchy view

**Proposed Sub-Modules:**
```
features/phonemes/
├── display.py          # Overview/menu
├── viewing.py          # All display modes (flat, nested, full)
├── frequency.py        # Frequency calculation logic
└── api.py              # API endpoints for phoneme CRUD
```

**Concerns Separated:**
- Display menu (1 route)
- Viewing modes (3 routes)
- Frequency management (logic)
- API operations

**Parallel Capacity:** 3-4 agents

<!-- section_id: "a9ce1aeb-57dd-490e-96eb-b00cefec8003" -->
## 3. Admin Feature

**Routes Found (4 routes + many APIs):**
- `/admin` - Admin dashboard
- `/admin/phonemes` - Phoneme management
- `/admin/templates` - Template system
- `/admin/storage` - Storage management

**Proposed Sub-Modules:**
```
features/admin/
├── dashboard.py            # Admin landing page
├── phoneme_management.py   # Phoneme admin operations
├── template_system.py      # Template import/export/apply
├── storage_management.py   # Storage admin operations
├── database_tools.py       # DB maintenance utilities
└── api.py                  # Admin API endpoints
```

**Concerns Separated:**
- Dashboard (1 route)
- Phoneme management (1 route + APIs)
- Template system (1 route + APIs)
- Storage management (1 route)
- Database tools (APIs)
- Bulk operations (APIs)

**Parallel Capacity:** 5-6 agents

<!-- section_id: "c229c4fe-9001-446d-bbdc-800966d692f5" -->
## 4. Groups Feature

**Already has routes extracted, but can be organized better:**

**Proposed Sub-Modules:**
```
features/groups/
├── display.py      # List groups, view group details
├── creation.py     # Create new groups
├── membership.py   # Manage members, invitations
├── sharing.py      # Share projects with groups
└── api.py          # Group API endpoints
```

**Parallel Capacity:** 4 agents

<!-- section_id: "c5cb4d15-bb55-4b35-af67-7375b9d44a5d" -->
## Summary

| Feature | Routes | Sub-Modules | Agents |
|---------|--------|-------------|--------|
| **words** | 6 + 5 APIs | 5 modules | 5 ✅ DONE |
| **projects** | 10 | 5 modules | 5 |
| **phonemes** | 4 | 4 modules | 4 |
| **admin** | 4 + APIs | 6 modules | 6 |
| **groups** | ~6 | 4 modules | 4 |

**Total Parallel Capacity:** 24+ agents across all features!

<!-- section_id: "30bd56a1-6836-4945-b82c-512e7bf5cd9f" -->
## Implementation Order

1. ✅ **Words** - COMPLETE (demonstrated pattern)
2. **Projects** - HIGH PRIORITY (many routes, complex)
3. **Admin** - HIGH PRIORITY (many APIs)
4. **Phonemes** - MEDIUM (simpler, fewer routes)
5. **Groups** - LOW (already mostly extracted)

<!-- section_id: "b8ba7bfa-1925-4c34-aa18-53110872dded" -->
## Pattern Applied

For each feature:
1. Analyze routes and identify distinct concerns
2. Create one file per concern
3. Keep shared logic in models.py or utils.py
4. Update __init__.py to import all sub-modules
5. Move templates to feature/templates/
6. Create focused tests for each sub-module
