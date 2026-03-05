---
resource_id: "760c4490-cb7a-494e-ae99-ebc2d5147e96"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: stage-workflow
description: "Work through stages (01-11) properly, understanding what content belongs in each stage. Use when starting feature work, determining which stage to work in, moving between stages, or creating stage outputs."
---

# Stage Workflow Skill

<!-- section_id: "12f6cee5-633f-4489-bf7c-a4cc91d222c5" -->
## WHEN to Use
- Starting work on a new feature or project (need to identify which stage)
- Moving content between stages
- The user asks "which stage should this go in?"
- Creating stage outputs (research docs, plans, designs, code)
- When stage transitions are needed (e.g., done with research, moving to planning)

<!-- section_id: "90e934a1-f6c1-4b41-b776-e84fcb43c17b" -->
## WHEN NOT to Use
- Working entirely within a single known stage on a known task
- Simple file edits where the stage is obvious
- Non-stage-related work (e.g., updating global rules)

<!-- section_id: "5dcd6ee9-48ff-44ec-a8ce-5fc16e852b38" -->
## References (MUST READ)

| Reference | Path | Why |
|-----------|------|-----|
| Stages | `.0agnostic/01_knowledge/layer_stage_system/STAGES_EXPLAINED.md` | Stage purposes, completeness rule |
| Sub-stages | `.0agnostic/01_knowledge/layer_stage_system/SUB_STAGES_EXPLAINED.md` | When to use sub-stages |
| Overview | `.0agnostic/01_knowledge/layer_stage_system/OVERVIEW.md` | System overview |
| Stage guides | `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_NN_NAME.md` | What each stage agent does — identity, methodology, inputs/outputs, boundaries |
| Agent template | `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` | Template for writing stage 0AGNOSTIC.md files |
| Delegation principles | `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` | 7 core principles governing stage delegation |

**Knowledge path**: `.0agnostic/01_knowledge/layer_stage_system/`

<!-- section_id: "aabe8cb5-8bca-4e22-a46c-d06d47373a5d" -->
## Protocol

<!-- section_id: "83f296a4-85f5-4e8f-8644-0ee33f357e79" -->
### 1. Identify Current Stage

Ask: "What phase of work am I in?"

| If doing... | Use stage |
|-------------|-----------|
| Gathering requirements | 01_request_gathering |
| Researching solutions | 02_research |
| Defining constraints | 03_instructions |
| Designing architecture | 04_design |
| Breaking down tasks | 05_planning |
| Implementing | 06_development |
| Testing/validating | 07_testing |
| Reviewing/critiquing | 08_criticism |
| Fixing issues | 09_fixing |
| Finalizing deliverable | 10_current_product |
| Archiving old versions | 11_archives |

<!-- section_id: "457429a0-820c-4bcb-ab42-f3bd83d4636f" -->
### 2. Work in outputs/ Folder

All stage content goes in `outputs/`:

```
stage_X_04_design/
└── outputs/
    ├── architecture.md
    ├── diagrams/
    └── decisions.md
```

<!-- section_id: "e40b048b-721a-4019-856c-87cf2608f692" -->
### 3. Stage Agent Delegation

Each stage has a dedicated agent role. Before operating in a stage:

1. **Read the stage guide**: `stage_guides/STAGE_NN_NAME.md` — defines what the agent IS and IS NOT
2. **Respect scope boundaries**: Do NOT perform work belonging to another stage (see `02_rules/static/STAGE_BOUNDARY_RULE.md`)
3. **Write a stage report**: Before leaving, update `outputs/stage_report.md` (see `03_protocols/stage_report_protocol.md`)
4. **Managers delegate, agents operate**: The entity manager reads stage reports and decides what to delegate — it does not carry operational methodology

**Key rules** (in `.0agnostic/02_rules/`):

| Rule | Type | What It Says |
|------|------|-------------|
| Stage Boundary Rule | Static | Never do work belonging to another stage |
| Stage Report Rule | Static | Always write stage_report.md before exiting |
| Manager Delegation Rule | Static | Managers delegate; agents operate within scope |
| Stage Loop Rule | Dynamic | How to loop back (07→08→09→07 quality loop) |
| Parallel Stages Rule | Dynamic | How to run stages concurrently (01+02) |

<!-- section_id: "3a1a3ad4-c4ed-4b2e-8113-974ea689594e" -->
### 4. Stage Transitions

When moving to next stage:
1. Ensure current stage outputs are complete
2. Write/update `outputs/stage_report.md` with status and handoff notes
3. Create handoff document (optional — use `/handoff-creation`)
4. Move to next stage folder
5. Reference previous stage outputs as needed

<!-- section_id: "f3ea11fd-5492-48d3-9d74-0686ee7f0325" -->
### 5. [CRITICAL] Never Skip Stages

All 11 stages must exist, even if empty.

If a stage isn't needed for this work:
- Leave it empty
- Do NOT delete it
- Do NOT skip creating it

<!-- section_id: "cccd0f41-d32e-476b-ab01-bd2d496c2e04" -->
## Stage Content Guide

| Stage | Key Outputs | Guide |
|-------|-------------|-------|
| 01 | requirements.md (tree of needs), user_stories.md | `STAGE_01_REQUEST_GATHERING.md` |
| 02 | topic-based research dirs with README.md index | `STAGE_02_RESEARCH.md` |
| 03 | constraints.md (MUST/MUST NOT), guidelines.md | `STAGE_03_INSTRUCTIONS.md` |
| 04 | design.md (architecture + rationale + alternatives) | `STAGE_04_DESIGN.md` |
| 05 | plan.md (ordered tasks, dependencies, MVP-first) | `STAGE_05_PLANNING.md` |
| 06 | artifacts in entity root (not outputs/) + status tracking | `STAGE_06_DEVELOPMENT.md` |
| 07 | test scripts (run_all_tests.sh), test_results.md | `STAGE_07_TESTING.md` |
| 08 | critique.md (critical/major/minor/suggestion severity) | `STAGE_08_CRITICISM.md` |
| 09 | fixes_log.md (what, why, where, verification) | `STAGE_09_FIXING.md` |
| 10 | promoted deliverables (from earlier stages) | `STAGE_10_CURRENT_PRODUCT.md` |
| 11 | versioned snapshots, CHANGELOG.md | `STAGE_11_ARCHIVES.md` |

<!-- section_id: "29a6be2c-5ab0-41da-a6d3-ce506c2c08e2" -->
## Agent Context

Before starting stage work:
1. Find the `.gab.jsonld` for your role in the stage directory
2. Read the matching `.integration.md` (same base name) for mode constraints and allowed transitions
3. Query via jq for precise stage-specific constraints if needed

<!-- section_id: "5596b42d-3969-4fcb-a98d-a56e95781936" -->
## Agnostic System

When working in a stage directory:
- If `0AGNOSTIC.md` exists, it is the **source of truth** — edit it, not `CLAUDE.md`
- If `.0agnostic/` exists, check for stage-specific resources
- After modifying `0AGNOSTIC.md`, run `agnostic-sync.sh` to regenerate tool-specific files
- If `.1merge/` exists, it provides tool-specific overrides

<!-- section_id: "24c3497c-8cd0-4baf-83ff-3d3a2e520e47" -->
## AALang Reference

Stage workflows are managed by the orchestrator's StageStateActor:
`layer_0/layer_0_01_ai_manager_system/personal/layer_0_orchestrator.gab.jsonld`

The StageStateActor tracks current stage (01-11) and stage-specific specialists.

---

*This skill ensures proper stage workflow following STAGES_EXPLAINED.md and stage guides*
