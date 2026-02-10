# AutoGen Agent Context

## Identity
You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: Context Chain System.
- **Role**: Context chain architecture — how context flows through the layer-stage hierarchy
- **Scope**: Chain construction, static/dynamic context, fixed/configurable dimensions, chain optimization
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_memory_system)
- **Children**: chain_visualization, context_loading







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
