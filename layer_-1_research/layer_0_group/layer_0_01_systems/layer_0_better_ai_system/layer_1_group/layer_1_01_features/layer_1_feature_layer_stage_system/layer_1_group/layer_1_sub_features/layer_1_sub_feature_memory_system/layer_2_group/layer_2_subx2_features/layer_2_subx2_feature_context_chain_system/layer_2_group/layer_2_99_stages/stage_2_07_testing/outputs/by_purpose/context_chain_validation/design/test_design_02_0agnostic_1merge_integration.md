---
resource_id: "82df2119-6cea-4efb-a6ae-e59a8415b971"
resource_type: "output"
resource_name: "test_design_02_0agnostic_1merge_integration"
---
# Test Design: 02 0AGNOSTIC + .1merge Avenue Web Integration

**Validates**: `stage_2_04_design/outputs/by_topic/02_0agnostic_1merge_avenue_web_integration_design.md`
**Type**: Structural (bash) + Integration (bash)
**Script name**: `test_0agnostic_1merge_integration.sh`

---

<!-- section_id: "178ec3ab-e258-4c79-ab53-6a0e9b802287" -->
## What We're Testing

The end-to-end propagation pipeline: 0AGNOSTIC → agnostic-sync → .1merge → tool files → avenue web. The 3-tier merge model (synced → overrides → additions). Static-to-dynamic bridging. Reproducibility of generated files. Cross-tool application through .1merge scoping.

---

<!-- section_id: "6dfc9026-9215-4462-806a-c139b18421b6" -->
## Test Cases

<!-- section_id: "52a8b556-37e8-4a5c-9acc-90fe09f62372" -->
### TC-02-01: Propagation pipeline — content flows from 0AGNOSTIC to tool files

**Steps**:
1. Add a unique marker string to 0AGNOSTIC.md (e.g., in the Identity section, add a test-visible phrase)
2. Run agnostic-sync.sh
3. Verify the marker appears in CLAUDE.md
4. Verify the marker appears in AGENTS.md
5. Verify the marker appears in GEMINI.md and OPENAI.md
6. Remove the marker and re-run sync to restore state

**Expected**: Content authored in 0AGNOSTIC.md propagates to all 4 generated tool files
**Type**: Integration

<!-- section_id: "e36dfc4f-5ff1-452f-9560-9b1a7380c6bc" -->
### TC-02-02: .1merge 3-tier structure — dirs exist with correct naming

**Steps**:
1. For context_chain_system, check `.1merge/` exists
2. For each tool dir (`.1claude_merge/`, `.1agents_merge/`, etc.):
   - Verify `0_synced/` exists (tier 0 — from 0AGNOSTIC)
   - Verify `1_overrides/` exists (tier 1 — tool-specific modifications)
   - Verify `2_additions/` exists (tier 2 — tool-only content)
3. Verify naming is consistent across all tool merge dirs

**Expected**: 3-tier structure present for each tool's merge directory
**Note**: Extends existing test_1merge_structure with tier naming validation
**Type**: Structural

<!-- section_id: "9619897f-6b6e-49bd-a653-e04c4c4d1bd4" -->
### TC-02-03: .1merge scoping — additions appear only in target tool file

**Steps**:
1. Find entities where `.1merge/.1claude_merge/2_additions/` has content
2. Read the additions content
3. Verify it appears in CLAUDE.md but NOT in AGENTS.md or GEMINI.md
4. If `.1merge/.1agents_merge/2_additions/` has content:
   - Verify it appears in AGENTS.md but NOT in CLAUDE.md
5. Cross-check: no additions content leaks across tool boundaries

**Expected**: Each tool's additions stay scoped to that tool's generated file only
**Type**: Integration

<!-- section_id: "f33265bd-b3a4-4941-b30d-cbe5cee9a544" -->
### TC-02-04: .1merge overrides — tier 1 takes precedence over tier 0

**Steps**:
1. Find entities where `.1merge/.1claude_merge/1_overrides/` has content
2. Read the override content
3. Read the corresponding section in `0_synced/` (if exists)
4. Read the generated CLAUDE.md
5. Verify the override content appears (not the synced content) in the generated file

**Expected**: Override tier (1) takes precedence over synced tier (0) in generated output
**Note**: May need to create test fixtures if no overrides currently exist
**Type**: Integration

<!-- section_id: "4d29fe48-7ff0-472f-8409-fc25177ff1b2" -->
### TC-02-05: Generated file reproducibility — re-running sync produces identical output

**Steps**:
1. Read current CLAUDE.md, record checksum
2. Run agnostic-sync.sh
3. Read CLAUDE.md again, record checksum
4. Compare checksums

**Expected**: Running sync twice produces identical output (deterministic generation)
**Type**: Integration

<!-- section_id: "e591d1fc-2cbb-4682-96be-3929aaaa0bf2" -->
### TC-02-06: Static-to-dynamic bridge — CLAUDE.md contains pointers to dynamic resources

**Steps**:
1. Read CLAUDE.md for context_chain_system
2. Check for pointers to dynamic resources:
   - Skills references (`.claude/skills/` or skill names)
   - Episodic memory references (`.0agnostic/04_episodic_memory/`)
   - Knowledge references (`.0agnostic/01_knowledge/`)
   - Protocol references (`.0agnostic/03_protocols/`)
3. Count pointer types present

**Expected**: Static context (CLAUDE.md) bridges to dynamic context via at least 3 types of pointers
**Type**: Structural

<!-- section_id: "161a6a1f-b996-4f3e-a3a8-7b92ea6f97e2" -->
### TC-02-07: Canonical source traceability — generated files point back to source

**Steps**:
1. For each generated tool file (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md):
   - Verify footer contains "auto-generated from 0AGNOSTIC.md"
   - Verify footer contains "Do not edit directly"
   - Verify footer contains "edit 0AGNOSTIC.md instead"
2. For .cursorrules and copilot-instructions.md (if generated):
   - Verify similar traceability markers

**Expected**: Every generated file is traceable back to its canonical source
**Type**: Structural

<!-- section_id: "58e61332-f665-4489-ae44-909ca629fbd7" -->
### TC-02-08: Design constraint — no tool-specific logic in 0AGNOSTIC.md

**Steps**:
1. Read 0AGNOSTIC.md
2. Search for tool-specific patterns:
   - "CLAUDE.md" (ok as a reference, not ok as tool-specific logic)
   - "Claude Code" / "Cursor" / "Gemini" / "Copilot" as behavior targets
   - Tool-specific instructions like "use Read tool" or "use Bash"
3. Distinguish between references (acceptable) and tool-specific instructions (violation)
4. Report any tool-specific instructions found

**Expected**: 0AGNOSTIC.md is tool-agnostic — it references tools but doesn't contain tool-specific behavior
**Note**: Heuristic test — some references are acceptable, explicit tool instructions are not
**Type**: Structural (heuristic)

<!-- section_id: "99857d65-e435-4b57-9dbe-628088d4e0f1" -->
### TC-02-09: Cross-tool application — each tool has a merge directory

**Steps**:
1. List all subdirs in `.1merge/`
2. Verify at minimum:
   - `.1claude_merge/` exists (for Claude Code)
   - `.1agents_merge/` or equivalent exists (for Codex/OpenAI)
3. For each tool merge dir, verify the 3-tier structure (TC-02-02)
4. Count tools covered vs tools listed in design doc's cross-tool table

**Expected**: .1merge covers the primary tools with individual merge directories
**Type**: Structural

<!-- section_id: "b675ea10-7021-43f0-90c6-3776e0e453a4" -->
### TC-02-10: 8-avenue integration matrix — sources match design

**Steps**:
1. For each of the 8 MVP avenues, verify the source matches the design:
   - Avenue 1 (System prompt): sourced from 0AGNOSTIC + .1merge emissions
   - Avenue 2 (Path rules): sourced from .1merge tool rule projections OR .claude/rules/
   - Avenue 3 (Skills): sourced from 0AGNOSTIC protocols/skills mapped to .claude/skills/
   - Avenue 4 (@import): sourced from generated context files with path references
   - Avenue 5 (JSON-LD): sourced from orchestrator/agent/index .jsonld files
   - Avenue 6 (Integration.md): sourced from JSON-LD transpilation (jsonld-to-md.sh)
   - Avenue 7 (Episodic memory): sourced from .0agnostic/04_episodic_memory/
   - Avenue 8 (0AGNOSTIC fallback): sourced from 0AGNOSTIC.md directly
2. For each, verify the source artifact exists and has content

**Expected**: All 8 avenues have their documented sources present
**Type**: Structural

---

<!-- section_id: "6a3f7be0-e641-4d9a-9452-7f95a9fb5e6f" -->
## Coverage Gap Analysis

| Design Concept | Test Case | Status |
|---------------|-----------|--------|
| Propagation pipeline | TC-02-01 | New |
| 3-tier merge structure | TC-02-02 | Extends existing |
| .1merge scoping | TC-02-03 | New |
| Override precedence | TC-02-04 | New |
| Reproducibility | TC-02-05 | New |
| Static-to-dynamic bridge | TC-02-06 | New |
| Source traceability | TC-02-07 | New (extends existing) |
| Tool-agnostic 0AGNOSTIC | TC-02-08 | New (heuristic) |
| Cross-tool coverage | TC-02-09 | New |
| 8-avenue source matrix | TC-02-10 | New |
| Rollback strategy | Not testable | Designed but not implemented |
| Canonical class surfaces (knowledge, principles, rules, protocols) | Covered by TC-06-01, TC-06-02 | Cross-reference |
