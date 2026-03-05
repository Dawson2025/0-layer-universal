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

<!-- section_id: "ff6af3fb-be30-4001-a23e-49c8b80d8683" -->
## Structural Tests

<!-- section_id: "5c5d87c7-7a26-45a6-a748-97a5b60bf83a" -->
### TC-ACMP-01: Rule file exists with two-tier structure

**Steps**:
1. Check rule file exists at new path
2. Verify it contains Tier 1 (AI Context) and Tier 2 (General Filesystem) sections
3. Verify Tier 1 scope table lists all AI context file patterns
4. Verify Tier 2 scope table lists trigger conditions

**Expected**: Rule file has both tiers with complete scope definitions
**Type**: Structural

<!-- section_id: "d5bcf219-54ea-4757-824f-fe7867cf59c6" -->
### TC-ACMP-02: Rule loaded on every API request

**Steps**:
1. Verify rule is in `0_every_api_request/` directory
2. Confirm CLAUDE.md Critical Rule #1 references this protocol
3. Check global `~/.claude/CLAUDE.md` also references it

**Expected**: Rule is discoverable at every level via CLAUDE.md chain
**Type**: Structural

<!-- section_id: "1c306ab1-f790-42dc-aebe-20932670173a" -->
### TC-ACMP-03: Tier 1 scope covers all AI context patterns

**Steps**:
1. Read the Tier 1 scope table
2. Verify patterns include: 0AGNOSTIC.md, .0agnostic/, .1merge/, CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .claude/, .cursor/, .codex/, .gemini/, .github/, *_rules/, *_prompts/, *_knowledge/, status.json, *.gab.jsonld, *.integration.md

**Expected**: All AI context file patterns are listed
**Type**: Structural

<!-- section_id: "b3889ccb-20ee-4fb8-aee3-708b7c4cec8a" -->
### TC-ACMP-04: Tier 2 triggers defined

**Steps**:
1. Read the Tier 2 scope table
2. Verify triggers: 2+ dirs, 3+ files, moving/renaming across dirs, entity scaffolding, user-requested restructuring
3. Verify exemptions: single file edit, single file creation, appends

**Expected**: Trigger conditions and exemptions are clearly defined
**Type**: Structural

<!-- section_id: "4a4d51e0-7b81-4340-bbfb-b11b6a6dc39f" -->
### TC-ACMP-05: Diagram requirements specified

**Steps**:
1. Check for Diagram Requirements section
2. Verify it requires: full paths, directory tree, content summary, action type markers, annotations

**Expected**: Diagram format is fully specified
**Type**: Structural

---

<!-- section_id: "64b05441-e24a-414b-99d4-689d2ce87836" -->
## Behavioral Tests

<!-- section_id: "33c419de-75fe-4ae1-bdfc-c7ef2aea5a7e" -->
### TC-ACMP-06: Agent shows Tier 1 diagram before AI context changes

**Setup**: Ask an agent to modify a .0agnostic/ file
**Check**: Agent presents a diagram with propagation chain BEFORE making changes
**Type**: Behavioral

<!-- section_id: "6a723fd8-4bfc-4084-a185-3f3c75745d07" -->
### TC-ACMP-07: Agent shows Tier 2 diagram before structural filesystem changes

**Setup**: Ask an agent to create a new directory structure with 3+ files
**Check**: Agent presents a before/after diagram BEFORE creating directories/files
**Type**: Behavioral

<!-- section_id: "85be8d06-118b-4bf1-9874-d36834c7a1a4" -->
### TC-ACMP-08: Agent does NOT show diagram for single file edits

**Setup**: Ask an agent to edit content within one existing file
**Check**: Agent proceeds without a diagram (Tier 2 exemption)
**Type**: Behavioral

<!-- section_id: "12b97a77-3fca-43f7-8299-3b650663d870" -->
### TC-ACMP-09: Agent waits for approval before proceeding

**Setup**: Trigger either Tier 1 or Tier 2
**Check**: Agent presents diagram and explicitly waits for user response before executing
**Type**: Behavioral

---

<!-- section_id: "825eabc3-4ad7-4fd5-8796-a6c4536b9d38" -->
## Test Case Summary

| Category | Count | Type |
|----------|-------|------|
| Structural | 5 (TC-ACMP-01 to TC-ACMP-05) | Structural |
| Behavioral | 4 (TC-ACMP-06 to TC-ACMP-09) | Behavioral |
| **Total** | **9** | |
