<!-- derived_from: "95eb30f5-0216-43e9-8408-49dbfc41eaa4" -->
# AutoGen Agent Context

## Identity

**Role**: L8 Teams Layer Agent
**Scope**: Team/group management, membership, invitations, project sharing
**Depends On**: L2 Infrastructure (auth, firebase), L3 Users (sessions), L7 Projects (project data)
**Provides**: ICollaborationProvider

## Key Behaviors

### Sub-layers
- L8.1 Core: Group/team CRUD, group detail views
- L8.2 Membership: Member management (add, remove, roles)
- L8.3 Invites: Invitation system (tokens, join via link)
- L8.4 Project Sharing: Share projects with groups, manage shares

### Dependency Shape
DAG — Core is foundation; Membership and Invites depend on Core; Project Sharing depends on Core and Membership

## Triggers

| Situation | Action |
|-----------|--------|
| Group CRUD | Check core/ sub-layer |
| Member management | Check membership/ sub-layer |
| Invitation issues | Check invites/ sub-layer |
| Project sharing | Check project_sharing/ sub-layer |


## Current Status

**Phase**: Routes extracted — group CRUD, membership, invites, project sharing
**Routes file**: routes.py (group routes, member management, invite links, project share/unshare)

## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
