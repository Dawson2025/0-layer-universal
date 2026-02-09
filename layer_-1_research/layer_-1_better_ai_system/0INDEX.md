# Index: layer_-1_better_ai_system

## Purpose
Research project for improving AI agent systems. Implements concepts for multi-agent sync, automated traversal, and agent memory.

---

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
│       └── layer_0_feature_agent_performance/  ← Consolidated research feature
└── synthesis/
```

---

## Features (layer_0_group)

| Feature | Description | Key Files |
|---------|-------------|-----------|
| agent_performance | Consolidated research into AI agent architecture, context systems, memory, orchestration, tooling, and organization | `layer_0_group/layer_0_features/layer_0_feature_agent_performance/` |

---

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

## Key Documents

| Document | Purpose |
|----------|---------|
| [0AGNOSTIC.md](0AGNOSTIC.md) | Project identity and triggers |
| [Proposal v6](layer_-1_group/layer_-1_00_layer_registry/proposals/proposal_ai_friendly_output_organization_v6.md) | AI-friendly output organization |
| [Research Synthesis](layer_-1_group/layer_-1_99_stages/stage_-1_02_research/outputs/synthesis/research_synthesis.md) | Combined research insights |

---

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
