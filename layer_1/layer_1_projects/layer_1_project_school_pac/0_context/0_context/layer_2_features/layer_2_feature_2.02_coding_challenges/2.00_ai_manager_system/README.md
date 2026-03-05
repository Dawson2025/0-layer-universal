---
resource_id: "2469b75a-ace6-405f-be25-93d9c22b11fa"
resource_type: "readme
document"
resource_name: "README"
---
# 2.00 AI Manager System - Coding Challenges Feature

## Purpose

Contains the AI manager configuration for coordinating the coding challenges feature as a whole.

## Scope

This manager oversees:

- Workflow creation (developing new coding challenge workflows)
- Workflow execution (running completed workflows)
- Results tracking (linking to completed work)

## Contents

- `feature_manager_prompt.md` - System prompt for the coding challenges feature manager
- `agent_config.yaml` - Configuration file for the coding challenges feature manager agent.
- Agent configurations for feature-level coordination

## Relationship to Sub-Components

```text
2.00_ai_manager_system/          # THIS - Feature-level manager
├── (coordinates)
│   ├── 2.01_workflow_creation/  # Has its own manager for workflow development
│   ├── 2.02_workflows/          # Has stages for workflow execution
│   └── 2.03_results/            # Results storage
```

## Usage

The feature manager is invoked when working on coding challenges at a high level, coordinating between workflow creation, execution, and results.
