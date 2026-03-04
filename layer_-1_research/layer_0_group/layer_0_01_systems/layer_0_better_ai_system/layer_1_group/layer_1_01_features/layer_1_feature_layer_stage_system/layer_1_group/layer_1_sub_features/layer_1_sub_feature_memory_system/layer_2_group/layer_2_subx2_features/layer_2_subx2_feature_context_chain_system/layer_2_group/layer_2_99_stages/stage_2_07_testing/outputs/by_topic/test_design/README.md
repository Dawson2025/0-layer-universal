# Test Design Index

Tests designed for all 8 context chain system design documents (docs 01-08 in `stage_2_04_design/outputs/by_topic/`).

## Coverage Map

| Design Doc | Test Design | Existing Coverage | New Tests |
|------------|-------------|-------------------|-----------|
| 01 Context Chain System Design | `test_design_01_context_chain_system.md` | Partial (avenue coverage, chain traversal) | 4-layer validation, dual-path reachability, JSON-LD contract, compaction-safe subset |
| 02 0AGNOSTIC + .1merge Integration | `test_design_02_0agnostic_1merge_integration.md` | Partial (.1merge structure, agnostic-sync) | Propagation pipeline, 3-tier merge, scoping, reproducibility, cross-tool |
| 03 Propagation Chain | `test_design_03_propagation_chain.md` | Partial (chain traversal, agnostic-sync) | 4-layer chain validation, chain integrity rules |
| 04 Consolidation Funnel | `test_design_04_consolidation_funnel.md` | None | Stage funnel structure, cross-level report flow, sync-handoffs, app-specific propagation |
| 05 Hierarchy Inheritance | `test_design_05_hierarchy_inheritance.md` | Partial (CLAUDE.md cascade) | Hot rule promotion, parent ref consistency, gap detection |
| 06 Source-to-Avenue Flow | `test_design_06_source_to_avenue.md` | Partial (avenue coverage) | Numbering consistency, loading order, authority direction |
| 07 Sync Architecture | `test_design_07_sync_architecture.md` | Partial (agnostic-sync only) | All 5 sync scripts, dependency order, registry |
| 08 Discovery Temperatures | `test_design_08_discovery_temperatures.md` | Partial (skill discovery chain) | Hot/Warm/Cold structural, promotion system, hook, token budget |

## Test Types

- **Structural (bash scripts)**: File existence, content patterns, directory structure — automatable, repeatable
- **Behavioral (manual/agent)**: Agent discovery simulation, correct loading order — requires agent execution
- **Integration (bash scripts)**: End-to-end sync pipelines, cross-entity propagation — automatable

## Codex Runtime Mode Requirement

- For Codex agent runtime validation in this stage, always run with:
  - `codex --dangerously-bypass-approvals-and-sandbox` (or `codex exec --dangerously-bypass-approvals-and-sandbox ...`)
- Rationale: sandboxed mode can block sync/write operations and produce false negatives unrelated to context-chain correctness.
- See `outputs/by_topic/codex_runtime_validation_report.md` for command patterns and evidence.

## Test Case Summary

| Design Doc | Test Cases | Structural | Integration | Behavioral |
|------------|-----------|------------|-------------|------------|
| 01 | 8 (TC-01-01 to TC-01-08) | 6 | 1 | 0 |
| 02 | 10 (TC-02-01 to TC-02-10) | 5 | 5 | 0 |
| 03 | 7 (TC-03-01 to TC-03-07) | 5 | 2 | 0 |
| 04 | 17 (TC-04-01 to TC-04-17) | 9 | 8 | 0 |
| 05 | 8 (TC-05-01 to TC-05-08) | 7 | 1 | 0 |
| 06 | 7 (TC-06-01 to TC-06-07) | 7 | 0 | 0 |
| 07 | 8 (TC-07-01 to TC-07-08) | 2 | 6 | 0 |
| 08 | 10 (TC-08-01 to TC-08-10) | 7 | 2 | 0 |
| **Total** | **75** | **48** | **25** | **0** |

## Relationship to Existing Tests

These complement the existing 76-PASS suite. Existing tests focus on entity scaffolding. These new tests focus on **propagation mechanics** — how context actually moves through the hierarchy.

| Existing Test | What It Covers | What It Misses |
|---------------|---------------|----------------|
| test_agnostic_sync | Tool file generation | .1merge injection, hot rule promotion |
| test_context_chain_traversal | Parent chain, CLAUDE.md cascade | Content propagation (not just existence) |
| test_avenue_coverage_functional | Avenue existence | Avenue ordering, comprehensiveness |
| test_1merge_structure | Directory structure | Content flow through 3 tiers |
| test_instantiation_readiness | Entity scaffolding | Operational readiness post-instantiation |
| test_skill_discovery_chain | Hot/Warm/Cold for one skill | Systematic temperature validation |

## Cross-References Between Test Designs

Several test cases across different designs validate overlapping concepts:

| Concept | Primary Test | Also Covered By |
|---------|-------------|-----------------|
| 8 MVP avenues exist | TC-01-02 | TC-02-10, TC-06-03, TC-06-04 |
| .1merge 3-tier structure | TC-02-02 | TC-03-04 |
| CLAUDE.md auto-generated footer | TC-02-07 | TC-03-03, TC-03-07 |
| Hot rule promotion | TC-05-03, TC-05-04 | TC-08-07 |
| Static→dynamic bridging | TC-02-06 | TC-01-05, TC-08-05 |
| Avenue 5/6 pairing | TC-01-03 | TC-01-04 |
| .1merge scoping (no cross-app leak) | TC-04-11 | TC-02-03 |
| Content profiles (Full/Medium/Lean) | TC-04-10 | TC-08-02 |
| App config directories | TC-04-12 | TC-04-13 |
| Complete pipeline (.0agnostic→app) | TC-04-14 | TC-02-01 |
