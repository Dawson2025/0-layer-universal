---
resource_id: "0e600d28-7553-4a85-830f-ffccf9115798"
resource_type: "readme
document"
resource_name: "README"
---
# Layer 1 (Project) AI Manager System

<!-- section_id: "7afc5a0a-db07-4d89-8dae-bfdb04e4de76" -->
## Overview

This directory contains the AI manager system for **Layer 1 - Project**, which manages project-specific work and constraints. Layer 1 sits between universal rules (Layer 0) and feature-specific implementation (Layer 2), ensuring that all features within a project align with project-level architecture, domain requirements, and business rules.

<!-- section_id: "d612610d-1ef2-45b6-ae5c-6a07c135ee96" -->
## Manager/Worker Roles at Layer 1

<!-- section_id: "c34607df-4ef1-45de-b24e-c11f77a354fe" -->
### Manager Responsibilities

The **Layer 1 Manager** is responsible for:

1. **Project-Level Coordination**: Orchestrates all features and work within a single project
2. **Context Inheritance**: Applies all Layer 0 universal constraints plus project-specific rules:
   - Project domain and business logic
   - Tech stack and architecture patterns
   - Project-specific security/compliance requirements (e.g., GDPR, HIPAA)
   - Integration points with external systems
3. **Feature Decomposition**: Breaks down project-level tasks into feature-level work for Layer 2 managers
4. **Cross-Feature Integration**: Ensures features work together cohesively
5. **Project-Wide Quality Assurance**: Validates that all features meet project-level acceptance criteria
6. **Upward Reporting**: Aggregates feature results and reports status to Layer 0

<!-- section_id: "018731a2-3c23-4f64-9105-75dca0b61c42" -->
### Worker Characteristics

Layer 1 workers handle:
- **Project-wide refactors**: Changes that span multiple features
- **Integration tasks**: Connecting features or external systems
- **Project documentation**: README, architecture docs, deployment guides
- **Cross-cutting concerns**: Logging, monitoring, error handling patterns

<!-- section_id: "3c2bb000-3650-428a-91d2-6ed5a8ca2565" -->
### Tool Recommendations

Based on the ideal hierarchy system:

- **Managers**: **Claude Code** (primary) or **Gemini CLI**
  - Claude Code for project-wide reasoning and multi-feature coordination
  - Gemini CLI for long planning sessions and requirements gathering
- **Workers**:
  - **Claude Code** for complex cross-feature refactors
  - **Codex CLI** for focused project documentation updates

<!-- section_id: "11eae1bf-854b-498a-a92a-df6f84356d97" -->
## Handoff Consumption and Production

<!-- section_id: "17bc4e1f-e990-4967-b8f5-2cbbcdb7d01c" -->
### Incoming Handoffs (Upstream from Layer 0)

Layer 1 receives handoffs from Layer 0:
- **Location**: `layer_1_project/1.01_manager_handoff_documents/1.00_to_universal/incoming.json`
- **Content**:
  - Project-level goals and requirements
  - All Layer 0 universal constraints
  - High-level acceptance criteria
  - References to universal standards

**Example**: Layer 0 requests implementation of an e-commerce platform
```json
{
  "schemaVersion": "1.0.0",
  "id": "l0-to-l1-ecommerce-platform-20241223",
  "kind": "vertical",
  "layer": 0,
  "from": "layer_0/planning",
  "to": "layer_1/projects/ecommerce/request",
  "task": "Build complete e-commerce platform with payment processing",
  "constraints": [
    "All Layer 0 universal constraints apply",
    "TypeScript strict mode",
    "Comprehensive testing and documentation",
    "Security-first design"
  ],
  "acceptanceCriteria": [
    "Users can browse products and make purchases",
    "Secure payment processing via Stripe",
    "Admin panel for inventory management",
    "All components tested and documented"
  ],
  "status": "pending"
}
```

<!-- section_id: "2f761f21-da81-4644-a991-55149ab09f16" -->
### Outgoing Handoffs (Downstream to Layer 2)

Layer 1 produces handoffs for Layer 2 feature managers:
- **Location**: `layer_1_project/1.01_manager_handoff_documents/1.01_to_features/outgoing.json`
- **Content**:
  - Feature-level tasks decomposed from project goals
  - Layer 0 + Layer 1 constraints combined
  - Project-specific context (architecture, domain rules, integrations)
  - Feature acceptance criteria aligned with project goals

**Example**: Layer 1 decomposes to authentication feature
```json
{
  "schemaVersion": "1.0.0",
  "id": "l1-to-l2-auth-feature-20241223",
  "kind": "vertical",
  "layer": 1,
  "from": "layer_1/projects/ecommerce/planning",
  "to": "layer_2/features/auth-system/request",
  "task": "Implement authentication and authorization system for e-commerce platform",
  "constraints": [
    "All Layer 0 universal constraints apply",
    "All Layer 1 project constraints (GDPR compliance, payment security)",
    "Support OAuth 2.0 (Google, GitHub) and email/password",
    "JWT-based session management",
    "Role-based access control (customer, admin, super-admin)",
    "Integration with existing user database schema"
  ],
  "artifacts": {
    "urls": ["https://docs.project.com/database-schema"],
    "files": ["src/db/schema.sql"]
  },
  "acceptanceCriteria": [
    "Users can register, login, and reset passwords",
    "OAuth integration working with Google and GitHub",
    "Admin panel accessible only to admin roles",
    "All auth endpoints have rate limiting",
    "GDPR-compliant user data handling"
  ],
  "status": "pending"
}
```

<!-- section_id: "d80a0441-cd3a-46c5-91dd-866e5b6d7308" -->
### Horizontal Handoffs (Stage-to-Stage)

Within Layer 1, handoffs flow between stages:
- **Location**: Each stage's `hand_off_documents/outgoing.json` → next stage's `incoming.json`
- **Pipeline**: request → instructions → planning → design → implementation → testing → criticism → fixing → archiving

<!-- section_id: "30f52997-eb0b-40af-aaf0-db694be72274" -->
### Upward Handoffs (To Layer 0)

Layer 1 reports results back to Layer 0:
- **Location**: `layer_1_project/1.01_manager_handoff_documents/1.00_to_universal/outgoing.json`
- **Content**:
  - Project completion status
  - Aggregated metrics from all features
  - Discovered issues or improvements
  - Recommendations for universal rule updates

**Example**: Project completion report
```json
{
  "schemaVersion": "1.0.0",
  "id": "l1-to-l0-ecommerce-complete-20241223",
  "kind": "vertical",
  "layer": 1,
  "from": "layer_1/projects/ecommerce/archiving",
  "to": "layer_0/archiving",
  "task": "E-commerce platform implementation complete",
  "status": "completed",
  "results": {
    "summary": "Successfully implemented e-commerce platform with 5 core features",
    "featuresCompleted": ["auth-system", "product-catalog", "shopping-cart", "checkout", "admin-panel"],
    "metrics": {
      "totalDuration": "3 weeks",
      "testCoverage": 89.5,
      "linesOfCode": 15234,
      "componentsBuilt": 47
    }
  },
  "nextActions": [
    "Consider adding universal rule for payment security patterns",
    "Update universal TypeScript config based on lessons learned",
    "Add GDPR compliance checklist to universal protocols"
  ]
}
```

<!-- section_id: "6aa7b5c7-ed55-469a-93df-8a2b8da22f2b" -->
## Stage Pipeline

Layer 1 operates through the same chronological pipeline as all layers:

1. **stage_1.00_request_gathering**: Clarify project-level requirements
2. **stage_1.01_instructions**: Add project-specific constraints and context
3. **stage_1.02_planning**: Decompose into features and cross-feature work
4. **stage_1.03_design**: Define project architecture, data models, APIs
5. **stage_1.04_development**: Implement project-wide infrastructure
6. **stage_1.05_testing**: Integration and end-to-end testing across features
7. **stage_1.06_criticism**: Review against project goals and quality standards
8. **stage_1.07_fixing**: Resolve cross-feature issues and refactor
9. **stage_1.09_archives**: Document project decisions and final state

<!-- section_id: "9240f5e0-d073-4fce-b1d1-a63ceac6637a" -->
## Manager/Worker Workflow at Layer 1

<!-- section_id: "beceba89-9491-4e24-850e-52b112211d25" -->
### Manager Workflow

1. **Read Incoming Handoff** from Layer 0:
   - Located at `1.01_manager_handoff_documents/1.00_to_universal/incoming.json`
   - Contains project-level goals and universal constraints

2. **Process Through Stages**:
   - Run request → instructions → planning stages
   - Enrich with project-specific context at each stage
   - Decompose project into features during planning

3. **Spawn Feature Workers** (Layer 2 managers):
   - Create handoff for each feature
   - Write to `1.01_manager_handoff_documents/1.01_to_features/outgoing/feature-*.json`
   - May spawn features in parallel if they're independent

4. **Monitor Feature Progress**:
   - Watch for completion of Layer 2 feature handoffs
   - Collect results from `1.01_manager_handoff_documents/1.01_to_features/incoming/feature-*.json`

5. **Aggregate and Report**:
   - Run testing → criticism → fixing stages on integrated system
   - Aggregate all feature results
   - Write final report to `1.01_manager_handoff_documents/1.00_to_universal/outgoing.json`

<!-- section_id: "b55f4bbc-e746-4c29-9c08-1f8190c93a20" -->
### Worker Workflow (Cross-Feature Tasks)

1. **Read Task Handoff**: Receive specific cross-feature task
2. **Execute Bounded Work**: Perform 1-3 focused actions
3. **Write Results**: Update handoff with status and artifacts
4. **Exit**: Return control to manager

<!-- section_id: "6dcbcd3b-2954-4d98-9e7d-41678dc7e0e2" -->
## Parallel Execution at Layer 1

Layer 1 managers can parallelize work by:

1. **Identifying Independent Features**: During planning, determine which features have no dependencies
2. **Creating Parallel Handoffs**: Generate one handoff per independent feature
3. **Spawning Concurrent Layer 2 Managers**: Launch multiple feature managers simultaneously
4. **Barrier Synchronization**: Wait for all features to complete before integration testing
5. **Aggregating Results**: Combine all feature outputs into project-level result

**Example**: E-commerce platform with 5 independent features
```
Batch 1 (parallel):
  - auth-system
  - product-catalog
  - shopping-cart
  - payment-processing

Batch 2 (after Batch 1):
  - admin-panel (depends on auth-system)

Batch 3 (after all features):
  - integration-tests
```

<!-- section_id: "0e96b699-ffa6-46fc-b56e-4179c596082b" -->
## Deeper References

For comprehensive understanding of the manager/worker model, handoff protocol, and orchestration patterns, see:

- **Architecture**: [ideal_ai_manager_hierarchy_system/architecture.md](../../../code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md)
- **Tools and Context**: [ideal_ai_manager_hierarchy_system/tools_and_context_systems.md](../../../code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md)
- **Parallel Execution**: [ideal_ai_manager_hierarchy_system/parallel_execution.md](../../../code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md)
- **Supervisor Patterns**: [ideal_ai_manager_hierarchy_system/supervisor_patterns.md](../../../code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md)
- **Handoff Schema**: [../layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md](../../layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md)

<!-- section_id: "c89c32cb-3ae7-4fc9-b509-8862ced0246f" -->
## Directory Structure

```
layer_1_project/
├── 1.00_ai_manager_system/
│   └── README.md (this file)
├── 1.01_manager_handoff_documents/
│   ├── 1.00_to_universal/
│   │   ├── incoming.json       # Tasks from Layer 0
│   │   └── outgoing.json       # Results to Layer 0
│   └── 1.01_to_features/
│       ├── incoming/            # Results from Layer 2 features
│       │   ├── feature-auth.json
│       │   └── feature-*.json
│       └── outgoing/            # Tasks to Layer 2 features
│           ├── feature-auth.json
│           └── feature-*.json
├── 1.02_sub_layers/
│   └── (Project-specific infrastructure, shared utilities)
└── 1.99_stages/
    ├── stage_1.00_request_gathering/
    ├── stage_1.01_instructions/
    └── ... (full stage pipeline)
```

<!-- section_id: "3720249c-25f3-40b3-9664-2d870af901bb" -->
## Best Practices

1. **Clear Project Scope**: Define what belongs in this project vs. other projects or universal layer
2. **Consistent Architecture**: Establish and enforce project-wide architectural patterns
3. **Feature Independence**: Design features to minimize inter-dependencies for parallelism
4. **Integration Testing**: Always test integrated system, not just individual features
5. **Document Decisions**: Capture architectural decisions and trade-offs for future reference
6. **Bubble Up Learnings**: Report patterns to Layer 0 that could become universal rules
