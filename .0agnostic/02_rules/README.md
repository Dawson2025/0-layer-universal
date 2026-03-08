---
resource_id: "f2aabe29-7fdd-4057-aea3-6a1a2b6c0fc8"
resource_type: "readme_rule"
resource_name: "README"
---
# Rules — Universal Rule System

<!-- section_id: "e8fa64a8-62b0-4006-9bbf-978937091381" -->
## Structure

Rules are organized by **activation category**, and each rule lives in its own directory with co-located tests.

| Category | Path | When Rules Apply |
|----------|------|-----------------|
| Every API Request | `0_every_api_request/` | Loaded on every AI agent turn, unconditionally |
| Static | `static/` | Always active once loaded — behavioral constraints |
| Dynamic | `dynamic/` | Triggered by specific conditions or scenarios |
| Scenario-Based | `1_scenario_based/` | Read on-demand when a matching scenario is detected |

<!-- section_id: "5391248e-d082-4535-9f02-592b46d585c2" -->
## Per-Rule Directory Structure

Every rule follows this structure:

```
rule_name/
├── rule_name.md          <- The rule itself
└── tests/
    ├── test_design.md    <- Test case definitions (what to verify)
    ├── test_structural.sh <- Automated structural verification
    └── results/          <- Test run outputs (timestamped)
```

<!-- section_id: "148cbe07-0b74-435a-9edc-e5f875d28cad" -->
## Testing

- **Run all tests**: `bash run_all_rule_tests.sh`
- **Run one category**: `bash {category}/tests/run_category_tests.sh`
- **Performance history**: `test_results_history.md`
- **Testing protocol**: `../03_protocols/rule_testing_protocol.md`

<!-- section_id: "ad297a4d-5d2f-4cfe-baaf-4daa3c418f60" -->
## Rules Index

| Rule | Category | Hot? | Purpose |
|------|----------|------|---------|
| AI_CONTEXT_MODIFICATION_PROTOCOL | every_api_request | No | Two-tier filesystem change visualization |
| I0_FILE_CHANGE_REPORTING | static | Yes | Report file changes with full absolute paths |
| agnostic_update_protocol | static | No | Sync chain for .0agnostic/ modifications |
| MANAGER_DELEGATION_RULE | static | No | Managers delegate, don't operate |
| STAGE_BOUNDARY_RULE | static | No | Stage agents stay within stage scope |
| STAGE_REPORT_RULE | static | No | All stage agents write stage reports |
| browser_extraction_rule | dynamic | No | Use Chrome for React-rendered pages |
| I0_source_of_truth_rule | dynamic | No | 0AGNOSTIC.md is the source of truth |
| PARALLEL_STAGES_RULE | dynamic | No | Rules for parallel stages |
| STAGE_LOOP_RULE | dynamic | No | Stage looping (test-fix-retest) |
| safety_governance | scenario | No | Security decision framework |
| LAYER_CONTEXT_HEADER_PROTOCOL | scenario | No | File header conventions |
| sequential_development_methodology | scenario | No | Multi-step development workflow |
| CROSS_OS_COMPATIBILITY_RULES | scenario | No | Cross-platform requirements |
