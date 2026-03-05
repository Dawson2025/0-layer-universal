<!-- derived_from: "22d3523f-49fa-45d2-a865-f36d53268b4e" -->
# AutoGen Agent Context

## Identity
Stage 06 (development) for the navigation research sub-feature.
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
