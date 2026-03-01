# System Prompt Architecture - Implementation Plan

**Status**: Draft
**Date**: 2026-01-26
**Based On**:
- `stage_-1_03_instructions/.../system_prompt_architecture_instructions.md`
- `stage_-1_04_design/.../system_prompt_architecture_design.md`

---

## Execution Summary

**FULL SYSTEM IMPLEMENTATION** - Apply to entire `0_layer_universal/`

| Phase | Description | Scope |
|-------|-------------|-------|
| 1 | Root & Layer Containers | 0_layer_universal/, layer_0_group/, layer_1/, layer_-1_research/ |
| 2 | All Stages Containers | Every layer_X_99_stages/ |
| 3 | All Sub_layers Containers | Every layer_X_03_sub_layers/ |
| 4 | All Individual Stages | Every stage_X_XX_*/ |
| 5 | All Individual Sub_layers | Every sub_layer_X_XX_*/ |
| 6 | Root CLAUDE.md with Rules | Embed universal rules |
| 7 | Verify & Test | Full system validation |

---

## Phase 1: Pilot in better_ai_system

**Goal**: Implement pattern in this research project first to validate approach.

### Task 1.1: Convert stage_-1_00_stage_manager to registry
```
Location: layer_-1_group/layer_-1_99_stages/

Steps:
1. [ ] Move CLAUDE.md from stage_-1_00_stage_manager/ to layer_-1_99_stages/CLAUDE.md
2. [ ] Move .claude/ from stage_-1_00_stage_manager/ to layer_-1_99_stages/.claude/
3. [ ] Rename stage_-1_00_stage_manager/ to stage_-1_00_registry/
4. [ ] Keep only data files in registry (stages.yaml if exists)
```

### Task 1.2: Create hand_off_documents at stages level
```
Location: layer_-1_group/layer_-1_99_stages/

Steps:
1. [ ] Create hand_off_documents/incoming/from_above/
2. [ ] Create hand_off_documents/incoming/from_below/
3. [ ] Create hand_off_documents/outgoing/to_above/
4. [ ] Create hand_off_documents/outgoing/to_below/
5. [ ] Add README.md explaining structure
```

### Task 1.3: Update stages CLAUDE.md with manager role
```
Location: layer_-1_group/layer_-1_99_stages/CLAUDE.md

Content:
- Role: Stages Manager
- Responsibilities
- On Session Start instructions
- Children list (stages)
```

### Task 1.4: Ensure each stage has hand_off_documents
```
For each stage_-1_XX_*/:
1. [ ] Verify/create hand_off_documents/incoming/from_above/
2. [ ] Verify/create hand_off_documents/incoming/from_below/
3. [ ] Verify/create hand_off_documents/outgoing/to_above/
4. [ ] Verify/create hand_off_documents/outgoing/to_below/
```

### Task 1.5: Test delegation flow
```
Test:
1. [ ] Start session at layer_-1_99_stages/
2. [ ] Create test task handoff
3. [ ] Verify stage can read from incoming/from_above/
4. [ ] Verify stage can write to outgoing/to_above/
```

---

## Phase 2: Expand to layer_0

**Goal**: Apply pattern to universal layer.

### Task 2.1: Convert layer_0_00_layer_registry
```
Location: layer_0_group/

Steps:
1. [ ] Move any CLAUDE.md content to layer_0_group/CLAUDE.md
2. [ ] Ensure layer_0_00_layer_registry/ contains only data
```

### Task 2.2: Create hand_off_documents at layer_0
```
Location: layer_0_group/

Steps:
1. [ ] Create four-directional hand_off_documents/
2. [ ] Update layer_0_group/CLAUDE.md with manager role
```

### Task 2.3: Update layer_0_99_stages
```
Apply same pattern as Phase 1 to layer_0_99_stages/
```

### Task 2.4: Update layer_0_03_sub_layers
```
Location: layer_0_group/layer_0_03_sub_layers/

Steps:
1. [ ] Create CLAUDE.md (Sub_layers Manager)
2. [ ] Create .claude/
3. [ ] Create hand_off_documents/
4. [ ] Ensure sub_layer_0_00_registry exists (data only)
5. [ ] Verify each sub_layer has CLAUDE.md
```

### Task 2.5: Update root CLAUDE.md
```
Location: 0_layer_universal/CLAUDE.md

Steps:
1. [ ] Add embedded universal rules
2. [ ] Add Root Manager role
3. [ ] Add navigation to layers
4. [ ] Create hand_off_documents/ at root
```

---

## Phase 3: Expand to layer_1

**Goal**: Apply pattern to all projects.

### Task 3.1: Update layer_1 structure
```
For layer_1/ and each layer_1_project_*/:
1. [ ] Ensure CLAUDE.md exists with manager role
2. [ ] Create hand_off_documents/
3. [ ] Update stages and sub_layers within
```

---

## Phase 4: Verify & Document

### Task 4.1: Verification tests
```
Run all test cases from design document:
1. [ ] Simple delegation test
2. [ ] Skip-level escalation test
3. [ ] Multi-level aggregation test
```

### Task 4.2: Update documentation
```
1. [ ] Update master documentation with new pattern
2. [ ] Create migration guide for future projects
3. [ ] Archive old structure documentation
```

---

## Execution Order

```
Week 1: Phase 1 (Pilot)
├── Day 1: Tasks 1.1, 1.2
├── Day 2: Tasks 1.3, 1.4
└── Day 3: Task 1.5 (testing)

Week 2: Phase 2 (layer_0)
├── Day 1: Tasks 2.1, 2.2
├── Day 2: Tasks 2.3, 2.4
└── Day 3: Task 2.5

Week 3: Phase 3 (layer_1) + Phase 4
├── Day 1-2: Task 3.1
└── Day 3: Tasks 4.1, 4.2
```

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Breaking existing references | Search all files for old paths before renaming |
| Incomplete migration | Use verification checklist after each phase |
| Confusion during transition | Keep old structure documented in archives |

---

## Success Criteria

- [ ] All 00 positions are registries (data only)
- [ ] All containers have CLAUDE.md with manager role
- [ ] All containers have four-directional hand_off_documents/
- [ ] Root CLAUDE.md has embedded universal rules
- [ ] Delegation test passes
- [ ] Escalation test passes
- [ ] Aggregation test passes

---

## Ready to Execute

When this plan is approved:
1. Start with Phase 1, Task 1.1
2. Follow modification protocol (show changes, get approval)
3. Commit after each task
4. Verify before moving to next phase
