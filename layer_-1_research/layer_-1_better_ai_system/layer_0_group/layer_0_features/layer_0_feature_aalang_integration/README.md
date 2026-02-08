# AALang Integration Research

## Purpose

This research feature tracks how AALang/GAB is integrated into our layer-stage AI system, identifies gaps, and plans deeper adoption.

---

## Current State

AALang is integrated in three main areas:

| Integration Point | Location | Pattern | Status |
|-------------------|----------|---------|--------|
| Context Loading Agent | `layer_0/layer_0_03_context_agents/` | 4-mode-13-actor | Defined |
| Layer 0 Orchestrator | `layer_0/layer_0_01_ai_manager_system/personal/` | 5-mode-15-actor | Defined |
| Project Orchestrators | Various `layer_N/` directories | 5-mode-15-actor (inherited) | Template exists |

### What Exists

1. **context_loading_gab.jsonld** — Full AALang agent definition for CLAUDE.md chain traversal
2. **layer_0_orchestrator.gab.jsonld** — Full AALang agent definition for multi-agent coordination
3. **layer_6_orchestrator.gab.jsonld** — Project-level orchestrator inheriting from layer_0 template
4. **GAB compiler** (professor submodule) — Tool for creating new AALang agents

### CLAUDE.md Audit (2026-02-07)

- **298 CLAUDE.md files** across the system, **15,363 total lines**
- **717 lines** in the static chain (5 files always loaded) — target is <400
- Every CLAUDE.md has 15-25 lines of **ceremonial AALang pseudo-code** that doesn't connect to real artifacts
- **6 CRITICAL rules duplicated** across `~/.claude/CLAUDE.md` and `~/CLAUDE.md`
- **No `.claude/rules/` directory** — path-specific rules not being used
- **4 root skills** exist but descriptions are vague — agents don't invoke them

### Approved Approach: Hybrid with Three-Layer Redundancy

JSON-LD as source-of-truth (design-time) + markdown as runtime interface + skills as bridge.

**Reference chain architecture** (decided 2026-02-07):
- **Layer 1 (primary)**: jq instructions in CLAUDE.md → agent reads JSON-LD graph → gets precise skill mappings
- **Layer 2 (fallback)**: SKILL.md descriptions with WHEN/WHEN NOT patterns → Claude Code's native skill matcher
- **Layer 3 (second fallback)**: Transpiled `.integration.md` files → auto-generated markdown from JSON-LD

See [architecture_decision_reference_chain.md](architecture_decision_reference_chain.md) for full analysis.
See [implementation_plan.md](implementation_plan.md) for the phased execution plan.

### Core Problems Being Addressed

1. **Instructions lost across sessions** — markdown too imprecise for machine execution
2. **Agent Teams ephemeral** — created then destroyed, context lost
3. **Skills underutilized** — agents don't invoke skills when they should
4. **Context chain inefficiency** — static context wastes space on non-critical content
5. **Markdown vs JSON-LD tension** — need both human readability and machine precision

See [problems_and_vision.md](problems_and_vision.md) for full analysis.

---

## Research Files

| File | Topic |
|------|-------|
| [verification_results.md](verification_results.md) | **READ FIRST** — What was verified true/false on 2026-02-07 |
| [problems_and_vision.md](problems_and_vision.md) | 5 core problems and the architectural vision (REVISED post-verification) |
| [context_chain_integration.md](context_chain_integration.md) | How AALang fits into the CLAUDE.md context chain (VERIFIED) |
| [orchestrator_integration.md](orchestrator_integration.md) | How orchestrators work within our layer hierarchy |
| [skills_integration.md](skills_integration.md) | How to improve skill discovery and invocation (REVISED) |
| [agent_teams_convergence.md](agent_teams_convergence.md) | Merging Agent Teams interactivity with layer-stage persistence |
| [adoption_roadmap.md](adoption_roadmap.md) | Phased plan for deeper AALang adoption (REVISED 2026-02-07) |
| [implementation_plan.md](implementation_plan.md) | **Concrete implementation plan** — 6 phases, specific file changes, success criteria |
| [claude_md_audit.md](claude_md_audit.md) | CLAUDE.md chain audit — 717 lines in static chain, duplication analysis, recommendations |
| [selective_jsonld_navigation.md](selective_jsonld_navigation.md) | **PROVEN** — Agents can navigate JSON-LD graphs via jq, loading only 2-5% of files |
| [architecture_decision_reference_chain.md](architecture_decision_reference_chain.md) | **KEY DECISION** — Three-layer redundancy model: jq-first + skill descriptions + transpiled markdown |

---

## Related Research Features

| Feature | Relationship |
|---------|-------------|
| `layer_0_feature_context_framework` | Context chain design — AALang provides the loading agent |
| `layer_0_feature_multi_agent_orchestration` | Orchestration patterns — AALang defines the orchestrator |
| `layer_0_feature_structure_framework` | System structure — AALang agents live within this structure |

---

*Research feature: layer_0_feature_aalang_integration*
*Last updated: 2026-02-07*
