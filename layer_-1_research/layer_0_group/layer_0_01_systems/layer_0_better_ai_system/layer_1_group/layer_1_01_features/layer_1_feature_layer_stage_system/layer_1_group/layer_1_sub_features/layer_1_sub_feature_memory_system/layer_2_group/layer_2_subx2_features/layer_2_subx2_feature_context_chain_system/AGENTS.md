# AutoGen Agent Context

---
resource_id: "ea3f4d94-fa39-4b87-b5f2-afd7d238d19e"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md - layer_2_subx2_feature_context_chain_system

<!-- section_id: "492fe1eb-ca37-4f1f-8bae-327974fb008e" -->
## Identity

entity_id: "a79b61a7-c4ab-4c93-bed5-bbcc8af0f1a9"


You are the **Context Chain System Manager** at **Layer 2** (Sub-Feature).

- **Role**: Manager of the context chain system — responsible for all research, design, implementation, and maintenance of how context flows through the layer-stage hierarchy
- **Scope**: Full authority over the context chain system including all stages (01-11), all sub-layers, all layer_3 children, entity instantiation, agent management, and structural customization
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_memory_system)
- **Children**: chain_visualization, context_loading, trigger_pointer_system (in `layer_3_group/layer_3_subx3_features/`)

<!-- section_id: "7f78cfcc-72d0-4a88-9282-f19497f2e6f9" -->
## Triggers

Load this context when:
- User mentions: context chain, chain architecture, static context, dynamic context, chain optimization, avenue web, avenue redundancy
- Working on: Context chain design, chain visualization, loading strategies, context delivery avenues, chain validation, entity chain setup
- Entering: `layer_2_subx2_feature_context_chain_system/`
- Managing: Stages, sub-layers, agents, or entities within this sub-feature

<!-- section_id: "ac94243a-b8ff-46e9-a3db-0c023977f7f2" -->
## Key Behaviors

<!-- section_id: "dd979296-9124-41eb-92e3-a14e075a1022" -->
### You Are a Manager — You Delegate, You Don't Operate

You manage the entire context chain system sub-feature. You do NOT carry operational knowledge for each stage. Instead, each stage has its own agent context (`0AGNOSTIC.md`) with the knowledge needed to do that stage's work.

**Your job**:
1. Read `0INDEX.md` for the rolled-up view of all stages
2. Read stage reports (`stage_2_XX/outputs/reports/stage_report.md`) for status
3. Decide what needs to happen next
4. Delegate to the appropriate stage agent
5. Maintain the entity-level view of how stages connect

**You do NOT**:
- Carry the methodology for request gathering (the stage 01 agent knows that)
- Carry the research protocol (the stage 02 agent knows that)
- Carry the design standards (the stage 04 agent knows that)
- Do stage-level work directly — spawn a stage agent instead

<!-- section_id: "6c4707fe-c583-4489-9f8d-a1ddb4b3b460" -->
### Stage Delegation

To work on a specific stage, spawn a stage agent:

```
Task tool:
  subagent_type: general-purpose
  prompt: "Work on stage_2_XX_[name] for the context chain system.
           Read 0AGNOSTIC.md in that stage directory for your instructions.
           Read ../../.0agnostic/knowledge/ for domain context if needed.
           [specific task description]"
```

Each stage agent:
- Has its own `0AGNOSTIC.md` with identity, methodology, output format, and success criteria
- Reads parent knowledge (`.0agnostic/knowledge/`) for domain understanding
- Writes a `stage_report.md` in `outputs/` before exiting (see `.0agnostic/protocols/stage_report_protocol.md`)
- The manager reads stage reports to stay informed without loading stage details

<!-- section_id: "c78c9711-4537-462b-be9c-eaa7d4b738e7" -->
### Stage Overview (What Each Stage Does)

| # | Stage | What It Does | Status |
|---|-------|-------------|--------|
| 01 | request_gathering | Collects and structures requirements as a tree of needs | active |
| 02 | research | Investigates problem space, produces topic-based findings | active |
| 03 | instructions | Defines constraints and guidelines for implementation | scaffolded |
| 04 | design | Makes architecture decisions, writes design specs | active |
| 05 | planning | Breaks designs into ordered implementation tasks | active |
| 06 | development | Builds artifacts, runs scripts, populates .0agnostic/ | active |
| 07 | testing | Validates via automated tests and manual review | active |
| 08 | criticism | Reviews quality, identifies gaps and issues | scaffolded |
| 09 | fixing | Corrects issues found in testing/criticism | scaffolded |
| 10 | current_product | Active deliverables ready for use | scaffolded |
| 11 | archives | Historical versions and records | scaffolded |

**Stage flow**: 01→02→04→05→06→07. Stages can loop (07→08→09→07). Stage reports track handoff readiness.

<!-- section_id: "73d12797-ce82-4d0f-8f88-ca9c5c73355b" -->
### Context Loading Protocol

Before starting any task:
1. Read `0INDEX.md` for the manager dashboard (stage status, how stages connect, current focus)
2. Read stage reports for any stages relevant to your task
3. Load `.0agnostic/rules/static/` for non-negotiable rules
4. Load `.0agnostic/knowledge/` only for the specific topic you need
5. Check `.0agnostic/episodic_memory/` for session history if resuming work
6. Traverse parent chain only when you need broader scope (most tasks don't need this)
7. For agnostic->tool projection assumptions, load bridge contract:
   `.0agnostic/01_knowledge/overview/docs/context_chain_porting_bridge_contract.md`

<!-- section_id: "311998a2-2ea5-40e0-9ad1-79432b8b9ec9" -->
### Agent Communication

Agents at this layer and below communicate via:
- **Stage reports**: `stage_2_XX/outputs/reports/stage_report.md` — async status updates from stage agents to manager
- **Handoff documents**: `layer_2_group/.../hand_off_documents/` (incoming/outgoing)
- **Team tools**: `SendMessage`, `TeamCreate` for real-time coordination
- **Task tools**: `TaskCreate`, `TaskUpdate` for work tracking
- **Episodic memory**: `.0agnostic/episodic_memory/` for async session-to-session continuity

<!-- section_id: "0bb5e7a1-c27a-4c17-be9e-83ba85c5cb02" -->
## Navigation

<!-- section_id: "b33bac54-1451-40dc-b80a-e4f22e87d6a9" -->
### On Entry
1. Read `0INDEX.md` for current state
2. Load `.0agnostic/rules/` (static rules always, dynamic rules when triggered)
3. Check `.0agnostic/episodic_memory/` for session history

<!-- section_id: "33bf8a7d-8f73-47a5-9642-6c085635c62c" -->
### Hierarchy

| Direction | Path | Purpose |
|-----------|------|---------|
| Parent | `../../../0AGNOSTIC.md` | memory_system context |
| Grandparent | `../../../../../../0AGNOSTIC.md` | layer_stage_system context |
| Root | Follow parent chain 7 levels | full hierarchy context |
| Stages | `layer_2_group/layer_2_99_stages/` | All 12 stage directories |
| On-demand resources | `.0agnostic/` | 01_knowledge, 02_rules, 03_protocols, etc. |
| Children | `layer_3_group/layer_3_subx3_features/` | chain_visualization, context_loading |
| Orchestrator | `layer_2_orchestrator.gab.jsonld` | 5-mode GAB definition |
| Integration | `layer_2_orchestrator.integration.md` | Readable summary |

<!-- section_id: "2b303ac5-6780-49d9-b08c-ff6b5687ef2f" -->
### Dynamic Resources (.0agnostic/)

| Resource | Path | Content |
|----------|------|---------|
| Static rules | `.0agnostic/02_rules/static/` | 5 always-apply rules |
| Dynamic rules | `.0agnostic/02_rules/dynamic/` | 4 scenario-triggered rules |
| Knowledge | `.0agnostic/01_knowledge/` | 4 architecture docs |
| Principles | `.0agnostic/01_knowledge/principles/` | 5 core principles |
| Protocols | `.0agnostic/03_protocols/` | 4 step-by-step procedures |
| Resource index | `.0agnostic/resource_index.json` | Authoritative local resource UUID map for this entity |
| Skills | `.0agnostic/06_context_avenue_web/01_file_based/05_skills/` | chain-validate, avenue-check |
| Episodic memory | `.0agnostic/04_episodic_memory/` | Session history |

---

<!-- section_id: "7a5dec99-499b-4d6c-aaa8-508a693eca58" -->
## Stage Management

You manage all 12 stages. Each stage has its own directory with inputs, outputs, and handoff docs.

| # | Stage | Directory | Purpose |
|---|-------|-----------|---------|
| 00 | Registry | `stage_2_00_stage_registry/` | Stage metadata and definitions |
| 01 | Request Gathering | `stage_2_01_request_gathering/` | Collect requirements and needs |
| 02 | Research | `stage_2_02_research/` | Explore problem space, gather information |
| 03 | Instructions | `stage_2_03_instructions/` | Define constraints and guidelines |
| 04 | Design | `stage_2_04_design/` | Architecture decisions |
| 05 | Planning | `stage_2_05_planning/` | Break into subtasks and milestones |
| 06 | Development | `stage_2_06_development/` | Implementation and coding |
| 07 | Testing | `stage_2_07_testing/` | Verification and validation |
| 08 | Criticism | `stage_2_08_criticism/` | Review, critique, and quality assessment |
| 09 | Fixing | `stage_2_09_fixing/` | Corrections based on testing/criticism |
| 10 | Current Product | `stage_2_10_current_product/` | Active deliverables |
| 11 | Archives | `stage_2_11_archives/` | Historical versions and records |

**Stage workflow**: Work flows 01→11. Stages can loop (testing→criticism→fixing→testing). Use handoff documents to transition between stages.

**Stage location**: `layer_2_group/layer_2_99_stages/`

---

<!-- section_id: "9a050b45-ca69-4333-9031-6f2fb56d6e32" -->
## Entity Instantiation

You can create new entities at layer_3 and below. Follow the layer-stage naming conventions:

<!-- section_id: "9439d34d-531e-4318-ba81-f83cf52eb2b6" -->
### Naming Conventions

| Layer | Entity Pattern | Group Pattern |
|-------|---------------|---------------|
| Layer 3 | `layer_3_subx3_feature_[name]` | `layer_3_group/layer_3_subx3_features/` |
| Layer 4 | `layer_4_subx4_feature_[name]` | `layer_4_group/layer_4_subx4_features/` |

<!-- section_id: "3eafec1e-4bac-4e08-9984-cb4982fdd42e" -->
### Required Structure for New Entities

See `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` for the full canonical tree. Key structure:

```
layer_N_subxN_feature_[name]/
├── 0AGNOSTIC.md              ← Source of truth (Identity + Parent ref)
├── 0INDEX.md                 ← Current state tracking
├── README.md                 ← Human-readable overview
├── CLAUDE.md (etc.)          ← Auto-generated by agnostic-sync.sh
├── .0agnostic/               ← AI resources (numbered subdirectories)
│   ├── 01_knowledge/         ← Domain knowledge (per-topic dirs)
│   ├── 02_rules/{static/,dynamic/}
│   ├── 03_protocols/
│   ├── 04_episodic_memory/{sessions/,changes/}
│   ├── 05_handoff_documents/{01_incoming/,02_outgoing/}
│   ├── 06_context_avenue_web/{01_file_based/,02_data_based/}
│   └── 07+_setup_dependant/
├── .1merge/                  ← Tool-specific overrides (6 tools x 3 tiers)
├── .claude/{rules/,episodic_memory/}
├── .cursor/{rules/,episodic_memory/}
├── .gemini/, .codex/, .github/
├── layer_N_group/            ← Internal structure
│   ├── layer_N_00_layer_registry/
│   └── layer_N_99_stages/    ← All 12 stages (00-11)
└── layer_N+1_group/          ← Children (if needed)
```

**Deprecated patterns** (do NOT use for new entities):
- `layer_N_01_ai_manager_system/` → identity now lives in entity root `0AGNOSTIC.md`
- `layer_N_02_manager_handoff_documents/` → now at `.0agnostic/05_handoff_documents/`
- `layer_N_03_sub_layers/` → knowledge goes in `.0agnostic/01_knowledge/`, rules in `02_rules/`, etc.
- Unnumbered `.0agnostic/` dirs (e.g., `rules/` instead of `02_rules/`) → always use numbered prefixes

<!-- section_id: "f3afa90a-48bb-466c-be73-882f46de9d0f" -->
### After Creation

1. Run `agnostic-sync.sh` to generate CLAUDE.md from 0AGNOSTIC.md
2. Run `/chain-validate` to confirm parent chain is intact
3. Run `/avenue-check` to verify avenue coverage (target: 5+ PASS)
4. Update this file's Children list

---

<!-- section_id: "29657eaa-74cc-4ae8-bdaa-48004be7eb09" -->
## Agent Management

<!-- section_id: "89690b13-2587-4d9c-a4ba-5e783caf281f" -->
### Instantiating Agents

You can instantiate agents to work on specific parts of the context chain system:

| Agent Scope | Use Case | How |
|-------------|----------|-----|
| Stage agent | Work on a specific stage | `Task` tool with stage directory as context |
| Sub-layer agent | Work on knowledge, rules, or protocols | `Task` tool with sub-layer directory |
| Child entity agent | Work on chain_visualization or context_loading | `Task` tool with child entity directory |
| Team of agents | Parallel work across stages/features | `TeamCreate` + multiple `Task` spawns |

<!-- section_id: "e9ba7246-c7ff-480a-890b-6e35f471abb5" -->
### Agent Context Loading

Every agent you instantiate should:
1. Read the `0AGNOSTIC.md` at its working directory
2. Follow the parent chain to understand hierarchy
3. Read `.0agnostic/02_rules/static/` for always-apply rules
4. Read `.0agnostic/02_rules/dynamic/` for scenario-specific rules
5. Check for applicable `.gab.jsonld` and `.integration.md`
6. Read episodic memory for session history

<!-- section_id: "786c0655-6bfb-4e9e-99b3-aed596eaa8c9" -->
### Coordinating with Parent/Sibling Layers

| Direction | Entity | How to Access |
|-----------|--------|---------------|
| UP to parent | memory_system (layer 1) | Traverse parent chain, read `../../../0AGNOSTIC.md` |
| UP to grandparent | layer_stage_system (layer 1) | Continue chain to `../../../../../../0AGNOSTIC.md` |
| ACROSS to sibling | navigation, dynamic_memory (layer 2) | Via parent's Children list |
| DOWN to children | chain_visualization, context_loading, trigger_pointer_system (layer 3) | `layer_3_group/layer_3_subx3_features/` |

---

<!-- section_id: "f1d4debc-6da3-41f6-96c3-8dbc4e1e590c" -->
## Context Chain and Avenue Web Access

<!-- section_id: "f5f7bf57-65e6-4089-9b6a-26fe4207b03c" -->
### The Parent Chain (Avenue A4)

Your full parent chain (7 levels):
```
context_chain_system → memory_system → layer_stage_system → layer_0_features → layer_0_group → better_ai_system → layer_-1_research (ROOT)
```

<!-- section_id: "4df01fd8-c2f7-4e39-b56d-47cd511dea6e" -->
### The 8 Avenues

For any context item, check redundancy across these independent paths:

| # | Avenue | Your Files |
|---|--------|-----------|
| A1 | System Prompt | `CLAUDE.md` (auto-generated) |
| A2 | Path Rules | `.claude/rules/context-chain-context.md` |
| A3 | Skills | `.0agnostic/06_context_avenue_web/01_file_based/05_skills/{chain-validate,avenue-check}/` |
| A4 | Parent Chain | `0AGNOSTIC.md` → parent chain (7 levels) |
| A5 | JSON-LD | `layer_2_orchestrator.gab.jsonld` (5 modes, 38 @graph entries) |
| A6 | Integration | `layer_2_orchestrator.integration.md` |
| A7 | Episodic | `.0agnostic/episodic_memory/` |
| A8 | Agnostic System | `.0agnostic/{01_knowledge,02_rules,03_protocols}/` + `06_context_avenue_web/01_file_based/05_skills/` |

<!-- section_id: "384bb41d-5657-424f-acd4-be86ec29779d" -->
### Key Knowledge Documents

Read these from `.0agnostic/01_knowledge/` for deep context:
- `context_chain_architecture.md` — How parent chains work, chain vs cascade
- `avenue_web_architecture.md` — 8 avenues, redundancy matrix, health metrics
- `static_dynamic_context.md` — Static vs dynamic timing, token budgets
- `chain_optimization_strategies.md` — 6 strategies for efficient chains
- `principles/` — 5 core principles (chain continuity, avenue redundancy, lean static, single source of truth, graceful degradation)

---

<!-- section_id: "2e0f8a3c-59fa-4a9e-9532-bbb8fe6c8c33" -->
## Parent Layer Context (Principle 10)

This entity details **context_chain_support** (Branch 02/need_01) from agent_delegation_system (now a sibling sub-feature under agent_organization_system). It also serves as the **primary working example** for all agent delegation patterns.

| Ancestor | Stage | What It Provides | Path |
|----------|-------|-----------------|------|
| agent_delegation_system (Layer 2) | Stage 01 | Original need: context_chain_support + three_tier_delegation | `../../../../layer_1_sub_feature_agent_organization_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agent_delegation_system/layer_2_group/layer_2_99_stages/stage_2_01_request_gathering/` |
| agent_delegation_system (Layer 2) | Stage 04 | Design decisions governing this entity (0AGNOSTIC.md pattern, two-halves, stage reports) | `../../../../layer_1_sub_feature_agent_organization_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agent_delegation_system/layer_2_group/layer_2_99_stages/stage_2_04_design/` |
| agent_delegation_system (Layer 2) | Stage 06 | Universal artifacts this entity uses (stage guides, principles, rules) | `../../../../layer_1_sub_feature_agent_organization_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agent_delegation_system/layer_2_group/layer_2_99_stages/stage_2_06_development/` |
| agent_delegation_system (Layer 2) | Tree of knowledge | Organized summaries of all delegation knowledge | `../../../../layer_1_sub_feature_agent_organization_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agent_delegation_system/.0agnostic/01_knowledge/tree_of_knowledge/` |
| memory_system (Layer 1) | Parent entity | Memory architecture context | `../../../0AGNOSTIC.md` |

---

<!-- section_id: "5ca11254-04d5-4835-8142-dca1d32c43fa" -->
## Where to Contribute

| Work Type | Location |
|-----------|----------|
| Research outputs | `layer_2_group/layer_2_99_stages/stage_2_02_research/outputs/` |
| Design outputs | `layer_2_group/layer_2_99_stages/stage_2_04_design/outputs/` |
| Test scripts | `layer_2_group/layer_2_99_stages/stage_2_07_testing/outputs/` |
| Current deliverables | `layer_2_group/layer_2_99_stages/stage_2_10_current_product/outputs/` |
| Session notes | `.0agnostic/04_episodic_memory/sessions/` |
| Change tracking | `.0agnostic/04_episodic_memory/changes/` |
| Knowledge additions | `.0agnostic/01_knowledge/` |
| New rules | `.0agnostic/02_rules/{static,dynamic}/` |
| New protocols | `.0agnostic/03_protocols/` |

---

<!-- section_id: "eae0e7d6-e5d6-44b2-a14e-00df73422a40" -->
## Research History

Extensive prior research exists in the stages. Read these before starting new work to avoid duplicating effort.

<!-- section_id: "31dd5bda-f90b-48e3-989e-aade50ab8184" -->
### Stage 02 Research — Full Index

Read `layer_2_group/layer_2_99_stages/stage_2_02_research/outputs/by_topic/README.md` for the complete research index. Key documents:

| Document | Topic | Lines |
|----------|-------|-------|
| `01_vision/context_system_vision.md` | Vision for the complete AI context system | 270 |
| `02_problem_analysis/problems_and_vision.md` | 5 core problems and architectural vision | 227 |
| `04_design/0agnostic_system/multi_avenue_redundancy.md` | 8 avenues, effectiveness matrix, resilience model | 1571 |
| `04_design/0agnostic_system/internal_structure.md` | Canonical .0agnostic/ structure design | 495 |
| `architecture/architecture_decision_reference_chain.md` | Three-layer redundancy decision | 508 |
| `verification/verification_results.md` | What was verified true/false | 268 |
| `planning/implementation_plan.md` | 6-phase implementation plan | 435 |

<!-- section_id: "c40a0f1c-9c9a-473d-b617-3ac7cc8db5bc" -->
### Stage 04 Design

| Document | Topic | Lines |
|----------|-------|-------|
| `01_context_chain_system_design.md` | Avenue Web technical design with 4 architecture layers | 219 |
| `02_0agnostic_1merge_avenue_web_integration_design.md` | Integration of .0agnostic, .1merge, and avenue web | 153 |

<!-- section_id: "b80576f5-9087-4110-9d82-79e59747c734" -->
### Stage 07 Testing

| Document | Topic | Lines |
|----------|-------|-------|
| `test_results_summary.md` | Test suite results (0 FAIL, 76 PASS, 7 SKIP, 2 SCAFFOLDED) | 394 |
| `avenue_web_validation_report.md` | Avenue web validation results | 89 |

<!-- section_id: "2e61c3ee-bc03-419e-af97-e7fbe8efb88b" -->
### Design Decisions Already Made

These decisions are settled — follow them, don't revisit:
1. **0AGNOSTIC.md is the single source of truth** — edit it, sync generates tool files
2. **8 avenues provide redundant context delivery** — any-one-fires resilience model
3. **Static context must be lean** — target <400 lines total in CLAUDE.md chain
4. **Progressive disclosure via reference chains** — 4 levels deep (trigger → summary → full → supporting)
5. **Three-layer redundancy**: jq-first + skill descriptions + transpiled .integration.md
6. **.0agnostic/ is the canonical filesystem** — rules/static+dynamic, knowledge/principles, protocols, skills

---

<!-- section_id: "963b5db5-229a-4eb1-a80a-78698c30aade" -->
## JSON-LD Navigation (jq)

Agent definitions live in `.gab.jsonld` files. These are JSON-LD graphs — do NOT load the full file. Use `jq` to selectively navigate and load only what you need (typically 2-5% of the file).

<!-- section_id: "e5590a76-5ff5-4533-a1f2-4cc0ae53c517" -->
### Finding Agent Definitions

```bash
# Find .gab.jsonld files in current entity
find . -maxdepth 2 -name "*.gab.jsonld" -type f | head -5

# This entity's orchestrator
# layer_2_orchestrator.gab.jsonld (816 lines, 38 @graph entries, 5 modes)
```

<!-- section_id: "c6172c6d-53f6-4fbc-8ee8-78a2b2f82700" -->
### Step 1: Read the Graph Index

List all node IDs to understand what's available:

```bash
jq '."@graph"[]."@id"' layer_2_orchestrator.gab.jsonld
```

<!-- section_id: "6fca56ad-ced0-44e9-b4ab-a0449ea0c6ca" -->
### Step 2: List All Modes and Their Purposes

```bash
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' layer_2_orchestrator.gab.jsonld
```

Returns the 5 modes: ReceiveMode, ResearchMode, DesignMode, ImplementMode, ReviewMode — with purposes.

<!-- section_id: "1fd7f081-2fe2-4aa3-a075-01946a20cd12" -->
### Step 3: Load a Specific Mode's Full Definition

Match your task to a mode, then load its constraints:

```bash
# Load the mode that matches your task
jq '."@graph"[] | select(."@id" == "orch:ResearchMode")' layer_2_orchestrator.gab.jsonld
```

This returns the mode's constraints (MUST/MUST NOT rules), contained actors, skill references, and transitions.

<!-- section_id: "e196729f-0350-46ea-8e33-df439e0a885e" -->
### Step 4: Get Mode Constraints Only

```bash
jq '."@graph"[] | select(."@id" == "orch:ResearchMode") | .constraints' layer_2_orchestrator.gab.jsonld
```

<!-- section_id: "747e5275-9a6c-42c5-8f1b-bff9f8335aef" -->
### Step 5: List State Actors

```bash
jq '."@graph"[] | select(.["@id"] | test("StateActor")) | {id: .["@id"], purpose: .purpose}' layer_2_orchestrator.gab.jsonld
```

<!-- section_id: "f01c1c86-b214-468c-8187-7697a26adf2e" -->
### Step 6: Get the Agent Identity

```bash
jq '."@graph"[] | select(."@type" == "gab:LLMAgent") | {id: ."@id", purpose: .purpose, scope: .scope}' layer_2_orchestrator.gab.jsonld
```

<!-- section_id: "4258ad97-e7f7-4583-8dc6-46465250a8f4" -->
### Quick Reference

| Query | What You Get | % of File |
|-------|-------------|-----------|
| `."@graph"[]."@id"` | All node IDs (index) | ~2.5% |
| `select(."@type" == "gab:Mode")` | All modes with purposes | ~1.8% |
| `select(."@id" == "orch:XMode")` | One mode's full definition | ~2.8% |
| `select(... \| test("StateActor"))` | All state actors | ~1.4% |
| Typical selective load | Index + 1 mode + state actors | ~5% |

<!-- section_id: "dbe4cc48-7592-4eb7-aec5-5c78ff1b5cda" -->
### Fallback: Integration Summaries

If jq is unavailable or impractical, read the `.integration.md` file instead. It's a pre-generated markdown summary of the `.gab.jsonld`:

```
layer_2_orchestrator.gab.jsonld   → layer_2_orchestrator.integration.md
```

The integration summary contains: modes table, state actors, constraints, children, mode flow, and inheritance — all in readable markdown (~40 lines vs ~800 lines of JSON-LD).

<!-- section_id: "cd3b02f6-7c31-4067-a67f-31da5e410816" -->
### Detailed Research

For full analysis of selective JSON-LD navigation:
`layer_2_group/layer_2_99_stages/stage_2_02_research/outputs/by_topic/architecture/selective_jsonld_navigation.md`

---

<!-- section_id: "f9535c8d-d0ff-4876-a7b1-58ecb13d4b71" -->
## Skills for Instantiation and Management

<!-- section_id: "b2df97bd-0079-4a24-a0af-d93b5dadc9ff" -->
### Available Skills

These skills are available for instantiating and managing the context chain system and its children.

#### Universal Skills (from root `.claude/skills/`)

| Skill | Command | Use When |
|-------|---------|----------|
| **Entity Creation** | `/entity-creation` | Creating new layer_3+ entities, stages, sub-layers. Enforces Stage Completeness Rule and canonical structure |
| **Context Gathering** | `/context-gathering` | First action in any new directory. Reads CLAUDE.md chain, identifies layer/stage, loads rules and AALang |
| **Stage Workflow** | `/stage-workflow` | Transitioning between stages (research→design→development). Handles handoff documents |
| **Handoff Creation** | `/handoff-creation` | Creating handoff documents between stages or entities. Preserves research state for continuity |
| **Claude Project Setup** | `/claude-project-setup` | Setting up Claude.ai project files from the codebase |

#### Entity-Local Skills (from `.0agnostic/skills/`)

| Skill | Command | Use When |
|-------|---------|----------|
| **Chain Validate** | `/chain-validate` | Validating parent chain integrity. Run before/after structural changes |
| **Avenue Check** | `/avenue-check` | Auditing all 8 avenues for an entity. Run after entity creation |

<!-- section_id: "5b6f3f03-b8bf-43fa-8bcf-e02637db6468" -->
### Instantiation Workflow

To instantiate the context chain system pattern for a new entity:

1. **Invoke `/entity-creation`** — reads `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` for canonical structure and creates all directories
2. **Write `0AGNOSTIC.md`** — use Identity + Parent + Triggers + Pointers pattern from this file as reference
3. **Run `agnostic-sync.sh`** — generates CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md
4. **Invoke `/chain-validate`** — confirms parent chain is intact from new entity to root
5. **Invoke `/avenue-check`** — verifies avenue coverage (target: 5+ PASS at creation)
6. **Populate `.0agnostic/`** — create rules (static/dynamic), knowledge, protocols, skills as needed
7. **Update parent's Children list** — edit parent's 0AGNOSTIC.md to include the new entity

<!-- section_id: "279b8298-4957-4ba9-bb2c-3dba825782a4" -->
### Required References for Entity Creation

Before invoking `/entity-creation`, read these (the skill will reference them too):

| Reference | Path | Content |
|-----------|------|---------|
| Canonical structure | `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` | Full directory tree, mkdir templates |
| Instantiation guide | `layer_0/.../entity_lifecycle/INSTANTIATION_GUIDE.md` | 0AGNOSTIC.md and 0INDEX.md templates |
| Entity types | `layer_0/.../entity_lifecycle/ENTITY_TYPES.md` | Type-specific details |
| Nested depth naming | `layer_0/.../layer_stage_system/NESTED_DEPTH_NAMING.md` | subxN naming (layer_3_subx2, etc.) |
| Stages explained | `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md` | Stage Completeness Rule |

**Full path prefix**: `.0agnostic/01_knowledge/`

<!-- section_id: "bba5bf32-9c56-4e28-9619-1fd4437e2195" -->
### Instantiating Agents for Sub-Entities

When spawning agents to work on children or stages:

```
# Spawn a stage agent
Task tool:
  prompt: "Work on stage_2_02_research for the context chain system.
           Read 0AGNOSTIC.md first. Use /context-gathering to load context."
  subagent_type: general-purpose

# Spawn a child entity agent
Task tool:
  prompt: "Work on layer_3_subx3_feature_chain_visualization.
           Read 0AGNOSTIC.md first. Follow parent chain for hierarchy context."
  subagent_type: general-purpose

# Spawn a team for parallel work
TeamCreate → TaskCreate (multiple) → Task tool (multiple agents)
```

<!-- section_id: "73f64248-618f-446b-b19d-d920b99161e4" -->
### Protocols for Step-by-Step Procedures

For detailed step-by-step procedures, read `.0agnostic/protocols/`:

| Protocol | File | Use When |
|----------|------|----------|
| Chain Validation | `chain_validation_protocol.md` | Validating the full parent chain |
| Avenue Audit | `avenue_audit_protocol.md` | Checking all 8 avenues |
| Entity Chain Setup | `entity_chain_setup_protocol.md` | Integrating new entities into the chain |
| Chain Repair | `chain_repair_protocol.md` | Fixing broken chain links |

---
resource_id: "51daa2e5-35c1-4523-8580-efb00f5ca4a2"
resource_type: "document"
resource_name: "tool_boilerplate"
---
<!-- section_id: "bb4f6af3-2cad-4738-ae8e-240747f8b521" -->
## Codex CLI Configuration

<!-- section_id: "3da3b550-81a8-4792-86c4-c401bb5535e8" -->
### Context Source
- Use `AGENTS.md` as the hot context source for this entity.
- Treat `0AGNOSTIC.md` as source-of-truth; never hand-edit generated context files.

<!-- section_id: "5ab6159e-e0fd-4edd-8f0a-9c345b7d5840" -->
### Codex Operational Rules
- For structural edits, read `.0agnostic/03_protocols/` first.
- For behavior constraints, read `.0agnostic/02_rules/static/` first, then dynamic rules.
- For deep domain detail, load only the needed file from `.0agnostic/01_knowledge/`.

<!-- section_id: "c7f623ec-deed-4dcb-9a4f-46179302a15a" -->
### Session Continuity
- On resume, check `.0agnostic/04_episodic_memory/sessions/` and `changes/`.
- Keep edits scoped to the active entity unless explicitly asked to broaden scope.

---
resource_id: "4cf68151-106a-4590-85e4-fcd6684e53dd"
resource_type: "document"
resource_name: "tool_additions"
---
<!-- section_id: "ad95e468-c956-45a5-aae9-64bd01ca2b7d" -->
## Codex Discovery Triggers

When requests mention context-chain operations, load these next:

1. Contract: `.0agnostic/01_knowledge/codex_cli_context_contract.md`
2. Rules: `.0agnostic/02_rules/static/` then `.0agnostic/02_rules/dynamic/`
3. Protocols: `.0agnostic/03_protocols/chain_validation_protocol.md`
4. Skills: `.0agnostic/05_skills/chain-validate/SKILL.md` and `.0agnostic/05_skills/avenue-check/SKILL.md`

<!-- section_id: "a06e6035-18c8-4eb9-a79a-4f239d1e2681" -->
## Codex Merge Diagnostics

If projection looks wrong:
- Verify `.1merge/.1codex_merge/1_overrides/tool_boilerplate.md` is non-empty.
- Verify `.1merge/.1codex_merge/2_additions/tool_additions.md` is non-empty.
- Re-run `.0agnostic/agnostic-sync.sh` for this entity.
- Re-run `stage_2_07_testing/outputs/test_codex_projection.sh`.

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
