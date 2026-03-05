---
resource_id: "7cd5c20b-666f-4a2c-bf1c-20c241fad408"
resource_type: "output"
resource_name: "test_design_02_0agnostic_1merge_integration"
---
# Test Design: 02 0AGNOSTIC + .1merge Avenue Web Integration

**Validates**: `stage_2_04_design/outputs/by_topic/02_0agnostic_1merge_avenue_web_integration_design.md`
**Type**: Structural (bash) + Integration (bash)
**Script name**: `test_0agnostic_1merge_integration.sh`

---

<!-- section_id: "c8cc7c59-32a3-499d-8c5b-9adba4ecad7e" -->
## What We're Testing

The end-to-end propagation pipeline: 0AGNOSTIC → agnostic-sync → .1merge → tool files → avenue web. The 3-tier merge model (synced → overrides → additions). Static-to-dynamic bridging. Reproducibility of generated files. Cross-tool application through .1merge scoping.

---

<!-- section_id: "f1e0989d-8960-4c56-b16b-4f23da176364" -->
## Test Cases

<!-- section_id: "81980a58-bcd5-42b5-89c5-d1650b62ee87" -->
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

<!-- section_id: "a406944d-db03-4851-8408-d53095b3c047" -->
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

<!-- section_id: "ed46860a-e523-4078-b55d-eb16d425a0c0" -->
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

<!-- section_id: "3a776f02-1aad-4202-8ee5-961c4d9e6edf" -->
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

<!-- section_id: "597f7ed1-1810-4d68-b860-c41a8d967b2d" -->
### TC-02-05: Generated file reproducibility — re-running sync produces identical output

**Steps**:
1. Read current CLAUDE.md, record checksum
2. Run agnostic-sync.sh
3. Read CLAUDE.md again, record checksum
4. Compare checksums

**Expected**: Running sync twice produces identical output (deterministic generation)
**Type**: Integration

<!-- section_id: "9a483978-3602-4850-b2e4-876b726b8744" -->
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

<!-- section_id: "ad73e19c-67a4-46b5-aaf0-f8752b8589ef" -->
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

<!-- section_id: "f89e6e47-7ff0-47e6-b60d-089ea4c8da11" -->
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

<!-- section_id: "fd81afbb-568b-49c2-9349-cc8b5b9a75b8" -->
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

<!-- section_id: "71ec2afb-15a9-423d-acb5-08577dd1b99c" -->
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

<!-- section_id: "e391313e-d780-48c5-8aff-e4f562b45732" -->
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
