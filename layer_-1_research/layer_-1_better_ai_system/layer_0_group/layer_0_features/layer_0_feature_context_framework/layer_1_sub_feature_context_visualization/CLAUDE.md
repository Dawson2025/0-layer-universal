# Context Visualization

## Identity

**Layer**: 1 (Sub-Feature)
**Parent**: layer_0_feature_context_framework
**Role**: Provide visual understanding of context flow, architecture, and propagation

## Purpose

Make context flow **visible** and **predictable** through standardized diagrams.

## Diagram Types

| Type | File | Purpose |
|------|------|---------|
| Context Architecture | `diagrams/current/context_architecture.md` | What context exists, where it lives |
| Context Flow | `diagrams/current/context_flow.md` | When context loads, in what order |
| Context Propagation | `diagrams/current/context_propagation.md` | How context moves through hierarchy |
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
