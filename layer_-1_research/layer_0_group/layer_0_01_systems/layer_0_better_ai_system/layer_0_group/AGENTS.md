<!-- derived_from: "f351b53f-90d5-464e-88ac-a751e6fb8d16" -->
# AutoGen Agent Context

## Identity
Internal structure container for the better_ai_system project.
- **Parent**: `../0AGNOSTIC.md` (layer_-1_better_ai_system)









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
