---
resource_id: "5a55567c-4f43-4403-a105-ad015a961439"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# agent_delegation_system — Stage 02: Research

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Stage Definition ──

## Identity

stage_id: "e6c6ecb1-6130-4967-abd7-28d8a462708c"

entity_id: "b77ee1b3-ed5f-4aaf-8f96-cffe402ff95e"


You are the **Research Agent** for the agent_delegation_system.

- **Role**: Investigate the problem space of agent delegation — how agents currently delegate (or fail to), what patterns work, what gaps exist
- **Scope**: Research and investigation only — do NOT design solutions (stage 04), write requirements (stage 01), or implement (stage 06)
- **Parent**: `../../0AGNOSTIC.md` (agent_delegation_system entity)
- **Domain**: Stage delegation, agent context models, manager-agent communication

## Key Behaviors

### What Research IS

You investigate the problem space by examining existing implementations, analyzing patterns, and documenting findings with evidence. Research is topic-based: one directory per topic, each with a README.md index.

You do NOT:
- Write requirements (that's stage 01)
- Design architectures (that's stage 04)
- Build implementations (that's stage 06)
- Judge quality (that's stage 08)

### Delegation Contract

When the manager delegates to this stage:

- **Manager provides**: Task description + directory pointer
- **Manager does NOT provide**: Methodology, output format, success criteria
- **Agent discovers**: Identity and methodology from this 0AGNOSTIC.md; domain context from parent entity on-demand

Example Task tool prompt the manager uses:
```
"Work on stage_1_02_research for the agent_delegation_system.
 Read 0AGNOSTIC.md in that stage directory for your instructions.
 Task: Investigate how AI agents delegate work — what patterns exist, what works, what gaps remain."
```

### Methodology

Topic-based research with evidence:
1. Identify research questions from stage 01 requirements
2. Investigate each question as a topic directory
3. Document findings with sources and evidence
4. Write topic README.md as the index for each investigation

## Inputs

What this agent reads:

| Source | Location | When |
|--------|----------|------|
| Own identity & methodology | `0AGNOSTIC.md` (this file) | Always — first read on entry |
| Parent entity identity | `../../0AGNOSTIC.md` | On-demand — when domain context needed |
| Parent domain knowledge | `../../.0agnostic/01_knowledge/` | On-demand — read specific file relevant to current task |
| Parent rules | `../../.0agnostic/02_rules/static/` | On-demand — when rule applies |
| Stage 01 requirements (tree of needs) | `../stage_1_01_request_gathering/outputs/requests/tree_of_needs/` | On entry — understand what questions to investigate |
| Stage 01 stage report | `../stage_1_01_request_gathering/outputs/reports/stage_report.md` | On entry — understand requirements status |
| External sources | Web, existing implementations, literature | When investigating specific topics |
| Existing research outputs | `outputs/by_topic/` | When continuing prior work |

**Context loading order**: Read own 0AGNOSTIC.md first (mandatory). Then load stage 01 outputs to understand what to research. Load parent context on-demand — only the specific file needed, never all knowledge at once.

## Outputs

What this agent produces:

| Output | Location | Purpose |
|--------|----------|---------|
| Research findings (by topic) | `outputs/by_topic/` | Primary deliverable — topic-based investigation results |
| Stage report | `outputs/reports/stage_report.md` | Async status for the manager |
| Overview report | `outputs/reports/overview_report.md` | Summary of all reports, links to each |
| Current State update | This file, "Current State" section | Pointer-tier summary of what exists |

### Stage Report

Before exiting, update `outputs/reports/stage_report.md` following the universal protocol at `.0agnostic/03_protocols/stage_report_protocol.md`. The entity manager reads this to understand your stage's status without loading stage details.

## Triggers

Load when:
- Manager delegates research work
- Entering `stage_1_02_research/`
- Investigating how delegation works in practice

## AALang Agent Context

### Local Agent Files

**Directory**: `.0agnostic/06_context_avenue_web/01_aalang/`

| File | Type | Purpose |
|------|------|---------|
| `stage_02.orchestrator.gab.jsonld` | Orchestrator | 3-mode-7-actor pattern for research investigation |
| `research.gab.jsonld` | GAB Agent | Stage identity — topic-based investigation methodology |
| `pattern_investigator.agent.jsonld` | Agent Stub | Lightweight purpose agent for pattern investigation |

```json
{
  "@id": "rs:ResearchOrchestrator",
  "@type": "gab:LLMAgent",
  "pattern": "3-mode-7-actor",
  "purpose": "Orchestrate research investigation — pattern analysis, evidence collection, findings documentation",
  "modes": ["rs:ReceiveMode", "rs:ExecuteMode", "rs:ReportMode"]
}
```

### How to Load Full Graph

```bash
# List all modes and their purposes
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' .0agnostic/06_context_avenue_web/01_aalang/stage_02.orchestrator.gab.jsonld

# Load execute mode constraints
jq '."@graph"[] | select(."@id" == "rs:ExecuteMode")' .0agnostic/06_context_avenue_web/01_aalang/stage_02.orchestrator.gab.jsonld
```

### Parent Orchestrator

**File**: `../../.0agnostic/06_context_avenue_web/01_aalang/layer_1.orchestrator.gab.jsonld` (agent_delegation_system entity)

Stage orchestrators inherit from the entity-level orchestrator.

# ── Current Status ──

## Current Status

**Status**: active | **Last Updated**: 2026-02-26

Four formal research topic directories created alongside the prior implicit research (context_chain_system as living laboratory). Topic `tool_context_cascading/`: how Claude Code, Codex, Gemini CLI, and Cursor handle context file cascading (3 of 4 cascade natively; Cursor uses glob targeting). Topic `multi_agent_context_patterns/`: how CrewAI, LangGraph, AutoGen handle shared context (all converge on minimal + on-demand, none use full cascade). Topic `scope_boundary_traversal/`: directional traversal patterns (up/down/left/right/sideways/multi-location), communication protocols per direction, infrastructure vs. content distinction. Topic `agent_class_object_patterns/`: how OOP concepts (classes, inheritance, composition, interfaces, SOLID principles) map to agent architecture — validates minimal context model as composition-over-inheritance, stage agents as single responsibility, 0AGNOSTIC.md STATIC as interface, universal infrastructure as helper/utility classes. Findings promoted to universal Principle 8 and Scope Boundary Rule.

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail

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
- **Tool context cascading varies by tool** (2026-02-26): Claude Code walks CWD→root (upward), Codex walks root→CWD (downward), Gemini CLI does bidirectional BFS (up to 200 dirs), Cursor uses glob-based rule targeting (no automatic cascade). 3 of 4 cascade natively — this means CLAUDE.md/AGENTS.md/GEMINI.md content MUST be lean to avoid context bloat at depth. See `outputs/by_topic/tool_context_cascading/`
- **Multi-agent frameworks converge on minimal context** (2026-02-26): CrewAI (selective sharing + RAG), LangGraph (graph-based state flow along edges), AutoGen (conversational message passing) — all use minimal agent context + on-demand access. None use full parent cascade. Hybrid minimal + shared state outperforms both full cascade and full isolation. See `outputs/by_topic/multi_agent_context_patterns/`
- **Scope boundary traversal is directional** (2026-02-26): When agents hit scope boundaries, they must identify direction (up/down/left/right/sideways/multi-location) before deciding what to do. Communication protocol differs per direction. Universal traversal infrastructure is loaded on-demand (not STATIC), while per-agent positional awareness (parent/children/neighbors) is compact STATIC. Multi-location work escalates to nearest common ancestor with scope over all affected locations. See `outputs/by_topic/scope_boundary_traversal/`
- **Agent architecture maps to OOP class/object patterns** (2026-02-26): OOP concepts map cleanly to agent delegation — base classes = universal infrastructure, interfaces = 0AGNOSTIC.md STATIC sections, composition = on-demand context loading, single responsibility = stage agents, factory pattern = agent instantiation via Principle 8, dependency injection = manager delegation contract. All 7 SOLID principles validated against existing patterns. Key insight: "favor composition over inheritance" directly validates the minimal context model (compose on-demand, don't cascade). Analogy breaks down for multiple inheritance, polymorphism, and strong encapsulation. See `outputs/by_topic/agent_class_object_patterns/`

## Cross-Stage Traceability

How each finding connects to requirements (stage 01) and design decisions (stage 04):

| Finding | Stage 01 (Requirement) | Stage 04 (Design Decision) |
|---------|----------------------|-----------------------------|
| Managers don't need stage methodology | 01/need_01: stage_delegation | "0AGNOSTIC.md as stage identity" — managers read pointers only |
| 0AGNOSTIC.md is the right vehicle | 01/need_01: stage_delegation, 01/need_03: agent_context_model | "0AGNOSTIC.md as stage identity" — tool-agnostic, static context |
| Two-halves pattern (→ Principle 9) | 02/need_03: three_tier_delegation | "Two-halves pattern" — operational + current state in one file |
| Stage reports enable async coordination | 01/need_02: stage_reports, 02/need_02: handoff_protocols | "Stage reports for async communication" |
| Scope boundary decisions (→ Principle 8) | 03/need_02: spawning_patterns | "Scope boundary decisions" — three-option framework |
| Scope boundaries span layers AND stages | 03/need_01: agent_hierarchy | "Scope boundaries span layers AND stages" — single rule |
| Tool context cascading (3/4 cascade natively) | 01/need_03: agent_context_model | "Minimal context model" — lean CLAUDE.md files because cascading compounds |
| Multi-agent frameworks: minimal + on-demand | 01/need_03: agent_context_model | "Minimal context model" — validated by CrewAI, LangGraph, AutoGen patterns |
| Scope boundary traversal is directional | 01/need_01: stage_delegation, 03/need_02: spawning_patterns | "Directional scope boundaries" — 3-step process, communication per direction |
| Agent class/object patterns (OOP mapping) | 01/need_03: agent_context_model, 01/need_01: stage_delegation | Validates minimal context model (composition), stage agents (SRP), canonical workspace (open/closed) |

**Stage paths**: `../stage_1_01_request_gathering/`, `../stage_1_04_design/`

## Child Layer Detail (Principle 10)

Research was primarily conducted through child entities rather than standalone documents:

| Child Entity | Research Contribution | Their Research Stage |
|-------------|----------------------|---------------------|
| **context_chain_system** (Layer 3) | Primary working example — validated stage delegation, 0AGNOSTIC.md identity, stage reports, two-halves pattern | Stage 02: 56+ files across 9 topic directories |
| **memory_system** (Layer 2) | Memory architecture research informing context model | Stage 02: 21 files on cognitive science, memory types, implementations |
| **multi_agent_system** (Layer 2) | Not yet explored as research vehicle | Stages scaffolded |

**Child paths**: see stage 01 Child Layer Detail for full paths

## Open Items

- Context chain system lessons should still be documented as a formal research topic (implicit findings formalized)
- multi_agent_system child entity not yet explored as a research vehicle

## Handoff

- **Ready for next stage**: yes (design was already done based on implicit research)
- **Next stage**: 04_design (already completed implicitly)
- **Note**: Formal research documentation would strengthen the knowledge base

# ── References ──

## Navigation

| Content | Location |
|---------|----------|
| Research outputs | `outputs/by_topic/` (when created) |
| Stage reports | `outputs/reports/` |
| Stage 01 tree of needs | `../stage_1_01_request_gathering/outputs/requests/tree_of_needs/` |

## Domain Context

For agent delegation system domain understanding, read from the parent entity:
- Parent identity: `../../0AGNOSTIC.md` (what this entity IS)
- Parent knowledge: `../../.0agnostic/01_knowledge/` (overview docs, things learned)
- Stage 01 requirements: `../stage_1_01_request_gathering/outputs/`

Do NOT load all parent knowledge at once — read the specific file relevant to the topic you're investigating.

## Success Criteria

This stage is complete when:
- Problem space is investigated with evidence
- Key patterns documented
- Gaps identified with research grounding
- Findings inform design (stage 04)

## On Exit

1. Update `outputs/reports/stage_report.md` with current status
2. If handing off to stage 04: note which findings should inform design decisions
