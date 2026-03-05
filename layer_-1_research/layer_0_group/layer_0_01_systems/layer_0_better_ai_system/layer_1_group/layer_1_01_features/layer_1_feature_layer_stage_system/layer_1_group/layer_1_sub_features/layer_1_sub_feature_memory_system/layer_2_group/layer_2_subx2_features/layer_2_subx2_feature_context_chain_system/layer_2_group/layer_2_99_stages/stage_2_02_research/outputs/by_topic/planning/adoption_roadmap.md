---
resource_id: "ec6ac5e6-661c-4150-9587-62acb474a082"
resource_type: "output"
resource_name: "adoption_roadmap"
---
# AALang Adoption Roadmap (Revised 2026-02-07)

<!-- section_id: "83870fb2-29b8-4038-9be3-d41c392881c8" -->
## Current State

AALang/GAB is integrated at multiple points but with a gap between **design-time precision** (JSON-LD definitions) and **runtime effectiveness** (what the LLM actually follows). The CLAUDE.md files have ceremonial pseudo-code that doesn't connect to real artifacts.

<!-- section_id: "e6679199-f7dc-43e1-93e8-4417feafc419" -->
### What Exists

| Artifact | Count | Quality |
|----------|-------|---------|
| Orchestrator JSON-LD files | 17 | 6 substantial (~286-701 lines), 11 stubs |
| Stage agent JSON-LD files | 67 | Mostly 17-line stubs |
| Root skills (`.claude/skills/`) | 4 | Basic descriptions, need WHEN/WHEN NOT patterns |
| Custom agents (`.claude/agents/`) | 3 | context-gatherer, layer-manager, stage-manager |
| Commands (`.claude/commands/`) | 4 | create-entity, gather-context, layer-status, stage-advance |
| Path-specific rules (`.claude/rules/`) | 0 | **Directory doesn't exist** |
| CLAUDE.md files | 298 | 15,363 total lines; 717 in static chain (target: <400) |
| Integration markdown companions | 0 | **None exist yet** |

<!-- section_id: "001d7871-a932-442a-a8fc-fa8f57aaf347" -->
### What's Been Verified (Research Completed)

- Professor's upstream docs reviewed: 10 substantive docs, 3 test result docs
- 5 core problems identified, mapped against professor's solutions
- JSON-LD vs markdown accuracy research: JSON-LD scores lowest for LLM comprehension
- Professor acknowledges context window pressure: "significant context windows needed"
- 9 unique research contributions identified beyond professor's work
- Hybrid approach validated: JSON-LD for design-time, markdown for runtime

---

<!-- section_id: "4d34ba00-cb4b-484b-8e87-b8d5ccbcc653" -->
## Adoption Tiers (Revised)

<!-- section_id: "81915c33-5a37-474a-ae98-600fc8175e84" -->
### Tier 1: Documentation & Knowledge — COMPLETE

- Knowledge base: `sub_layer_0_01_knowledge_system/aalang_gab_system/` (7 docs)
- Research docs: `layer_0_feature_aalang_integration/` (8 docs + this roadmap)
- Professor's docs analysis: comprehensive review of upstream
- Verification results: 5 claims verified via independent research

<!-- section_id: "2b0864a3-ed83-434b-9676-ad9cc0636144" -->
### Tier 2: CLAUDE.md Optimization — READY TO START

**Goal**: Slim static chain from 717 to ~350 lines, replace ceremonial AALang with real references.

Tasks:
- [ ] Condense 6 CRITICAL rules (3-5 lines each, not 10-15)
- [ ] Remove duplicate rules across `~/.claude/CLAUDE.md` and `~/CLAUDE.md`
- [ ] Replace AALang pseudo-code blocks with 3-line references to actual JSON-LD files
- [ ] Create @import targets for verbose content (compliance checklist, scenario rules, ASCII diagrams)
- [ ] Slim `layer_0/CLAUDE.md` (206 → ~80 lines, move ASCII diagrams to @imports)

<!-- section_id: "72b0656d-2f1f-43e9-b950-dcd872c5033a" -->
### Tier 3: Path-Specific Rules — READY TO START

**Goal**: Create `.claude/rules/` directory with context that auto-loads by path.

Tasks:
- [ ] Create `.claude/rules/` directory
- [ ] `research-context.md` (paths: `layer_-1_research/**`)
- [ ] `school-context.md` (paths: `layer_1/layer_1_projects/layer_1_project_school/**`)
- [ ] `universal-layer.md` (paths: `layer_0/**`)
- [ ] `aalang-context.md` (paths: `layer_0/layer_0_01_ai_manager_system/**`)
- [ ] `development-stages.md` (paths: `**/stage_*_06_development/**`)

<!-- section_id: "7a726800-7c17-401b-aede-fe08a3c51cd7" -->
### Tier 4: Integration Companions + Skill Enhancement — SHORT-TERM

**Goal**: Bridge JSON-LD definitions to runtime with readable markdown + better skill descriptions.

Tasks:
- [ ] Create `.integration.md` for `layer_0_orchestrator.gab.jsonld` (701 lines → ~50 line summary)
- [ ] Create `.integration.md` for `context_loading.gab.jsonld` (1065 lines → ~40 line summary)
- [ ] Enhance 4 root skills with WHEN/WHEN NOT patterns and JSON-LD references
- [ ] Create `/aalang-load` skill (reads JSON-LD, presents as markdown)
- [ ] Create `/team-create` skill (generates spawn prompts from orchestrator definitions)

<!-- section_id: "9151c5fc-5c32-4803-badd-821911ea15ed" -->
### Tier 5: Fill JSON-LD Definitions — MEDIUM-TERM

**Goal**: Key layers/stages have real JSON-LD definitions (not stubs).

Approach:
- **Manual** (~35): Root, layer_0, layer_1, layer_-1, all 11 stages for layer_0
- **Template** (~50): Project-level orchestrators, sub-layer agents
- **Auto-generate** (ongoing): Entity-creation skill generates definitions for new directories

Tasks:
- [ ] Create orchestrator templates: `orchestrator_template.gab.jsonld`
- [ ] Create stage agent templates: `stage_agent_template.gab.jsonld`
- [ ] Expand 17-line stage agent stubs with real content
- [ ] Update entity-creation skill to auto-generate JSON-LD + CLAUDE.md + integration.md

<!-- section_id: "90a10f85-e443-42e4-805f-ffd52e812deb" -->
### Tier 6: Agent Teams Persistence — LONGER-TERM

**Goal**: Teams that persist across sessions via orchestrator definitions + hand-off docs.

Tasks:
- [ ] Design team state persistence format
- [ ] Create `/team-create` skill backed by orchestrator JSON-LD
- [ ] Design hand-off document format for team state
- [ ] Test: spawn team → close session → resume from hand-off docs
- [ ] Integrate with AALang state actors for state tracking

---

<!-- section_id: "e2ec022f-ecbd-4af5-bb13-0d852c9fabe4" -->
## Key Decisions

<!-- section_id: "3d38bd89-7dce-4051-bfe2-a2108b23051b" -->
### Decision 1: Hybrid Approach

**Approved (2026-02-07)**: JSON-LD as source-of-truth + skills as runtime interface + compact CLAUDE.md references.

**Why hybrid**: JSON-LD forces precision (the professor's "Explicit Over Implicit"). Markdown communicates that precision effectively to the LLM. Skills make it actionable at runtime. CLAUDE.md files just point to where things are.

<!-- section_id: "7a57d81e-bf67-44c4-b6c8-88d5c48d5e66" -->
### Decision 2: Three-Layer Redundancy Model

**Approved (2026-02-07)**: No single mechanism reliably solves skill invocation. Use three redundant layers.

```
Layer 1 (PRIMARY):       CLAUDE.md jq instructions → agent reads JSON-LD → gets skill mappings
Layer 2 (FALLBACK):      SKILL.md WHEN/WHEN NOT patterns → Claude Code's native matcher
Layer 3 (2ND FALLBACK):  Transpiled .integration.md → auto-generated markdown from JSON-LD
```

**Why three layers**: Skill invocation is probabilistic. Each layer is an independent chance to get it right. Three chances > one chance. Current state (zero layers) is the worst case — no regression possible.

**Why jq-first**: "Run this command" is a concrete instruction the LLM reliably follows. Probabilistic skill matching ("does this situation match this description?") is the mechanism that's currently failing.

**Why transpiler**: Auto-generated markdown from JSON-LD provides the same precision in the format LLMs read best. Never drifts from source of truth. No tool calls needed — just Read.

See: `architecture_decision_reference_chain.md` for the full analysis.

---

<!-- section_id: "55be7137-d107-4c72-9904-3ce14e056bcb" -->
## Scale

| Level | Directories | JSON-LD Files | Coverage |
|-------|------------|---------------|----------|
| Root + main layers | ~5 | 2 | 40% |
| Key stages | ~30 | 67 (stubs) | ~100% structure, ~0% content |
| Sub-layers | ~20 | 0 | 0% |
| Projects | ~10 | 6 | 60% |
| Deeply nested | ~21,500 | Some stubs | <1% |
| **Total** | ~21,606 | 84 | <1% |

Practical target: Cover ~85 key definitions (manual + template), auto-generate the rest.

---

<!-- section_id: "a989e3d8-ca45-40c7-b6ca-5de85c3f6183" -->
## Dependencies

| Dependency | Status | Needed For |
|-----------|--------|------------|
| Professor's upstream AALang synced | DONE (2026-02-07) | Tier 4, 5 |
| CLAUDE.md audit complete | DONE (2026-02-07) | Tier 2 |
| Research verification complete | DONE (2026-02-07) | All tiers |
| Claude Code @import feature | Available | Tier 2 |
| Claude Code path-specific rules | Available | Tier 3 |

---

<!-- section_id: "c7028386-8b40-4176-89ab-bff8991a8ed0" -->
## Detailed Plan

See: `implementation_plan.md` for the full phased implementation plan with specific file changes.

---

*Adoption roadmap for: layer_0_feature_aalang_integration*
*Original: 2026-02-07*
*Revised: 2026-02-07 (post professor's docs review, post CLAUDE.md audit)*
*Status: Tiers 1 complete, Tiers 2-3 ready to execute, Tiers 4-6 planned*
