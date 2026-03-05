---
resource_id: "93485aab-dc63-444f-a182-8a1d0b52b855"
resource_type: "document"
resource_name: "INSTRUCTIONS_CONTEXT_GATHERING_SYSTEM.sync-conflict-20260126-102106-IF2WOGZ"
---
# INSTRUCTIONS: Context Gathering System

**Created:** 2026-01-15
**Status:** Instructions Complete
**Purpose:** Define how AI agents gather relevant context within the layer-stage system

---

<!-- section_id: "0720316b-e3e6-4367-a703-b92a142b69c5" -->
## 1. Overview

The context gathering system determines:
- What context is always relevant (vertical chain)
- What context is conditionally relevant (horizontal siblings)
- How to identify tasks that need context
- How to traverse the init prompt chain

---

<!-- section_id: "0123d5eb-f642-4b17-8a1d-001065892258" -->
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

<!-- section_id: "fabe1fb0-d65c-4bdf-9fe7-1308459a494e" -->
## 3. Vertical Chain (Always Relevant)

The vertical chain consists of **ancestors** and **descendants** of the current entity.

<!-- section_id: "c1d97493-bdec-4c54-86c8-a035f61a044f" -->
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

<!-- section_id: "9017cc77-7983-4dd9-8ef6-ef749d324bb0" -->
### 3.2 What to Gather from Ancestors

| Ancestor Level | What to Gather |
|----------------|----------------|
| **Universal (Layer 0)** | Framework rules, universal principles, global init prompt |
| **Project (Layer 1)** | Project-specific rules, context, conventions |
| **Feature (Layer 2)** | Feature-specific context, current stage status |

<!-- section_id: "34211053-e03e-4205-a83d-5b489c8d3764" -->
### 3.3 What to Gather from Descendants

| Descendant Type | What to Gather |
|-----------------|----------------|
| **Sub-projects** | Status, dependencies, blockers |
| **Features** | Status, relationships to current work |
| **Components** | Status, if relevant to current task |

---

<!-- section_id: "c9577917-207f-4c3c-a44f-29a72d4fc8fe" -->
## 4. Horizontal Siblings (Conditionally Relevant)

Horizontal siblings are entities at the **same level** as the current entity.

<!-- section_id: "545ff047-1e9b-4fcd-8107-3715aca1567d" -->
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

<!-- section_id: "e158bf02-78e2-46f2-9953-24a406d7fe9f" -->
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

<!-- section_id: "4c6bd75a-cc7a-4bd3-8fd3-ff680e47862b" -->
### 4.3 Examples

| Scenario | Sibling Relevant? | Why |
|----------|-------------------|-----|
| Working on `math` feature, `science` feature exists | ❌ No | Not related, not task-relevant |
| Working on `math` feature, `calc_helper` utility exists | ✅ Yes | Related (shared code), task-relevant (using it) |
| Working on `auth` feature, `user` feature exists | ✅ Yes | Related (auth uses user), task-relevant |
| Working on `auth` feature, `billing` feature exists | ❌ No | Not related to current auth task |

---

<!-- section_id: "503a27eb-5aa5-429d-a3d9-130d96d83ed5" -->
## 5. Task Sources

Tasks that determine what context is relevant come from multiple sources:

<!-- section_id: "70db0024-bbe4-45c5-8587-01cac16b3f06" -->
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

<!-- section_id: "362d714b-3e8b-429f-a397-017a08085f60" -->
### 5.2 Task Source Priority

```
1. Current User Request     ← HIGHEST PRIORITY
2. status.json (in_progress)
3. Handoff documents
4. Todo lists (pending)     ← LOWEST PRIORITY
```

<!-- section_id: "9842271a-c6cb-47e7-9b91-6b7fd9d9715c" -->
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

<!-- section_id: "89e8c2f9-fc5b-44c8-aa00-a3a31708f2f7" -->
## 6. Init Prompt Chain

The init prompt chain is how context is inherited from universal down to current location.

<!-- section_id: "ef23f93c-8df1-482d-844f-4aacc9c1608b" -->
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

<!-- section_id: "8175aef3-a14c-4074-8494-e0dc823963d5" -->
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

<!-- section_id: "cddf4f42-1a33-4af4-8ccf-cd430b6f12f1" -->
## 7. Claude Code Integration

Claude Code's hierarchical CLAUDE.md discovery aligns with our init prompt chain.

<!-- section_id: "736b2b1a-11f6-4262-b6f7-ed96ef79fd6e" -->
### 7.1 CLAUDE.md Discovery Order

```
1. ~/.claude/CLAUDE.md                    # User global
2. 0_layer_universal/CLAUDE.md            # Universal (Layer 0)
3. .../layer_1_project_school/CLAUDE.md   # Project (Layer 1)
4. .../layer_2_feature_math/CLAUDE.md     # Feature (Layer 2)
5. .../layer_3_component_calc/CLAUDE.md   # Component (Layer 3)
```

<!-- section_id: "151dbd78-e042-4c69-b6e1-9375159ac2a3" -->
### 7.2 Inheritance Behavior

- Later CLAUDE.md files **override** earlier ones where conflicts exist
- All relevant context is **combined** automatically
- Skills, commands, agents are **inherited** from ancestors
- Child entities can **extend** parent configurations

<!-- section_id: "5f604f76-e2a0-4304-8bba-83083ecd8fee" -->
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

<!-- section_id: "8fc163da-8f05-47a0-a8de-e0c34e9c7eb1" -->
## 8. Context Gathering Algorithm

<!-- section_id: "a856daf9-b942-4d86-a9c0-51f4c7397775" -->
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

<!-- section_id: "26a426af-ed2b-4a14-b6b3-ea3a0dccc147" -->
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

<!-- section_id: "ed27b8ba-d70d-4b2a-9d0c-4f29242cfdca" -->
## 9. Implementation Notes

<!-- section_id: "adc3c6e2-c13e-47d4-9028-095e44a2b7fc" -->
### 9.1 For Claude Code

When using Claude Code, context gathering happens automatically via:
- CLAUDE.md hierarchical discovery
- Skills that navigate the layer hierarchy
- Commands that gather specific context

<!-- section_id: "be56fcdb-1795-4141-ae7b-d57e1a161931" -->
### 9.2 For Other AI Tools

For tools without hierarchical discovery:
- Read the init_prompt_chain manually
- Check status.json at each level
- Apply the algorithm above

<!-- section_id: "b6137a3a-8650-433a-bda1-2bc663a06ec1" -->
### 9.3 Tool-Agnostic Implementation

The agnostic `init_prompt.md` files should:
1. Reference their parent init_prompt
2. List their children init_prompts
3. Define entity-specific context rules
4. Be the source of truth for tool-specific files

---

<!-- section_id: "a289e3f4-9289-47eb-8337-c0ff2ca81372" -->
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
