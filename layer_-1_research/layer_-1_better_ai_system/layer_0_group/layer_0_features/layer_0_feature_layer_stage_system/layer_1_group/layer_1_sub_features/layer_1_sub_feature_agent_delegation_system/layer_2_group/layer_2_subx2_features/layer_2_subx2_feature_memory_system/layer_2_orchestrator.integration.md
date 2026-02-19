# Memory System Orchestrator

**Type**: Entity Orchestrator | **Layer**: 1

## Purpose
Research orchestrator for memory and context systems — how AI agents remember, load, and navigate context.

## Modes
| Mode | Purpose | Actors |
|------|---------|--------|
| ReceiveMode | Parse incoming memory research tasks, validate scope | ReceiveActor1 (Senior Memory Task Receiver), ReceiveActor2 (Junior Task Registrar) |
| ResearchMode | Investigate memory systems, gather data on context persistence | ResearchActor1 (Senior Memory Researcher), ResearchActor2 (Junior Data Gatherer) |
| DesignMode | Design memory architecture improvements | DesignActor1 (Senior Memory Architect), DesignActor2 (Junior Schema Designer) |
| ImplementMode | Execute designs, create memory system artifacts | ImplementActor1 (Senior Memory Implementer), ImplementActor2 (Junior Context Builder) |
| ReviewMode | Validate output, ensure quality | ReviewActor1 (Senior Memory Reviewer), ReviewActor2 (Junior Consistency Checker) |

## State Actors
- **LayerStateActor**: Tracks layer position and inheritance chain
- **ChildRegistryStateActor**: Tracks child sub-feature entities and their status
- **TaskStateActor**: Tracks active research tasks and their progress

## Children
- context_chain_system
- navigation
- dynamic_memory

## Constraints
- Scope is limited to memory and context system research
- Must escalate cross-feature requests to layer_stage_system orchestrator
- Must respect layer_0 safety rules
- Research output belongs in stage directories, not production systems

## Mode Flow
ReceiveMode -> ResearchMode -> DesignMode -> ImplementMode -> ReviewMode -> ReceiveMode

## Inheritance
- **Parent**: Layer Stage System Orchestrator (`../../../`)
- **Inherits from**: layer_stage_system
- **Can override**: non-safety context
