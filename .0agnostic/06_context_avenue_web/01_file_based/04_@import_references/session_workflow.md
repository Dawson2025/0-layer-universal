# Session Workflow

## Session Start Protocol

```
1. Load CLAUDE.md chain (automatic)
         │
         ▼
2. Identify task type
         │
    ┌────┴────┬────────────┬─────────────┐
    ▼         ▼            ▼             ▼
  AI Work   Orchestration  Context    Rules/Knowledge
    │         │            │             │
    ▼         ▼            ▼             ▼
  Load      Load         Load          Load
professor/ personal/  context_agents/ sub_layers/
         │
         ▼
3. Check hand_off_documents/incoming/
         │
         ▼
4. Begin work with full context
```

## Steps

1. **Sync**: `git pull && git status`
2. **Read rules**: `sub_layer_0_02_rules/` (especially modification protocol)
3. **Identify context**: What layer? What stage?
4. **Check episodic memory**: Read `memory/episodic.md` for recent session history; if resuming work, also read `.0agnostic/episodic_memory/index.md` in the working directory
5. **AALang context**: Find the `.gab.jsonld` for your role, read its matching `.integration.md` (same base name), and query via jq for mode constraints
6. **Check agnostic system**: If `0AGNOSTIC.md` exists in the working directory, it is the source of truth — edit it, not `CLAUDE.md`. Check `.0agnostic/` for on-demand resources. Check `.1merge/` for tool-specific overrides.
7. **Check skills**: Read `.claude/skills/*/SKILL.md` — match WHEN/WHEN NOT conditions to your task. Key skills: `/context-gathering`, `/stage-workflow`, `/entity-creation`, `/handoff-creation`
8. **Do work**: Follow stage guidelines, mode constraints, and agnostic system conventions
9. **Update episodic memory**: After significant work, update `.0agnostic/episodic_memory/index.md` in the working layer, then run `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh`
10. **If context was modified**: Edit `0AGNOSTIC.md` (not CLAUDE.md), then run `agnostic-sync.sh` to regenerate tool-specific files
11. **Commit/push**: Per AI_CONTEXT_COMMIT_PUSH_RULE.md
