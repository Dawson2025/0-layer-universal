---
resource_id: "0e24a8c5-a593-4d43-b338-ec57eef46359"
resource_type: "document"
resource_name: "instructions"
---
# AutoGen Agent Context

<!-- section_id: "60e4f766-f710-406d-acfc-217c19fad722" -->
## Identity

**Role**: L7 Projects Layer Agent
**Scope**: Project management, dashboard, navigation, variants, storage type switching
**Depends On**: L2 Infrastructure (auth, firebase, storage), L3 Users (sessions), L5 Templates (template application), L6 Content (word data)
**Provides**: IProjectProvider

<!-- section_id: "c662c5aa-072b-4a92-9c99-1f57a0ca0985" -->
## Key Behaviors

<!-- section_id: "2e40f573-987d-4c31-a920-d60c96fb9bc6" -->
### Sub-layers
- L7.1 Core: Project CRUD, enter/exit, edit, rename, branch
- L7.2 Dashboard: User dashboard view, project listing
- L7.3 Navigation: Main menu, navigation structure
- L7.4 Variants: Variant menu system
- L7.5 Storage Type: Cloud migration, storage type switching

<!-- section_id: "dc43dfda-7002-4ad3-8aa9-c4a19ec39906" -->
### Dependency Shape
Star — Core is hub; Dashboard, Navigation, Variants, Storage Type all depend on Core

<!-- section_id: "dbf659dc-676f-493f-92d4-14566f9137f6" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Project CRUD | Check core/ sub-layer |
| Dashboard issues | Check dashboard/ sub-layer |
| Navigation problems | Check navigation/ sub-layer |
| Cloud migration | Check storage_type/ sub-layer |


<!-- section_id: "0c41ff9e-9e2a-4ef1-98c9-51575d273f6b" -->
## Current Status

**Phase**: Routes extracted — dashboard, menu, project CRUD, migration, sharing
**Routes file**: routes.py (index, dashboard, main-menu, project CRUD, cloud migration)

<!-- section_id: "d122099b-5259-4d84-9978-e15b76d01856" -->
## AutoGen-Specific Configuration

<!-- section_id: "5f5e8805-4275-4ec8-a600-2ccaf2a61d7b" -->
### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

<!-- section_id: "ece7da17-9467-4517-8684-7e65c4ec6000" -->
### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
