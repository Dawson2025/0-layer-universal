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

<!-- section_id: "de491a2a-35ed-4437-83e9-5d62b427d982" -->
## Sub-Layers (3)

| ID | Sub-Layer | Depends On | Purpose |
|----|-----------|------------|---------|
| L3.1 | User Model | — | `User` class, database table, core fields |
| L3.2 | Profiles | L3.1 | User preferences, display settings, avatar |
| L3.3 | Sessions | L3.1 | Session management, active session state |

<!-- section_id: "df000ffb-85d7-4c7b-a637-762cbce3f4f9" -->
## Internal Dependency Shape: Sequence

```
L3.1 User Model → L3.2 Profiles → L3.3 Sessions
```

<!-- section_id: "8bef243e-bd15-4424-9384-3949e18cdf54" -->
## Context Model (~500 tokens)

<!-- section_id: "bd7efe1e-da7b-44a1-a9f1-17db24ae191f" -->
### STATIC
- Layer identity, sub-layer list
- IUserProvider interface definition (3 methods)
- Neighbor interfaces: IStorageProvider (4 methods), IAuthProvider (4 methods)

<!-- section_id: "4ad152a7-598a-420e-bc0d-4a2d0cb695c0" -->
### ON-DEMAND
- User model schema
- Profile preferences structure
- Session management implementation

<!-- section_id: "5e21cc81-0ac4-4959-85e2-13ac163d8cce" -->
## Scope Boundaries

**In scope**: User identity, profiles, sessions, preferences
**Out of scope**: Authentication flows (→ L2), phoneme data (→ L4), projects (→ L7)
