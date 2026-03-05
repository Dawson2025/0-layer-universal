---
resource_id: "fb812e05-e0ba-4fd7-99fe-45c220aaa34f"
resource_type: "rule"
resource_name: "test_design"
---
# Test Design: STAGE_REPORT_RULE

**Rule**: `../STAGE_REPORT_RULE.md`
**Type**: Structural + Behavioral
**Scope**: Validates that stage agents write stage reports in canonical handoff locations

---

## Structural Tests

### TC-SRR-01: Rule file exists and references correct canonical locations

**Steps**:
1. Check rule exists
2. Verify it references `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md`
3. Verify it references `.0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md`

**Expected**: Rule points to both outgoing handoff directions
**Type**: Structural

### TC-SRR-02: Stage report protocol exists and is consistent

**Steps**:
1. Check `.0agnostic/03_protocols/stage_report_protocol.md` exists
2. Verify it matches the rule's requirements (canonical locations, format, line limit)

**Expected**: Protocol and rule are aligned
**Type**: Structural

### TC-SRR-03: Active stages have stage reports

**Steps**:
1. Find all stages marked as "active" or "complete"
2. Check for stage_report.md in their canonical handoff locations
3. Report coverage: N stages with reports / M active stages

**Expected**: All active/complete stages have stage reports
**Type**: Structural

---

## Behavioral Tests

### TC-SRR-04: Stage agent writes report before exiting
### TC-SRR-05: Report follows canonical format (under 30 lines)
### TC-SRR-06: Report goes to both to_above and to_below

---

## Test Case Summary

| Category | Count | Type |
|----------|-------|------|
| Structural | 3 | Structural |
| Behavioral | 3 | Behavioral |
| **Total** | **6** | |
