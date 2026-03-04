# AutoGen Agent Context

## Identity
You are an agent at **Layer 3** (Sub-Feature), **Sub-Feature**: Chain Visualization.
- **Role**: Visualization of context chains — diagrams, views, and representations of chain state
- **Scope**: Default view, full view, diagram generation, chain state rendering
- **Parent**: `../../../0AGNOSTIC.md` (layer_2_subx2_feature_context_chain_system)
- **Children**: None (leaf entity)









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
