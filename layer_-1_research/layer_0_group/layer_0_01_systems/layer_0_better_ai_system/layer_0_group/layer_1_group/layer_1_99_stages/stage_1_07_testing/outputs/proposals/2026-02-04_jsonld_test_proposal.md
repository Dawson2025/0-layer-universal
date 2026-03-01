# Test Proposal: JSON-LD Navigation System

## Metadata

| Field | Value |
|-------|-------|
| **Proposal ID** | TEST-2026-02-04-JSONLD |
| **Status** | Draft |
| **Created** | 2026-02-04 |
| **Related Proposal** | PROP-2026-02-03-JSONLD |
| **Prototype Location** | `layer_0_group/layer_0_features/layer_0_feature_better_layer_stage_system/` |

---

## Purpose

Define what needs to be tested, specifications for each test, and methodology for validating the JSON-LD navigation system prototype.

---

## Tree of Test Needs

```
00_jsonld_validation
├── 01_navigation_works
│   ├── need_01_parent_traversal      → Agent can go up the hierarchy
│   ├── need_02_child_traversal       → Agent can go down the hierarchy
│   ├── need_03_sibling_discovery     → Agent can find related entities
│   └── need_04_cross_reference       → Links resolve correctly
├── 02_triggers_fire
│   ├── need_01_session_start         → onSessionStart triggers load correct files
│   ├── need_02_stage_entry           → Stage-specific skills are identified
│   └── need_03_action_triggers       → Entity creation triggers are found
├── 03_tree_of_needs_linkage
│   ├── need_01_needs_discoverable    → Agent can find tree of needs
│   ├── need_02_mapping_clear         → Need-to-feature mapping is understandable
│   └── need_03_hierarchy_navigable   → Branches/needs traversable
└── 04_agent_usability
    ├── need_01_faster_than_markdown  → JSON-LD parsing beats text parsing
    ├── need_02_no_missing_info       → All needed context is present
    └── need_03_intuitive_structure   → Agent can use without special training
```

---

## Test Specifications

### T01: Parent Traversal

| Field | Value |
|-------|-------|
| **Need** | 01_navigation_works > need_01_parent_traversal |
| **Input** | Agent at `stage_0_01_request_gathering/index.jsonld` |
| **Action** | Follow `nav:parent` chain to root |
| **Expected** | Reach `layer_0_feature_better_layer_stage_system/index.jsonld` |
| **Success Criteria** | All `@id` links resolve; parent names match actual folders |

### T02: Child Traversal

| Field | Value |
|-------|-------|
| **Need** | 01_navigation_works > need_02_child_traversal |
| **Input** | Agent at root `index.jsonld` |
| **Action** | Follow `nav:children` to find stages |
| **Expected** | Reach all 11 stages via links |
| **Success Criteria** | `nav:children` → `nav:stages` → all stage `@id`s resolve |

### T03: Sibling Discovery

| Field | Value |
|-------|-------|
| **Need** | 01_navigation_works > need_03_sibling_discovery |
| **Input** | Agent at root `index.jsonld` |
| **Action** | Read `rel:siblings` |
| **Expected** | Find links to related features (ai_context_system, etc.) |
| **Success Criteria** | Sibling paths exist and are valid relative paths |

### T04: Session Start Triggers

| Field | Value |
|-------|-------|
| **Need** | 02_triggers_fire > need_01_session_start |
| **Input** | Agent reads `index.jsonld` |
| **Action** | Execute `trigger:onSessionStart` actions |
| **Expected** | Agent knows to read CLAUDE.md and index.jsonld |
| **Success Criteria** | Trigger actions have valid targets; priority order is clear |

### T05: Stage Entry Triggers

| Field | Value |
|-------|-------|
| **Need** | 02_triggers_fire > need_02_stage_entry |
| **Input** | Agent at `layer_0_99_stages/index.jsonld` |
| **Action** | Find skill for stage 01 |
| **Expected** | `stages[0].trigger:skill` points to workflow |
| **Success Criteria** | Skill path resolves; skill folder exists |

### T06: Tree of Needs Discovery

| Field | Value |
|-------|-------|
| **Need** | 03_tree_of_needs_linkage > need_01_needs_discoverable |
| **Input** | Agent at root `index.jsonld` |
| **Action** | Follow `nav:treeOfNeeds` |
| **Expected** | Reach `tree_of_needs/index.jsonld` |
| **Success Criteria** | Tree structure is parseable; rootNeed.branches exist |

### T07: Need-to-Feature Mapping

| Field | Value |
|-------|-------|
| **Need** | 03_tree_of_needs_linkage > need_02_mapping_clear |
| **Input** | Agent reads `tree_of_needs/index.jsonld` |
| **Action** | Interpret `rel:mapsTo` on a branch |
| **Expected** | Understand that branch maps to layer+1 feature |
| **Success Criteria** | `relativeDepth` and `entityType` are present and clear |

### T08: Full Navigation Test

| Field | Value |
|-------|-------|
| **Need** | 04_agent_usability > need_02_no_missing_info |
| **Input** | Agent starts fresh, given only root path |
| **Action** | Navigate to a specific need in tree_of_needs |
| **Expected** | Agent can find path without reading markdown |
| **Success Criteria** | Complete navigation using only JSON-LD links |

---

## Test Methodology

### Phase 1: Link Validation (Automated)

**Method**: Script that parses all `index.jsonld` files and validates:
- All `@id` paths resolve to existing files/folders
- All `@type` values are in schema
- No broken cross-references

**Output**: Pass/fail report with broken links listed

### Phase 2: Agent Walkthrough (Manual)

**Method**: Agent (Claude) attempts each test specification above using only JSON-LD files

**Protocol**:
1. Agent states current location
2. Agent reads index.jsonld
3. Agent describes what it learned
4. Agent follows link to next location
5. Agent confirms arrival

**Output**: Test log with pass/fail for each specification

### Phase 3: Comparison Test

**Method**: Same navigation task, two approaches:
1. Using JSON-LD only
2. Using CLAUDE.md + folder traversal

**Metrics**:
- Steps to complete
- Files read
- Accuracy of final destination
- Information completeness

**Output**: Comparison table

---

## Test Environment

| Item | Location |
|------|----------|
| **Prototype** | `layer_0_group/layer_0_features/layer_0_feature_better_layer_stage_system/` |
| **Test Logs** | `stage_-1_07_testing/outputs/test_logs/` |
| **Results** | `stage_-1_07_testing/outputs/results/` |

---

## Success Criteria (Overall)

| Criterion | Threshold |
|-----------|-----------|
| Link resolution | 100% of `@id` links resolve |
| Trigger coverage | All trigger types have valid targets |
| Navigation completeness | Agent reaches all areas via JSON-LD |
| Usability | Agent prefers JSON-LD over markdown parsing |

---

## Risks

| Risk | Mitigation |
|------|------------|
| Broken links after restructure | Run link validation after any changes |
| Schema mismatch | Keep schema.jsonld updated |
| Agent confusion | Add comments/descriptions to ambiguous links |

---

## Next Steps

1. **Review this proposal** - User approval
2. **Create test log template** - Standard format for recording results
3. **Run Phase 1** - Automated link validation
4. **Run Phase 2** - Agent walkthrough tests
5. **Run Phase 3** - Comparison test (if Phase 1-2 pass)
6. **Document results** - In `stage_-1_07_testing/outputs/results/`

---

## Version

- **Proposal Version**: 1.0.0
- **Created**: 2026-02-04
