---
resource_id: "33bde27b-a7a5-46ad-bcb3-d9ea37e5662a"
resource_type: "skill_document"
resource_name: "SKILL"
---
# Skill: Stage Workflow

<!-- section_id: "3cb9c2c1-4a96-4eac-acdc-cd820b0cab8d" -->
## Purpose

Work through stages properly, understanding what content belongs in each stage.

<!-- section_id: "93edf965-4fed-4ac9-8fdc-f2bdc8fddf25" -->
## When to Use

- Starting work on a new feature/project
- Moving content between stages
- Determining which stage to work in
- Creating stage outputs

<!-- section_id: "849670ff-b65c-4924-a7c2-28211e9b4dd7" -->
## References (MUST READ)

| Reference | Path | Why |
|-----------|------|-----|
| Stages | `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md` | Stage purposes, completeness rule |
| Sub-stages | `layer_0/.../layer_stage_system/SUB_STAGES_EXPLAINED.md` | When to use sub-stages |
| Overview | `layer_0/.../layer_stage_system/OVERVIEW.md` | System overview |

**Full path**: `layer_0/layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/layer_stage_system/`

<!-- section_id: "5ad89fff-e84e-4077-829c-aa6155e80b90" -->
## Protocol

<!-- section_id: "94d44ef8-f89a-46cb-b2c0-0970dc44254f" -->
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

<!-- section_id: "335335ce-8280-4056-98cc-5f83c4c50275" -->
### 2. Work in outputs/ Folder

All stage content goes in `outputs/`:

```
stage_X_05_design/
└── outputs/
    ├── architecture.md
    ├── diagrams/
    └── decisions.md
```

<!-- section_id: "35f6c635-afc8-452b-b647-12eaee9ebc8c" -->
### 3. Stage Transitions

When moving to next stage:
1. Ensure current stage outputs are complete
2. Create handoff document (optional)
3. Move to next stage folder
4. Reference previous stage outputs as needed

<!-- section_id: "cef81e0b-368f-4ca2-b847-179217470884" -->
### 4. [CRITICAL] Never Skip Stages

All 11 stages must exist, even if empty.

If a stage isn't needed for this work:
- Leave it empty
- Do NOT delete it
- Do NOT skip creating it

<!-- section_id: "1c719a2f-9b5e-4e0f-b5f2-247166ef4bea" -->
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
