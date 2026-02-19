# AutoGen Agent Context

## Identity

You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Agent Delegation System.

- **Role**: Agent delegation system — how AI agents delegate work across the layer-stage hierarchy, encompassing both what agents remember (memory) and how they coordinate (multi-agent)
- **Scope**: Stage delegation, agent context models, manager-agent communication, stage reports, context chains, agent hierarchies
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_layer_stage_system)
- **Children**: memory_system, multi_agent_system (in `layer_2_group/layer_2_subx2_features/`)


## Navigation

### Children

| Child | Purpose | Location |
|-------|---------|----------|
| memory_system | Context chains, navigation, dynamic memory | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_memory_system/` |
| multi_agent_system | Agent hierarchies, orchestration, delegation patterns | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_multi_agent_system/` |

### Key Locations

| Content | Location |
|---------|----------|
| Entity source of truth | `0AGNOSTIC.md` (this file) |
| Dashboard | `0INDEX.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| On-demand resources | `.0agnostic/` (01_knowledge, 02_rules, 03_protocols, etc.) |
| Children | `layer_2_group/layer_2_subx2_features/` |

---




## Key Behaviors

### What This System Covers

The agent delegation system spans two domains:

1. **Memory** (what agents know): Context chains, navigation, dynamic memory, episodic memory — how context flows through the hierarchy and what each agent has access to
2. **Multi-Agent Coordination** (how agents work together): Agent hierarchies, orchestration, delegation patterns, stage reports, handoff protocols

These two domains are deeply coupled: delegation decisions depend on what context is available, and context loading depends on delegation structure.

### Domain Concepts

- **Stage delegation model**: Managers delegate to stage agents. Managers don't carry operational knowledge — each stage agent has its own 0AGNOSTIC.md with methodology, output format, and success criteria.
- **Stage reports**: Stage agents write `outputs/stage_report.md` before exiting. Managers read these for async status without loading stage details.
- **Agent context model**: What each agent type (manager, stage agent, sub-feature agent) knows in its static and dynamic context.
- **Context chains**: How context traverses from root to leaf entities through the hierarchy.
- **Three-tier knowledge**: Pointers (0AGNOSTIC.md) -> Distilled (.0agnostic/knowledge/) -> Full (stage outputs).



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
