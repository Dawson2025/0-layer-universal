# Layer 0 (Universal) AI Manager System

## Overview

This directory contains the AI manager system for **Layer 0 - Universal**, the highest level of abstraction in the AI Manager Hierarchy System. Layer 0 defines global rules, constraints, and workflows that apply to all work across all projects, features, and components.

## Manager/Worker Roles at Layer 0

### Manager Responsibilities

The **Layer 0 Manager** is responsible for:

1. **Accepting External Requests**: Receives user requests or system-triggered work items
2. **Universal Constraint Application**: Ensures all work adheres to universal rules:
   - Programming language standards (TypeScript, Python conventions)
   - Security and safety policies (no secrets, input validation, etc.)
   - Code quality and testing expectations
   - Documentation and organization standards
3. **High-Level Decomposition**: Breaks down requests into project-level tasks for Layer 1 managers
4. **Cross-Project Orchestration**: Coordinates work that spans multiple projects or impacts universal infrastructure
5. **Aggregation and Reporting**: Collects results from lower layers and synthesizes final outcomes

### Worker Characteristics

At Layer 0, workers are typically:
- **Research agents**: Gathering context about universal standards or new technologies
- **Policy reviewers**: Ensuring compliance with universal rules
- **Documentation generators**: Creating or updating universal documentation

Layer 0 workers are less common than Layer 0 managers, as most execution happens at lower layers.

### Tool Recommendations

Based on the ideal hierarchy system:

- **Managers**: **Claude Code** or **Gemini CLI**
  - Claude Code for deep reasoning and multi-file context
  - Gemini CLI for long research and planning sessions
- **Workers**: **Claude Code** for complex analysis tasks
  - **Codex CLI** for simple universal documentation updates

## Handoff Consumption and Production

### Incoming Handoffs (Upstream)

Layer 0 receives handoffs from:
- **External Users**: Initial requests via `stage_0_01_request_gathering`
- **System Triggers**: Automated tasks (e.g., scheduled audits, dependency updates)

**Location**: `layer_0/layer_0_99_stages/stage_0_01_request_gathering/hand_off_documents/incoming.json`

**Characteristics**:
- May be informal or unstructured initially
- Converted to structured handoffs during request gathering stage
- Contain high-level goals without implementation details

### Outgoing Handoffs (Downstream)

Layer 0 produces handoffs for:
- **Layer 1 (Project)**: Project-level tasks with universal constraints applied
- **Internal Stages**: Between Layer 0 stages (request → instructions → planning → etc.)

**Vertical Handoffs to Layer 1**:
- **Location**: `layer_0/layer_0_02_manager_handoff_documents/layer_0_01_to_specific/outgoing.json`
- **Content**:
  - High-level project goals
  - All applicable universal constraints
  - Acceptance criteria that include universal quality bars
  - References to universal documentation and standards

**Horizontal Handoffs (Stage-to-Stage)**:
- **Location**: Each stage's `hand_off_documents/outgoing.json` → next stage's `incoming.json`
- **Content**: Progressively refined understanding of the work as it moves through the pipeline

### Upward Handoffs (From Layer 1)

Layer 0 receives result handoffs from Layer 1:
- **Location**: `layer_0/layer_0_02_manager_handoff_documents/layer_0_01_to_specific/incoming.json`
- **Content**:
  - Aggregated results from all project-level work
  - Metrics and outcomes
  - Discovered issues or improvements to universal rules
  - Recommendations for universal documentation updates

## Stage Pipeline

Layer 0 operates through a chronological pipeline of stages:

1. **stage_0_01_request_gathering**: Clarify and structure incoming requests
2. **stage_0_02_research**: Gather context and explore solutions
3. **stage_0_03_instructions**: Transform requests into explicit instructions with universal constraints
4. **stage_0_04_planning**: Decompose into project-level tasks and dependencies
5. **stage_0_05_design**: Define high-level architecture and cross-project patterns
6. **stage_0_06_development**: Implement universal infrastructure or update universal docs
7. **stage_0_07_testing**: Verify universal rules and infrastructure
8. **stage_0_08_criticism**: Review against universal quality standards
9. **stage_0_09_fixing**: Resolve issues found in criticism
10. **stage_0_10_current_product**: Active deliverables and system guides
11. **stage_0_11_archives**: Record decisions, patterns, and final artifacts

Each stage:
- Reads from its `incoming` handoff
- Performs stage-specific work
- Writes results to its `outgoing` handoff
- May spawn workers for parallel subtasks

## Handoff Flow Example

### Scenario: User wants to add a new web application project

1. **Request Stage** receives user input:
   ```json
   {
     "schemaVersion": "1.0.0",
     "id": "l0-request-new-webapp-20241223",
     "layer": 0,
     "stage": "request",
     "from": "user",
    "to": "layer_0/stage_0_01_request_gathering",
     "task": "Create new web application for task management",
     "status": "pending"
   }
   ```

2. **Instructions Stage** adds universal constraints:
   ```json
   {
     "schemaVersion": "1.0.0",
     "id": "l0-instructions-new-webapp-20241223",
     "layer": 0,
     "stage": "instructions",
    "from": "layer_0/stage_0_03_instructions",
    "to": "layer_0/stage_0_04_planning",
     "task": "Create new web application for task management",
     "constraints": [
       "Use TypeScript strict mode",
       "Follow Layer 0 security rules (no hardcoded secrets)",
       "Implement comprehensive error handling",
       "Include unit and integration tests with >80% coverage",
       "Document all public APIs and components"
     ],
     "status": "completed"
   }
   ```

3. **Planning Stage** decomposes to Layer 1:
   ```json
   {
     "schemaVersion": "1.0.0",
     "id": "l0-to-l1-webapp-project-20241223",
     "kind": "vertical",
     "layer": 0,
    "from": "layer_0/stage_0_04_planning",
     "to": "layer_1/projects/task-manager/request",
     "task": "Implement task management web application",
     "constraints": [
       "All Layer 0 universal constraints apply",
       "Use TypeScript strict mode",
       "Follow security, testing, and documentation standards"
     ],
     "subtasks": [
       "Define project architecture and tech stack",
       "Implement core features (task CRUD, auth, notifications)",
       "Deploy to production environment"
     ],
     "status": "pending"
   }
   ```

## Deeper References

For comprehensive understanding of the manager/worker model, handoff protocol, and orchestration patterns, see:

- **Architecture**: [ideal_ai_manager_hierarchy_system/architecture.md](../../layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_ai_manager_hierarchy_system/layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md)
- **Tools and Context**: [ideal_ai_manager_hierarchy_system/tools_and_context_systems.md](../../layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_ai_manager_hierarchy_system/layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md)
- **Parallel Execution**: [ideal_ai_manager_hierarchy_system/parallel_execution.md](../../layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_ai_manager_hierarchy_system/layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md)
- **Supervisor Patterns**: [ideal_ai_manager_hierarchy_system/supervisor_patterns.md](../../layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_ai_manager_hierarchy_system/layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md)
- **Handoff Schema**: [../layer_0_02_manager_handoff_documents/layer_0_00_to_universal/handoff_schema.md](../layer_0_02_manager_handoff_documents/layer_0_00_to_universal/handoff_schema.md)

## Directory Structure

```
layer_0/
├── layer_0_01_ai_manager_system/
│   └── README.md (this file)
├── layer_0_02_manager_handoff_documents/
│   ├── layer_0_00_to_universal/
│   │   ├── incoming.json       # External requests
│   │   ├── outgoing.json       # Results back to external
│   │   └── handoff_schema.md   # Canonical schema definition
│   └── layer_0_01_to_specific/
│       ├── incoming.json       # Results from Layer 1
│       └── outgoing.json       # Tasks to Layer 1
├── layer_0_03_sub_layers/
│   └── (Universal sub-systems: rules, tools, protocols, etc.)
└── layer_0_99_stages/
    ├── stage_0_01_request_gathering/
    ├── stage_0_02_research/
    ├── stage_0_03_instructions/
    ├── stage_0_04_planning/
    ├── stage_0_05_design/
    ├── stage_0_06_development/
    ├── stage_0_07_testing/
    ├── stage_0_08_criticism/
    ├── stage_0_09_fixing/
    ├── stage_0_10_current_product/
    └── stage_0_11_archives/
```

## Best Practices

1. **Keep Universal Rules Minimal**: Only include constraints that truly apply everywhere
2. **Document Rationale**: Explain why universal rules exist so lower layers understand intent
3. **Enable Override Mechanisms**: Allow lower layers to request exceptions with justification
4. **Aggregate Learnings**: Capture patterns from lower layers that should become universal rules
5. **Version Universal Standards**: Track changes to universal rules and communicate updates

## Related Documentation

- Layer 0 Context Files: See `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` in this directory and sub-layers
- Universal Rules: `layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/`
- Universal Protocols: `layer_0/layer_0_03_sub_layers/sub_layer_0_05+_setup_dependant/sub_layer_0_05_operating_systems/_shared/sub_layer_0_06_environments/_shared/sub_layer_0_07_coding_apps/_shared/sub_layer_0_09_ai_apps/_shared/sub_layer_0_13_protocols/`
