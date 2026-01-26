# 0_layer_universal

## FIRST: Read Universal Rules

**BEFORE doing any work**, read and follow rules from:

```
layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/
├── AI_CONTEXT_MODIFICATION_PROTOCOL.md   ← Show diagram before modifying AI context
├── AI_CONTEXT_COMMIT_PUSH_RULE.md        ← Commit and push after AI context changes
├── safety_governance.md                   ← Security boundaries and permissions
└── LAYER_CONTEXT_HEADER_PROTOCOL.md      ← File header requirements
```

## Navigation: How to Find Things

### Sub-Layers (layer_0/layer_0_03_sub_layers/)

| Sub-Layer | Purpose | When to Read |
|-----------|---------|--------------|
| `sub_layer_0_01_prompts/` | Init prompts, session start | Start of session |
| `sub_layer_0_02_knowledge_system/` | Domain knowledge | When context needed |
| `sub_layer_0_03_principles/` | Guiding principles | Design decisions |
| `sub_layer_0_04_rules/` | **Universal rules** | **ALWAYS** |
| `sub_layer_0_05+_setup_dependant/` | OS/tool setup | Environment issues |

### Stages (layer_N/layer_N_99_stages/)

| Stage | Purpose |
|-------|---------|
| 01_request_gathering | Clarify requirements |
| 02_research | Explore, gather info |
| 03_instructions | Define constraints |
| 04_planning | Break into subtasks |
| 05_design | Architecture |
| 06_development | Implementation |
| 07_testing | Verification |
| 08_criticism | Review |
| 09_fixing | Corrections |
| 10_current_product | Deliverable |
| 11_archives | History |

### Quick Lookup

| Need | Location |
|------|----------|
| Universal init prompt | `layer_0/layer_0_03_sub_layers/sub_layer_0_01_prompts/universal_init_prompt.md` |
| All rules | `layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/` |
| Git rules | `sub_layer_0_04_rules/0_instruction_docs/git_commit_rule.md` |
| Terminal protocol | `sub_layer_0_04_rules/0_instruction_docs/MASTER_TERMINAL_EXECUTION_REFERENCE.md` |
| Layer-Stage Framework | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/` |
| Research projects | `layer_-1_research/` |

## Structure Overview

```
0_layer_universal/
├── CLAUDE.md                 ← You are here (navigation guide)
├── .claude/settings.json     ← Tool permissions
├── layer_0/                  ← Universal (applies to ALL)
│   ├── layer_0_03_sub_layers/
│   │   ├── sub_layer_0_01_prompts/      ← Session init
│   │   ├── sub_layer_0_02_knowledge/    ← Domain knowledge
│   │   ├── sub_layer_0_03_principles/   ← Principles
│   │   ├── sub_layer_0_04_rules/        ← RULES (read first!)
│   │   └── sub_layer_0_05+_setup/       ← OS/tool config
│   └── layer_0_99_stages/    ← Universal stages
├── layer_1/                  ← Projects, features
└── layer_-1_research/        ← Research projects
```

## Session Workflow

1. **Sync**: `git pull && git status`
2. **Read rules**: `sub_layer_0_04_rules/` (especially modification protocol)
3. **Read init prompt**: `sub_layer_0_01_prompts/universal_init_prompt.md`
4. **Identify context**: What layer? What stage?
5. **Do work**: Follow stage guidelines
6. **Commit/push**: Per AI_CONTEXT_COMMIT_PUSH_RULE.md

## Conventions

- **Naming**: Use underscores: `layer_0_01_name`, `stage_0_02_name`
- **Layers**: Lower numbers = more universal (Layer 0 applies to all)
- **Stages**: 01-11, workflow phases
- **Sub-layers**: 01-05+, content types (prompts, knowledge, rules, etc.)
