---
resource_id: "fb5f1b0a-149a-4d75-af65-ddc4f95196bf"
resource_type: "knowledge"
resource_name: "STAGES_EXPLAINED"
---
# Stages Explained

<!-- section_id: "b8aa1fbd-b02a-45a0-af80-341ab94e13fa" -->
## Overview

Stages represent the **workflow phases** that work passes through. Every entity with stages MUST have all 11 stages.

---

<!-- section_id: "0e25662e-85ea-4ef6-b06e-276d6f3f06bc" -->
## The 11 Stages

| # | Stage | Purpose | Guide |
|---|-------|---------|-------|
| 01 | request_gathering | Transform vague needs into structured, testable requirements (tree of needs) | [Guide](stage_guides/STAGE_01_REQUEST_GATHERING.md) |
| 02 | research | Investigate problem space, produce topic-based findings with evidence | [Guide](stage_guides/STAGE_02_RESEARCH.md) |
| 03 | instructions | Define constraints, guidelines, and non-negotiable rules | [Guide](stage_guides/STAGE_03_INSTRUCTIONS.md) |
| 04 | design | Make architecture decisions, write design specs with rationale | [Guide](stage_guides/STAGE_04_DESIGN.md) |
| 05 | planning | Break design into ordered, actionable tasks with MVP approach | [Guide](stage_guides/STAGE_05_PLANNING.md) |
| 06 | development | Build artifacts following the plan — track status, follow design | [Guide](stage_guides/STAGE_06_DEVELOPMENT.md) |
| 07 | testing | Write and run test scripts, document PASS/FAIL results | [Guide](stage_guides/STAGE_07_TESTING.md) |
| 08 | criticism | Review quality, identify gaps and issues by severity | [Guide](stage_guides/STAGE_08_CRITICISM.md) |
| 09 | fixing | Resolve issues from testing/criticism, document fixes | [Guide](stage_guides/STAGE_09_FIXING.md) |
| 10 | current_product | Hold final validated deliverables ready for use | [Guide](stage_guides/STAGE_10_CURRENT_PRODUCT.md) |
| 11 | archives | Store historical versions and deprecated content | [Guide](stage_guides/STAGE_11_ARCHIVES.md) |

---

<!-- section_id: "5e098536-4df4-428b-8265-94ac16da063c" -->
## Stage Completeness Rule

**[CRITICAL] ALL 11 stages MUST be created when an entity uses stages.**

<!-- section_id: "60e3fbe9-058e-4a39-962b-fa8a834817a3" -->
### Why This Rule Exists

1. **Consistency**: AI agents always know where to put content
2. **Discoverability**: No guessing which stages exist
3. **Workflow tracking**: Clear progression through phases
4. **No skipping**: Empty stages are valid; missing stages are NOT

<!-- section_id: "8c49f1a9-3443-4e72-99ff-a1ea1f737a77" -->
### Required Structure

When creating any entity with stages, create ALL of them:

```
entity_99_stages/
├── stage_XX_01_request_gathering/
│   └── outputs/
├── stage_XX_02_research/
│   └── outputs/
├── stage_XX_03_instructions/
│   └── outputs/
├── stage_XX_04_design/
│   └── outputs/
├── stage_XX_05_planning/
│   └── outputs/
├── stage_XX_06_development/
│   └── outputs/
├── stage_XX_07_testing/
│   └── outputs/
├── stage_XX_08_criticism/
│   └── outputs/
├── stage_XX_09_fixing/
│   └── outputs/
├── stage_XX_10_current_product/
│   └── outputs/
└── stage_XX_11_archives/
    └── outputs/
```

Where `XX` is the layer number (e.g., `stage_0_01_...` for layer_0, `stage_1_01_...` for layer_1).

<!-- section_id: "7bd70cdc-3845-4eed-8f41-f614b45566c7" -->
### Empty vs Missing

| State | Valid? | Example |
|-------|--------|---------|
| Stage exists with content | ✅ Yes | `stage_0_04_design/outputs/design.md` |
| Stage exists but empty | ✅ Yes | `stage_0_03_instructions/outputs/` (empty folder) |
| Stage missing entirely | ❌ NO | Only stages 01, 05, 10 exist |

<!-- section_id: "3e66f8e1-b46f-4bc9-9577-22eb222cfbca" -->
### Enforcement

When creating entities with stages:
1. **Always** create all 11 stage folders
2. **Always** create outputs/ subfolder in each
3. **Never** skip stages you think are "unnecessary"
4. Empty stages stay empty until needed

---

<!-- section_id: "5fedf21b-8cdb-493e-ba39-cee74a12e873" -->
## Stage Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         STAGE WORKFLOW                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  01_request_gathering                                                       │
│       │                                                                     │
│       │ "What do we need?"                                                 │
│       ▼                                                                     │
│  02_research                                                                │
│       │                                                                     │
│       │ "What exists? What's possible?"                                    │
│       ▼                                                                     │
│  03_instructions                                                            │
│       │                                                                     │
│       │ "What are the constraints?"                                        │
│       ▼                                                                     │
│  04_design                                                                  │
│       │                                                                     │
│       │ "What's the architecture?"                                         │
│       ▼                                                                     │
│  05_planning                                                                │
│       │                                                                     │
│       │ "How do we break this down?"                                       │
│       ▼                                                                     │
│  06_development                                                             │
│       │                                                                     │
│       │ "Build it"                                                         │
│       ▼                                                                     │
│  07_testing                                                                 │
│       │                                                                     │
│       │ "Does it work?"                                                    │
│       ▼                                                                     │
│  08_criticism                                                               │
│       │                                                                     │
│       │ "What's wrong? What's better?"                                     │
│       ▼                                                                     │
│  09_fixing                                                                  │
│       │                                                                     │
│       │ "Fix the issues"                                                   │
│       ▼                                                                     │
│  10_current_product                                                         │
│       │                                                                     │
│       │ "Final deliverable"                                                │
│       ▼                                                                     │
│  11_archives                                                                │
│                                                                             │
│       "Historical record"                                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "25e75a0d-2448-468a-a7b2-80fcaf318107" -->
## Stage Naming Convention

```
stage_{layer}_{number}_{name}/
```

Examples:
- `stage_0_01_request_gathering/` - Layer 0, stage 01
- `stage_1_04_design/` - Layer 1, stage 04
- `stage_-1_02_research/` - Layer -1 (research), stage 02

---

<!-- section_id: "782b8ddc-fc07-424e-af80-17caa5405967" -->
## Stage Contents

Each stage folder contains:

```
stage_X_NN_name/
├── CLAUDE.md              ← Optional: stage-specific context
├── outputs/               ← REQUIRED: stage outputs
│   └── (content files)
└── hand_off_documents/    ← Optional: stage transitions
    ├── incoming/
    └── outgoing/
```

---

<!-- section_id: "df00a588-e400-4f7f-8bcf-7ac1ede1e011" -->
## See Also

- [SUB_STAGES_EXPLAINED.md](SUB_STAGES_EXPLAINED.md) - Sub-stages within stages
- [OVERVIEW.md](OVERVIEW.md) - Layer-stage system overview
- [LAYERS_EXPLAINED.md](LAYERS_EXPLAINED.md) - Layers (scope)

---

*This document is the source of truth for stage structure and the Stage Completeness Rule.*
