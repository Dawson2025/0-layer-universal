# agent_delegation_system — Stage 04: Design

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Stage Definition ──

## Identity

You are the **Design Agent** for the agent_delegation_system.

- **Role**: Make architecture decisions for agent delegation patterns and document them with rationale
- **Scope**: Design and architecture only — do NOT gather requirements (stage 01), research (stage 02), or implement (stage 06)
- **Parent**: `../../0AGNOSTIC.md` (agent_delegation_system entity)
- **Domain**: Stage delegation architecture, agent context models, communication patterns

## Key Behaviors

### What Design IS

You make architecture decisions with documented rationale. Each decision includes: what was decided, why, what alternatives were considered, and what trade-offs were accepted.

You do NOT:
- Gather requirements (that's stage 01)
- Research the problem space (that's stage 02)
- Implement the design (that's stage 06)
- Review quality (that's stage 08)

### Delegation Contract

When the manager delegates to this stage:

- **Manager provides**: Task description + directory pointer
- **Manager does NOT provide**: Methodology, output format, success criteria
- **Agent discovers**: Identity and methodology from this 0AGNOSTIC.md; domain context from parent entity on-demand

Example Task tool prompt the manager uses:
```
"Work on stage_1_04_design for the agent_delegation_system.
 Read 0AGNOSTIC.md in that stage directory for your instructions.
 Task: Design the architecture and patterns for how AI agents delegate work."
```

### Methodology

Design decision records with rationale and alternatives:
1. Read requirements from stage 01 and findings from stage 02
2. Propose architecture decisions
3. Document alternatives considered and trade-offs
4. Get design approval before handing off to planning/development

## Inputs

What this agent reads:

| Source | Location | When |
|--------|----------|------|
| Own identity & methodology | `0AGNOSTIC.md` (this file) | Always — first read on entry |
| Parent entity identity | `../../0AGNOSTIC.md` | On-demand — when domain context needed |
| Parent domain knowledge | `../../.0agnostic/01_knowledge/` | On-demand — read specific file relevant to current task |
| Parent rules | `../../.0agnostic/02_rules/static/` | On-demand — when rule applies |
| Stage 01 requirements (tree of needs) | `../stage_1_01_request_gathering/outputs/requests/tree_of_needs/` | On entry — understand what to design for |
| Stage 01 stage report | `../stage_1_01_request_gathering/outputs/reports/stage_report.md` | On entry — understand requirements status |
| Stage 02 research findings | `../stage_1_02_research/outputs/by_topic/` | On entry — understand what was investigated |
| Stage 02 stage report | `../stage_1_02_research/outputs/reports/stage_report.md` | On entry — understand research status |
| Existing design outputs | `outputs/design_decisions/` | When continuing prior work |

**Context loading order**: Read own 0AGNOSTIC.md first (mandatory). Then load stage 01 requirements and stage 02 findings to understand what to design. Load parent context on-demand — only the specific file needed, never all knowledge at once.

## Outputs

What this agent produces:

| Output | Location | Purpose |
|--------|----------|---------|
| Design decisions | `outputs/design_decisions/` | Primary deliverable — architecture decisions with rationale |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` | Async status for the manager |
| Output report | `outputs/reports/output_report.md` | Summary of all outputs, links to each |
| Current State update | This file, "Current State" section | Pointer-tier summary of what exists |

### Stage Report

Before exiting, update `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` following the universal protocol at `.0agnostic/03_protocols/stage_report_protocol.md`. The entity manager reads this to understand your stage's status without loading stage details.

## Triggers

Load when:
- Manager delegates design work
- Entering `stage_1_04_design/`
- Architecture decisions needed for agent delegation

## AALang Agent Context

### Local Agent Files

**Directory**: `.0agnostic/06_context_avenue_web/01_aalang/`

| File | Type | Purpose |
|------|------|---------|
| `stage_04.orchestrator.gab.jsonld` | Orchestrator | 3-mode-7-actor pattern for architecture design |
| `design.gab.jsonld` | GAB Agent | Stage identity — requirements-driven design methodology |
| `architecture_designer.agent.jsonld` | Agent Stub | Lightweight purpose agent for architecture design |

```json
{
  "@id": "ds:DesignOrchestrator",
  "@type": "gab:LLMAgent",
  "pattern": "3-mode-7-actor",
  "purpose": "Orchestrate architecture design — decisions, alternatives, rationale documentation",
  "modes": ["ds:ReceiveMode", "ds:ExecuteMode", "ds:ReportMode"]
}
```

### How to Load Full Graph

```bash
# List all modes and their purposes
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' .0agnostic/06_context_avenue_web/01_aalang/stage_04.orchestrator.gab.jsonld

# Load execute mode constraints
jq '."@graph"[] | select(."@id" == "ds:ExecuteMode")' .0agnostic/06_context_avenue_web/01_aalang/stage_04.orchestrator.gab.jsonld
```

### Parent Orchestrator

**File**: `../../.0agnostic/06_context_avenue_web/01_aalang/layer_1.orchestrator.gab.jsonld` (agent_delegation_system entity)

Stage orchestrators inherit from the entity-level orchestrator.

# ── Current Status ──

## Current Status

**Status**: active | **Last Updated**: 2026-02-26

9 architecture decisions: 7 implicit (0AGNOSTIC.md pattern, two-halves, stage reports, scope boundaries, universal guides, scope decisions, scope spans layers+stages) + 2 formal — **context propagation design** (consolidation funnel + cross-level connection map) and **minimal context model** (agents get own STATIC + neighbor interfaces + on-demand access, not full ancestor cascade). Minimal context model validated by both tool cascading research (3/4 tools cascade natively, making lean content critical) and multi-agent framework research (CrewAI, LangGraph, AutoGen all converge on minimal + on-demand). Design outputs at `outputs/design_decisions/`.

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail

### Key Design Decisions

| Decision | Rationale | Alternative Rejected |
|----------|-----------|---------------------|
| **0AGNOSTIC.md as stage identity** | Loads as static context, tool-agnostic (works with Claude, Gemini, etc.), single source of truth | JSON-LD only (too rigid), README.md (no tooling support) |
| **Two-halves pattern** (operational + state) → Principle 9 | Agents need both "how to work" and "what's here" from a single file | Separate files for guidance vs state (more files to manage, less likely to stay in sync) |
| **Stage reports for async communication** | Managers shouldn't load stage outputs; reports provide summary | Real-time messaging only (doesn't survive sessions), shared state files (coordination complexity) |
| **Scope boundary enforcement via IS/IS NOT** | Explicit NOT list prevents scope creep better than just defining what IS | Implicit boundaries (agents guess what's out of scope) |
| **Universal stage guides + entity templates** | Universal guides define what ANY stage 01/02/etc. does; entity templates are instantiated per-entity | Per-entity everything (no reuse), purely universal (no customization) |
| **Scope boundary decisions** → Principle 8 | When agents reach scope boundaries, they decide: do it yourself (small/coupled), delegate (significant, agent exists), or instantiate (significant, no agent exists). Default: delegate. | No framework (agents guess), always delegate (misses trivial cases), always self-handle (context overflow) |
| **Scope boundaries span layers AND stages** | A single Scope Boundary Rule covers both dimensions — layer boundaries (sibling/parent/child entities) and stage boundaries (different stages within an entity) | Separate rules for layers vs stages (artificial split, same decision framework applies) |
| **Minimal context model** (2026-02-26) | Agents get own STATIC + compact neighbor interface summaries + on-demand DYNAMIC. No full ancestor cascade. Validated by tool cascading research (3/4 tools cascade natively — lean content prevents bloat) and multi-agent frameworks (CrewAI, LangGraph, AutoGen all use minimal + on-demand). Relay pattern for cross-hierarchy communication. | Full STATIC cascade (context waste at depth), full isolation (agents lack neighbor awareness), selective cascade (complex sync tooling) |

### Codified In

- Universal template: `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md`
- 11 stage guides: `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_NN_NAME.md`
- 9 delegation principles: `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` (includes Principle 8: Scope Boundary Decisions, Principle 9: Two-Halves Context Pattern)
- Scope Boundary Rule: `.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE.md`
- Working example: context_chain_system stages 01-11

## Cross-Stage Traceability

How each decision connects to requirements (stage 01), research (stage 02), and artifacts (stage 06):

| Decision | Stage 01 (Requirement) | Stage 02 (Finding) | Stage 06 (Artifact) |
|----------|----------------------|---------------------|---------------------|
| 0AGNOSTIC.md as stage identity | 01/need_01: stage_delegation | Validated via context_chain_system | 11 stage guides, stage agent template |
| Two-halves pattern (P9) | 01/need_03: agent_context_model, 02/need_03: three_tier_delegation | Discovered: agents need "what's here" + "how to work" | STAGE_AGENT_TEMPLATE with Current State, Principle 9 |
| Stage reports for async | 01/need_02: stage_reports, 02/need_02: handoff_protocols | Stage reports tested in working example | Stage report protocol, STAGE_REPORT_RULE, Principle 4 |
| Scope boundary IS/IS NOT | 01/need_01: stage_delegation | Agents without NOT lists drift into other stages | Every stage guide has IS/IS NOT sections |
| Universal guides + entity templates | 03/need_01: agent_hierarchy | 11 stages tested in context_chain_system | 11 STAGE_NN_NAME.md guides + template |
| Scope boundary decisions (P8) | 03/need_02: spawning_patterns | Agents need framework for out-of-scope work | Principle 8, Scope Boundary Rule |
| Scope spans layers AND stages | 03/need_01: agent_hierarchy | "Stage boundary" concept too narrow | Expanded Scope Boundary Rule |
| Minimal context model | 01/need_03: agent_context_model | Tool cascading + multi-agent frameworks both validate minimal + on-demand | `minimal_context_model.md`, STAGE_AGENT_TEMPLATE (already implements pattern) |

**Stage paths**: `../stage_1_01_request_gathering/`, `../stage_1_02_research/`, `../stage_1_06_development/`

## Child Layer Detail (Principle 10)

Design decisions are implemented differently at each child layer:

| Child Entity | Design Decisions Applied | Their Design Stage |
|-------------|------------------------|-------------------|
| **context_chain_system** (Layer 3) | All 7 decisions — full implementation as working example. Additionally has its own design decisions (avenue web, 8 avenues, progressive disclosure) | Stage 04: 2 design docs (chain system design, .0agnostic integration) |
| **memory_system** (Layer 2) | Three-tier knowledge, stage reports, two-halves pattern | Stage 04: scaffolded |
| **multi_agent_system** (Layer 2) | Scope boundary decisions, spawning patterns, agent hierarchy | Stage 04: scaffolded |

**Child paths**: see stage 01 Child Layer Detail for full paths

## Open Items

- Multi-agent spawning patterns not yet designed
- Cursor-specific context strategy (glob targeting vs self-contained rules) needs design doc

## Handoff

- **Ready for next stage**: yes (design was implemented through development)
- **Next stage**: 05_planning / 06_development (already completed)

# ── References ──

## Navigation

| Content | Location |
|---------|----------|
| Design decisions | `outputs/design_decisions/` |
| Output report | `outputs/reports/output_report.md` |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` |
| Stage 01 tree of needs | `../stage_1_01_request_gathering/outputs/requests/tree_of_needs/` |
| Stage 02 research | `../stage_1_02_research/outputs/by_topic/` |
| Universal template | `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` |
| Delegation principles | `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |

## Domain Context

For agent delegation system domain understanding, read from the parent entity:
- Parent identity: `../../0AGNOSTIC.md` (what this entity IS)
- Parent knowledge: `../../.0agnostic/01_knowledge/` (overview docs, things learned)
- Stage 01 requirements: `../stage_1_01_request_gathering/outputs/`
- Stage 02 findings: `../stage_1_02_research/outputs/`

Do NOT load all parent knowledge at once — read the specific file relevant to the decision you're making.

## Success Criteria

This stage is complete when:
- Architecture decisions documented with rationale
- Alternatives considered for each decision
- Design is implementable (stage 06 can follow it)

## On Exit

1. Update `outputs/reports/stage_report.md` with current status
2. If handing off to stage 05: note the implementation order
3. If handing off to stage 06: note which designs are ready for implementation
