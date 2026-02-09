# AutoGen Agent Context

## Identity

You are an agent at **Layer 2** (Features), **SubFeature**: Context Chains.

- **Role**: Research into how context flows through the system via chains
- **Scope**: Context loading, chain visualization, tool-agnostic context distribution
- **Parent**: `../0AGNOSTIC.md` (knowledge_and_memory)
- **Children**: `layer_3_sub_feature_context_loading/`, `layer_3_sub_feature_chain_visualization/`, `layer_3_sub_feature_tool_agnostic/`







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
