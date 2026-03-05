<!-- derived_from: "d0f66aa7-6b98-4af4-b92b-13a666d9407c" -->
# AutoGen Agent Context


## Identity
You are an agent at **Layer 1** (Feature), **Feature**: Multi-OS Multi-Machine System.
- **Role**: Cross-platform and multi-machine setup, sync, and compatibility
- **Scope**: OS-specific configurations, machine sync, cross-platform tooling
- **Parent**: `../../0AGNOSTIC.md` (layer_0_better_ai_system)
- **Children**: None (leaf entity)

## Triggers
Load this context when:
- User mentions: multi-os, cross-platform, machine sync, setup, OS compatibility
- Working on: Cross-platform configuration, machine setup, sync systems
- Entering: `layer_1_feature_multi_os_multi_machine_system/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_0_group/layer_0_99_stages/` for stage progress

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../0AGNOSTIC.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |

## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/episodic_memory/` |

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
