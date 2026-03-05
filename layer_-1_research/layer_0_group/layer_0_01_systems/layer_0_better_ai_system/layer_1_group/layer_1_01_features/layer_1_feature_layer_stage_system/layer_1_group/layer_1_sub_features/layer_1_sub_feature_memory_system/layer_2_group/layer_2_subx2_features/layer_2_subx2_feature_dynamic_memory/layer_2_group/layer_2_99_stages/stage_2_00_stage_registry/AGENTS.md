<!-- derived_from: "04179c02-c1cf-4e36-b0e0-2f51d35d195c" -->
# AutoGen Agent Context

## Identity
Stage 00 (stage_registry) for the dynamic_memory research sub-feature.
- **Parent**: `../../0AGNOSTIC.md`
- **Purpose**: Stage metadata and registration








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
