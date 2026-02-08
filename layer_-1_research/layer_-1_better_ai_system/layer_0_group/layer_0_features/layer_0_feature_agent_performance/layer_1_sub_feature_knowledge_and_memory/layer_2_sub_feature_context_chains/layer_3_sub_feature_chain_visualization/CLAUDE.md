# Context Visualization

## Identity

**Layer**: 1 (Sub-Feature)
**Parent**: layer_0_feature_context_framework
**Role**: Provide visual understanding of context flow, architecture, and propagation

## Purpose

Make context flow **visible** and **predictable** through standardized diagrams.

## Diagram Types

### Current State Diagrams

| Type | File | Purpose |
|------|------|---------|
| Context Architecture | `diagrams/current/context_architecture.md` | What context exists, where it lives |
| Context Flow | `diagrams/current/context_flow.md` | When context loads, in what order |
| Context Propagation | `diagrams/current/context_propagation.md` | How context moves through hierarchy |
| Agent Instantiation Chain | `diagrams/current/agent_instantiation_chain.md` | What agents start with and how they load more |
| Context Loading Sequence | `diagrams/current/context_loading_sequence.md` | Exact order from session start to end |

### Official vs Custom Loading

| Type | File | Purpose |
|------|------|---------|
| Official Claude Code Loading | `diagrams/current/official_claude_code_loading.md` | What Claude Code auto-loads (tool's behavior) |
| Custom Layer-Stage Loading | `diagrams/current/custom_layer_stage_loading.md` | What we've added (index.jsonld, skills, etc.) |

### Specific Operation Flows

| Type | File | Purpose |
|------|------|---------|
| Entity Creation Flow | `diagrams/current/specific_flows/entity_creation_flow.md` | How context loads for creating entities |
| Git Commit Flow | `diagrams/current/specific_flows/git_commit_flow.md` | How context loads for commits |
| Stage Workflow Flow | `diagrams/current/specific_flows/stage_workflow_flow.md` | How context loads when entering stages |

### Proposed Changes

| Type | File | Purpose |
|------|------|---------|
| Before/After | `diagrams/proposed/{name}/` | Impact of proposed changes |

## When to Use

1. **Debugging context issues** - Why didn't agent get right context?
2. **Planning improvements** - What would change if we modify flow?
3. **Onboarding** - How does the system work?
4. **Validating proposals** - Will this change have intended effect?

## Key Behaviors

- Keep diagrams updated when context system changes
- Create before/after diagrams for any context-related proposal
- Use consistent diagram format (ASCII art in markdown)

## Navigation

- **Parent**: `../` (Context Framework)
- **Siblings**: Context System, Dynamic Memory, Navigation System
- **Children**: `diagrams/`, `tools/`
