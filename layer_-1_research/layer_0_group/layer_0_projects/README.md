# layer_0_projects — Layer 0 Research Projects

This directory contains all layer_0 level research projects being validated before promotion to production.

## Structure

Each research project is a complete entity with its own `.0agnostic/` system, stages (01-11), and layer hierarchy.

## Current Projects

| Project | Status | Purpose |
|---------|--------|---------|
| `layer_-1_better_ai_system` | Active | SHIMI concepts, agent memory, multi-agent sync |
| `layer_-1_langtrak_dev_agent_system` | Active | Development of language tracking agent system |
| `layer_-1_learning_simulation_system` | Active | Research on learning simulation frameworks |

## Adding New Projects

New layer_0 research projects should be created by:
1. Using the `/entity-creation` skill with layer=0
2. Following the canonical directory structure
3. Creating proper `.0agnostic/` resources
4. Registering in parent layer_0_group registry

## Navigation

- **Parent Group**: `../README.md` (layer_0_group)
- **Parent Research**: `../../0AGNOSTIC.md` (layer_-1_research)
- **Registry**: `../layer_0_00_layer_registry/`
- **Stages**: `../layer_0_99_stages/`
- **Promotion Protocol**: `../../.0agnostic/03_protocols/research_promotion_protocol.md`

## Promotion Process

Once a layer_0 project is validated:
1. Complete all relevant stages (through stage 10_current_product)
2. Create handoff documentation in `.0agnostic/05_handoff_documents/`
3. Use research promotion protocol to move to production layer_0
4. Archive research in stage_0_11_archives
