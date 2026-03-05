---
resource_id: "eb35160d-e84a-4076-a0d4-341bb285356b"
resource_type: "document"
resource_name: "proposal_cleanup_and_staged_proposals_v1"
---
# Proposal: Cleanup & Staged Proposals System v1

**Status**: Implemented
**Created**: 2026-02-03
**Implemented**: 2026-02-03
**Scope**: Cleanup misnamed directories, relocate orphaned content, add proposal staging, add _hierarchy naming convention

---

## Problem Statement

### 1. Naming Inconsistencies
Directories named `*_content` should follow the `*_group` convention per v6:
```
WRONG:  sub_layer_-1_05_content
RIGHT:  sub_layer_-1_05_group
```

### 2. Orphaned Folders in Universal Layer
These folders exist at `layer_0/sub_layer_0_05+_setup_dependant/` but don't follow proper structure:

| Folder | Contents | Issue |
|--------|----------|-------|
| `sub_layer_0_14_archives/` | legacy, migration_reports, old_docs, old_scripts, ui_controls | Should be in layer_0_99_stages/stage_0_11_archives/ |
| `templates/` | 0AGNOSTIC.md.template, .0agnostic-template/ | Should be in .0agnostic/ or sub_layer_0_01_prompts/ |
| `scripts/` | agnostic-sync.sh | Duplicates .0agnostic/hooks/scripts/ |

### 3. Missing Hierarchy Indicator
Sub-layers that contain nested sub-layers (hierarchical organization) have no naming indicator to signal this structure to AI agents.

### 4. No Proposal Staging System
Currently proposals are flat files. No way to:
- Experiment with alternative approaches on specific layers/stages
- Version proposals with staged rollouts
- A/B test different implementations

---

## Proposed Solution

### Phase 1: Rename `_content` → `_group`

Find and rename all `*_content` directories to `*_group`:
```bash
# Pattern
sub_layer_N_XX_content → sub_layer_N_XX_group
subxN_layer_XX_content → subxN_layer_XX_group
```

**Affected locations**:
- `layer_-1_group/.../sub_layer_-1_05_content` → `sub_layer_-1_05_group`
- `layer_-1_group/.../sub_layer_-1_06_content` → `sub_layer_-1_06_group`
- `layer_0_group/.../sub_layer_0_05_content` → `sub_layer_0_05_group`
- `layer_0_group/.../sub_layer_0_06_content` → `sub_layer_0_06_group`
- All nested `subxN_layer_XX_content` directories

### Phase 2: Relocate Archives

Move `sub_layer_0_14_archives/` contents to proper archive location:

```
FROM: layer_0/sub_layer_0_05+_setup_dependant/sub_layer_0_14_archives/
TO:   layer_0/layer_0_99_stages/stage_0_11_archives/setup_dependant_archives/

Contents mapping:
├── legacy/                → archives/legacy/
├── migration_reports/     → archives/migration_reports/
├── old_docs/              → archives/old_docs/
├── old_scripts/           → archives/old_scripts/
└── ui_controls/           → archives/ui_controls/
```

Then delete the empty `sub_layer_0_14_archives/` folder.

### Phase 3: Relocate Templates

Move templates to `.0agnostic/templates/` (the canonical location):

```
FROM: layer_0/sub_layer_0_05+_setup_dependant/templates/
TO:   .0agnostic/templates/

Contents:
├── 0AGNOSTIC.md.template
└── .0agnostic-template/
```

Then delete the empty `templates/` folder.

### Phase 4: Add `_hierarchy` Suffix

Add `_hierarchy` suffix to sub-layers that contain nested sub-layers:

```
BEFORE: sub_layer_0_05+_setup_dependant
AFTER:  sub_layer_0_05+_setup_dependant_hierarchy
```

**Convention**:
| Suffix | Meaning |
|--------|---------|
| `_group` | Contains child content (like layer_N_group) |
| `_hierarchy` | Contains nested sub-layers in hierarchical organization |

**Affected directories**:
- `layer_0/layer_0_03_sub_layers/sub_layer_0_05+_setup_dependant` → `sub_layer_0_05+_setup_dependant_hierarchy`
- Research project copies follow same pattern

### Phase 5: Consolidate Scripts

The `scripts/agnostic-sync.sh` should be in `.0agnostic/hooks/scripts/`:

```
FROM: layer_0/sub_layer_0_05+_setup_dependant/scripts/agnostic-sync.sh
TO:   .0agnostic/hooks/scripts/agnostic-sync.sh  (if not exists)
      OR verify it's a duplicate and delete
```

Then delete the empty `scripts/` folder.

### Phase 5: Staged Proposals System

Add staging infrastructure to layer registries for experimental proposals:

#### 5.1 New Structure for Proposals

```
layer_N_00_layer_registry/
├── proposals/
│   ├── active/                              # Currently active proposals
│   │   └── proposal_v6.md
│   ├── staging/                             # Proposals being tested
│   │   ├── stage_experimental/              # Highly experimental
│   │   │   ├── stage_01_request_gathering/
│   │   │   ├── stage_02_research/
│   │   │   ├── stage_03_instructions/
│   │   │   ├── stage_04_planning/
│   │   │   ├── stage_05_design/
│   │   │   ├── stage_06_development/
│   │   │   ├── stage_07_testing/
│   │   │   ├── stage_08_criticism/
│   │   │   ├── stage_09_fixing/
│   │   │   ├── stage_10_current_product/
│   │   │   └── stage_11_archives/
│   │   ├── stage_testing/                   # Under active testing
│   │   │   ├── stage_01_request_gathering/
│   │   │   ├── stage_02_research/
│   │   │   ├── stage_03_instructions/
│   │   │   ├── stage_04_planning/
│   │   │   ├── stage_05_design/
│   │   │   ├── stage_06_development/
│   │   │   ├── stage_07_testing/
│   │   │   ├── stage_08_criticism/
│   │   │   ├── stage_09_fixing/
│   │   │   ├── stage_10_current_product/
│   │   │   └── stage_11_archives/
│   │   └── stage_rollout/                   # Gradual rollout
│   │       ├── stage_01_request_gathering/
│   │       ├── stage_02_research/
│   │       ├── stage_03_instructions/
│   │       ├── stage_04_planning/
│   │       ├── stage_05_design/
│   │       ├── stage_06_development/
│   │       ├── stage_07_testing/
│   │       ├── stage_08_criticism/
│   │       ├── stage_09_fixing/
│   │       ├── stage_10_current_product/
│   │       └── stage_11_archives/
│   ├── archived/                            # Historical proposals
│   │   └── proposal_v1-v5.md
│   └── 0INDEX.md                            # Proposal index with status
```

#### 5.2 Staging Level Purposes

| Staging Level | Purpose | Workflow |
|---------------|---------|----------|
| **experimental** | Early ideas, high risk | Full 01-11 stages for careful iteration |
| **testing** | Validated concepts, moderate risk | Full 01-11 stages for refinement |
| **rollout** | Production-ready, low risk | Full 01-11 stages for deployment tracking |

Each proposal progresses through its own 01-11 stages within each staging level before graduating to the next level.

#### 5.3 Proposal Staging Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           STAGING PIPELINE                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  EXPERIMENTAL (limited scope)                                               │
│  ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐                  │
│  │ 01 │ 02 │ 03 │ 04 │ 05 │ 06 │ 07 │ 08 │ 09 │ 10 │ 11 │ ──┐             │
│  └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘   │             │
│   req  res  ins  pln  des  dev  tst  crt  fix  prd  arc     │             │
│                                                              ▼             │
│  TESTING (expanded scope)                                                   │
│  ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐                  │
│  │ 01 │ 02 │ 03 │ 04 │ 05 │ 06 │ 07 │ 08 │ 09 │ 10 │ 11 │ ──┐             │
│  └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘   │             │
│   req  res  ins  pln  des  dev  tst  crt  fix  prd  arc     │             │
│                                                              ▼             │
│  ROLLOUT (full scope)                                                       │
│  ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐                  │
│  │ 01 │ 02 │ 03 │ 04 │ 05 │ 06 │ 07 │ 08 │ 09 │ 10 │ 11 │ ──▶ ACTIVE      │
│  └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘                  │
│   req  res  ins  pln  des  dev  tst  crt  fix  prd  arc                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

Scope progression:
  experimental: 1 layer, 1-2 stages, 1 feature
  testing:      1 layer group, multiple stages, multiple features
  rollout:      all layers, all stages, gradual percentage increase
```

#### 5.4 Proposal Metadata

Each staged proposal gets metadata header:

```markdown
---
proposal_id: v7_alternative_staging
status: experimental
applies_to:
  layers: [-1]              # Only research layer
  stages: [02, 03]          # Only research & instructions stages
  features: [better_layer_stage_system]
rollout_percentage: 10%     # For gradual rollouts
parent_proposal: v6         # What it's based on
experiment_start: 2026-02-03
experiment_end: 2026-02-10
---
```

#### 5.5 Benefits

| Capability | Description |
|------------|-------------|
| **Safe experimentation** | Test new approaches on limited scope |
| **Gradual rollout** | Increase scope as confidence grows |
| **A/B testing** | Run multiple approaches simultaneously |
| **Easy rollback** | Revert by changing status |
| **Version history** | Track evolution of approaches |

---

## Implementation Plan

| Phase | Task | Status | Impact |
|-------|------|--------|--------|
| 1 | Rename `_content` → `_group` | ✅ Done | ~10 directories renamed |
| 2 | Relocate archives | ✅ Done | 5 subdirs → stage_0_11_archives/ |
| 3 | Relocate templates | ✅ Done | 2 items → .0agnostic/templates/ |
| 4 | Add `_hierarchy` suffix | ✅ Done | 3 directories renamed |
| 5 | Consolidate scripts | ✅ Done | 1 file → .0agnostic/hooks/scripts/ |
| 6 | Create staging structure | ✅ Done | 3 staging levels × 11 stages each |

---

## Verification Checklist

- [ ] No `*_content` directories remain (all renamed to `*_group`)
- [ ] `sub_layer_0_14_archives/` removed from setup_dependant
- [ ] `templates/` removed from setup_dependant
- [ ] `scripts/` removed from setup_dependant
- [ ] Proposal staging structure created in layer registries
- [ ] 0INDEX.md for proposals created

---

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Breaking existing references | Search and update all references before rename |
| Lost archive content | Verify content moved before deleting source |
| Script duplication confusion | Clearly document canonical location |

---

*Proposal for cleanup and enhanced proposal management*
