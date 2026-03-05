---
resource_id: "22c41467-7c70-49c9-b42c-8c9b5d562bea"
resource_type: "rule"
resource_name: "test_design"
---
# Test Design: I0_FILE_CHANGE_REPORTING

**Rule**: `../I0_FILE_CHANGE_REPORTING.md`
**Type**: Structural + Behavioral
**Scope**: Validates that agents discover, load, and comply with the file change reporting rule

---

<!-- section_id: "0c5c2d8c-e346-4307-8c32-835754c19ffb" -->
## Structural Precondition Tests

<!-- section_id: "66ed7131-dfcf-4be1-b9b8-519857d34c34" -->
### TC-FCR-01: Rule file exists with correct frontmatter

**Steps**:
1. Check rule file exists at `.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING/I0_FILE_CHANGE_REPORTING.md`
2. Verify YAML frontmatter contains `promote: hot`, `hot_summary:` mentioning "full absolute paths", `hot_trigger:`
3. Verify body contains the two-part rule format (inline + summary)

**Expected**: Rule file exists with hot promotion frontmatter and complete specification
**Type**: Structural

<!-- section_id: "2585940c-3ee9-4ab0-b7fb-07372d6818ba" -->
### TC-FCR-02: Hot rule appears in root CLAUDE.md promoted rules

**Steps**:
1. Read root CLAUDE.md
2. Search for Promoted Rules section
3. Verify table contains row matching trigger "Any turn that modifies files" and summary mentioning "full absolute paths"

**Expected**: Hot summary from rule frontmatter appears in CLAUDE.md Promoted Rules table
**Type**: Structural

<!-- section_id: "77bd4c7f-63b9-432d-be1f-b501fa8d29f8" -->
### TC-FCR-03: CLAUDE.md cascade delivers rule to all levels

**Steps**:
1. Starting from root CLAUDE.md, verify it exists at `/home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md`
2. Claude Code loads ALL CLAUDE.md files from root to cwd — verify root is in chain
3. Count CLAUDE.md files in the chain

**Expected**: Root CLAUDE.md with promoted rule is always first in cascade
**Type**: Structural

<!-- section_id: "6bc6bc66-7118-4077-ba46-d54a0a3f778b" -->
### TC-FCR-04: Rule references in ~/.claude/CLAUDE.md (global)

**Steps**:
1. Read `~/.claude/CLAUDE.md`
2. Search for file change reporting references
3. Verify it mentions the rule or points to the full rule file

**Expected**: Global CLAUDE.md also references the rule
**Type**: Structural

<!-- section_id: "dc2a309f-157a-4988-8b13-cc4d563a7324" -->
### TC-FCR-13: Home directory copy in sync

**Steps**:
1. Diff repo copy vs `~/.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING/I0_FILE_CHANGE_REPORTING.md`
2. Files should be identical

**Expected**: Home directory copy matches repo copy exactly
**Type**: Structural

---

<!-- section_id: "4ac9ebf4-fc8d-4aec-a196-f4f76353cbb6" -->
## Behavioral Compliance Tests

<!-- section_id: "fc20d979-be3e-4f09-a20e-ea41aec82535" -->
### TC-FCR-05: Agent reports files when creating new files
<!-- section_id: "a7630bf0-6b08-49d0-8a38-faec664f348e" -->
### TC-FCR-06: Agent reports files when editing existing files
<!-- section_id: "4158cff5-93e1-4817-ad60-b9aea0e9b3c3" -->
### TC-FCR-07: Agent reports multiple file changes correctly
<!-- section_id: "5c204c4c-1439-42f0-8a83-084fb11cceb5" -->
### TC-FCR-08: Agent does NOT report when no files changed
<!-- section_id: "ded09676-1a71-4fe1-a64c-9b10bd3b6500" -->
### TC-FCR-09: Agent uses full absolute paths, never abbreviated
<!-- section_id: "1312f13c-92e9-4481-ab74-29d0deefb2dd" -->
### TC-FCR-10: Sub-agent file changes reported by delegating agent

(See full behavioral test descriptions in the agent_delegation_system stage_1_07_testing test design for detailed setup/check/expected for each)

---

<!-- section_id: "e16f412b-7532-4b02-a950-703f86e9d032" -->
## Discovery Chain Tests

<!-- section_id: "9bcb2276-fe67-4a43-a2f5-2ac37349a3a1" -->
### TC-FCR-11: Rule discovery temperature (Hot)
<!-- section_id: "9b44444b-b9ca-4e7b-9b4b-8fb2378b1afa" -->
### TC-FCR-12: Agent acknowledges rule existence

---

<!-- section_id: "c508986c-6b16-4218-bc47-e8548261b473" -->
## Compliance Scoring Framework

| Criterion | Score | Description |
|-----------|-------|-------------|
| Report present | 0 or 1 | File change report included when files modified? |
| Inline references | 0 or 1 | Changes described WITH their paths inline? |
| All files listed | 0 or 1 | ALL modified files in the summary? |
| Full absolute paths | 0 or 1 | Every path starts from `/home/` with no abbreviation? |
| Correct grouping | 0 or 1 | Files grouped by operation type? |
| Correct ordering | 0 or 1 | Priority order correct (Added > Updated > Moved > Removed)? |
| End of response | 0 or 1 | Summary appears at end, after main content? |
| **Total** | **0-7** | Perfect compliance = 7/7 |

**Passing threshold**: 6/7
**Critical failures**: Report absent (0) or abbreviated paths (0)

<!-- section_id: "432e5af3-05c9-404a-bf0d-bbd6fc20fbdc" -->
## Test Case Summary

| Category | Count | Type |
|----------|-------|------|
| Structural preconditions | 5 (TC-FCR-01 to TC-FCR-04, TC-FCR-13) | Structural |
| Behavioral compliance | 6 (TC-FCR-05 to TC-FCR-10) | Behavioral |
| Discovery and awareness | 2 (TC-FCR-11, TC-FCR-12) | Mixed |
| **Total** | **13** | |
