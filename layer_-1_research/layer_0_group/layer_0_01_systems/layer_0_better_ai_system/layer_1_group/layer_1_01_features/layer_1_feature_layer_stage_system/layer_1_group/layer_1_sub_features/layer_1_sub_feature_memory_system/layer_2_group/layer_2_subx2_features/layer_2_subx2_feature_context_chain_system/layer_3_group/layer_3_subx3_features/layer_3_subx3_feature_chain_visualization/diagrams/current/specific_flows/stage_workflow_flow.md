---
resource_id: "dd3e760e-b549-4122-b92b-1206dcb347a0"
resource_type: "document"
resource_name: "stage_workflow_flow"
---
# Stage Workflow Flow

**Purpose**: Show how context loads when an agent enters a stage (e.g., 05_design, 07_testing).

---

## Current Flow: Stage Entry

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    STAGE WORKFLOW CONTEXT FLOW                                   │
│                    (Entering stage_-1_05_design)                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

    USER: "Let's design the context visualization system"
           or: Agent navigates to stage_-1_05_design/
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 1: Agent has base context (from session start)                      │
    │                                                                           │
    │  Working directory: .../layer_-1_99_stages/                               │
    │  or: .../stage_-1_05_design/                                              │
    │                                                                           │
    │  Already knows from CLAUDE.md chain:                                      │
    │  • Stages are numbered 01-11                                              │
    │  • 05 = design stage                                                      │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 2: Agent reads stage's CLAUDE.md (if exists)                        │
    │                                                                           │
    │  READ: .../stage_-1_05_design/CLAUDE.md                                   │
    │                                                                           │
    │  Finds:                                                                   │
    │  • Stage identity and purpose                                             │
    │  • What this stage is for (architecture decisions)                        │
    │  • References to skills and outputs                                       │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 3: Agent checks for stage-specific skill                            │
    │                                                                           │
    │  LOOK FOR: .../stage_-1_05_design/.claude/skills/05_design-workflow/      │
    │                                                                           │
    │  If exists, READ: SKILL.md                                                │
    │                                                                           │
    │  Finds:                                                                   │
    │  • Design stage procedures                                                │
    │  • Output formats (proposals, diagrams)                                   │
    │  • Quality criteria                                                       │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 4: Agent checks outputs folder structure                            │
    │                                                                           │
    │  READ: .../stage_-1_05_design/outputs/                                    │
    │                                                                           │
    │  Typical structure:                                                       │
    │  └── outputs/                                                             │
    │      ├── proposals/           ← Design proposals go here                  │
    │      ├── diagrams/            ← Architecture diagrams                     │
    │      └── decisions/           ← Design decisions                          │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  STEP 5: Agent works within stage context                                 │
    │                                                                           │
    │  Design work:                                                             │
    │  • Create proposals in outputs/proposals/                                 │
    │  • Create diagrams in outputs/diagrams/                                   │
    │  • Follow skill procedures                                                │
    │  • Use stage-appropriate outputs                                          │
    └───────────────────────────────────────────────────────────────────────────┘
```

---

## Context Chain for Stage Workflow

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    CONTEXT CHAIN: STAGE WORKFLOW                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

    BASE CONTEXT (auto-loaded)
    ══════════════════════════
    │
    │   .../0_layer_universal/CLAUDE.md
    │       │
    │       │ Contains: Stage definitions (01-11)
    │       │           "Use appropriate stages"
    │       ▼
    │   .../layer_-1_99_stages/CLAUDE.md
    │       │
    │       │ Contains: Stages Manager role
    │       │           Children list (00-11)
    │       ▼
    ▼
    STAGE-SPECIFIC CONTEXT (agent reads when entering stage)
    ════════════════════════════════════════════════════════
    │
    │   stage_-1_05_design/CLAUDE.md
    │       │
    │       │ Contains: Stage identity, purpose
    │       │           "For architecture decisions"
    │       ▼
    │   stage_-1_05_design/.claude/skills/05_design-workflow/SKILL.md
    │       │
    │       │ Contains: Design procedures
    │       │           Output formats
    │       │           Quality criteria
    │       ▼
    │   stage_-1_05_design/outputs/ (directory structure)
    │       │
    │       │ Tells agent: Where to put outputs
    │       ▼
    ▼
    AGENT WORKS IN DESIGN STAGE CONTEXT
```

---

## Stage Context Loading Pattern

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  STAGE ENTRY PATTERN                                                             │
└─────────────────────────────────────────────────────────────────────────────────┘

                         ┌─────────────────┐
                         │  Enter Stage    │
                         └────────┬────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
    ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
    │ Stage CLAUDE.md │ │ Stage Skill     │ │ Outputs Folder  │
    │ (identity)      │ │ (procedures)    │ │ (structure)     │
    └────────┬────────┘ └────────┬────────┘ └────────┬────────┘
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │ Agent has stage context │
                    │ Ready to do stage work  │
                    └─────────────────────────┘
```

---

## Stages and Their Contexts

| Stage | Purpose | Key Context Files |
|-------|---------|-------------------|
| 01_request_gathering | Collect requirements | SKILL.md (gathering procedures) |
| 02_research | Explore problem | SKILL.md (research methods) |
| 03_instructions | Define constraints | SKILL.md (instruction formats) |
| 04_planning | Break into tasks | SKILL.md (planning templates) |
| 05_design | Architecture | SKILL.md (proposal formats, diagrams) |
| 06_development | Implementation | SKILL.md (coding standards) |
| 07_testing | Verification | SKILL.md (test procedures) |
| 08_criticism | Review | SKILL.md (review criteria) |
| 09_fixing | Corrections | SKILL.md (fix procedures) |
| 10_current_product | Deliverable | SKILL.md (delivery formats) |
| 11_archives | History | SKILL.md (archival procedures) |

---

## Proposed Improvement: trigger:onStageEnter

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  PROPOSED: Automatic Stage Context Loading                                       │
└─────────────────────────────────────────────────────────────────────────────────┘

Currently: Agent must know to read stage skill manually

Proposed: index.jsonld in stage has trigger:

    {
      "trigger:onStageEnter": {
        "skill": ".claude/skills/05_design-workflow/",
        "loads": ["procedures", "outputFormats"]
      }
    }

Agent reads index.jsonld → automatically loads stage workflow skill
```

---

*Last updated: 2026-02-05*
