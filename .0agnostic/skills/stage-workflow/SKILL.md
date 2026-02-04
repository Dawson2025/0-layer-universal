# Skill: Stage Workflow

## Purpose

Work through stages properly, understanding what content belongs in each stage.

## When to Use

- Starting work on a new feature/project
- Moving content between stages
- Determining which stage to work in
- Creating stage outputs

## References (MUST READ)

| Reference | Path | Why |
|-----------|------|-----|
| Stages | `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md` | Stage purposes, completeness rule |
| Sub-stages | `layer_0/.../layer_stage_system/SUB_STAGES_EXPLAINED.md` | When to use sub-stages |
| Overview | `layer_0/.../layer_stage_system/OVERVIEW.md` | System overview |

**Full path**: `layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/layer_stage_system/`

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
2. Create handoff document (optional)
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

---

*This skill ensures proper stage workflow following STAGES_EXPLAINED.md*
