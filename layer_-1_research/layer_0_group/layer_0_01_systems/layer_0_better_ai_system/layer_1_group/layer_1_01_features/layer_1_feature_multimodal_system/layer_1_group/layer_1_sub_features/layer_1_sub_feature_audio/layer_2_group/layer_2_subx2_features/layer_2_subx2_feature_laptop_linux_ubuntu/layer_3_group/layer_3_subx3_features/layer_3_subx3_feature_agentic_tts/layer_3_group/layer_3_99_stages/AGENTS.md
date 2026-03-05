<!-- derived_from: "67aa0921-77ff-459d-8254-c22481f57040" -->
# AutoGen Agent Context

## Identity
Stages container for the agentic TTS sub-feature.
- **Parent**: `../../0AGNOSTIC.md` (layer_3_subx3_feature_agentic_tts)

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
