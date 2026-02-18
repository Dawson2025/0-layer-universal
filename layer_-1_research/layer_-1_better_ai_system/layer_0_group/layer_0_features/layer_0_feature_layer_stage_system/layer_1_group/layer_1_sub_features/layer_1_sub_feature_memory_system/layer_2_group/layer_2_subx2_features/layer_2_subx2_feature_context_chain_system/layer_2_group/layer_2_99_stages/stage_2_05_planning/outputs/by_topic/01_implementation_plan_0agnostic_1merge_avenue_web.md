# Implementation Plan: 0AGNOSTIC + .1merge + Avenue Web

## Objective
Implement and validate the 8-avenued MVP using `0AGNOSTIC` as source, `.1merge` as projection, and the Avenue Web as runtime behavior.

## Scope
In scope:
- End-to-end MVP implementation of all 8 current avenues.
- Merge pipeline definition and validation for at least core tools.
- Stage-level acceptance checks and rollback plan.

Out of scope:
- Full post-MVP advanced avenues (A2A, telemetry, policy, provenance).
- Deep per-tool optimization beyond baseline correctness.

## Workstreams
1. Source Modeling
- Normalize canonical content in `0AGNOSTIC` for rules, skills, knowledge, memory, and references.
- Ensure each critical rule has both context-chain and reference-chain routes.
- Build a JSON-LD inventory by class:
  - layer orchestrators
  - stage orchestrators
  - stage agents
  - layer/feature indexes
  - GAB runtime/spec graph files

2. Merge Pipeline
- Define merge precedence: `0_synced -> 1_overrides -> 2_additions`.
- Document conflict policy and deterministic merge behavior.
- Define expected emitted artifacts per tool.

3. Emission and Sync
- Generate/update tool files from merge outputs.
- Validate deterministic regeneration (same input -> same output).

4. MVP Avenue Enablement
- Avenue 1: system prompt chain present and points to next routes.
- Avenue 2: path rules load for matching contexts.
- Avenue 3: skills are discoverable and invocable.
- Avenue 4: `@import` links resolve correctly.
- Avenue 5: JSON-LD query/read path works.
- Avenue 6: `.integration.md` exists and matches JSON-LD semantics.
- Avenue 7: episodic memory read/write path works.
- Avenue 8: direct `0AGNOSTIC` fallback works when projections are absent.

5. Verification and QA
- Build an avenue validation matrix by tool and by stage trigger.
- Build a JSON-LD validation matrix by graph class and query type (discovery, lookup by id, mode extraction, transition extraction).
- Run scenario tests:
  - fresh task bootstrap
  - path-triggered work
  - skill-triggered deep dive
  - compaction/restart recovery
  - fallback path activation

6. Adoption and Rollout
- Start with primary tools (Claude/Codex/Cursor/Gemini).
- Expand to remaining tool projections after baseline passes.

## Milestones
1. M1 - Canonical + Merge Spec Complete
- Deliverables: source map, merge policy, emission map, JSON-LD class inventory.

2. M2 - 8 Avenue Wiring Complete
- Deliverables: all 8 avenues connected and traceable.

3. M3 - Validation Complete
- Deliverables: passed test matrix for primary tools.

4. M4 - Rollout + Monitoring
- Deliverables: adoption checklist, divergence/rollback process.

## Acceptance Criteria
1. All 8 MVP avenues pass at least one end-to-end scenario each.
2. Merge outputs are deterministic and reproducible.
3. Generated tool files are traceable back to source and merge tier.
4. Failure in any single avenue does not block context loading.
5. Documented fallback to `0AGNOSTIC` verified in test.
6. Avenue 5 passes for all required JSON-LD classes (orchestrator, stage, layer/index, GAB runtime/spec).

## Risks and Mitigations
1. Merge drift across tools
- Mitigation: regenerate and diff checks in CI.

2. Missing references in emitted files
- Mitigation: link validation pass for imports and pointers.

3. Skill trigger variance across tools
- Mitigation: dual route (path rules + explicit invocation guidance).

4. Context bloat
- Mitigation: progressive disclosure defaults and compaction-safe subset.

## Execution Order (High Level)
1. Finalize design artifacts in Stage 2.04.
2. Build merge/emission specification.
3. Wire and test the 8 MVP avenues.
4. Validate primary tools.
5. Roll out and monitor.
6. Queue post-MVP advanced avenues.

## Post-MVP Queue
1. Advanced MCP primitives and richer docs retrieval.
2. Telemetry-as-context and policy-as-context.
3. Provenance/identity controls.
4. Multi-agent/A2A orchestration expansion.
