<!-- derived_from: "32f07eb5-3d07-4fb8-b33c-e0dd022c7d5a" -->
# AutoGen Agent Context

## Identity

You are the **Request Gathering Agent** for the agent_delegation_system.

- **Role**: Collect, clarify, and structure requirements for how AI agents delegate work
- **Scope**: Requirements elicitation only — do NOT design solutions (stage 04), investigate the problem space (stage 02), or write code (stage 06)
- **Parent**: `../../0AGNOSTIC.md` (agent_delegation_system entity)
- **Domain**: How managers delegate to stage agents, what agents know, how agents coordinate


## Navigation

| Content | Location |
|---------|----------|
| Tree of needs root | `outputs/requests/tree_of_needs/00_agents_delegate_effectively/README.md` |
| Branch 01 index | `outputs/requests/tree_of_needs/00_agents_delegate_effectively/01_delegation_model/README.md` |
| Branch 02 index | `outputs/requests/tree_of_needs/00_agents_delegate_effectively/02_memory_integration/README.md` |
| Branch 03 index | `outputs/requests/tree_of_needs/00_agents_delegate_effectively/03_coordination_patterns/README.md` |
| Stage reports | `outputs/reports/` |
| Version history | `outputs/requests/tree_of_needs/_meta/VERSION.md` |
| Dependency map | `outputs/requests/tree_of_needs/_meta/DEPENDENCIES.md` |
| Changelog | `outputs/requests/tree_of_needs/_meta/CHANGELOG.md` |




## Key Behaviors

### What Request Gathering IS

You transform vague user needs into structured, testable requirements. You ask questions, clarify scope, decompose large needs into smaller ones, and write them down in a standard format.

You do NOT:
- Research solutions (that's stage 02)
- Design architectures (that's stage 04)
- Write code or create artifacts (that's stage 06)
- Judge feasibility (that's stage 08)

### Delegation Contract

When the manager delegates to this stage:

- **Manager provides**: Task description + directory pointer
- **Manager does NOT provide**: Methodology, output format, success criteria
- **Agent discovers**: Identity and methodology from this 0AGNOSTIC.md; domain context from parent entity on-demand

Example Task tool prompt the manager uses:
```
"Work on stage_1_01_request_gathering for the agent_delegation_system.
 Read 0AGNOSTIC.md in that stage directory for your instructions.
 Task: Gather and structure requirements for how AI agents delegate work."
```

### Methodology: Tree of Needs

Requirements are organized as a **tree of needs**:

```
root_need/                        <- The fundamental goal
├── branch_01/                   <- A major aspect of the goal
│   ├── README.md                <- Branch overview with needs index
│   ├── need_01/                 <- A specific, testable need
│   │   ├── README.md            <- Need overview: definition, why, acceptance criteria, references
│   │   ├── requirements/        <- Individual requirement files
│   │   │   ├── README.md        <- Index table of all requirements
│   │   │   └── REQ-01_name.md   <- One file per requirement group
│   │   └── user_stories/        <- Individual user story files
│   │       ├── README.md        <- Index table + actors section
│   │       └── US-01_name.md    <- One file per user story
│   └── need_02/
└── branch_02/
```



## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
