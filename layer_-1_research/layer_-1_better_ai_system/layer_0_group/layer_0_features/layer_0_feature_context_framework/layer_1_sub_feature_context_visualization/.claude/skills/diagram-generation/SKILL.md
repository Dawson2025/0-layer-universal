# Diagram Generation Skill

## Purpose

Generate and update context visualization diagrams for proposals and documentation.

## When to Use

1. **Creating a proposal** that affects context flow
2. **Debugging context issues** - visualize current state
3. **Documenting changes** - update diagrams after implementation
4. **Comparing before/after** - show impact of changes

## Diagram Types

### 1. Context Architecture Diagram

Shows **what** context exists and **where** it lives.

```
Template:
┌───────────────────────────────────────────────────────────────┐
│                    CONTEXT ARCHITECTURE                        │
│                    [Current/Proposed State]                    │
└───────────────────────────────────────────────────────────────┘

┌────────────────────────┬────────────────────────┐
│    STATIC CONTEXT      │    DYNAMIC CONTEXT     │
├────────────────────────┼────────────────────────┤
│                        │                        │
│  [List static sources] │  [List dynamic sources]│
│                        │                        │
└────────────────────────┴────────────────────────┘
```

### 2. Context Flow Diagram

Shows **when** context loads and **in what order**.

```
Template:
┌───────────────────────────────────────────────────────────────┐
│                      CONTEXT FLOW                              │
│                    [Current/Proposed State]                    │
└───────────────────────────────────────────────────────────────┘

                         SESSION START
                              │
                              ▼
┌───────────────────────────────────────────────────────────────┐
│ PHASE 1: [Phase Name]                                          │
│ ═════════════════════                                          │
│                                                                │
│ [Description of what happens]                                  │
│                                                                │
│ Status: [✅ Works / ⚠️ Inconsistent / ❌ Missing]              │
└───────────────────────────────────────────────────────────────┘
                              │
                              ▼
                         [Next Phase]
```

### 3. Context Propagation Diagram

Shows **how** context moves through hierarchy.

```
Template:
┌───────────────────────────────────────────────────────────────┐
│                   CONTEXT PROPAGATION                          │
│                    [Current/Proposed State]                    │
└───────────────────────────────────────────────────────────────┘

                    ┌─────────────────┐
                    │     Parent      │
                    │                 │
                    │ DEFINES:        │
                    │ • [what]        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Child       │
                    │                 │
                    │ INHERITS:       │
                    │ • [what] ✅/⚠️  │
                    └─────────────────┘
```

### 4. Before/After Comparison Diagram

Shows **impact** of proposed changes.

```
Template:
┌───────────────────────────────────────────────────────────────┐
│                    [CHANGE DESCRIPTION]                        │
└───────────────────────────────────────────────────────────────┘

         BEFORE                              AFTER
         ══════                              ═════

┌─────────────────────────┐    ┌─────────────────────────┐
│                         │    │                         │
│  [Current state]        │    │  [Proposed state]       │
│                         │    │                         │
│  Status: ❌             │    │  Status: ✅             │
│                         │    │                         │
└─────────────────────────┘    └─────────────────────────┘

WHY IT CHANGES:
┌─────────────────────────────────────────────────────────────────┐
│ • [Reason 1]                                                    │
│ • [Reason 2]                                                    │
└─────────────────────────────────────────────────────────────────┘
```

## Generating Diagrams

### For a New Proposal

1. Create directory: `diagrams/proposed/{proposal_name}/`
2. Create `before.md` with current state diagram
3. Create `after.md` with proposed state diagram
4. Include both in proposal document

### For Current State Updates

1. Edit files in `diagrams/current/`
2. Update "Last Updated" date
3. Commit with descriptive message

## Symbols Reference

| Symbol | Meaning |
|--------|---------|
| `✅` | Works correctly |
| `⚠️` | Inconsistent or partial |
| `❌` | Missing or broken |
| `───▶` | Flow direction |
| `═══` | Section header underline |
| `┌─┐` | Box corners |
| `│` | Vertical line |
| `├` | T-junction |
| `└` | Bottom corner |

## Checklist for Proposal Diagrams

Before submitting a proposal that affects context:

- [ ] Created `diagrams/proposed/{proposal_name}/` directory
- [ ] Created `before.md` showing current state
- [ ] Created `after.md` showing proposed state
- [ ] Highlighted what changes (use ❌ → ✅ pattern)
- [ ] Explained why it changes
- [ ] Updated proposal to reference diagrams

## Example: Entity Creation Before/After

```markdown
# Entity Creation Flow

## Before

Agent creates: `mkdir subfeature_automation` ❌ Wrong name

## After

1. Trigger fires: `onEntityCreation`
2. Load: `conventions.childNaming`
3. Validate: Must match `layer_{N}_{type}_{name}`
4. Create: `mkdir layer_1_sub_feature_automation` ✅ Correct
```
