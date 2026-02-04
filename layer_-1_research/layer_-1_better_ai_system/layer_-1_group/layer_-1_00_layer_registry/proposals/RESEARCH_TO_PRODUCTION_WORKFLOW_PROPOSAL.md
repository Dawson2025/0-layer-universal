# Proposal: Research-to-Production Workflow

## Problem Statement

We just created documentation directly in production `layer_0/`:
- `layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md`
- `layer_stage_system/NESTED_DEPTH_NAMING.md`
- `layer_stage_system/SUB_STAGES_EXPLAINED.md`
- `agent_coordination/SCOPE_VS_DELEGATION.md`
- `agent_coordination/HANDOFF_PROTOCOLS.md`
- `agent_coordination/MULTI_AGENT_PATTERNS.md`
- `sub_layer_0_04_rules/AI_CONTEXT_PROPOSAL_REQUIREMENTS.md`

**Question**: Should this content have gone through the research project first? How should research and production relate?

---

## Option A: Research-First Workflow

**All new content goes through research before production.**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESEARCH-FIRST WORKFLOW                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. NEW IDEA                                                                │
│     │                                                                       │
│     ▼                                                                       │
│  layer_-1_better_ai_system/                                                │
│  research_targets/target_layer_0/features/feature_X/                       │
│     │                                                                       │
│     │ research, design, iterate                                            │
│     ▼                                                                       │
│  2. DRAFT → REVIEW → APPROVED                                              │
│     │                                                                       │
│     │ user approves                                                        │
│     ▼                                                                       │
│  3. ready_for_production/ populated                                        │
│     │                                                                       │
│     │ merge/copy to production                                             │
│     ▼                                                                       │
│  4. layer_0/layer_0_03_sub_layers/...                                      │
│     │                                                                       │
│     │ archive research                                                     │
│     ▼                                                                       │
│  5. graduated/feature_X/                                                   │
│                                                                             │
│  PROS:                                                                      │
│  - All changes reviewed before production                                  │
│  - Clear history of what was proposed vs accepted                          │
│  - Research project is the "staging area"                                  │
│                                                                             │
│  CONS:                                                                      │
│  - Slower for small documentation additions                                │
│  - Duplicates content temporarily                                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Option B: Size-Based Workflow

**Small changes go direct, large changes go through research.**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SIZE-BASED WORKFLOW                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  NEW CHANGE                                                                 │
│     │                                                                       │
│     ├── Small (1-2 files, no architectural impact)?                        │
│     │       │                                                               │
│     │       ▼                                                               │
│     │   DIRECT TO PRODUCTION                                               │
│     │   layer_0/layer_0_03_sub_layers/...                                  │
│     │                                                                       │
│     └── Large (3+ files, architectural change)?                            │
│             │                                                               │
│             ▼                                                               │
│         RESEARCH FIRST                                                     │
│         layer_-1_better_ai_system/research_targets/...                     │
│             │                                                               │
│             ▼                                                               │
│         (review, approve, graduate)                                        │
│                                                                             │
│  PROS:                                                                      │
│  - Fast for small fixes/additions                                          │
│  - Rigorous for big changes                                                │
│                                                                             │
│  CONS:                                                                      │
│  - Judgment call on "small" vs "large"                                     │
│  - May miss documenting the rationale for small changes                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Option C: Research as Design Doc (RECOMMENDED)

**Research contains PROPOSALS and DESIGNS. Production contains FINAL content. Research mirrors production structure.**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESEARCH AS DESIGN DOC                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  RESEARCH PROJECT (layer_-1_better_ai_system)                              │
│  ├── Contains: Proposals, designs, rationale, alternatives considered      │
│  ├── Structure: Mirrors production for easy reference                      │
│  └── Purpose: "Why we built it this way"                                   │
│                                                                             │
│  PRODUCTION (layer_0, layer_1)                                             │
│  ├── Contains: Final documentation, actual system                          │
│  ├── Structure: The real thing                                             │
│  └── Purpose: "How it works"                                               │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │  Research Project                     Production                    │   │
│  │  (layer_-1_better_ai_system)         (layer_0)                     │   │
│  │                                                                     │   │
│  │  research_targets/                    layer_0/                      │   │
│  │  └── target_layer_0/                  └── layer_0_03_sub_layers/   │   │
│  │      └── features/                        └── sub_layer_0_02_.../  │   │
│  │          └── feature_agent_coord/             └── agent_coord/     │   │
│  │              ├── proposal.md      ←──────────────┐                 │   │
│  │              ├── design.md        ←──────────────┤ references      │   │
│  │              ├── alternatives.md  ←──────────────┤                 │   │
│  │              └── decisions.md     ←──────────────┘                 │   │
│  │                                                                     │   │
│  │  "Why we did it"                      "What it is"                 │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  WORKFLOW:                                                                  │
│  1. For new features: Write proposal in research FIRST                     │
│  2. Get approval                                                           │
│  3. Implement in production                                                │
│  4. Research keeps the "design doc" permanently (not archived)             │
│                                                                             │
│  PROS:                                                                      │
│  - Research = permanent design documentation                               │
│  - Production stays clean (just "how it works")                            │
│  - Easy to find "why was this built this way?"                             │
│  - No duplication of final content                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Recommended Structure for Research Project

If we adopt Option C, here's how the research project should be organized:

```
layer_-1_better_ai_system/
├── CLAUDE.md
├── 0INDEX.md
│
├── layer_-1_group/                          ← Project internals
│   ├── layer_-1_00_layer_registry/
│   │   └── proposals/                       ← Project-level proposals
│   ├── layer_-1_03_sub_layers/
│   └── layer_-1_99_stages/
│
├── research_targets/
│   │
│   └── target_layer_0/                      ← Research targeting layer_0
│       ├── CLAUDE.md
│       ├── 0INDEX.md
│       │
│       ├── features/                        ← Features (groups of changes)
│       │   │
│       │   ├── feature_layer_stage_system/  ← Mirrors production topic
│       │   │   ├── CLAUDE.md
│       │   │   ├── STATUS.md                ← active|complete
│       │   │   ├── proposal/
│       │   │   │   └── PROPOSAL.md          ← Why build this
│       │   │   ├── design/
│       │   │   │   ├── SUB_LAYERS_DESIGN.md
│       │   │   │   ├── SUB_STAGES_DESIGN.md
│       │   │   │   └── NESTED_DEPTH_DESIGN.md
│       │   │   ├── decisions/
│       │   │   │   └── NAMING_DECISIONS.md  ← Why subxN not subN
│       │   │   └── alternatives/
│       │   │       └── REJECTED_APPROACHES.md
│       │   │
│       │   ├── feature_agent_coordination/  ← Mirrors production topic
│       │   │   ├── proposal/
│       │   │   ├── design/
│       │   │   │   ├── SCOPE_VS_DELEGATION_DESIGN.md
│       │   │   │   ├── HANDOFF_DESIGN.md
│       │   │   │   └── MULTI_AGENT_DESIGN.md
│       │   │   └── decisions/
│       │   │
│       │   ├── feature_ai_context_flow/
│       │   ├── feature_rules_system/
│       │   └── ...
│       │
│       └── reference_impl/                  ← Examples, prototypes
│
└── synthesis/                               ← Cross-feature insights
    └── LESSONS_LEARNED.md
```

---

## Mapping: What We Just Created → Research Location

| Production Location | Research Location | Content Type |
|---------------------|-------------------|--------------|
| `layer_0/.../layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md` | `feature_layer_stage_system/design/SUB_LAYERS_DESIGN.md` | Design rationale |
| `layer_0/.../layer_stage_system/NESTED_DEPTH_NAMING.md` | `feature_layer_stage_system/design/NESTED_DEPTH_DESIGN.md` | Design rationale |
| `layer_0/.../layer_stage_system/SUB_STAGES_EXPLAINED.md` | `feature_layer_stage_system/design/SUB_STAGES_DESIGN.md` | Design rationale |
| `layer_0/.../agent_coordination/SCOPE_VS_DELEGATION.md` | `feature_agent_coordination/design/SCOPE_VS_DELEGATION_DESIGN.md` | Design rationale |
| `layer_0/.../agent_coordination/HANDOFF_PROTOCOLS.md` | `feature_agent_coordination/design/HANDOFF_DESIGN.md` | Design rationale |
| `layer_0/.../agent_coordination/MULTI_AGENT_PATTERNS.md` | `feature_agent_coordination/design/MULTI_AGENT_DESIGN.md` | Design rationale |
| `layer_0/.../sub_layer_0_04_rules/AI_CONTEXT_PROPOSAL_REQUIREMENTS.md` | `feature_ai_context_flow/design/PROPOSAL_REQUIREMENTS_DESIGN.md` | Design rationale |

**Note**: The research versions would contain:
- WHY we designed it this way
- Alternatives we considered
- Decisions we made and why
- Links to the production versions

The production versions contain:
- HOW it works (the actual documentation)

---

## Action Plan

**Option 1: Retroactive Documentation (Minimal)**
- Create research feature folders
- Add brief design docs that link to production
- Document the rationale after the fact

**Option 2: Full Backfill (Thorough)**
- Create complete design docs in research
- Extract rationale from the production docs
- Add alternatives/decisions documentation

**Option 3: Going Forward Only**
- Leave existing production docs as-is
- Apply research-first workflow to future changes
- Gradually backfill as we revisit topics

---

## Recommendation

I recommend **Option C (Research as Design Doc)** with **Action Plan Option 3 (Going Forward Only)**.

This means:
1. Reorganize the research project structure (per previous proposal)
2. For the docs we just created, add lightweight design docs that link to production
3. Future changes follow research-first workflow
4. Research becomes the permanent "why" documentation

---

## Decision Request

1. **Do you approve Option C workflow?** (Research = design docs, Production = final docs)
2. **Which action plan for existing content?** (Minimal backfill, full backfill, or going forward only)
3. **Should I proceed with both reorganization proposals?**

