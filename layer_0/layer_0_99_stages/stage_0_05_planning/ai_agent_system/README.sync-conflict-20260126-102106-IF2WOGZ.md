---
resource_id: "be96d2b6-fa66-4380-b9bf-7249a9bac544"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-102106-IF2WOGZ"
---
# Stage 0.02 Planning - AI Agent System

<!-- section_id: "6bc52bc2-b083-4ebd-a046-c32fd012c667" -->
## Overview

This directory contains AI agent configuration for the **Planning Stage** at Layer 0 (Universal). The planning stage is responsible for decomposing high-level goals into structured, actionable tasks that can be delegated to lower layers or subsequent stages.

<!-- section_id: "5fb6e651-4afa-40bb-a7b3-ce3810b1bef1" -->
## Stage Purpose

The planning stage:
- Receives clarified requirements from the instructions stage
- Analyzes scope and complexity
- Decomposes work into project-level tasks (for Layer 1) or stage-level subtasks
- Identifies dependencies and execution order
- Creates structured plan with acceptance criteria

<!-- section_id: "e715e68b-1465-4a54-9b82-8caf2896c879" -->
## Manager/Worker Workflow

<!-- section_id: "afc7e8ed-9ad3-403b-94f0-18a6809ceccd" -->
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

<!-- section_id: "1ccd8494-8e6d-447f-af5f-33c9bf9ed921" -->
### Worker Workflow (Less Common for Planning)

Planning is typically manager-heavy, but workers may be used for:
- **Research tasks**: Investigate technical options
- **Analysis tasks**: Review existing code or documentation
- **Estimation tasks**: Assess complexity or resource needs

Worker pattern:
1. Read focused research handoff
2. Perform bounded research (1-3 turns)
3. Report findings in result handoff

<!-- section_id: "b62ad358-56b8-4f01-a5ee-7c867a16727b" -->
## Handoff Flow

<!-- section_id: "bb1b038f-7259-4efc-828c-71e2c15425bb" -->
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

<!-- section_id: "6a308039-5041-4a0f-ac3c-269b260342a1" -->
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

<!-- section_id: "4964e314-9ced-40fa-a37c-64ed9db516ab" -->
## Tool Recommendations

For Layer 0 planning stage:

<!-- section_id: "717ae50c-be4a-40af-a848-08a063a9e19b" -->
### Primary Tool: Claude Code or Gemini CLI

**Claude Code**:
- Best for: Complex planning requiring deep understanding of codebase
- Strengths: Multi-file context, strong reasoning, good at dependency analysis
- Use when: Planning impacts existing universal infrastructure

**Gemini CLI**:
- Best for: Long planning sessions with many clarifying questions
- Strengths: Large context window, research-focused, good for exploratory planning
- Use when: Planning new projects or technologies

<!-- section_id: "0e03118c-cf38-4f21-ac1b-e8390273b4a1" -->
### When to Use Workers

Spawn workers for specific research tasks:
- **Tool**: Codex CLI for quick lookups, Claude Code for deep analysis
- **Pattern**: 1 worker per research question, execute in parallel
- **Example**: "Research available React table libraries" → Codex worker provides options

<!-- section_id: "07bf0e48-f7f0-4b80-a4b9-583dc21fcc86" -->
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

<!-- section_id: "112f0bab-8304-4b1e-a8e7-955214fe9a39" -->
## Context Files

This stage uses standard context cascading:
- **CLAUDE.md**: Universal → project → stage (if exists)
- **AGENTS.md**: Universal → project → stage (if exists)
- **GEMINI.md**: Manual merge of relevant context

Stage-specific context (if needed) goes in this directory.

<!-- section_id: "a4759b9e-de3a-46ae-b973-af1d6bea1a56" -->
## Deeper References

For comprehensive understanding of planning patterns and decomposition strategies:

- **Architecture**: [../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md](../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md)
- **Parallel Execution**: [../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md](../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md)
- **Handoff Schema**: [../../../0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md](../../../0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md)

<!-- section_id: "ee7bc110-eb05-436d-8840-c01fa46bfa25" -->
## Best Practices

1. **Be Specific**: Create concrete, actionable subtasks, not vague goals
2. **Identify Dependencies**: Explicitly note what must complete before what
3. **Estimate Complexity**: Flag high-risk or complex subtasks
4. **Consider Parallelism**: Identify which subtasks can run concurrently
5. **Define Success**: Ensure each subtask has clear acceptance criteria
6. **Think Ahead**: Anticipate integration points and potential issues
