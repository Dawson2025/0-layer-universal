---
resource_id: "7deecd2f-200d-483d-a0be-66cf1be5a7d9"
resource_type: "output"
resource_name: "test_design_06_source_to_avenue"
---
# Test Design: 06 Source of Truth to Avenue Flow

**Validates**: `stage_2_04_design/outputs/by_topic/06_source_of_truth_to_avenue_flow.md`
**Type**: Structural (bash)
**Script name**: `test_source_to_avenue.sh`

---

## What We're Testing

The .0agnostic/ numbering encodes information flow: 01-05 are content producers, 06 is delivery, 07+ is environment. Avenues are ordered by comprehensiveness. Authority flows one direction: source → avenues, never reverse.

---

## Test Cases

### TC-06-01: .0agnostic/ numbering consistency

**Steps**:
1. For each entity with `.0agnostic/`:
   - List subdirectories
   - Verify 01-05 are content dirs (knowledge, rules, protocols, episodic_memory, handoff_documents)
   - Verify 06 is delivery (context_avenue_web)
   - Verify 07+ is environment (setup_dependant) if present
2. Flag any entities with non-standard numbering or missing standard dirs

**Expected**: Numbering is consistent across all entities
**Type**: Structural

### TC-06-02: Source dirs (01-05) contain authored content

**Steps**:
1. For context_chain_system entity:
   - Check 01_knowledge/ has .md files (not just .gitkeep)
   - Check 02_rules/ has static/ and/or dynamic/ with rules
   - Check 03_protocols/ has protocol .md files
   - Check 04_episodic_memory/ has index.md or session files
   - Check 05_handoff_documents/ has incoming/ and outgoing/

**Expected**: At least 3 of 5 source dirs have real content (for an active entity)
**Type**: Structural

### TC-06-03: Delivery dir (06) contains generated/organized content

**Steps**:
1. Check `.0agnostic/06_context_avenue_web/` structure:
   - `00_context_avenue_web_registry/` exists (management hub)
   - `01_file_based/` exists with avenue subdirs
   - Avenue subdirs follow numbering (01_aalang through 08_hooks)
2. For file-based avenues present, verify they have content

**Expected**: Avenue web follows documented structure and numbering
**Type**: Structural

### TC-06-04: Avenue comprehensiveness ordering

**Steps**:
1. Read the avenue web registry (if exists) or scan avenue dirs
2. Verify ordering matches design:
   - 01 aalang (.gab.jsonld — most comprehensive)
   - 02 integration (.integration.md)
   - 03 auto_memory
   - 04 @import_references
   - 05 skills
   - 06 agents
   - 07 path_specific_rules
   - 08 hooks (least comprehensive)
3. Flag any avenues that are out of order or misnamed

**Expected**: Avenue numbering matches documented comprehensiveness order
**Type**: Structural

### TC-06-05: Authority direction — 06 doesn't contain source content

**Steps**:
1. Scan all files in `.0agnostic/06_context_avenue_web/`
2. Check for patterns that suggest source content (original prose, research notes, design decisions)
3. Generated files should have markers (auto-generated footers, script references, registry entries)

**Expected**: Avenue web dir contains only generated/organized/registry content, not original source material
**Note**: Heuristic test — looks for "auto-generated" markers and absence of original authoring patterns
**Type**: Structural (heuristic)

### TC-06-06: Context loading order — tool file loaded before .0agnostic/

**Steps**:
1. Read CLAUDE.md for entity
2. Verify it does NOT include full .0agnostic/ content inline (would violate loading order)
3. Verify it contains pointer references to .0agnostic/ (agent reads on demand)
4. Check CLAUDE.md line count is reasonable (<170 lines for entity)

**Expected**: CLAUDE.md is lean and pointer-based, not a dump of .0agnostic/ content
**Type**: Structural

### TC-06-07: Three zones are non-overlapping

**Steps**:
1. Categorize all .0agnostic/ content:
   - Zone 1 (hub): 0AGNOSTIC.md
   - Zone 2 (source): 01-05
   - Zone 3 (delivery): 06
2. Verify no source files (original knowledge, rules, protocols) live in 06
3. Verify no delivery files (generated avenues) live in 01-05

**Expected**: Clean separation between source (01-05) and delivery (06)
**Type**: Structural

---

## Coverage Gap Analysis

| Design Concept | Test Case | Status |
|---------------|-----------|--------|
| Numbering convention | TC-06-01 | New |
| Source dirs have content | TC-06-02 | New |
| Delivery dir structure | TC-06-03 | New |
| Comprehensiveness ordering | TC-06-04 | New |
| Authority direction | TC-06-05, TC-06-07 | New |
| Context loading order | TC-06-06 | New |
| Data-based avenues (09-13) | Not yet testable | Designed but not built |
