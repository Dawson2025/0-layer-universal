---
resource_id: "400a70c0-21f4-4623-911c-46505c433208"
resource_type: "output"
resource_name: "test_design_rule_compliance_file_change_reporting"
---
# Test Design: Rule Compliance — File Change Reporting

**Validates**: `.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING.md`
**Type**: Behavioral (agent execution) + Structural (bash)
**Scope**: Tests whether AI agents discover, load, and comply with the file change reporting rule across the context chain

---

<!-- section_id: "d0927d90-11ea-4da2-a821-8898ffbd33ba" -->
## What We're Testing

The file change reporting rule (`I0_FILE_CHANGE_REPORTING.md`) requires that agents report all filesystem changes at the end of every turn using full absolute paths. This test design validates three aspects:

1. **Discovery**: Does the rule reach the agent through the context chain? (hot rule promotion → CLAUDE.md cascade → agent reads it)
2. **Loading**: Does the agent's loaded context actually contain the rule text?
3. **Compliance**: When the agent modifies files, does it produce the required report with full absolute paths?

These are primarily **behavioral tests** — they require actual agent execution or simulated agent responses to validate. Some structural preconditions can be verified with bash scripts.

---

<!-- section_id: "f5b16272-2274-43ae-990d-2e805ad36b21" -->
## Structural Precondition Tests

<!-- section_id: "8f6e9778-5a24-4f40-9ac5-eba7fa8ef0ec" -->
### TC-FCR-01: Rule file exists with correct frontmatter

**Steps**:
1. Check `.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING.md` exists at the root level
2. Verify YAML frontmatter contains:
   - `promote: hot`
   - `hot_summary:` with text mentioning "full absolute paths"
   - `hot_trigger:` with text mentioning "modifies files"
3. Verify body contains the rule format, priority order, and rules list

**Expected**: Rule file exists with hot promotion frontmatter and complete rule specification
**Type**: Structural

<!-- section_id: "5157561e-6e2f-459d-9384-eced8067c6df" -->
### TC-FCR-02: Hot rule appears in root CLAUDE.md promoted rules

**Steps**:
1. Read `/home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md`
2. Search for `## Promoted Rules` section
3. Verify the promoted rules table contains a row matching:
   - Trigger: "Any turn that modifies files"
   - Summary: mentions "full absolute paths" and "NEVER abbreviated"
4. Verify the reference path is correct: `.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING.md`

**Expected**: The hot_summary from the rule's frontmatter appears in the root CLAUDE.md promoted rules table
**Type**: Structural

<!-- section_id: "642881c2-0f6a-42da-b87b-73b6099b8ba2" -->
### TC-FCR-03: CLAUDE.md cascade delivers rule to all levels

**Steps**:
1. Starting from root CLAUDE.md, trace the cascade down to context_chain_system:
   - `/home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md`
   - `.../layer_-1_research/CLAUDE.md`
   - `.../layer_-1_better_ai_system/CLAUDE.md`
   - `.../layer_0_group/CLAUDE.md`
   - `.../layer_0_features/CLAUDE.md`
   - `.../layer_0_feature_layer_stage_system/CLAUDE.md`
   - `.../layer_1_sub_feature_agent_delegation_system/CLAUDE.md`
   - `.../layer_2_subx2_feature_memory_system/CLAUDE.md`
   - `.../layer_3_subx3_feature_context_chain_system/CLAUDE.md`
2. Claude Code loads ALL CLAUDE.md files from root to cwd — verify root CLAUDE.md (which has the promoted rule) is in this chain
3. Count how many CLAUDE.md files are in the chain

**Expected**: The root CLAUDE.md with the promoted rule is always the first file in the cascade, ensuring every agent at every level sees the rule
**Note**: Claude Code's cascade walk loads all CLAUDE.md from filesystem root to cwd — the rule just needs to be in the root
**Type**: Structural

<!-- section_id: "5755eaa5-470f-4636-b8eb-1c5193b91964" -->
### TC-FCR-04: Rule references in ~/.claude/CLAUDE.md (global)

**Steps**:
1. Read `~/.claude/CLAUDE.md` (user's global Claude Code config)
2. Search for file change reporting references
3. Verify it mentions the rule or points to the full rule file
4. Check if the hot_summary or equivalent text appears

**Expected**: The global CLAUDE.md also references the file change reporting rule (belt-and-suspenders with cascade)
**Type**: Structural

---

<!-- section_id: "21a1ff57-fe24-4cec-be62-c1f4ec4d0055" -->
## Behavioral Compliance Tests

These tests require actual agent execution. They can be run by:
- Spawning a test agent via Task tool and examining its response
- Reviewing session transcripts for compliance
- Creating a compliance checker script that parses agent output

<!-- section_id: "4e754c88-5375-4082-a62a-273d8b2b37f4" -->
### TC-FCR-05: Agent reports files when creating new files

**Setup**:
1. Spawn a test agent at any level in the hierarchy
2. Ask it to create a new file (e.g., "Create a file at outputs/test_file.md with content 'test'")
3. Examine the agent's response

**Check**:
1. Response ends with a file change report section
2. Report lists the created file under **Added**
3. The path is a full absolute path starting from `/home/dawson/...`
4. Path is NOT abbreviated (no `...` in the middle, no relative path, no basename-only)

**Expected**: Agent produces a file change report with full absolute path for the added file
**Type**: Behavioral

<!-- section_id: "fa6641d0-b9cf-489a-8d3f-8d792cfb326b" -->
### TC-FCR-06: Agent reports files when editing existing files

**Setup**:
1. Spawn a test agent
2. Ask it to edit an existing file (e.g., "Add a comment to 0INDEX.md")
3. Examine the agent's response

**Check**:
1. Response ends with a file change report section
2. Report lists the edited file under **Updated**
3. The path is a full absolute path starting from `/home/dawson/...`
4. Path is NOT abbreviated

**Expected**: Agent produces a file change report with full absolute path for the updated file
**Type**: Behavioral

<!-- section_id: "0b7aed6c-6563-4860-aceb-fe9c27deb469" -->
### TC-FCR-07: Agent reports multiple file changes correctly

**Setup**:
1. Spawn a test agent
2. Ask it to perform a task that modifies 3+ files (e.g., "Update stage_report.md and 0INDEX.md and create a new summary file")
3. Examine the agent's response

**Check**:
1. Response ends with a file change report section
2. ALL modified files are listed (not just some)
3. Files are grouped by operation type (Added, Updated, etc.)
4. Priority order is correct (Added first, then Updated, then Moved, then Removed)
5. Every path is full absolute starting from `/home/dawson/...`

**Expected**: Agent correctly reports all file changes with proper grouping, ordering, and full absolute paths
**Type**: Behavioral

<!-- section_id: "4816b5bb-4eda-46aa-b6cd-dfddead514ca" -->
### TC-FCR-08: Agent does NOT report when no files changed

**Setup**:
1. Spawn a test agent
2. Ask it a question that requires no file changes (e.g., "What stage is currently active?")
3. Examine the agent's response

**Check**:
1. Response does NOT contain a file change report section
2. No "Files changed this turn" text when nothing changed

**Expected**: Agent omits the report when no files were modified (rule says "no report is needed")
**Type**: Behavioral

<!-- section_id: "c3b56960-bd7a-470d-9f2b-50082462f9da" -->
### TC-FCR-09: Agent uses full absolute paths, never abbreviated

**Setup**:
1. Spawn a test agent at a deep level (e.g., context_chain_system stage_3_07_testing)
2. Ask it to create or modify a file
3. Examine the path format in the file change report

**Check**:
1. Path starts with `/home/dawson/dawson-workspace/code/0_layer_universal/`
2. Path includes ALL intermediate directories (no `...` abbreviation)
3. Path ends with the actual filename
4. Even for very long paths (300+ characters), the full path is shown

**Bad patterns to check for**:
- `stages_manager_pattern.md` (basename only)
- `.../stage_1_04_design/outputs/design_decisions/stages_manager_pattern.md` (tail only)
- `stage_1_04_design/outputs/design_decisions/stages_manager_pattern.md` (relative path)
- `/home/dawson/.../stages_manager_pattern.md` (abbreviated middle)

**Expected**: Full absolute path with zero abbreviation, even when paths are very long
**Type**: Behavioral

<!-- section_id: "d793ad1c-9601-497e-bb29-0da2398d866f" -->
### TC-FCR-10: Sub-agent file changes are reported by delegating agent

**Setup**:
1. Spawn a manager agent that delegates file-modifying work to a sub-agent via Task tool
2. Sub-agent creates/modifies files and returns
3. Examine the manager agent's response after sub-agent returns

**Check**:
1. Manager agent reports the sub-agent's file changes in its own response
2. Paths are full absolute
3. Report attributes changes to the sub-agent's work (or includes them in the overall report)

**Expected**: Delegating agent includes sub-agent file changes in its own end-of-turn report
**Note**: Rule #6 states "For agent-delegated work, the delegating agent reports the summary when the sub-agent returns"
**Type**: Behavioral

---

<!-- section_id: "db7a8b43-86f8-48ca-acf8-84bfa6f6db1f" -->
## Discovery Chain Test

<!-- section_id: "9f129283-d1d6-4de9-b59b-9cb9de673014" -->
### TC-FCR-11: Rule discovery temperature — is the rule Hot, Warm, or Cold?

**Steps**:
1. Check if the rule is Hot (loaded automatically):
   - Verify `promote: hot` in frontmatter ✓
   - Verify hot_summary appears in CLAUDE.md Promoted Rules ✓
   - If both: rule is Hot — agents see it without any action
2. Check if agents can find the full rule if they need more detail:
   - The hot_summary references the full rule path
   - An agent can Read the full rule file on-demand
3. Verify the discovery chain:
   - Root CLAUDE.md → Promoted Rules table → hot_summary text → link to full rule file

**Expected**: The rule is at Hot temperature — agents see the summary automatically in every session without needing to search for it. The full rule is discoverable via the reference path in the hot_summary.
**Type**: Structural + Behavioral

<!-- section_id: "c6d796ea-bf7a-4a25-aff6-0dc1eb171ab8" -->
### TC-FCR-12: Agent acknowledges rule existence in its loaded context

**Setup**:
1. Spawn a test agent
2. Ask it: "What rules apply to file change reporting?"
3. Examine the agent's response

**Check**:
1. Agent references the file change reporting rule
2. Agent can name the rule file path or describe its requirements
3. Agent mentions "full absolute paths" as a requirement

**Expected**: Agent is aware of the rule's existence and can describe its requirements
**Type**: Behavioral

---

<!-- section_id: "0607c796-4603-413e-ab8c-a24eb8448287" -->
## Compliance Scoring Framework

For systematic evaluation across many sessions, use this scoring rubric:

| Criterion | Score | Description |
|-----------|-------|-------------|
| Report present | 0 or 1 | Did the agent include a file change report when files were modified? |
| All files listed | 0 or 1 | Are ALL modified files in the report (not just some)? |
| Full absolute paths | 0 or 1 | Does every path start from `/home/` with no abbreviation? |
| Correct grouping | 0 or 1 | Are files grouped by operation type (Added/Updated/Moved/Removed)? |
| Correct ordering | 0 or 1 | Is priority order correct (Added > Updated > Moved > Removed)? |
| End of response | 0 or 1 | Does the report appear at the end, after main content? |
| **Total** | **0-6** | Perfect compliance = 6/6 |

**Passing threshold**: 5/6 (allowing minor ordering issues)
**Critical failures**: Report absent (0/6) or abbreviated paths (paths score = 0)

---

<!-- section_id: "cc872104-6948-4da3-aade-9bd8a1046239" -->
## Coverage Gap Analysis

| Rule Aspect | Test Case | Status |
|------------|-----------|--------|
| Rule file structure | TC-FCR-01 | New (Structural) |
| Hot promotion to CLAUDE.md | TC-FCR-02 | New (Structural) |
| CLAUDE.md cascade delivery | TC-FCR-03 | New (Structural) |
| Global config reference | TC-FCR-04 | New (Structural) |
| Create file compliance | TC-FCR-05 | New (Behavioral) |
| Edit file compliance | TC-FCR-06 | New (Behavioral) |
| Multi-file compliance | TC-FCR-07 | New (Behavioral) |
| No-change omission | TC-FCR-08 | New (Behavioral) |
| Full path enforcement | TC-FCR-09 | New (Behavioral) |
| Sub-agent delegation | TC-FCR-10 | New (Behavioral) |
| Discovery temperature | TC-FCR-11 | New (Structural + Behavioral) |
| Agent awareness | TC-FCR-12 | New (Behavioral) |
| 10+ files grouping | Not yet designed | Rule #5 edge case |
| Cross-tool compliance (Codex, Gemini) | Not yet designed | Different tools, same rule |

<!-- section_id: "80bc6ec7-dec0-4175-86e9-ab6a76ed33a0" -->
## Test Case Summary

| Category | Count | Type |
|----------|-------|------|
| Structural preconditions | 4 (TC-FCR-01 to TC-FCR-04) | Structural |
| Behavioral compliance | 6 (TC-FCR-05 to TC-FCR-10) | Behavioral |
| Discovery and awareness | 2 (TC-FCR-11, TC-FCR-12) | Mixed |
| **Total** | **12** | **4 structural, 6 behavioral, 2 mixed** |
