# AutoGen Agent Context

## Identity
You are an AI agent working within the layer_0 (universal) context. This layer contains rules, prompts, and knowledge that apply across ALL projects.


## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Rules**: `.0agnostic/rules/`
- **Prompts**: `.0agnostic/prompts/`
- **Knowledge**: `.0agnostic/knowledge/`
- **Agents**: `.0agnostic/agents/`


## Key Behaviors



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
