---
resource_id: "48c06808-7ce3-4f75-a3c1-6a0e8bc94229"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

entity_id: "3283e3a7-922a-4857-be48-32b99bc92897"

**Role**: L5 Templates Layer Agent
**Scope**: Template creation, application, cloud sharing, phoneme selection templates
**Depends On**: L2 Infrastructure (auth, firebase, storage), L3 Users (sessions), L4 Phoneme System (phoneme data)
**Provides**: ITemplateProvider

## Key Behaviors

### Sub-layers
- L5.1 Core: Template CRUD, local template management
- L5.2 Admin: Template administration, import/export, cloud template management

### Dependency Shape
Sequence: Core → Admin (admin builds on core operations)

## Triggers

| Situation | Action |
|-----------|--------|
| Template CRUD | Check core/ sub-layer |
| Template admin/cloud | Check admin/ sub-layer |

# ── Current Status ──

## Current Status

**Phase**: Routes extracted — all template routes from monolithic app.py
**Routes file**: routes.py (template CRUD, cloud templates, import/export, phoneme templates)

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Parent context | ../0AGNOSTIC.md |
