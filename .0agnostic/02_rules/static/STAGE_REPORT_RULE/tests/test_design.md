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

<!-- section_id: "5df4b3bf-c6df-4c04-872f-956ac60363f1" -->
## Structural Tests

<!-- section_id: "1152f312-f370-42b5-86e3-2bc17c86bcc1" -->
### TC-SRR-01: Rule file exists and references correct canonical locations

**Steps**:
1. Check rule exists
2. Verify it references `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md`
3. Verify it references `.0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md`

**Expected**: Rule points to both outgoing handoff directions
**Type**: Structural

<!-- section_id: "b3364878-25e4-417d-a341-261b3f2b1b5a" -->
### TC-SRR-02: Stage report protocol exists and is consistent

**Steps**:
1. Check `.0agnostic/03_protocols/stage_report_protocol.md` exists
2. Verify it matches the rule's requirements (canonical locations, format, line limit)

**Expected**: Protocol and rule are aligned
**Type**: Structural

<!-- section_id: "a8dabe84-7317-4f8d-89a8-ec0fbd86d2d9" -->
### TC-SRR-03: Active stages have stage reports

**Steps**:
1. Find all stages marked as "active" or "complete"
2. Check for stage_report.md in their canonical handoff locations
3. Report coverage: N stages with reports / M active stages

**Expected**: All active/complete stages have stage reports
**Type**: Structural

---

<!-- section_id: "ae883912-a6c5-4d9f-910b-3c1fbda44603" -->
## Behavioral Tests

<!-- section_id: "0722bd8a-8047-4cb2-8708-0e3654c2ad76" -->
### TC-SRR-04: Stage agent writes report before exiting
<!-- section_id: "95dcfb6a-da49-472c-8bca-0b06c4cc9bc1" -->
### TC-SRR-05: Report follows canonical format (under 30 lines)
<!-- section_id: "f9e774e3-97a5-4575-b185-9c96217b7e13" -->
### TC-SRR-06: Report goes to both to_above and to_below

---

<!-- section_id: "de8d730b-4df9-4c89-94f7-cda651353e82" -->
## Test Case Summary

| Category | Count | Type |
|----------|-------|------|
| Structural | 3 | Structural |
| Behavioral | 3 | Behavioral |
| **Total** | **6** | |
