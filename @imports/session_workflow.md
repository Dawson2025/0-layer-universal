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
2. **Read rules**: `sub_layer_0_05_rules/` (especially modification protocol)
3. **Identify context**: What layer? What stage?
4. **Check episodic memory**: Read `memory/episodic.md` for recent session history; if resuming work, also read `outputs/episodic/index.md` in the working directory
5. **AALang context**: Find the `.gab.jsonld` for your role, read its matching `.integration.md` (same base name), and query via jq for mode constraints
6. **Do work**: Follow stage guidelines and mode constraints
7. **Update episodic memory**: After significant work, update `outputs/episodic/index.md` in the working layer, then run `tools/episodic-sync.sh`
8. **Commit/push**: Per AI_CONTEXT_COMMIT_PUSH_RULE.md
