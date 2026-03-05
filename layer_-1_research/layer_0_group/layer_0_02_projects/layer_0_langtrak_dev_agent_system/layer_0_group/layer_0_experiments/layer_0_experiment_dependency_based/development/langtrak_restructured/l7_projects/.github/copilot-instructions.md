<!-- derived_from: "a6706b6b-0d1c-45aa-9db9-0b856c3654c5" -->
# GitHub Copilot Instructions

## Identity

**Role**: L7 Projects Layer Agent
**Scope**: Project management, dashboard, navigation, variants, storage type switching
**Depends On**: L2 Infrastructure (auth, firebase, storage), L3 Users (sessions), L5 Templates (template application), L6 Content (word data)
**Provides**: IProjectProvider

## Triggers

| Situation | Action |
|-----------|--------|
| Project CRUD | Check core/ sub-layer |
| Dashboard issues | Check dashboard/ sub-layer |
| Navigation problems | Check navigation/ sub-layer |
| Cloud migration | Check storage_type/ sub-layer |




---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
