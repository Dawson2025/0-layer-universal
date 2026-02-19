# agent_delegation_system — Layer 1 Sub-Feature

## Identity

You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Agent Delegation System.

- **Role**: Agent delegation system — how AI agents delegate work across the layer-stage hierarchy, encompassing both what agents remember (memory) and how they coordinate (multi-agent)
- **Scope**: Stage delegation, agent context models, manager-agent communication, stage reports, context chains, agent hierarchies
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_layer_stage_system)
- **Children**: memory_system, multi_agent_system (in `layer_2_group/layer_2_subx2_features/`)

## Triggers

Load this context when:
- User mentions: agent delegation, stage delegation, manager delegation, agent context, stage reports
- Working on: How managers delegate to stage agents, what agents know, how agents coordinate
- Entering: `layer_1_sub_feature_agent_delegation_system/`

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
| Tree of knowledge | `.0agnostic/01_knowledge/tree_of_knowledge/00_agent_delegation_knowledge/` |
| Tree of needs | `layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/outputs/requests/tree_of_needs/` |
| Children | `layer_2_group/layer_2_subx2_features/` |

---

## Current State

**Phase**: active (stage 01 populated, universal artifacts produced, working example established) | **Last Updated**: 2026-02-19

### What's Been Done

This entity has progressed through multiple stages, producing universal artifacts that now live at `layer_0/.0agnostic/`:

| Stage Work | What Was Produced | Where It Lives |
|-----------|-------------------|----------------|
| **01 Request Gathering** | Tree of needs: 9 requirements across 3 branches (delegation_model, memory_integration, coordination_patterns) | `layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/outputs/requests/tree_of_needs/` |
| **02 Research** | Investigation of how stage agents should operate — explored context_chain_system as working example (stages 01-07 active, 76 PASS tests) | Context_chain_system entity: `layer_2_group/.../layer_3_subx3_feature_context_chain_system/` |
| **04 Design** | Designed the stage agent 0AGNOSTIC.md pattern: identity + methodology + scope boundaries + current state summary | Universal template: `layer_0/.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` |
| **05 Planning** | Planned stage-by-stage guide creation for all 11 stages | Plan executed across all 11 stages |
| **06 Development** | Created 11 universal stage guides, 3 static rules, 2 dynamic rules, 7 delegation principles, stage report protocol | See "Universal Artifacts" below |

### Universal Artifacts (at `layer_0/.0agnostic/`)

| Artifact | Count | Location |
|----------|-------|----------|
| Stage guides | 11 | `01_knowledge/layer_stage_system/stage_guides/STAGE_NN_NAME.md` |
| Stage agent template | 1 | `01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` |
| Delegation principles | 9 | `01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Static rules | 3 | `02_rules/static/` (scope boundary, report, delegation) |
| Dynamic rules | 2 | `02_rules/dynamic/` (loops, parallel) |
| Stage report protocol | 1 | `03_protocols/stage_report_protocol.md` |

### Working Example: context_chain_system

The context_chain_system (grandchild entity via memory_system) serves as the **primary working example** of agent delegation in practice:
- All 11 stage 0AGNOSTIC.md files populated with identity, methodology, scope, current state
- Stages 01-07 active with real outputs (requirements, research, design, plans, implementations, tests)
- 76 PASS tests validating the context chain implementation
- Entity-level `.0agnostic/` fully populated: 50+ files (knowledge, rules, protocols, skills)

**Path**: `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_memory_system/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_context_chain_system/`

### Key Discoveries (Formalized as Universal Principles)

| Discovery | Principle | Rule/Artifact |
|-----------|-----------|---------------|
| **Two-Halves Context Pattern**: Every 0AGNOSTIC.md needs operational guidance (static) + current state summary (updated) — together they make the pointer tier functional | Principle 9 | Universal template includes Current State section |
| **Scope Boundary Decisions**: When agents hit layer or stage boundaries, they decide: do it yourself (small/coupled), delegate (significant, agent exists), or instantiate (significant, no agent). Default: delegate. | Principle 8 | Scope Boundary Rule at `layer_0/.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE.md` |

Full details: `.0agnostic/01_knowledge/tree_of_knowledge/00_agent_delegation_knowledge/02_patterns_and_principles/`

### Tree of Knowledge

Entity knowledge is organized as a **tree of knowledge** (mirroring the tree of needs in stage 01). The tree lives in `.0agnostic/01_knowledge/tree_of_knowledge/` and contains **summaries + references** — the main bulk of detailed content stays in the stages.

| Branch | Topics | Question Answered |
|--------|--------|-------------------|
| `01_delegation_model/` | stage_delegation, stage_reports, agent_context_model | How do managers delegate to stage agents? |
| `02_patterns_and_principles/` | two_halves_pattern, scope_boundary_decisions, three_tier_knowledge | What patterns govern delegation? |
| `03_implementation/` | universal_artifacts, working_examples | What was built and where? |

---

## Success Criteria

This entity succeeds when:
- Stage delegation model is well-defined and tested across the hierarchy
- Agent context models are clear — each agent type knows what it knows
- Memory and multi-agent systems work together coherently
- Stage report protocol is standardized and in use

## On Exit

1. Update `0INDEX.md` with current state
2. If delegating to children, note which child and what work
