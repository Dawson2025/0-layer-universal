# AALang Adoption Roadmap

## Current State Summary

AALang is integrated at three points: context loading, universal orchestration, and project orchestration templates. The integration is **specification-complete but execution-unclear** — the agent definitions exist as complete `.jsonld` files, but their actual runtime status needs investigation.

---

## Adoption Tiers

### Tier 1: Documentation & Knowledge (CURRENT)

**Status**: In progress

What we have:
- Knowledge base docs in `sub_layer_0_01_knowledge_system/aalang_gab_system/`
- Research docs in `layer_0_feature_aalang_integration/`
- Understanding of Mode-Actor pattern, GAB compiler, runtime behaviors

What's needed:
- Verify accuracy of knowledge docs against latest upstream AALang
- Clarify which parts are aspirational vs operational

### Tier 2: Verify Existing Integrations

**Status**: Not started

Tasks:
- [ ] Test the context loading agent — load it into an LLM and see if it actually traverses the CLAUDE.md chain as specified
- [ ] Test the orchestrator — load it and see if it correctly receives/delegates/monitors/aggregates
- [ ] Check if `.claude/context_state.json` is created by the context loading agent
- [ ] Check if `spawn_agent.sh` works for spawning child agents
- [ ] Test project orchestrator inheritance — does `"extends"` actually work?

### Tier 3: Connect to Claude Code Features

**Status**: Not started

Potential integration points:

| Claude Code Feature | AALang Integration |
|----|-----|
| Agent Teams (experimental) | Could use orchestrator pattern for team coordination |
| CLAUDE.md auto-loading | Already aligns with context loading agent's purpose |
| Task tool (subagent spawning) | Maps to orchestrator's Delegation mode |
| MCP servers | AALang could define agent-to-MCP communication patterns |

Questions to resolve:
- Does Claude Code's built-in CLAUDE.md loading make the context loading agent redundant, or complementary?
- Can agent teams use AALang orchestrator definitions to structure coordination?
- Can the Task tool's subagent spawning be formalized through AALang patterns?

### Tier 4: Create New Agents

**Status**: Not started

Once we understand what works, use GAB to create new agents:
- **Stage workflow agents**: One agent per stage (01-11) that knows how to execute that stage's work
- **Layer manager agents**: Formalize what CLAUDE.md files describe as AALang agent definitions
- **Hand-off processing agents**: Agents that read/write/route hand-off documents

### Tier 5: Full System Coverage

**Status**: Future

Long-term vision:
- Every layer has an orchestrator (inherited from layer 0)
- Every stage has a stage-specific agent (created via GAB)
- Context loading is fully automated and verified
- Cross-layer communication uses AALang message passing patterns
- New projects/features automatically get scaffolded with appropriate agents

---

## Immediate Next Steps

1. **Sync with upstream** — Pull latest AALang changes from `yenrab/AALang-Gab` to ensure we're working with current specs
2. **Test context loading agent** — Load `context_loading_gab.jsonld` into a Claude session and test whether it actually executes
3. **Document findings** — Update these research files with results of testing
4. **Investigate Claude Code + AALang overlap** — Understand where Claude Code's built-in features overlap with AALang's specifications

---

## Dependencies

| This research depends on | For |
|--------------------------|-----|
| `layer_0_feature_context_framework` | Understanding what the context chain should look like |
| `layer_0_feature_multi_agent_orchestration` | Understanding orchestration requirements |
| Professor's AALang upstream | Latest language specification |
| Claude Code agent teams feature | Understanding platform capabilities |

---

*Research feature: layer_0_feature_aalang_integration/adoption_roadmap*
*Last updated: 2026-02-07*
