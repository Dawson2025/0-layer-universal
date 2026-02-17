# AutoGen Agent Context

## Identity
You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Organization.
- **Role**: Structural organization of the layer-stage system — how entities, layers, and stages are arranged
- **Scope**: Entity structure, directory conventions, naming patterns, registry management
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_layer_stage_system)
- **Children**: entities









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
