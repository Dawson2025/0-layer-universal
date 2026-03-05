<!-- derived_from: "95eb30f5-0216-43e9-8408-49dbfc41eaa4" -->
# GitHub Copilot Instructions

## Identity

**Role**: L8 Teams Layer Agent
**Scope**: Team/group management, membership, invitations, project sharing
**Depends On**: L2 Infrastructure (auth, firebase), L3 Users (sessions), L7 Projects (project data)
**Provides**: ICollaborationProvider

## Triggers

| Situation | Action |
|-----------|--------|
| Group CRUD | Check core/ sub-layer |
| Member management | Check membership/ sub-layer |
| Invitation issues | Check invites/ sub-layer |
| Project sharing | Check project_sharing/ sub-layer |




---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
