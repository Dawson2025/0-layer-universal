# Context Loading Protocol

**Purpose**: Define how AI agents load and process context in the layer-stage system.

**Related Agents**: `sub_layer_0_01_context_agents/`

---

## Overview

When an AI agent starts a session in the layer-stage system, it must:

1. **Load** all relevant context files
2. **Validate** its position and completeness
3. **Propagate** inheritance and resolve overrides
4. **Deliver** confirmation that it's ready for work

This ensures agents understand where they are and what rules apply before doing any work.

---

## The 4 Phases

### Phase 1: Context Loading

**Goal**: Load all CLAUDE.md files in the chain from root to cwd.

**Loading Order**:
1. `~/.claude/CLAUDE.md` (user global settings)
2. `~/CLAUDE.md` (user root)
3. All CLAUDE.md files in path from `~` to current working directory
4. `.claude/rules/*.md` files at each project root
5. `CLAUDE.local.md` (personal overrides, gitignored)

**Track**:
- Each file loaded (path, timestamp, approximate tokens)
- Which layer each file belongs to
- Initial confidence score

**Exit Condition**: Initial confidence >= 0.6

### Phase 2: Context Validation

**Goal**: Identify current position and verify required context is loaded.

**Identify Position**:
- Current layer: -1 (research), 0 (universal), 1+ (projects)
- Current stage: 01-11 (if working in a stage)
- Current sub_layer: if nested (e.g., sub_layer_0_04_rules)

**Build Inheritance Chain**:
- What layers does current position inherit from?
- Example: Working in layer_1 → inherits from layer_0

**Check Required Context**:
- `sub_layer_0_04_rules/` must be loaded for any work
- `sub_layer_0_05_protocols/` should be loaded at session start
- Layer-specific knowledge for current layer

**Exit Condition**: Confidence >= 0.8

### Phase 3: Context Propagation

**Goal**: Resolve inheritance and apply overrides.

**Inheritance Model**:
```
Layer 0 (base) → Layer 1 (inherits, can override) → Layer 2+ (inherits, can override)
```

**Key Principles**:
- Higher-numbered layers inherit ALL context from lower layers
- Higher-numbered layers CAN override lower layers when needed
- Overrides should be explicit (use `@override` marker)
- Later files in chain override earlier (within same layer)
- `CLAUDE.local.md` has highest precedence

**Resolve Conflicts**:
1. Detect same rule defined differently in multiple layers
2. Apply precedence: higher layer wins, later in chain wins
3. Record overrides for transparency
4. Escalate unresolvable conflicts to user

**Exit Condition**: All inheritance resolved, conflicts handled

### Phase 4: Context Delivery

**Goal**: Confirm ready and present summary (if debug mode).

**If Debug Mode Enabled** (`/context-debug on`):
- Show all files loaded
- Show current position
- Show inheritance chain
- Show overrides applied
- Show confidence scores

**Ready Indicators**:
- [ ] Agent knows current layer
- [ ] Agent knows current stage (or N/A)
- [ ] Agent knows applicable rules
- [ ] Agent knows inheritance chain
- [ ] Confidence >= 0.8

**Exit Condition**: User provides a task

---

## Layer Inheritance Rules

### Base Principle

```
Layer N inherits from layers 0 through N-1
Layer N can override any inherited context
```

### Examples

**Working in Layer 1 (project)**:
- Inherits: All layer_0 rules, protocols, knowledge
- Can override: Any layer_0 context if project needs differ

**Working in Layer 2 (sub-project)**:
- Inherits: All layer_0 AND layer_1 context
- Can override: Any layer_0 or layer_1 context

**Working in Layer -1 (research)**:
- Inherits: layer_0 (universal rules still apply)
- Can override: Most things (research is experimental)
- Note: Some safety rules in layer_0 cannot be overridden

### Override Syntax

In CLAUDE.md or rule files, use:

```markdown
@override layer_0/sub_layer_0_04_rules/git_commit_rule.md
Reason: This project uses a different commit format.

[New rule content here]
```

---

## Confidence Scoring

| Factor | Weight | Description |
|--------|--------|-------------|
| Layer Identified | 0.25 | Know which layer we're in |
| Stage Identified | 0.15 | Know which stage (or N/A) |
| Rules Awareness | 0.25 | Required rules are loaded |
| Inheritance Resolved | 0.15 | Overrides are clear |
| Required Context Loaded | 0.20 | All must-have files present |

**Overall Confidence** = weighted sum of all factors

**Threshold**: >= 0.8 before starting work

---

## Debug Commands

| Command | Effect |
|---------|--------|
| `/context-debug on` | Enable full debug output |
| `/context-debug off` | Disable debug output |
| `/context-debug verbose` | Show each file as it loads |
| `/context-status` | Show current context state |

---

## Integration with CLAUDE.md

Each CLAUDE.md file should include position information:

```markdown
## AALang Integration

@agent ctx:ContextLoadingAgent

### Context Chain Position
- **Position**: 5 of 7
- **Layer**: 1 (project)
- **Parent**: ../CLAUDE.md
- **Children**: feature_a/CLAUDE.md, feature_b/CLAUDE.md
- **Inherits**: layer_0
- **Can Override**: layer_0

### On Load
Update state actors:
- ctx:ContextLoadingStateActor.loadedFiles += this
- ctx:NavigationStateActor.currentLayer = 1
- ctx:ContextConfidenceStateActor.layerIdentified = 1.0
```

---

## Related Documentation

- **Agent Definitions**: `sub_layer_0_01_ai_system/context_agents/`
- **Priority Rules**: `sub_layer_0_04_rules/context_priority_rules.md`
- **Scope Boundaries**: `sub_layer_0_04_rules/context_scope_boundaries.md`
- **Quality Checklist**: `context_quality_checklist.md`
