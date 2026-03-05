---
resource_id: "48c06808-7ce3-4f75-a3c1-6a0e8bc94229"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "ad1738bb-9d52-4593-a6e1-e48cc088c1e9" -->
## Identity

entity_id: "3283e3a7-922a-4857-be48-32b99bc92897"

**Role**: L5 Templates Layer Agent
**Scope**: Template creation, application, cloud sharing, phoneme selection templates
**Depends On**: L2 Infrastructure (auth, firebase, storage), L3 Users (sessions), L4 Phoneme System (phoneme data)
**Provides**: ITemplateProvider

<!-- section_id: "d48ec9b6-bed6-433d-9ee8-d1ced3b61657" -->
## Key Behaviors

<!-- section_id: "69865f68-94bd-40af-a03b-54420d8b2613" -->
### Sub-layers
- L5.1 Core: Template CRUD, local template management
- L5.2 Admin: Template administration, import/export, cloud template management

<!-- section_id: "b6b05a2d-3169-4343-a2fa-2ee9faeba720" -->
### Dependency Shape
Sequence: Core → Admin (admin builds on core operations)

<!-- section_id: "bbbb837a-2733-47fb-9b75-b83764fca249" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Template CRUD | Check core/ sub-layer |
| Template admin/cloud | Check admin/ sub-layer |

# ── Current Status ──

<!-- section_id: "cd0fbc70-2f1f-4c22-a9e1-871b4afb5ddc" -->
## Current Status

**Phase**: Routes extracted — all template routes from monolithic app.py
**Routes file**: routes.py (template CRUD, cloud templates, import/export, phoneme templates)

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

<!-- section_id: "3515472d-7687-4d83-82d6-8d60fb5a64b2" -->
## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Parent context | ../0AGNOSTIC.md |
