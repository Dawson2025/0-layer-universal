---
resource_id: "d2410ee1-56af-4c52-855f-735ec86b9b2c"
resource_type: "output"
resource_name: "02_0agnostic_1merge_avenue_web_integration_design"
---
# 0AGNOSTIC + .1merge Integration Design for the Avenue Web

<!-- section_id: "4903cb42-c581-4b89-977f-af81d74e98df" -->
## Purpose
Define how `0AGNOSTIC` (source of truth), `.1merge` (tool projections), the context chain, and the `multi_avenue_redundancy_web` connect as one architecture.

<!-- section_id: "3ac1d932-0c1f-4c50-af3d-13ad27a9129b" -->
## Core Positioning
- `0AGNOSTIC` is the canonical content model.
- `.1merge` is the projection and customization model per tool.
- The Avenue Web is the runtime loading model (context chain + reference chain).

<!-- section_id: "5e8882ad-2128-428e-94a3-a5d22c43ab98" -->
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

<!-- section_id: "ba88d468-bf8e-4ab6-9b40-b956622ed6d0" -->
## How They Connect
1. Author once in `0AGNOSTIC`.
2. Merge per tool via `.1merge` (`synced -> overrides -> additions`).
3. Emit tool-native context files.
4. Runtime agent follows Avenue Web routes to load only needed context.
5. Episodic memory and updates feed back into next sessions.

<!-- section_id: "f45baa20-3b35-4569-b3d0-d42a82601cb0" -->
## Propagation Model: 0AGNOSTIC -> Sync -> .1merge -> Avenue Web
Canonical content classes in `0AGNOSTIC`:
- knowledge
- principles
- rules
- protocols

Propagation pipeline:
1. Author/update canonical content in `0AGNOSTIC` trees.
2. Run sync (`agnostic-sync.sh`) to copy canonical artifacts into `.1merge/*/0_synced`.
3. Apply tool-specific adjustments in `.1merge/*/1_overrides`.
4. Add tool-only capabilities in `.1merge/*/2_additions`.
5. Emit final tool files (system prompt docs, rules, skills, imports, memory surfaces).
6. Runtime agent consumes emitted files through Avenue Web routes.

This keeps one source of truth while allowing controlled tool specialization.

<!-- section_id: "d43e4c24-e267-473c-afc0-71e635f16dd2" -->
## Static -> Dynamic Bridging in the Avenue Web
Context chaining bridge:
- Static: generated prompts/rules/skills/indexes from `0AGNOSTIC` + `.1merge`.
- Dynamic: runtime retrieval (skills, JSON-LD traversal, memory, docs/search, feedback).
- Bridge mechanism: static artifacts contain pointers, triggers, and constraints that invoke dynamic loads only when needed.

Reference chaining bridge:
- Static references: path rules, trigger tables, imports, index pointers.
- Dynamic references: tool outputs, query handles, memory links, follow-up selectors.
- Bridge mechanism: static references route to dynamic resolution endpoints (JSON-LD node queries, skill invocations, memory lookups).

Result:
- principles/rules from canonical static sources remain authoritative,
- while dynamic context retrieval provides relevance and efficiency at execution time.

<!-- section_id: "98cc509b-858c-453e-b897-b73a62307777" -->
## Cross-Tool Application Model (Best-Fit by Tool)
The Avenue Web is common architecture; application is tool-specific through `.1merge` outputs and runtime routing.

| Tool/App | Best Static Surfaces | Best Dynamic Surfaces | Best-Fit Strategy |
|---|---|---|---|
| Claude Code | `CLAUDE.md`, path rules, skills | tools, hooks, memory, JSON-LD queries | Use strong rule + skill routing; pair with compaction-safe memory hooks. |
| Codex CLI | `AGENTS.md`/`OPENAI.md`, local files | shell tools, JSON-LD queries, retrieval | Keep static prompts concise; drive dynamic via scripted query paths. |
| Gemini CLI | `GEMINI.md`, imports | extensions/tools, JSON-LD and retrieval | Lean on imported modular context and extension-driven dynamic lookups. |
| Cursor IDE/CLI | `.cursor/rules`, AGENTS-style docs | built-in indexing, MCP, terminal tools | Maximize path-attached rules + semantic retrieval from index surfaces. |
| Windsurf | workspace rules/workflows | memories, runtime retrieval | Route via workflow docs first, then selective memory + JSON-LD lookup. |
| GitHub Copilot | `.github` instructions/skills | limited dynamic runtime | Bias toward stronger static propagation and short reference chains. |
| Aider | repo files/instructions | command execution + repo mapping | Use canonical static files + command-driven JSON-LD extraction. |
| Cline / Roo | mode rule files | memory bank, tools | Mode-scoped static context with explicit dynamic handoffs. |
| OpenCode / Junie / Amazon Q | platform-native instruction files | varying tool/runtime depth | Keep portable static baseline; dynamically enable only proven runtime routes. |

Design rule:
- Core Avenue Web semantics remain identical across tools.
- `.1merge` encodes the per-tool adaptation without forking canonical `0AGNOSTIC` content.

<!-- section_id: "8ae55db2-a218-44ed-b096-6c990bc7fb61" -->
## Context Chain Mapping
- Stage-level static context: generated agent files + path rules.
- Task-level dynamic context: skills, JSON-LD summaries, memory, retrieval.
- Fallback context: direct read of `0AGNOSTIC`.

<!-- section_id: "83c73405-020a-4d0a-9692-3c7f5074e265" -->
## Reference Chain Mapping
- Trigger tables and path rules point to skills.
- Skills and prompts point to knowledge/integration summaries.
- Summaries point to deeper JSON-LD and source docs.
- Memory points to prior decisions and changed files.

<!-- section_id: "bc65d2e3-af57-40d6-9823-54fe0c6112ac" -->
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

<!-- section_id: "f974dbef-d5d8-43f0-8ac3-c77a2f745fdf" -->
## Design Constraints
1. No tool-specific logic in canonical `0AGNOSTIC` unless unavoidable.
2. `.1merge` overrides must be explicit, scoped, and documented.
3. Every critical rule must have at least:
- one static context path and one dynamic context path
- one static reference path and one dynamic reference path
4. Emitted files must be reproducible from source + merge rules.

<!-- section_id: "bf61f4ac-0ccf-41d9-a7dc-19d44730f41a" -->
## Design Outputs Required by Planning
1. Merge workflow for `0_synced -> 1_overrides -> 2_additions`.
2. Generation map from source artifacts to emitted files per tool.
3. Validation checks for 8 MVP avenues.
4. Rollback strategy when generated files diverge from source.
5. JSON-LD inventory and traversal contract covering orchestrator, stage, layer, and index graph classes.
