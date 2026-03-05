---
resource_id: "00a86f16-abe7-47b0-8535-79868adb87a6"
resource_type: "output"
resource_name: "test_design_07_sync_architecture"
---
# Test Design: 07 Unified Sync Architecture

**Validates**: `stage_2_04_design/outputs/by_topic/07_unified_sync_architecture.md`
**Type**: Integration (bash)
**Script name**: `test_sync_architecture.sh`

---

<!-- section_id: "4783cb99-16cb-41a5-ab0d-e72b39ffce87" -->
## What We're Testing

5 existing sync scripts work correctly and independently. Dependency ordering is respected. Zero-dependency guarantee holds (file-based syncs need only standard unix tools). Each script transforms the right inputs to the right outputs.

---

<!-- section_id: "15832f53-a446-4ad9-9a8d-f9f7ab04a6e8" -->
## Test Cases

<!-- section_id: "fe474041-2bb4-49de-91f3-8bd0883b94b6" -->
### TC-07-01: agnostic-sync.sh — input/output contract

**Steps**:
1. Verify script exists and is executable at `.0agnostic/agnostic-sync.sh`
2. Run against context_chain_system entity
3. Verify inputs consumed: 0AGNOSTIC.md, .1merge/ (if present), promote:hot rules
4. Verify outputs produced: CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, .github/copilot-instructions.md
5. Verify exit code 0

**Expected**: All 6 output files generated from 0AGNOSTIC.md source
**Note**: Extends existing test_agnostic_sync with .cursorrules and copilot-instructions.md coverage
**Type**: Integration

<!-- section_id: "86fa9f95-e8e7-430c-abf2-a8d7ce50e00d" -->
### TC-07-02: episodic-sync.sh — aggregates to auto-memory

**Steps**:
1. Verify script exists at `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh`
2. Create a test episodic memory entry (or use existing)
3. Run episodic-sync.sh
4. Verify output at `~/.claude/projects/.../memory/episodic.md`
5. Verify content from multiple entities is aggregated

**Expected**: Episodic memory from .0agnostic/04_episodic_memory/ lands in Claude auto-memory
**Type**: Integration

<!-- section_id: "9d995b9e-2c07-4eee-b7c0-90eda07e09a8" -->
### TC-07-03: jsonld-to-md.sh — generates integration summaries

**Steps**:
1. Verify script exists at `.0agnostic/01_knowledge/layer_stage_system/resources/tools/jsonld-to-md.sh`
2. Run against `layer_2_orchestrator.gab.jsonld`
3. Verify `layer_2_orchestrator.integration.md` is generated
4. Verify .integration.md contains: modes list, constraints, skill mappings
5. Verify exit code 0

**Expected**: .integration.md generated from .gab.jsonld with correct structure
**Type**: Integration

<!-- section_id: "4e2f4f99-118c-40b6-b69e-3d30bd36a86d" -->
### TC-07-04: sync-handoffs.sh — distributes reports

**Steps**:
1. Verify script exists at `.0agnostic/01_knowledge/layer_stage_system/resources/tools/sync-handoffs.sh`
2. Ensure at least one stage_report.md exists
3. Run sync-handoffs.sh for context_chain_system
4. Check distribution targets:
   - Entity `from_below/stage_reports/` has copies
   - Sibling stages `from_sides/` have copies
   - Parent entity `from_below/layer_reports/` has layer_report (if exists)
5. Verify file content matches source (not corrupted)

**Expected**: Reports distributed to all three directions
**Type**: Integration

<!-- section_id: "5d551bb1-e3cb-4b32-8411-b297d38bb6b2" -->
### TC-07-05: user-level-sync.sh — extends chain to ~/.0agnostic/

**Steps**:
1. Verify script exists at `.0agnostic/01_knowledge/layer_stage_system/resources/tools/user-level-sync.sh`
2. Run user-level-sync.sh
3. Verify `~/.0agnostic/` directory exists
4. Verify universal artifacts from root `.0agnostic/` appear in `~/.0agnostic/`
5. Verify non-universal (entity-specific) content is NOT copied

**Expected**: Universal context extends beyond repo boundary to user level
**Type**: Integration

<!-- section_id: "41c86e01-fdec-4173-aee4-135fcdacee53" -->
### TC-07-06: Dependency ordering — Phase 1 before Phase 2

**Steps**:
1. Modify 0AGNOSTIC.md with a unique marker string
2. Run agnostic-sync.sh (Phase 1, step 1) — verify marker in CLAUDE.md
3. Run jsonld-to-md.sh (Phase 1, step 2) — verify it reads current agent files
4. Run episodic-sync.sh (Phase 2) — verify it reads current episodic content

**Expected**: Later scripts see outputs from earlier scripts (dependency ordering works)
**Type**: Integration

<!-- section_id: "39b35bca-7e73-4f65-94af-c0505d3f5fcc" -->
### TC-07-07: Zero-dependency guarantee — file-based syncs use standard tools

**Steps**:
1. For each file-based sync script (agnostic-sync, jsonld-to-md, episodic-sync, sync-handoffs, user-level-sync):
   - Parse script for external tool dependencies (`which`, `command -v`, imports)
   - Verify only standard unix tools used: bash, awk, sed, jq, grep, find, sort
   - Flag any dependency on PostgreSQL, Python, Node, etc.
2. Verify scripts have `#!/bin/bash` or `#!/usr/bin/env bash` shebang

**Expected**: All file-based sync scripts work with standard unix tools only
**Type**: Structural

<!-- section_id: "b33608ad-a3f3-401f-a6a3-6d2c70b0e085" -->
### TC-07-08: sync-registry.json matches actual scripts

**Steps**:
1. Read `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/sync-registry.json` (if exists)
2. For each entry, verify the script path exists
3. For each actual sync script in the tools directory, verify it has a registry entry
4. Flag orphan entries (registry has script that doesn't exist) or unregistered scripts

**Expected**: Registry is complete and accurate
**Note**: sync-registry.json may not exist yet — test becomes SKIP if missing
**Type**: Structural

---

<!-- section_id: "acc38f2d-7cf7-406d-9d0e-535c51102618" -->
## Coverage Gap Analysis

| Design Concept | Test Case | Status |
|---------------|-----------|--------|
| agnostic-sync.sh | TC-07-01 | Extends existing |
| episodic-sync.sh | TC-07-02 | New |
| jsonld-to-md.sh | TC-07-03 | New |
| sync-handoffs.sh | TC-07-04 | New |
| user-level-sync.sh | TC-07-05 | New |
| Dependency ordering | TC-07-06 | New |
| Zero-dependency guarantee | TC-07-07 | New |
| sync-registry.json | TC-07-08 | New |
| sync-main.sh orchestrator | Not testable | Not yet implemented |
| Data-based sync scripts | Not testable | Not yet implemented |
