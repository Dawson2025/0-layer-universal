<!-- derived_from: "a6706b6b-0d1c-45aa-9db9-0b856c3654c5" -->
# Claude Code Context

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

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
