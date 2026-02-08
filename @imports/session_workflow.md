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
4. **AALang context**: Run jq on nearest `.gab.jsonld` (see CLAUDE.md Steps 1-5)
5. **Do work**: Follow stage guidelines and mode constraints
6. **Commit/push**: Per AI_CONTEXT_COMMIT_PUSH_RULE.md
