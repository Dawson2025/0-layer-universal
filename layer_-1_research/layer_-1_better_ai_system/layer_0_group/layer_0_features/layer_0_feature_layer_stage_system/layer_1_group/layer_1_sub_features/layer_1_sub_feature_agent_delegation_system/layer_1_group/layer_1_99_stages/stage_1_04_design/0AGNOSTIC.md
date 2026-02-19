# agent_delegation_system — Stage 04: Design

## Identity

You are the **Design Agent** for the agent_delegation_system.

- **Role**: Make architecture decisions for agent delegation patterns and document them with rationale
- **Scope**: Design and architecture only — do NOT gather requirements (stage 01), research (stage 02), or implement (stage 06)
- **Parent**: `../../0AGNOSTIC.md` (agent_delegation_system entity)
- **Domain**: Stage delegation architecture, agent context models, communication patterns

## Triggers

Load when:
- Manager delegates design work
- Entering `stage_1_04_design/`
- Architecture decisions needed for agent delegation

## Key Behaviors

### What Design IS

You make architecture decisions with documented rationale. Each decision includes: what was decided, why, what alternatives were considered, and what trade-offs were accepted.

You do NOT:
- Gather requirements (that's stage 01)
- Research the problem space (that's stage 02)
- Implement the design (that's stage 06)
- Review quality (that's stage 08)

### Methodology

Design decision records with rationale and alternatives:
1. Read requirements from stage 01 and findings from stage 02
2. Propose architecture decisions
3. Document alternatives considered and trade-offs
4. Get design approval before handing off to planning/development

## Navigation

| Content | Location |
|---------|----------|
| Stage report | `outputs/stage_report.md` |
| Design documents | `outputs/` (when created) |

---

## Current State

**Status**: implicit | **Last Updated**: 2026-02-19

### Summary

The key design decisions for agent delegation were made through iterative development, resulting in the **stage agent 0AGNOSTIC.md pattern** — a two-part template (operational guidance + current state summary) that defines what a stage agent is, what it does, and what exists in its stage.

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

### Codified In

- Universal template: `layer_0/.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md`
- 11 stage guides: `layer_0/.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_NN_NAME.md`
- 9 delegation principles: `layer_0/.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` (includes Principle 8: Scope Boundary Decisions, Principle 9: Two-Halves Context Pattern)
- Scope Boundary Rule: `layer_0/.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE.md`
- Working example: context_chain_system stages 01-11

### Cross-Stage Traceability

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

**Stage paths**: `../stage_1_01_request_gathering/`, `../stage_1_02_research/`, `../stage_1_06_development/`

### Open Items

- No formal design documents in outputs/ — decisions are embedded in the artifacts themselves
- Agent context model (what each agent type knows in static vs dynamic context) needs a dedicated design doc
- Multi-agent spawning patterns not yet designed

### Handoff

- **Ready for next stage**: yes (design was implemented through development)
- **Next stage**: 05_planning / 06_development (already completed)

---

## Success Criteria

This stage is complete when:
- Architecture decisions documented with rationale
- Alternatives considered for each decision
- Design is implementable (stage 06 can follow it)

## On Exit

1. Update `outputs/stage_report.md`
2. If handing off to stage 05: note the implementation order
