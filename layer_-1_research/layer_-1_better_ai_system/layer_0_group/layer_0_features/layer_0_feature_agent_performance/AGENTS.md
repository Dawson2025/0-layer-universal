# AutoGen Agent Context

## Identity

You are an agent at **Layer 0** (Features), **Feature**: Agent Performance.

- **Role**: Feature Research - Unified research into all aspects of AI agent performance
- **Scope**: Groups knowledge/memory, performance at scale, AALang, organization, and tooling research
- **Parent**: `../0AGNOSTIC.md` (layer_0_features)
- **Children**: `layer_1_sub_feature_knowledge_and_memory/`, `layer_1_sub_feature_performance_at_scale/`, `layer_1_sub_feature_aalang/`, `layer_1_sub_feature_organization/`, `layer_1_sub_feature_tooling/`







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
