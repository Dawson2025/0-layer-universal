# sub_layer_0_02_rules

Universal rules that apply across all layers, stages, OS, and tool contexts.

---

## Directory Structure

```
sub_layer_0_02_rules/
├── README.md                    # This file
├── 0_every_api_request/         # Rules for EVERY interaction (include in prompts)
│   ├── AI_CONTEXT_MODIFICATION_PROTOCOL.md
│   ├── AI_CONTEXT_COMMIT_PUSH_RULE.md
│   └── CONTEXT_TRAVERSAL_RULE.md
├── 1_scenario_based/            # Rules for specific scenarios (reference, don't include)
│   ├── safety_governance.md
│   ├── AI_DOCUMENTATION_PROTOCOL.md
│   ├── LAYER_CONTEXT_HEADER_PROTOCOL.md
│   ├── sequential_development_methodology.md
│   └── CROSS_OS_COMPATIBILITY_RULES.md
└── 0_instruction_docs/          # Additional instruction documents
```

---

## 0_every_api_request (Always Apply)

These rules MUST be followed on EVERY interaction. They should be **summarized in CLAUDE.md files**.

| Rule | Summary |
|------|---------|
| **AI_CONTEXT_MODIFICATION_PROTOCOL** | Show diagram, wait for approval before modifying AI context |
| **AI_CONTEXT_COMMIT_PUSH_RULE** | Git add/commit/push after approved AI context changes |
| **CONTEXT_TRAVERSAL_RULE** | Read CLAUDE.md files and gather context before starting work |

---

## 1_scenario_based (Apply When Relevant)

These rules are important but only apply in specific scenarios. **Reference them in CLAUDE.md** but don't include full content.

| Rule | When to Apply |
|------|---------------|
| **safety_governance** | Security decisions, permission escalations, sensitive operations |
| **AI_DOCUMENTATION_PROTOCOL** | Creating/organizing documentation |
| **LAYER_CONTEXT_HEADER_PROTOCOL** | Creating new files that need layer/stage headers |
| **sequential_development_methodology** | Multi-step development tasks |
| **CROSS_OS_COMPATIBILITY_RULES** | Cross-platform code/scripts |

---

## How to Use in CLAUDE.md Files

### Include summaries of 0_every_api_request rules:

```markdown
## Universal Rules (ALWAYS FOLLOW)

### 1. AI Context Modification Protocol
Before modifying AI context files: show diagram, wait for approval, then execute.

### 2. AI Context Commit/Push Rule
After approved changes: git add, commit, push.

### 3. Context Traversal Rule
Before starting: read CLAUDE.md files in path, identify layer/stage, check sub_layers.
```

### Reference 1_scenario_based rules:

```markdown
## Scenario-Based Rules (Read When Needed)

| Scenario | Rule Location |
|----------|---------------|
| Security decisions | `sub_layer_0_02_rules/1_scenario_based/safety_governance.md` |
| Documentation | `sub_layer_0_02_rules/1_scenario_based/AI_DOCUMENTATION_PROTOCOL.md` |
| File headers | `sub_layer_0_02_rules/1_scenario_based/LAYER_CONTEXT_HEADER_PROTOCOL.md` |
```

---

## Notes

- All rules are **mandatory** unless explicitly marked optional
- Safety rules take precedence over other rules in case of conflict
- Rules in `0_every_api_request/` save context by being summarized rather than fully included
