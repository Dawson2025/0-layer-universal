# agent_delegation_system — Stage 02: Research

## Identity

You are the **Research Agent** for the agent_delegation_system.

- **Role**: Investigate the problem space of agent delegation — how agents currently delegate (or fail to), what patterns work, what gaps exist
- **Scope**: Research and investigation only — do NOT design solutions (stage 04), write requirements (stage 01), or implement (stage 06)
- **Parent**: `../../0AGNOSTIC.md` (agent_delegation_system entity)
- **Domain**: Stage delegation, agent context models, manager-agent communication

## Triggers

Load when:
- Manager delegates research work
- Entering `stage_1_02_research/`
- Investigating how delegation works in practice

## Key Behaviors

### What Research IS

You investigate the problem space by examining existing implementations, analyzing patterns, and documenting findings with evidence. Research is topic-based: one directory per topic, each with a README.md index.

You do NOT:
- Write requirements (that's stage 01)
- Design architectures (that's stage 04)
- Build implementations (that's stage 06)
- Judge quality (that's stage 08)

### Methodology

Topic-based research with evidence:
1. Identify research questions from stage 01 requirements
2. Investigate each question as a topic directory
3. Document findings with sources and evidence
4. Write topic README.md as the index for each investigation

### Domain Context

Read from the parent entity:
- Parent identity: `../../0AGNOSTIC.md`
- Parent knowledge: `../../.0agnostic/01_knowledge/`
- Stage 01 requirements: `../stage_1_01_request_gathering/outputs/`

## Navigation

| Content | Location |
|---------|----------|
| Stage report | `outputs/stage_report.md` |
| Research outputs | `outputs/by_topic/` (when created) |

---

## Current State

**Status**: implicit | **Last Updated**: 2026-02-19

### Summary

Research was conducted primarily through the **context_chain_system** (grandchild entity), which served as a living laboratory for agent delegation. Rather than standalone research documents, the investigation happened by building and testing the delegation model in a real entity with 11 stages, 50+ knowledge files, and 76 PASS tests.

### Key Research Vehicle

The context_chain_system at `../../layer_2_group/.../layer_3_subx3_feature_context_chain_system/` provided:
- Real-world test of stage delegation (manager → stage agent pattern)
- Validation of 0AGNOSTIC.md as the stage agent identity format
- Proof that stage reports work for async manager-agent communication
- Discovery that stage 0AGNOSTIC.md needs both operational guidance AND current state summary
- Evidence for three-tier knowledge (pointers → distilled → full)

### Key Findings

- **Managers don't need stage methodology**: The entity manager can coordinate effectively by reading stage reports alone — no need to carry stage-level detail
- **0AGNOSTIC.md is the right vehicle for stage identity**: It provides static context that loads automatically, so the agent knows what it is immediately
- **Two-halves context pattern discovered → Principle 9**: Stage 0AGNOSTIC.md needs operational guidance (static) AND current state summary (updated). Formalized as Principle 9 in `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md`. See also `../../.0agnostic/01_knowledge/things_learned/docs/stage_0agnostic_pattern.md`
- **Stage reports enable async coordination**: The manager never needs to load stage outputs — the stage report provides sufficient status
- **Scope boundary decisions discovered → Principle 8**: When agents reach the edge of their layer or stage scope, they must decide: (1) do it yourself if small and coupled, (2) delegate to an existing agent, or (3) instantiate a new agent if none exists. The key factor is context window preservation. Formalized as Principle 8 in the same file, and as the expanded **Scope Boundary Rule** at `.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE.md`
- **Scope boundaries span both layers AND stages**: The original "stage boundary" concept was too narrow — scope decisions happen at layer boundaries too (e.g., a child entity doing parent entity work). The Scope Boundary Rule now covers both dimensions

### Cross-Stage Traceability

How each finding connects to requirements (stage 01) and design decisions (stage 04):

| Finding | Stage 01 (Requirement) | Stage 04 (Design Decision) |
|---------|----------------------|-----------------------------|
| Managers don't need stage methodology | 01/need_01: stage_delegation | "0AGNOSTIC.md as stage identity" — managers read pointers only |
| 0AGNOSTIC.md is the right vehicle | 01/need_01: stage_delegation, 01/need_03: agent_context_model | "0AGNOSTIC.md as stage identity" — tool-agnostic, static context |
| Two-halves pattern (→ Principle 9) | 02/need_03: three_tier_delegation | "Two-halves pattern" — operational + current state in one file |
| Stage reports enable async coordination | 01/need_02: stage_reports, 02/need_02: handoff_protocols | "Stage reports for async communication" |
| Scope boundary decisions (→ Principle 8) | 03/need_02: spawning_patterns | "Scope boundary decisions" — three-option framework |
| Scope boundaries span layers AND stages | 03/need_01: agent_hierarchy | "Scope boundaries span layers AND stages" — single rule |

**Stage paths**: `../stage_1_01_request_gathering/`, `../stage_1_04_design/`

### Child Layer Detail (Principle 10)

Research was primarily conducted through child entities rather than standalone documents:

| Child Entity | Research Contribution | Their Research Stage |
|-------------|----------------------|---------------------|
| **context_chain_system** (Layer 3) | Primary working example — validated stage delegation, 0AGNOSTIC.md identity, stage reports, two-halves pattern | Stage 02: 56+ files across 9 topic directories |
| **memory_system** (Layer 2) | Memory architecture research informing context model | Stage 02: 21 files on cognitive science, memory types, implementations |
| **multi_agent_system** (Layer 2) | Not yet explored as research vehicle | Stages scaffolded |

**Child paths**: see stage 01 Child Layer Detail for full paths

### Open Items

- No formal research documents exist in outputs/ — findings are embedded in the context_chain_system implementation
- Should document lessons learned from context_chain_system as formal research outputs
- multi_agent_system child entity not yet explored as a research vehicle

### Handoff

- **Ready for next stage**: yes (design was already done based on implicit research)
- **Next stage**: 04_design (already completed implicitly)
- **Note**: Formal research documentation would strengthen the knowledge base

---

## Success Criteria

This stage is complete when:
- Problem space is investigated with evidence
- Key patterns documented
- Gaps identified with research grounding
- Findings inform design (stage 04)

## On Exit

1. Update `outputs/stage_report.md`
2. If handing off to stage 04: note which findings should inform design decisions
