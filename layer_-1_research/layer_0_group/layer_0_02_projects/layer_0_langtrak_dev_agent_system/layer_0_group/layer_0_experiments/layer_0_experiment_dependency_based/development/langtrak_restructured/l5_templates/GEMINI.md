# Gemini Context

## Identity

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


## Current Status

**Phase**: Routes extracted — all template routes from monolithic app.py
**Routes file**: routes.py (template CRUD, cloud templates, import/export, phoneme templates)

## Gemini-Specific Notes

### Context Loading
Load detailed resources from .0agnostic/ when needed:
- rules/ - Behavioral constraints
- prompts/ - Task-specific prompts
- knowledge/ - Reference information
- agents/ - Agent definitions

### Session Continuity
Maintain episodic memory in .0agnostic/episodic_memory/:
- sessions/ - Timestamped session records
- changes/ - Divergence and conflict logs
- index.md - Searchable session index

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
