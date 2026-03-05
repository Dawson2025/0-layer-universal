---
resource_id: "2469b75a-ace6-405f-be25-93d9c22b11fa"
resource_type: "readme
document"
resource_name: "README"
---
# 2.00 AI Manager System - Coding Challenges Feature

<!-- section_id: "8c7f4649-74ce-479c-b695-b0c12e797e3e" -->
## Purpose

Contains the AI manager configuration for coordinating the coding challenges feature as a whole.

<!-- section_id: "dd84f9a0-624a-4ab9-b460-8e953f3326ff" -->
## Scope

This manager oversees:

- Workflow creation (developing new coding challenge workflows)
- Workflow execution (running completed workflows)
- Results tracking (linking to completed work)

<!-- section_id: "f7be9781-873e-41ab-83f2-c11244048a8b" -->
## Contents

- `feature_manager_prompt.md` - System prompt for the coding challenges feature manager
- `agent_config.yaml` - Configuration file for the coding challenges feature manager agent.
- Agent configurations for feature-level coordination

<!-- section_id: "ac9b8c08-af7c-44b1-bb00-2e81eb238231" -->
## Relationship to Sub-Components

```text
2.00_ai_manager_system/          # THIS - Feature-level manager
├── (coordinates)
│   ├── 2.01_workflow_creation/  # Has its own manager for workflow development
│   ├── 2.02_workflows/          # Has stages for workflow execution
│   └── 2.03_results/            # Results storage
```

<!-- section_id: "0ef29eb1-c8e8-45d1-9e82-0f63afcb6c5c" -->
## Usage

The feature manager is invoked when working on coding challenges at a high level, coordinating between workflow creation, execution, and results.
