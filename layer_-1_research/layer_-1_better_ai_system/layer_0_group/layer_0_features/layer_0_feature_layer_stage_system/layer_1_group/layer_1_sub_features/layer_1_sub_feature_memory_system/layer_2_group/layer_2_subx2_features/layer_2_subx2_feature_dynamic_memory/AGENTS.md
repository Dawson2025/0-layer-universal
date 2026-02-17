# AutoGen Agent Context

## Identity
You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: Dynamic Memory.
- **Role**: Dynamic and episodic memory — runtime memory, session persistence, episodic recall
- **Scope**: Episodic memory bridge, session history, dynamic context loading, memory persistence
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_memory_system)
- **Children**: None (leaf entity)









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
