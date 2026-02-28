# AutoGen Agent Context


## Identity
Features registry for the better_ai_system research project.
- **Role**: Container for research features at Layer 0
- **Parent**: `../0AGNOSTIC.md` (layer_0_group)
- **Children**: layer_stage_system, multi_os_multi_machine_system, multimodal_system

## Triggers
Load this context when:
- Browsing or selecting research features
- Entering: `layer_0_features/`

## Pointers
### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../0AGNOSTIC.md` |
| Layer-Stage System | `layer_0_feature_layer_stage_system/` |
| Multi-OS System | `layer_0_feature_multi_os_multi_machine_system/` |
| Multimodal System | `layer_0_feature_multimodal_system/` |

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
