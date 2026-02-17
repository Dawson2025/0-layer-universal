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

1. **context_loading.gab.jsonld** — Full AALang agent definition for CLAUDE.md chain traversal
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

See [architecture_decision_reference_chain.md](architecture/architecture_decision_reference_chain.md) for full analysis.
See [implementation_plan.md](planning/implementation_plan.md) for the phased execution plan.

### Core Problems Being Addressed

1. **Instructions lost across sessions** — markdown too imprecise for machine execution
2. **Agent Teams ephemeral** — created then destroyed, context lost
3. **Skills underutilized** — agents don't invoke skills when they should
4. **Context chain inefficiency** — static context wastes space on non-critical content
5. **Markdown vs JSON-LD tension** — need both human readability and machine precision

See [problems_and_vision.md](02_problem_analysis/problems_and_vision.md) for full analysis.

---

## Research Files

### 01_vision/ — What's possible
| File | Topic |
|------|-------|
| [context_system_vision.md](01_vision/context_system_vision.md) | Vision for a complete AI context system — static/dynamic separation, reference chains, AI traversal, tool agnosticism |

### 02_problem_analysis/ — Problem identification and analysis
| File | Topic |
|------|-------|
| [problems_and_vision.md](02_problem_analysis/problems_and_vision.md) | 5 core problems and the architectural vision (REVISED post-verification) |
| [rule_propagation_problem.md](02_problem_analysis/rule_propagation_problem.md) | Universal rules not automatically applied to all sessions |

### 03_obstacles/ — What stands in the way
| File | Topic |
|------|-------|
| [obstacles.md](03_obstacles/obstacles.md) | 8 key obstacles: skill invocation, context budget, JSON-LD mismatch, session loss, tool fragmentation, and more |
| [skill_reliability_per_tool.md](03_obstacles/skill_reliability_per_tool.md) | **PRIMARY RESEARCH** — Instruction/skill adherence evaluated across 8 tools (Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Windsurf, Aider, Junie) with real GitHub issues and benchmarks |

### 04_design/ — Possible designs and approaches
| File | Topic |
|------|-------|
| [referencing_methods_and_skill_invocation.md](04_design/referencing_methods_and_skill_invocation.md) | All 11 referencing methods surveyed + 5 design approaches for skill invocation |

### architecture/ — Architecture decisions and technical approaches
| File | Topic |
|------|-------|
| [architecture_decision_reference_chain.md](architecture/architecture_decision_reference_chain.md) | **KEY DECISION** — Three-layer redundancy model: jq-first + skill descriptions + transpiled markdown |
| [selective_jsonld_navigation.md](architecture/selective_jsonld_navigation.md) | **PROVEN** — Agents can navigate JSON-LD graphs via jq, loading only 2-5% of files |

### integration/ — How components integrate with each other
| File | Topic |
|------|-------|
| [context_chain_integration.md](integration/context_chain_integration.md) | How AALang fits into the CLAUDE.md context chain (VERIFIED) |
| [orchestrator_integration.md](integration/orchestrator_integration.md) | How orchestrators work within our layer hierarchy |
| [skills_integration.md](integration/skills_integration.md) | How to improve skill discovery and invocation (REVISED) |
| [agent_teams_convergence.md](integration/agent_teams_convergence.md) | Merging Agent Teams interactivity with layer-stage persistence |

### verification/ — Audits and verification of assumptions
| File | Topic |
|------|-------|
| [verification_results.md](verification/verification_results.md) | **READ FIRST** — What was verified true/false on 2026-02-07 |
| [claude_md_audit.md](verification/claude_md_audit.md) | CLAUDE.md chain audit — 717 lines in static chain, duplication analysis, recommendations |

### planning/ — Roadmaps and execution plans
| File | Topic |
|------|-------|
| [implementation_plan.md](planning/implementation_plan.md) | **Concrete implementation plan** — 6 phases, specific file changes, success criteria |
| [adoption_roadmap.md](planning/adoption_roadmap.md) | Phased plan for deeper AALang adoption (REVISED 2026-02-07) |

---

## Related Research Features

| Feature | Relationship |
|---------|-------------|
| `layer_0_feature_context_framework` | Context chain design — AALang provides the loading agent |
| `layer_0_feature_multi_agent_orchestration` | Orchestration patterns — AALang defines the orchestrator |
| `layer_0_feature_structure_framework` | System structure — AALang agents live within this structure |

---

*Research feature: layer_0_feature_aalang_integration*
*Last updated: 2026-02-16*
