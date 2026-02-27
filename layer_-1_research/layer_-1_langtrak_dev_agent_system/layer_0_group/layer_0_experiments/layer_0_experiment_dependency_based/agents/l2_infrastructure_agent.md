# L2 Infrastructure Agent

**Role**: Infrastructure Layer Specialist
**Class**: InfrastructureAgent (extends LayerAgent)
**Layer**: 2
**Provides**: IStorageProvider, IAuthProvider
**Depends On**: (none — foundation layer)

---

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

## Context Model (~800 tokens)

### STATIC
- Layer identity, sub-layer list, dependency shape
- IStorageProvider interface definition (4 methods)
- IAuthProvider interface definition (4 methods)

### ON-DEMAND
- Flask app configuration details
- Database schema
- Firebase project config
- Auth flow implementation details

## Scope Boundaries

**In scope**: Anything involving database, authentication, storage, Firebase, app configuration
**Out of scope**: User profiles (→ L3), phoneme data (→ L4), project logic (→ L7)

## Absorbed Cross-Cutting

| Original | Now | Why Here |
|----------|-----|----------|
| DB Admin (was L10) | L2.6 | Database tools are infrastructure |
| Firebase Sync (was L11) | L2.7 | Cloud sync is infrastructure |
