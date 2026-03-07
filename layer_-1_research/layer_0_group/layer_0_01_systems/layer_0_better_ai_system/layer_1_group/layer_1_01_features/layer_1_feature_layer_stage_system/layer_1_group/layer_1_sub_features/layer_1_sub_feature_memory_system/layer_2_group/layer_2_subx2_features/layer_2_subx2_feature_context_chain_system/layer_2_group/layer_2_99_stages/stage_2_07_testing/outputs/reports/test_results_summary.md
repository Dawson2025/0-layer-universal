---
resource_id: "5768d4b2-2c0f-4326-be31-dd7b7790ec09"
resource_type: "output"
resource_name: "test_results_summary"
---
# Test Results Summary

**Date**: 2026-02-25 19:09:35
**Entity**: layer_2_subx2_feature_context_chain_system
**Runner**: run_all_tests.sh

---

<!-- section_id: "c71531d6-6ce3-4f66-8698-93fc9e5df818" -->
## test_outputs_purpose_taxonomy

**Status**: PASS | **Exit code**: 0
| Metric | Count |
|--------|-------|
| PASS | 68 |
| FAIL | 0 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: Outputs Purpose Taxonomy ===
  [32mPASS[0m  Exists: outputs/by_purpose
  [32mPASS[0m  Purpose exists: context_chain_validation
  [32mPASS[0m  Suite dir exists: context_chain_validation/design
  [32mPASS[0m  Suite has artifacts: context_chain_validation/design
  [32mPASS[0m  Suite dir exists: context_chain_validation/implementation
  [32mPASS[0m  Suite has artifacts: context_chain_validation/implementation
  [32mPASS[0m  Suite dir exists: context_chain_validation/runs
  [32mPASS[0m  Suite has artifacts: context_chain_validation/runs
  [32mPASS[0m  Suite dir exists: context_chain_validation/results
  [32mPASS[0m  Suite has artifacts: context_chain_validation/results
  [32mPASS[0m  Suite dir exists: context_chain_validation/insights
  [32mPASS[0m  Suite has artifacts: context_chain_validation/insights
  [32mPASS[0m  Purpose exists: codex_runtime_validation
  [32mPASS[0m  Suite dir exists: codex_runtime_validation/design
  [32mPASS[0m  Suite has artifacts: codex_runtime_validation/design
  [32mPASS[0m  Suite dir exists: codex_runtime_validation/implementation
  [32mPASS[0m  Suite has artifacts: codex_runtime_validation/implementation
  [32mPASS[0m  Suite dir exists: codex_runtime_validation/runs
  [32mPASS[0m  Suite has artifacts: codex_runtime_validation/runs
  [32mPASS[0m  Suite dir exists: codex_runtime_validation/results
  [32mPASS[0m  Suite has artifacts: codex_runtime_validation/results
  [32mPASS[0m  Suite dir exists: codex_runtime_validation/insights
  [32mPASS[0m  Suite has artifacts: codex_runtime_validation/insights
  [32mPASS[0m  Purpose exists: reports_funnel_validation
  [32mPASS[0m  Suite dir exists: reports_funnel_validation/design
  [32mPASS[0m  Suite has artifacts: reports_funnel_validation/design
  [32mPASS[0m  Suite dir exists: reports_funnel_validation/implementation
  [32mPASS[0m  Suite has artifacts: reports_funnel_validation/implementation
  [32mPASS[0m  Suite dir exists: reports_funnel_validation/runs
  [32mPASS[0m  Suite has artifacts: reports_funnel_validation/runs
  [32mPASS[0m  Suite dir exists: reports_funnel_validation/results
  [32mPASS[0m  Suite has artifacts: reports_funnel_validation/results
  [32mPASS[0m  Suite dir exists: reports_funnel_validation/insights
  [32mPASS[0m  Suite has artifacts: reports_funnel_validation/insights
  [32mPASS[0m  Purpose exists: avenue_web_validation
  [32mPASS[0m  Suite dir exists: avenue_web_validation/design
  [32mPASS[0m  Suite has artifacts: avenue_web_validation/design
  [32mPASS[0m  Suite dir exists: avenue_web_validation/implementation
  [32mPASS[0m  Suite has artifacts: avenue_web_validation/implementation
  [32mPASS[0m  Suite dir exists: avenue_web_validation/runs
  [32mPASS[0m  Suite has artifacts: avenue_web_validation/runs
  [32mPASS[0m  Suite dir exists: avenue_web_validation/results
  [32mPASS[0m  Suite has artifacts: avenue_web_validation/results
  [32mPASS[0m  Suite dir exists: avenue_web_validation/insights
  [32mPASS[0m  Suite has artifacts: avenue_web_validation/insights
  [32mPASS[0m  Purpose exists: cross_entity_porting_bridge_validation
  [32mPASS[0m  Suite dir exists: cross_entity_porting_bridge_validation/design
  [32mPASS[0m  Suite has artifacts: cross_entity_porting_bridge_validation/design
  [32mPASS[0m  Suite dir exists: cross_entity_porting_bridge_validation/implementation
  [32mPASS[0m  Suite has artifacts: cross_entity_porting_bridge_validation/implementation
  [32mPASS[0m  Suite dir exists: cross_entity_porting_bridge_validation/runs
  [32mPASS[0m  Suite has artifacts: cross_entity_porting_bridge_validation/runs
  [32mPASS[0m  Suite dir exists: cross_entity_porting_bridge_validation/results
  [32mPASS[0m  Suite has artifacts: cross_entity_porting_bridge_validation/results
  [32mPASS[0m  Suite dir exists: cross_entity_porting_bridge_validation/insights
  [32mPASS[0m  Suite has artifacts: cross_entity_porting_bridge_validation/insights
  [32mPASS[0m  Purpose exists: full_suite_validation
  [32mPASS[0m  Suite dir exists: full_suite_validation/design
  [32mPASS[0m  Suite has artifacts: full_suite_validation/design
  [32mPASS[0m  Suite dir exists: full_suite_validation/implementation
  [32mPASS[0m  Suite has artifacts: full_suite_validation/implementation
  [32mPASS[0m  Suite dir exists: full_suite_validation/runs
  [32mPASS[0m  Suite has artifacts: full_suite_validation/runs
  [32mPASS[0m  Suite dir exists: full_suite_validation/results
  [32mPASS[0m  Suite has artifacts: full_suite_validation/results
  [32mPASS[0m  Suite dir exists: full_suite_validation/insights
  [32mPASS[0m  Suite has artifacts: full_suite_validation/insights
  [32mPASS[0m  Compatibility note exists: outputs/by_topic/README.md

================================
  [32mPASS[0m: 68
  [31mFAIL[0m: 0
  [33mSKIP[0m: 0
================================
```

</details>

---

<!-- section_id: "bfad47fe-ee24-4a09-9bac-f052716947aa" -->
## test_cross_entity_porting_bridge

**Status**: PASS | **Exit code**: 0
| Metric | Count |
|--------|-------|
| PASS | 7 |
| FAIL | 0 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: Cross-Entity Porting Bridge ===
  [32mPASS[0m  Upstream bridge contract exists
  [32mPASS[0m  Downstream bridge contract exists
  [32mPASS[0m  Upstream agnostic sync design exists
  [32mPASS[0m  Downstream codex contract exists
  [32mPASS[0m  Downstream bridge references upstream tool_and_app_agnostic
  [32mPASS[0m  Upstream bridge references downstream context_chain_system
  [32mPASS[0m  Downstream bridge includes codex max-permission runtime policy

================================
  [32mPASS[0m: 7
  [31mFAIL[0m: 0
  [33mSKIP[0m: 0
================================
```

</details>

---

<!-- section_id: "b9bf7f26-3ef8-43de-820a-3bdac76c06bb" -->
## test_reports_funnel_structure

**Status**: PASS | **Exit code**: 0
| Metric | Count |
|--------|-------|
| PASS | 12 |
| FAIL | 0 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: Reports Funnel Structure ===
  [32mPASS[0m  Exists: outputs/reports
  [32mPASS[0m  Exists: outputs/reports/stage_report.md
  [32mPASS[0m  Exists: outputs/reports/output_report.md
  [32mPASS[0m  Exists: .0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md
  [32mPASS[0m  Exists: .0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md
  [32mPASS[0m  Exists: .0agnostic/05_handoff_documents/02_outgoing/01_to_above/overview_report.md
  [32mPASS[0m  Exists: .0agnostic/05_handoff_documents/02_outgoing/03_to_below/overview_report.md
  [32mPASS[0m  Exists: /home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_agent_delegation_system/layer_1_group/layer_1_subx2_features/layer_1_subx2_feature_memory_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_context_chain_system/.0agnostic/05_handoff_documents/02_outgoing/01_to_above/layer_report.md
  [32mPASS[0m  Exists: /home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_agent_delegation_system/layer_1_group/layer_1_subx2_features/layer_1_subx2_feature_memory_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_context_chain_system/.0agnostic/05_handoff_documents/02_outgoing/03_to_below/layer_report.md
  [32mPASS[0m  Canonical stage_report matches to_above handoff copy
  [32mPASS[0m  Canonical stage_report matches to_below handoff copy
  [32mPASS[0m  Legacy stage_report exists for compatibility

================================
  [32mPASS[0m: 12
  [31mFAIL[0m: 0
  [33mSKIP[0m: 0
================================
```

</details>

---

<!-- section_id: "a482a9ad-32d1-4d23-8068-664071d11530" -->
## test_agnostic_sync

**Status**: PASS | **Exit code**: 0
| Metric | Count |
|--------|-------|
| PASS | 22 |
| FAIL | 0 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: agnostic-sync.sh ===
Entity: layer_2_subx2_feature_context_chain_system
Sync script: /home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh

  [32mPASS[0m  agnostic-sync.sh exists and is executable
  [32mPASS[0m  0AGNOSTIC.md exists at entity root

--- Test 1: Sync produces all 4 tool files ---
  [32mPASS[0m  agnostic-sync.sh exited with code 0
  [32mPASS[0m  CLAUDE.md generated
  [32mPASS[0m  AGENTS.md generated
  [32mPASS[0m  GEMINI.md generated
  [32mPASS[0m  OPENAI.md generated

--- Test 2: CLAUDE.md contains Identity section ---
  [32mPASS[0m  CLAUDE.md contains ## Identity
  [32mPASS[0m  Identity section has content (10 lines)

--- Test 3: CLAUDE.md contains Triggers section ---
  [32mPASS[0m  CLAUDE.md contains ## Triggers

--- Test 4: CLAUDE.md has auto-generated footer ---
  [32mPASS[0m  CLAUDE.md has auto-generated footer
  [32mPASS[0m  CLAUDE.md references agnostic-sync.sh

--- Test 5: All tool files contain Identity section ---
  [32mPASS[0m  AGENTS.md contains ## Identity
  [32mPASS[0m  AGENTS.md has auto-generated footer
  [32mPASS[0m  GEMINI.md contains ## Identity
  [32mPASS[0m  GEMINI.md has auto-generated footer
  [32mPASS[0m  OPENAI.md contains ## Identity
  [32mPASS[0m  OPENAI.md has auto-generated footer

--- Test 6: Re-sync reflects modifications ---
  [32mPASS[0m  CLAUDE.md updated with new content after re-sync
  [32mPASS[0m  AGENTS.md updated with new content after re-sync

--- Test 7: Graceful failure on missing 0AGNOSTIC.md ---
  [32mPASS[0m  Sync fails with non-zero exit on missing 0AGNOSTIC.md (exit=1)
  [32mPASS[0m  Error message mentions missing file

================================
  [32mPASS[0m: 22
  [31mFAIL[0m: 0
  [33mSKIP[0m: 0
================================
```

</details>

---

<!-- section_id: "41cbf879-cf57-4f0a-a1e5-f38de029376f" -->
## test_context_chain_traversal

**Status**: PASS | **Exit code**: 0
| Metric | Count |
|--------|-------|
| PASS | 25 |
| FAIL | 0 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: Context Chain Traversal ===
Entity: layer_2_subx2_feature_context_chain_system

--- Test 1: Source file exists ---
  [32mPASS[0m  0AGNOSTIC.md exists at entity root

--- Test 2: Parent reference resolves ---
  [32mPASS[0m  Parent reference found: ../../../0AGNOSTIC.md
  [32mPASS[0m  Parent resolves to: /home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_agent_delegation_system/layer_1_group/layer_1_subx2_features/layer_1_subx2_feature_memory_system/0AGNOSTIC.md
  [32mPASS[0m  Parent entity: layer_1_subx2_feature_memory_system

--- Test 3: Full chain traversal ---
  [32mPASS[0m  Chain traversal complete — no broken references
  [32mPASS[0m  Chain depth: 7 levels above entity

  Chain (bottom → top):
    └── layer_2_subx2_feature_context_chain_system
      └── layer_1_subx2_feature_memory_system
        └── layer_1_sub_feature_agent_delegation_system
          └── layer_0_feature_layer_stage_system
            └── layer_0_features
              └── layer_0_group
                └── layer_-1_better_ai_system
                  └── layer_-1_research

--- Test 4: CLAUDE.md at each chain level ---
  [32mPASS[0m  CLAUDE.md at entity root (level 0)
  [32mPASS[0m  CLAUDE.md at layer_1_subx2_feature_memory_system (level 1)
  [32mPASS[0m  CLAUDE.md at layer_1_sub_feature_agent_delegation_system (level 2)
  [32mPASS[0m  CLAUDE.md at layer_0_feature_layer_stage_system (level 3)
  [32mPASS[0m  CLAUDE.md at layer_0_features (level 4)
  [32mPASS[0m  CLAUDE.md at layer_0_group (level 5)
  [32mPASS[0m  CLAUDE.md at layer_-1_better_ai_system (level 6)
  [32mPASS[0m  CLAUDE.md at layer_-1_research (level 7)
  [32mPASS[0m  Total CLAUDE.md files in chain: 8

--- Test 5: Auto-generated footers ---
  [32mPASS[0m  layer_2_subx2_feature_context_chain_system/CLAUDE.md has sync footer
  [32mPASS[0m  layer_1_subx2_feature_memory_system/CLAUDE.md has sync footer
  [32mPASS[0m  layer_1_sub_feature_agent_delegation_system/CLAUDE.md has sync footer
  [32mPASS[0m  layer_0_feature_layer_stage_system/CLAUDE.md has sync footer
  [32mPASS[0m  layer_0_features/CLAUDE.md has sync footer
  [32mPASS[0m  layer_0_group/CLAUDE.md has sync footer
  [32mPASS[0m  layer_-1_better_ai_system/CLAUDE.md has sync footer
  [32mPASS[0m  layer_-1_research/CLAUDE.md has sync footer

--- Test 6: 0AGNOSTIC.md density in filesystem path ---
  [32mPASS[0m  Total 0AGNOSTIC.md in filesystem path to root: 9
  [32mPASS[0m  Sufficient chain density (>= 3 files)

================================
  [32mPASS[0m: 25
  [31mFAIL[0m: 0
  [33mSKIP[0m: 0
================================
```

</details>

---

<!-- section_id: "5512cb4c-ab04-4e32-97f2-326e645086f2" -->
## test_avenue_coverage_functional

**Status**: PASS | **Exit code**: 0
| Metric | Count |
|--------|-------|
| PASS | 16 |
| FAIL | 0 |
| SKIP | 0 |
| SCAFFOLDED | 2 |

<details>
<summary>Full output</summary>

```
=== Test: Avenue Coverage (Functional) ===
Entity: layer_2_subx2_feature_context_chain_system

--- A1: System Prompt (CLAUDE.md) ---
  [32mPASS[0m       A1: CLAUDE.md has 399 lines of content
  [32mPASS[0m       A1: CLAUDE.md has Identity section

--- A2: Path Rules (.claude/rules/) ---
  [32mPASS[0m       A2: .claude/rules/ has 1 .md files
  [32mPASS[0m       A2: Rules have 23 lines of content

--- A3: Skills (.0agnostic/05_skills/) ---
  [32mPASS[0m       A3: 05_skills has 2 SKILL.md files

--- A4: References (parent chain) ---
  [32mPASS[0m       A4: Parent reference resolves (../../../0AGNOSTIC.md)
  [32mPASS[0m       A4: Children references documented

--- A5: JSON-LD (.gab.jsonld) ---
  [32mPASS[0m       A5: 1 .gab.jsonld file(s) found
  [32mPASS[0m       A5: layer_2_orchestrator.gab.jsonld is valid JSON
  [32mPASS[0m       A5: layer_2_orchestrator.gab.jsonld has @graph (GAB-compliant)
  [32mPASS[0m       A5: layer_2_orchestrator.gab.jsonld has 5 modes

--- A6: Integration (.integration.md) ---
  [32mPASS[0m       A6: layer_2_orchestrator.integration.md has 30 lines of content

--- A7: Episodic Memory ---
  [32mPASS[0m       A7: 07_episodic_memory exists
  [33mSCAFFOLDED[0m A7: sessions/ exists but is empty
  [33mSCAFFOLDED[0m A7: changes/ exists but is empty

--- A8: 0AGNOSTIC Source ---
  [32mPASS[0m       A8: 0AGNOSTIC.md has 384 lines of content
  [32mPASS[0m       A8: 0AGNOSTIC.md has Identity section
  [32mPASS[0m       A8: 0AGNOSTIC.md has Navigation/Pointers section

================================
  [32mPASS[0m:       16
  [33mSCAFFOLDED[0m: 2
  [31mFAIL[0m:       0
================================
  Functional coverage: 88%
  (PASS=16, SCAFFOLDED=2 need content, FAIL=0 need fixing)
```

</details>

---

<!-- section_id: "cd346248-b193-4f10-bea2-584d6af9ccea" -->
## test_1merge_structure

**Status**: PASS | **Exit code**: 0
| Metric | Count |
|--------|-------|
| PASS | 17 |
| FAIL | 0 |
| SKIP | 6 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: .1merge/ Structure ===
Entity: layer_2_subx2_feature_context_chain_system

--- Test 1: .1merge/ exists ---
  [32mPASS[0m  .1merge/ directory exists

--- Test 2: Tool merge directories ---
  [32mPASS[0m  .1claude_merge/ exists
  [32mPASS[0m  .1cursor_merge/ exists
  [32mPASS[0m  .1gemini_merge/ exists
  [32mPASS[0m  .1aider_merge/ exists
  [32mPASS[0m  .1codex_merge/ exists
  [32mPASS[0m  .1copilot_merge/ exists

--- Test 3: 3-tier structure ---
  [32mPASS[0m  All 18 tier directories present (18/18)

--- Test 4: Content in overrides/additions ---
  [32mPASS[0m  .1codex_merge/1_overrides/tool_boilerplate.md (11 lines)
  [32mPASS[0m  .1codex_merge/2_additions/tool_additions.md (12 lines)

--- Test 5: 0_synced/ alignment check ---
  [33mSKIP[0m  .1claude_merge/0_synced/ is empty (sync hasn't populated it yet)
  [33mSKIP[0m  .1cursor_merge/0_synced/ is empty (sync hasn't populated it yet)
  [33mSKIP[0m  .1gemini_merge/0_synced/ is empty (sync hasn't populated it yet)
  [33mSKIP[0m  .1aider_merge/0_synced/ is empty (sync hasn't populated it yet)
  [33mSKIP[0m  .1codex_merge/0_synced/ is empty (sync hasn't populated it yet)
  [33mSKIP[0m  .1copilot_merge/0_synced/ is empty (sync hasn't populated it yet)

--- Test 6: Additions compatibility ---
  [32mPASS[0m  Sync succeeds with addition present (exit=0)

--- Test 7: Naming conventions ---
  [32mPASS[0m  .1claude_merge follows naming convention
  [32mPASS[0m  .1cursor_merge follows naming convention
  [32mPASS[0m  .1gemini_merge follows naming convention
  [32mPASS[0m  .1aider_merge follows naming convention
  [32mPASS[0m  .1codex_merge follows naming convention
  [32mPASS[0m  .1copilot_merge follows naming convention

================================
  [32mPASS[0m: 17
  [31mFAIL[0m: 0
  [33mSKIP[0m: 6
================================
```

</details>

---

<!-- section_id: "0b39c188-1c79-4253-8f87-92c3fb885ff0" -->
## test_instantiation_readiness

**Status**: PASS | **Exit code**: 0
| Metric | Count |
|--------|-------|
| PASS | 0 |
| FAIL | 0 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: Instantiation Readiness ===
Entity: layer_2_subx2_feature_context_chain_system
Path: /home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_agent_delegation_system/layer_1_group/layer_1_subx2_features/layer_1_subx2_feature_memory_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_context_chain_system

--- Check 1: 0AGNOSTIC.md ---
  [32mREADY[0m      0AGNOSTIC.md exists
  [32mREADY[0m      Has ## Identity section
  [32mREADY[0m      Has parent reference

--- Check 2: agnostic-sync.sh ---
  [32mREADY[0m      agnostic-sync.sh found at /home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh
  [32mREADY[0m      agnostic-sync.sh is executable

--- Check 3: .0agnostic/ structure ---
  [32mREADY[0m      .0agnostic/ directory exists
  [32mREADY[0m      .0agnostic/01_knowledge/
  [32mREADY[0m      .0agnostic/02_rules/
  [32mREADY[0m      .0agnostic/03_protocols/
  [32mREADY[0m      .0agnostic/04_agents/
  [32mREADY[0m      .0agnostic/05_skills/
  [32mREADY[0m      .0agnostic/06_hooks/
  [32mREADY[0m      .0agnostic/07_episodic_memory/
  [32mREADY[0m      .0agnostic/07_episodic_memory/sessions/
  [32mREADY[0m      .0agnostic/07_episodic_memory/changes/
  [32mREADY[0m      .0agnostic/06_hooks/scripts/

--- Check 4: .1merge/ structure ---
  [32mREADY[0m      .1merge/ directory exists
  [32mREADY[0m      All 6 tools × 3 tiers present

--- Check 5: Tool config directories ---
  [32mREADY[0m      .claude/ exists
  [32mREADY[0m      .cursor/ exists
  [32mREADY[0m      .gemini/ exists
  [32mREADY[0m      .codex/ exists
  [32mREADY[0m      .github/ exists
  [32mREADY[0m      .claude/rules/ exists

--- Check 6: Orchestrator (.gab.jsonld) ---
  [32mREADY[0m      1 .gab.jsonld file(s) found
  [32mREADY[0m      layer_2_orchestrator.gab.jsonld is valid JSON

--- Check 7: Integration summary (.integration.md) ---
  [32mREADY[0m      1 .integration.md file(s) found

--- Check 8: Parent chain ---
  [32mREADY[0m      Parent chain has 7 ancestors (>= 2)

--- Check 9: Internal structure ---
  [32mREADY[0m      layer_2_group/ exists
  [32mREADY[0m      Stages directory exists
  [32mREADY[0m      12 stages present (>= 12)

--- Check 10: Generated tool files ---
  [32mREADY[0m      CLAUDE.md exists
  [32mREADY[0m      AGENTS.md exists
  [32mREADY[0m      GEMINI.md exists
  [32mREADY[0m      OPENAI.md exists

================================
  [32mREADY[0m:      35
  [31mNOT READY[0m:  0
  [33mWARN[0m:       0
================================

  [32m>>> ENTITY IS READY FOR INSTANTIATION <<<[0m

  Next steps:
    1. Populate .0agnostic/ with rules, knowledge, skills
    2. Create .claude/rules/ path rules
    3. Flesh out .gab.jsonld with modes, actors, personas
    4. Generate .integration.md from .gab.jsonld
    5. Run agnostic-sync.sh to regenerate tool files
    6. Re-run this test to verify PASS on all checks
```

</details>

---

<!-- section_id: "061e1583-2931-4569-b93f-08fee7f20511" -->
## test_codex_projection

**Status**: PASS | **Exit code**: 0
| Metric | Count |
|--------|-------|
| PASS | 10 |
| FAIL | 0 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: Codex Projection to AGENTS.md ===
Entity: layer_2_subx2_feature_context_chain_system
  [32mPASS[0m  Codex override file exists and is non-empty
  [32mPASS[0m  Codex additions file exists and is non-empty
  [32mPASS[0m  Sync succeeds
  [32mPASS[0m  AGENTS.md includes Codex override section
  [32mPASS[0m  AGENTS.md includes Codex additions section
  [32mPASS[0m  CLAUDE.md does not contain Codex override section
  [32mPASS[0m  CLAUDE.md does not contain Codex additions
  [32mPASS[0m  Re-sync with marker succeeds
  [32mPASS[0m  Marker appears in AGENTS.md
  [32mPASS[0m  Marker does not leak into CLAUDE.md

================================
  [32mPASS[0m: 10
  [31mFAIL[0m: 0
  [33mSKIP[0m: 0
================================
```

</details>

---

<!-- section_id: "4bb2102a-b88b-4970-a805-4db822826506" -->
## test_codex_discovery_chain

**Status**: PASS | **Exit code**: 0
| Metric | Count |
|--------|-------|
| PASS | 13 |
| FAIL | 0 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: Codex Discovery Chain ===
Entity: layer_2_subx2_feature_context_chain_system
  [32mPASS[0m  Sync succeeds
  [32mPASS[0m  .codex/ directory exists
  [32mPASS[0m  .1codex_merge has non-scaffold content (2 files)
  [32mPASS[0m  Codex contract file exists
  [32mPASS[0m  Contract contains: ## Discovery Temperatures
  [32mPASS[0m  Contract contains: ### Hot context
  [32mPASS[0m  Contract contains: ### Warm context
  [32mPASS[0m  Contract contains: ### Cold context
  [32mPASS[0m  Contract contains: ## Trigger Contract
  [32mPASS[0m  Contract contains: ## Validation Contract
  [32mPASS[0m  AGENTS.md has Codex trigger section
  [32mPASS[0m  Discovery prompt simulation hits >=3 trigger tokens (4/4)
  [32mPASS[0m  AGENTS.md has sync footer

================================
  [32mPASS[0m: 13
  [31mFAIL[0m: 0
  [33mSKIP[0m: 0
================================
```

</details>

---

<!-- section_id: "4b538d85-e228-4195-a112-b05081d33d03" -->
## test_codex_context_conditions

**Status**: PASS | **Exit code**: 0
| Metric | Count |
|--------|-------|
| PASS | 19 |
| FAIL | 0 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: Codex Context Conditions ===
Entity: layer_2_subx2_feature_context_chain_system
  [32mPASS[0m  Sync succeeds
  [32mPASS[0m  AGENTS.md exists
  [32mPASS[0m  AGENTS.md contains ## Identity
  [32mPASS[0m  AGENTS.md contains ## Codex CLI Configuration
  [32mPASS[0m  AGENTS.md contains ## Codex Discovery Triggers
  [32mPASS[0m  Conditional trigger framing exists
  [32mPASS[0m  Static + dynamic rules are both discoverable from AGENTS.md
  [32mPASS[0m  Trigger token present: context chain
  [32mPASS[0m  Mapped reference present in AGENTS.md: .0agnostic/01_knowledge/codex_cli_context_contract.md
  [32mPASS[0m  Mapped file exists: .0agnostic/01_knowledge/codex_cli_context_contract.md
  [32mPASS[0m  Trigger token present: agnostic-sync
  [32mPASS[0m  Mapped reference present in AGENTS.md: .0agnostic/03_protocols/chain_validation_protocol.md
  [32mPASS[0m  Mapped file exists: .0agnostic/03_protocols/chain_validation_protocol.md
  [32mPASS[0m  Trigger token present: chain-validate
  [32mPASS[0m  Mapped reference present in AGENTS.md: .0agnostic/05_skills/chain-validate/SKILL.md
  [32mPASS[0m  Mapped file exists: .0agnostic/05_skills/chain-validate/SKILL.md
  [32mPASS[0m  Trigger token present: avenue-check
  [32mPASS[0m  Mapped reference present in AGENTS.md: .0agnostic/05_skills/avenue-check/SKILL.md
  [32mPASS[0m  Mapped file exists: .0agnostic/05_skills/avenue-check/SKILL.md

================================
  [32mPASS[0m: 19
  [31mFAIL[0m: 0
  [33mSKIP[0m: 0
================================
```

</details>

---

<!-- section_id: "a8f03efc-a3f2-4530-82fb-6da6a3ebe530" -->
## test_codex_governance_runtime

**Status**: FAIL | **Exit code**: 1
| Metric | Count |
|--------|-------|
| PASS | 2 |
| FAIL | 4 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: Codex Governance Runtime ===
Entity: layer_2_group
  [32mPASS[0m  Principle single source of truth
  [32mPASS[0m  Principle lean static context
  [31mFAIL[0m  Knowledge static vs dynamic (expected: .0agnostic/01_knowledge/static_dynamic_context.md, got: <empty>)
  [31mFAIL[0m  Static rule traversal (expected: .0agnostic/02_rules/static/context_traversal.md, got: <empty>)
  [31mFAIL[0m  Dynamic rule after agnostic edits (expected: .0agnostic/02_rules/dynamic/sync_after_agnostic_edit.md, got: <empty>)
  [31mFAIL[0m  Protocol stage report (expected: .0agnostic/03_protocols/stage_report_protocol.md, got: <empty>)

================================
  [32mPASS[0m: 2
  [31mFAIL[0m: 4
  [33mSKIP[0m: 0
================================
```

</details>

---

<!-- section_id: "6dff000e-eb3d-483f-9cbb-01848537510c" -->
## test_codex_runtime_behavior

**Status**: FAIL | **Exit code**: 1
| Metric | Count |
|--------|-------|
| PASS | 0 |
| FAIL | 5 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: Codex Runtime Behavior ===
Entity: layer_2_subx2_feature_context_chain_system
  [31mFAIL[0m  Codex runtime execution failed for projection test (got: <empty>)
  [31mFAIL[0m  Codex runtime execution failed for context conditions test (got: <empty>)
  [31mFAIL[0m  Codex contract-path discovery mismatch (got: <empty>)
  [31mFAIL[0m  Codex chain-validate mapping mismatch (got: <empty>)
  [31mFAIL[0m  Codex governance behavior probe failed (got: <empty>)

================================
  [32mPASS[0m: 0
  [31mFAIL[0m: 5
  [33mSKIP[0m: 0
================================
```

</details>

---

<!-- section_id: "fa27dbd7-2ab2-4872-be75-f9a368297a50" -->
## test_codex_ci_gate

**Status**: FAIL | **Exit code**: 1
| Metric | Count |
|--------|-------|
| PASS | 4 |
| FAIL | 1 |
| SKIP | 0 |
| SCAFFOLDED | 0 |

<details>
<summary>Full output</summary>

```
=== Test: Codex CI Gate ===
Entity: layer_2_subx2_feature_context_chain_system
  [32mPASS[0m  .1codex_merge has non-scaffold content (2 files)
  [32mPASS[0m  test_codex_projection.sh passed
  [32mPASS[0m  test_codex_discovery_chain.sh passed
  [32mPASS[0m  test_codex_context_conditions.sh passed
  [31mFAIL[0m  test_codex_runtime_behavior.sh failed
=== Test: Codex Runtime Behavior ===
Entity: layer_2_subx2_feature_context_chain_system
  [31mFAIL[0m  Codex runtime execution failed for projection test (got: <empty>)
  [31mFAIL[0m  Codex runtime execution failed for context conditions test (got: <empty>)
  [31mFAIL[0m  Codex contract-path discovery mismatch (got: <empty>)
  [31mFAIL[0m  Codex chain-validate mapping mismatch (got: <empty>)
  [31mFAIL[0m  Codex governance behavior probe failed (got: <empty>)

================================
  [32mPASS[0m: 0
  [31mFAIL[0m: 5
  [33mSKIP[0m: 0
================================

================================
  [32mPASS[0m: 4
  [31mFAIL[0m: 1
================================
```

</details>

---


<!-- section_id: "a8315022-b927-46c2-82d5-963b4bfd67a3" -->
## Overall Summary

| Metric | Count |
|--------|-------|
| **Total PASS** | 215 |
| **Total FAIL** | 10 |
| **Total SKIP** | 6 |
| **Total SCAFFOLDED** | 2 |
| **Readiness Score** | 92% |

<!-- section_id: "22491cf3-7eb4-4b7a-90ed-949000fa2956" -->
### Interpretation

- **PASS**: Check is fully functional
- **FAIL**: Check failed — must be fixed before instantiation
- **SKIP**: Check was skipped (dependency unavailable)
- **SCAFFOLDED**: Structure exists but content is empty — needs population during instantiation

<!-- section_id: "509aa897-8203-4b8b-a199-1ae27174d4bc" -->
### Next Steps

**Fix 10 failing checks before instantiation.**

Review each FAIL above and resolve the underlying issue.
