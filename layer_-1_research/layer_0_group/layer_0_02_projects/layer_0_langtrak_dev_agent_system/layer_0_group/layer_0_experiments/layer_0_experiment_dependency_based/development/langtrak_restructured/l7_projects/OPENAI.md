<!-- derived_from: "a6706b6b-0d1c-45aa-9db9-0b856c3654c5" -->
# OpenAI Context

## Identity

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


## Current Status

**Phase**: Routes extracted — dashboard, menu, project CRUD, migration, sharing
**Routes file**: routes.py (index, dashboard, main-menu, project CRUD, cloud migration)

## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
