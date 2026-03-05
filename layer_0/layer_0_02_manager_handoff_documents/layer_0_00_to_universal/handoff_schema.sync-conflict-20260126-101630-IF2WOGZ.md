---
resource_id: "a5fc09d8-b4ec-4428-ae81-5f69180c5947"
resource_type: "document"
resource_name: "handoff_schema.sync-conflict-20260126-101630-IF2WOGZ"
---
# Handoff Schema Definition

<!-- section_id: "0c626a49-ba5b-4158-a9ff-60953086b897" -->
## Overview

This document defines the canonical handoff schema used throughout the AI Manager Hierarchy System. Handoffs are the primary mechanism for communicating work, state, and results between managers, workers, layers, and stages.

All agents participating in the hierarchy must read and write handoffs conforming to this schema.

<!-- section_id: "fab66ad4-f549-43f0-8294-9fc52f764282" -->
## Schema Version

**Current Version:** `1.0.0`

This schema follows semantic versioning. Agents should check `schemaVersion` and handle backward compatibility appropriately.

<!-- section_id: "70fa1dcc-a4f1-46f7-94be-f03ac5260f0c" -->
## Core Principles

1. **Forward Compatibility**: Additional fields can be added without breaking existing agents
2. **Versioned**: Every handoff includes `schemaVersion` for evolution tracking
3. **Structured but Flexible**: Required fields ensure consistency; optional fields allow specialization
4. **Human-Readable**: JSON format with descriptive field names for debugging and transparency

<!-- section_id: "d840bc96-b430-4024-96b7-82ad9960b419" -->
## Canonical Schema (JSON Schema Form)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AI Manager Hierarchy Handoff",
  "description": "Canonical handoff document for inter-agent communication",
  "type": "object",
  "required": ["schemaVersion", "id", "layer", "stage", "from", "to", "task", "status"],
  "properties": {
    "schemaVersion": {
      "type": "string",
      "description": "Version of this handoff schema (semver)",
      "example": "1.0.0"
    },
    "id": {
      "type": "string",
      "description": "Unique identifier for this handoff (for traceability and DAG construction)",
      "example": "layer2-auth-implementation-20241223-a1b2c3"
    },
    "kind": {
      "type": "string",
      "description": "Type of handoff (optional but recommended for filtering/routing)",
      "enum": ["request", "instruction", "plan", "design", "implementation", "test", "criticism", "fix", "archive", "vertical", "horizontal"],
      "example": "implementation"
    },
    "layer": {
      "description": "Numeric layer ID or string identifier",
      "oneOf": [
        {"type": "integer", "minimum": 0, "maximum": 10},
        {"type": "string", "pattern": "^layer_[0-9]+_.*$"}
      ],
      "example": 2
    },
    "stage": {
      "type": "string",
      "description": "Name of the current or target stage",
      "example": "stage_2.04_development"
    },
    "from": {
      "type": "string",
      "description": "Identifier of the agent/stage/layer that created this handoff",
      "example": "layer_2/features/auth-system/planning"
    },
    "to": {
      "type": "string",
      "description": "Intended recipient agent/stage/layer",
      "example": "layer_3/components/login-form/implementation"
    },
    "createdAt": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp of handoff creation",
      "example": "2024-12-23T12:34:56Z"
    },
    "updatedAt": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp of last update",
      "example": "2024-12-23T13:45:12Z"
    },
    "parentIds": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Array of parent handoff IDs (for DAG lineage tracking)",
      "example": ["layer2-auth-planning-20241223-x1y2z3"]
    },
    "task": {
      "type": "string",
      "description": "Human-readable summary of what needs to be done or what was done",
      "example": "Implement login form component with email/password fields, validation, and submit handler"
    },
    "constraints": {
      "type": "array",
      "items": {
        "oneOf": [
          {"type": "string"},
          {"type": "object"}
        ]
      },
      "description": "List of constraints, rules, or requirements (inherited from higher layers + local)",
      "example": [
        "Use TypeScript strict mode",
        "Follow Layer 0 security rules (no hardcoded secrets)",
        "Validate email format client-side",
        {"type": "performance", "maxLoadTime": "200ms"}
      ]
    },
    "environment": {
      "type": "object",
      "description": "Environment metadata (OS, repo, branch, etc.)",
      "properties": {
        "os": {"type": "string", "example": "wsl"},
        "repoPath": {"type": "string", "example": "/home/user/projects/my-app"},
        "branch": {"type": "string", "example": "feature/auth-system"},
        "featureFlags": {"type": "object"}
      }
    },
    "subtasks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "description": {"type": "string"},
          "assignedTo": {"type": "string"},
          "status": {"type": "string", "enum": ["pending", "in_progress", "completed", "failed"]}
        }
      },
      "description": "List of smaller tasks (for managers decomposing work)",
      "example": [
        {"id": "subtask-1", "description": "Create LoginForm.tsx skeleton", "status": "completed"},
        {"id": "subtask-2", "description": "Add form validation logic", "status": "in_progress"}
      ]
    },
    "acceptanceCriteria": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Bullets describing success conditions",
      "example": [
        "All TypeScript files compile without errors",
        "Unit tests pass with >80% coverage",
        "Form validates email format and password strength",
        "Submit handler calls auth API with correct payload"
      ]
    },
    "artifacts": {
      "type": "object",
      "description": "References to files, URLs, database entities, or other resources",
      "properties": {
        "files": {
          "type": "array",
          "items": {"type": "string"},
          "example": ["src/components/LoginForm.tsx", "src/hooks/useLogin.ts"]
        },
        "urls": {
          "type": "array",
          "items": {"type": "string"},
          "example": ["https://docs.example.com/auth-api"]
        },
        "dependencies": {
          "type": "array",
          "items": {"type": "string"},
          "example": ["react-hook-form@7.48.0", "zod@3.22.0"]
        }
      }
    },
    "status": {
      "type": "string",
      "enum": ["pending", "in_progress", "completed", "failed", "blocked"],
      "description": "Current status of the work described by this handoff",
      "example": "completed"
    },
    "results": {
      "type": "object",
      "description": "Stage-specific outputs and findings",
      "properties": {
        "summary": {"type": "string"},
        "filesCreated": {"type": "array", "items": {"type": "string"}},
        "filesModified": {"type": "array", "items": {"type": "string"}},
        "testsAdded": {"type": "array", "items": {"type": "string"}},
        "metrics": {"type": "object"}
      },
      "example": {
        "summary": "Successfully implemented login form with validation",
        "filesCreated": ["src/components/LoginForm.tsx", "src/components/LoginForm.test.tsx"],
        "filesModified": ["src/routes/auth.tsx"],
        "testsAdded": ["Login form renders correctly", "Email validation works"],
        "metrics": {
          "linesOfCode": 245,
          "testCoverage": 87.5,
          "duration": "15 minutes"
        }
      }
    },
    "errors": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "message": {"type": "string"},
          "code": {"type": "string"},
          "severity": {"type": "string", "enum": ["warning", "error", "critical"]},
          "recoverable": {"type": "boolean"}
        }
      },
      "description": "Descriptions of failures, exceptions, or blockers",
      "example": [
        {"message": "Type error in useLogin.ts line 42", "severity": "error", "recoverable": true}
      ]
    },
    "nextActions": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Suggested next steps for the next stage or manager",
      "example": [
        "Run integration tests to verify auth flow",
        "Update auth documentation with new component",
        "Review accessibility compliance"
      ]
    }
  }
}
```

<!-- section_id: "0c7daeca-61d9-4795-8037-bad71ebae86a" -->
## Flow Types

<!-- section_id: "6a04085d-6e53-4e6e-a8f7-e52d5709d71c" -->
### Vertical Handoffs (Layer-to-Layer)

Vertical handoffs pass tasks and results **between layers** in the hierarchy.

**Downward** (from higher abstraction to lower):
- L0 → L1: Universal constraints applied to project-level goals
- L1 → L2: Project context applied to feature-level tasks
- L2 → L3: Feature requirements decomposed to component tasks
- L3 → L4: Component broken into sub-components

**Upward** (from lower to higher):
- L4 → L3 → L2 → L1 → L0: Results, summaries, metrics, and status aggregated up

**Example**: Layer 1 project manager sends handoff to Layer 2 feature manager

```json
{
  "schemaVersion": "1.0.0",
  "id": "l1-to-l2-auth-feature-20241223",
  "kind": "vertical",
  "layer": 1,
  "stage": "planning",
  "from": "layer_1/project/ecommerce/planning",
  "to": "layer_2/features/auth-system/request",
  "createdAt": "2024-12-23T10:00:00Z",
  "task": "Implement complete authentication system for ecommerce platform",
  "constraints": [
    "Follow Layer 0 TypeScript and security rules",
    "GDPR compliant user data handling",
    "Support OAuth 2.0 and email/password auth",
    "Session management with JWT tokens"
  ],
  "acceptanceCriteria": [
    "Users can register, login, and reset passwords",
    "OAuth integration with Google and GitHub",
    "Session tokens are secure and expire appropriately",
    "All auth endpoints have rate limiting"
  ],
  "status": "pending"
}
```

<!-- section_id: "fecfc60c-302f-4116-8c30-6dbd29d8d2cc" -->
### Horizontal Handoffs (Stage-to-Stage)

Horizontal handoffs move work through the **chronological pipeline** within a single layer.

**Pipeline**: `request → instructions → planning → design → implementation → testing → criticism → fixing → archiving`

Each stage:
- Reads from `hand_off_documents/incoming.*`
- Writes to `hand_off_documents/outgoing.*`
- Preserves prior context while appending its own contributions

**Example**: Planning stage completes and passes to design stage

```json
{
  "schemaVersion": "1.0.0",
  "id": "l2-auth-planning-to-design-20241223",
  "kind": "horizontal",
  "layer": 2,
  "stage": "planning",
  "from": "layer_2/features/auth-system/planning",
  "to": "layer_2/features/auth-system/design",
  "createdAt": "2024-12-23T11:30:00Z",
  "updatedAt": "2024-12-23T11:45:00Z",
  "parentIds": ["l1-to-l2-auth-feature-20241223"],
  "task": "Design authentication system architecture",
  "constraints": [
    "Follow Layer 0 TypeScript and security rules",
    "GDPR compliant user data handling",
    "Support OAuth 2.0 and email/password auth"
  ],
  "subtasks": [
    {
      "id": "component-login",
      "description": "Login form component",
      "status": "pending"
    },
    {
      "id": "component-register",
      "description": "Registration form component",
      "status": "pending"
    },
    {
      "id": "component-reset",
      "description": "Password reset flow",
      "status": "pending"
    },
    {
      "id": "api-handlers",
      "description": "Auth API endpoints",
      "status": "pending"
    },
    {
      "id": "integration-tests",
      "description": "End-to-end auth tests",
      "status": "pending"
    }
  ],
  "results": {
    "summary": "Decomposed auth system into 5 parallelizable components",
    "plan": "Components can be developed independently, integration tests run after all complete"
  },
  "status": "completed",
  "nextActions": [
    "Design component interfaces and data flows",
    "Define API contracts",
    "Plan database schema for user/session storage"
  ]
}
```

<!-- section_id: "b3efc40f-8fce-4b52-b0a9-92b329ea6b21" -->
## File Locations

<!-- section_id: "bc3d8ca2-b2d1-42a7-b5f3-58c4786f3292" -->
### Stage-Level Handoffs

Each stage directory has:
```
stage_X.YY_<stage_name>/
  hand_off_documents/
    incoming.json       # Handoff to be processed by this stage
    outgoing.json       # Handoff produced after stage completes
    incoming/           # Optional: multiple parallel incoming tasks
      task-1.json
      task-2.json
    outgoing/           # Optional: multiple parallel outgoing results
      task-1.json
      task-2.json
```

<!-- section_id: "4f20c8b0-9ee0-44ae-a1c5-6ce9a291ab22" -->
### Layer-Level Handoffs

Each layer's manager handoff directory:
```
layer_N/
  layer_N_02_manager_handoff_documents/
    layer_N_00_to_universal/
      incoming.json     # From L(N-1) to this layer
      outgoing.json     # From this layer back to L(N-1)
    layer_N_01_to_specific/
      incoming.json     # From this layer to L(N+1)
      outgoing.json     # From L(N+1) back to this layer
```

<!-- section_id: "60851c5f-d59d-4f18-9a03-9b3a19474a1b" -->
## Extensibility

<!-- section_id: "ef38f8f6-dec3-461c-b83c-ac83f9abb0cb" -->
### Adding Custom Fields

Agents may add custom fields to handoffs as long as:
1. All required fields are present
2. Custom fields don't conflict with reserved names
3. Unknown fields are gracefully ignored by agents that don't understand them

**Example**: Adding security scan results
```json
{
  "schemaVersion": "1.0.0",
  "id": "...",
  "status": "completed",
  "results": {...},
  "securityScanResults": {
    "vulnerabilities": 0,
    "warnings": 2,
    "scanTool": "npm audit",
    "timestamp": "2024-12-23T12:00:00Z"
  }
}
```

<!-- section_id: "f076bb60-c51b-4901-b744-b8e75bf29092" -->
### Version Evolution

When the schema evolves:
1. Increment `schemaVersion` following semver
2. Document changes in this file
3. Agents should handle multiple versions gracefully:
   - Read: Accept older versions, map to current understanding
   - Write: Use current version

<!-- section_id: "26e3c160-4a2c-4ce1-81e9-476b63f5e0f9" -->
## Reference Implementations

For detailed implementation patterns, see:
- **Architecture**: `/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_ai_manager_hierarchy_system/layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md`
- **Parallel Execution**: `/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_ai_manager_hierarchy_system/layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md`
- **Supervisor Patterns**: `/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_ai_manager_hierarchy_system/layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/things_learned/ideal_ai_manager_hierarchy_system/supervisor_patterns.md`

<!-- section_id: "2a780b6d-7b43-45b3-9389-1543393333a5" -->
## Usage Guidelines

1. **Managers**: Read incoming handoffs, decompose to subtasks, spawn workers, aggregate results to outgoing handoffs
2. **Workers**: Read single incoming handoff, perform bounded work (1-3 actions), write outgoing handoff with results
3. **Supervisors**: Watch handoff directories, route to appropriate agents based on policy, monitor completion
4. **Debugging**: All handoffs are human-readable JSON files in the filesystem for easy inspection and debugging

<!-- section_id: "6d5a2df3-066d-47f0-8d69-58f55a78e9f0" -->
## Change Log

<!-- section_id: "9e93cb4f-fcee-4874-b222-340fd77c80c5" -->
### Version 1.0.0 (2024-12-23)
- Initial canonical schema definition
- Support for vertical and horizontal handoff flows
- Core required and optional fields established
- JSON Schema formal specification
