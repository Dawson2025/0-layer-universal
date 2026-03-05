---
resource_id: "9b217153-d393-42ac-9d69-7b99589e2b8d"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-035814-IF2WOGZ"
---
# Stage 0.02 Planning - AI Agent System

<!-- section_id: "6864aa0a-bb35-4bd8-9bf4-07aa8ef2d414" -->
## Overview

This directory contains AI agent configuration for the **Planning Stage** at Layer 0 (Universal). The planning stage is responsible for decomposing high-level goals into structured, actionable tasks that can be delegated to lower layers or subsequent stages.

<!-- section_id: "39e83b1d-6e22-408b-b454-50e498e6ae1b" -->
## Stage Purpose

The planning stage:
- Receives clarified requirements from the instructions stage
- Analyzes scope and complexity
- Decomposes work into project-level tasks (for Layer 1) or stage-level subtasks
- Identifies dependencies and execution order
- Creates structured plan with acceptance criteria

<!-- section_id: "3ad0bb94-117e-42b2-b452-80eee88a8210" -->
## Manager/Worker Workflow

<!-- section_id: "f51edc5f-f472-4701-920a-11edde037f15" -->
### Manager Workflow (Typical for Planning Stage)

1. **Read Incoming Handoff**:
   - Location: `../hand_off_documents/incoming.json`
   - Source: Previous stage (stage_0_03_instructions)
   - Contains: Clarified requirements with universal constraints applied

2. **Analyze and Decompose**:
   - Assess scope: Is this a single project, multiple projects, or universal infrastructure?
   - Identify major components or projects
   - Determine dependencies between tasks
   - Estimate complexity and required resources

3. **Create Structured Plan**:
   - For project-level work: Decompose to Layer 1 tasks (one per project)
   - For universal infrastructure: Break into implementation subtasks
   - For multi-stage work: Create stage-by-stage plan within Layer 0

4. **Spawn Workers** (if needed):
   - Complex planning may use worker agents for research or analysis
   - Example: Worker researches technology options for a requirement
   - Example: Worker analyzes existing codebase to identify impact areas

5. **Write Outgoing Handoff**:
   - Location: `../hand_off_documents/outgoing.json`
   - Destination: Next stage (stage_0_05_design) OR Layer 1 managers
   - Contains: Structured plan with subtasks, dependencies, acceptance criteria

<!-- section_id: "f2fdba89-05d2-46dd-8df7-0c9406a55e39" -->
### Worker Workflow (Less Common for Planning)

Planning is typically manager-heavy, but workers may be used for:
- **Research tasks**: Investigate technical options
- **Analysis tasks**: Review existing code or documentation
- **Estimation tasks**: Assess complexity or resource needs

Worker pattern:
1. Read focused research handoff
2. Perform bounded research (1-3 turns)
3. Report findings in result handoff

<!-- section_id: "d13b4bf5-1c39-48ec-8444-cb9020fc4f02" -->
## Handoff Flow

<!-- section_id: "cb394064-86e0-48d9-8fc9-976a6d4c20fe" -->
### Incoming Handoff (from Instructions Stage)

**File**: `../hand_off_documents/incoming.json`

**Example**:
```json
{
  "schemaVersion": "1.0.0",
  "id": "l0-instructions-to-planning-20241223",
  "layer": 0,
  "stage": "instructions",
  "from": "layer_0/stage_0_03_instructions",
  "to": "layer_0/stage_0_04_planning",
  "task": "Create new web application for project management",
  "constraints": [
    "Use TypeScript strict mode",
    "Follow Layer 0 security rules",
    "Comprehensive error handling",
    "Unit and integration tests with >80% coverage",
    "Document all public APIs"
  ],
  "acceptanceCriteria": [
    "Users can create, update, delete tasks",
    "Team collaboration features work",
    "Reporting dashboard functional",
    "All tests passing",
    "Documentation complete"
  ],
  "status": "completed"
}
```

<!-- section_id: "58cfb8d2-f1b4-49dd-8dda-f83f21692f67" -->
### Outgoing Handoff (to Design Stage or Layer 1)

**File**: `../hand_off_documents/outgoing.json`

**Example** (planning to design within Layer 0):
```json
{
  "schemaVersion": "1.0.0",
  "id": "l0-planning-to-design-20241223",
  "layer": 0,
  "stage": "planning",
  "from": "layer_0/stage_0_04_planning",
  "to": "layer_0/stage_0_05_design",
  "task": "Design architecture for project management web app",
  "constraints": [
    "All Layer 0 constraints from instructions stage",
    "Use TypeScript strict mode",
    "Security-first design",
    "Testable architecture"
  ],
  "subtasks": [
    {
      "id": "design-data-model",
      "description": "Design database schema for tasks, users, teams",
      "status": "pending"
    },
    {
      "id": "design-api",
      "description": "Design REST API endpoints and contracts",
      "status": "pending"
    },
    {
      "id": "design-ui-architecture",
      "description": "Design component hierarchy and state management",
      "status": "pending"
    }
  ],
  "results": {
    "summary": "Decomposed app into 3 main design areas",
    "plan": "Sequential design: data model first, then API, then UI (UI depends on API)"
  },
  "status": "completed",
  "nextActions": [
    "Design data model with focus on scalability",
    "Define API contracts before implementation",
    "Choose state management approach (Redux, Zustand, etc.)"
  ]
}
```

**Example** (planning to Layer 1 project):
```json
{
  "schemaVersion": "1.0.0",
  "id": "l0-to-l1-pm-webapp-20241223",
  "kind": "vertical",
  "layer": 0,
  "from": "layer_0/stage_0_04_planning",
  "to": "layer_1/projects/pm-webapp/request",
  "task": "Implement project management web application",
  "constraints": [
    "All Layer 0 universal constraints apply",
    "Use TypeScript strict mode",
    "Security, testing, documentation standards"
  ],
  "subtasks": [
    {
      "id": "project-architecture",
      "description": "Define project architecture and tech stack",
      "status": "pending"
    },
    {
      "id": "core-features",
      "description": "Implement core features (task CRUD, teams, auth)",
      "status": "pending"
    },
    {
      "id": "deployment",
      "description": "Deploy to production environment",
      "status": "pending"
    }
  ],
  "acceptanceCriteria": [
    "All acceptance criteria from instructions stage met",
    "Project follows universal architecture patterns",
    "Deployment pipeline configured"
  ],
  "status": "pending",
  "createdAt": "2024-12-23T12:00:00Z"
}
```

<!-- section_id: "b8eaf659-ebd9-427d-8094-1abb8bcf8fd5" -->
## Tool Recommendations

For Layer 0 planning stage:

<!-- section_id: "480fbf35-7d8b-4f59-a4d7-310602c8ebc3" -->
### Primary Tool: Claude Code or Gemini CLI

**Claude Code**:
- Best for: Complex planning requiring deep understanding of codebase
- Strengths: Multi-file context, strong reasoning, good at dependency analysis
- Use when: Planning impacts existing universal infrastructure

**Gemini CLI**:
- Best for: Long planning sessions with many clarifying questions
- Strengths: Large context window, research-focused, good for exploratory planning
- Use when: Planning new projects or technologies

<!-- section_id: "bc46d49c-4501-46ac-89a6-07cf53827ded" -->
### When to Use Workers

Spawn workers for specific research tasks:
- **Tool**: Codex CLI for quick lookups, Claude Code for deep analysis
- **Pattern**: 1 worker per research question, execute in parallel
- **Example**: "Research available React table libraries" → Codex worker provides options

<!-- section_id: "3887351d-6c70-401f-853e-19e285a4c5a5" -->
## Parallel Execution

Planning stage itself is typically sequential (one manager), but can spawn parallel research workers:

```python
# Pseudo-code for planning stage manager

# Read incoming handoff
incoming = read_handoff("incoming.json")

# Identify research needs
research_tasks = [
    "Research authentication libraries",
    "Research database options",
    "Research deployment platforms"
]

# Spawn research workers in parallel
research_results = execute_parallel([
    spawn_worker("codex", task) for task in research_tasks
])

# Synthesize plan using research results
plan = create_plan(incoming, research_results)

# Write outgoing handoff
write_handoff("outgoing.json", plan)
```

<!-- section_id: "98e5e175-76a7-4d66-8bd2-84f5284a677a" -->
## Context Files

This stage uses standard context cascading:
- **CLAUDE.md**: Universal → project → stage (if exists)
- **AGENTS.md**: Universal → project → stage (if exists)
- **GEMINI.md**: Manual merge of relevant context

Stage-specific context (if needed) goes in this directory.

<!-- section_id: "bcaa7de3-a4e5-4fa1-b956-cc0cd37561b3" -->
## Deeper References

For comprehensive understanding of planning patterns and decomposition strategies:

- **Architecture**: [../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md](../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md)
- **Parallel Execution**: [../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md](../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md)
- **Handoff Schema**: [../../../0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md](../../../0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md)

<!-- section_id: "9c13b210-1b0c-4be6-be43-b4ac481fc96a" -->
## Best Practices

1. **Be Specific**: Create concrete, actionable subtasks, not vague goals
2. **Identify Dependencies**: Explicitly note what must complete before what
3. **Estimate Complexity**: Flag high-risk or complex subtasks
4. **Consider Parallelism**: Identify which subtasks can run concurrently
5. **Define Success**: Ensure each subtask has clear acceptance criteria
6. **Think Ahead**: Anticipate integration points and potential issues
