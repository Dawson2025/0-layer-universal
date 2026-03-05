---
resource_id: "9935526a-ff8f-4ec5-905d-917e61597528"
resource_type: "rule"
resource_name: "AI_CONTEXT_PROPOSAL_REQUIREMENTS"
---
# AI Context Proposal Requirements

## [CRITICAL] Rule: Diagram Requirement

**ALL proposals that modify the AI context flow architecture MUST include:**

1. **Before Diagram** - Current state of AI context flow
2. **After Diagram** - Proposed state with changes
3. **Agent Workflow Diagram** - How AI agents will work with the change

**Failure to include diagrams = Proposal is incomplete and cannot proceed.**

---

## What Requires This Rule

Any proposal that involves changes to:

| Change Type | Examples |
|-------------|----------|
| Layer structure | Adding/removing/renaming layers |
| Sub-layer structure | Adding/removing sub-layers, changing hierarchy |
| Stage structure | Adding/removing stages or sub-stages |
| Context files | Modifying CLAUDE.md, 0AGNOSTIC.md structure |
| Critical rules | Adding/modifying/removing critical rules |
| Sync system | Changing how .0agnostic/ generates files |
| Navigation patterns | Changing how agents traverse the system |
| Entry points | Adding new agent entry points |

---

## Required Diagram Types

### 1. Context Flow Diagram

Shows how context cascades through the system.

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONTEXT FLOW (BEFORE)                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  layer_0/CLAUDE.md                                              │
│       │                                                         │
│       ▼                                                         │
│  layer_1/CLAUDE.md                                              │
│       │                                                         │
│       ▼                                                         │
│  [current structure...]                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    CONTEXT FLOW (AFTER)                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  layer_0/CLAUDE.md                                              │
│       │                                                         │
│       ▼                                                         │
│  layer_1/CLAUDE.md                                              │
│       │                                                         │
│       ▼                                                         │
│  [NEW: additional context point]  ← CHANGE HIGHLIGHTED          │
│       │                                                         │
│       ▼                                                         │
│  [rest of structure...]                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Critical Rules Cascade Diagram

Shows how rules inherit and accumulate.

```
┌─────────────────────────────────────────────────────────────────┐
│                    CRITICAL RULES CASCADE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  layer_0/CLAUDE.md                                              │
│  ├── CRITICAL: "Rule A"                                         │
│  ├── CRITICAL: "Rule B"                                         │
│  │                                                              │
│  └── [new_entity]/CLAUDE.md                                     │
│      ├── INHERITS: Rule A, Rule B                               │
│      └── ADDS: "NEW Rule C"  ← PROPOSED ADDITION                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3. Agent Workflow Diagram

Shows how an agent will navigate and work with the change.

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT WORKFLOW WITH CHANGE                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Agent enters: [entry point]                                 │
│  2. Loads: [context files in order]                             │
│  3. NEW STEP: [what agent does differently]  ← CHANGE           │
│  4. Follows: [rules from cascade]                               │
│  5. Outputs: [where deliverables go]                            │
│                                                                 │
│  Example session:                                               │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ > Agent: "I'm in [location]"                             │   │
│  │ > Agent: "I see NEW [thing] - loading context"           │   │
│  │ > Agent: "Following rules: [inherited + new]"            │   │
│  │ > Agent: "Creating output in [location]"                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Proposal Template with Diagrams

```markdown
# Proposal: [Name]

## Summary
[Brief description of the change]

## Motivation
[Why this change is needed]

---

## Current State (BEFORE)

### Context Flow Diagram
```
[ASCII diagram showing current context flow]
```

### Critical Rules (Current)
```
[Show current rules cascade]
```

### Current Agent Workflow
```
[Show how agents currently work]
```

---

## Proposed Change (AFTER)

### Context Flow Diagram (Proposed)
```
[ASCII diagram showing NEW context flow with changes highlighted]
```

### Critical Rules (Proposed)
```
[Show new rules cascade with additions/changes highlighted]
```

### Agent Workflow (Proposed)
```
[Show how agents will work AFTER the change]
```

---

## Impact Analysis

### Files Created/Modified
| File | Change |
|------|--------|
| [path] | [created/modified/deleted] |

### Agents Affected
| Agent Entry Point | Impact |
|-------------------|--------|
| [entry point] | [how it's affected] |

### Critical Rules Affected
| Rule | Change |
|------|--------|
| [rule] | [added/modified/removed] |

---

## Implementation Plan

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Rollback Plan

If change fails:
1. [Rollback step 1]
2. [Rollback step 2]
```

---

## Diagram Quality Requirements

### Must Include:

1. **Clear boxes/sections** for each component
2. **Arrows** showing flow direction
3. **Labels** identifying each element
4. **CHANGE MARKERS** highlighting what's new/different
5. **Layer numbers** where applicable

### Must Show:

1. **Entry points** where agents can start
2. **Context cascade** order of loading
3. **Inheritance** of rules/context
4. **Pointers** to resources
5. **Outputs** where work products go

### Format:

- Use ASCII art (works in all tools)
- Box width: ~60-70 characters
- Clear hierarchy with indentation
- Use symbols: │ ├ └ ─ ▼ ▶ →

---

## Example: Adding a Sub-Layer

### Before Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    CURRENT CONTEXT FLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  layer_0/CLAUDE.md                                              │
│       │                                                         │
│       ▼                                                         │
│  layer_0_04_sub_layers/                                         │
│  ├── sub_layer_0_01_knowledge_system/                                    │
│  ├── sub_layer_0_01_knowledge_system/                           │
│  ├── sub_layer_0_01_knowledge_system/principles/                                 │
│  └── sub_layer_0_02_rules/                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### After Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROPOSED CONTEXT FLOW                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  layer_0/CLAUDE.md                                              │
│       │                                                         │
│       ▼                                                         │
│  layer_0_04_sub_layers/                                         │
│  ├── sub_layer_0_01_knowledge_system/                                    │
│  ├── sub_layer_0_01_knowledge_system/                           │
│  ├── sub_layer_0_01_knowledge_system/principles/                                 │
│  ├── sub_layer_0_02_rules/                                      │
│  └── sub_layer_0_04b_workflows/  ← NEW SUB-LAYER                │
│       │                                                         │
│       ├── 0AGNOSTIC.md           ← Identity                     │
│       ├── CLAUDE.md              ← Tool context                 │
│       └── .claude/               ← Tool config                  │
│                                                                 │
│  NEW CRITICAL RULES:                                            │
│  ├── INHERITS: All layer_0 rules                                │
│  └── ADDS: "Workflows must have clear entry/exit points"        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Agent Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT WORKFLOW WITH NEW SUB-LAYER             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Agent sees: "workflow" in user request                      │
│  2. Trigger matches: sub_layer_0_04b_workflows                  │
│  3. Loads:                                                      │
│     a. layer_0/CLAUDE.md                                        │
│     b. sub_layer_0_04b_workflows/CLAUDE.md  ← NEW               │
│  4. Critical rules active:                                      │
│     - [layer_0 rules]                                           │
│     - "Workflows must have clear entry/exit points"  ← NEW      │
│  5. Agent works in: sub_layer_0_04b_workflows/                  │
│  6. Outputs to: sub_layer_0_04b_workflows/outputs/              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Self-Check Before Submitting Proposal

- [ ] Does proposal include BEFORE context flow diagram?
- [ ] Does proposal include AFTER context flow diagram?
- [ ] Are changes clearly highlighted in AFTER diagram?
- [ ] Does proposal show critical rules cascade?
- [ ] Does proposal include agent workflow diagram?
- [ ] Does workflow show how agent navigates the change?
- [ ] Are all affected files listed?
- [ ] Is implementation plan clear?
- [ ] Is rollback plan included?

---

*This rule applies to ALL AI context architecture proposals.*
*Proposals without diagrams will be returned for completion.*
