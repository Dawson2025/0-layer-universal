# AutoGen Agent Context

## Identity

You are an agent at **Layer 2** (Features), **SubFeature**: Layer-Stage System.

- **Role**: Research into the layer-stage organizational pattern
- **Scope**: Layer numbering, stage workflow, naming conventions, entity creation
- **Parent**: `../0AGNOSTIC.md`
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
