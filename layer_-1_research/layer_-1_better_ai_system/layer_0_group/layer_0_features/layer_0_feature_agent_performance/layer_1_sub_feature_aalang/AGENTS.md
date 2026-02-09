# AutoGen Agent Context

## Identity

You are an agent at **Layer 1** (Features), **SubFeature**: AALang Integration.

- **Role**: Research into AALang/GAB integration with the layer-stage system
- **Scope**: GAB agent definitions, JSON-LD navigation, mode/actor/persona patterns
- **Parent**: `../0AGNOSTIC.md`
- **Children**: None (leaf node -- contains working documents)







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
