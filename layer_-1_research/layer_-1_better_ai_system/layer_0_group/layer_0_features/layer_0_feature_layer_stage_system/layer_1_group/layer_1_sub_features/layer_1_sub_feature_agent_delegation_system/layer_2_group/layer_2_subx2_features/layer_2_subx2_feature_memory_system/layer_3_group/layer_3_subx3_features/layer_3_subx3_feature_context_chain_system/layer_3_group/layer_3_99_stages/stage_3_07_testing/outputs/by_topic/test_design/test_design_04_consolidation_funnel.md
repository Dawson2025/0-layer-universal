# Test Design: 04 Consolidation Funnel (Bottom-Up)

**Validates**: `stage_3_04_design/outputs/by_topic/04_context_propagation_funnel.md`
**Type**: Structural (bash) + Integration (bash)
**Script name**: `test_consolidation_funnel.sh`

---

## What We're Testing

Bottom-up consolidation: outputs → output_report → .0agnostic → stage_report → 0AGNOSTIC.md. This pattern should be consistent across all active stages. Cross-level flow: stage reports → entity from_below, entity reports → parent from_below.

---

## Test Cases

### TC-04-01: Active stages have outputs

**Steps**:
1. Find all stages marked "active" (have `outputs/` with content beyond .gitkeep)
2. For each, check `outputs/` contains at least one work product file

**Expected**: Every active stage has content in outputs/
**Type**: Structural

### TC-04-02: Active stages have stage reports

**Steps**:
1. For each active stage (has outputs with content)
2. Check `outputs/stage_report.md` exists
3. Verify it contains required sections: Status, Summary, Key Outputs, Findings, Open Items, Handoff
4. Verify it is under 30 lines (protocol requirement)

**Expected**: Every active stage has a stage_report.md with all required sections, <30 lines
**Type**: Structural

### TC-04-03: Stage report references outputs

**Steps**:
1. For each stage_report.md
2. Check it mentions at least one file from `outputs/` or `outputs/by_topic/`
3. Verify Key Outputs section has at least one entry

**Expected**: Stage reports reference their stage's outputs (not empty summaries)
**Type**: Structural

### TC-04-04: Entity has incoming stage reports (from_below)

**Steps**:
1. For context_chain_system entity, check `.0agnostic/05_handoff_documents/01_incoming/03_from_below/stage_reports/`
2. Verify it contains stage report copies for active stages
3. Cross-check: each file in from_below matches an actual stage_report.md

**Expected**: Entity's from_below/stage_reports/ mirrors active stage reports
**Note**: This requires sync-handoffs.sh to have been run
**Type**: Integration

### TC-04-05: Entity has consolidation reports (outgoing)

**Steps**:
1. Check `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/`
2. Verify `stages_report.md` exists (consolidation of all stage reports)
3. Verify it references all active stages
4. If entity has children: verify `child_layers_report.md` exists

**Expected**: Entity produces consolidation reports for its parent
**Type**: Structural

### TC-04-06: 0AGNOSTIC.md reflects current stage status

**Steps**:
1. Read entity 0AGNOSTIC.md Current Status section
2. Compare against stage_report.md statuses
3. Flag if 0AGNOSTIC.md status is stale (mentions fewer active stages than exist)

**Expected**: 0AGNOSTIC.md status is consistent with stage reports
**Type**: Structural (heuristic — fuzzy match on stage count)

### TC-04-07: Recursive pattern — child entity reports flow to parent

**Steps**:
1. For memory_system (parent of context_chain_system):
   - Check `from_below/layer_reports/` for context_chain_system layer_report
2. For context_chain_system:
   - Check `from_below/stage_reports/` for active stage reports

**Expected**: Reports flow upward at both stage→entity and entity→parent levels
**Type**: Integration

### TC-04-08: sync-handoffs.sh distributes correctly

**Steps**:
1. Run sync-handoffs.sh for context_chain_system
2. Verify stage reports appear in entity from_below/
3. Verify sibling stages get from_sides/ copies
4. Verify parent entity gets layer_report

**Expected**: sync-handoffs.sh populates all three directions (up, lateral, down)
**Type**: Integration

---

## Coverage Gap Analysis

| Design Concept | Test Case | Status |
|---------------|-----------|--------|
| Stage-internal funnel | TC-04-01, TC-04-02, TC-04-03 | New |
| Cross-level flow | TC-04-04, TC-04-07 | New |
| Consolidation reports | TC-04-05 | New |
| 0AGNOSTIC.md as entry point | TC-04-06 | New |
| sync-handoffs.sh | TC-04-08 | New |
| Recursive pattern | TC-04-07 | New |
