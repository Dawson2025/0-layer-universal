<!-- derived_from: "dfaeba9f-1ff6-4d76-b05e-1acb7331c5f3" -->
# AutoGen Agent Context

## Identity
Stage 11 (archives) for the dynamic_memory research sub-feature.
- **Parent**: `../../0AGNOSTIC.md`
- **Purpose**: Archived versions and history








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
