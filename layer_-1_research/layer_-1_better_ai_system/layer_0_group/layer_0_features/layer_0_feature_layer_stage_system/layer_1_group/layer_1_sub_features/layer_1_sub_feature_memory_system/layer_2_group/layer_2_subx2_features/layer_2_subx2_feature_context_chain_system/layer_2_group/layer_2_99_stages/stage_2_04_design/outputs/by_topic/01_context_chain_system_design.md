# Context Chain System - Stage 2.04 Design

## Purpose
Define the technical design for implementing the `multi_avenue_redundancy_web` (Avenue Web / Web of Avenues) in the context chain system.

## Stage Order Rule
Design must execute before planning.

- Intended workflow order: request gathering -> research -> instructions -> design -> planning -> development -> testing -> criticism -> fixing -> current product -> archives.
- Stage directory numbering now aligns with intended order: `stage_2_04_design` before `stage_2_05_planning`.
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

## Minimum Viable Avenue Set (MVP)
MVP required before planning can start: implement all current 8 core avenues of the Avenue Web.

1. System prompt chain (`CLAUDE.md` / `AGENTS.md` / `GEMINI.md`)
2. Path-specific rules
3. Skills (progressive disclosure)
4. `@import` reference chaining
5. JSON-LD agent definitions (`.gab.jsonld` via jq/native parsing)
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

## Next Artifact (Planning Stage)
Planning should produce:
- implementation phases
- milestone gates
- test matrix
- rollback strategy
- ownership mapping

All planning items must trace back to a design section in this document.
