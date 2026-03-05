<!-- derived_from: "f351b53f-90d5-464e-88ac-a751e6fb8d16" -->
# Layer 0 Group Orchestrator

**Type**: Container Orchestrator | **Layer**: 0

## Purpose

Container orchestrator that routes incoming work to the `layer_0_features/` child registry. Does not execute tasks directly — all work is delegated downward to feature entities.

## Modes

| Mode | Purpose | Actors |
|------|---------|--------|
| RouteMode (initial) | Parse incoming tasks and determine routing destination | RouteActor1 (Senior Route Analyst), RouteActor2 (Junior Route Executor) |
| RegistryMode | Maintain registry of child entities, capabilities, and status | RegistryActor1 (Senior Registry Manager), RegistryActor2 (Junior Registry Clerk) |
| MonitorMode | Monitor child health and status, detect issues | MonitorActor1 (Senior Health Monitor), MonitorActor2 (Junior Status Checker) |

## Mode Transitions

```
RouteMode -> RegistryMode -> MonitorMode -> RouteMode (cycle)
```

## State Actors

- **ContainerStateActor** (Container State Manager): Tracks child entities and their status across all modes. Maintains routing history and health status.

## Children

- `layer_0_features/` (Layer0FeaturesOrchestrator) — Routes to research feature entities

## Parent

- `../` (BetterAiSystemOrchestrator)

## Constraints

- Scope limited to routing work to `layer_0_features/`
- Must escalate cross-scope requests to parent
- Do NOT execute tasks directly — route to children
- Layer_0 safety rules with severity='absolute' require user approval to override
