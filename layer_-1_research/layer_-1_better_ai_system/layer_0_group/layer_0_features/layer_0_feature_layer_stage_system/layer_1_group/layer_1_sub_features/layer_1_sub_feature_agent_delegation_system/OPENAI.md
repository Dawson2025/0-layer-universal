# OpenAI Context

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
| On-demand resources | `.0agnostic/` (01_knowledge, 02_rules, 03_protocols, 04_episodic_memory, 05_handoff_documents, 06_context_avenue_web, 07+_setup_dependant) |
| Tree of knowledge | `.0agnostic/01_knowledge/tree_of_knowledge/00_agent_delegation_knowledge/` |
| Tree of needs | `layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/outputs/requests/tree_of_needs/` |
| Handoff documents | `.0agnostic/05_handoff_documents/` (stage overview, 01_incoming/{from_above,from_below}, 02_outgoing/{to_above,to_below}) |
| Context avenue web | `.0agnostic/06_context_avenue_web/` (aalang, integration MDs, @imports, skills, agents, rules, hooks) |
| Children | `layer_2_group/layer_2_subx2_features/` |




## Key Behaviors

### What This System Covers

The agent delegation system spans two domains:

1. **Memory** (what agents know): Context chains, navigation, dynamic memory, episodic memory — how context flows through the hierarchy and what each agent has access to
2. **Multi-Agent Coordination** (how agents work together): Agent hierarchies, orchestration, delegation patterns, stage reports, handoff protocols

These two domains are deeply coupled: delegation decisions depend on what context is available, and context loading depends on delegation structure.

### Domain Concepts

- **Stage delegation model**: Managers delegate to stage agents. Managers don't carry operational knowledge — each stage agent has its own 0AGNOSTIC.md with methodology, output format, and success criteria.
- **Stage reports**: Stage agents write `outputs/reports/stage_report.md` before exiting. Managers read these for async status without loading stage details.
- **Agent context model**: What each agent type (manager, stage agent, sub-feature agent) knows in its static and dynamic context.
- **Context chains**: How context traverses from root to leaf entities through the hierarchy.
- **Three-tier knowledge**: Pointers (0AGNOSTIC.md) -> Distilled (.0agnostic/knowledge/) -> Full (stage outputs).


## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
