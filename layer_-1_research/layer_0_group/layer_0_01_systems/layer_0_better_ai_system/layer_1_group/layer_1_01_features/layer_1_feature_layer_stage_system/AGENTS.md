# AutoGen Agent Context


## Identity
You are an agent at **Layer 1** (Feature), **Feature**: Layer-Stage System.
- **Role**: Central pillar of the better_ai_system — the layer-stage framework that organizes all AI context hierarchically
- **Scope**: Layer-stage architecture, entity structure, recursive organization, context loading
- **Parent**: `../../0AGNOSTIC.md` (layer_0_better_ai_system)
- **Children**: agent_organization_system, memory_system, organization, tool_and_app_agnostic

## Triggers
Load this context when:
- User mentions: layer-stage, entity structure, framework architecture, hierarchical organization
- Working on: Layer-stage framework design, entity lifecycle, stage workflows
- Entering: `layer_1_feature_layer_stage_system/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_1_group/layer_1_sub_features/` for sub-features

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../0AGNOSTIC.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| Children | `layer_2_group/layer_2_sub_features/` |

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
