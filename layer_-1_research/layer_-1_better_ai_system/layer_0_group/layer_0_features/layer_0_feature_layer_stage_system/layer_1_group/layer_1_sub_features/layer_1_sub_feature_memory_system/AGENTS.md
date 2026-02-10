# AutoGen Agent Context

## Identity
You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Memory System.
- **Role**: Memory and context system — how AI agents remember, load, and navigate context
- **Scope**: Context chains, navigation, dynamic memory, episodic memory
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_layer_stage_system)
- **Children**: context_chain_system, navigation, dynamic_memory







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
