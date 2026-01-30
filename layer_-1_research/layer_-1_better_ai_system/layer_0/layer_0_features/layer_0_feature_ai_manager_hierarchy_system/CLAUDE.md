# layer_0_feature_ai_manager_hierarchy_system

## Overview
Research feature exploring hierarchical AI manager/worker patterns for coordinating multi-agent development workflows.

## Status
**Progress**: ~57% (Phases 1-4 of 7 complete)
**Current Stage**: 02_research

## Purpose
Design and implement a hierarchical system where:
- Managers coordinate work across layers and stages
- Workers perform bounded tasks with clear inputs/outputs
- Handoff documents pass structured state between agents
- Tools are specialized by role (managers use Claude Code, workers use Codex, etc.)

## Key Concepts
- **Layers**: L-1 (Research) → L0 (Features) → L1 (Sub-features) → L2+ (Components)
- **Stages**: 01 (request) → 02 (research) → ... → 10 (current_product) → 11 (archives)
- **Handoffs**: JSON/Markdown documents with task, constraints, artifacts, status
- **Tool Quartets**: CLAUDE.md, AGENTS.md, GEMINI.md per OS/layer

## Structure
```
layer_0_feature_ai_manager_hierarchy_system/
├── CLAUDE.md
├── layer_0/
│   ├── layer_0_00_layer_registry/
│   ├── layer_0_01_ai_manager_system/
│   ├── layer_0_02_manager_handoff_documents/
│   ├── layer_0_03_sub_layers/
│   │   ├── sub_layer_0_01_prompts/
│   │   ├── sub_layer_0_02_knowledge_system/   # overview, things_learned
│   │   ├── sub_layer_0_03_principles/
│   │   ├── sub_layer_0_04_rules/
│   │   └── sub_layer_0_05+_setup_dependant/
│   └── layer_0_99_stages/
│       ├── stage_0_00_stage_registry/
│       ├── stage_0_02_research/               # CURRENT - chat_history
│       ├── stage_0_06_development/            # implementation
│       └── ...
└── layer_1/
    ├── layer_1_features/
    ├── layer_1_sub_projects/
    └── layer_1_components/
```

## Key Locations
| Content | Location |
|---------|----------|
| Overview | `layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/overview/` |
| Research findings | `layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/things_learned/` |
| Chat history | `layer_0/layer_0_99_stages/stage_0_02_research/outputs/chat_history/` |
| Implementation | `layer_0/layer_0_99_stages/stage_0_06_development/outputs/implementation/` |

## Completed Phases
1. ✅ Navigation and overview integration
2. ✅ Framework alignment
3. ✅ Manager/Worker + Handoff standardization
4. ✅ OS and Tool Variants (quartets)

## Remaining Phases
5. ❌ Orchestration and CLI recursion integration
6. ❌ Observability, safety, deployment guidance
7. ❌ Rollout and migration strategy
