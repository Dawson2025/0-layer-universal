# Better AI System - Research Project

**Status**: Stage 01 (Research) - Active

## Purpose

Research and design improvements to the AI-assisted development system, exploring:
- Hierarchical manager/worker architectures
- Dynamic memory systems for AI context
- Framework orchestration patterns
- Observability and safety mechanisms

## Structure

```
better_ai_system/
├── CLAUDE.md                    # AI context for this project
├── README.md                    # This file
├── layer_1/                     # Project organization
│   ├── layer_1_00_ai_manager_system/
│   ├── layer_1_01_manager_handoff_documents/
│   ├── layer_1_02_sub_layers/
│   └── layer_1_99_stages/       # Project stages
│       ├── stage_1_00_request_gathering/
│       ├── stage_1_01_research/      # CURRENT STAGE
│       ├── stage_1_02_instructions/
│       └── ...
└── layer_2/
    └── layer_2_features/        # Research topics
        ├── layer_2_feature_ai_manager_hierarchy_system/
        ├── layer_2_feature_ai_dynamic_memory_system/
        └── layer_2_feature_multi_os_system/
```

## Research Features

### 1. AI Manager Hierarchy System (~57% complete)
Designing a hierarchical system where:
- **Managers** coordinate work, spawn workers, aggregate results
- **Workers** do bounded tasks and exit
- **Handoffs** pass structured state between agents
- **Tools** are specialized (Claude Code for managers, Codex for workers, etc.)

**Key Docs:**
- `layer_2/layer_2_features/layer_2_feature_ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`
- `layer_2/layer_2_features/layer_2_feature_ai_manager_hierarchy_system/implementation/artifacts/progress_assessment.md`

### 2. AI Dynamic Memory System (Early Research)
Exploring data structures and algorithms for:
- Dynamic context management
- Memory hierarchies for AI agents
- Efficient retrieval and storage patterns

**Key Docs:**
- `layer_2/layer_2_features/layer_2_feature_ai_dynamic_memory_system/chat_history/`

### 3. Multi-OS System (~85% complete)
Cross-OS workspace synchronization and remote access:
- **Syncthing**: File sync via VPS relay (Ubuntu ↔ VPS ↔ Windows)
- **SSH Mesh**: Full connectivity between all devices
- **Health Monitoring**: Automated status checks and self-healing

**Key Docs:**
- `layer_2/layer_2_features/layer_2_feature_multi_os_system/STATUS.md`
- `layer_2/layer_2_features/layer_2_feature_multi_os_system/README.md`

## Current Focus

The AI Manager Hierarchy System has phases 1-4 complete:
1. ✅ Navigation and overview integration
2. ✅ Framework alignment
3. ✅ Manager/Worker + Handoff standardization
4. ✅ OS and Tool Variants (quartets)

Remaining work:
5. ❌ Orchestration and CLI recursion
6. ❌ Observability, safety, deployment
7. ❌ Rollout and migration strategy

## How to Contribute

1. Check the current stage in `layer_1/layer_1_99_stages/status_1.json`
2. Review existing research in `layer_2/layer_2_features/`
3. Add findings to the appropriate feature's `things_learned/` directory
4. Update handoff documents when transitioning work
