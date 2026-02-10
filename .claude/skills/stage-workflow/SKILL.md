---
name: stage-workflow
description: "Work through stages (01-11) properly, understanding what content belongs in each stage. Use when starting feature work, determining which stage to work in, moving between stages, or creating stage outputs."
---

# Stage Workflow Skill

## WHEN to Use
- Starting work on a new feature or project (need to identify which stage)
- Moving content between stages
- The user asks "which stage should this go in?"
- Creating stage outputs (research docs, plans, designs, code)
- When stage transitions are needed (e.g., done with research, moving to planning)

## WHEN NOT to Use
- Working entirely within a single known stage on a known task
- Simple file edits where the stage is obvious
- Non-stage-related work (e.g., updating global rules)

## References (MUST READ)

| Reference | Path | Why |
|-----------|------|-----|
| Stages | `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md` | Stage purposes, completeness rule |
| Sub-stages | `layer_0/.../layer_stage_system/SUB_STAGES_EXPLAINED.md` | When to use sub-stages |
| Overview | `layer_0/.../layer_stage_system/OVERVIEW.md` | System overview |

**Full path**: `layer_0/layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/layer_stage_system/`

## Protocol

### 1. Identify Current Stage

Ask: "What phase of work am I in?"

| If doing... | Use stage |
|-------------|-----------|
| Gathering requirements | 01_request_gathering |
| Researching solutions | 02_research |
| Defining constraints | 03_instructions |
| Breaking down tasks | 04_planning |
| Designing architecture | 05_design |
| Implementing | 06_development |
| Testing/validating | 07_testing |
| Reviewing/critiquing | 08_criticism |
| Fixing issues | 09_fixing |
| Finalizing deliverable | 10_current_product |
| Archiving old versions | 11_archives |

### 2. Work in outputs/ Folder

All stage content goes in `outputs/`:

```
stage_X_05_design/
└── outputs/
    ├── architecture.md
    ├── diagrams/
    └── decisions.md
```

### 3. Stage Transitions

When moving to next stage:
1. Ensure current stage outputs are complete
2. Create handoff document (optional — use `/handoff-creation`)
3. Move to next stage folder
4. Reference previous stage outputs as needed

### 4. [CRITICAL] Never Skip Stages

All 11 stages must exist, even if empty.

If a stage isn't needed for this work:
- Leave it empty
- Do NOT delete it
- Do NOT skip creating it

## Stage Content Guide

| Stage | Typical Outputs |
|-------|-----------------|
| 01 | requirements.md, questions.md |
| 02 | findings.md, prior_art.md, research_notes.md |
| 03 | constraints.md, guidelines.md |
| 04 | plan.md, tasks.md, breakdown.md |
| 05 | design.md, architecture.md, diagrams/ |
| 06 | code/, drafts/, implementations/ |
| 07 | test_results.md, validation.md |
| 08 | review.md, alternatives.md, trade_offs.md |
| 09 | fixes.md, revisions/, changelog.md |
| 10 | final content (ready for use) |
| 11 | previous_versions/, archive/ |

## Agent Context

Before starting stage work:
1. Find the `.gab.jsonld` for your role in the stage directory
2. Read the matching `.integration.md` (same base name) for mode constraints and allowed transitions
3. Query via jq for precise stage-specific constraints if needed

## Agnostic System

When working in a stage directory:
- If `0AGNOSTIC.md` exists, it is the **source of truth** — edit it, not `CLAUDE.md`
- If `.0agnostic/` exists, check for stage-specific resources
- After modifying `0AGNOSTIC.md`, run `agnostic-sync.sh` to regenerate tool-specific files
- If `.1merge/` exists, it provides tool-specific overrides

## AALang Reference

Stage workflows are managed by the orchestrator's StageStateActor:
`layer_0/layer_0_01_ai_manager_system/personal/layer_0_orchestrator.gab.jsonld`

The StageStateActor tracks current stage (01-11) and stage-specific specialists.

---

*This skill ensures proper stage workflow following STAGES_EXPLAINED.md*
