---
resource_id: "a8e00820-56fc-4256-a2af-1f24a7a4ef71"
resource_type: "output"
resource_name: "stages_manager_pattern"
---
# Design Decision: Stages Manager Pattern

**Date**: 2026-02-24
**Status**: Proposed — pending approval
**Scope**: Agent delegation architecture — how entities coordinate their stages

---

## Problem Statement

Currently, entity managers directly delegate to stage agents and carry all stage coordination knowledge:

```
Entity Manager (0AGNOSTIC.md)
├── Stage overview table (11 stages, status, descriptions)
├── Stage delegation instructions (how to spawn stage agents)
├── Stage flow diagram (01→02→04→05→06→07, loops)
├── Stage transition rules (when to move between stages)
└── Directly spawns stage agents as needed
```

The `layer_N_99_stages/` directory exists at every entity but is a thin container:
- 0AGNOSTIC.md: ~7 lines ("Stages container for X")
- A `.gab.jsonld` orchestrator exists but isn't used as a real manager
- No coordination logic, no dependency tracking

**Contradiction**: Entity managers claim "You are a manager — you delegate, you don't operate" and "You do NOT carry the methodology for request gathering." But they DO carry all stage coordination logic — which IS operational knowledge about how stages relate, when to transition, and what to do with reports.

---

## Proposed Solution: Stages Manager

Upgrade `layer_N_99_stages/` from a thin container to a **proper stages manager** with its own `.0agnostic/`, `.1merge/`, and full `0AGNOSTIC.md` — the standard agnostic system that every managed entity uses.

### New architecture

```
Entity Manager (entity root 0AGNOSTIC.md)
│
│  Focuses on:
│  ├── Entity identity and scope
│  ├── Children management (child entities)
│  ├── Parent communication (layer reports up, instructions down)
│  ├── Strategic decisions (what to work on, priorities)
│  └── Entity-level status (0INDEX.md dashboard)
│
│  Delegates stage coordination to:
│
└──▶ Stages Manager (layer_N_99_stages/ 0AGNOSTIC.md)
     │
     │  Focuses on:
     │  ├── Stage dependency graph (which stages feed which)
     │  ├── Stage transitions (when to move from design → planning → dev)
     │  ├── Stage report consolidation (reads all → writes stages_report.md)
     │  ├── Inter-stage handoffs (what goes from stage 02 to stage 04)
     │  ├── Parallel stage coordination (which stages can run concurrently)
     │  └── Stage status tracking (active, scaffolded, blocked, complete)
     │
     │  Delegates stage work to:
     │
     ├──▶ Stage 01 Agent (request_gathering)
     ├──▶ Stage 02 Agent (research)
     ├──▶ Stage 04 Agent (design)
     ├──▶ Stage 06 Agent (development)
     ├──▶ Stage 07 Agent (testing)
     └──▶ ...
```

### What the entity manager loses

These sections move from entity 0AGNOSTIC.md to stages manager 0AGNOSTIC.md:

| Section | Currently in | Moves to |
|---------|-------------|----------|
| Stage Overview table (11 rows) | Entity 0AGNOSTIC.md | Stages Manager 0AGNOSTIC.md |
| Stage Delegation instructions | Entity 0AGNOSTIC.md | Stages Manager 0AGNOSTIC.md |
| Stage flow diagram | Entity 0AGNOSTIC.md | Stages Manager 0AGNOSTIC.md |
| "How Stages Connect" | Entity 0INDEX.md | Stages Manager (owns this) |

### What the entity manager keeps

| Concern | Why |
|---------|-----|
| "Current Focus" with active stage mentions | Strategic overview — entity decides priority |
| Children management | Entity-level concern |
| Parent communication | Entity-level concern |
| Entity identity, scope, triggers | Entity-level concern |
| Navigation table pointing to stages manager | Delegation pointer |

### What the stages manager gains

| Content | Purpose |
|---------|---------|
| Stage dependency graph | Which stages feed which — explicit edges |
| Transition rules | When 02→04 is ready, when 07→08→09 loop triggers |
| Consolidation protocol | How to read all stage reports → produce stages_report.md |
| Parallel stage rules | Which stages can run concurrently (01+02 yes, 06+07 no) |
| Blocking detection | How to identify when a stage is stuck and escalate |
| Stage registry | stage_N_00_stage_registry as managed inventory |

---

## Design Constraints

### 1. Full agnostic system — proper knowledge management

The stages manager gets the standard agnostic infrastructure because its coordination knowledge is real domain knowledge that deserves structured access:

```
layer_N_99_stages/
├── 0AGNOSTIC.md                          ◄── Stages Manager identity + stage coordination
├── 0INDEX.md                             ◄── Dashboard: all stages status, flow, dependencies
├── CLAUDE.md (generated)
├── AGENTS.md (generated)
├── GEMINI.md (generated)
├── OPENAI.md (generated)
├── .cursorrules (generated)
│
├── .0agnostic/
│   ├── 01_knowledge/
│   │   ├── stage_dependency_graph.md     ◄── Which stages feed which, explicit edges
│   │   ├── stage_lifecycle_model.md      ◄── Stage states: scaffolded → active → complete
│   │   └── parallel_stage_rules.md       ◄── Which stages can run concurrently
│   ├── 02_rules/
│   │   ├── static/
│   │   │   ├── stage_transition_rules.md ◄── When 02→04 is ready, handoff validation
│   │   │   └── consolidation_rules.md    ◄── How to produce stages_report.md
│   │   └── dynamic/
│   │       └── blocking_detection.md     ◄── How to identify stuck stages, escalation
│   ├── 03_protocols/
│   │   ├── stage_transition_protocol.md  ◄── Step-by-step for moving between stages
│   │   └── consolidation_protocol.md     ◄── How to read all reports → produce summary
│   ├── 04_episodic_memory/
│   │   └── index.md                      ◄── Session history of stage coordination decisions
│   ├── 05_handoff_documents/
│   │   ├── 01_incoming/
│   │   │   ├── 01_from_above/            ◄── Entity manager directives
│   │   │   └── 03_from_below/
│   │   │       └── stage_reports/        ◄── All active stage reports (via sync-handoffs)
│   │   └── 02_outgoing/
│   │       └── 01_to_above/
│   │           └── stages_report.md      ◄── Consolidated report for entity manager
│   └── 06_context_avenue_web/
│       └── 01_file_based/                ◄── Avenues specific to stages management
│
├── .1merge/
│   └── .1claude_merge/
│       ├── 0_synced/
│       ├── 1_overrides/
│       └── 2_additions/                  ◄── Claude-specific stage coordination instructions
│
├── layer_N_99_stages_orchestrator.gab.jsonld  (existing — now properly used)
├── layer_N_99_stages_orchestrator.integration.md (existing)
│
├── stage_N_00_stage_registry/            ◄── Managed inventory
├── stage_N_01_request_gathering/
├── stage_N_02_research/
├── ...
└── stage_N_11_archives/
```

**Why full .0agnostic?** Stage coordination knowledge is real domain knowledge:
- **01_knowledge/**: Dependency graphs, lifecycle models, parallel rules — these are facts about how stages relate
- **02_rules/**: Transition rules, consolidation rules — these are constraints on stage coordination
- **03_protocols/**: Step-by-step procedures for transitions and consolidation
- **04_episodic_memory/**: Record of coordination decisions across sessions (e.g., "We moved 07→08 early because...")
- **05_handoff_documents/**: The stages manager is the natural ingestion point for stage reports (from_below) and produces the consolidated stages_report.md (outgoing)
- **06_context_avenue_web/**: Avenues for the stages manager agent to load its knowledge

Without `.0agnostic/`, this knowledge has nowhere structured to live — it'd be crammed into 0AGNOSTIC.md prose or spread across stage directories. The three-tier knowledge model (pointers in 0AGNOSTIC.md → distilled in .0agnostic/ → full in stage outputs) applies here too.

**Why .1merge?** Different AI tools need different stage coordination instructions. For example:
- Claude Code addition: "Use Task tool to spawn stage agents" / "Use SendMessage for team coordination"
- Codex addition: different agent spawning mechanism
- The merge system keeps tool-specific instructions out of the agnostic source

**What it does NOT have**:
- Its own stages (recursive stages-of-stages would be absurd)
- Its own children (the stages ARE what it manages, not children entities)
- A `layer_N+1_group/` directory

### 2. Zero extra delegation hops for simple tasks

For simple cases ("go work on stage 06"), the entity manager can still directly delegate to a stage agent. The stages manager is consulted when:
- Deciding WHICH stage to work on next
- Transitioning between stages
- Consolidating stage reports
- Resolving inter-stage dependencies

### 3. Backward compatible

Existing entities continue to work. The upgrade is:
1. Expand the existing `layer_N_99_stages/0AGNOSTIC.md` from thin container to stages manager
2. Create `.0agnostic/` with numbered subdirectories (01_knowledge through 06_context_avenue_web)
3. Create `.1merge/.1claude_merge/` with 3-tier structure (0_synced, 1_overrides, 2_additions)
4. Move stage coordination content from entity 0AGNOSTIC.md to stages manager 0AGNOSTIC.md
5. Populate `.0agnostic/01_knowledge/` with stage dependency graph, lifecycle model, parallel rules
6. Populate `.0agnostic/02_rules/` with transition rules and consolidation rules
7. Populate `.0agnostic/03_protocols/` with transition and consolidation protocols
8. Run agnostic-sync.sh to regenerate CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md
9. The existing orchestrator `.gab.jsonld` already defines the modes

### 4. Optional per entity

Small entities with 1-2 active stages don't need this. The pattern applies when:
- Entity has 4+ active stages
- Inter-stage dependencies are non-trivial
- Stage transitions need coordination (not just "go do stage X")

---

## Delegation Flow Examples

### Example 1: "What should we work on next?"

**Before (current)**:
```
User → Entity Manager → reads all stage reports → decides → spawns stage agent
```

**After (with stages manager)**:
```
User → Entity Manager → asks Stages Manager "what's the next priority?"
  Stages Manager → reads stage reports, checks dependency graph → recommends stage
Entity Manager → approves → Stages Manager spawns stage agent
```

### Example 2: "Stage 04 design is done, transition to planning"

**Before (current)**:
```
Stage 04 agent → writes stage_report.md → exits
Entity Manager → reads report → manually decides 05 is next → spawns stage 05 agent
```

**After (with stages manager)**:
```
Stage 04 agent → writes stage_report.md → exits
Stages Manager → detects 04 completion → checks dependency graph →
  04 feeds 05 → validates handoff readiness → spawns stage 05 agent
  → notifies Entity Manager via stages_report.md update
```

### Example 3: "Run testing and criticism in parallel"

**Before**: Entity manager must know that 07 and 08 can run concurrently.
**After**: Stages manager owns the parallel/sequential rules and coordinates multi-stage execution.

---

## Relationship to Existing Artifacts

| Artifact | Current Role | New Role |
|----------|-------------|----------|
| `layer_N_99_stages/0AGNOSTIC.md` | Thin container ("Stages container for X") | Stages Manager identity with coordination knowledge |
| `layer_N_99_stages/0INDEX.md` | Does not exist | Stages dashboard: all stages status, flow, dependencies |
| `layer_N_99_stages/CLAUDE.md` | Auto-generated thin file | Auto-generated with stage coordination context |
| `layer_N_99_stages/AGENTS.md` | Does not exist | Auto-generated (for Codex/Cursor cross-consumption) |
| `layer_N_99_stages/GEMINI.md` | Does not exist | Auto-generated (for Gemini CLI) |
| `layer_N_99_stages/.0agnostic/` | Does not exist | Full agnostic system: knowledge, rules, protocols, episodic memory, handoff docs |
| `layer_N_99_stages/.1merge/` | Does not exist | Tool-specific merge dirs (Claude, Codex, Gemini, Cursor, Copilot) |
| `layer_N_99_stages_orchestrator.gab.jsonld` | Exists but minimally used | Backs the Stages Manager with mode definitions |
| `stage_N_00_stage_registry/` | Stage registry directory | Managed by Stages Manager (inventory of stages) |
| `status_N.json` | Status file at stages level | Owned by Stages Manager |

---

## Tradeoffs

### Benefits

1. **Cleaner entity manager** — entity 0AGNOSTIC.md shrinks by ~30-40 lines, focuses on entity-level concerns
2. **Explicit stage coordination** — dependency graph, transition rules, parallel rules all have a home
3. **Natural consolidation** — stages_report.md authorship belongs to the stages manager
4. **Existing infrastructure** — orchestrator .gab.jsonld already exists, 0AGNOSTIC.md just needs expansion
5. **Recursive consistency** — follows the "managers delegate, operators do work" pattern one level deeper
6. **Blocking detection** — stages manager can track which stages are stuck and escalate to entity manager

### Costs

1. **Extra context load** — stages manager 0AGNOSTIC.md (~50-80 lines) plus `.0agnostic/` resources loaded on demand. Net effect depends on how much entity manager shrinks.
2. **More files to maintain** — `.0agnostic/` adds ~10-15 files (knowledge, rules, protocols). These are mostly written once and updated rarely.
3. **Migration work** — every entity's 0AGNOSTIC.md needs stage content extracted, and `.0agnostic/`/`.1merge/` scaffolded
4. **Learning curve** — agents need to know about the two-level manager pattern and that stage coordination lives in `.0agnostic/` not in the entity manager
5. **Optional complexity** — small entities with 2 stages don't benefit, yet the pattern exists

### Mitigations

| Cost | Mitigation |
|------|------------|
| Extra context load | 0AGNOSTIC.md stays under 80 lines (pointers only). `.0agnostic/` resources are loaded on-demand — agents read only what they need. Entity manager shrinks by ~30-40 lines, partially offsetting the new files. |
| More files to maintain | Most `.0agnostic/` content (dependency graphs, transition rules) is written once during entity setup and updated only when stage structure changes. Templates can pre-populate standard content. |
| Migration work | Do incrementally — start with context_chain_system (most active, best test case). Create a migration script or checklist. |
| Learning curve | Document pattern in entity_structure.md canonical reference. The pattern is consistent with how every other managed entity works (same `.0agnostic/` structure). |
| Optional complexity | Mark as "recommended for 4+ active stages, optional otherwise". Small entities keep the thin container pattern. |

---

## Implementation Plan (if approved)

### Phase 1: Pilot with context_chain_system

1. Upgrade `layer_3_99_stages/0AGNOSTIC.md` from thin container ("Stages container for...") to stages manager identity with coordination knowledge
2. Create `layer_3_99_stages/.0agnostic/` with numbered subdirectories:
   - `01_knowledge/` — stage_dependency_graph.md, stage_lifecycle_model.md, parallel_stage_rules.md
   - `02_rules/static/` — stage_transition_rules.md, consolidation_rules.md
   - `02_rules/dynamic/` — blocking_detection.md
   - `03_protocols/` — stage_transition_protocol.md, consolidation_protocol.md
   - `04_episodic_memory/` — index.md
   - `05_handoff_documents/` — incoming (from_above, from_below/stage_reports), outgoing (stages_report.md)
   - `06_context_avenue_web/01_file_based/` — avenues for stages management
3. Create `layer_3_99_stages/.1merge/.1claude_merge/` with 3-tier structure (0_synced, 1_overrides, 2_additions)
4. Move stage coordination content from `layer_3_subx3_feature_context_chain_system/0AGNOSTIC.md` (stage overview table, stage delegation instructions, stage flow diagram) to stages manager 0AGNOSTIC.md
5. Create `layer_3_99_stages/0INDEX.md` as the stages dashboard (all stages status, flow, dependencies)
6. Run agnostic-sync.sh to regenerate CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md at stages manager level
7. Update entity-level 0INDEX.md to reference stages manager
8. Test: verify stage agents still get proper context, verify stages manager can read stage reports, verify agnostic-sync produces correct output

### Phase 2: Document pattern

1. Add stages_manager_pattern to entity_structure.md
2. Add to STAGES_EXPLAINED.md (stage lifecycle)
3. Update .0agnostic/01_knowledge/ at root level

### Phase 3: Gradual rollout

1. Apply to agent_delegation_system (4+ active stages)
2. Apply to memory_system (3+ active stages)
3. Leave small entities (chain_visualization, etc.) as-is

---

## Resolved Questions

1. ~~**Should the stages manager have its own .0agnostic/?**~~ **YES** — resolved in Design Constraint #1. Stage coordination knowledge is real domain knowledge (dependency graphs, transition rules, lifecycle models) that deserves the full agnostic infrastructure. Without `.0agnostic/`, this knowledge would be crammed into 0AGNOSTIC.md prose.

2. ~~**Who writes stages_report.md?**~~ **The stages manager writes it**, entity manager reads it. This is the same pattern as stage agents writing stage_report.md. The stages manager's `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stages_report.md` is the consolidated output. The entity manager reads it from its own `.0agnostic/05_handoff_documents/01_incoming/03_from_below/`.

4. ~~**Should the stage_00_stage_registry be the stages manager's knowledge base?**~~ **YES** — the registry is managed inventory. The stages manager owns the registry as its canonical list of stages, their metadata, and their current status. This complements `.0agnostic/01_knowledge/` which holds the relational knowledge (dependencies, lifecycle model, parallel rules).

## Open Questions

1. **Can the stages manager escalate to the entity manager?** For example, "stage 07 found critical issues — should we loop to stage 09 or redesign from stage 04?" This is a strategic decision that should flow upward. Proposed: stages manager writes an escalation in its `stages_report.md` with options; entity manager reads it and decides.

2. **Should agnostic-sync.sh cascade into the stages manager?** Currently agnostic-sync.sh runs at entity level. Should it also regenerate CLAUDE.md inside `layer_N_99_stages/`, or does the stages manager run its own sync separately?

3. **How does the stages manager interact with entity children?** Entity managers delegate to both stages (via stages manager) and children (directly). Should the stages manager know about children, or is that strictly the entity manager's domain?

---

## Related

- **Context propagation funnel**: `...context_chain_system/.../04_context_propagation_funnel.md` — bottom-up consolidation pattern that the stages manager would implement
- **Stage report protocol**: `.0agnostic/03_protocols/stage_report_protocol.md` — defines the reports the stages manager consumes
- **Entity structure**: `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` — would need updating

---

## Sources

Research informing the app-specific propagation context in the parent design decisions:

- [Cursor CLI Configuration](https://cursor.com/docs/cli/reference/configuration) — CLI config files: `~/.cursor/cli-config.json`, `.cursor/cli.json`
- [Using Cursor Agent CLI](https://cursor.com/docs/cli/using) — CLI reads `.cursor/rules/`, CLAUDE.md, and AGENTS.md as rules
- [Codex CLI Custom Instructions (AGENTS.md)](https://developers.openai.com/codex/guides/agents-md/) — AGENTS.md cascade walk, AGENTS.override.md, `~/.codex/` global config
- [Codex CLI Config Basics](https://developers.openai.com/codex/config-basic/) — `.codex/config.toml` project overrides, trust settings
- [Codex CLI Advanced Configuration](https://developers.openai.com/codex/config-advanced/) — project_doc_max_bytes, fallback filenames
- [Gemini CLI Configuration](https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html) — `~/.gemini/` directory, settings.json
- [Gemini CLI GEMINI.md Files](https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html) — Hierarchical loading (global → parent dirs → cwd → subdirs), .geminiignore, /memory commands
- [Codex CLI Agent Skills](https://developers.openai.com/codex/skills/) — Agent Skills system for Codex
