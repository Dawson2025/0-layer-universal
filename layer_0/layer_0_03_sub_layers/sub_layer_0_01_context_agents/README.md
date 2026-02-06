# Context Agents

AALang agents for managing context loading in the layer-stage system.

## Overview

These agents implement a 4-phase context loading sequence that ensures AI agents understand their position and applicable rules before starting work.

## Files

| File | Purpose |
|------|---------|
| `context_loading_agent.jsonld` | Main agent definition with workflow |
| `context_state_actors.jsonld` | State tracking (loaded files, confidence, navigation, debug) |
| `context_modes.jsonld` | 4 phase definitions (Loading, Validation, Propagation, Delivery) |

## The 4 Phases

```
Phase 1: LOADING          Phase 2: VALIDATION       Phase 3: PROPAGATION      Phase 4: DELIVERY
─────────────────────     ─────────────────────     ─────────────────────     ─────────────────────
Load CLAUDE.md chain      Identify position         Resolve inheritance       Confirm ready
Load .claude/rules/       Check required files      Apply overrides           Present summary
Track loaded files        Calculate confidence      Resolve conflicts         Wait for task

Exit: confidence >= 0.6   Exit: confidence >= 0.8   Exit: resolved            Exit: user task
```

## Layer Inheritance Model

Higher-numbered layers inherit from lower layers but CAN override when necessary:

```
layer_0 (universal base)
    │
    ├── Provides default rules, protocols, knowledge
    │
    ▼
layer_1 (project)
    │
    ├── Inherits ALL of layer_0
    ├── CAN override layer_0 when project needs differ
    │
    ▼
layer_2+ (sub-projects)
    │
    ├── Inherits from all lower layers
    └── CAN override any inherited context
```

### Override Rules

1. **Higher layer wins**: Layer 1 can override Layer 0
2. **Later in chain wins**: Within same layer, later files override earlier
3. **Explicit preferred**: Use `@override` marker for clarity
4. **CLAUDE.local.md wins**: Personal overrides have highest precedence

## State Actors

### ContextLoadingStateActor
Tracks what files have been loaded, their layers, and any overrides detected.

### ContextConfidenceStateActor
Tracks confidence scores for:
- Layer identification (0.25 weight)
- Stage identification (0.15 weight)
- Rules awareness (0.25 weight)
- Inheritance resolved (0.15 weight)
- Required context loaded (0.20 weight)

Threshold: **0.8 overall confidence** required before work begins.

### NavigationStateActor
Tracks current position:
- Current layer (-1, 0, 1, 2, ...)
- Current stage (01-11, if applicable)
- Current sub_layer (if nested)
- Inheritance chain

### DebugContextStateActor
Controls debug output. Enable with `/context-debug on`.

## Usage in CLAUDE.md

Each CLAUDE.md file should include:

```markdown
## AALang Integration

@agent ctx:ContextLoadingAgent
@position layer: 1, depth: 5
@inherits layer_0
@canOverride layer_0

### On Load
- ctx:ContextLoadingStateActor.loadedFiles += this file
- ctx:NavigationStateActor.currentLayer = 1
```

## Integration with GAB

These agents inherit patterns from gab.jsonld:
- Mode-based workflow (Clarification → Discussion → Formalization → Generation)
- State actor pattern for tracking
- Confidence-gated transitions
- Quality checklists before completion

## Related Files

- `../sub_layer_0_01_ai_system/gab.jsonld` - Parent AALang specification
- `../sub_layer_0_04_rules/context_priority_rules.md` - Priority documentation
- `../sub_layer_0_05_protocols/context_loading_protocol.md` - Human-readable protocol
