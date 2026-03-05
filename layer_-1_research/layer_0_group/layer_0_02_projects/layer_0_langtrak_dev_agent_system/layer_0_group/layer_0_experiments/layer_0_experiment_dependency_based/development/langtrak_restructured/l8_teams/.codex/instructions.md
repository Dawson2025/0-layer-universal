---
resource_id: "7789748e-5bb6-40fc-83c4-d367b697ad5f"
resource_type: "document"
resource_name: "instructions"
---
# AutoGen Agent Context

<!-- section_id: "5e8058d9-f887-4e3e-9363-5886ed143106" -->
## Identity

**Role**: L8 Teams Layer Agent
**Scope**: Team/group management, membership, invitations, project sharing
**Depends On**: L2 Infrastructure (auth, firebase), L3 Users (sessions), L7 Projects (project data)
**Provides**: ICollaborationProvider

<!-- section_id: "4242b36a-71dc-45a5-94b1-0a0bacebe0a4" -->
## Key Behaviors

<!-- section_id: "79af8961-5cbb-41b4-91bf-f5004d89b53a" -->
### Sub-layers
- L8.1 Core: Group/team CRUD, group detail views
- L8.2 Membership: Member management (add, remove, roles)
- L8.3 Invites: Invitation system (tokens, join via link)
- L8.4 Project Sharing: Share projects with groups, manage shares

<!-- section_id: "85142d46-1565-4b32-883a-399499f664c0" -->
### Dependency Shape
DAG — Core is foundation; Membership and Invites depend on Core; Project Sharing depends on Core and Membership

<!-- section_id: "3dafde17-542b-4eff-b973-8a757d765082" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Group CRUD | Check core/ sub-layer |
| Member management | Check membership/ sub-layer |
| Invitation issues | Check invites/ sub-layer |
| Project sharing | Check project_sharing/ sub-layer |


<!-- section_id: "0e381e59-8a90-4483-a64e-7fd84237f0ef" -->
## Current Status

**Phase**: Routes extracted — group CRUD, membership, invites, project sharing
**Routes file**: routes.py (group routes, member management, invite links, project share/unshare)

<!-- section_id: "74926729-a541-4a47-b5d0-0b1952fd9cf1" -->
## AutoGen-Specific Configuration

<!-- section_id: "78b6c621-ff4d-4a8b-91f0-50de6f60f354" -->
### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

<!-- section_id: "c82b8858-9dfc-4013-9d01-c332002f4b59" -->
### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
