# AutoGen Agent Context

## Identity
You are an agent at **Layer 0** (Feature), **Feature**: Layer-Stage System.
- **Role**: Central pillar of the better_ai_system — the layer-stage framework that organizes all AI context hierarchically
- **Scope**: Layer-stage architecture, entity structure, recursive organization, context loading
- **Parent**: `../0AGNOSTIC.md` (layer_0_features)
- **Children**: memory_system, organization, multi_agent_system, tool_and_app_agnostic









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
