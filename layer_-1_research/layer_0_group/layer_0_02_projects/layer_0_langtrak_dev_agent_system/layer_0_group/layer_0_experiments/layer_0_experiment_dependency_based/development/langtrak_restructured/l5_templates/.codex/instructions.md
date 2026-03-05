---
resource_id: "e48d42f0-ee72-42ee-b4a7-0d33e1421431"
resource_type: "document"
resource_name: "instructions"
---
# AutoGen Agent Context

<!-- section_id: "677bf510-719e-4da0-b549-a358814b11f6" -->
## Identity

**Role**: L5 Templates Layer Agent
**Scope**: Template creation, application, cloud sharing, phoneme selection templates
**Depends On**: L2 Infrastructure (auth, firebase, storage), L3 Users (sessions), L4 Phoneme System (phoneme data)
**Provides**: ITemplateProvider

<!-- section_id: "edb757f0-9c84-47fa-9a0b-97b0082ae3a8" -->
## Key Behaviors

<!-- section_id: "ec0daec8-305c-4dcb-a50f-7e362d705327" -->
### Sub-layers
- L5.1 Core: Template CRUD, local template management
- L5.2 Admin: Template administration, import/export, cloud template management

<!-- section_id: "58781dc1-2d4f-487e-a829-833438e6f9da" -->
### Dependency Shape
Sequence: Core → Admin (admin builds on core operations)

<!-- section_id: "95ecf850-ee2e-43d3-afb5-c01d40815f43" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Template CRUD | Check core/ sub-layer |
| Template admin/cloud | Check admin/ sub-layer |


<!-- section_id: "eb6b992b-bec6-4e02-8ac5-68ac64ad56d1" -->
## Current Status

**Phase**: Routes extracted — all template routes from monolithic app.py
**Routes file**: routes.py (template CRUD, cloud templates, import/export, phoneme templates)

<!-- section_id: "8dd7267b-db1b-4eb9-b000-f422f86ac799" -->
## AutoGen-Specific Configuration

<!-- section_id: "5b9d8104-1231-4fec-95f0-427cccbd8a6a" -->
### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

<!-- section_id: "a25bd3cf-5965-45e1-b206-b9c45012d950" -->
### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
