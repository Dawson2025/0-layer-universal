---
resource_id: "b6d2ab73-db3b-4ba8-8ee3-4e108f9499aa"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

entity_id: "a6706b6b-0d1c-45aa-9db9-0b856c3654c5"

**Role**: L7 Projects Layer Agent
**Scope**: Project management, dashboard, navigation, variants, storage type switching
**Depends On**: L2 Infrastructure (auth, firebase, storage), L3 Users (sessions), L5 Templates (template application), L6 Content (word data)
**Provides**: IProjectProvider

## Key Behaviors

### Sub-layers
- L7.1 Core: Project CRUD, enter/exit, edit, rename, branch
- L7.2 Dashboard: User dashboard view, project listing
- L7.3 Navigation: Main menu, navigation structure
- L7.4 Variants: Variant menu system
- L7.5 Storage Type: Cloud migration, storage type switching

### Dependency Shape
Star — Core is hub; Dashboard, Navigation, Variants, Storage Type all depend on Core

## Triggers

| Situation | Action |
|-----------|--------|
| Project CRUD | Check core/ sub-layer |
| Dashboard issues | Check dashboard/ sub-layer |
| Navigation problems | Check navigation/ sub-layer |
| Cloud migration | Check storage_type/ sub-layer |

# ── Current Status ──

## Current Status

**Phase**: Routes extracted — dashboard, menu, project CRUD, migration, sharing
**Routes file**: routes.py (index, dashboard, main-menu, project CRUD, cloud migration)

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Core module | core/ |
| Parent context | ../0AGNOSTIC.md |
