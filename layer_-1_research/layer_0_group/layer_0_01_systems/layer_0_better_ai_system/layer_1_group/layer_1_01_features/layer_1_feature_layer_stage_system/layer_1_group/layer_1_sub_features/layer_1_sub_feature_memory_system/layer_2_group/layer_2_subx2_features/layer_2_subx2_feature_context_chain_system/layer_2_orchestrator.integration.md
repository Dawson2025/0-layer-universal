<!-- derived_from: "a79b61a7-c4ab-4c93-bed5-bbcc8af0f1a9" -->
# Context Chain System Orchestrator

**Type**: Entity Orchestrator | **Layer**: 2

## Purpose
Research orchestrator for context chain architecture — how context flows through the layer-stage hierarchy.

## Modes
| Mode | Purpose | Actors |
|------|---------|--------|
| ReceiveMode | Parse incoming context chain research tasks, validate scope | ReceiveActor1 (Senior Chain Task Analyst), ReceiveActor2 (Junior Chain Task Logger) |
| ResearchMode | Investigate context chain patterns, analyze context flow | ResearchActor1 (Senior Chain Researcher), ResearchActor2 (Junior Chain Pattern Finder) |
| DesignMode | Design context chain architecture improvements | DesignActor1 (Senior Chain Architect), DesignActor2 (Junior Chain Specification Writer) |
| ImplementMode | Execute designs, create context chain artifacts | ImplementActor1 (Senior Chain Builder), ImplementActor2 (Junior Chain Artifact Writer) |
| ReviewMode | Validate output, ensure quality | ReviewActor1 (Senior Chain Reviewer), ReviewActor2 (Junior Chain Validator) |

## State Actors
- **LayerStateActor**: Tracks layer position and inheritance chain
- **ChildRegistryStateActor**: Tracks child entities and their status
- **TaskStateActor**: Tracks active research tasks and their progress

## Children
- chain_visualization
- context_loading

## Constraints
- Scope is limited to context chain architecture research
- Must escalate cross-feature requests to memory_system orchestrator
- Must respect layer_0 safety rules
- Research output belongs in stage directories, not production systems

## Mode Flow
ReceiveMode -> ResearchMode -> DesignMode -> ImplementMode -> ReviewMode -> ReceiveMode

## Inheritance
- **Parent**: Memory System Orchestrator (`../../../`)
- **Inherits from**: memory_system
- **Can override**: non-safety context
