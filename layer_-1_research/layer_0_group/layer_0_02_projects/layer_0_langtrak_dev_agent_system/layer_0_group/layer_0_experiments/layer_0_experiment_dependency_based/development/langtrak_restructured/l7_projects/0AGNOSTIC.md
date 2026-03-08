---
resource_id: "b6d2ab73-db3b-4ba8-8ee3-4e108f9499aa"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "d50e8cbe-248f-4d74-b787-f0f7006ac94c" -->
## Identity

entity_id: "a6706b6b-0d1c-45aa-9db9-0b856c3654c5"

**Role**: L7 Projects Layer Agent
**Scope**: Project management, dashboard, navigation, variants, storage type switching
**Depends On**: L2 Infrastructure (auth, firebase, storage), L3 Users (sessions), L5 Templates (template application), L6 Content (word data)
**Provides**: IProjectProvider

<!-- section_id: "5022e5fd-59dd-4700-864e-676e5a7d4c6f" -->
## Key Behaviors

<!-- section_id: "43bb6c8e-a30d-4762-a2e5-be1a72ec2148" -->
### Sub-layers
- L7.1 Core: Project CRUD, enter/exit, edit, rename, branch
- L7.2 Dashboard: User dashboard view, project listing
- L7.3 Navigation: Main menu, navigation structure
- L7.4 Variants: Variant menu system
- L7.5 Storage Type: Cloud migration, storage type switching

<!-- section_id: "7f028935-a9d5-40d0-a332-4e6c14859b52" -->
### Dependency Shape
Star — Core is hub; Dashboard, Navigation, Variants, Storage Type all depend on Core

<!-- section_id: "21eed893-722e-4758-985d-da72a2e69c2d" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Project CRUD | Check core/ sub-layer |
| Dashboard issues | Check dashboard/ sub-layer |
| Navigation problems | Check navigation/ sub-layer |
| Cloud migration | Check storage_type/ sub-layer |

# ── Current Status ──

<!-- section_id: "4df0cd76-85fa-467d-9655-acd77785693a" -->
## Current Status

**Phase**: Routes extracted — dashboard, menu, project CRUD, migration, sharing
**Routes file**: routes.py (index, dashboard, main-menu, project CRUD, cloud migration)

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

<!-- section_id: "aa00a06f-1f43-4ce3-975e-87ca105ca5e9" -->
## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Core module | core/ |
| Parent context | ../0AGNOSTIC.md |
