# Stage Report: 07_testing

## Status
active

## Last Updated
2026-02-25

## Summary
Test suite now uses purpose-based output taxonomy (`outputs/by_purpose/<purpose>/{design,implementation,runs,results,insights}`) and enforces it via an automated gate. Codex-specific projection, discovery, runtime, and condition-based checks remain passing and integrated into the full-suite runner.

## Key Outputs
- `outputs/reports/stage_report.md`: Canonical stage handoff status report
- `outputs/reports/output_report.md`: Stage output navigation hub for propagation funnel
- `outputs/reports/test_results_summary.md`: Latest full suite results (200 PASS, 0 FAIL, 6 SKIP, 2 SCAFFOLDED)
- `outputs/by_purpose/README.md`: Canonical testing output taxonomy and purpose list
- `outputs/by_purpose/codex_runtime_validation/results/codex_runtime_behavior_test_report.md`: Codex runtime behavior report
- `outputs/by_purpose/reports_funnel_validation/results/latest_results.md`: Reports-funnel suite result pointer
- `outputs/by_purpose/avenue_web_validation/results/avenue_web_validation_report.md`: Avenue web validation report
- `outputs/reports/codex_runtime_validation_report.md`: Codex runtime validation and execution-mode requirement
- `outputs/test_skill_discovery_chain.md`: Skill discovery chain test — 6 checkpoints, all PASS, plus fresh agent simulation
- `outputs/test_codex_projection.sh`: Validates `.1codex_merge` -> `AGENTS.md` projection and no Claude leakage
- `outputs/test_codex_discovery_chain.sh`: Validates Codex discovery checkpoints and contract coverage
- `outputs/test_codex_context_conditions.sh`: Validates static context plus condition -> rules/protocols/skills mapping
- `outputs/test_codex_ci_gate.sh`: CI-style gate (fails when Codex merge is scaffold-only or Codex tests fail)
- `outputs/test_reports_funnel_structure.sh`: Validates canonical report locations and handoff mirror copies
- `outputs/test_outputs_purpose_taxonomy.sh`: Validates purpose/suite output structure and artifact presence
- Test scripts in `outputs/` for repeatable execution

## Findings
- Codex merge-to-output path is now functional: `.1merge/.1codex_merge/*` projects into `AGENTS.md`
- Codex projection isolation validated: Codex additions do not appear in `CLAUDE.md`
- Codex discovery chain checks pass (contract + trigger tokens + generated AGENTS footer)
- Codex condition checks pass: trigger conditions map to expected rules/protocols/skills and referenced files exist
- CI-style Codex gate passes and is integrated into `run_all_tests.sh`
- Codex runtime execution requirement is now explicit: run agent tests with `codex --dangerously-bypass-approvals-and-sandbox` to avoid sandbox-induced false negatives
- Stage testing outputs are now canonicalized by purpose and suite phase; `by_topic` is retained as compatibility only
- Stage reporting now follows canonical `outputs/reports/` + `.0agnostic/05_handoff_documents/02_outgoing/` mirror pattern for funnel propagation
- agnostic-sync.sh correctly generates all 4 tool files + validates .0agnostic/ references
- Chain integrity validated across 7 levels
- **Skill discovery chain (Claude) remains validated**: Hot (CLAUDE.md) -> Warm (path rules) -> Cold (rules/skills)

## Open Items
- A7 episodic memory remains scaffolded (sessions/changes directories exist but may be empty)
- macOS mirror of claude_in_chrome not yet migrated to .0agnostic/ convention (consistency issue)
- agnostic-sync.sh validation reports 29 warnings on root 0AGNOSTIC.md (old format, needs comprehensive update — separate task)
- Add CI/runtime wrapper to enforce `--dangerously-bypass-approvals-and-sandbox` for Codex runtime validation jobs

## Handoff
- **Ready for next stage**: yes for Codex projection feature set
- **Next stage**: 08_criticism (review quality and completeness)
- **What next stage needs to know**: Codex projection/discovery/conditions/runtime tests and gate are in place and passing; testing outputs are now organized under `outputs/by_purpose/<purpose>/{design,implementation,runs,results,insights}`; `by_topic` is compatibility-only; Codex runtime validation should always run with `--dangerously-bypass-approvals-and-sandbox`; aggregate suite currently reports 0 FAIL
