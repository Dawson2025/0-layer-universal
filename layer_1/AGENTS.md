# AutoGen Agent Context

## Identity
You are an AI agent working within the layer_1 (projects) context. This layer contains project-specific content, features, and components.


## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Universal rules**: Inherit from `../layer_0/.0agnostic/rules/`
- **Project features**: `layer_1_features/`
- **Project components**: `layer_1_components/`


## Key Behaviors



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
