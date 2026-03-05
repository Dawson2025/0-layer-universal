---
resource_id: "80c3bd9c-c522-40b9-9c58-e72a625edd1f"
resource_type: "document"
resource_name: "INSTRUCTIONS_CONTEXT_GATHERING_SYSTEM.sync-conflict-20260126-035816-IF2WOGZ"
---
# INSTRUCTIONS: Context Gathering System

**Created:** 2026-01-15
**Status:** Instructions Complete
**Purpose:** Define how AI agents gather relevant context within the layer-stage system

---

<!-- section_id: "80677b5d-43d8-4e93-b1a2-187fd383c421" -->
## 1. Overview

The context gathering system determines:
- What context is always relevant (vertical chain)
- What context is conditionally relevant (horizontal siblings)
- How to identify tasks that need context
- How to traverse the init prompt chain

---

<!-- section_id: "d1095c84-c670-43ab-bfac-ce6666a27107" -->
## 2. Core Principle

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   VERTICAL CHAIN = ALWAYS RELEVANT                                          │
│   HORIZONTAL SIBLINGS = ONLY WHEN TASK-RELEVANT                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "b6312239-0599-4e33-814e-a794c4b7f1a2" -->
## 3. Vertical Chain (Always Relevant)

The vertical chain consists of **ancestors** and **descendants** of the current entity.

<!-- section_id: "59a5dd8a-d806-4ca8-abe6-c1a85e07575b" -->
### 3.1 Diagram

```
                    ┌─────────────────────┐
                    │  0_layer_universal  │  ← ANCESTOR (always relevant)
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  layer_1_project_   │  ← ANCESTOR (always relevant)
                    │       school        │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  layer_2_feature_   │  ← CURRENT ENTITY
                    │       math          │     (YOU ARE HERE)
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
     ┌────────▼───────┐ ┌──────▼──────┐ ┌──────▼──────┐
     │ layer_3_comp_  │ │ layer_3_    │ │ layer_3_    │  ← DESCENDANTS
     │   algebra      │ │ comp_calc   │ │ comp_geo    │    (always relevant)
     └────────────────┘ └─────────────┘ └─────────────┘
```

<!-- section_id: "025930c3-150e-49b0-84e5-b77fbfc63d24" -->
### 3.2 What to Gather from Ancestors

| Ancestor Level | What to Gather |
|----------------|----------------|
| **Universal (Layer 0)** | Framework rules, universal principles, global init prompt |
| **Project (Layer 1)** | Project-specific rules, context, conventions |
| **Feature (Layer 2)** | Feature-specific context, current stage status |

<!-- section_id: "7e35a95e-97d7-4a03-80eb-a248c7facf8d" -->
### 3.3 What to Gather from Descendants

| Descendant Type | What to Gather |
|-----------------|----------------|
| **Sub-projects** | Status, dependencies, blockers |
| **Features** | Status, relationships to current work |
| **Components** | Status, if relevant to current task |

---

<!-- section_id: "4874ffe3-5d2d-4f80-961a-87523654c007" -->
## 4. Horizontal Siblings (Conditionally Relevant)

Horizontal siblings are entities at the **same level** as the current entity.

<!-- section_id: "1be22d3c-1f6a-448e-97f2-f4e34d6fe5ca" -->
### 4.1 Diagram

```
                    ┌─────────────────────┐
                    │      PARENT         │
                    └──────────┬──────────┘
                               │
       ┌───────────────────────┼───────────────────────┐
       │                       │                       │
┌──────▼──────┐         ┌──────▼──────┐         ┌──────▼──────┐
│  SIBLING A  │         │   CURRENT   │         │  SIBLING B  │
│             │ ◄─────► │   ENTITY    │ ◄─────► │             │
└─────────────┘         └─────────────┘         └─────────────┘
       │                                               │
       │              ONLY RELEVANT WHEN:              │
       │    1. Sibling is RELATED to current entity    │
       │                     AND                       │
       │    2. Relationship is RELEVANT to current     │
       │       TASK                                    │
       └───────────────────────────────────────────────┘
```

<!-- section_id: "758d977a-c333-4a50-9cc5-f88722c3dcba" -->
### 4.2 When Siblings Are Relevant

**Condition 1: Sibling is RELATED**
- Shares dependencies
- Has cross-references
- Is part of same workflow
- Is documented as related

**Condition 2: Relationship is TASK-RELEVANT**
- Current task involves the relationship
- Current task affects both entities
- Current task requires knowledge from sibling

<!-- section_id: "d2309911-8187-43ce-a2c0-b6bc6ed0bbec" -->
### 4.3 Examples

| Scenario | Sibling Relevant? | Why |
|----------|-------------------|-----|
| Working on `math` feature, `science` feature exists | ❌ No | Not related, not task-relevant |
| Working on `math` feature, `calc_helper` utility exists | ✅ Yes | Related (shared code), task-relevant (using it) |
| Working on `auth` feature, `user` feature exists | ✅ Yes | Related (auth uses user), task-relevant |
| Working on `auth` feature, `billing` feature exists | ❌ No | Not related to current auth task |

---

<!-- section_id: "0a1db86b-c65d-48f2-9db2-ced8904ff514" -->
## 5. Task Sources

Tasks that determine what context is relevant come from multiple sources:

<!-- section_id: "dcb92f5a-b222-4844-9bd2-60e07b75f6d0" -->
### 5.1 Task Source Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           TASK SOURCES                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. CURRENT USER REQUEST                                                    │
│     └─► What the user is asking right now                                   │
│                                                                             │
│  2. STATUS.JSON (in_progress)                                               │
│     └─► Tasks marked as in_progress in status files                         │
│                                                                             │
│  3. TODO LISTS (pending)                                                    │
│     └─► Pending tasks that have been set but not started                    │
│                                                                             │
│  4. HANDOFF DOCUMENTS                                                       │
│     └─► Tasks passed from previous stage or parent layer                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- section_id: "d2290169-77b0-4f29-b23a-5384824f1412" -->
### 5.2 Task Source Priority

```
1. Current User Request     ← HIGHEST PRIORITY
2. status.json (in_progress)
3. Handoff documents
4. Todo lists (pending)     ← LOWEST PRIORITY
```

<!-- section_id: "5461bd1c-cc83-4524-b39b-da3c860fc8fe" -->
### 5.3 Status.json Structure

```json
{
  "layer": 2,
  "entity": "layer_2_feature_math",
  "current_stage": "stage_2_04_development",
  "last_updated": "2026-01-15",
  "stages": {
    "stage_2_01_instructions": "completed",
    "stage_2_02_planning": "completed",
    "stage_2_03_design": "completed",
    "stage_2_04_development": "in_progress",
    "stage_2_05_testing": "not_started"
  },
  "tasks_in_progress": [
    "Implement algebra module",
    "Write unit tests for calculator"
  ],
  "blockers": [],
  "notes": "On track for completion"
}
```

---

<!-- section_id: "62e99d75-45a7-4b42-8a92-4b37f94ca552" -->
## 6. Init Prompt Chain

The init prompt chain is how context is inherited from universal down to current location.

<!-- section_id: "4a6727d4-cce8-4b67-8573-bc8d1b1b9adb" -->
### 6.1 Chain Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         INIT PROMPT CHAIN                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  0_layer_universal/                                                         │
│  └── layer_0/layer_0_00_ai_manager_system/agnostic/init_prompt.md          │
│      │                                                                      │
│      │  "You are operating in the Layer-Stage Framework..."                 │
│      │  "Always check parent layers for inherited rules..."                 │
│      │                                                                      │
│      ▼                                                                      │
│  layer_1_project_school/                                                    │
│  └── layer_1/layer_1_00_ai_manager_system/agnostic/init_prompt.md          │
│      │                                                                      │
│      │  "This is the school project..."                                     │
│      │  "Follow academic conventions..."                                    │
│      │                                                                      │
│      ▼                                                                      │
│  layer_2_feature_math/                                                      │
│  └── layer_2/layer_2_00_ai_manager_system/agnostic/init_prompt.md          │
│      │                                                                      │
│      │  "This feature handles math coursework..."                           │
│      │  "Use LaTeX for equations..."                                        │
│      │                                                                      │
│      ▼                                                                      │
│  (current working location)                                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- section_id: "6990e6f3-09d6-422e-985d-b8336b689bf0" -->
### 6.2 Init Prompt Template

```markdown
# Layer N: Entity Name

## Inherited From
- Parent: [link to parent init_prompt.md]

## Purpose
[What this entity does]

## Context Rules
[Entity-specific context rules]

## Conventions
[Entity-specific conventions]

## Children
- [link to child 1 init_prompt.md]
- [link to child 2 init_prompt.md]
```

---

<!-- section_id: "8a5ab54b-71d1-4e9b-9978-3660cf7370c5" -->
## 7. Claude Code Integration

Claude Code's hierarchical CLAUDE.md discovery aligns with our init prompt chain.

<!-- section_id: "af7b3b83-2a33-4dbc-93cf-844e6c733c80" -->
### 7.1 CLAUDE.md Discovery Order

```
1. ~/.claude/CLAUDE.md                    # User global
2. 0_layer_universal/CLAUDE.md            # Universal (Layer 0)
3. .../layer_1_project_school/CLAUDE.md   # Project (Layer 1)
4. .../layer_2_feature_math/CLAUDE.md     # Feature (Layer 2)
5. .../layer_3_component_calc/CLAUDE.md   # Component (Layer 3)
```

<!-- section_id: "b1191489-07a6-453b-9c40-b751e0a69cfa" -->
### 7.2 Inheritance Behavior

- Later CLAUDE.md files **override** earlier ones where conflicts exist
- All relevant context is **combined** automatically
- Skills, commands, agents are **inherited** from ancestors
- Child entities can **extend** parent configurations

<!-- section_id: "962e7a5d-54dd-4f24-8f32-8eea88d8cceb" -->
### 7.3 Agnostic → CLAUDE.md Relationship

```
agnostic/init_prompt.md          CLAUDE.md
        │                             │
        │    ┌─────────────────┐      │
        └───►│   GENERATES     │◄─────┘
             │   or FEEDS      │
             └─────────────────┘
                     │
                     ▼
         Tool-specific implementation
         of agnostic source
```

---

<!-- section_id: "473aa1f7-d9e3-4233-84a7-14a95715ca2f" -->
## 8. Context Gathering Algorithm

<!-- section_id: "3fec0c45-db57-4bbb-86e4-0f5837a39291" -->
### 8.1 Pseudocode

```
function gatherContext(currentEntity):
    context = {}

    # Step 1: Gather vertical chain (always)
    context.ancestors = gatherAncestors(currentEntity)
    context.descendants = gatherDescendants(currentEntity)

    # Step 2: Identify current tasks
    tasks = []
    tasks.add(currentUserRequest)
    tasks.add(getInProgressFromStatus(currentEntity))
    tasks.add(getPendingFromHandoffs(currentEntity))
    tasks.add(getPendingFromTodos(currentEntity))

    # Step 3: Check horizontal siblings (conditionally)
    siblings = getSiblings(currentEntity)
    for sibling in siblings:
        if isRelated(sibling, currentEntity):
            for task in tasks:
                if isRelevantToTask(sibling, task):
                    context.relevantSiblings.add(sibling)

    # Step 4: Load init prompt chain
    context.initPromptChain = loadInitPromptChain(currentEntity)

    return context
```

<!-- section_id: "b06e596a-919b-44ee-8096-6e0928eb5d97" -->
### 8.2 Flowchart

```
                    ┌─────────────────┐
                    │     START       │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Gather Vertical │
                    │     Chain       │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Identify Tasks  │
                    │ from all sources│
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  For each       │
                    │  Sibling:       │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
     ┌────────▼────────┐           ┌────────▼────────┐
     │  Is Related?    │           │     Skip        │
     └────────┬────────┘           └─────────────────┘
              │
              │ YES
              │
     ┌────────▼────────┐
     │ Is Relevant to  │
     │   any Task?     │
     └────────┬────────┘
              │
     ┌────────┴────────┐
     │ YES             │ NO
     │                 │
┌────▼─────┐    ┌──────▼──────┐
│ Include  │    │    Skip     │
│ in       │    │             │
│ Context  │    └─────────────┘
└──────────┘
```

---

<!-- section_id: "70ed9038-df34-4926-a1ac-b875da4daed2" -->
## 9. Implementation Notes

<!-- section_id: "2416244f-5719-41a8-b9c3-0786ac1ff500" -->
### 9.1 For Claude Code

When using Claude Code, context gathering happens automatically via:
- CLAUDE.md hierarchical discovery
- Skills that navigate the layer hierarchy
- Commands that gather specific context

<!-- section_id: "3f499188-04ed-46e9-9615-34bf6f63d9a8" -->
### 9.2 For Other AI Tools

For tools without hierarchical discovery:
- Read the init_prompt_chain manually
- Check status.json at each level
- Apply the algorithm above

<!-- section_id: "b9121e2e-513f-4981-9f76-c29779072c5e" -->
### 9.3 Tool-Agnostic Implementation

The agnostic `init_prompt.md` files should:
1. Reference their parent init_prompt
2. List their children init_prompts
3. Define entity-specific context rules
4. Be the source of truth for tool-specific files

---

<!-- section_id: "359a72f4-f7ec-403f-91b8-76c231900db9" -->
## 10. Success Criteria

- [ ] Vertical chain is always gathered
- [ ] Horizontal siblings are checked conditionally
- [ ] Task sources are all checked
- [ ] Init prompt chain is traversable
- [ ] Claude Code discovers CLAUDE.md hierarchically
- [ ] Agnostic init_prompts feed tool-specific files
- [ ] Context gathering is documented at each level

---

**Document Location:** `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0_03_instructions/hand_off_documents/INSTRUCTIONS_CONTEXT_GATHERING_SYSTEM.md`

**Last Updated:** 2026-01-15

**Related Documents:**
- `INSTRUCTIONS_LAYER_STAGE_RESTRUCTURE.md`
- `INSTRUCTIONS_LAYER_STAGE_SYSTEM_INTERNAL_STRUCTURE.md`
