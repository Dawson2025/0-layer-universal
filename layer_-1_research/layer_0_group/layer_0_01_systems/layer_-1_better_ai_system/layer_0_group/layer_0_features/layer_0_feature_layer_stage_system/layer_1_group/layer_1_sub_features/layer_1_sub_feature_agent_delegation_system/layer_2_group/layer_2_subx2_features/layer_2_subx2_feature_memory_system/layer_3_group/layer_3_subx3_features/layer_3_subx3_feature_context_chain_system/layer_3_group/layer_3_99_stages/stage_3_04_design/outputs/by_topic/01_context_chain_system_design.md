# Context Chain System - Stage 2.04 Design

## Purpose
Define the technical design for implementing the `multi_avenue_redundancy_web` (Avenue Web / Web of Avenues) in the context chain system.

## Stage Order Rule
Design must execute before planning.

- Intended workflow order: request gathering -> research -> instructions -> design -> planning -> development -> testing -> criticism -> fixing -> current product -> archives.
- Stage directory numbering now aligns with intended order: `stage_3_04_design` before `stage_3_05_planning`.
- Execution precedence for this feature: **run Stage 2.04 Design outputs first, then Stage 2.05 Planning**.

## Scope
In scope:
- Context chaining and reference chaining architecture.
- Static and dynamic context loading pathways.
- Portable cross-tool mechanisms with tool-specific extensions.
- Design handoff contract for planning stage.

Out of scope:
- Detailed task sequencing, sprint breakdown, and time estimates (planning stage).
- Implementation code changes (development stage).

## Design Goals
1. Reliability: critical context must be reachable through redundant avenues.
2. Portability: maximize cross-tool compatibility.
3. Progressive disclosure: load minimal context first, deeper context on demand.
4. Compaction safety: preserve critical context through context compression.
5. Governance readiness: allow policy, identity, and provenance controls.

## Core Design Model
The system is modeled as a graph:
- Nodes: context artifacts (AGENTS.md, rules, skills, resources, memory, docs).
- Edges: reference links and trigger routes.
- Gateways: tools/protocol calls (MCP tools, hooks, search, CI, telemetry).

Two mandatory chain types:
- Context chaining: loads the right content for the current task.
- Reference chaining: routes to the next source/tool/query with low token cost.

## Architecture Layers
1. Static Context Layer
- `0AGNOSTIC.md`
- Generated tool files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `OPENAI.md`)
- Path rules and static knowledge references

2. Dynamic Retrieval Layer
- Skills and prompts
- Semantic search/indexing
- Session/episodic memory
- CI feedback and web/docs retrieval

3. Orchestration Layer
- MCP server (resources/prompts/tools)
- Advanced MCP primitives (roots, elicitation, sampling, list_changed)
- Hooks and policy checks
- Subagent delegation / A2A handoffs (where available)

4. Trust and Governance Layer
- Policy-as-context gates (allow/deny context/tool usage)
- Provenance metadata for context sources
- Agent identity assertions for controlled environments

## Canonical Propagation Contract
`0AGNOSTIC` canonical classes (knowledge, principles, rules, protocols) must propagate into runtime context through sync + merge:

1. Canonical authoring in `0AGNOSTIC`.
2. Sync into `.1merge/*/0_synced`.
3. Tool adaptation in `.1merge/*/1_overrides` and `.1merge/*/2_additions`.
4. Emission to tool-facing context files.
5. Runtime loading via Avenue Web (context chaining + reference chaining).

Design requirement:
- Every critical principle/rule/protocol must be traceable from runtime artifact back to canonical source path and merge tier.

## Canonical Filesystem Contract (.0agnostic)
The design must include an explicit canonical filesystem model for source classes and routing metadata.

Required canonical class surfaces:
- `.0agnostic/knowledge/`
- `.0agnostic/principles/`
- `.0agnostic/rules/`
- `.0agnostic/protocols/`

Required system surfaces:
- `.0agnostic/hooks/` (sync/validation/compaction hooks)
- `.0agnostic/episodic_memory/` (cross-session memory)
- `.0agnostic/sync-config.yaml` (projection rules)

Required design behavior:
- Canonical class paths are tool-agnostic sources only.
- Tool-specific behavior is encoded in `.1merge`.
- Emitted tool files must include source traceability to canonical class and merge tier.

## Minimum Viable Avenue Set (MVP)
MVP required before planning can start: implement all current 8 core avenues of the Avenue Web.

1. System prompt chain (`CLAUDE.md` / `AGENTS.md` / `GEMINI.md`)
2. Path-specific rules
3. Skills (progressive disclosure)
4. `@import` reference chaining
5. JSON-LD graph family (`.gab.jsonld` and related `.jsonld` via jq/native parsing)
6. Integration summaries (`.integration.md`)
7. Episodic memory
8. Direct source fallback (`0AGNOSTIC.md`)

Post-MVP expansion (after the 8 are validated end-to-end):
1. MCP resources/prompts/tools and advanced MCP primitives
2. Semantic search and indexing
3. Policy/telemetry/provenance extensions

## Design Decisions
1. Canonical term: `multi_avenue_redundancy_web`.
- Synonyms kept for readability: Avenue Web, Web of Avenues.

2. Enforce dual-path reachability.
- Each critical instruction requires:
  - one static + one dynamic context chain path
  - one static + one dynamic reference chain path

3. Prioritize MCP-centered portability.
- MCP is first-class integration surface.
- Tool-native features are additive, not foundational.

4. Separate design from planning artifacts.
- Design defines architecture and constraints.
- Planning consumes design and produces sequencing/execution plan.

5. Treat JSON-LD as a graph family, not a single file type.
- Include all relevant classes in Avenue 5:
  - layer orchestrators (`layer_*_orchestrator.gab.jsonld`)
  - stage orchestrators (`layer_*_99_stages_orchestrator.gab.jsonld`)
  - stage agents (`stage_*_agent.jsonld`)
  - layer/feature indexes (`index.jsonld`)
  - GAB runtime/spec files used by orchestrators (`gab.jsonld`, `gab-runtime.jsonld`, `gab-formats.jsonld`, equivalent project variants)

6. Treat JSON-LD + integration summaries as one enforced pair.
- Every JSON-LD graph artifact in active hierarchy must have a matching `.integration.md`.
- Integration summaries are generated artifacts and must not drift from JSON-LD semantics.

7. Enforce static-chain budget and compaction-safe subset.
- Keep always-loaded static chain compact; move deep detail behind reference chains.
- Define and preserve a compaction-safe subset (identity, critical rules, active stage pointers, fallback routes).

## JSON-LD Coverage Contract (Avenue 5)
Design-time coverage must include all runtime-relevant graph classes, including orchestrator families identified in research:
- layer orchestrators: `layer_*_orchestrator.gab.jsonld`
- stage orchestrators: `layer_*_99_stages_orchestrator.gab.jsonld`
- stage agents: `stage_*_agent.jsonld`
- layer/feature/stage indexes: `index.jsonld`
- runtime/spec graphs: `gab.jsonld`, `gab-runtime.jsonld`, `gab-formats.jsonld`
- orchestrator project variants (including gabwork/orchestrator-specific variants where present)

Validation rule:
- Avenue 5 passes only when required graph classes are discoverable.
- Avenue 6 passes only when all discovered graph files have matching integration summaries.

## Handoff Contract to Planning Stage
Planning inputs required from this design stage:
1. Canonical architecture and layer model
2. Baseline avenue set and ranked expansion order
3. Acceptance criteria and non-goals
4. Risk register with mitigations

Planning must not redefine architecture unless new constraints are documented.

## Acceptance Criteria for Stage 2.04
1. Architecture layers and interfaces are explicitly documented.
2. Context chaining and reference chaining are explicitly distinguished.
3. All 8 MVP avenues are defined and testable.
4. Design-to-planning handoff contract is defined.
5. Stage order rule is explicit: design before planning.

## Risks and Mitigations
1. Stage-order confusion due to directory numbering.
- Mitigation: keep explicit precedence rule in both design and planning files.

2. Overfitting to one tool.
- Mitigation: treat MCP + agnostic files as primary interface.

3. Context bloat.
- Mitigation: progressive disclosure plus compaction-safe context subset.

4. Inconsistent team behavior.
- Mitigation: generated team docs and sync process from `0AGNOSTIC.md`.

5. Static chain inflation reduces reliability.
- Mitigation: enforce static-chain budget and push detail to reference-chained dynamic routes.

6. JSON-LD coverage blind spots (missing orchestrator variants).
- Mitigation: class-based JSON-LD inventory and validation, not hardcoded single-file assumptions.

## Ranked Avenue Expansion (Post-MVP)
After the 8-avenued MVP is stable, use this ranked expansion order:

Tier 1 (next):
1. MCP resources/prompts/tools
2. Team context distribution automation
3. Compaction hooks and recovery surfaces

Tier 2:
1. Semantic search/indexing
2. Documentation APIs
3. Plugin/extension packaging

Tier 3:
1. CI/CD feedback loops
2. LSP-backed context assist
3. Multi-agent isolation patterns

## Next Artifact (Planning Stage)
Planning should produce:
- implementation phases
- milestone gates
- test matrix
- rollback strategy
- ownership mapping

All planning items must trace back to a design section in this document.
