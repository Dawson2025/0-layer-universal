---
resource_id: "da09d4fe-8004-41de-81d4-cf7d058210a5"
resource_type: "output"
resource_name: "test_design_08_discovery_temperatures"
---
# Test Design: 08 Discovery Temperature Model

**Validates**: `stage_2_04_design/outputs/by_topic/08_discovery_temperature_model.md`
**Type**: Structural (bash) + Behavioral (manual/agent)
**Script name**: `test_discovery_temperatures.sh`

---

<!-- section_id: "fcc1d120-4413-49b6-8f0b-45bb25bf4a86" -->
## What We're Testing

Three context temperatures: Hot (always loaded via CLAUDE.md), Warm (on directory entry via .claude/rules/), Cold (on demand/trigger). The hot rule promotion system. PostToolUse hooks. Three-layer defense in depth. Token budgets.

---

<!-- section_id: "63cef9ef-c0f9-44dd-a93a-46d0caa02f8e" -->
## Test Cases

<!-- section_id: "07041573-e5c9-4512-b534-9f361da0437e" -->
### TC-08-01: Hot context — CLAUDE.md contains required sections

**Steps**:
1. For each entity CLAUDE.md in the chain:
   - Verify `## Identity` section exists (entity identity)
   - Verify `## Triggers` section exists (navigation pointers)
   - Verify auto-generated footer exists
2. For root CLAUDE.md:
   - Verify critical rules present (Modification Protocol, Stage Completeness, Commit/Push)
3. For entities with promoted rules:
   - Verify `## Promoted Rules` table exists

**Expected**: Hot context always contains identity, triggers, critical rules, promoted rules
**Type**: Structural

<!-- section_id: "7bc8a536-ec2b-4436-8929-d35a563cd3d4" -->
### TC-08-02: Hot context — token budget compliance

**Steps**:
1. For each entity CLAUDE.md:
   - Count total lines
   - Flag if >170 lines (entity budget target)
2. For the full CLAUDE.md cascade (root to context_chain_system):
   - Sum all CLAUDE.md line counts
   - Flag if total >400 lines (chain budget target)

**Expected**: Individual CLAUDE.md files <170 lines, total chain <400 lines
**Note**: These are targets, not hard limits — report violations as warnings
**Type**: Structural

<!-- section_id: "03f3b1fe-adc5-4417-bdaa-2e1800814987" -->
### TC-08-03: Warm context — .claude/rules/ files have path matchers

**Steps**:
1. For root `.claude/rules/`:
   - List all .md files
   - For each, check it describes a path scope (e.g., "Applies to: *.0agnostic/**")
   - Verify the described scope matches actual directory patterns
2. For entity `.claude/rules/`:
   - Verify rules exist
   - Verify they are scoped (not universal — universal goes in hot)

**Expected**: Warm rules are scoped to specific paths, not universal
**Type**: Structural

<!-- section_id: "c8755612-63d1-480c-9740-ddc4588a79db" -->
### TC-08-04: Warm context — rules fire on correct paths

**Steps**:
1. Read `agnostic-edits.md` rule (known warm rule)
2. Verify it specifies `.0agnostic/**` as its scope
3. Verify it contains actionable instructions for that path
4. Read `research-context.md` rule
5. Verify it targets research directories

**Expected**: Warm rules have clear path scopes that match their content
**Type**: Structural

<!-- section_id: "de6963cc-557d-4038-ba50-ec0405327f5e" -->
### TC-08-05: Cold context — .0agnostic/ resources exist and are organized

**Steps**:
1. For context_chain_system:
   - Check `.0agnostic/01_knowledge/` has knowledge docs
   - Check `.0agnostic/02_rules/dynamic/` has trigger-based rules
   - Check `.0agnostic/03_protocols/` has procedure docs
   - Check `.0agnostic/04_episodic_memory/` has memory structure
   - Check `.claude/skills/` has SKILL.md files with WHEN/WHEN NOT
2. For each cold resource, verify it is NOT inlined in CLAUDE.md (stays cold)

**Expected**: Cold content exists in organized locations, not duplicated into hot context
**Type**: Structural

<!-- section_id: "4af56253-927f-4caf-90b0-6f17fe3ddd50" -->
### TC-08-06: Cold context — skills have WHEN conditions

**Steps**:
1. Find all `.claude/skills/*/SKILL.md` files
2. For each, verify:
   - `## WHEN` section exists with trigger conditions
   - `## WHEN NOT` section exists with exclusion conditions
3. Verify WHEN conditions are specific enough (not "always")

**Expected**: Skills are properly gated with specific trigger conditions
**Type**: Structural

<!-- section_id: "ef9b94b9-1fee-42ed-9a4e-97bf79bcfa92" -->
### TC-08-07: Hot rule promotion — full pipeline

**Steps**:
1. Find a rule with `promote: hot` frontmatter
2. Verify its `hot_trigger` and `hot_summary` are defined
3. Run agnostic-sync.sh
4. Verify CLAUDE.md has a Promoted Rules table
5. Verify the rule appears in the table
6. Read the full rule from the path in the table
7. Verify the full rule file matches the promoted one

**Expected**: End-to-end promotion: rule file → frontmatter → sync → CLAUDE.md table → path back to full rule
**Type**: Integration

<!-- section_id: "5f9257e2-c631-4e42-8510-4a68fd1fa7aa" -->
### TC-08-08: PostToolUse hook — agnostic-edit-guard exists

**Steps**:
1. Verify `.0agnostic/06_context_avenue_web/01_file_based/08_hooks/scripts/agnostic-edit-guard.sh` exists
2. Verify it is executable
3. Verify `.claude/settings.json` has a PostToolUse hook entry for it
4. Test with a .0agnostic/ path: verify it returns `additionalContext`
5. Test with a non-.0agnostic/ path: verify it returns empty JSON

**Expected**: Hook fires for .0agnostic/ edits and returns context, stays silent for other paths
**Type**: Integration

<!-- section_id: "b53dcd72-4c73-4a3e-842c-3fab103cf422" -->
### TC-08-09: Three-layer defense — all layers present for .0agnostic/ protection

**Steps**:
1. **Layer 1 (Hot)**: Check CLAUDE.md Promoted Rules table contains "modifying .0agnostic/" trigger
2. **Layer 2 (Warm)**: Check `.claude/rules/agnostic-edits.md` exists and scopes to `.0agnostic/**`
3. **Layer 3 (Hook)**: Check PostToolUse hook for .0agnostic/ edit guard exists in settings.json

**Expected**: All three layers are configured and active
**Type**: Structural

<!-- section_id: "f5570117-c8f8-4b48-9ab5-bb7bc528cef1" -->
### TC-08-10: Temperature assignment — no hot content that should be cold

**Steps**:
1. Read CLAUDE.md for context_chain_system
2. Check for content that should be cold (detailed knowledge, full protocols, long code blocks)
3. Flag CLAUDE.md sections that are >20 lines (these might be too detailed for hot)
4. Verify that detailed content has pointers ("Full rule: path/to/file.md") rather than inline content

**Expected**: Hot context is lean — pointers to cold, not inline cold content
**Type**: Structural (heuristic)

---

<!-- section_id: "40f2764f-0290-4253-891c-eaa8c15aaf7f" -->
## Coverage Gap Analysis

| Design Concept | Test Case | Status |
|---------------|-----------|--------|
| Hot context structure | TC-08-01 | New |
| Token budget | TC-08-02 | New |
| Warm context scoping | TC-08-03, TC-08-04 | New |
| Cold context organization | TC-08-05, TC-08-06 | New |
| Hot rule promotion pipeline | TC-08-07 | New |
| PostToolUse hook | TC-08-08 | New |
| Three-layer defense | TC-08-09 | New |
| Temperature assignment heuristic | TC-08-10 | New |
| Empirical agent discovery | Covered by test_skill_discovery_chain.md | Existing |
