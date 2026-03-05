---
resource_id: "3ab7badf-f1ae-4787-9016-859c69c55f9c"
resource_type: "document"
resource_name: "structure_overview"
---
# Structure Overview

```
0_layer_universal/
├── CLAUDE.md                 ← Root Manager
├── .claude/                  ← Tool permissions, settings, skills, rules
├── hand_off_documents/       ← Four-directional communication
│   ├── incoming/from_above/  ← User requests
│   ├── incoming/from_below/  ← Layer results
│   ├── outgoing/to_above/    ← Results to user
│   └── outgoing/to_below/    ← Tasks to layers
├── layer_0/                  ← Universal (applies to ALL)
│   ├── layer_0_01_ai_manager_system/
│   │   ├── professor/        ← AALang/GAB (submodule)
│   │   └── personal/         ← Orchestrator
│   ├── layer_0_02_manager_handoff_documents/
│   ├── layer_0_03_context_agents/
│   ├── layer_0_04_sub_layers/
│   │   ├── sub_layer_0_01_knowledge_system/ (incl. principles/)
│   │   ├── sub_layer_0_02_rules/           ← READ FIRST (static/ + dynamic/)
│   │   ├── sub_layer_0_03_protocols/
│   │   └── sub_layer_0_04+_setup_dependant/
│   └── layer_0_99_stages/
├── layer_1/                  ← Projects, features
└── layer_-1_research/        ← Research projects
```
