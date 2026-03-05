---
resource_id: "a5f0a140-49e0-4e76-8ebd-eb2713d7da88"
resource_type: "output"
resource_name: "test_design_05_hierarchy_inheritance"
---
# Test Design: 05 Hierarchy Inheritance Model

**Validates**: `stage_2_04_design/outputs/by_topic/05_hierarchy_inheritance_model.md`
**Type**: Structural (bash)
**Script name**: `test_hierarchy_inheritance.sh`

---

<!-- section_id: "5f64c658-c74b-42df-9714-ed48d777ff0e" -->
## What We're Testing

What context propagates across hierarchy levels, by which mechanism, and whether documented gaps are accurately described. The CLAUDE.md cascade is the primary enforcement mechanism — universal rules must appear at every level.

---

<!-- section_id: "f869589e-8859-4225-ab05-4319966b4295" -->
## Test Cases

<!-- section_id: "2f39b846-d3a5-466b-820c-f6a189dfcb62" -->
### TC-05-01: CLAUDE.md cascade delivers universal rules

**Steps**:
1. Read root `0_layer_universal/CLAUDE.md`
2. Extract key universal rules (AI Context Modification Protocol, Stage Completeness Rule, Commit/Push Rule)
3. For each entity CLAUDE.md in the chain down to context_chain_system:
   - Verify the agent would see all universal rules (via the filesystem walk)
4. Count total CLAUDE.md files in the path

**Expected**: Universal rules are present in the root CLAUDE.md and the cascade delivers them to every child
**Note**: Claude Code auto-loads every CLAUDE.md from root to working directory — this test verifies the root has the right content
**Type**: Structural

<!-- section_id: "dffa9031-fd89-4444-9ff2-9cc8aa992ec4" -->
### TC-05-02: Parent references form unbroken chain

**Steps**:
1. Start at context_chain_system 0AGNOSTIC.md
2. Follow `**Parent**:` reference
3. At each parent, verify:
   - 0AGNOSTIC.md exists at the referenced path
   - The parent also has a **Parent** reference (except root)
4. Continue until reaching root (no parent reference)

**Expected**: Unbroken parent chain from leaf to root with no dangling references
**Note**: Extends existing test_context_chain_traversal but validates 0AGNOSTIC.md chain, not just CLAUDE.md
**Type**: Structural

<!-- section_id: "5f9af48f-9bc0-4837-8d95-a9828bf10604" -->
### TC-05-03: Hot rule promotion — promote: hot frontmatter works

**Steps**:
1. Find all `.0agnostic/02_rules/` files with `promote: hot` in YAML frontmatter
2. For each promoted rule, extract `hot_trigger` and `hot_summary`
3. Run agnostic-sync.sh for that entity
4. Check generated CLAUDE.md for `## Promoted Rules` table
5. Verify promoted rule appears in the table with matching trigger/summary

**Expected**: Every rule with `promote: hot` appears in the Promoted Rules table of generated tool files
**Type**: Integration

<!-- section_id: "c518f26a-61e9-4e57-a974-40f11e46b7e1" -->
### TC-05-04: Hot promotion content matches source

**Steps**:
1. For each promoted rule in CLAUDE.md's Promoted Rules table:
   - Extract the "Full rule:" path
   - Read that path
   - Verify the file exists and has `promote: hot` frontmatter
2. Count promoted rules in table vs promoted rules in filesystem

**Expected**: Promoted Rules table is complete (no missing rules) and paths are valid
**Type**: Structural

<!-- section_id: "21d6cfb9-4a5d-4d45-864b-badbf896e3e0" -->
### TC-05-05: Gap 1 detection — conventions.childNaming

**Steps**:
1. For entities with children, read parent 0AGNOSTIC.md or index.jsonld
2. Check if `childNaming` convention is defined
3. Check if children follow the naming convention
4. Report violations (convention defined but not followed)

**Expected**: Document which entities have naming convention violations (known gap)
**Outcome**: PASS = gap is accurately documented; FAIL = gap is worse/better than documented
**Type**: Structural (audit)

<!-- section_id: "bdbb040c-b725-472e-8140-f479fd94d4e0" -->
### TC-05-06: Gap 2 detection — layer number consistency

**Steps**:
1. For each entity in the hierarchy:
   - Extract layer number from directory name (e.g., `layer_2_...` → 3)
   - Extract parent's layer number
   - Verify child = parent + 1
2. Report any mismatches

**Expected**: Layer numbers are consistent (or violations match documented gap)
**Type**: Structural (audit)

<!-- section_id: "f2920d7b-946c-43e6-bb7b-46bebe5d36cd" -->
### TC-05-07: Gap 3 detection — inherited context visibility

**Steps**:
1. Pick 3 entities at different depths (root, mid, leaf)
2. For each, trace the full inheritance chain:
   - CLAUDE.md cascade (count files, total lines)
   - 0AGNOSTIC.md parent chain (count entities)
   - .0agnostic/02_rules/static/ at each level
3. Report total inherited context per entity

**Expected**: Audit report showing inherited context volume at different depths
**Outcome**: Informational — validates gap 3 description
**Type**: Structural (audit)

<!-- section_id: "85c60150-eea0-44d6-8359-d1a62d8c34a3" -->
### TC-05-08: Dynamic rules don't cross entity boundaries

**Steps**:
1. Find all `.0agnostic/02_rules/dynamic/` files at context_chain_system level
2. Verify they are NOT present in child entities (chain_visualization, context_loading)
3. Find dynamic rules at root level
4. Verify they are NOT automatically present in descendant entities

**Expected**: Dynamic rules stay scoped to their entity (confirms gap 4)
**Type**: Structural

---

<!-- section_id: "cc8d4df6-3913-4d94-92a5-da104ed6b3dc" -->
## Coverage Gap Analysis

| Design Concept | Test Case | Status |
|---------------|-----------|--------|
| CLAUDE.md cascade (always propagates) | TC-05-01 | New |
| 0AGNOSTIC parent chain | TC-05-02 | New (extends chain traversal) |
| Hot rule promotion | TC-05-03, TC-05-04 | New |
| Gap 1 (childNaming) | TC-05-05 | New (audit) |
| Gap 2 (layer number) | TC-05-06 | New (audit) |
| Gap 3 (visibility) | TC-05-07 | New (audit) |
| Gap 4 (dynamic rules) | TC-05-08 | New |
