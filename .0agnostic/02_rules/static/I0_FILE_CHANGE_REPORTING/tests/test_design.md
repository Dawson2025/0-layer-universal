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

## Structural Precondition Tests

### TC-FCR-01: Rule file exists with correct frontmatter

**Steps**:
1. Check rule file exists at `.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING/I0_FILE_CHANGE_REPORTING.md`
2. Verify YAML frontmatter contains `promote: hot`, `hot_summary:` mentioning "full absolute paths", `hot_trigger:`
3. Verify body contains the two-part rule format (inline + summary)

**Expected**: Rule file exists with hot promotion frontmatter and complete specification
**Type**: Structural

### TC-FCR-02: Hot rule appears in root CLAUDE.md promoted rules

**Steps**:
1. Read root CLAUDE.md
2. Search for Promoted Rules section
3. Verify table contains row matching trigger "Any turn that modifies files" and summary mentioning "full absolute paths"

**Expected**: Hot summary from rule frontmatter appears in CLAUDE.md Promoted Rules table
**Type**: Structural

### TC-FCR-03: CLAUDE.md cascade delivers rule to all levels

**Steps**:
1. Starting from root CLAUDE.md, verify it exists at `/home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md`
2. Claude Code loads ALL CLAUDE.md files from root to cwd — verify root is in chain
3. Count CLAUDE.md files in the chain

**Expected**: Root CLAUDE.md with promoted rule is always first in cascade
**Type**: Structural

### TC-FCR-04: Rule references in ~/.claude/CLAUDE.md (global)

**Steps**:
1. Read `~/.claude/CLAUDE.md`
2. Search for file change reporting references
3. Verify it mentions the rule or points to the full rule file

**Expected**: Global CLAUDE.md also references the rule
**Type**: Structural

### TC-FCR-13: Home directory copy in sync

**Steps**:
1. Diff repo copy vs `~/.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING/I0_FILE_CHANGE_REPORTING.md`
2. Files should be identical

**Expected**: Home directory copy matches repo copy exactly
**Type**: Structural

---

## Behavioral Compliance Tests

### TC-FCR-05: Agent reports files when creating new files
### TC-FCR-06: Agent reports files when editing existing files
### TC-FCR-07: Agent reports multiple file changes correctly
### TC-FCR-08: Agent does NOT report when no files changed
### TC-FCR-09: Agent uses full absolute paths, never abbreviated
### TC-FCR-10: Sub-agent file changes reported by delegating agent

(See full behavioral test descriptions in the agent_delegation_system stage_1_07_testing test design for detailed setup/check/expected for each)

---

## Discovery Chain Tests

### TC-FCR-11: Rule discovery temperature (Hot)
### TC-FCR-12: Agent acknowledges rule existence

---

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

## Test Case Summary

| Category | Count | Type |
|----------|-------|------|
| Structural preconditions | 5 (TC-FCR-01 to TC-FCR-04, TC-FCR-13) | Structural |
| Behavioral compliance | 6 (TC-FCR-05 to TC-FCR-10) | Behavioral |
| Discovery and awareness | 2 (TC-FCR-11, TC-FCR-12) | Mixed |
| **Total** | **13** | |
