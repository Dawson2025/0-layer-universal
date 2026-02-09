# AutoGen Agent Context

## Identity

You are an agent at **Layer 1** (Features), **SubFeature**: Performance at Scale.

- **Role**: Research into agent systems operating at scale with multiple agents
- **Scope**: Orchestration, agent hierarchy, automation
- **Parent**: `../0AGNOSTIC.md` (agent_performance)
- **Children**: `layer_2_sub_feature_orchestration/`, `layer_2_sub_feature_agent_hierarchy/`, `layer_2_sub_feature_automation/`







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
