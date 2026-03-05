---
resource_id: "0a75420e-8f96-4884-80e5-756f5960aa84"
resource_type: "document"
resource_name: "APPLYING_SUB_FEATURE_PATTERN"
---
# Applying Sub-Feature Pattern Across All Features

<!-- section_id: "9dae7922-1138-4f14-a53b-287e68d82c83" -->
## Strategy

Based on the routes analysis, here's how to apply the sub-feature pattern to each major feature:

<!-- section_id: "4bb809fb-81a9-4ae4-905c-86084fd657e1" -->
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

<!-- section_id: "00e71a9d-e7cf-4958-99f5-e31c3e6bf991" -->
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

<!-- section_id: "e47a54d1-96d9-4bdd-8c73-c7b21eaac084" -->
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

<!-- section_id: "fbb394f5-a9c6-4cda-832c-a09026c778d2" -->
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

<!-- section_id: "37acc430-7f25-49e3-83ec-9e2310fd659b" -->
## Summary

| Feature | Routes | Sub-Modules | Agents |
|---------|--------|-------------|--------|
| **words** | 6 + 5 APIs | 5 modules | 5 ✅ DONE |
| **projects** | 10 | 5 modules | 5 |
| **phonemes** | 4 | 4 modules | 4 |
| **admin** | 4 + APIs | 6 modules | 6 |
| **groups** | ~6 | 4 modules | 4 |

**Total Parallel Capacity:** 24+ agents across all features!

<!-- section_id: "493e58d0-e949-4835-9471-9259f8d229a4" -->
## Implementation Order

1. ✅ **Words** - COMPLETE (demonstrated pattern)
2. **Projects** - HIGH PRIORITY (many routes, complex)
3. **Admin** - HIGH PRIORITY (many APIs)
4. **Phonemes** - MEDIUM (simpler, fewer routes)
5. **Groups** - LOW (already mostly extracted)

<!-- section_id: "5f35983e-85a7-4e27-bdb0-9f2cedecea63" -->
## Pattern Applied

For each feature:
1. Analyze routes and identify distinct concerns
2. Create one file per concern
3. Keep shared logic in models.py or utils.py
4. Update __init__.py to import all sub-modules
5. Move templates to feature/templates/
6. Create focused tests for each sub-module
