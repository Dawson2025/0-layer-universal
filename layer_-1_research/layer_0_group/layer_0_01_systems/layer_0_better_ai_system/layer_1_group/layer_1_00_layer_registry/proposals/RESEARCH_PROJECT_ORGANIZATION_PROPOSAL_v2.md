---
resource_id: "cd16bd7d-12bd-46a6-a58a-44f059303bcc"
resource_type: "document"
resource_name: "RESEARCH_PROJECT_ORGANIZATION_PROPOSAL_v2"
---
# Proposal v2: Research Project Organization (With Proper Stages)

<!-- section_id: "6ef3d9ce-0442-49e8-a889-d0ba0884c5d9" -->
## Key Correction

Research content must use the **stage system** (01-11), not ad-hoc folders like `proposal/`, `design/`, `decisions/`.

---

<!-- section_id: "9dc0bc20-c175-4671-9299-f7f25791349d" -->
## Proper Stage Mapping

| Stage | Purpose | Research Content |
|-------|---------|------------------|
| 01_request_gathering | Clarify requirements | What problem are we solving? |
| 02_research | Explore, gather info | Background research, prior art |
| 03_instructions | Define constraints | Rules/constraints for the solution |
| 04_planning | Break into subtasks | Implementation plan |
| 05_design | Architecture/design | Design docs, diagrams |
| 06_development | Implementation | Draft content, prototypes |
| 07_testing | Verification | Review, validation |
| 08_criticism | Review and analysis | Alternatives considered, trade-offs |
| 09_fixing | Corrections | Revisions based on feedback |
| 10_current_product | Final deliverable | Ready for production |
| 11_archives | Historical records | Previous versions |

---

<!-- section_id: "e44f8387-098d-4f02-8905-adc047ef834a" -->
## Revised Structure

```
layer_-1_better_ai_system/
├── CLAUDE.md
├── 0INDEX.md
│
├── layer_-1_group/                              ← Project internals (META)
│   ├── layer_-1_00_layer_registry/
│   │   └── proposals/                           ← Project-level proposals
│   ├── layer_-1_03_sub_layers/
│   └── layer_-1_99_stages/                      ← PROJECT's own stages
│       ├── stage_-1_01_request_gathering/
│       ├── stage_-1_02_research/
│       └── ...
│
└── research_targets/                            ← Research ABOUT other layers
    │
    └── target_layer_0/                          ← Research targeting layer_0
        ├── CLAUDE.md
        ├── 0INDEX.md
        │
        ├── target_0_99_stages/                  ← Stages for layer_0 research overall
        │   └── (if needed for cross-feature work)
        │
        └── features/                            ← Individual features being researched
            │
            ├── feature_layer_stage_system/
            │   ├── CLAUDE.md
            │   ├── STATUS.md                    ← draft|review|approved|graduated
            │   │
            │   └── feature_99_stages/           ← THIS FEATURE'S stages
            │       │
            │       ├── stage_01_request_gathering/
            │       │   └── outputs/
            │       │       └── requirements.md
            │       │
            │       ├── stage_02_research/
            │       │   └── outputs/
            │       │       ├── prior_art.md
            │       │       └── existing_patterns.md
            │       │
            │       ├── stage_05_design/
            │       │   └── outputs/
            │       │       ├── SUB_LAYERS_DESIGN.md
            │       │       ├── SUB_STAGES_DESIGN.md
            │       │       └── NESTED_DEPTH_DESIGN.md
            │       │
            │       ├── stage_08_criticism/
            │       │   └── outputs/
            │       │       ├── alternatives_considered.md
            │       │       └── trade_offs.md
            │       │
            │       └── stage_10_current_product/
            │           └── outputs/             ← READY FOR PRODUCTION
            │               ├── SUB_LAYERS_AS_ENTRY_POINTS.md
            │               ├── NESTED_DEPTH_NAMING.md
            │               └── SUB_STAGES_EXPLAINED.md
            │
            ├── feature_agent_coordination/
            │   ├── CLAUDE.md
            │   ├── STATUS.md
            │   │
            │   └── feature_99_stages/
            │       ├── stage_01_request_gathering/
            │       ├── stage_02_research/
            │       ├── stage_05_design/
            │       │   └── outputs/
            │       │       ├── SCOPE_VS_DELEGATION_DESIGN.md
            │       │       ├── HANDOFF_DESIGN.md
            │       │       └── MULTI_AGENT_DESIGN.md
            │       ├── stage_08_criticism/
            │       └── stage_10_current_product/
            │           └── outputs/
            │               ├── SCOPE_VS_DELEGATION.md
            │               ├── HANDOFF_PROTOCOLS.md
            │               └── MULTI_AGENT_PATTERNS.md
            │
            ├── feature_ai_context_flow/
            └── ...
```

---

<!-- section_id: "14b7d313-db1b-4e08-a4be-7e3b7b1af3c4" -->
## AI Agent Context Flow (With Stages)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              RESEARCH PROJECT CONTEXT CASCADE (WITH STAGES)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Entry: layer_-1_better_ai_system/CLAUDE.md                                │
│       │                                                                     │
│       ├── Working on project meta (proposals about the project itself)?    │
│       │       │                                                             │
│       │       ▼                                                             │
│       │   layer_-1_group/layer_-1_99_stages/                               │
│       │   stage_-1_02_research/ or stage_-1_05_design/                     │
│       │                                                                     │
│       └── Working on a research FEATURE?                                   │
│               │                                                             │
│               ▼                                                             │
│       research_targets/target_layer_0/features/feature_X/CLAUDE.md         │
│               │                                                             │
│               │ What stage of work?                                        │
│               │                                                             │
│               ├── Gathering requirements?                                  │
│               │   └── feature_99_stages/stage_01_request_gathering/        │
│               │                                                             │
│               ├── Researching?                                             │
│               │   └── feature_99_stages/stage_02_research/                 │
│               │                                                             │
│               ├── Designing?                                               │
│               │   └── feature_99_stages/stage_05_design/                   │
│               │                                                             │
│               ├── Reviewing/critiquing?                                    │
│               │   └── feature_99_stages/stage_08_criticism/                │
│               │                                                             │
│               └── Finalizing for production?                               │
│                   └── feature_99_stages/stage_10_current_product/          │
│                                                                             │
│  HANDOFF TO PRODUCTION:                                                     │
│  stage_10_current_product/outputs/  ──────▶  layer_0/.../                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "785e9782-debd-4bd9-ae04-2823ffffecca" -->
## Feature Workflow (Using Stages)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FEATURE WORKFLOW THROUGH STAGES                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. stage_01_request_gathering/                                            │
│     └── "What problem are we solving?"                                     │
│     └── outputs/requirements.md                                            │
│                                                                             │
│  2. stage_02_research/                                                     │
│     └── "What exists? What patterns? What prior art?"                      │
│     └── outputs/research_findings.md                                       │
│                                                                             │
│  3. stage_05_design/                                                       │
│     └── "How should we solve it?"                                          │
│     └── outputs/DESIGN_DOCS.md                                             │
│                                                                             │
│  4. stage_08_criticism/                                                    │
│     └── "What are the trade-offs? What alternatives?"                      │
│     └── outputs/alternatives.md, trade_offs.md                             │
│                                                                             │
│  5. stage_10_current_product/                                              │
│     └── "Final content ready for production"                               │
│     └── outputs/ ← THESE FILES GET COPIED TO PRODUCTION                    │
│                                                                             │
│  6. UPDATE STATUS.md → "graduated"                                         │
│                                                                             │
│  7. COPY to production:                                                    │
│     stage_10_current_product/outputs/X.md                                  │
│         │                                                                   │
│         ▼                                                                   │
│     layer_0/layer_0_03_sub_layers/.../X.md                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "8825663a-06ba-47a5-bdc9-4093fcf365c3" -->
## What We Just Created → Proper Stage Locations

The docs we created today should be organized as:

```
research_targets/target_layer_0/features/

├── feature_layer_stage_system/
│   ├── STATUS.md                          → graduated
│   └── feature_99_stages/
│       ├── stage_05_design/
│       │   └── outputs/
│       │       ├── why_sub_layers_as_entry_points.md
│       │       ├── why_nested_depth_naming.md
│       │       └── why_sub_stages.md
│       └── stage_10_current_product/
│           └── outputs/
│               ├── SUB_LAYERS_AS_ENTRY_POINTS.md    ← copied to production
│               ├── NESTED_DEPTH_NAMING.md           ← copied to production
│               └── SUB_STAGES_EXPLAINED.md          ← copied to production

├── feature_agent_coordination/
│   ├── STATUS.md                          → graduated
│   └── feature_99_stages/
│       ├── stage_05_design/
│       │   └── outputs/
│       │       ├── why_scope_vs_delegation.md
│       │       ├── why_handoff_protocols.md
│       │       └── why_multi_agent_patterns.md
│       └── stage_10_current_product/
│           └── outputs/
│               ├── SCOPE_VS_DELEGATION.md           ← copied to production
│               ├── HANDOFF_PROTOCOLS.md             ← copied to production
│               └── MULTI_AGENT_PATTERNS.md          ← copied to production

└── feature_ai_context_flow/
    ├── STATUS.md                          → graduated
    └── feature_99_stages/
        ├── stage_05_design/
        └── stage_10_current_product/
            └── outputs/
                └── AI_CONTEXT_PROPOSAL_REQUIREMENTS.md  ← copied to production
```

---

<!-- section_id: "1ee7f3a5-2ca0-4cd5-8fe1-7aeb702a75be" -->
## Summary of Changes

| Before (Wrong) | After (Correct) |
|----------------|-----------------|
| `feature_X/proposal/` | `feature_X/feature_99_stages/stage_01_request_gathering/outputs/` |
| `feature_X/design/` | `feature_X/feature_99_stages/stage_05_design/outputs/` |
| `feature_X/decisions/` | `feature_X/feature_99_stages/stage_08_criticism/outputs/` |
| `feature_X/alternatives/` | `feature_X/feature_99_stages/stage_08_criticism/outputs/` |
| `feature_X/ready_for_production/` | `feature_X/feature_99_stages/stage_10_current_product/outputs/` |

---

<!-- section_id: "009c57e4-56c4-42e1-a1e6-e1f926d0a4e2" -->
## Decision Request

1. **Approve this structure?** (Features have their own `feature_99_stages/`)
2. **Should I reorganize the existing research project?**
3. **Should I backfill the design docs for what we just created?**

