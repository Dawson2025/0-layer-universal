---
resource_id: "f49ac7b6-e801-47cf-a439-954445e40723"
resource_type: "document"
resource_name: "RESEARCH_PROJECT_ORGANIZATION_PROPOSAL"
---
# Proposal: Research Project Organization

## Problem Statement

The current organization of `layer_-1_better_ai_system` has structural issues:

1. **Naming Confusion**: `layer_0_group/` contains research ABOUT layer_0 improvements, but the internal structure mirrors production layer_0, making it look like a duplicate
2. **Unclear Status**: Features like `layer_0_feature_better_layer_stage_system` don't clearly indicate they're proposals/drafts vs production-ready
3. **Missing Handoff Path**: No clear mechanism to graduate research to production
4. **Agent Entry Point Confusion**: AI agents may confuse research layer_0_group with production layer_0

---

## Current Structure (BEFORE)

```
layer_-1_better_ai_system/                    ← Research project root
├── CLAUDE.md                                 ← Entry point
├── 0AGNOSTIC.md                              ← Identity source
├── 0INDEX.md                                 ← Navigation
│
├── layer_-1_group/                           ← "This layer's internals"
│   ├── layer_-1_00_layer_registry/           ← Registration
│   │   └── proposals/                        ← Proposals for this project
│   ├── layer_-1_03_sub_layers/               ← Sub-layers
│   └── layer_-1_99_stages/                   ← Research workflow
│       ├── stage_-1_01_request_gathering/
│       ├── stage_-1_02_research/
│       ├── stage_-1_04_design/
│       └── ...
│
└── layer_0_group/                            ← "Children" (CONFUSING NAME)
    ├── layer_0_00_layer_registry/            ← Mirrors production
    ├── layer_0_03_sub_layers/                ← Mirrors production
    └── layer_0_features/                     ← 8 research features
        ├── layer_0_feature_ai_automation_system/
        ├── layer_0_feature_ai_context_system/
        ├── layer_0_feature_ai_documentation_system/
        ├── layer_0_feature_ai_dynamic_memory_system/
        ├── layer_0_feature_ai_manager_hierarchy_system/
        ├── layer_0_feature_ai_rules_system/
        ├── layer_0_feature_better_layer_stage_system/
        └── layer_0_feature_better_setup_system/
```

**Issues:**
- `layer_0_group/` is NOT production layer_0 but looks like it
- Features have `layer_0_feature_` prefix but are research, not production
- No clear handoff path to production `layer_0/`
- AI agents traversing from research may think they're in production

---

## Proposed Structure (AFTER)

```
layer_-1_better_ai_system/                    ← Research project root
├── CLAUDE.md                                 ← Entry point
├── 0AGNOSTIC.md                              ← Identity source
├── 0INDEX.md                                 ← Navigation
│
├── layer_-1_group/                           ← "This layer's internals" (UNCHANGED)
│   ├── layer_-1_00_layer_registry/
│   ├── layer_-1_03_sub_layers/
│   └── layer_-1_99_stages/
│
├── research_targets/                         ← RENAMED from layer_0_group
│   │
│   ├── target_layer_0/                       ← Research targeting production layer_0
│   │   ├── CLAUDE.md                         ← Agent entry point
│   │   ├── 0INDEX.md                         ← Index of features
│   │   ├── STATUS.md                         ← Overall status
│   │   │
│   │   ├── features/                         ← Research features (RENAMED)
│   │   │   ├── feature_ai_automation_system/
│   │   │   │   ├── CLAUDE.md                 ← Agent entry point
│   │   │   │   ├── STATUS.md                 ← draft|review|approved|graduated
│   │   │   │   ├── proposal/                 ← Proposals
│   │   │   │   ├── research/                 ← Research outputs
│   │   │   │   ├── design/                   ← Design outputs
│   │   │   │   └── ready_for_production/     ← Handoff content
│   │   │   │
│   │   │   ├── feature_ai_context_system/
│   │   │   ├── feature_better_layer_stage_system/
│   │   │   └── ...
│   │   │
│   │   └── reference_impl/                   ← Reference implementations
│   │       └── (drafts of what production might look like)
│   │
│   └── target_layer_1/                       ← Research targeting layer_1 (if needed)
│       └── ...
│
├── graduated/                                ← Archive of graduated features
│   └── (features moved here after merging to production)
│
└── synthesis/                                ← Cross-feature insights
    └── (combined learnings)
```

---

## Key Changes

| Before | After | Reason |
|--------|-------|--------|
| `layer_0_group/` | `research_targets/target_layer_0/` | Clearly indicates this targets layer_0, not IS layer_0 |
| `layer_0_features/` | `features/` | Remove redundant `layer_0_` prefix |
| `layer_0_feature_X/` | `feature_X/` | Shorter, clearer naming |
| (none) | `STATUS.md` in each feature | Track draft→review→approved→graduated |
| (none) | `ready_for_production/` | Clear handoff folder |
| (none) | `graduated/` | Archive graduated features |
| `synthesis/` (empty) | `synthesis/` (used) | Cross-feature insights |

---

## AI Agent Context Flow (How Agents Work With This)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESEARCH PROJECT CONTEXT CASCADE                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Entry Point: layer_-1_better_ai_system/CLAUDE.md                          │
│       │                                                                     │
│       │ identifies                                                          │
│       ▼                                                                     │
│  Role: Research Project Manager                                             │
│  Scope: Research, design, planning (NOT production)                        │
│       │                                                                     │
│       ├── Working on project internals?                                    │
│       │       │                                                             │
│       │       ▼                                                             │
│       │   layer_-1_group/CLAUDE.md                                         │
│       │   (stages, sub-layers, proposals)                                  │
│       │                                                                     │
│       └── Working on a research feature?                                   │
│               │                                                             │
│               ▼                                                             │
│       research_targets/target_layer_0/CLAUDE.md                            │
│       (targeting production layer_0)                                       │
│               │                                                             │
│               ▼                                                             │
│       features/feature_X/CLAUDE.md                                         │
│       (specific feature being researched)                                  │
│                                                                             │
│  CRITICAL RULES INHERITED:                                                  │
│  - All layer_0 universal rules (from production)                           │
│  - Research-specific rules (proposals need diagrams, etc.)                 │
│  - This project's rules                                                     │
│                                                                             │
│  CLEAR SEPARATION:                                                          │
│  - research_targets/ = RESEARCH (proposals, drafts)                        │
│  - ../../../layer_0/ = PRODUCTION (actual system)                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Feature Lifecycle (Handoff to Production)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FEATURE LIFECYCLE                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. DRAFT                                                                   │
│     └── Status: draft                                                       │
│     └── Location: features/feature_X/                                      │
│     └── Work: proposal/, research/, design/                                │
│                                                                             │
│  2. REVIEW                                                                  │
│     └── Status: review                                                      │
│     └── Location: Same, but STATUS.md updated                              │
│     └── Work: User reviewing, providing feedback                           │
│                                                                             │
│  3. APPROVED                                                                │
│     └── Status: approved                                                    │
│     └── Location: ready_for_production/ populated                          │
│     └── Work: Finalized content ready for merge                            │
│                                                                             │
│  4. GRADUATED                                                               │
│     └── Status: graduated                                                   │
│     └── Location: Moved to graduated/                                      │
│     └── Work: Merged to production layer_0/ (or layer_1/)                  │
│                                                                             │
│  Handoff Process:                                                           │
│  ┌──────────────────┐        ┌──────────────────────────────┐              │
│  │ ready_for_       │        │ Production                   │              │
│  │ production/      │───────▶│ layer_0/layer_0_03_sub_layers│              │
│  │ (research)       │  merge │ (actual system)              │              │
│  └──────────────────┘        └──────────────────────────────┘              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## STATUS.md Template (For Each Feature)

```markdown
# Feature Status: [feature_name]

## Current Status: [draft|review|approved|graduated]

## Target
- **Production Location**: `layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/...`
- **Scope**: [what this feature adds/changes]

## Progress
- [ ] Proposal written
- [ ] Research complete
- [ ] Design complete
- [ ] User approved
- [ ] Ready for production populated
- [ ] Merged to production
- [ ] Moved to graduated/

## Handoff Checklist
- [ ] All files in ready_for_production/ are final
- [ ] No research-specific content (remove TODOs, drafts)
- [ ] File paths adjusted for production location
- [ ] CLAUDE.md integration documented

## History
| Date | Status | Notes |
|------|--------|-------|
| YYYY-MM-DD | draft | Initial creation |
```

---

## Implementation Steps

1. **Rename `layer_0_group/` to `research_targets/target_layer_0/`**
2. **Rename `layer_0_features/` to `features/`**
3. **Remove `layer_0_` prefix from all feature folders**
4. **Add `STATUS.md` to each feature**
5. **Add `ready_for_production/` folder to each feature**
6. **Create `graduated/` folder at project root**
7. **Update all CLAUDE.md files** to reflect new paths
8. **Update 0INDEX.md** with new structure

---

## Migration Commands (Draft)

```bash
# Base path
BASE="/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system"

# 1. Rename layer_0_group to research_targets/target_layer_0
mkdir -p "$BASE/research_targets"
mv "$BASE/layer_0_group" "$BASE/research_targets/target_layer_0"

# 2. Rename layer_0_features to features
mv "$BASE/research_targets/target_layer_0/layer_0_features" "$BASE/research_targets/target_layer_0/features"

# 3. Remove layer_0_ prefix from features
cd "$BASE/research_targets/target_layer_0/features"
for dir in layer_0_feature_*; do
  newname="${dir#layer_0_}"
  mv "$dir" "$newname"
done

# 4. Create graduated folder
mkdir -p "$BASE/graduated"

# 5. Add STATUS.md and ready_for_production/ to each feature
# (done via script or manually)
```

---

## Decision Request

**Do you approve this reorganization?**

If approved, I will:
1. Execute the migration
2. Update all CLAUDE.md and 0INDEX.md files
3. Create STATUS.md for each feature
4. Commit with `[AI Context] Reorganize better_ai_system research project`

---

*This proposal follows AI_CONTEXT_PROPOSAL_REQUIREMENTS.md by including before/after diagrams and agent workflow diagrams.*
