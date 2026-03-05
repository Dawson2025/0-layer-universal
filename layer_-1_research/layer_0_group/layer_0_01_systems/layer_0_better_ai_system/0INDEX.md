---
resource_id: "3882a527-06d2-4bc1-9d1e-8faa57279cfc"
resource_type: "index
document"
resource_name: "0INDEX"
---
# Index: layer_-1_better_ai_system

<!-- section_id: "45b25623-ca6d-406e-a217-591f18d8b39f" -->
## Purpose
Research project for improving AI agent systems. Implements concepts for multi-agent sync, automated traversal, and agent memory.

---

<!-- section_id: "253208a7-484e-403d-943f-122997395874" -->
## Structure Overview

```
layer_-1_better_ai_system/
├── 0AGNOSTIC.md              ← Project identity (source of truth)
├── 0INDEX.md                 ← This index
├── CLAUDE.md                 ← Auto-generated (do not edit)
├── .0agnostic/               ← AI tool configuration
│   ├── agents/
│   ├── episodic/{sessions,changes}
│   ├── hooks/scripts/
│   ├── knowledge/
│   ├── rules/
│   └── skills/
├── .1merge/                  ← Tool-specific overrides (6 tools x 3 tiers)
├── .claude/rules/            ← Claude Code config
├── .cursor/rules/            ← Cursor config
├── .github/instructions/     ← GitHub config
├── layer_-1_group/           ← Internals (this layer's content)
│   ├── layer_-1_00_layer_registry/proposals/
│   ├── layer_-1_01_ai_manager_system/
│   ├── layer_-1_02_manager_handoff_documents/
│   │   ├── incoming/{from_above,from_below}
│   │   └── outgoing/{to_above,to_below}
│   ├── layer_-1_03_sub_layers/
│   │   ├── sub_layer_-1_02_knowledge_system/{overview,things_learned}
│   │   └── ... (prompts, principles, rules, setup)
│   └── layer_-1_99_stages/   ← Research workflow stages (01-11)
├── layer_0_group/            ← Children (features)
│   ├── layer_0_00_layer_registry/proposals/
│   └── layer_0_features/
│       ├── layer_0_feature_layer_stage_system/        ← Central pillar: framework, memory, agents, organization
│       ├── layer_0_feature_multi_os_multi_machine_system/  ← Cross-platform setup
│       └── layer_0_feature_multimodal_system/         ← Future: video, audio, TTS/STT, 3D
└── synthesis/
```

---

<!-- section_id: "686d8437-78cf-44dd-adab-c80568e3745f" -->
## Features (layer_0_group)

| Feature | Description | Key Files |
|---------|-------------|-----------|
| layer_stage_system | Central pillar: layer-stage framework, memory/context chains, organization, multi-agent, tool-agnostic | `layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/` |
| multi_os_multi_machine_system | Cross-platform setup, configuration, and synchronization | `layer_0_group/layer_0_features/layer_0_feature_multi_os_multi_machine_system/` |
| multimodal_system | Future multimodal capabilities (video, audio, TTS/STT, 3D) | `layer_0_group/layer_0_features/layer_0_feature_multimodal_system/` |

---

<!-- section_id: "26e5a15d-7f97-48d9-8fbf-3da2e24a821d" -->
## Research Stages (layer_-1_group)

| Stage | Purpose | Location |
|-------|---------|----------|
| 01 | Request Gathering | `layer_-1_group/layer_-1_99_stages/stage_-1_01_request_gathering/` |
| 02 | Research | `layer_-1_group/layer_-1_99_stages/stage_-1_02_research/` |
| 03 | Instructions | `layer_-1_group/layer_-1_99_stages/stage_-1_03_instructions/` |
| 04 | Planning | `layer_-1_group/layer_-1_99_stages/stage_-1_04_planning/` |
| 05 | Design | `layer_-1_group/layer_-1_99_stages/stage_-1_05_design/` |
| 06 | Development | `layer_-1_group/layer_-1_99_stages/stage_-1_06_development/` |
| 07 | Testing | `layer_-1_group/layer_-1_99_stages/stage_-1_07_testing/` |
| 08 | Criticism | `layer_-1_group/layer_-1_99_stages/stage_-1_08_criticism/` |
| 09 | Fixing | `layer_-1_group/layer_-1_99_stages/stage_-1_09_fixing/` |
| 10 | Current Product | `layer_-1_group/layer_-1_99_stages/stage_-1_10_current_product/` |
| 11 | Archives | `layer_-1_group/layer_-1_99_stages/stage_-1_11_archives/` |

---

<!-- section_id: "fb7243f7-f1c2-4115-afe8-d101f10ba4a7" -->
## Key Documents

| Document | Purpose |
|----------|---------|
| [0AGNOSTIC.md](0AGNOSTIC.md) | Project identity and triggers |
| [Proposal v6](layer_-1_group/layer_-1_00_layer_registry/proposals/proposal_ai_friendly_output_organization_v6.md) | AI-friendly output organization |
| [Research Synthesis](layer_-1_group/layer_-1_99_stages/stage_-1_02_research/outputs/synthesis/research_synthesis.md) | Combined research insights |

---

<!-- section_id: "c7812bdb-9600-4971-bf9e-975d4b23525d" -->
## Navigation Guide

| Looking for... | Go to... |
|----------------|----------|
| Proposals | `layer_-1_group/layer_-1_00_layer_registry/proposals/` |
| Research | `layer_-1_group/layer_-1_99_stages/stage_-1_02_research/outputs/` |
| Designs | `layer_-1_group/layer_-1_99_stages/stage_-1_05_design/outputs/` |
| Features | `layer_0_group/layer_0_features/` |
| Session logs | `.0agnostic/episodic/` |

---

*This index enables automated traversal and discovery.*
