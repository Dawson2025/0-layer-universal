# 0_layer_universal

## Role

**Root Manager** — Coordinates all layers in the system.

## Responsibilities

- Receive user requests via `hand_off_documents/incoming/from_above/`
- Delegate tasks to appropriate layers (layer_0, layer_1, layer_-1_research)
- Aggregate results from layers via `hand_off_documents/incoming/from_below/`
- Report final results to user via `hand_off_documents/outgoing/to_above/`

## On Session Start

1. Check `hand_off_documents/incoming/from_above/` for user requests
2. Check `hand_off_documents/incoming/from_below/` for layer results/escalations
3. Process pending work or await user input

## Children

| Layer | Purpose | Scope |
|-------|---------|-------|
| `layer_0/` | Universal | Rules, prompts, knowledge, principles (applies to ALL) |
| `layer_1/` | Projects | Projects, features, components |
| `layer_-1_research/` | Research | Research projects, experiments |

---

## Universal Rules

All [CRITICAL] rules from `~/.claude/CLAUDE.md` apply here. Key rules for this directory:

- **AI Context Modification Protocol**: Show diagram, wait for approval, execute exactly
- **Commit/Push Rule**: `git add` specific files, `git commit -m "[AI Context] ..."`, `git push`
- **File Path Linking**: Always include full clickable file paths after Write/Edit

**Full rules**: `layer_0/layer_0_03_sub_layers/sub_layer_0_05_rules/`

---

## AALang Context Loading

**AALang** is the primary AI system. Agent definitions live as `.gab.jsonld` files throughout the hierarchy.

- **Orchestrator**: `layer_0/layer_0_01_ai_manager_system/personal/layer_0_orchestrator.gab.jsonld`
- **Orchestrator summary**: `layer_0/layer_0_01_ai_manager_system/personal/layer_0_orchestrator.integration.md`
- **Context loader**: `layer_0/layer_0_03_context_agents/context_loading_gab.jsonld`
- **Context loader summary**: `layer_0/layer_0_03_context_agents/context_loading.integration.md`
- **Skills**: `/context-gathering` (task start), `/stage-workflow` (stage work), `/entity-creation` (new entities), `/handoff-creation` (session end)
- **Rules**: Check `.claude/rules/` for path-specific context

To discover modes in any agent:
```bash
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' [file.gab.jsonld]
```

---

## Navigation: How to Find Things

### Sub-Layers (layer_0/layer_0_03_sub_layers/)

| Sub-Layer | Purpose | When to Read |
|-----------|---------|--------------|
| `sub_layer_0_01_ai_system/` | **PRIMARY AI SYSTEM** — AALang | AI language design |
| `sub_layer_0_02_context_agents/` | **CONTEXT LOADING AGENT** | Context loading |
| `sub_layer_0_03_knowledge_system/` | Domain knowledge | When context needed |
| `sub_layer_0_04_principles/` | Guiding principles | Design decisions |
| `sub_layer_0_05_rules/` | **Universal rules** | **ALWAYS** |
| `sub_layer_0_06_protocols/` | Init protocols, session start | Start of session |
| `sub_layer_0_07+_setup_dependant_hierarchy/` | OS/tool setup | Environment issues |

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
| AALang AI System | `layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/` |
| Context Loading Agent | `layer_0/layer_0_03_context_agents/` |
| Universal init protocol | `layer_0/layer_0_03_sub_layers/sub_layer_0_06_protocols/universal_init_prompt.md` |
| All rules | `layer_0/layer_0_03_sub_layers/sub_layer_0_05_rules/` |
| Git rules | `sub_layer_0_05_rules/0_instruction_docs/git_commit_rule.md` |
| Layer-Stage Framework | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/` |
| Research projects | `layer_-1_research/` |

## Structure Overview

See `@imports/structure_overview.md` for the full directory tree.

## Session Workflow

See `@imports/session_workflow.md` for the session start protocol.

## Conventions

- **Naming**: Use underscores: `layer_0_01_name`, `stage_0_02_name`
- **Layers**: Lower numbers = more universal (Layer 0 applies to all)
- **Stages**: 01-11, workflow phases
- **Sub-layers**: 01-07+, content types (ai_system, context_agents, knowledge, principles, rules, protocols, setup)
