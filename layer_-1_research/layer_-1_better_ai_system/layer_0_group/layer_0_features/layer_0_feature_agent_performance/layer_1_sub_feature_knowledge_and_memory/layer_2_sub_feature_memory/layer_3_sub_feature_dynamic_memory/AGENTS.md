# AutoGen Agent Context

## Identity

You are an agent at **Layer 3** (Features), **SubFeature**: Dynamic Memory.

- **Role**: Research into dynamic (runtime) memory for agents
- **Scope**: Auto-memory, episodic memory, session-to-session continuity
- **Parent**: `../0AGNOSTIC.md` (memory)
- **Children**: None (leaf node)







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
