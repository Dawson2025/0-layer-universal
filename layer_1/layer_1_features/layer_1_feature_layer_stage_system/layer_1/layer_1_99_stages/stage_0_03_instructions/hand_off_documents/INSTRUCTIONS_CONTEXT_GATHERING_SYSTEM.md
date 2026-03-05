---
resource_id: "22d6f36c-4d0e-4126-86e9-73e4cf41ba52"
resource_type: "document"
resource_name: "INSTRUCTIONS_CONTEXT_GATHERING_SYSTEM"
---
# INSTRUCTIONS: Context Gathering System

**Created:** 2026-01-15
**Status:** Instructions Complete
**Purpose:** Define how AI agents gather relevant context within the layer-stage system

---

<!-- section_id: "0861815a-b5fa-4098-9090-55fff6fb8741" -->
## 1. Overview

The context gathering system determines:
- What context is always relevant (vertical chain)
- What context is conditionally relevant (horizontal siblings)
- How to identify tasks that need context
- How to traverse the init prompt chain

---

<!-- section_id: "ae39aa5e-bbae-4ba9-80bd-567734130a11" -->
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

<!-- section_id: "899e164e-270b-423f-8f54-9b6630feac23" -->
## 3. Vertical Chain (Always Relevant)

The vertical chain consists of **ancestors** and **descendants** of the current entity.

<!-- section_id: "c76f69ff-1bbc-46be-b297-79c32b19c9f6" -->
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

<!-- section_id: "a85c49e0-9363-4bce-8db0-7a3bfe7837ed" -->
### 3.2 What to Gather from Ancestors

| Ancestor Level | What to Gather |
|----------------|----------------|
| **Universal (Layer 0)** | Framework rules, universal principles, global init prompt |
| **Project (Layer 1)** | Project-specific rules, context, conventions |
| **Feature (Layer 2)** | Feature-specific context, current stage status |

<!-- section_id: "8416ad9b-9f4a-43b0-8bfd-551a279afbb1" -->
### 3.3 What to Gather from Descendants

| Descendant Type | What to Gather |
|-----------------|----------------|
| **Sub-projects** | Status, dependencies, blockers |
| **Features** | Status, relationships to current work |
| **Components** | Status, if relevant to current task |

---

<!-- section_id: "9ef7f701-c955-420c-a254-01c6f3898a0c" -->
## 4. Horizontal Siblings (Conditionally Relevant)

Horizontal siblings are entities at the **same level** as the current entity.

<!-- section_id: "afdf28cd-60f5-4ba7-a4d5-a839f080bf81" -->
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

<!-- section_id: "aaaf9c27-f500-4afe-bd64-97bfc3200e31" -->
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

<!-- section_id: "4133094d-58fe-42d3-a34d-26e94c38b3b1" -->
### 4.3 Examples

| Scenario | Sibling Relevant? | Why |
|----------|-------------------|-----|
| Working on `math` feature, `science` feature exists | ❌ No | Not related, not task-relevant |
| Working on `math` feature, `calc_helper` utility exists | ✅ Yes | Related (shared code), task-relevant (using it) |
| Working on `auth` feature, `user` feature exists | ✅ Yes | Related (auth uses user), task-relevant |
| Working on `auth` feature, `billing` feature exists | ❌ No | Not related to current auth task |

---

<!-- section_id: "e927fa6a-26b8-4fef-933d-194ee9e95d4e" -->
## 5. Task Sources

Tasks that determine what context is relevant come from multiple sources:

<!-- section_id: "09a38f95-944d-458f-91cc-32d0df3479fd" -->
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

<!-- section_id: "dd41565d-89f4-4ba3-988e-065f415dbb35" -->
### 5.2 Task Source Priority

```
1. Current User Request     ← HIGHEST PRIORITY
2. status.json (in_progress)
3. Handoff documents
4. Todo lists (pending)     ← LOWEST PRIORITY
```

<!-- section_id: "3688b595-6487-40de-9f80-21dc1a162439" -->
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

<!-- section_id: "3719f77c-8a70-491c-820c-34bce2412cac" -->
## 6. Init Prompt Chain

The init prompt chain is how context is inherited from universal down to current location.

<!-- section_id: "8806212b-f141-461b-b2cc-06183fffaa2d" -->
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

<!-- section_id: "d9911ae4-9787-4c41-9443-082ae438e48e" -->
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

<!-- section_id: "73c67cea-c461-4d1d-b1eb-989b628e217d" -->
## 7. Claude Code Integration

Claude Code's hierarchical CLAUDE.md discovery aligns with our init prompt chain.

<!-- section_id: "8156f026-79d8-4e1d-b224-d5d86569eea6" -->
### 7.1 CLAUDE.md Discovery Order

```
1. ~/.claude/CLAUDE.md                    # User global
2. 0_layer_universal/CLAUDE.md            # Universal (Layer 0)
3. .../layer_1_project_school/CLAUDE.md   # Project (Layer 1)
4. .../layer_2_feature_math/CLAUDE.md     # Feature (Layer 2)
5. .../layer_3_component_calc/CLAUDE.md   # Component (Layer 3)
```

<!-- section_id: "50d42be0-1636-444d-bc0c-8e1f68cc9cc8" -->
### 7.2 Inheritance Behavior

- Later CLAUDE.md files **override** earlier ones where conflicts exist
- All relevant context is **combined** automatically
- Skills, commands, agents are **inherited** from ancestors
- Child entities can **extend** parent configurations

<!-- section_id: "ddc694ab-3f3b-49e3-a6e2-05bd6762e473" -->
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

<!-- section_id: "e8f4148d-105b-4582-a9b5-1fc1fdd2c8e9" -->
## 8. Context Gathering Algorithm

<!-- section_id: "8d2efdc3-5f01-4839-9da0-ba2d7badff9c" -->
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

<!-- section_id: "5ba32138-6ba0-4b5e-81aa-df594606c162" -->
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

<!-- section_id: "170bad4f-0394-4af4-894a-078470801898" -->
## 9. Implementation Notes

<!-- section_id: "300e8a19-4166-4b91-938b-fb21f6d3d5d1" -->
### 9.1 For Claude Code

When using Claude Code, context gathering happens automatically via:
- CLAUDE.md hierarchical discovery
- Skills that navigate the layer hierarchy
- Commands that gather specific context

<!-- section_id: "1d372c7f-2c0c-4ce1-895e-5caf82aba44c" -->
### 9.2 For Other AI Tools

For tools without hierarchical discovery:
- Read the init_prompt_chain manually
- Check status.json at each level
- Apply the algorithm above

<!-- section_id: "3d96664b-76c3-4ba3-888b-865609853ac5" -->
### 9.3 Tool-Agnostic Implementation

The agnostic `init_prompt.md` files should:
1. Reference their parent init_prompt
2. List their children init_prompts
3. Define entity-specific context rules
4. Be the source of truth for tool-specific files

---

<!-- section_id: "02178b0e-4760-4e76-9a9c-270e6f02a608" -->
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
