# Stages Explained

## Overview

Stages represent the **workflow phases** that work passes through. Every entity with stages MUST have all 11 stages.

---

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

## Stage Completeness Rule

**[CRITICAL] ALL 11 stages MUST be created when an entity uses stages.**

### Why This Rule Exists

1. **Consistency**: AI agents always know where to put content
2. **Discoverability**: No guessing which stages exist
3. **Workflow tracking**: Clear progression through phases
4. **No skipping**: Empty stages are valid; missing stages are NOT

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
├── stage_XX_04_planning/
│   └── outputs/
├── stage_XX_05_design/
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

### Empty vs Missing

| State | Valid? | Example |
|-------|--------|---------|
| Stage exists with content | ✅ Yes | `stage_0_05_design/outputs/design.md` |
| Stage exists but empty | ✅ Yes | `stage_0_03_instructions/outputs/` (empty folder) |
| Stage missing entirely | ❌ NO | Only stages 01, 05, 10 exist |

### Enforcement

When creating entities with stages:
1. **Always** create all 11 stage folders
2. **Always** create outputs/ subfolder in each
3. **Never** skip stages you think are "unnecessary"
4. Empty stages stay empty until needed

---

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
│  04_planning                                                                │
│       │                                                                     │
│       │ "How do we break this down?"                                       │
│       ▼                                                                     │
│  05_design                                                                  │
│       │                                                                     │
│       │ "What's the architecture?"                                         │
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

## Stage Naming Convention

```
stage_{layer}_{number}_{name}/
```

Examples:
- `stage_0_01_request_gathering/` - Layer 0, stage 01
- `stage_1_05_design/` - Layer 1, stage 05
- `stage_-1_02_research/` - Layer -1 (research), stage 02

---

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

## See Also

- [SUB_STAGES_EXPLAINED.md](SUB_STAGES_EXPLAINED.md) - Sub-stages within stages
- [OVERVIEW.md](OVERVIEW.md) - Layer-stage system overview
- [LAYERS_EXPLAINED.md](LAYERS_EXPLAINED.md) - Layers (scope)

---

*This document is the source of truth for stage structure and the Stage Completeness Rule.*
