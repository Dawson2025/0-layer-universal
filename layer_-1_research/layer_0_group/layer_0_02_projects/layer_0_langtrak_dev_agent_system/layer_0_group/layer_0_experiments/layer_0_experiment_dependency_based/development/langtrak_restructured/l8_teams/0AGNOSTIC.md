---
resource_id: "c3684647-2af7-4c2b-a7c1-3be9a2aac58e"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "8601cf3d-e0d5-459c-9603-34c1c54c4db7" -->
## Identity

entity_id: "95eb30f5-0216-43e9-8408-49dbfc41eaa4"

**Role**: L8 Teams Layer Agent
**Scope**: Team/group management, membership, invitations, project sharing
**Depends On**: L2 Infrastructure (auth, firebase), L3 Users (sessions), L7 Projects (project data)
**Provides**: ICollaborationProvider

<!-- section_id: "377d8841-49d5-4b13-a988-715fc60f3ebc" -->
## Key Behaviors

<!-- section_id: "448e4b6f-b721-44c4-8547-b4d872c65aa8" -->
### Sub-layers
- L8.1 Core: Group/team CRUD, group detail views
- L8.2 Membership: Member management (add, remove, roles)
- L8.3 Invites: Invitation system (tokens, join via link)
- L8.4 Project Sharing: Share projects with groups, manage shares

<!-- section_id: "8dc7cedc-6903-418b-9a2c-f3df3052e3fd" -->
### Dependency Shape
DAG — Core is foundation; Membership and Invites depend on Core; Project Sharing depends on Core and Membership

<!-- section_id: "6e52c387-10f1-4dda-8cad-56ba5d328d7c" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Group CRUD | Check core/ sub-layer |
| Member management | Check membership/ sub-layer |
| Invitation issues | Check invites/ sub-layer |
| Project sharing | Check project_sharing/ sub-layer |

# ── Current Status ──

<!-- section_id: "24171f91-23fc-466a-80d0-b8d36e785368" -->
## Current Status

**Phase**: Routes extracted — group CRUD, membership, invites, project sharing
**Routes file**: routes.py (group routes, member management, invite links, project share/unshare)

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

<!-- section_id: "38b39ede-6790-4143-b514-0d8cbe04b8a7" -->
## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Core module | core/ |
| Parent context | ../0AGNOSTIC.md |
