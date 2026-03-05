<!-- derived_from: "8da21493-e9da-4430-a539-b9531dab5110" -->
# OpenAI Context


## Identity

You are an agent at **Layer 0** (AI System), researched at **Layer -1** (Research).

- **Role**: Research Project Manager - Coordinate research into improving AI system architecture
- **Scope**: Research, design, planning for AI framework improvements. Does not implement in production systems.
- **Parent**: `../../../0AGNOSTIC.md` (layer_-1_research)
- **Children**: `layer_0_group/layer_0_features/` contains 3 research features (layer_stage_system, multi_os_multi_machine_system, multimodal_system)

## Triggers

Load this context when:
- User mentions: "better ai system", "framework improvements", "layer-stage research"
- Working on: AI architecture, context systems, memory systems, manager hierarchies
- Entering: `/layer_-1_research/layer_0_group/layer_0_01_systems/layer_0_better_ai_system/`

## Pointers

### On Entry
1. Read `0INDEX.md` for current state and stage status
2. Check `.0agnostic/episodic/index.md` for recent sessions

### Resources (load on-demand)
| Resource | Location |
|----------|----------|
| Orchestrator Agent | `better_ai_system_orchestrator.gab.jsonld` (+ `.integration.md`) |
| Rules | `.0agnostic/02_rules/` |
| Knowledge | `.0agnostic/01_knowledge/` |
| Agents | `.0agnostic/agents/` |
| Skills | `.0agnostic/skills/` |
| Proposals | `layer_-1_group/layer_-1_00_layer_registry/proposals/` |

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Features | `layer_0_group/layer_0_features/` |
| Stages | `layer_0_group/layer_0_99_stages/` |

## Where to Contribute

| Work Type | Location |
|-----------|----------|
| Research | `layer_0_group/layer_0_99_stages/stage_0_02_research/outputs/` |
| Instructions | `layer_0_group/layer_0_99_stages/stage_0_03_instructions/outputs/` |
| Design | `layer_0_group/layer_0_99_stages/stage_0_04_design/outputs/` |
| Proposals (org changes) | `layer_0_group/layer_0_00_layer_registry/proposals/` |
| Session notes | `.0agnostic/episodic/sessions/` |

## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
