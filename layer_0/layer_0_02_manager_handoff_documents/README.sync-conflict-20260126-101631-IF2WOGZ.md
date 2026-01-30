# Layer 0 Universal Manager Handoff Documents

## Overview

This directory contains handoff documents for **Layer 0 (Universal)** managers. Handoffs are the primary mechanism for communicating work, state, and results between layers, stages, and agents in the AI Manager Hierarchy System.

## Purpose

Manager handoff documents at Layer 0 serve two purposes:

1. **External Communication** (`0.00_to_universal/`): Handoffs between external users/systems and the Layer 0 manager
2. **Downward Communication** (`0.01_to_specific/`): Handoffs between Layer 0 and Layer 1 (Project) managers

## Directory Structure

```
0.01_manager_handoff_documents/
├── README.md (this file)
├── 0.00_to_universal/
│   ├── incoming.json          # External requests into Layer 0
│   ├── outgoing.json          # Layer 0 results back to external
│   └── handoff_schema.md      # CANONICAL HANDOFF SCHEMA
└── 0.01_to_specific/
    ├── incoming.json          # Results from Layer 1 projects
    ├── outgoing.json          # Tasks to Layer 1 projects
    ├── incoming/              # Optional: multiple project results
    │   ├── project-a.json
    │   └── project-b.json
    └── outgoing/              # Optional: multiple project tasks
        ├── project-a.json
        └── project-b.json
```

## Handoff Schema

All handoffs must conform to the **canonical handoff schema** defined in:

**[0.00_to_universal/handoff_schema.md](0.00_to_universal/handoff_schema.md)**

This schema defines:
- Required and optional fields
- Data types and validation rules
- Vertical (layer-to-layer) and horizontal (stage-to-stage) handoff patterns
- Example handoffs for common scenarios
- Extensibility guidelines

**Always consult the schema document when creating or reading handoffs.**

## Handoff Flows at Layer 0

### External → Layer 0 (Incoming)

**File**: `0.00_to_universal/incoming.json`

**Content**: User requests, system-triggered tasks, or external work items

**Example**:
```json
{
  "schemaVersion": "1.0.0",
  "id": "external-request-20241223-001",
  "layer": 0,
  "stage": "request",
  "from": "user:john@example.com",
  "to": "layer_0/stage_0_01_request_gathering",
  "task": "Create new web application for project management",
  "status": "pending",
  "createdAt": "2024-12-23T10:00:00Z"
}
```

### Layer 0 → External (Outgoing)

**File**: `0.00_to_universal/outgoing.json`

**Content**: Final results, completion status, aggregated outcomes

**Example**:
```json
{
  "schemaVersion": "1.0.0",
  "id": "external-response-20241223-001",
  "layer": 0,
  "stage": "archiving",
  "from": "layer_0/stage_0_09_archives",
  "to": "user:john@example.com",
  "task": "Web application project management system",
  "status": "completed",
  "results": {
    "summary": "Successfully created project management web app with 3 core features",
    "projectsCreated": ["project-mgmt-webapp"],
    "featuresImplemented": ["task-tracking", "team-collaboration", "reporting"],
    "deploymentUrl": "https://pm.example.com"
  },
  "createdAt": "2024-12-23T10:00:00Z",
  "updatedAt": "2024-12-30T15:30:00Z"
}
```

### Layer 0 → Layer 1 (Downward)

**File**: `0.01_to_specific/outgoing.json` (or `outgoing/project-*.json`)

**Content**: Project-level tasks with universal constraints applied

**Example**:
```json
{
  "schemaVersion": "1.0.0",
  "id": "l0-to-l1-webapp-20241223",
  "kind": "vertical",
  "layer": 0,
  "from": "layer_0/stage_0_04_planning",
  "to": "layer_1/projects/pm-webapp/request",
  "task": "Implement project management web application",
  "constraints": [
    "All Layer 0 universal constraints apply",
    "Use TypeScript strict mode",
    "Follow security best practices (no secrets, input validation)",
    "Comprehensive testing (>80% coverage)",
    "Complete API and component documentation"
  ],
  "acceptanceCriteria": [
    "Users can create, update, and delete tasks",
    "Team collaboration features working",
    "Reporting dashboard functional",
    "All tests passing",
    "Documentation complete"
  ],
  "status": "pending",
  "createdAt": "2024-12-23T11:00:00Z"
}
```

### Layer 1 → Layer 0 (Upward)

**File**: `0.01_to_specific/incoming.json` (or `incoming/project-*.json`)

**Content**: Project results, aggregated metrics, learnings

**Example**:
```json
{
  "schemaVersion": "1.0.0",
  "id": "l1-to-l0-webapp-complete-20241223",
  "kind": "vertical",
  "layer": 1,
  "from": "layer_1/projects/pm-webapp/archiving",
  "to": "layer_0/archiving",
  "task": "Project management web application complete",
  "status": "completed",
  "results": {
    "summary": "Web app successfully implemented with all features",
    "featuresCompleted": ["task-tracking", "team-collaboration", "reporting"],
    "metrics": {
      "duration": "1 week",
      "testCoverage": 87.3,
      "componentsBuilt": 34
    }
  },
  "nextActions": [
    "Consider adding real-time collaboration to universal feature library",
    "Update universal docs with task management patterns discovered"
  ],
  "createdAt": "2024-12-23T11:00:00Z",
  "updatedAt": "2024-12-30T15:00:00Z"
}
```

## Multiple Projects

When Layer 0 manages multiple projects in parallel, use subdirectories:

**Outgoing to multiple projects**:
```
0.01_to_specific/outgoing/
  ├── project-webapp.json
  ├── project-mobile-app.json
  └── project-api-service.json
```

**Incoming from multiple projects**:
```
0.01_to_specific/incoming/
  ├── project-webapp.json
  ├── project-mobile-app.json
  └── project-api-service.json
```

Each file follows the canonical handoff schema.

## Best Practices

1. **Always validate against schema**: Check that handoffs include all required fields
2. **Use unique IDs**: Generate globally unique handoff IDs for traceability
3. **Preserve parent context**: Include `parentIds` to maintain DAG lineage
4. **Be specific in constraints**: Clearly list all applicable universal rules
5. **Provide clear acceptance criteria**: Define measurable success conditions
6. **Update timestamps**: Set `createdAt` on creation, `updatedAt` on modifications
7. **Status tracking**: Keep `status` field current (pending → in_progress → completed/failed)
8. **Human-readable**: Write `task` and other text fields for human understanding, not just machines

## Related Documentation

- **Canonical Schema**: [0.00_to_universal/handoff_schema.md](0.00_to_universal/handoff_schema.md) ← **START HERE**
- **Layer 0 Manager System**: [../0.00_ai_manager_system/README.md](../0.00_ai_manager_system/README.md)
- **Architecture Reference**: [../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md](../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md)
- **Parallel Execution**: [../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md](../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md)
