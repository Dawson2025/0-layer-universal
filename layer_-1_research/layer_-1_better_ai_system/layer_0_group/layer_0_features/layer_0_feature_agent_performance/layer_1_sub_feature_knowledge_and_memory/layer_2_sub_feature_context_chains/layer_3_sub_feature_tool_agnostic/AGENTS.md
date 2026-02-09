# AutoGen Agent Context

## Identity

You are an agent at **Layer 3** (Features), **SubFeature**: Tool Agnostic System.

- **Role**: Research and development of the tool-agnostic context distribution system
- **Scope**: 0AGNOSTIC.md, .0agnostic/, .1merge/, agnostic-sync.sh — the infrastructure that keeps context tool-independent
- **Parent**: `../0AGNOSTIC.md` (context_chains)
- **Children**: None (leaf node — has full stage structure in `layer_0/layer_0_99_stages/`)







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
