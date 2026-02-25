# Test Design: Stages Manager Pattern

**Validates**: `stage_1_04_design/outputs/design_decisions/stages_manager_pattern.md`
**Type**: Structural (bash) + Integration (bash)
**Script name**: `test_stages_manager_pattern.sh`

---

## What We're Testing

The stages manager pattern upgrades `layer_N_99_stages/` from a thin container to a proper managed entity with `.0agnostic/`, `.1merge/`, and full `0AGNOSTIC.md`. We validate: the stages manager has correct structure, stage coordination content lives in the stages manager (not the entity manager), handoff documents flow correctly, and generated tool files are produced.

---

## Test Cases

### TC-SM-01: Stages manager has full .0agnostic/ structure

**Steps**:
1. For each entity with an upgraded stages manager (start with context_chain_system):
   - Check `layer_N_99_stages/.0agnostic/` exists
   - Verify numbered subdirectories exist:
     - `01_knowledge/`
     - `02_rules/static/`
     - `02_rules/dynamic/`
     - `03_protocols/`
     - `04_episodic_memory/`
     - `05_handoff_documents/01_incoming/01_from_above/`
     - `05_handoff_documents/01_incoming/03_from_below/stage_reports/`
     - `05_handoff_documents/02_outgoing/01_to_above/`
     - `06_context_avenue_web/01_file_based/`

**Expected**: All numbered subdirectories exist following the standard agnostic structure
**Type**: Structural

### TC-SM-02: Stages manager .0agnostic/01_knowledge/ has coordination knowledge

**Steps**:
1. Check `layer_N_99_stages/.0agnostic/01_knowledge/` contains:
   - `stage_dependency_graph.md` — which stages feed which
   - `stage_lifecycle_model.md` — stage states (scaffolded → active → complete)
   - `parallel_stage_rules.md` — which stages can run concurrently
2. Verify each file has content (not empty or .gitkeep only)
3. Verify dependency graph references actual stage numbers (01-11)

**Expected**: Knowledge directory contains the three core coordination documents with real content
**Type**: Structural

### TC-SM-03: Stages manager .0agnostic/02_rules/ has transition and consolidation rules

**Steps**:
1. Check `.0agnostic/02_rules/static/` contains:
   - `stage_transition_rules.md` — when stages are ready to transition
   - `consolidation_rules.md` — how to produce stages_report.md
2. Check `.0agnostic/02_rules/dynamic/` contains:
   - `blocking_detection.md` — how to identify stuck stages
3. Verify transition rules reference actual stage flow (01→02→04→05→06→07)

**Expected**: Rules directory has transition, consolidation, and blocking detection rules with real content
**Type**: Structural

### TC-SM-04: Stages manager .0agnostic/03_protocols/ has step-by-step procedures

**Steps**:
1. Check `.0agnostic/03_protocols/` contains:
   - `stage_transition_protocol.md` — step-by-step for moving between stages
   - `consolidation_protocol.md` — how to read all reports and produce summary
2. Verify each protocol has numbered steps (not just descriptions)

**Expected**: Protocols directory has actionable step-by-step procedures
**Type**: Structural

### TC-SM-05: Stages manager has .1merge/ with 3-tier structure

**Steps**:
1. Check `layer_N_99_stages/.1merge/` exists
2. Verify `.1claude_merge/` subdirectory exists with:
   - `0_synced/`
   - `1_overrides/`
   - `2_additions/`
3. Check if other tool merge dirs exist (`.1agents_merge/`, etc.) — optional but allowed

**Expected**: .1merge has at minimum a Claude merge directory with the standard 3-tier structure
**Type**: Structural

### TC-SM-06: Stages manager 0AGNOSTIC.md has coordination identity

**Steps**:
1. Read `layer_N_99_stages/0AGNOSTIC.md`
2. Verify it contains:
   - Identity section (role as stages manager, not just "thin container")
   - Stage overview table or stage list
   - Stage flow diagram or dependency references
   - Pointers to `.0agnostic/01_knowledge/` resources
   - Pointers to `.0agnostic/03_protocols/` procedures
3. Verify it is NOT the old thin container format (~7 lines)
4. Verify line count is 40-120 lines (substantial but not bloated)

**Expected**: 0AGNOSTIC.md is a proper manager identity with coordination knowledge pointers
**Type**: Structural

### TC-SM-07: Entity manager 0AGNOSTIC.md does NOT contain stage coordination

**Steps**:
1. Read the parent entity's 0AGNOSTIC.md (e.g., context_chain_system/0AGNOSTIC.md)
2. Verify it does NOT contain:
   - Full stage overview table with 11 rows (should be in stages manager)
   - Stage delegation instructions ("spawn a stage agent with...")
   - Stage flow diagram (01→02→04→05→06→07)
   - Stage transition rules
3. Verify it DOES contain:
   - Navigation pointer to stages manager
   - "Current Focus" or strategic stage mentions (high-level, not coordination)
   - Entity identity, children, parent references

**Expected**: Stage coordination content has moved to stages manager; entity manager retains only strategic references
**Type**: Structural (heuristic)

### TC-SM-08: Generated tool files exist at stages manager level

**Steps**:
1. Run agnostic-sync.sh for the stages manager
2. Verify generated files exist at `layer_N_99_stages/`:
   - `CLAUDE.md` (with stages coordination context, not thin container)
   - `AGENTS.md`
   - `GEMINI.md`
   - `OPENAI.md`
   - `.cursorrules`
3. Verify each generated file has content (non-empty)
4. Verify CLAUDE.md contains stage coordination context (not just "Stages container for X")

**Expected**: agnostic-sync produces all generated tool files with stages manager content
**Type**: Integration

### TC-SM-09: 0INDEX.md exists as stages dashboard

**Steps**:
1. Check `layer_N_99_stages/0INDEX.md` exists
2. Verify it contains:
   - All stages listed with current status
   - Stage flow or dependency information
   - References to active stage reports
3. Verify it references the stages manager role

**Expected**: 0INDEX.md serves as the stages dashboard for the stages manager
**Type**: Structural

### TC-SM-10: Stage reports flow into stages manager from_below

**Steps**:
1. For each active stage (has `outputs/stage_report.md`):
   - Check if a copy exists in `layer_N_99_stages/.0agnostic/05_handoff_documents/01_incoming/03_from_below/stage_reports/`
2. Cross-check: each file in `from_below/stage_reports/` matches an actual stage_report.md
3. Verify no stale reports (from_below has reports only for stages that still have them)

**Expected**: Stages manager's from_below mirrors active stage reports
**Note**: Requires sync-handoffs.sh to have been run
**Type**: Integration

### TC-SM-11: Stages manager produces consolidated stages_report.md

**Steps**:
1. Check `layer_N_99_stages/.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stages_report.md` exists
2. Verify it references all active stages
3. Verify it contains: overall status, per-stage summaries, blocking issues (if any)
4. Verify it is under 50 lines (consolidated summary, not full detail)

**Expected**: Stages manager produces a consolidated report for the entity manager
**Type**: Structural

### TC-SM-12: Orchestrator .gab.jsonld backs the stages manager

**Steps**:
1. Check `layer_N_99_stages_orchestrator.gab.jsonld` exists
2. Verify it defines modes relevant to stage coordination (not just generic modes)
3. Check that the orchestrator's `@id` or purpose references stages management
4. Verify `layer_N_99_stages_orchestrator.integration.md` exists with readable summary

**Expected**: The existing orchestrator file properly backs the stages manager role
**Type**: Structural

### TC-SM-13: stage_00_stage_registry is managed by stages manager

**Steps**:
1. Check `stage_N_00_stage_registry/` exists
2. Verify it contains stage metadata (stage list, status, descriptions)
3. Verify the stages manager 0AGNOSTIC.md references the registry
4. Cross-check: registry stage count matches actual stage directories

**Expected**: The stage registry serves as the stages manager's inventory and is referenced from 0AGNOSTIC.md
**Type**: Structural

### TC-SM-14: Stages manager does NOT have its own stages or children

**Steps**:
1. Verify `layer_N_99_stages/` does NOT contain a `layer_N+1_group/` directory
2. Verify `layer_N_99_stages/` does NOT contain `stage_N_*` directories inside a nested stages container
3. Verify the stages manager 0AGNOSTIC.md does NOT reference children entities

**Expected**: The stages manager manages stages but does not recursively contain stages-of-stages or children
**Type**: Structural

---

## Coverage Gap Analysis

| Design Concept | Test Case | Status |
|---------------|-----------|--------|
| Full .0agnostic/ structure | TC-SM-01 | New |
| Coordination knowledge files | TC-SM-02 | New |
| Transition and consolidation rules | TC-SM-03 | New |
| Step-by-step protocols | TC-SM-04 | New |
| .1merge/ 3-tier structure | TC-SM-05 | New |
| Manager identity in 0AGNOSTIC.md | TC-SM-06 | New |
| Clean separation from entity manager | TC-SM-07 | New (heuristic) |
| Generated tool files | TC-SM-08 | New |
| 0INDEX.md dashboard | TC-SM-09 | New |
| Stage reports flow (from_below) | TC-SM-10 | New |
| Consolidated stages_report.md | TC-SM-11 | New |
| Orchestrator .gab.jsonld | TC-SM-12 | New |
| Stage registry as inventory | TC-SM-13 | New |
| No recursive stages/children | TC-SM-14 | New |
| Zero extra hops for simple tasks | Not directly testable | Design constraint — behavioral |
| Optional per entity (4+ stages) | Not directly testable | Policy, not structure |
| Backward compatibility | Covered by TC-SM-08 | agnostic-sync still works |

## Test Case Summary

| Category | Count | Type |
|----------|-------|------|
| .0agnostic/ structure | 4 (TC-SM-01 to TC-SM-04) | Structural |
| .1merge/ structure | 1 (TC-SM-05) | Structural |
| 0AGNOSTIC.md content | 2 (TC-SM-06, TC-SM-07) | Structural |
| Generated files | 1 (TC-SM-08) | Integration |
| Dashboard and reporting | 2 (TC-SM-09, TC-SM-11) | Structural |
| Handoff flow | 1 (TC-SM-10) | Integration |
| Orchestrator and registry | 2 (TC-SM-12, TC-SM-13) | Structural |
| Negative constraints | 1 (TC-SM-14) | Structural |
| **Total** | **14** | **12 structural, 2 integration** |
