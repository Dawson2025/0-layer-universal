# Layer 2 (Feature) AI Manager System

## Overview

This directory contains the AI manager system for **Layer 2 - Features**, which manages individual feature domains within a project. Layer 2 sits between project-level coordination (Layer 1) and concrete component implementation (Layer 3), ensuring that all components within a feature work together cohesively while respecting both universal and project-level constraints.

## Manager/Worker Roles at Layer 2

### Manager Responsibilities

The **Layer 2 Manager** is responsible for:

1. **Feature-Level Coordination**: Orchestrates all components and work within a single feature
2. **Context Inheritance**: Applies Layer 0 + Layer 1 constraints plus feature-specific rules:
   - Feature domain logic and business rules
   - Feature-specific data models and APIs
   - Inter-component contracts and interfaces
   - Feature-level security and performance requirements
3. **Component Decomposition**: Breaks down feature-level tasks into component-level work for Layer 3 managers/workers
4. **Intra-Feature Integration**: Ensures all components within the feature work together
5. **Feature Quality Assurance**: Validates that the complete feature meets acceptance criteria
6. **Upward Reporting**: Aggregates component results and reports feature status to Layer 1

### Worker Characteristics

Layer 2 workers handle:
- **Feature-wide utilities**: Shared helpers used across multiple components
- **Feature integration code**: Glue code connecting components
- **Feature documentation**: Feature-specific guides and API documentation
- **Feature testing**: Integration tests that span multiple components

### Tool Recommendations

Based on the ideal hierarchy system:

- **Managers**: **Claude Code** (primary) or **Gemini CLI**
  - Claude Code for feature-wide reasoning and multi-component coordination
  - Gemini CLI for complex planning with many components
- **Workers**:
  - **Claude Code** for multi-component integration tasks
  - **Codex CLI** for single-file utilities or focused documentation

## Handoff Consumption and Production

### Incoming Handoffs (Upstream from Layer 1)

Layer 2 receives handoffs from Layer 1 project managers:
- **Location**: `layer_2_features/2.01_manager_handoff_documents/2.00_to_project/incoming.json`
- **Content**:
  - Feature-level goals and requirements
  - All Layer 0 + Layer 1 constraints
  - Project context (architecture, integrations, domain)
  - Feature acceptance criteria

**Example**: Layer 1 requests implementation of authentication feature
```json
{
  "schemaVersion": "1.0.0",
  "id": "l1-to-l2-auth-feature-20241223",
  "kind": "vertical",
  "layer": 1,
  "from": "layer_1/projects/ecommerce/planning",
  "to": "layer_2/features/auth-system/request",
  "task": "Implement authentication and authorization system",
  "constraints": [
    "All Layer 0 universal constraints apply",
    "All Layer 1 project constraints (GDPR, payment security)",
    "Support OAuth 2.0 (Google, GitHub) and email/password",
    "JWT-based session management",
    "Role-based access control (customer, admin)",
    "Integration with user database schema"
  ],
  "acceptanceCriteria": [
    "Users can register, login, reset passwords",
    "OAuth integration working",
    "Admin access properly restricted",
    "Rate limiting on all auth endpoints",
    "GDPR-compliant data handling"
  ],
  "status": "pending"
}
```

### Outgoing Handoffs (Downstream to Layer 3)

Layer 2 produces handoffs for Layer 3 component managers/workers:
- **Location**: `layer_2_features/2.01_manager_handoff_documents/2.01_to_components/outgoing/`
- **Content**:
  - Component-level tasks decomposed from feature goals
  - Layer 0 + Layer 1 + Layer 2 constraints combined
  - Feature-specific context (data models, APIs, component contracts)
  - Component acceptance criteria aligned with feature goals

**Example**: Layer 2 decomposes auth feature to login component
```json
{
  "schemaVersion": "1.0.0",
  "id": "l2-to-l3-login-component-20241223",
  "kind": "vertical",
  "layer": 2,
  "from": "layer_2/features/auth-system/planning",
  "to": "layer_3/components/login-form/implementation",
  "task": "Implement login form component with validation",
  "constraints": [
    "All Layer 0 + Layer 1 + Layer 2 constraints apply",
    "Use React Hook Form for form management",
    "Validate email format and password strength client-side",
    "Display clear error messages for invalid inputs",
    "Support both OAuth and email/password flows",
    "Integrate with auth API endpoints defined in feature spec"
  ],
  "artifacts": {
    "files": ["src/features/auth/types.ts", "src/features/auth/api.ts"],
    "urls": ["https://docs.project.com/auth-api"]
  },
  "acceptanceCriteria": [
    "Form renders correctly with email and password fields",
    "Client-side validation prevents invalid submissions",
    "Successful login redirects to dashboard",
    "Failed login shows appropriate error message",
    "OAuth buttons trigger correct flow",
    "Unit tests cover all validation logic"
  ],
  "status": "pending"
}
```

### Horizontal Handoffs (Stage-to-Stage)

Within Layer 2, handoffs flow between stages:
- **Location**: Each stage's `hand_off_documents/outgoing.json` → next stage's `incoming.json`
- **Pipeline**: request → instructions → planning → design → implementation → testing → criticism → fixing → archiving

### Upward Handoffs (To Layer 1)

Layer 2 reports results back to Layer 1:
- **Location**: `layer_2_features/2.01_manager_handoff_documents/2.00_to_project/outgoing.json`
- **Content**:
  - Feature completion status
  - Aggregated metrics from all components
  - Integration test results
  - Recommendations for project-level improvements

**Example**: Feature completion report
```json
{
  "schemaVersion": "1.0.0",
  "id": "l2-to-l1-auth-complete-20241223",
  "kind": "vertical",
  "layer": 2,
  "from": "layer_2/features/auth-system/archiving",
  "to": "layer_1/projects/ecommerce/archiving",
  "task": "Authentication feature implementation complete",
  "status": "completed",
  "results": {
    "summary": "Successfully implemented complete auth system with 6 components",
    "componentsCompleted": [
      "login-form",
      "registration-form",
      "password-reset-flow",
      "oauth-integration",
      "session-management",
      "auth-api-handlers"
    ],
    "filesCreated": 23,
    "testsAdded": 47,
    "metrics": {
      "testCoverage": 91.2,
      "duration": "4 days",
      "linesOfCode": 2847
    }
  },
  "nextActions": [
    "Integrate auth with other features (cart, checkout)",
    "Add auth to admin panel",
    "Consider 2FA as future enhancement"
  ]
}
```

## Stage Pipeline

Layer 2 operates through the chronological pipeline:

1. **stage_2.00_request_gathering**: Clarify feature requirements
2. **stage_2.01_instructions**: Add feature-specific constraints
3. **stage_2.02_planning**: Decompose into components and integration work
4. **stage_2.03_design**: Define feature architecture, data models, component interfaces
5. **stage_2.04_development**: Implement feature-wide infrastructure and glue code
6. **stage_2.05_testing**: Integration testing across all components
7. **stage_2.06_criticism**: Review against feature goals
8. **stage_2.07_fixing**: Resolve integration issues
9. **stage_2.08_archives**: Document feature architecture and decisions

## Manager/Worker Workflow at Layer 2

### Manager Workflow

1. **Read Incoming Handoff** from Layer 1:
   - Located at `2.01_manager_handoff_documents/2.00_to_project/incoming.json`
   - Contains feature-level goals and project + universal constraints

2. **Process Through Stages**:
   - Run request → instructions → planning stages
   - Enrich with feature-specific context (data models, APIs, contracts)
   - Decompose feature into components during planning

3. **Spawn Component Workers** (Layer 3):
   - Create handoff for each component
   - Write to `2.01_manager_handoff_documents/2.01_to_components/outgoing/component-*.json`
   - Identify independent components for parallel execution

4. **Monitor Component Progress**:
   - Watch for Layer 3 component handoffs
   - Collect results from `2.01_manager_handoff_documents/2.01_to_components/incoming/component-*.json`

5. **Integration and Aggregation**:
   - Run integration tests across all components
   - Execute criticism and fixing stages
   - Aggregate results and write to `2.01_manager_handoff_documents/2.00_to_project/outgoing.json`

### Worker Workflow (Feature-Wide Tasks)

1. **Read Task Handoff**: Receive specific feature-wide task (e.g., create shared types)
2. **Execute Bounded Work**: Perform 1-3 focused actions
3. **Write Results**: Update handoff with created artifacts
4. **Exit**: Return control to manager

## Parallel Execution at Layer 2

Layer 2 is the **primary parallelization layer** where significant speedup occurs:

### Decomposition Strategy

During the planning stage, identify:
- **Independent Components**: Can be developed in parallel (e.g., login form, registration form, password reset)
- **Shared Dependencies**: Must be created first (e.g., auth types, API client)
- **Integration Components**: Must run after all independents complete (e.g., integration tests)

### Execution Pattern

```
Batch 0 (sequential - dependencies):
  - auth-types
  - auth-api-client

Batch 1 (parallel - independent components):
  - login-form
  - registration-form
  - password-reset-flow
  - oauth-integration

Batch 2 (sequential - integration):
  - session-management (uses results from Batch 1)
  - integration-tests
```

### Example: Auth Feature Parallelization

```python
# Pseudo-code for Layer 2 manager

# Planning stage output
components = {
    "auth-types": {"dependencies": []},
    "auth-api": {"dependencies": ["auth-types"]},
    "login-form": {"dependencies": ["auth-types", "auth-api"]},
    "register-form": {"dependencies": ["auth-types", "auth-api"]},
    "reset-flow": {"dependencies": ["auth-types", "auth-api"]},
    "oauth": {"dependencies": ["auth-types", "auth-api"]},
    "integration-tests": {"dependencies": ["login-form", "register-form", "reset-flow", "oauth"]}
}

# Build dependency graph and get parallel batches
batches = get_parallel_batches(components)

# Execute batches sequentially, components within batch in parallel
for batch in batches:
    # Spawn all components in batch concurrently
    results = execute_parallel_batch(batch, layer=3, stage="implementation")

    # Check for failures before continuing
    if too_many_failures(results):
        escalate_to_layer_1()
        break
```

## Deeper References

For comprehensive understanding of the manager/worker model, handoff protocol, and orchestration patterns, see:

- **Architecture**: [ideal_ai_manager_hierarchy_system/architecture.md](../../../code/0_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md)
- **Tools and Context**: [ideal_ai_manager_hierarchy_system/tools_and_context_systems.md](../../../code/0_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md)
- **Parallel Execution**: [ideal_ai_manager_hierarchy_system/parallel_execution.md](../../../code/0_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md)
- **Supervisor Patterns**: [ideal_ai_manager_hierarchy_system/supervisor_patterns.md](../../../code/0_ai_context/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md)
- **Handoff Schema**: [../layer_0_universal/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md](../../layer_0_universal/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md)

## Directory Structure

```
layer_2_features/
├── 2.00_ai_manager_system/
│   └── README.md (this file)
├── 2.01_manager_handoff_documents/
│   ├── 2.00_to_project/
│   │   ├── incoming.json       # Tasks from Layer 1
│   │   └── outgoing.json       # Results to Layer 1
│   └── 2.01_to_components/
│       ├── incoming/            # Results from Layer 3 components
│       │   ├── component-login.json
│       │   └── component-*.json
│       └── outgoing/            # Tasks to Layer 3 components
│           ├── component-login.json
│           └── component-*.json
├── 2.02_sub_layers/
│   └── (Feature-specific sub-features or utilities)
└── 2.99_stages/
    ├── stage_2.00_request_gathering/
    ├── stage_2.01_instructions/
    └── ... (full stage pipeline)
```

## Best Practices

1. **Clear Component Boundaries**: Define clean interfaces between components
2. **Minimize Dependencies**: Design components to be as independent as possible
3. **Shared Code First**: Create shared types, utilities, and APIs before components
4. **Integration Testing**: Always test integrated feature, not just individual components
5. **Document Contracts**: Clearly specify component interfaces and data flows
6. **Monitor Parallelism**: Track which components can be built concurrently
7. **Feature Flags**: Use feature flags to deploy incomplete features safely
