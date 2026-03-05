---
resource_id: "84c6a4e0-552c-4f44-adaf-c76010a4bfd7"
resource_type: "rule"
resource_name: "test_design"
---
# Test Design: AI_CONTEXT_MODIFICATION_PROTOCOL (Filesystem Change Visualization)

**Rule**: `../AI_CONTEXT_MODIFICATION_PROTOCOL.md`
**Type**: Structural + Behavioral
**Scope**: Validates that the two-tier filesystem change visualization protocol is discoverable and followed

---

## Structural Tests

### TC-ACMP-01: Rule file exists with two-tier structure

**Steps**:
1. Check rule file exists at new path
2. Verify it contains Tier 1 (AI Context) and Tier 2 (General Filesystem) sections
3. Verify Tier 1 scope table lists all AI context file patterns
4. Verify Tier 2 scope table lists trigger conditions

**Expected**: Rule file has both tiers with complete scope definitions
**Type**: Structural

### TC-ACMP-02: Rule loaded on every API request

**Steps**:
1. Verify rule is in `0_every_api_request/` directory
2. Confirm CLAUDE.md Critical Rule #1 references this protocol
3. Check global `~/.claude/CLAUDE.md` also references it

**Expected**: Rule is discoverable at every level via CLAUDE.md chain
**Type**: Structural

### TC-ACMP-03: Tier 1 scope covers all AI context patterns

**Steps**:
1. Read the Tier 1 scope table
2. Verify patterns include: 0AGNOSTIC.md, .0agnostic/, .1merge/, CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .claude/, .cursor/, .codex/, .gemini/, .github/, *_rules/, *_prompts/, *_knowledge/, status.json, *.gab.jsonld, *.integration.md

**Expected**: All AI context file patterns are listed
**Type**: Structural

### TC-ACMP-04: Tier 2 triggers defined

**Steps**:
1. Read the Tier 2 scope table
2. Verify triggers: 2+ dirs, 3+ files, moving/renaming across dirs, entity scaffolding, user-requested restructuring
3. Verify exemptions: single file edit, single file creation, appends

**Expected**: Trigger conditions and exemptions are clearly defined
**Type**: Structural

### TC-ACMP-05: Diagram requirements specified

**Steps**:
1. Check for Diagram Requirements section
2. Verify it requires: full paths, directory tree, content summary, action type markers, annotations

**Expected**: Diagram format is fully specified
**Type**: Structural

---

## Behavioral Tests

### TC-ACMP-06: Agent shows Tier 1 diagram before AI context changes

**Setup**: Ask an agent to modify a .0agnostic/ file
**Check**: Agent presents a diagram with propagation chain BEFORE making changes
**Type**: Behavioral

### TC-ACMP-07: Agent shows Tier 2 diagram before structural filesystem changes

**Setup**: Ask an agent to create a new directory structure with 3+ files
**Check**: Agent presents a before/after diagram BEFORE creating directories/files
**Type**: Behavioral

### TC-ACMP-08: Agent does NOT show diagram for single file edits

**Setup**: Ask an agent to edit content within one existing file
**Check**: Agent proceeds without a diagram (Tier 2 exemption)
**Type**: Behavioral

### TC-ACMP-09: Agent waits for approval before proceeding

**Setup**: Trigger either Tier 1 or Tier 2
**Check**: Agent presents diagram and explicitly waits for user response before executing
**Type**: Behavioral

---

## Test Case Summary

| Category | Count | Type |
|----------|-------|------|
| Structural | 5 (TC-ACMP-01 to TC-ACMP-05) | Structural |
| Behavioral | 4 (TC-ACMP-06 to TC-ACMP-09) | Behavioral |
| **Total** | **9** | |
