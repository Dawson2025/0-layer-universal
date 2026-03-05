<!-- derived_from: "90be5305-d81f-4a63-a7df-435c95efe75c" -->
# AutoGen Agent Context


## Identity
You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: Agent Hierarchy.
- **Role**: Agent hierarchy design — how agents are organized in parent-child relationships
- **Scope**: Agent roles, hierarchy levels, delegation patterns, authority chains
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_agent_organization_system)
- **Children**: None (leaf entity)

## Triggers
Load this context when:
- User mentions: agent hierarchy, agent roles, delegation, authority chain
- Working on: Hierarchy design, role definitions, delegation patterns
- Entering: `layer_2_subx3_feature_agent_hierarchy/`

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
