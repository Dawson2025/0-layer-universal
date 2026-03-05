<!-- derived_from: "8d73b1e4-c3f8-4f91-b816-324d7e76b294" -->
# Layer Stage System Orchestrator

**Type**: Entity Orchestrator | **Layer**: 0

## Purpose
Research orchestrator for the layer-stage framework — the hierarchical organization system for all AI context.

## Modes
| Mode | Purpose | Actors |
|------|---------|--------|
| ReceiveMode | Parse incoming research tasks, validate scope | ReceiveActor1 (Senior Research Intake Analyst), ReceiveActor2 (Junior Research Logger) |
| ResearchMode | Investigate existing work, gather data, analyze patterns | ResearchActor1 (Senior Framework Investigator), ResearchActor2 (Junior Pattern Collector) |
| DesignMode | Design solutions, create specifications | DesignActor1 (Senior Architecture Designer), DesignActor2 (Junior Specification Writer) |
| ImplementMode | Execute designs, create artifacts | ImplementActor1 (Senior Framework Builder), ImplementActor2 (Junior Artifact Creator) |
| ReviewMode | Validate output, ensure quality | ReviewActor1 (Senior Quality Reviewer), ReviewActor2 (Junior Validation Checker) |

## State Actors
- **LayerStateActor**: Tracks layer position and inheritance chain
- **ChildRegistryStateActor**: Tracks child sub-feature entities and their status
- **TaskStateActor**: Tracks active research tasks and their progress

## Children
- memory_system
- organization
- multi_agent_system
- tool_and_app_agnostic

## Constraints
- Scope is limited to layer-stage framework research and its sub-features
- Must escalate cross-feature requests to layer_0_features
- Must respect layer_0 safety rules
- Research output belongs in stage directories, not production systems

## Mode Flow
ReceiveMode -> ResearchMode -> DesignMode -> ImplementMode -> ReviewMode -> ReceiveMode

## Inheritance
- **Parent**: Layer 0 Features Orchestrator (`../`)
- **Inherits from**: layer_0_features
- **Can override**: non-safety context
