# AutoGen Agent Context

## Identity
Internal structure container for the memory_system entity.
- **Parent**: `../0AGNOSTIC.md`

## Contents
- `layer_1_00_layer_registry/` — Registry and proposals
- `layer_1_01_ai_manager_system/` — AI manager orchestration
- `layer_1_02_manager_handoff_documents/` — Handoff communication
- `layer_1_99_stages/` — Stage workflow (00-11)

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
