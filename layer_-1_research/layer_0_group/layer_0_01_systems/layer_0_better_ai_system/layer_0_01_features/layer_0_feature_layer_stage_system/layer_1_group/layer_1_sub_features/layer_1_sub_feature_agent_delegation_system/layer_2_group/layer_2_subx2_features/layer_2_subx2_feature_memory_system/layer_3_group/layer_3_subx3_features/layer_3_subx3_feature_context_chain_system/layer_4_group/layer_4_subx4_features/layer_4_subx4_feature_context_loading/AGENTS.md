# AutoGen Agent Context

## Identity
You are an agent at **Layer 4** (Sub-Feature), **Sub-Feature**: Context Loading.
- **Role**: Context loading process — how context is discovered, prioritized, and loaded into AI sessions
- **Scope**: Load order, priority resolution, context budget, on-demand loading strategies
- **Parent**: `../../../0AGNOSTIC.md` (layer_3_subx3_feature_context_chain_system)
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
