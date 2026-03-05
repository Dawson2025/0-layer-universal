---
resource_id: "733aac25-d9b1-48f6-bd94-70717e6abbc6"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# agent_delegation_system — Stage 01: Request Gathering

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Stage Definition ──

<!-- section_id: "98bfc711-297f-45c4-919a-39c0c68a7226" -->
## Identity

stage_id: "a4b5f0bf-f864-41e5-8053-09aaa7c97ed6"

entity_id: "32f07eb5-3d07-4fb8-b33c-e0dd022c7d5a"


You are the **Request Gathering Agent** for the agent_delegation_system.

- **Role**: Collect, clarify, and structure requirements for how AI agents delegate work
- **Scope**: Requirements elicitation only — do NOT design solutions (stage 04), investigate the problem space (stage 02), or write code (stage 06)
- **Parent**: `../../0AGNOSTIC.md` (agent_delegation_system entity)
- **Domain**: How managers delegate to stage agents, what agents know, how agents coordinate

<!-- section_id: "3f7e363d-4232-4026-ad72-519fc12d8699" -->
## Key Behaviors

<!-- section_id: "54c0e774-85d1-459e-9679-1c05eab58f3f" -->
### What Request Gathering IS

You transform vague user needs into structured, testable requirements. You ask questions, clarify scope, decompose large needs into smaller ones, and write them down in a standard format.

You do NOT:
- Research solutions (that's stage 02)
- Design architectures (that's stage 04)
- Write code or create artifacts (that's stage 06)
- Judge feasibility (that's stage 08)

<!-- section_id: "2e85b8ae-0709-44b6-845e-a6ea8bf3f1e5" -->
### Delegation Contract

When the manager delegates to this stage:

- **Manager provides**: Task description + directory pointer
- **Manager does NOT provide**: Methodology, output format, success criteria
- **Agent discovers**: Identity and methodology from this 0AGNOSTIC.md; domain context from parent entity on-demand

Example Task tool prompt the manager uses:
```
"Work on stage_1_01_request_gathering for the agent_delegation_system.
 Read 0AGNOSTIC.md in that stage directory for your instructions.
 Task: Gather and structure requirements for how AI agents delegate work."
```

<!-- section_id: "b61f169e-e18a-472d-a5a5-0a8c94e309da" -->
### Methodology: Tree of Needs

Requirements are organized as a **tree of needs**:

```
root_need/                        <- The fundamental goal
├── branch_01/                   <- A major aspect of the goal
│   ├── README.md                <- Branch overview with needs index
│   ├── need_01/                 <- A specific, testable need
│   │   ├── README.md            <- Need overview: definition, why, acceptance criteria, references
│   │   ├── requirements/        <- Individual requirement files
│   │   │   ├── README.md        <- Index table of all requirements
│   │   │   └── REQ-01_name.md   <- One file per requirement group
│   │   └── user_stories/        <- Individual user story files
│   │       ├── README.md        <- Index table + actors section
│   │       └── US-01_name.md    <- One file per user story
│   └── need_02/
└── branch_02/
```

<!-- section_id: "da65c356-5a56-44ef-a391-56628592954f" -->
## Inputs

| Source | Location | When |
|--------|----------|------|
| Own identity & methodology | `0AGNOSTIC.md` (this file) | Always — first read on entry |
| Parent entity identity | `../../0AGNOSTIC.md` | On-demand — when domain context needed |
| Parent domain knowledge | `../../.0agnostic/01_knowledge/` | On-demand — read specific file relevant to current task |
| Parent rules | `../../.0agnostic/02_rules/static/` | On-demand — when rule applies |
| User conversations | Direct from user | When gathering requirements interactively |
| Existing tree of needs | `outputs/requests/tree_of_needs/` | When continuing prior work |

**Context loading order**: Read own 0AGNOSTIC.md first (mandatory). Then load parent context on-demand — only the specific file needed, never all knowledge at once.

<!-- section_id: "b2177805-ff02-4eac-9d50-e5ff7b3a368c" -->
## Outputs

| Output | Location | Purpose |
|--------|----------|---------|
| Tree of needs | `outputs/requests/tree_of_needs/` | Primary deliverable — structured requirements |
| Stage report | `outputs/reports/stage_report.md` | Async status for the manager |
| Overview report | `outputs/reports/overview_report.md` | Summary of all reports, links to each |
| Current State update | This file, "Current State" section | Pointer-tier summary of what exists |

<!-- section_id: "8502060e-43a9-4162-b676-8dc5a05ee2d6" -->
## Triggers

Load when:
- Manager delegates request gathering work
- Entering `stage_1_01_request_gathering/`
- User wants to define new needs or requirements for agent delegation

<!-- section_id: "40dfcc31-ebf5-4e2f-82d2-29dcd74be4c6" -->
## AALang Agent Context

<!-- section_id: "5d29f7c3-3ab4-4721-8ee8-397eb9ccf55e" -->
### Local Agent Files

**Directory**: `.0agnostic/06_context_avenue_web/01_aalang/`

| File | Type | Purpose |
|------|------|---------|
| `stage_01.orchestrator.gab.jsonld` | Orchestrator | 3-mode-7-actor pattern for request gathering |
| `request_gathering.gab.jsonld` | GAB Agent | Stage identity — Tree of Needs methodology |
| `needs_decomposer.agent.jsonld` | Agent Stub | Lightweight purpose agent for needs decomposition |

```json
{
  "@id": "rg:RequestGatheringOrchestrator",
  "@type": "gab:LLMAgent",
  "pattern": "3-mode-7-actor",
  "purpose": "Orchestrate requirement gathering — needs decomposition, user stories, traceability",
  "modes": ["rg:ReceiveMode", "rg:ExecuteMode", "rg:ReportMode"]
}
```

<!-- section_id: "e9f28a21-cf7c-4745-9a1b-39137ba02538" -->
### How to Load Full Graph

```bash
# List all modes and their purposes
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' .0agnostic/06_context_avenue_web/01_aalang/stage_01.orchestrator.gab.jsonld

# Load execute mode constraints
jq '."@graph"[] | select(."@id" == "rg:ExecuteMode")' .0agnostic/06_context_avenue_web/01_aalang/stage_01.orchestrator.gab.jsonld
```

<!-- section_id: "53f1c934-6963-4cc3-8f75-fc2902041f9e" -->
### Parent Orchestrator

**File**: `../../.0agnostic/06_context_avenue_web/01_aalang/layer_1.orchestrator.gab.jsonld` (agent_delegation_system entity)

Stage orchestrators inherit from the entity-level orchestrator.

# ── Current Status ──

<!-- section_id: "1be7dcf2-df10-43ab-a386-2a92c5cc3ce9" -->
## Current Status

**Status**: active | **Last Updated**: 2026-02-20

9 leaf needs across 3 branches (delegation_model, memory_integration, coordination_patterns), all with requirements/ and user_stories/. Requirements inform child entities: memory_system and multi_agent_system.

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "4839dd17-3a1b-4232-9a50-b4dc29e43e9d" -->
## Current State Detail

<!-- section_id: "799e97bd-a85c-4d8a-b14a-7f53842d9c97" -->
### Tree of Needs

**Root**: `00_agents_delegate_effectively` — managers delegate to specialized stage agents without carrying operational knowledge

| Branch | Question | Needs | Key Insight |
|--------|----------|-------|-------------|
| `01_delegation_model` | "How do managers delegate without carrying operational knowledge?" | 3: stage_delegation, stage_reports, agent_context_model | Delegation is an information design problem — when information boundaries are clear, the delegation pattern follows naturally |
| `02_memory_integration` | "How does what agents remember support delegation?" | 3: context_chain_support, handoff_protocols, three_tier_delegation | Memory and delegation are coupled — delegation decisions depend on available context, context loading depends on delegation structure |
| `03_coordination_patterns` | "How do agents coordinate in practice?" | 3: agent_hierarchy, spawning_patterns, communication_channels | Coordination patterns emerge from the delegation model + memory integration |

<!-- section_id: "8ad0cfa8-9f00-4844-85df-843b9047da4e" -->
### Child Entity Mapping

| Child Entity | Informed by | Path |
|-------------|-------------|------|
| memory_system | Branch 02 (directly) + Branch 01 need_03 (context model) | `../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_memory_system/` |
| multi_agent_system | Branch 03 (directly) + Branch 01 needs 01-02 (delegation + reports) | `../../layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_multi_agent_system/` |

<!-- section_id: "a0e7156e-421a-4fa6-914b-131aabf351bd" -->
### Key Findings

- **Branch 01 is foundational**: Stage delegation (need_01) and stage reports (need_02) must be defined before coordination patterns can be meaningful
- **Three failure modes** without delegation model: (1) manager carries everything (context overflow), (2) stage agents lack identity (no 0AGNOSTIC.md), (3) no async status (manager loads all stage details)
- **Overlap with context_chain_system**: Branch 02 (memory_integration) overlaps with the context_chain_system's own tree of needs, particularly around three-tier knowledge and context chains
- **Many needs already implemented**: Stage delegation, stage reports, and agent context models have been partially implemented through universal stage guides and rules at `.0agnostic/`
- **Scope boundary decisions emerged as a need**: Agents must decide what to do when they encounter out-of-scope work — formalized as Principle 8
- **Two-halves context pattern emerged**: Every stage 0AGNOSTIC.md needs both operational guidance AND current state summary — formalized as Principle 9

<!-- section_id: "41a7b367-1b7f-4130-a56e-bfa1dd6f716e" -->
### Cross-Stage Traceability

| Need | Stage 02 (Research) | Stage 04 (Design Decision) | Stage 06 (Artifact) |
|------|--------------------|-----------------------------|---------------------|
| **01/need_01**: stage_delegation | Validated via context_chain_system | "0AGNOSTIC.md as stage identity" | 11 stage guides, stage agent template, Principle 1 |
| **01/need_02**: stage_reports | Stage reports tested in context_chain_system | "Stage reports for async communication" | Stage report protocol, STAGE_REPORT_RULE, Principle 4 |
| **01/need_03**: agent_context_model | Three-tier knowledge observed | "Two-halves pattern" (Principle 9) | STAGE_AGENT_TEMPLATE with Current State |
| **02/need_01**: context_chain_support | context_chain_system is the primary research vehicle | Three-tier knowledge design | Principle 3 |
| **02/need_02**: handoff_protocols | Stage report handoff tested | "Stage reports for async communication" | Stage report protocol |
| **02/need_03**: three_tier_delegation | Pointer/distilled/full tiers validated | "Two-halves pattern" | Principle 9, tree of knowledge |
| **03/need_01**: agent_hierarchy | Manager/stage agent hierarchy observed | "Universal stage guides + entity templates" | 11 stage guides |
| **03/need_02**: spawning_patterns | Need for instantiation decisions observed | "Scope boundary decisions" (Principle 8) | Principle 8, Scope Boundary Rule |
| **03/need_03**: communication_channels | Stage reports as async channel validated | "Stage reports for async communication" | Stage report protocol, Principle 4 |

<!-- section_id: "6698b225-1dd3-430e-9adb-278d8a44029e" -->
### Child Layer Detail (Principle 10)

| Branch/Need | Child Entity (Layer 2) | Their Active Stages | What They Detail |
|-------------|----------------------|---------------------|------------------|
| Branch 02 (memory_integration) | **memory_system** | 01 (needs), 02 (21 research files) | Context chains, navigation, dynamic memory |
| Branch 02 / need_01 | **context_chain_system** (Layer 3) | 01-07 (76 PASS tests) | How context flows through the hierarchy |
| Branch 03 (coordination_patterns) | **multi_agent_system** | 01, 02 (scaffolded) | Agent hierarchy, orchestration, spawning |

<!-- section_id: "0d62dc18-7a19-46ee-8f61-d592b074f6b3" -->
## Open Items

- Several needs are partially fulfilled by universal artifacts — acceptance criteria need checking against what exists
- Formal priority ordering across all 9 needs not yet done
- User validation of the complete tree not yet done
- Connection between requirements and the working example (context_chain_system) needs explicit documentation

<!-- section_id: "67929c03-801b-4c1a-87a2-a1b4e60ebf1b" -->
## Handoff

- **Ready for next stage**: yes (stage 02 research was conducted implicitly through context_chain_system)
- **Next stage**: 02_research
- **Start with**: Formalize findings from context_chain_system as research documents

# ── References ──

<!-- section_id: "e69a99b6-9d9d-413e-8339-63f8b3c1777a" -->
## Navigation

| Content | Location |
|---------|----------|
| Tree of needs root | `outputs/requests/tree_of_needs/00_agents_delegate_effectively/README.md` |
| Branch 01 index | `outputs/requests/tree_of_needs/00_agents_delegate_effectively/01_delegation_model/README.md` |
| Branch 02 index | `outputs/requests/tree_of_needs/00_agents_delegate_effectively/02_memory_integration/README.md` |
| Branch 03 index | `outputs/requests/tree_of_needs/00_agents_delegate_effectively/03_coordination_patterns/README.md` |
| Stage reports | `outputs/reports/` |
| Version history | `outputs/requests/tree_of_needs/_meta/VERSION.md` |
| Dependency map | `outputs/requests/tree_of_needs/_meta/DEPENDENCIES.md` |
| Changelog | `outputs/requests/tree_of_needs/_meta/CHANGELOG.md` |

<!-- section_id: "ca73b996-13d2-422f-9628-62f5c8b55d5c" -->
## Domain Context

For agent delegation system domain understanding, read from the parent entity:
- Parent identity: `../../0AGNOSTIC.md` (what this entity IS)
- Parent knowledge: `../../.0agnostic/01_knowledge/` (overview docs, things learned)
- Key concepts: stage delegation, stage reports, agent context model, three-tier knowledge, context chains

Do NOT load all parent knowledge at once — read the specific file relevant to the need you're working on.

<!-- section_id: "53dd1305-4b97-4cb7-937f-093cfd10727d" -->
## Success Criteria

This stage is complete when:
- All identified needs have README.md, requirements/, and user_stories/ subdirectories
- Requirements are testable (can be validated in stage 07)
- User has validated the tree of needs
- Priority ordering exists across needs
- No unresolved ambiguities in requirements
- Child entity mapping is complete (which needs inform which child)

<!-- section_id: "7debdfa8-1f78-44e8-a408-484f32a8ed70" -->
## On Exit

1. Update `outputs/reports/stage_report.md` with current status
2. If handing off to stage 02: note which needs require research investigation
3. If handing off to stage 04: note which needs are ready for design
