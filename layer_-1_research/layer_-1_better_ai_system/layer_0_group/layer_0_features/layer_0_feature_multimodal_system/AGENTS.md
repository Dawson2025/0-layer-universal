# AutoGen Agent Context

## Identity
You are an agent at **Layer 0** (Feature), **Feature**: Multimodal System.
- **Role**: Future multimodal capabilities — voice, vision, and other modalities
- **Scope**: Multimodal input/output, modality-specific workflows, future capabilities
- **Parent**: `../0AGNOSTIC.md` (layer_0_features)
- **Children**: None (leaf entity)







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
