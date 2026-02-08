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

### What's Unclear

- How much of the AALang spec is actually executed vs aspirational
- Whether the context loading agent's confidence calculations are actually computed
- Whether the orchestrator's circuit breaker and safeguards are enforced at runtime
- How project orchestrators are actually invoked (manual vs automatic)

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
| [adoption_roadmap.md](adoption_roadmap.md) | Phased plan for deeper AALang adoption |

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
