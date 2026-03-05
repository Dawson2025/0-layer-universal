---
resource_id: "adfb2076-7522-4ef5-a2a6-b040885be7c0"
resource_type: "output"
resource_name: "test_design_03_propagation_chain"
---
# Test Design: 03 Propagation Chain Architecture

**Validates**: `stage_2_04_design/outputs/by_topic/03_propagation_chain_architecture.md`
**Type**: Structural (bash) + Integration (bash)
**Script name**: `test_propagation_chain.sh`

---

<!-- section_id: "9e6108bf-658e-445f-bc46-6ab191930454" -->
## What We're Testing

The 4-layer propagation chain: Knowledge (.0agnostic/ 01-05) → Agnostic Source (0AGNOSTIC.md) → Tool Files (CLAUDE.md etc) → Agent Action (runtime). Each layer must exist, content must flow directionally, and chain integrity rules must hold.

---

<!-- section_id: "54333e9b-a2b0-44ee-a018-b63130dce688" -->
## Test Cases

<!-- section_id: "5dfe15fe-6540-4a98-8529-6def385ac64a" -->
### TC-03-01: Layer 1 (Knowledge) exists and has content

**Precondition**: Entity has `.0agnostic/` directory
**Steps**:
1. For each entity with 0AGNOSTIC.md in the hierarchy, check `.0agnostic/` exists
2. Check at least one of 01-05 subdirs has content files (not just .gitkeep)

**Expected**: Every entity with 0AGNOSTIC.md has at least one content source in .0agnostic/01-05
**Type**: Structural

<!-- section_id: "ac70b4b4-32b1-4dc8-8c48-ac35a052ca64" -->
### TC-03-02: Layer 2 (Agnostic Source) references Layer 1

**Precondition**: Entity has 0AGNOSTIC.md
**Steps**:
1. Read 0AGNOSTIC.md
2. Check for references to `.0agnostic/` (patterns: `.0agnostic/`, `01_knowledge`, `02_rules`, `03_protocols`, `Resources Available`, `Navigation`)
3. Count reference density

**Expected**: Every 0AGNOSTIC.md references .0agnostic/ content at least once
**Metric**: Reference count per 0AGNOSTIC.md (flag if 0)
**Type**: Structural

<!-- section_id: "2722e226-2803-4fb6-a729-b00e2e8b9fcf" -->
### TC-03-03: Layer 3 (Tool Files) generated from Layer 2

**Precondition**: Entity has 0AGNOSTIC.md and agnostic-sync.sh is accessible
**Steps**:
1. Run `agnostic-sync.sh` against entity
2. Check CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md all exist
3. Verify each has `auto-generated from 0AGNOSTIC.md` footer
4. Verify Identity section content matches between 0AGNOSTIC.md STATIC and CLAUDE.md

**Expected**: All 4 tool files exist, have footer, content derived from 0AGNOSTIC.md
**Type**: Integration (extends existing test_agnostic_sync)

<!-- section_id: "80b5a7b4-a28a-4c27-952c-87c5ddf03760" -->
### TC-03-04: Layer 3 includes .1merge overrides

**Precondition**: Entity has `.1merge/.1claude_merge/2_additions/` with content
**Steps**:
1. Find entities with .1merge additions content
2. Run agnostic-sync.sh
3. Verify CLAUDE.md contains the additions content
4. Verify AGENTS.md does NOT contain Claude-specific additions (scoped correctly)

**Expected**: .1merge additions appear in correct tool file only
**Type**: Integration

<!-- section_id: "17d8c6e9-3973-49eb-a466-631aa31f3d13" -->
### TC-03-05: Chain integrity — no orphan tool files

**Precondition**: Scan all entities
**Steps**:
1. Find all CLAUDE.md files in the hierarchy
2. For each, check a corresponding 0AGNOSTIC.md exists in the same directory
3. Flag any CLAUDE.md without a source 0AGNOSTIC.md

**Expected**: Every CLAUDE.md (with auto-generated footer) has a corresponding 0AGNOSTIC.md
**Type**: Structural

<!-- section_id: "73ad9cce-a0f7-4ce7-8720-0c14c474dc3a" -->
### TC-03-06: Chain integrity — no orphan 0AGNOSTIC.md files

**Precondition**: Scan all entities
**Steps**:
1. Find all 0AGNOSTIC.md files
2. For each, check CLAUDE.md exists (indicating sync has been run)
3. Flag any 0AGNOSTIC.md without generated tool files

**Expected**: Every 0AGNOSTIC.md has generated tool files (or is explicitly exempt)
**Type**: Structural

<!-- section_id: "d3301035-1347-4d8c-bf8d-c75a96f2b10b" -->
### TC-03-07: Unidirectional flow — tool files don't contain edit instructions

**Steps**:
1. Read each generated CLAUDE.md
2. Verify footer says "Do not edit directly"
3. Verify no patterns like "Edit this file" or "modify CLAUDE.md" in generated tool files

**Expected**: Generated files consistently direct edits to 0AGNOSTIC.md
**Type**: Structural

---

<!-- section_id: "30f58abb-cb2b-4dba-afc3-50671e9e2426" -->
## Coverage Gap Analysis

| Design Concept | Test Case | Status |
|---------------|-----------|--------|
| 4-layer chain exists | TC-03-01 through TC-03-04 | New |
| Chain integrity rules | TC-03-05, TC-03-06 | New |
| Unidirectional flow | TC-03-07 | New |
| .1merge 3-tier merge | TC-03-04 | New (extends existing) |
| Layer 4 (Agent Action) | Not testable structurally | Covered by skill_discovery_chain |
