# AutoGen Agent Context

## Identity

You are an agent at **Layer 2** (Features), **SubFeature**: Memory Systems.

- **Role**: Research into agent memory mechanisms
- **Scope**: Dynamic memory, session persistence, episodic memory
- **Parent**: `../0AGNOSTIC.md` (knowledge_and_memory)
- **Children**: `layer_3_sub_feature_dynamic_memory/`







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
