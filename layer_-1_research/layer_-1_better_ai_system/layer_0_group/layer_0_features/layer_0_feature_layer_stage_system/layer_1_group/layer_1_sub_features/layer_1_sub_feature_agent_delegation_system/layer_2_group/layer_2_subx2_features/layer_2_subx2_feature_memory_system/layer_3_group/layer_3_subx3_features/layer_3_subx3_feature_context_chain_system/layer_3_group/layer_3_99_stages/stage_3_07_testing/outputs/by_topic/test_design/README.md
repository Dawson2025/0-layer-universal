# Test Design Index

Tests designed for the 6 new context propagation design documents (docs 03-08 in `stage_3_04_design/outputs/by_topic/`).

## Coverage Map

| Design Doc | Test Design | Existing Coverage | New Tests |
|------------|-------------|-------------------|-----------|
| 03 Propagation Chain | `test_design_03_propagation_chain.md` | Partial (chain traversal, agnostic-sync) | 4-layer chain validation, chain integrity rules |
| 04 Consolidation Funnel | `test_design_04_consolidation_funnel.md` | None | Stage funnel structure, cross-level report flow, sync-handoffs |
| 05 Hierarchy Inheritance | `test_design_05_hierarchy_inheritance.md` | Partial (CLAUDE.md cascade) | Hot rule promotion, parent ref consistency, gap detection |
| 06 Source-to-Avenue Flow | `test_design_06_source_to_avenue.md` | Partial (avenue coverage) | Numbering consistency, loading order, authority direction |
| 07 Sync Architecture | `test_design_07_sync_architecture.md` | Partial (agnostic-sync only) | All 5 sync scripts, dependency order, registry |
| 08 Discovery Temperatures | `test_design_08_discovery_temperatures.md` | Partial (skill discovery chain) | Hot/Warm/Cold structural, promotion system, hook, token budget |

## Test Types

- **Structural (bash scripts)**: File existence, content patterns, directory structure — automatable, repeatable
- **Behavioral (manual/agent)**: Agent discovery simulation, correct loading order — requires agent execution
- **Integration (bash scripts)**: End-to-end sync pipelines, cross-entity propagation — automatable

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
