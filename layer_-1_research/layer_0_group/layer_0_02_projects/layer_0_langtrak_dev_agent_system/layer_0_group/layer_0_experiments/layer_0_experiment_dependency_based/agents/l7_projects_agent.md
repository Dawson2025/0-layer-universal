---
resource_id: "4b398eb5-11d6-4658-923a-09cf956220b2"
resource_type: "document"
resource_name: "l7_projects_agent"
---
# L7 Projects Agent

**Role**: Project Layer Specialist
**Class**: ProjectsAgent (extends LayerAgent)
**Layer**: 7
**Provides**: IProjectProvider
**Depends On**: IContentProvider (from L6)

---

## Sub-Layers (6)

| ID | Sub-Layer | Depends On | Purpose |
|----|-----------|------------|---------|
| L7.1 | Project Core | — | Project model, CRUD, metadata |
| L7.2 | Storage Type | L7.1 | Local (SQLite) vs cloud (Firestore) selection |
| L7.3 | Variants | L7.1 | Project duplication, forking, branching |
| L7.4 | Content Association | L7.1 | Links project to template and word collection |
| L7.5 | Dashboard | L7.1 | Project overview, stats, quick access (absorbed from L10) |
| L7.6 | Menu/Navigation | L7.1 | Main menu, navigation between projects (absorbed from L10) |

## Internal Dependency Shape: Star/Hub

```
              L7.1 Project Core
          /    |      |     \      \       \
   L7.2     L7.3   L7.4   L7.5   L7.6
  Storage  Variants Content Dashboard Menu
   Type              Assoc.
```

## Context Model (~600 tokens)

### STATIC
- Layer identity, sub-layer list, dependency shape
- IProjectProvider interface definition (3 methods)
- Neighbor interface: IContentProvider (4 methods)

### ON-DEMAND
- Project model schema
- Storage type switching logic
- Variant/fork implementation
- Dashboard metrics calculation
- Navigation routing

## Scope Boundaries

**In scope**: Project CRUD, storage type, variants, content association, dashboard, navigation
**Out of scope**: Content/words (→ L6), teams (→ L8), auth (→ L2)

## Absorbed Cross-Cutting

| Original | Now | Why Here |
|----------|-----|----------|
| Dashboard (was L10) | L7.5 | Project overview is a project view |
| Menu/Navigation (was L10) | L7.6 | Navigation is a project-level UI concern |
