# Gemini Context

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

## Gemini-Specific Notes

### Context Loading
Load detailed resources from .0agnostic/ when needed:
- rules/ - Behavioral constraints
- prompts/ - Task-specific prompts
- knowledge/ - Reference information
- agents/ - Agent definitions

### Session Continuity
Maintain episodic memory in .0agnostic/episodic_memory/:
- sessions/ - Timestamped session records
- changes/ - Divergence and conflict logs
- index.md - Searchable session index

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
