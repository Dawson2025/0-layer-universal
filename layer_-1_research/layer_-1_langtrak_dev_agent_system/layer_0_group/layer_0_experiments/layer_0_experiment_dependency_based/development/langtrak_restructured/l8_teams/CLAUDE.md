# Claude Code Context

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
