<!-- derived_from: "aa24709f-a54e-43db-ac3b-f2b61b2bbaac" -->
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

### Context Discovery
Before starting any task, traverse the context hierarchy:
1. Read this file (0AGNOSTIC.md)
2. Check `.0agnostic/` for detailed resources if needed
3. Follow layer-stage framework conventions

### Episodic Memory
Record your work in `.0agnostic/episodic_memory/`:
- Create session files for significant work
- Update divergence.log when changing outputs
- Enable next session to continue seamlessly

### Multi-Agent Safety
When modifying shared outputs:
- Check for locks before writing
- Use atomic writes (temp file → rename)
- Log changes to divergence.log



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
