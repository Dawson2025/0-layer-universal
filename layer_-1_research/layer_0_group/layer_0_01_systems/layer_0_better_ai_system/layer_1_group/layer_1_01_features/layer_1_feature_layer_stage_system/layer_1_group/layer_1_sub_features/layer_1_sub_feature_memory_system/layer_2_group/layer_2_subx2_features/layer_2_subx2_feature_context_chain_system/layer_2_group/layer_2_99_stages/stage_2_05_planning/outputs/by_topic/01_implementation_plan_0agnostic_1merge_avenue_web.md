---
resource_id: "ba6c99fa-ec1d-4d0f-b493-b8f9ef2544f8"
resource_type: "output"
resource_name: "01_implementation_plan_0agnostic_1merge_avenue_web"
---
# Implementation Plan: 0AGNOSTIC + .1merge + Avenue Web

<!-- section_id: "a18762e8-4e06-41d4-812c-acf6cc8eb246" -->
## Objective
Implement and validate the 8-avenued MVP using `0AGNOSTIC` as source, `.1merge` as projection, and the Avenue Web as runtime behavior.

<!-- section_id: "4fe8a8fc-7ec7-43d4-9694-edff2b66912a" -->
## Scope
In scope:
- End-to-end MVP implementation of all 8 current avenues.
- Merge pipeline definition and validation for at least core tools.
- Stage-level acceptance checks and rollback plan.

Out of scope:
- Full post-MVP advanced avenues (A2A, telemetry, policy, provenance).
- Deep per-tool optimization beyond baseline correctness.

<!-- section_id: "571b6cf1-2ea6-4c7d-a8c3-efe334beec84" -->
## Workstreams
1. Source Modeling
- Normalize canonical content in `0AGNOSTIC` for rules, skills, knowledge, memory, and references.
- Ensure each critical rule has both context-chain and reference-chain routes.
- Establish canonical class filesystem structure under `.0agnostic`:
  - `knowledge/`, `principles/`, `rules/`, `protocols/`
  - with explicit source ownership and traceability requirements
- Build a JSON-LD inventory by class:
  - layer orchestrators
  - stage orchestrators
  - stage agents
  - layer/feature indexes
  - GAB runtime/spec graph files
  - orchestrator project variants (including gabwork/orchestrator-specific variants where present)

2. Merge Pipeline
- Define merge precedence: `0_synced -> 1_overrides -> 2_additions`.
- Document conflict policy and deterministic merge behavior.
- Define expected emitted artifacts per tool.
- Map canonical classes (`knowledge`, `principles`, `rules`, `protocols`) to emitted artifact targets per tool.

3. Emission and Sync
- Generate/update tool files from merge outputs.
- Validate deterministic regeneration (same input -> same output).
- Add traceability metadata or mapping table: runtime artifact -> merge tier -> canonical source.
- Add transpilation validation: each JSON-LD in active hierarchy has matching `.integration.md`.
- Add static-chain budget validation for always-loaded context files.

4. MVP Avenue Enablement
- Avenue 1: system prompt chain present and points to next routes.
- Avenue 2: path rules load for matching contexts.
- Avenue 3: skills are discoverable and invocable.
- Avenue 4: `@import` links resolve correctly.
- Avenue 5: JSON-LD query/read path works.
- Avenue 6: `.integration.md` exists and matches JSON-LD semantics.
- Avenue 7: episodic memory read/write path works.
- Avenue 8: direct `0AGNOSTIC` fallback works when projections are absent.
- Verify static-to-dynamic bridge behavior:
  - static principles/rules/protocols route to dynamic retrieval where needed
  - dynamic retrieval does not bypass canonical constraints

5. Verification and QA
- Build an avenue validation matrix by tool and by stage trigger.
- Build a JSON-LD validation matrix by graph class and query type (discovery, lookup by id, mode extraction, transition extraction).
- Build a propagation validation matrix:
  - canonical class -> synced artifact -> merged output -> runtime load path
  - include both context chain and reference chain validation cases
- Run scenario tests:
  - fresh task bootstrap
  - path-triggered work
  - skill-triggered deep dive
  - compaction/restart recovery
  - fallback path activation
  - compaction-safe context rehydration

7. Research Gap Closure
- Translate research constraints into executable checks:
  - no canonical-class omissions in `.0agnostic`
  - no JSON-LD/integration summary drift
  - no unbounded static-chain growth
- Add per-tool best-fit validation profile:
  - static-first tools (Copilot/Amazon Q-class) must pass with minimal dynamic dependency
  - dynamic-capable tools (Claude/Codex/Cursor/Gemini-class) must pass both static and dynamic routes

6. Adoption and Rollout
- Start with primary tools (Claude/Codex/Cursor/Gemini).
- Expand to remaining tool projections after baseline passes.
- For each tool/app, define a best-fit route profile:
  - primary static surfaces
  - primary dynamic surfaces
  - required fallback routes

<!-- section_id: "a56bcbaa-72e2-4506-bf49-200343de0796" -->
## Milestones
1. M1 - Canonical + Merge Spec Complete
- Deliverables: source map, merge policy, emission map, JSON-LD class inventory, canonical-class propagation map.

2. M2 - 8 Avenue Wiring Complete
- Deliverables: all 8 avenues connected and traceable.

3. M3 - Validation Complete
- Deliverables: passed test matrix for primary tools.

4. M4 - Rollout + Monitoring
- Deliverables: adoption checklist, divergence/rollback process.

5. M5 - Cross-Tool Best-Fit Profiles
- Deliverables: per-tool avenue routing profiles and pass/fail validation evidence.

6. M6 - Research Alignment Closure
- Deliverables: checklist showing each major research requirement is either implemented, deferred with rationale, or explicitly out of scope.

<!-- section_id: "c6ad36ec-f8d9-4d87-9056-69ea2af96bfc" -->
## Acceptance Criteria
1. All 8 MVP avenues pass at least one end-to-end scenario each.
2. Merge outputs are deterministic and reproducible.
3. Generated tool files are traceable back to source and merge tier.
4. Failure in any single avenue does not block context loading.
5. Documented fallback to `0AGNOSTIC` verified in test.
6. Avenue 5 passes for all required JSON-LD classes (orchestrator, stage, layer/index, GAB runtime/spec).
7. Knowledge/principles/rules/protocols propagation is verified end-to-end (source -> sync -> merge -> runtime).
8. Static-to-dynamic bridging is verified for both context chaining and reference chaining.
9. Each supported tool/app has a documented best-fit Avenue Web route profile and validated fallback behavior.
10. JSON-LD coverage includes orchestrator variants (layer/stage/runtime/spec/gabwork variants where present), and each has a matching integration summary.
11. Static-chain budget and compaction-safe subset checks pass.

<!-- section_id: "1aad5769-3e30-4af7-b2b0-3b1b2d0ea83d" -->
## Risks and Mitigations
1. Merge drift across tools
- Mitigation: regenerate and diff checks in CI.

2. Missing references in emitted files
- Mitigation: link validation pass for imports and pointers.

3. Skill trigger variance across tools
- Mitigation: dual route (path rules + explicit invocation guidance).

4. Context bloat
- Mitigation: progressive disclosure defaults and compaction-safe subset.

<!-- section_id: "88316fe8-a48c-4d25-9080-82419c7fb353" -->
## Execution Order (High Level)
1. Finalize design artifacts in Stage 2.04.
2. Build merge/emission specification.
3. Wire and test the 8 MVP avenues.
4. Validate primary tools.
5. Roll out and monitor.
6. Queue post-MVP advanced avenues.

<!-- section_id: "c80197de-e02a-4684-9f42-a044f778bae9" -->
## Post-MVP Queue
1. Advanced MCP primitives and richer docs retrieval.
2. Telemetry-as-context and policy-as-context.
3. Provenance/identity controls.
4. Multi-agent/A2A orchestration expansion.
