---
resource_id: "669edf58-9d3e-4a23-acda-126d911ac87c"
resource_type: "document"
resource_name: "l3_users_agent"
---
# L3 Users Agent

**Role**: User Identity Layer Specialist
**Class**: UsersAgent (extends LayerAgent)
**Layer**: 3
**Provides**: IUserProvider
**Depends On**: IStorageProvider, IAuthProvider (from L2)

---

## Sub-Layers (3)

| ID | Sub-Layer | Depends On | Purpose |
|----|-----------|------------|---------|
| L3.1 | User Model | — | `User` class, database table, core fields |
| L3.2 | Profiles | L3.1 | User preferences, display settings, avatar |
| L3.3 | Sessions | L3.1 | Session management, active session state |

## Internal Dependency Shape: Sequence

```
L3.1 User Model → L3.2 Profiles → L3.3 Sessions
```

## Context Model (~500 tokens)

### STATIC
- Layer identity, sub-layer list
- IUserProvider interface definition (3 methods)
- Neighbor interfaces: IStorageProvider (4 methods), IAuthProvider (4 methods)

### ON-DEMAND
- User model schema
- Profile preferences structure
- Session management implementation

## Scope Boundaries

**In scope**: User identity, profiles, sessions, preferences
**Out of scope**: Authentication flows (→ L2), phoneme data (→ L4), projects (→ L7)
