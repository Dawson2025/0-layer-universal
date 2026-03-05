<!-- derived_from: "3283e3a7-922a-4857-be48-32b99bc92897" -->
# AutoGen Agent Context

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

## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
