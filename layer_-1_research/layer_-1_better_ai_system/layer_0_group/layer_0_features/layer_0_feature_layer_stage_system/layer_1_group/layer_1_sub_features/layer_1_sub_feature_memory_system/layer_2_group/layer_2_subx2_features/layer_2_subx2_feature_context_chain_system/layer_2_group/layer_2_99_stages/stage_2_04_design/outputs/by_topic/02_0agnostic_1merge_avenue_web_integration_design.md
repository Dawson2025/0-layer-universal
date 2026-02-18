# 0AGNOSTIC + .1merge Integration Design for the Avenue Web

## Purpose
Define how `0AGNOSTIC` (source of truth), `.1merge` (tool projections), the context chain, and the `multi_avenue_redundancy_web` connect as one architecture.

## Core Positioning
- `0AGNOSTIC` is the canonical content model.
- `.1merge` is the projection and customization model per tool.
- The Avenue Web is the runtime loading model (context chain + reference chain).

## System Components
1. `0AGNOSTIC`
- Holds canonical rules, skills, protocols, knowledge, memory conventions.
- Must remain tool-agnostic and minimal-duplication.

2. `.1merge`
- Per-tool merge trees with three tiers:
  - `0_synced` from `0AGNOSTIC`
  - `1_overrides` for tool-specific behavior
  - `2_additions` for tool-only capabilities
- Owns conflict resolution policy and final emitted files.

3. Generated Tool Files
- `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `OPENAI.md`, plus tool-native rule files.
- These are the high-reliability static context surfaces.

4. Avenue Web Runtime
- Loads static and dynamic context via the 8 MVP avenues.
- Uses references to traverse from coarse context to precise context.

5. JSON-LD Graph Family (Avenue 5 data plane)
- Layer orchestrators: `layer_*_orchestrator.gab.jsonld`
- Stage orchestrators: `layer_*_99_stages_orchestrator.gab.jsonld`
- Stage agents: `stage_*_agent.jsonld`
- Layer/feature indexes: `index.jsonld`
- GAB runtime/spec graph files used by orchestrators and agents

## How They Connect
1. Author once in `0AGNOSTIC`.
2. Merge per tool via `.1merge` (`synced -> overrides -> additions`).
3. Emit tool-native context files.
4. Runtime agent follows Avenue Web routes to load only needed context.
5. Episodic memory and updates feed back into next sessions.

## Context Chain Mapping
- Stage-level static context: generated agent files + path rules.
- Task-level dynamic context: skills, JSON-LD summaries, memory, retrieval.
- Fallback context: direct read of `0AGNOSTIC`.

## Reference Chain Mapping
- Trigger tables and path rules point to skills.
- Skills and prompts point to knowledge/integration summaries.
- Summaries point to deeper JSON-LD and source docs.
- Memory points to prior decisions and changed files.

## 8-Avenue MVP Integration Matrix
1. System prompt chain
- Source: `0AGNOSTIC` + `.1merge` emissions
- Role: static entry point

2. Path-specific rules
- Source: `.1merge` tool rule projections
- Role: automatic route selection by path

3. Skills
- Source: `0AGNOSTIC` protocols/skills
- Role: on-demand procedural loading

4. `@import` references
- Source: generated context files
- Role: progressive detail resolution

5. JSON-LD graph family
- Source: orchestrator JSON-LDs, stage-agent JSON-LDs, layer/index JSON-LDs, GAB runtime/spec JSON-LDs
- Role: structured orchestration, layer/stage routing, mode/state constraints, and graph-level references

6. `.integration.md` summaries
- Source: JSON-LD transpilation
- Role: LLM-readable operational summary

7. Episodic memory
- Source: runtime session artifacts
- Role: cross-session continuity

8. `0AGNOSTIC` fallback
- Source: canonical files
- Role: last-resort truth source

## Design Constraints
1. No tool-specific logic in canonical `0AGNOSTIC` unless unavoidable.
2. `.1merge` overrides must be explicit, scoped, and documented.
3. Every critical rule must have at least:
- one static context path and one dynamic context path
- one static reference path and one dynamic reference path
4. Emitted files must be reproducible from source + merge rules.

## Design Outputs Required by Planning
1. Merge workflow for `0_synced -> 1_overrides -> 2_additions`.
2. Generation map from source artifacts to emitted files per tool.
3. Validation checks for 8 MVP avenues.
4. Rollback strategy when generated files diverge from source.
5. JSON-LD inventory and traversal contract covering orchestrator, stage, layer, and index graph classes.
