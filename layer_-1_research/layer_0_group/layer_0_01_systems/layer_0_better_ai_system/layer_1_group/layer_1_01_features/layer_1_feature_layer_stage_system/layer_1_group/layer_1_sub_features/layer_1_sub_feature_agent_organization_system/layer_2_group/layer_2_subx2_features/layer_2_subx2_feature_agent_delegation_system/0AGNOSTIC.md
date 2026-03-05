---
resource_id: "88ec146f-1434-4978-a06a-7453d95cd148"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# agent_delegation_system — Layer 2 Sub-Feature

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "11ee2042-48f2-4aba-afd9-1c63e42119fb" -->
## Identity

entity_id: "b237d704-5b90-421c-85f4-c0ba15ada1ce"


You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: Agent Delegation System.

- **Role**: Agent delegation system — how AI agents delegate work across the layer-stage hierarchy, encompassing both what agents remember (memory) and how they coordinate (multi-agent)
- **Scope**: Stage delegation, agent context models, manager-agent communication, stage reports, context chains, agent hierarchies
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_agent_organization_system)
- **Children**: None (memory_system and multi_agent_system have been reorganized — memory_system promoted to L1 sibling, multi_agent_system absorbed into agent_organization_system)

<!-- section_id: "c231ba0b-5edf-4449-b7f8-0cdaed02c892" -->
## Key Behaviors

<!-- section_id: "4fca742d-07b5-4ee5-a71a-63b3e85dcf3b" -->
### What This System Covers

The agent delegation system spans two domains:

1. **Memory** (what agents know): Context chains, navigation, dynamic memory, episodic memory — how context flows through the hierarchy and what each agent has access to
2. **Multi-Agent Coordination** (how agents work together): Agent hierarchies, orchestration, delegation patterns, stage reports, handoff protocols

These two domains are deeply coupled: delegation decisions depend on what context is available, and context loading depends on delegation structure.

<!-- section_id: "309b4408-9447-4c24-8afc-61636ccd5626" -->
### Canonical Workspace for Delegation

This entity is the **canonical workspace** for all agent delegation patterns. When any agent (working anywhere in the system) encounters work related to delegation, they should:

1. Recognize it as out-of-scope (unless they're already in ADS)
2. Use scope boundary decisions (Principle 8) to traverse here
3. Work in the appropriate stage (research for investigation, design for architecture, development for implementation)
4. Propagate outputs to universal artifacts via the consolidation funnel

Delegation-related work includes: manager-agent contracts, scope boundaries, stage reports, agent context models, stage guides, delegation principles, any rules governing how agents work together.

**Update protocol**: `.0agnostic/03_protocols/agent_delegation_update_protocol.md`

<!-- section_id: "49650c14-6b0a-47a7-bbb1-bdeb2421c514" -->
### Domain Concepts

- **Stage delegation model**: Managers delegate to stage agents. Managers don't carry operational knowledge — each stage agent has its own 0AGNOSTIC.md with methodology, output format, and success criteria.
- **Stage reports**: Canonical stage report is `outputs/reports/stage_report.md`, mirrored to `.0agnostic/05_handoff_documents/02_outgoing/{01_to_above,03_to_below}/stage_report.md`.
- **Agent context model**: What each agent type (manager, stage agent, sub-feature agent) knows in its static and dynamic context.
- **Context chains**: How context traverses from root to leaf entities through the hierarchy.
- **Three-tier knowledge**: Pointers (0AGNOSTIC.md) -> Distilled (.0agnostic/knowledge/) -> Full (stage outputs).

<!-- section_id: "131fade0-cb19-4ac4-b82f-9e0f5727f880" -->
## Triggers

Load this context when:
- User mentions: agent delegation, stage delegation, manager delegation, agent context, stage reports
- Working on: How managers delegate to stage agents, what agents know, how agents coordinate
- Changing: delegation patterns, scope boundary decisions, agent communication protocols, stage methodology, stage guides
- Keywords: Principle 8, Scope Boundary Rule, manager-agent contracts, delegation principles, context chains, consolidation funnel, agent context model, stage report protocol
- Entering: `layer_2_subx2_feature_agent_delegation_system/`

<!-- section_id: "1fffab15-c09e-412e-b5ba-7cb8067693bb" -->
## AALang Agent Context

<!-- section_id: "116e5622-d86c-4539-a2a8-f9647d7d76dc" -->
### Local Agent Files

**Directory**: `.0agnostic/06_context_avenue_web/01_aalang/`

| File | Type | Purpose |
|------|------|---------|
| `layer_2.orchestrator.gab.jsonld` | Orchestrator | 5-mode-13-actor pattern for entity delegation management |
| `agent_delegation_system.gab.jsonld` | GAB Agent | Main entity identity — capabilities, constraints, context model |
| `stage_delegator.agent.jsonld` | Agent Stub | Lightweight purpose agent for delegation decisions |

```json
{
  "@id": "ads:AgentDelegationOrchestrator",
  "@type": "gab:LLMAgent",
  "pattern": "5-mode-13-actor",
  "purpose": "Orchestrate agent delegation system — manage stage agents, track delegation patterns",
  "modes": ["ads:ReceiveMode", "ads:ResearchMode", "ads:DesignMode", "ads:ImplementMode", "ads:ReviewMode"]
}
```

<!-- section_id: "56b307a8-c35a-48f6-86df-de3855002e81" -->
### How to Load Full Graph

```bash
# List all modes and their purposes
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' .0agnostic/06_context_avenue_web/01_aalang/layer_2.orchestrator.gab.jsonld

# Load a specific mode's constraints
jq '."@graph"[] | select(."@id" == "ads:ImplementMode")' .0agnostic/06_context_avenue_web/01_aalang/layer_2.orchestrator.gab.jsonld
```

<!-- section_id: "a256fc7e-1e1d-4f6a-baa2-7d1892e2ac7c" -->
### Parent Orchestrator

**File**: `../../../layer_1_orchestrator.gab.jsonld` (layer_1_sub_feature_agent_organization_system)

The entity-level orchestrator inherits from and is scoped by the parent sub-feature's orchestrator.

# ── Current Status ──

<!-- section_id: "de940a31-b595-4fa3-97e0-8c7e8e3b02d2" -->
## Current Status

**Phase**: active — 4 stages with content, universal artifacts in use, 4 formal research topics + 10 design decisions | **Last Updated**: 2026-02-26

Stages 01, 02, 04, and 06 have produced universal artifacts at root `.0agnostic/` (11 stage guides, 10 principles, 5 rules, stage report protocol, context propagation design). Stage 02 now has 4 formal research topics: tool context cascading (3/4 tools cascade natively), multi-agent context patterns (all converge on minimal + on-demand), scope boundary traversal (directional patterns), agent class/object patterns (OOP-to-agent mapping validates existing architecture via SOLID principles). Stage 04 has 10 architecture decisions including minimal context model (own STATIC + neighbor interfaces + on-demand, no full cascade) and directional scope boundaries (3-step: direction → handling → communication). Entity consolidation reports updated. Memory_system child has 24 research docs. Working example: context_chain_system (76 PASS tests).

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "c205940e-acb5-4367-8250-6a67d34c6ac0" -->
## Current State Detail

<!-- section_id: "58335855-83ed-474c-b34e-58a9c78b97c3" -->
### Stage Work Summary

| Stage Work | What Was Produced | Where It Lives |
|-----------|-------------------|----------------|
| **01 Request Gathering** | Tree of needs: 9 requirements across 3 branches (delegation_model, memory_integration, coordination_patterns) | `layer_2_group/layer_2_99_stages/stage_2_01_request_gathering/outputs/requests/tree_of_needs/` |
| **02 Research** | 4 formal topics (tool cascading, multi-agent patterns, scope traversal, agent class/object patterns) + implicit via context_chain_system living laboratory | `layer_2_group/layer_2_99_stages/stage_2_02_research/outputs/by_topic/` |
| **04 Design** | 10 architecture decisions: 0AGNOSTIC.md pattern, two-halves, stage reports, scope boundaries, universal guides, context propagation, minimal context model, directional scope boundaries | `layer_2_group/layer_2_99_stages/stage_2_04_design/outputs/design_decisions/` |
| **05 Planning** | Planned stage-by-stage guide creation for all 11 stages | Plan executed across all 11 stages |
| **06 Development** | Created 11 universal stage guides, 3 static rules, 2 dynamic rules, 7 delegation principles, stage report protocol | See "Universal Artifacts" below |

<!-- section_id: "d40cc9b9-65be-40e3-b30f-bc1d7b617437" -->
### Universal Artifacts (at `.0agnostic/`)

| Artifact | Count | Location |
|----------|-------|----------|
| Stage guides | 11 | `01_knowledge/layer_stage_system/stage_guides/STAGE_NN_NAME.md` |
| Stage agent template | 1 | `01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` |
| Delegation principles | 10 | `01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Static rules | 3 | `02_rules/static/` (scope boundary, report, delegation) |
| Dynamic rules | 2 | `02_rules/dynamic/` (loops, parallel) |
| Stage report protocol | 1 | `03_protocols/stage_report_protocol.md` |

<!-- section_id: "69123ab5-6351-478e-9d49-949a58884c91" -->
### Working Example: context_chain_system

The context_chain_system (now under memory_system, a sibling sub-feature) serves as the **primary working example** of agent delegation in practice:
- All 11 stage 0AGNOSTIC.md files populated with identity, methodology, scope, current state
- Stages 01-07 active with real outputs (requirements, research, design, plans, implementations, tests)
- 76 PASS tests validating the context chain implementation
- Entity-level `.0agnostic/` fully populated: 50+ files (knowledge, rules, protocols, skills)

**Path**: `../../../layer_1_sub_feature_memory_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_context_chain_system/` (sibling tree under layer_stage_system)

<!-- section_id: "164dee1d-a331-46fb-bfb7-055dce9ef216" -->
### Key Discoveries (Formalized as Universal Principles)

| Discovery | Principle | Rule/Artifact |
|-----------|-----------|---------------|
| **Two-Halves Context Pattern**: Every 0AGNOSTIC.md needs operational guidance (static) + current state summary (updated) — together they make the pointer tier functional | Principle 9 | Universal template includes Current State section |
| **Scope Boundary Decisions**: 3-step directional process — identify direction (up/down/left/right/sideways/multi-location), decide handling (do yourself/delegate/instantiate), communicate per direction. Multi-location escalates to nearest common ancestor. Default: delegate. | Principle 8 | Scope Boundary Rule at `.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE.md` |
| **Minimal Context Model**: Agents get own STATIC + compact neighbor interfaces + on-demand DYNAMIC. No full ancestor cascade. Validated by tool cascading (3/4 cascade natively) and multi-agent frameworks (CrewAI, LangGraph, AutoGen all use minimal + on-demand). | — | Design decision at `stage_1_04_design/outputs/design_decisions/minimal_context_model.md` |
| **Cross-Layer Stage References**: When content at one layer warrants a child entity, both layers maintain bidirectional stage references — parent points down (overview → detail), child points up (detail → context) | Principle 10 | Applied to all stages and child entities in this hierarchy |

Full details: `.0agnostic/01_knowledge/tree_of_knowledge/00_agent_delegation_knowledge/02_patterns_and_principles/`

<!-- section_id: "c1ded060-6dce-4b34-bc90-cfb501eba9c8" -->
### Tree of Knowledge

Entity knowledge is organized as a **tree of knowledge** (mirroring the tree of needs in stage 01). The tree lives in `.0agnostic/01_knowledge/tree_of_knowledge/` and contains **summaries + references** — the main bulk of detailed content stays in the stages.

| Branch | Topics | Question Answered |
|--------|--------|-------------------|
| `01_delegation_model/` | stage_delegation, stage_reports, agent_context_model | How do managers delegate to stage agents? |
| `02_patterns_and_principles/` | two_halves_pattern, scope_boundary_decisions, three_tier_knowledge | What patterns govern delegation? |
| `03_implementation/` | universal_artifacts, working_examples | What was built and where? |

# ── References ──

<!-- section_id: "1a12f342-db4c-4b91-9023-29e8a27b3ab8" -->
## Navigation

<!-- section_id: "61571eea-c2e1-40d2-ad74-c37310e5233f" -->
### Children

No active children. Former children have been reorganized:
- **memory_system** → promoted to L1 sibling under layer_stage_system
- **multi_agent_system** → absorbed into agent_organization_system (agent_hierarchy + orchestration extracted)

<!-- section_id: "ac7b5dab-f327-4c1e-9acc-82f0f2dfc00f" -->
### Key Locations

| Content | Location |
|---------|----------|
| Entity source of truth | `0AGNOSTIC.md` (this file) |
| Dashboard | `0INDEX.md` |
| Stages | `layer_2_group/layer_2_99_stages/` |
| On-demand resources | `.0agnostic/` (01_knowledge, 02_rules, 03_protocols, 04_episodic_memory, 05_handoff_documents, 06_context_avenue_web, 07+_setup_dependant) |
| Tree of knowledge | `.0agnostic/01_knowledge/tree_of_knowledge/00_agent_delegation_knowledge/` |
| Tree of needs | `layer_2_group/layer_2_99_stages/stage_2_01_request_gathering/outputs/requests/tree_of_needs/` |
| Things learned | `.0agnostic/01_knowledge/things_learned/docs/` |
| Handoff documents | `.0agnostic/05_handoff_documents/` (01_incoming/{from_above,from_below}, 02_outgoing/{to_above,to_below}) |
| Layer report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/layer_report.md` |
| Stages report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stages_report.md` |
| Child layers report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/child_layers_report.md` |
| Report + Porting contract | `.0agnostic/01_knowledge/overview/docs/report_and_porting_contract.md` |
| Context avenue web | `.0agnostic/06_context_avenue_web/` (aalang, integration MDs, auto-memory, @imports, skills, agents, rules, hooks) |
| Children | `layer_3_group/layer_3_subx3_features/` |

<!-- section_id: "a9d9fde3-3887-4b98-bbe1-3d99aeb03663" -->
## Success Criteria

This entity succeeds when:
- Stage delegation model is well-defined and tested across the hierarchy
- Agent context models are clear — each agent type knows what it knows
- Memory and multi-agent systems work together coherently
- Stage report protocol is standardized and in use

<!-- section_id: "8b14d76b-b598-4947-99f8-c6b88ed20ec2" -->
## On Exit

1. Update `0INDEX.md` with current state
2. If delegating to children, note which child and what work
