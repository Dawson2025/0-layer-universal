---
resource_id: "44f1d7ca-d828-408e-bf33-8c5f5dfa92da"
resource_type: "readme_document"
resource_name: "README"
---
# Layer 0 (Universal) AI Manager System

<!-- section_id: "54a98001-4f0f-4920-acde-553f45ab07b8" -->
## Overview

This directory contains the AI manager system for **Layer 0 - Universal**, the highest level of abstraction in the AI Manager Hierarchy System. Layer 0 defines global rules, constraints, and workflows that apply to all work across all projects, features, and components.

<!-- section_id: "055c32d8-8faf-4fe8-9f7d-2eb5fbae5304" -->
## Manager/Worker Roles at Layer 0

<!-- section_id: "4d238642-7fd9-4655-a500-af89e691c70a" -->
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

<!-- section_id: "c1da5a8f-8ebc-4866-aec3-9f85ccea4859" -->
### Worker Characteristics

At Layer 0, workers are typically:
- **Research agents**: Gathering context about universal standards or new technologies
- **Policy reviewers**: Ensuring compliance with universal rules
- **Documentation generators**: Creating or updating universal documentation

Layer 0 workers are less common than Layer 0 managers, as most execution happens at lower layers.

<!-- section_id: "33723f01-28d4-4a33-aee8-2d47d3952560" -->
### Tool Recommendations

Based on the ideal hierarchy system:

- **Managers**: **Claude Code** or **Gemini CLI**
  - Claude Code for deep reasoning and multi-file context
  - Gemini CLI for long research and planning sessions
- **Workers**: **Claude Code** for complex analysis tasks
  - **Codex CLI** for simple universal documentation updates

<!-- section_id: "49dbabd1-3303-4dee-90db-ab57b6635556" -->
## Handoff Consumption and Production

<!-- section_id: "9d964bd3-7714-474f-b8ac-89889d1e700b" -->
### Incoming Handoffs (Upstream)

Layer 0 receives handoffs from:
- **External Users**: Initial requests via `stage_0_01_request_gathering`
- **System Triggers**: Automated tasks (e.g., scheduled audits, dependency updates)

**Location**: `layer_0/layer_0_99_stages/stage_0_01_request_gathering/hand_off_documents/incoming.json`

**Characteristics**:
- May be informal or unstructured initially
- Converted to structured handoffs during request gathering stage
- Contain high-level goals without implementation details

<!-- section_id: "a0f1f6f1-6cf1-45bb-bc1f-d9f9174de522" -->
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

<!-- section_id: "0d8921b7-c7d4-4da2-8524-1653c26ee7ab" -->
### Upward Handoffs (From Layer 1)

Layer 0 receives result handoffs from Layer 1:
- **Location**: `layer_0/layer_0_02_manager_handoff_documents/layer_0_01_to_specific/incoming.json`
- **Content**:
  - Aggregated results from all project-level work
  - Metrics and outcomes
  - Discovered issues or improvements to universal rules
  - Recommendations for universal documentation updates

<!-- section_id: "87e55722-d3df-4a38-bf83-6d71976f38a9" -->
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

<!-- section_id: "f915be67-4290-4577-aabf-8515fc17e737" -->
## Handoff Flow Example

<!-- section_id: "7e5b98e0-2173-4d2b-99e1-2db72f2c887e" -->
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

<!-- section_id: "376561bf-bcbd-4e5a-9656-c82d2f84047e" -->
## Deeper References

For comprehensive understanding of the manager/worker model, handoff protocol, and orchestration patterns, see:

- **Architecture**: [ideal_ai_manager_hierarchy_system/architecture.md](../../layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_ai_manager_hierarchy_system/layer_0/layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md)
- **Tools and Context**: [ideal_ai_manager_hierarchy_system/tools_and_context_systems.md](../../layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_ai_manager_hierarchy_system/layer_0/layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md)
- **Parallel Execution**: [ideal_ai_manager_hierarchy_system/parallel_execution.md](../../layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_ai_manager_hierarchy_system/layer_0/layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md)
- **Supervisor Patterns**: [ideal_ai_manager_hierarchy_system/supervisor_patterns.md](../../layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_ai_manager_hierarchy_system/layer_0/layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md)
- **Handoff Schema**: [../layer_0_02_manager_handoff_documents/layer_0_00_to_universal/handoff_schema.md](../layer_0_02_manager_handoff_documents/layer_0_00_to_universal/handoff_schema.md)

<!-- section_id: "8e265508-eea7-4a1f-a0ad-767aaa1675ca" -->
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
├── layer_0_04_sub_layers/
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

<!-- section_id: "4f3a9374-8480-4ca5-90f0-2a4e29db69bc" -->
## Best Practices

1. **Keep Universal Rules Minimal**: Only include constraints that truly apply everywhere
2. **Document Rationale**: Explain why universal rules exist so lower layers understand intent
3. **Enable Override Mechanisms**: Allow lower layers to request exceptions with justification
4. **Aggregate Learnings**: Capture patterns from lower layers that should become universal rules
5. **Version Universal Standards**: Track changes to universal rules and communicate updates

<!-- section_id: "5dc430fe-7198-4913-9b82-569812bd57e9" -->
## Related Documentation

- Layer 0 Context Files: See `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` in this directory and sub-layers
- Universal Rules: `layer_0/layer_0_04_sub_layers/sub_layer_0_02_rules/`
- Universal Protocols: `layer_0/layer_0_04_sub_layers/sub_layer_0_05+_setup_dependant/sub_layer_0_05_operating_systems/_shared/sub_layer_0_06_environments/_shared/sub_layer_0_07_coding_apps/_shared/sub_layer_0_09_ai_apps/_shared/sub_layer_0_13_protocols/`
