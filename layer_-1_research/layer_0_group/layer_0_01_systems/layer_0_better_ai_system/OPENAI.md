# OpenAI Context

---
resource_id: "20d89d9d-e237-4e70-8254-100e464c38d5"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md - layer_0_better_ai_system

<!-- section_id: "a8daf4bf-df93-45a2-a38d-fbd19c46d584" -->
## Identity

entity_id: "8da21493-e9da-4430-a539-b9531dab5110"


You are an agent at **Layer 0** (AI System), researched at **Layer -1** (Research).

- **Role**: Research Project Manager - Coordinate research into improving AI system architecture
- **Scope**: Research, design, planning for AI framework improvements. Does not implement in production systems.
- **Parent**: `../../../0AGNOSTIC.md` (layer_-1_research)
- **Children**: `layer_0_group/layer_0_features/` contains 3 research features (layer_stage_system, multi_os_multi_machine_system, multimodal_system)

<!-- section_id: "eb55b5fd-d1c7-4434-9296-19f4e36a49c7" -->
## Triggers

Load this context when:
- User mentions: "better ai system", "framework improvements", "layer-stage research"
- Working on: AI architecture, context systems, memory systems, manager hierarchies
- Entering: `/layer_-1_research/layer_0_group/layer_0_01_systems/layer_0_better_ai_system/`

<!-- section_id: "856d8791-930c-4638-b02f-2d30e09f4488" -->
## Pointers

<!-- section_id: "21469ece-03bb-4d5b-a21e-cda6e4137cdc" -->
### On Entry
1. Read `0INDEX.md` for current state and stage status
2. Check `.0agnostic/episodic/index.md` for recent sessions

<!-- section_id: "f7e73fcc-87bc-44cd-bf8e-63b6aa16c56c" -->
### Resources (load on-demand)
| Resource | Location |
|----------|----------|
| Orchestrator Agent | `better_ai_system_orchestrator.gab.jsonld` (+ `.integration.md`) |
| Rules | `.0agnostic/02_rules/` |
| Knowledge | `.0agnostic/01_knowledge/` |
| Agents | `.0agnostic/agents/` |
| Skills | `.0agnostic/skills/` |
| Proposals | `layer_-1_group/layer_-1_00_layer_registry/proposals/` |

<!-- section_id: "512dcf61-f639-4a90-945c-fd24d9394568" -->
### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Features | `layer_0_group/layer_0_features/` |
| Stages | `layer_0_group/layer_0_99_stages/` |

<!-- section_id: "cc3fcdaf-dcfb-4dfe-8b8f-ee1ba11d4e91" -->
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
