# L8 Teams Agent

**Role**: Collaboration Layer Specialist
**Class**: TeamsAgent (extends LayerAgent)
**Layer**: 8
**Provides**: ICollaborationProvider
**Depends On**: IProjectProvider (from L7), IUserProvider (from L3)

---

## Sub-Layers (4)

| ID | Sub-Layer | Depends On | Purpose |
|----|-----------|------------|---------|
| L8.1 | Team Model | — | Team class, database table |
| L8.2 | Membership | L8.1 | Member management, roles |
| L8.3 | Invites | L8.2 | Invite codes, invite flow |
| L8.4 | Project Sharing | L8.1, L7 | Share projects with team members (cross-layer ref to L7) |

## Internal Dependency Shape: Short Sequence + Cross-Layer Reference

```
L8.1 Team Model → L8.2 Membership → L8.3 Invites
       |
L8.4 Project Sharing (depends on L8.1 + L7 Project interface)
```

## Context Model (~500 tokens)

### STATIC
- Layer identity, sub-layer list, dependency shape
- ICollaborationProvider interface definition (3 methods)
- Neighbor interfaces: IProjectProvider (3 methods), IUserProvider (3 methods)

### ON-DEMAND
- Team model schema
- Membership roles and permissions
- Invite flow implementation
- Project sharing access control

## Scope Boundaries

**In scope**: Teams, membership, invites, project sharing
**Out of scope**: Project logic (→ L7), user identity (→ L3), auth (→ L2)

## Cross-Layer References

L8 is unique in that it depends on TWO non-adjacent layers:
- L7 (IProjectProvider) — for project sharing
- L3 (IUserProvider) — for user identity in membership

This is the only layer that skips the linear chain.
