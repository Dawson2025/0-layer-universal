<!-- derived_from: "37550e84-0176-4b17-a017-b43f5c6f6a4d" -->
# AutoGen Agent Context

## Identity
Stage 09 (fixing) for the memory_system research sub-feature.
- **Parent**: `../../0AGNOSTIC.md`
- **Purpose**: Fix issues found in criticism








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
