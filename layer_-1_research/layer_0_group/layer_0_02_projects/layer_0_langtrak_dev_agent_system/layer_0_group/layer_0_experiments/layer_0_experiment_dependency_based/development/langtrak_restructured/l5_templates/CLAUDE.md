<!-- derived_from: "3283e3a7-922a-4857-be48-32b99bc92897" -->
# Claude Code Context

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
