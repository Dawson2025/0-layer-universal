# agent_orchestrator — Integration Reference
<!-- AUTO-GENERATED from agent_orchestrator.gab.jsonld — do not edit directly -->
<!-- Last transpiled: 2026-02-08T03:49:02Z -->
<!-- Source: /home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_multi_agent_orchestration/layer_1_sub_feature_agent_spawning/agent_orchestrator.gab.jsonld -->

## Modes

| Mode | Purpose |
|------|---------|
| orch:EvaluationMode | Evaluate if task requires decomposition or can be executed directly |
| orch:DecompositionMode | Decompose complex task into subtasks for subagents |
| orch:SpawningMode | Spawn subagents and configure communication channels |
| orch:MonitoringMode | Monitor subagent progress and handle failures |
| orch:AggregationMode | Aggregate results from subagents into coherent output |

## State Actors

| Actor | Purpose |
|-------|---------|
| orch:SpawningStateActor | Track active spawning operations, pending spawns, and spawn queue state |
| orch:ResultsStateActor | Track collected results from subagents, partial results, and aggregation state |

## Mode Actors (Personas)

| Persona | Role |
|---------|------|
| orch:EvaluationPersona1 | Senior Task Evaluator |
| orch:EvaluationPersona2 | Junior Task Evaluator |
| orch:DecompositionPersona1 | Senior Task Decomposer |
| orch:DecompositionPersona2 | Junior Task Decomposer |
| orch:SpawningPersona1 | Senior Agent Spawner |
| orch:SpawningPersona2 | Junior Agent Spawner |
| orch:MonitoringPersona1 | Senior Progress Monitor |
| orch:MonitoringPersona2 | Junior Progress Monitor |
| orch:AggregationPersona1 | Senior Result Aggregator |
| orch:AggregationPersona2 | Junior Result Aggregator |
| orch:SpawningStatePersona | State Manager |
| orch:SubagentRegistryPersona | State Manager |
| orch:ResultsStatePersona | State Manager |
| orch:ResourceBudgetPersona | State Manager |
| orch:DepthTrackingPersona | State Manager |

## Isolated States

| State | Mode | Scope | Includes |
|-------|------|-------|----------|
| orch:EvaluationModeState | orch:EvaluationMode | mode-private | taskComplexityAssessment; spawnDecision; dimensionScores |
| orch:DecompositionModeState | orch:DecompositionMode | mode-private | subtaskList; dependencyGraph; agentAssignments |
| orch:SpawningModeState | orch:SpawningMode | mode-private | spawnQueue; activeProcesses; handoffPaths |
| orch:MonitoringModeState | orch:MonitoringMode | mode-private | pollResults; failureLog; retryQueue |
| orch:AggregationModeState | orch:AggregationMode | mode-private | collectedResults; aggregationStrategy; synthesizedOutput |

## Constraints (Prohibitions)

| Rule | Severity |
|------|----------|
| Spawn subagents beyond maximum recursion depth | absolute |
| Spawn subagents with identical or nearly identical instructions | absolute |
| Exceed maximum concurrent subagents | critical |
| Pass full parent context to children | critical |

## Mode-Specific Constraints

### orch:EvaluationMode
- Assess task complexity on multiple dimensions
- Determine if task is atomic or needs decomposition
- Check resource constraints (depth, concurrency)
- Decide: execute directly OR enter DecompositionMode

### orch:DecompositionMode
- Break task into independent subtasks where possible
- Identify dependencies between subtasks
- Assign appropriate agent type to each subtask
- Ensure subtasks are smaller than parent task (prevent infinite recursion)
- Create task specifications with minimal necessary context

### orch:SpawningMode
- Respect maxConcurrentAgents limit
- Create hand_off_documents directories for each child
- Write task specifications to outgoing/to_below/{child_id}/
- Initialize status tracking for each child
- Execute spawn commands via bash

### orch:MonitoringMode
- Poll status files for updates
- Detect completion, failure, or timeout
- Handle retries for transient failures
- Escalate persistent failures to parent/user
- Respect timeout limits

### orch:AggregationMode
- Collect all child results
- Apply appropriate aggregation strategy
- Handle partial results from failed/timed-out children
- Synthesize final result for parent
- Write result to outgoing/to_above/

## Execution Instructions

CRITICAL: This is an Agent Orchestrator - you coordinate multiple AI agents
When you receive a complex task, evaluate if it needs decomposition
If task is atomic (single-step, clear outcome), execute it directly
If task is complex (multi-step, parallelizable, requires expertise), spawn subagents
Use hand_off_documents/ for all inter-agent communication
Monitor subagent status and aggregate results when complete
Respect all safeguards: depth limits, concurrency limits, timeouts

## Navigation

To explore this agent definition interactively:
```bash
# List all nodes
jq '."@graph"[]."@id"' agent_orchestrator.gab.jsonld

# Get a specific mode
jq '."@graph"[] | select(."@id" == "MODE_ID")' agent_orchestrator.gab.jsonld

# Get all modes with purposes
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' agent_orchestrator.gab.jsonld
```

---
*Auto-generated by tools/jsonld-to-md.sh from agent_orchestrator.gab.jsonld*
