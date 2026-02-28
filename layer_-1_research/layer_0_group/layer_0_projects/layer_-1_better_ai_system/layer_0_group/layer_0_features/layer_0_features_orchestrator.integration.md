# Layer 0 Features Orchestrator

**Type**: Container Orchestrator | **Layer**: 0

## Purpose

Container orchestrator that routes incoming work to 3 research feature children: layer_stage_system, multi_os_multi_machine_system, and multimodal_system. Does not execute tasks directly — all work is delegated to feature entities.

## Modes

| Mode | Purpose | Actors |
|------|---------|--------|
| RouteMode (initial) | Parse incoming tasks and determine which feature child to route to | RouteActor1 (Senior Feature Router), RouteActor2 (Junior Feature Dispatcher) |
| RegistryMode | Maintain registry of feature children, capabilities, and status | RegistryActor1 (Senior Feature Registry Manager), RegistryActor2 (Junior Feature Cataloger) |
| MonitorMode | Monitor feature child health and status, detect issues | MonitorActor1 (Senior Feature Monitor), MonitorActor2 (Junior Feature Status Tracker) |

## Mode Transitions

```
RouteMode -> RegistryMode -> MonitorMode -> RouteMode (cycle)
```

## State Actors

- **ContainerStateActor** (Feature Container State Manager): Tracks feature child entities and their status across all modes. Maintains routing history and health status.

## Children

- `layer_0_feature_layer_stage_system/` (LayerStageSystemOrchestrator) — Layer-stage system research, memory system, context chain system
- `layer_0_feature_multi_os_multi_machine_system/` (MultiOsSystemOrchestrator) — Multi-OS support research, multi-machine coordination
- `layer_0_feature_multimodal_system/` (MultimodalSystemOrchestrator) — Multimodal AI research, multi-interface support

## Parent

- `../` (Layer0GroupOrchestrator)

## Constraints

- Scope limited to routing work to the 3 feature children
- Must escalate cross-scope requests to parent layer_0_group orchestrator
- Do NOT execute tasks directly — route to children
- Layer_0 safety rules with severity='absolute' require user approval to override
