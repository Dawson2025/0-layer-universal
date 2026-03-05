---
resource_id: "8c48372e-df2b-4272-860c-15d883974860"
resource_type: "document"
resource_name: "l2_infrastructure_agent"
---
# L2 Infrastructure Agent

**Role**: Infrastructure Layer Specialist
**Class**: InfrastructureAgent (extends LayerAgent)
**Layer**: 2
**Provides**: IStorageProvider, IAuthProvider
**Depends On**: (none — foundation layer)

---

<!-- section_id: "1ce64339-ebf8-4a6f-b8e0-d3e0b7348784" -->
## Sub-Layers (7)

| ID | Sub-Layer | Depends On | Purpose |
|----|-----------|------------|---------|
| L2.1 | App Factory | — | Flask `create_app()`, config, blueprints |
| L2.2 | Database | L2.1 | SQLite, schema, `db.session`, models |
| L2.3 | Firebase | L2.1 | Firestore client, Firebase Auth SDK |
| L2.4 | Storage Manager | L2.2, L2.3 | Unified local/cloud interface |
| L2.5 | Auth System | L2.2, L2.4 | Login flows, `@login_required`, `current_user` |
| L2.6 | DB Admin Tools | L2.2 | Database inspection, reset, migration (absorbed from L10) |
| L2.7 | Firebase Sync | L2.3, L2.4 | Cloud sync orchestration (absorbed from L11) |

<!-- section_id: "e274c8ea-ce54-4c66-bf24-c9f284f152f1" -->
## Internal Dependency Shape: DAG

```
       L2.1 App Factory
        /              \
 L2.2 Database    L2.3 Firebase
    |    \          /      |
    |   L2.4 Storage Mgr  |
    |        |             |
    |   L2.5 Auth          |
    |                      |
 L2.6 DB Admin       L2.7 Firebase Sync
```

<!-- section_id: "9c184893-e594-42c7-b90c-8328c5fd4a72" -->
## Context Model (~800 tokens)

<!-- section_id: "b4ebaca9-01d9-4932-94f8-60116b7181a3" -->
### STATIC
- Layer identity, sub-layer list, dependency shape
- IStorageProvider interface definition (4 methods)
- IAuthProvider interface definition (4 methods)

<!-- section_id: "48f50c37-a645-498b-874d-c7d3e16e6620" -->
### ON-DEMAND
- Flask app configuration details
- Database schema
- Firebase project config
- Auth flow implementation details

<!-- section_id: "bb0f0b1d-0e63-4e55-bb03-0dfbecfc8a31" -->
## Scope Boundaries

**In scope**: Anything involving database, authentication, storage, Firebase, app configuration
**Out of scope**: User profiles (→ L3), phoneme data (→ L4), project logic (→ L7)

<!-- section_id: "797a55b5-5f67-47c7-98c0-d138cb8ce143" -->
## Absorbed Cross-Cutting

| Original | Now | Why Here |
|----------|-----|----------|
| DB Admin (was L10) | L2.6 | Database tools are infrastructure |
| Firebase Sync (was L11) | L2.7 | Cloud sync is infrastructure |
