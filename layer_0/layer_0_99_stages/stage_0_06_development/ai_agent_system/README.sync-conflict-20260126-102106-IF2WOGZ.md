---
resource_id: "d1b4388d-31d3-42f8-866c-f8533be39afb"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-102106-IF2WOGZ"
---
# Stage 0.04 Development - AI Agent System

<!-- section_id: "880ea9d6-720f-462b-a960-e62125455de8" -->
## Overview

This directory contains AI agent configuration for the **Development Stage** at Layer 0 (Universal). The development stage is responsible for implementing code, infrastructure, and documentation changes. At Layer 0, this typically means universal infrastructure, tools, protocols, or documentation that applies across all projects.

<!-- section_id: "528679a0-bf63-4b44-b6d8-401002b9cbb2" -->
## Stage Purpose

The development stage:
- Receives design specifications from the design stage
- Implements code, configuration, and documentation
- Creates or modifies universal infrastructure
- Produces artifacts ready for testing
- Reports implementation details and any deviations from design

<!-- section_id: "bfeeeb62-5186-4a85-8fcd-10f022c786fe" -->
## Manager/Worker Workflow

<!-- section_id: "db2e2a44-04a0-4a32-aa58-eb006a51d0d1" -->
### Manager Workflow (For Complex Universal Infrastructure)

Use manager pattern when implementing complex universal systems that span multiple files or sub-components:

1. **Read Incoming Handoff**:
   - Location: `../hand_off_documents/incoming.json`
   - Source: stage_0_05_design
   - Contains: Design specifications, architecture, interfaces

2. **Decompose to Workers**:
   - Break implementation into independent units
   - Assign each unit to a worker (potentially parallel)
   - Each worker handles 1-3 files or a cohesive module

3. **Spawn Workers**:
   - Create handoffs for each implementation unit
   - Execute workers (parallel if independent)
   - Monitor progress and collect results

4. **Integration**:
   - Assemble worker outputs into cohesive system
   - Ensure all parts work together
   - Verify against design specifications

5. **Write Outgoing Handoff**:
   - Location: `../hand_off_documents/outgoing.json`
   - Destination: stage_0_07_testing
   - Contains: List of files created/modified, implementation notes, deviations

<!-- section_id: "85bca3a7-5a8e-43af-aca0-099f280a83a1" -->
### Worker Workflow (Most Common for Development)

For focused implementation tasks (single file, module, or small set of related files):

1. **Read Task Handoff**:
   - Specific implementation requirement
   - Design constraints and specifications
   - Context files and dependencies

2. **Implement** (typically 1-3 turns):
   - Write code following design
   - Add inline documentation
   - Handle edge cases identified in design
   - Follow universal coding standards

3. **Write Result**:
   - Report files created/modified
   - Note any implementation decisions
   - Flag blockers or deviations from design

4. **Exit**: Return control to manager or next stage

<!-- section_id: "7a7d7b46-933c-4fc9-87a5-109134e0ed53" -->
## Handoff Flow

<!-- section_id: "925afd30-307f-4169-9981-a2fd1e9a3122" -->
### Incoming Handoff (from Design Stage)

**File**: `../hand_off_documents/incoming.json`

**Example**:
```json
{
  "schemaVersion": "1.0.0",
  "id": "l0-design-to-dev-20241223",
  "layer": 0,
  "stage": "design",
  "from": "layer_0/stage_0_05_design",
  "to": "layer_0/stage_0_06_development",
  "task": "Implement new universal logging protocol",
  "constraints": [
    "All Layer 0 constraints apply",
    "TypeScript strict mode",
    "Zero external dependencies for core functionality",
    "Support Node.js and browser environments",
    "Extensible plugin architecture"
  ],
  "artifacts": {
    "files": [
      "docs/design/logging-protocol-design.md",
      "src/types/logger.d.ts"
    ]
  },
  "subtasks": [
    {
      "id": "core-logger",
      "description": "Implement core Logger class",
      "assignedTo": "worker-1"
    },
    {
      "id": "formatters",
      "description": "Implement log formatters (JSON, text, etc.)",
      "assignedTo": "worker-2"
    },
    {
      "id": "transports",
      "description": "Implement log transports (console, file, remote)",
      "assignedTo": "worker-3"
    },
    {
      "id": "integration",
      "description": "Wire components together and export public API",
      "assignedTo": "manager"
    }
  ],
  "acceptanceCriteria": [
    "Logger implements design interface exactly",
    "All formatters produce correct output",
    "Transports write to correct destinations",
    "Plugin system allows custom extensions",
    "TypeScript types are complete and correct"
  ],
  "status": "completed"
}
```

<!-- section_id: "da31d123-d853-44b2-bf0c-71312f3fdcee" -->
### Outgoing Handoff (to Testing Stage)

**File**: `../hand_off_documents/outgoing.json`

**Example**:
```json
{
  "schemaVersion": "1.0.0",
  "id": "l0-dev-to-testing-20241223",
  "layer": 0,
  "stage": "development",
  "from": "layer_0/stage_0_06_development",
  "to": "layer_0/stage_0_07_testing",
  "task": "Universal logging protocol implementation complete",
  "status": "completed",
  "results": {
    "summary": "Implemented logging protocol with core, formatters, and transports",
    "filesCreated": [
      "src/universal/logging/Logger.ts",
      "src/universal/logging/formatters/JsonFormatter.ts",
      "src/universal/logging/formatters/TextFormatter.ts",
      "src/universal/logging/transports/ConsoleTransport.ts",
      "src/universal/logging/transports/FileTransport.ts",
      "src/universal/logging/transports/RemoteTransport.ts",
      "src/universal/logging/index.ts"
    ],
    "filesModified": [
      "src/universal/index.ts"
    ],
    "implementationNotes": [
      "Used singleton pattern for default logger instance",
      "Formatters are composable via plugin system",
      "File transport uses streaming for large logs",
      "Remote transport includes retry logic with exponential backoff"
    ],
    "deviations": [
      {
        "original": "Design specified polling for file transport",
        "actual": "Implemented streaming instead for better performance",
        "rationale": "Streaming reduces memory footprint for large log files"
      }
    ]
  },
  "nextActions": [
    "Write comprehensive unit tests for each component",
    "Write integration tests for end-to-end scenarios",
    "Test in both Node.js and browser environments",
    "Verify plugin system extensibility"
  ],
  "createdAt": "2024-12-23T13:00:00Z",
  "updatedAt": "2024-12-23T16:30:00Z"
}
```

<!-- section_id: "ddfe7eae-b66f-4442-92cc-e3198c1235ab" -->
## Tool Recommendations

For Layer 0 development stage:

<!-- section_id: "5e849988-c07f-4dc2-bb96-cc49e2e9ca1d" -->
### Primary Tools

**For Workers** (most implementation):
- **Codex CLI**: Fast, focused implementation of single modules
  - Use for: Individual classes, functions, utilities
  - Pattern: 1 file or small cohesive module per session (1-3 turns)
  - Example: Implement JsonFormatter.ts in single session

- **Claude Code**: Complex, multi-file implementation
  - Use for: Core components requiring deep reasoning
  - Use for: Security-critical code
  - Use for: Complex algorithms or state management
  - Example: Implement Logger class with intricate plugin system

**For Managers** (when decomposing):
- **Claude Code**: Orchestrating multiple workers and integration
  - Use for: Breaking down complex universal systems
  - Use for: Integrating multiple worker outputs

<!-- section_id: "15fa9f5f-9eaa-411a-9041-a9265082c407" -->
### Tool Selection Guide

```
Simple utility (< 100 LOC, 1 file):
  → Codex CLI worker (single session)

Standard component (< 300 LOC, 1-2 files):
  → Codex CLI worker (1-2 sessions) or Claude Code worker

Complex component (> 300 LOC, multiple files):
  → Claude Code manager → multiple Codex workers

Critical component (security, core infrastructure):
  → Claude Code worker (deep reasoning required)
```

<!-- section_id: "6397cd6c-07b3-4d3d-8c5c-a93bf08bfe9e" -->
## Parallel Execution

Development stage benefits significantly from parallelization:

<!-- section_id: "b4fff28a-719d-4761-bcd3-3a2191f13fab" -->
### Pattern: Parallel Component Implementation

```python
# Pseudo-code for development stage manager

# Read incoming design handoff
design = read_handoff("incoming.json")

# Identify independent implementation units from design
units = [
    {"id": "core-logger", "files": ["Logger.ts"], "complexity": "high"},
    {"id": "json-formatter", "files": ["JsonFormatter.ts"], "complexity": "low"},
    {"id": "text-formatter", "files": ["TextFormatter.ts"], "complexity": "low"},
    {"id": "console-transport", "files": ["ConsoleTransport.ts"], "complexity": "low"},
    {"id": "file-transport", "files": ["FileTransport.ts"], "complexity": "medium"},
]

# Separate by dependencies
batch_1 = ["json-formatter", "text-formatter"]  # No dependencies
batch_2 = ["console-transport", "file-transport"]  # Depend on formatters
batch_3 = ["core-logger"]  # Integrates everything

# Execute batches
for batch in [batch_1, batch_2, batch_3]:
    # Spawn workers in parallel within batch
    results = execute_parallel_batch([
        spawn_worker(select_tool(unit), create_handoff(unit))
        for unit_id in batch
        for unit in units if unit["id"] == unit_id
    ])

    # Check for failures before continuing
    if any_failures(results):
        escalate_and_abort()

# Integration step (manager)
integrate_components(all_results)
write_outgoing_handoff()
```

<!-- section_id: "ae735511-f1d6-4ee2-8ee2-559d0011f98e" -->
### Example: Logging Protocol Implementation

**Batch 0** (parallel - no dependencies):
- json-formatter (Codex)
- text-formatter (Codex)

**Batch 1** (parallel - depend on formatters):
- console-transport (Codex)
- file-transport (Codex)
- remote-transport (Claude Code - complex retry logic)

**Batch 2** (sequential - integrates all):
- core-logger (Claude Code - orchestrates all components)
- index.ts export (Codex - simple re-export)

<!-- section_id: "47b7b03f-8137-497e-9930-85e0498b30bf" -->
## Context Files

Development stage benefits from comprehensive context:

- **CLAUDE.md**: Universal coding standards, architecture patterns
- **AGENTS.md**: Quick reference for common patterns
- **Design artifacts**: Reference design documents from artifacts

<!-- section_id: "cfb92024-501d-4ac0-b045-092cbf7e120c" -->
## Deeper References

For comprehensive understanding of development patterns:

- **Architecture**: [../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md](../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md)
- **Tools and Context**: [../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md](../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md)
- **Parallel Execution**: [../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md](../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md)
- **Handoff Schema**: [../../../0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md](../../../0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md)

<!-- section_id: "dae0f571-11f8-4d6d-87b1-a084268ea6b4" -->
## Best Practices

1. **Follow Design**: Implement exactly as designed, document deviations
2. **Fresh Sessions**: Use new Codex sessions for each independent module
3. **Document As You Go**: Add inline comments and docstrings during implementation
4. **Handle Errors**: Implement comprehensive error handling and validation
5. **Think About Tests**: Structure code to be testable (inject dependencies, pure functions)
6. **Report Accurately**: List all files created/modified, note any issues
7. **Flag Blockers Early**: If stuck on design issue, report immediately rather than guessing

<!-- section_id: "d5928ed7-9cf7-48a3-8e72-30e2730243b2" -->
## Common Patterns

<!-- section_id: "1b2f0cab-cdb8-4f0e-8330-0a0677a0dc18" -->
### Pattern 1: Single File Utility (Codex)
```
Session: 1 turn
Worker: Codex CLI
Output: 1 file with implementation
Example: JsonFormatter.ts
```

<!-- section_id: "c4ffd3f9-41de-4f18-b6b8-ab8c07303a9d" -->
### Pattern 2: Standard Component (Codex)
```
Session: 2-3 turns
Worker: Codex CLI
Output: Main file + types/interfaces
Example: FileTransport.ts + FileTransportOptions.ts
```

<!-- section_id: "8e830ea7-1c5e-43a6-a733-1cd0c3310bbd" -->
### Pattern 3: Complex Component (Claude Code)
```
Session: 3-5 turns
Worker: Claude Code
Output: Multiple files with intricate logic
Example: Logger.ts (plugin system, lifecycle management)
```

<!-- section_id: "a846d528-01e8-49ba-bae0-3f20b4c08fa3" -->
### Pattern 4: Multi-Component System (Manager + Workers)
```
Manager: Claude Code (orchestrates)
Workers: Mixed (Codex for simple, Claude for complex)
Output: Integrated system with multiple modules
Example: Complete logging protocol (7 files)
```
