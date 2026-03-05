---
resource_id: "bf6bc508-3329-49d5-9838-78a07335cde4"
resource_type: "readme
document"
resource_name: "README"
---
# Layer 3 (Component) AI Manager System

## Overview

This directory contains the AI manager system for **Layer 3 - Components**, which manages concrete implementation units within a feature. Layer 3 is where abstract requirements become actual code, files, modules, UI components, and other tangible artifacts. Components at this layer are the primary execution points where most coding work happens.

## Manager/Worker Roles at Layer 3

### Manager Responsibilities

The **Layer 3 Manager** is responsible for:

1. **Component-Level Coordination**: Orchestrates implementation of a single component (or optionally sub-components at Layer 4)
2. **Context Inheritance**: Applies Layer 0 + Layer 1 + Layer 2 constraints plus component-specific details:
   - Component interface and contract specifications
   - Specific implementation requirements (algorithms, libraries, patterns)
   - Component-level performance and quality requirements
   - Testing expectations for this component
3. **Sub-Component Decomposition** (optional): For complex components, may break into Layer 4 sub-components:
   - UI elements (form, validation, display)
   - Logic modules (business rules, calculations)
   - Type definitions
   - Test suites
4. **Component Quality Assurance**: Ensures the component meets all acceptance criteria
5. **Upward Reporting**: Reports component completion and results to Layer 2

### Worker Characteristics

Layer 3 is the **primary worker layer** where most execution happens. Workers handle:
- **Code implementation**: Writing actual TypeScript, Python, etc.
- **Test creation**: Unit tests and component tests
- **Documentation**: Component-level docs and inline comments
- **Small refactors**: Focused improvements within component scope

Most Layer 3 work is done by **workers**, not managers, since components are often leaf nodes that don't need further decomposition.

### Tool Recommendations

Based on the ideal hierarchy system:

- **Managers** (when decomposing to Layer 4): **Claude Code**
  - For complex components that need sub-component coordination
- **Workers** (most common at Layer 3): **Codex CLI** (primary) or **Claude Code**
  - **Codex CLI** for focused implementation tasks (1-3 turns):
    - Implement a single component
    - Write unit tests for a component
    - Add a small feature to existing component
  - **Claude Code** for complex components:
    - Multi-file components with intricate logic
    - Components requiring deep reasoning about edge cases
    - Critical components where correctness is paramount

## Handoff Consumption and Production

### Incoming Handoffs (Upstream from Layer 2)

Layer 3 receives handoffs from Layer 2 feature managers:
- **Location**: `layer_3_components/3.01_manager_handoff_documents/3.00_to_features/incoming.json`
- **Content**:
  - Component-level implementation tasks
  - All Layer 0 + Layer 1 + Layer 2 constraints
  - Feature context (data models, APIs, interfaces)
  - Component acceptance criteria

**Example**: Layer 2 requests implementation of login form component
```json
{
  "schemaVersion": "1.0.0",
  "id": "l2-to-l3-login-component-20241223",
  "kind": "vertical",
  "layer": 2,
  "from": "layer_2/features/auth-system/planning",
  "to": "layer_3/components/login-form/implementation",
  "task": "Implement login form component with email/password validation",
  "constraints": [
    "All Layer 0 + Layer 1 + Layer 2 constraints apply",
    "Use React Hook Form for form management",
    "Validate email format and password strength client-side",
    "Display clear error messages",
    "Support OAuth and email/password flows",
    "Match design system styling"
  ],
  "artifacts": {
    "files": [
      "src/features/auth/types.ts",
      "src/features/auth/api.ts",
      "src/design-system/components/*"
    ]
  },
  "acceptanceCriteria": [
    "Form renders with email and password fields",
    "Client-side validation works correctly",
    "Successful login redirects to dashboard",
    "Failed login shows error message",
    "OAuth buttons work",
    "Unit tests cover all validation logic",
    "Component is accessible (ARIA labels, keyboard nav)"
  ],
  "status": "pending"
}
```

### Outgoing Handoffs (Downstream to Layer 4)

If the component is complex enough to decompose, Layer 3 can produce handoffs for Layer 4:
- **Location**: `layer_3_components/3.01_manager_handoff_documents/3.01_to_subcomponents/outgoing/`
- **Content**:
  - Sub-component tasks (e.g., form UI, validation logic, API integration)
  - Full constraint stack (L0 + L1 + L2 + L3)
  - Sub-component interfaces and contracts

**Example**: Decomposing login form into sub-components
```json
{
  "schemaVersion": "1.0.0",
  "id": "l3-to-l4-login-form-ui-20241223",
  "kind": "vertical",
  "layer": 3,
  "from": "layer_3/components/login-form/planning",
  "to": "layer_4/subcomponents/login-form-ui/implementation",
  "task": "Implement login form UI elements (inputs, buttons, labels)",
  "constraints": [
    "All higher layer constraints apply",
    "Use design system Input and Button components",
    "ARIA labels for accessibility",
    "Responsive layout (mobile and desktop)"
  ],
  "acceptanceCriteria": [
    "Email input with proper type and autocomplete",
    "Password input with show/hide toggle",
    "Submit button with loading state",
    "OAuth buttons styled consistently",
    "Accessible to screen readers"
  ],
  "status": "pending"
}
```

### Horizontal Handoffs (Stage-to-Stage)

Within Layer 3, handoffs flow between stages:
- **Location**: Each stage's `hand_off_documents/outgoing.json` → next stage's `incoming.json`
- **Pipeline**: request → instructions → planning → design → implementation → testing → criticism → fixing → archiving

### Upward Handoffs (To Layer 2)

Layer 3 reports results back to Layer 2:
- **Location**: `layer_3_components/3.01_manager_handoff_documents/3.00_to_features/outgoing.json`
- **Content**:
  - Component completion status
  - Implementation details (files created, tests added)
  - Any issues or blockers encountered
  - Suggestions for feature-level improvements

**Example**: Component completion report
```json
{
  "schemaVersion": "1.0.0",
  "id": "l3-to-l2-login-complete-20241223",
  "kind": "vertical",
  "layer": 3,
  "from": "layer_3/components/login-form/archiving",
  "to": "layer_2/features/auth-system/testing",
  "task": "Login form component implementation complete",
  "status": "completed",
  "results": {
    "summary": "Implemented full-featured login form with validation and OAuth support",
    "filesCreated": [
      "src/components/LoginForm.tsx",
      "src/components/LoginForm.test.tsx",
      "src/hooks/useLogin.ts",
      "src/hooks/useLogin.test.ts"
    ],
    "filesModified": [
      "src/components/index.ts",
      "src/routes/auth.tsx"
    ],
    "testsAdded": [
      "Login form renders correctly",
      "Email validation works",
      "Password strength validation works",
      "Submit handler calls API correctly",
      "OAuth buttons trigger correct flow",
      "Error states display properly"
    ],
    "metrics": {
      "linesOfCode": 342,
      "testCoverage": 94.5,
      "duration": "3 hours"
    }
  },
  "nextActions": [
    "Integrate with registration form for consistent styling",
    "Add to Storybook for design review"
  ]
}
```

## Stage Pipeline

Layer 3 operates through the chronological pipeline (often abbreviated for simple components):

1. **stage_3.00_request_gathering**: Clarify component requirements (often quick)
2. **stage_3.01_instructions**: Add component-specific constraints
3. **stage_3.02_planning**: Decide implementation approach (or decompose to Layer 4)
4. **stage_3.03_design**: Define component interface and internal structure
5. **stage_3.04_development**: **Primary stage** - write the code
6. **stage_3.05_testing**: Write and run unit/component tests
7. **stage_3.06_criticism**: Review code quality and correctness
8. **stage_3.07_fixing**: Fix bugs and refactor
9. **stage_3.09_archives**: Document component and finalize

For simple components, stages 1-4 may be very brief, with most work in stages 5-7 (development, testing, fixing).

## Worker Workflow at Layer 3

### Typical Worker Workflow (Simple Component)

1. **Read Incoming Handoff**:
   - Located at `3.01_manager_handoff_documents/3.00_to_features/incoming.json`
   - Contains component task and full constraint stack

2. **Execute Implementation** (usually in a single session):
   - Create component file(s)
   - Write implementation code
   - Add unit tests
   - Run tests and verify they pass

3. **Write Results**:
   - Update handoff with:
     - Files created/modified
     - Tests added
     - Status (completed or issues encountered)
   - Write to `3.01_manager_handoff_documents/3.00_to_features/outgoing.json`

4. **Exit**: Return control to Layer 2 manager

### Manager Workflow (Complex Component → Layer 4)

Only when a component is complex enough to warrant decomposition:

1. **Read Incoming Handoff** from Layer 2
2. **Planning Stage**: Decide to decompose into sub-components:
   - Form UI elements
   - Validation logic
   - API integration
   - Type definitions
   - Test suite
3. **Spawn Layer 4 Workers**: Create handoffs for each sub-component
4. **Monitor and Aggregate**: Collect sub-component results
5. **Integration**: Assemble sub-components into final component
6. **Report to Layer 2**: Write completion handoff

## Parallel Execution at Layer 3

### When to Parallelize

Parallel execution at Layer 3 is beneficial when:
- Layer 2 has decomposed a feature into many independent components
- Multiple workers are available
- Components share no file dependencies

**Example**: Auth feature decomposed by Layer 2
```
Parallel Batch (all can run simultaneously):
  - login-form component
  - registration-form component
  - password-reset-form component
  - oauth-button component
  - session-indicator component
```

### Execution Pattern

Layer 2 manager spawns multiple Layer 3 workers:
```python
# Pseudo-code from Layer 2 manager

# Create component handoffs
component_handoffs = [
    create_handoff("login-form"),
    create_handoff("registration-form"),
    create_handoff("password-reset-form"),
    create_handoff("oauth-button"),
    create_handoff("session-indicator")
]

# Spawn workers in parallel
with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(spawn_layer3_worker, handoff)
        for handoff in component_handoffs
    ]

    # Collect results
    results = [f.result() for f in futures]

# Aggregate and continue to integration testing
```

## Tool Selection Strategy at Layer 3

### Use Codex CLI when:
- Component is straightforward (single file, clear requirements)
- Implementation is 1-3 turns of work
- Component follows established patterns
- Speed and cost efficiency matter

**Example**: Simple utility function, basic React component, standard API endpoint

### Use Claude Code when:
- Component is complex (multiple files, intricate logic)
- Deep reasoning required (security, edge cases, performance)
- Component is critical to system correctness
- Multi-turn debugging needed

**Example**: Complex state management, cryptographic functions, core business logic

## Deeper References

For comprehensive understanding of the manager/worker model, handoff protocol, and orchestration patterns, see:

- **Architecture**: [ideal_ai_manager_hierarchy_system/architecture.md](../../../code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md)
- **Tools and Context**: [ideal_ai_manager_hierarchy_system/tools_and_context_systems.md](../../../code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md)
- **Parallel Execution**: [ideal_ai_manager_hierarchy_system/parallel_execution.md](../../../code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md)
- **Supervisor Patterns**: [ideal_ai_manager_hierarchy_system/supervisor_patterns.md](../../../code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md)
- **Handoff Schema**: [../layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md](../../layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md)

## Directory Structure

```
layer_3_components/
├── 3.00_ai_manager_system/
│   └── README.md (this file)
├── 3.01_manager_handoff_documents/
│   ├── 3.00_to_features/
│   │   ├── incoming.json       # Tasks from Layer 2
│   │   └── outgoing.json       # Results to Layer 2
│   └── 3.01_to_subcomponents/  # Optional, for complex components
│       ├── incoming/            # Results from Layer 4
│       └── outgoing/            # Tasks to Layer 4
├── 3.02_sub_layers/
│   └── (Component-specific helpers or Layer 4 sub-components)
└── 3.99_stages/
    ├── stage_3.00_request_gathering/
    ├── stage_3.01_instructions/
    └── ... (full stage pipeline)
```

## Best Practices

1. **Keep Components Focused**: Single responsibility, well-defined interface
2. **Write Tests First or Alongside**: TDD or concurrent test development
3. **Document Public APIs**: Clear JSDoc/docstrings for all exported functions
4. **Follow Conventions**: Match established patterns in the codebase
5. **Short Sessions**: Keep worker sessions brief (1-3 turns) for best results with Codex
6. **Fresh Context**: Start new worker sessions for new components rather than long-running sessions
7. **Test Before Reporting**: Always run tests and verify they pass before marking complete
8. **Report Blockers Early**: If stuck, report to Layer 2 immediately rather than attempting workarounds

## Common Patterns

### Pattern 1: Simple React Component (Codex Worker)

**Session**: 1-2 turns
**Files**: Component file + test file
**Workflow**:
1. Create component skeleton
2. Implement logic and JSX
3. Add unit tests
4. Verify tests pass
5. Report completion

### Pattern 2: Complex Business Logic (Claude Code Worker)

**Session**: 2-4 turns
**Files**: Logic module + types + tests + docs
**Workflow**:
1. Design algorithm and edge cases
2. Implement with error handling
3. Write comprehensive tests
4. Review for correctness
5. Document behavior
6. Report completion

### Pattern 3: Multi-File Component (Layer 3 Manager → Layer 4 Workers)

**Components**: UI + logic + types + tests
**Workflow**:
1. Plan decomposition (Layer 3 manager)
2. Spawn sub-component workers in parallel:
   - UI elements (Codex)
   - Business logic (Claude Code)
   - Type definitions (Codex)
   - Tests (Codex or Claude Code)
3. Integrate sub-components (Layer 3 manager)
4. Run integration tests
5. Report completion to Layer 2
