---
resource_id: "1e7ba6f4-3fd9-42d3-9aa7-ae2da23b512a"
resource_type: "readme_document"
resource_name: "README"
---
# Layer 3 Component Manager Handoff Documents

<!-- section_id: "949d22ec-9d19-4672-8b5d-2cd1a3e9bfd5" -->
## Overview

This directory contains handoff documents for **Layer 3 (Components)** managers and workers. Layer 3 is where concrete implementation happens, so handoffs here are typically between Layer 2 feature managers and Layer 3 workers executing component tasks.

<!-- section_id: "42eea977-6daa-446a-8a2d-5e9bba7ba182" -->
## Purpose

Manager handoff documents at Layer 3 serve:

1. **Upward Communication** (`3.00_to_features/`): Handoffs between Layer 3 and Layer 2 (Features)
2. **Downward Communication** (`3.01_to_subcomponents/`): Optional handoffs for complex components decomposed to Layer 4

<!-- section_id: "1882538c-ff35-44c9-9ea9-f75db525cd61" -->
## Directory Structure

```
3.01_manager_handoff_documents/
├── README.md (this file)
├── 3.00_to_features/
│   ├── incoming.json          # Tasks from Layer 2
│   └── outgoing.json          # Results to Layer 2
└── 3.01_to_subcomponents/     # Optional: for complex components
    ├── incoming/              # Results from Layer 4 sub-components
    │   ├── subcomp-ui.json
    │   ├── subcomp-logic.json
    │   └── subcomp-*.json
    └── outgoing/              # Tasks to Layer 4 sub-components
        ├── subcomp-ui.json
        ├── subcomp-logic.json
        └── subcomp-*.json
```

<!-- section_id: "6c895b5c-8350-4480-9842-f7e8cbf88275" -->
## Handoff Schema

All handoffs must conform to the **canonical handoff schema** defined in:

**[../../layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md](../../layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md)**

**Always consult the schema document when creating or reading handoffs.**

<!-- section_id: "e333bbd4-d8d7-4a11-b112-347ad8cc3682" -->
## Handoff Flows at Layer 3

<!-- section_id: "5b055c69-07d6-475c-8957-52812b9775c2" -->
### Layer 2 → Layer 3 (Incoming from Feature)

**File**: `3.00_to_features/incoming.json`

**Content**: Component implementation task with full constraint stack

**Example**:
```json
{
  "schemaVersion": "1.0.0",
  "id": "l2-to-l3-login-20241223",
  "kind": "vertical",
  "layer": 2,
  "from": "layer_2/features/auth-system/planning",
  "to": "layer_3/components/login-form/implementation",
  "task": "Implement login form component with validation",
  "constraints": [
    "All Layer 0 + Layer 1 + Layer 2 constraints apply",
    "Use React Hook Form for form management",
    "Validate email format and password strength",
    "Display clear error messages",
    "Support OAuth and email/password flows",
    "Match design system styling"
  ],
  "artifacts": {
    "files": [
      "src/features/auth/types.ts",
      "src/features/auth/api.ts",
      "src/design-system/components/Input.tsx"
    ]
  },
  "acceptanceCriteria": [
    "Form renders correctly",
    "Validation works",
    "Successful login redirects properly",
    "Error messages display",
    "Unit tests pass with >90% coverage"
  ],
  "status": "pending"
}
```

<!-- section_id: "1e7d6002-bb77-4dc2-be5d-77b088fdd751" -->
### Layer 3 → Layer 2 (Outgoing to Feature)

**File**: `3.00_to_features/outgoing.json`

**Content**: Component completion with implementation details

**Example**:
```json
{
  "schemaVersion": "1.0.0",
  "id": "l3-to-l2-login-complete-20241223",
  "kind": "vertical",
  "layer": 3,
  "from": "layer_3/components/login-form/archiving",
  "to": "layer_2/features/auth-system/testing",
  "task": "Login form component complete",
  "status": "completed",
  "results": {
    "summary": "Fully functional login form with validation and OAuth",
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
      "Form renders with email and password fields",
      "Email validation rejects invalid formats",
      "Password validation enforces strength requirements",
      "Submit calls API with correct credentials",
      "OAuth buttons trigger authentication flow",
      "Error states display appropriate messages"
    ],
    "metrics": {
      "linesOfCode": 342,
      "testCoverage": 94.5,
      "duration": "3 hours"
    }
  },
  "nextActions": [
    "Integrate with registration form for consistency",
    "Add to Storybook for design review"
  ]
}
```

<!-- section_id: "c9e53c02-f5d3-43e7-9934-6082fd759eb2" -->
## Simple Component Workflow (Most Common)

For most components, Layer 3 is a **worker layer** with minimal manager overhead:

1. **Receive Task**: Read `3.00_to_features/incoming.json`
2. **Implement**: Write code, tests, documentation (1-3 turns with Codex)
3. **Report**: Write results to `3.00_to_features/outgoing.json`

No stage pipeline needed - just direct execution.

<!-- section_id: "68882882-2a73-4b83-8b8b-2d88d9217691" -->
## Complex Component Workflow (Layer 4 Decomposition)

For complex components that benefit from decomposition:

<!-- section_id: "e3f2808d-a852-4868-a873-48e9659ff7c3" -->
### Layer 3 → Layer 4 (Downward to Sub-Components)

**File**: `3.01_to_subcomponents/outgoing/subcomp-<name>.json`

**Content**: Sub-component tasks (UI, logic, types, tests)

**Example**:
```json
{
  "schemaVersion": "1.0.0",
  "id": "l3-to-l4-login-ui-20241223",
  "kind": "vertical",
  "layer": 3,
  "from": "layer_3/components/login-form/planning",
  "to": "layer_4/subcomponents/login-ui/implementation",
  "task": "Implement login form UI elements",
  "constraints": [
    "All higher layer constraints",
    "Use design system Input and Button components",
    "ARIA labels for accessibility",
    "Responsive layout"
  ],
  "acceptanceCriteria": [
    "Email input with proper type",
    "Password input with show/hide toggle",
    "Submit button with loading state",
    "Accessible to screen readers"
  ],
  "status": "pending"
}
```

<!-- section_id: "515265c4-3e33-40b9-941a-f785483cac31" -->
### Layer 4 → Layer 3 (Upward from Sub-Components)

**File**: `3.01_to_subcomponents/incoming/subcomp-<name>.json`

**Content**: Sub-component implementation results

**Example**:
```json
{
  "schemaVersion": "1.0.0",
  "id": "l4-to-l3-login-ui-complete-20241223",
  "kind": "vertical",
  "layer": 4,
  "from": "layer_4/subcomponents/login-ui/implementation",
  "to": "layer_3/components/login-form/integration",
  "task": "Login UI elements complete",
  "status": "completed",
  "results": {
    "summary": "All UI elements implemented",
    "filesCreated": ["src/components/LoginForm/UI.tsx"],
    "metrics": {
      "linesOfCode": 87,
      "duration": "45 minutes"
    }
  }
}
```

<!-- section_id: "7277867d-f6d1-40fa-a4b6-30c77649422b" -->
## Decision: Simple Worker vs. Complex Manager

<!-- section_id: "275b85b8-b0dd-4d26-8d9e-81a827ddca76" -->
### Use Simple Worker Pattern When:
- Component fits in 1-3 files
- Single responsibility, clear interface
- Straightforward implementation (< 4 hours)
- Well-defined requirements with examples
- Standard patterns apply

**Tool**: Codex CLI for speed and cost efficiency

<!-- section_id: "be9d267c-fd1b-4fb4-9442-53142b5fb4fd" -->
### Use Complex Manager Pattern When:
- Component spans 5+ files
- Multiple concerns (UI, logic, types, tests, integration)
- Complex algorithms or business rules
- Critical component requiring deep reasoning
- Novel or experimental approach needed

**Tool**: Claude Code as manager, Codex as workers for sub-components

<!-- section_id: "eec5cd1b-0ab4-42f4-a028-c83ea427bfd6" -->
## Best Practices

1. **Default to Simple**: Start with simple worker pattern, only decompose if truly complex
2. **Fresh Sessions**: Use new Codex sessions for each component (avoid context dilution)
3. **Test Coverage**: Always write unit tests, aim for >80% coverage
4. **Clear Interfaces**: Define component props/types clearly before implementation
5. **Follow Patterns**: Match existing code style and conventions in the codebase
6. **Document Public APIs**: Add JSDoc/docstrings for exported functions
7. **Report Accurately**: Only mark complete when tests pass and acceptance criteria met
8. **Escalate Blockers**: If stuck, report to Layer 2 immediately

<!-- section_id: "605ae3cc-7851-40e6-a226-b2e33d9ffe97" -->
## Example: Simple Component (Login Form)

<!-- section_id: "c95e6420-3748-45a7-9864-fca9f4541aba" -->
### Worker receives task
```json
// 3.00_to_features/incoming.json
{
  "id": "l2-to-l3-login-20241223",
  "task": "Implement login form",
  "constraints": ["Use React Hook Form", "Validate inputs"],
  "status": "pending"
}
```

<!-- section_id: "c7fef65d-9248-4475-97d3-8c9e01421b4f" -->
### Worker implements in single session (Codex)
```
Turn 1: Create LoginForm.tsx with React Hook Form setup
Turn 2: Add validation logic and error handling
Turn 3: Write LoginForm.test.tsx with test cases
```

<!-- section_id: "0cb77684-2d6f-461b-890d-290b278bb3bf" -->
### Worker reports completion
```json
// 3.00_to_features/outgoing.json
{
  "id": "l3-to-l2-login-complete-20241223",
  "status": "completed",
  "results": {
    "filesCreated": ["LoginForm.tsx", "LoginForm.test.tsx"],
    "testCoverage": 94.5
  }
}
```

<!-- section_id: "01137ca3-79bf-4ed3-a4cd-025ff87a5f11" -->
## Example: Complex Component (Data Table)

<!-- section_id: "5110f385-6273-4d67-ab59-b3b8a9842078" -->
### Manager decomposes to Layer 4
```
// 3.01_to_subcomponents/outgoing/
subcomp-table-ui.json         (React table structure)
subcomp-table-sorting.json    (Sort logic)
subcomp-table-filtering.json  (Filter logic)
subcomp-table-pagination.json (Pagination logic)
subcomp-table-tests.json      (Test suite)
```

<!-- section_id: "c065b2c1-22f5-4293-b7ea-3e0c0d96ec4c" -->
### Sub-components execute in parallel
```
Batch 1 (parallel):
  - table-ui (Codex)
  - sorting, filtering, pagination (Codex each)

Batch 2 (after Batch 1):
  - integration tests (Claude Code)
```

<!-- section_id: "3bc6172e-84fd-4160-b641-a11b06bf8d09" -->
### Manager integrates and reports
```json
// 3.00_to_features/outgoing.json
{
  "status": "completed",
  "results": {
    "summary": "Complex data table with sorting, filtering, pagination",
    "subcomponentsIntegrated": 4
  }
}
```

<!-- section_id: "91ec09b9-f97d-4da9-9af9-77e626d12e59" -->
## Related Documentation

- **Canonical Schema**: [../../layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md](../../layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md) ← **START HERE**
- **Layer 3 Manager System**: [../3.00_ai_manager_system/README.md](../3.00_ai_manager_system/README.md)
- **Tool Selection**: [../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md](../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md)
