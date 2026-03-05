<!-- derived_from: "0b002a42-cabe-40e5-a14b-b6261149b461" -->
# AutoGen Agent Context

## Identity
Stage 06 (development) for the memory_system research sub-feature.
- **Parent**: `../../0AGNOSTIC.md`
- **Purpose**: Implement solutions








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
