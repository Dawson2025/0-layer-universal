---
resource_id: "422298d9-8661-44f2-8027-ff1a2393a23c"
resource_type: "protocol"
resource_name: "rule_testing_protocol"
---
# Rule Testing Protocol

**Scope**: Universal — applies to all rule tests at `.0agnostic/02_rules/`

<!-- section_id: "585b1d6f-fec0-472c-a6ff-66238f1d3c58" -->
## Purpose

Defines when and how to run rule compliance tests, how to track performance, and how to act on results.

<!-- section_id: "f4959238-7fd4-4021-82f2-d2a6373b2dea" -->
## When to Run

| Trigger | What to Run | Why |
|---------|-------------|-----|
| After modifying a rule | That rule's `tests/test_structural.sh` | Verify the change didn't break structural integrity |
| After running `agnostic-sync.sh` | `I0_FILE_CHANGE_REPORTING` and `AI_CONTEXT_MODIFICATION_PROTOCOL` tests | These depend on CLAUDE.md content |
| After running `sync-to-home.sh` | `HOME_SYNC` tests (when created) | Verify home directory is in sync |
| Periodic (weekly recommended) | `run_all_rule_tests.sh` | Catch drift and degradation |
| On new agent/entity setup | `run_all_rule_tests.sh` | Verify infrastructure supports rules |
| When compliance issue observed | Relevant rule's tests | Diagnose the specific failure |

<!-- section_id: "3d8c509d-3012-42d5-a8ab-beeaa5aac949" -->
## How to Run

<!-- section_id: "115741ff-d2bd-406a-8063-be494f46ab1d" -->
### Single rule
```bash
bash .0agnostic/02_rules/{category}/{rule}/tests/test_structural.sh [repo_root]
```

<!-- section_id: "e411926a-1505-4b25-a8dc-3c7ab58fa0bd" -->
### One category
```bash
bash .0agnostic/02_rules/{category}/tests/run_category_tests.sh [repo_root]
```

<!-- section_id: "8aa9b825-90ae-4d6e-bf3d-8a3bdba221ce" -->
### All rules
```bash
bash .0agnostic/02_rules/run_all_rule_tests.sh [repo_root]
```

<!-- section_id: "7daf34d4-62b8-4f1a-b0ae-62089abae9a9" -->
## Performance Tracking

Results are appended to `.0agnostic/02_rules/test_results_history.md` automatically by `run_all_rule_tests.sh`.

Track these metrics:
- **Reliability**: PASS / TOTAL across all rules (target: 90%+)
- **Trend**: Is reliability improving, stable, or declining over time?
- **Coverage**: How many rules have structural tests vs scaffolded-only?

<!-- section_id: "829129f5-4ca7-4edc-ae65-6852a0db1b29" -->
## Acting on Results

| Result | Action |
|--------|--------|
| All PASS | No action needed — record in history |
| FAIL on structural test | Fix the structural issue (missing file, broken reference, out-of-sync copy) |
| FAIL on sync test | Run `sync-to-home.sh` to re-sync, then re-run |
| SKIP (no test_structural.sh) | Low priority — write tests when the rule becomes actively validated |
| Reliability below 80% | Investigate systemic issues — are rules being maintained? |

<!-- section_id: "07932965-d150-4b55-a3c9-b58fd5f20f61" -->
## Behavioral Tests

Behavioral tests (agent compliance) cannot be automated with bash scripts. To evaluate behavioral compliance:

1. Review recent session transcripts for rule adherence
2. Use the Compliance Scoring Framework in each rule's `test_design.md`
3. Record findings in the rule's `tests/results/` directory
4. Aggregate behavioral scores periodically alongside structural results

<!-- section_id: "25d28f6d-4897-4cb9-8d3d-0d08b2fd7eed" -->
## Related

- **Master runner**: `.0agnostic/02_rules/run_all_rule_tests.sh`
- **Results history**: `.0agnostic/02_rules/test_results_history.md`
- **Rules README**: `.0agnostic/02_rules/README.md`
- **Sync script**: `.0agnostic/01_knowledge/layer_stage_system/resources/tools/sync-to-home.sh`
