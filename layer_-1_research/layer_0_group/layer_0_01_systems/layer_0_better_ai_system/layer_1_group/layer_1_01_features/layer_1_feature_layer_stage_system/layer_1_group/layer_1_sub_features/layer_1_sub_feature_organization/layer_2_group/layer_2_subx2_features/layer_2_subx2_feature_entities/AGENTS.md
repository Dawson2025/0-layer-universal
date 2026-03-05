<!-- derived_from: "3e5c2b6e-f22c-417e-bd2a-a109acf251c2" -->
# AutoGen Agent Context


## Identity
You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: Entities.
- **Role**: Entity management — how entities (features, sub-features, projects) are created, structured, and maintained
- **Scope**: Entity lifecycle, canonical structure, instantiation, registry management
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_organization)
- **Children**: None (leaf entity)

## Triggers
Load this context when:
- User mentions: entities, entity creation, entity lifecycle, canonical structure
- Working on: Entity management, structure templates, lifecycle workflows
- Entering: `layer_2_subx2_feature_entities/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_2_group/layer_2_99_stages/` for stage progress

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_2_group/layer_2_99_stages/` |

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
