# AutoGen Agent Context

## Identity
You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Multi-Agent System.
- **Role**: Multi-agent coordination — how multiple AI agents collaborate within the layer-stage framework
- **Scope**: Agent hierarchy, orchestration, spawning, inter-agent communication, recursive coordination
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_layer_stage_system)
- **Children**: agent_hierarchy, orchestration







## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": "outputs/episodic/"
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
