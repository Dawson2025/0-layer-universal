---
resource_id: "24117ac5-3ad3-469d-b444-5abf08a6609a"
resource_type: "readme_document"
resource_name: "README"
---
# Stage 0.04 Development - AI Agent System

<!-- section_id: "0aa5046f-5dfd-47bf-bdb5-d30e7a434003" -->
## Overview

This directory contains AI agent configuration for the **Development Stage** at Layer 0 (Universal). The development stage is responsible for implementing code, infrastructure, and documentation changes. At Layer 0, this typically means universal infrastructure, tools, protocols, or documentation that applies across all projects.

<!-- section_id: "91c7bfc2-414f-4b23-810a-78cbd3e941fa" -->
## Stage Purpose

The development stage:
- Receives design specifications from the design stage
- Implements code, configuration, and documentation
- Creates or modifies universal infrastructure
- Produces artifacts ready for testing
- Reports implementation details and any deviations from design

<!-- section_id: "39871796-a2a0-401d-9817-19f8139e39d9" -->
## Manager/Worker Workflow

<!-- section_id: "ff48c240-aae8-4b7c-8f49-3d2d03679484" -->
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

<!-- section_id: "2d119e5b-392f-4259-8e0c-81e5fb08e701" -->
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

<!-- section_id: "eb06fe6a-8e5e-4a28-a467-f5ce551ee4d7" -->
## Handoff Flow

<!-- section_id: "d48ed4a7-742c-4bb5-a31e-2f408a5d5ce8" -->
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

<!-- section_id: "76c9f453-15be-4bf3-bc9b-43d58ddcf034" -->
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

<!-- section_id: "0edb7fb1-ec92-4182-8bb2-f775887a2dd5" -->
## Tool Recommendations

For Layer 0 development stage:

<!-- section_id: "f2131b21-a6d2-4a35-84a5-f9e9a1dc70f9" -->
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

<!-- section_id: "3d2a9f3b-bf0d-43ea-ada9-204b58f37e71" -->
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

<!-- section_id: "0b288f36-7886-488b-aaa7-b8340816e9ec" -->
## Parallel Execution

Development stage benefits significantly from parallelization:

<!-- section_id: "6c65ca9f-c2ab-45e0-8c43-73970d7b5589" -->
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

<!-- section_id: "6f2c8207-978a-45f2-a85f-287dfbce52c3" -->
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

<!-- section_id: "485b4dfd-e009-4387-9871-9873c422043b" -->
## Context Files

Development stage benefits from comprehensive context:

- **CLAUDE.md**: Universal coding standards, architecture patterns
- **AGENTS.md**: Quick reference for common patterns
- **Design artifacts**: Reference design documents from artifacts

<!-- section_id: "28429fb6-cbde-4140-b046-525f032219de" -->
## Deeper References

For comprehensive understanding of development patterns:

- **Architecture**: [../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md](../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/architecture.md)
- **Tools and Context**: [../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md](../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/tools_and_context_systems.md)
- **Parallel Execution**: [../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md](../../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/parallel_execution.md)
- **Handoff Schema**: [../../../0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md](../../../0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md)

<!-- section_id: "3d49abd5-b6cd-49f1-88d4-c995fa0b1b23" -->
## Best Practices

1. **Follow Design**: Implement exactly as designed, document deviations
2. **Fresh Sessions**: Use new Codex sessions for each independent module
3. **Document As You Go**: Add inline comments and docstrings during implementation
4. **Handle Errors**: Implement comprehensive error handling and validation
5. **Think About Tests**: Structure code to be testable (inject dependencies, pure functions)
6. **Report Accurately**: List all files created/modified, note any issues
7. **Flag Blockers Early**: If stuck on design issue, report immediately rather than guessing

<!-- section_id: "18ca5dfe-c64d-41c8-9e40-349e2ca81337" -->
## Common Patterns

<!-- section_id: "38eca590-afe5-4462-abc9-891adc230798" -->
### Pattern 1: Single File Utility (Codex)
```
Session: 1 turn
Worker: Codex CLI
Output: 1 file with implementation
Example: JsonFormatter.ts
```

<!-- section_id: "182c70f4-15f3-42ce-b5ef-d60096246313" -->
### Pattern 2: Standard Component (Codex)
```
Session: 2-3 turns
Worker: Codex CLI
Output: Main file + types/interfaces
Example: FileTransport.ts + FileTransportOptions.ts
```

<!-- section_id: "46627d92-817a-4275-8589-e0d7848e0383" -->
### Pattern 3: Complex Component (Claude Code)
```
Session: 3-5 turns
Worker: Claude Code
Output: Multiple files with intricate logic
Example: Logger.ts (plugin system, lifecycle management)
```

<!-- section_id: "a8a0f5d6-d6e9-4407-a748-5e445f551b8d" -->
### Pattern 4: Multi-Component System (Manager + Workers)
```
Manager: Claude Code (orchestrates)
Workers: Mixed (Codex for simple, Claude for complex)
Output: Integrated system with multiple modules
Example: Complete logging protocol (7 files)
```
