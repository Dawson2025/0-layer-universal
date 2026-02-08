# AutoGen Agent Context

## Identity
You are an AI agent working within the layer_1 (projects) context. This layer contains project-specific content, features, and components.


## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Universal rules**: Inherit from `../layer_0/.0agnostic/rules/`
- **Project features**: `layer_1_features/`
- **Project components**: `layer_1_components/`


## Key Behaviors

### Agent Context Loading
Each directory may have a `.gab.jsonld` agent definition with a matching `.integration.md` summary (same base name):
- e.g., `layer_N_orchestrator.gab.jsonld` → `layer_N_orchestrator.integration.md`
- Read the `.integration.md` for a quick summary; query the `.gab.jsonld` via jq for precise mode constraints
- `.integration.md` files are auto-generated — do not edit directly

### Context Discovery
Before starting any task:
1. Read this file (0AGNOSTIC.md)
2. Check `../layer_0/` for universal rules
3. Check `.0agnostic/` for project-specific resources
4. Find the `.gab.jsonld` for your role and read its matching `.integration.md`
5. Read episodic memory if resuming work

### Episodic Memory
Record your work in `outputs/episodic/`:
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
