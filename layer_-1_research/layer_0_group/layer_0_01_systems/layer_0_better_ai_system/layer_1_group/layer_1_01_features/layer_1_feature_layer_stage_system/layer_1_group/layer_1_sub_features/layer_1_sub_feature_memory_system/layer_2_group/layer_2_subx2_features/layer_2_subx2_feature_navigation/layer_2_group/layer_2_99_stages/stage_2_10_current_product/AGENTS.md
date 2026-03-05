<!-- derived_from: "7f234693-0224-4eb9-bcff-e08d4a26f2d5" -->
# AutoGen Agent Context

## Identity
Stage 10 (current_product) for the navigation research sub-feature.
- **Parent**: `../../0AGNOSTIC.md`
- **Purpose**: Current working product








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
