# Proposal: JSON-LD Navigation System

## Metadata

| Field | Value |
|-------|-------|
| **Proposal ID** | PROP-2026-02-03-JSONLD |
| **Status** | Prototype Created |
| **Prototype** | `layer_0_group/layer_0_features/layer_0_feature_better_layer_stage_system/` |
| **Created** | 2026-02-03 |
| **Author** | Session collaboration |
| **Tree of Needs Branch** | 02_knowledge_accessible |

---

## Problem Statement

Currently, AI agents navigate the layer-stage system by:
1. Reading CLAUDE.md files (markdown)
2. Parsing text to find pointers ("Load skills from .claude/skills/")
3. Following folder conventions
4. Inferring relationships from naming patterns

**Issues:**
- Text parsing is fragile and inconsistent
- Triggers are embedded in prose, easy to miss
- Relationships between entities aren't explicit
- No machine-readable graph of the system
- Agents can't programmatically discover connections

---

## Proposed Solution

**Use JSON-LD files to provide structured, machine-readable navigation, triggers, and pointers.**

JSON-LD (JSON for Linked Data) provides:
- `@id` for unique identifiers and links
- `@type` for entity classification
- `@context` for vocabulary definitions
- Standard format agents can parse reliably

---

## Architecture

### File Placement

```
entity/
├── index.jsonld              ← Primary navigation file
├── CLAUDE.md                 ← Human-readable (could be generated)
├── .claude/
│   ├── skills/
│   │   ├── index.jsonld      ← Skills navigation
│   │   └── entity-creation/
│   │       └── index.jsonld  ← Skill-specific links
├── layer_X_group/
│   ├── index.jsonld          ← Group navigation
│   └── layer_X_features/
│       └── index.jsonld      ← Features index
└── layer_X_99_stages/
    ├── index.jsonld          ← Stages navigation
    └── stage_X_01_.../
        └── index.jsonld      ← Stage-specific links
```

### Schema Vocabulary

```
Namespace: https://layer-stage.dev/schema#

Prefixes:
  nav:      Navigation links
  trigger:  Conditional actions
  meta:     Metadata
  rel:      Relationships
```

---

## JSON-LD Structure

### 1. Entity Index (index.jsonld)

```jsonld
{
  "@context": {
    "@vocab": "https://layer-stage.dev/schema#",
    "nav": "https://layer-stage.dev/nav#",
    "trigger": "https://layer-stage.dev/trigger#",
    "rel": "https://layer-stage.dev/rel#",
    "meta": "https://layer-stage.dev/meta#"
  },

  "@id": ".",
  "@type": "Feature",

  "meta:name": "better_layer_stage_system",
  "meta:layer": 0,
  "meta:description": "A consistent, navigable layer-stage system",

  "nav:parent": {"@id": "../../"},
  "nav:children": {
    "stages": {"@id": "layer_0_group/layer_0_99_stages/"},
    "features": {"@id": "layer_0_group/layer_0_features/"},
    "subLayers": {"@id": "layer_0_03_sub_layers/"}
  },

  "nav:skills": {"@id": ".claude/skills/"},
  "nav:knowledge": {"@id": "layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/"},
  "nav:treeOfNeeds": {"@id": "layer_0_group/layer_0_99_stages/stage_0_01_request_gathering/outputs/requests/tree_of_needs/"},

  "trigger:onEnter": [
    {
      "@type": "Trigger",
      "condition": "sessionStart",
      "action": "loadSkills",
      "target": {"@id": ".claude/skills/"}
    }
  ],

  "trigger:onTask": [
    {
      "@type": "Trigger",
      "condition": "creatingEntity",
      "action": "loadSkill",
      "target": {"@id": ".claude/skills/entity-creation/"}
    },
    {
      "@type": "Trigger",
      "condition": "workingWithStages",
      "action": "loadSkill",
      "target": {"@id": ".claude/skills/stage-workflow/"}
    }
  ],

  "rel:satisfiesNeed": {"@id": "../../layer_-1_group/layer_-1_99_stages/stage_-1_01_request_gathering/outputs/requests/tree_of_needs/00_seamless_ai_collaboration/01_capable/need_03_discoverable/"},

  "rel:siblings": [
    {"@id": "../layer_0_feature_ai_context_system/"},
    {"@id": "../layer_0_feature_ai_manager_hierarchy_system/"}
  ]
}
```

### 2. Skills Index (.claude/skills/index.jsonld)

```jsonld
{
  "@context": {
    "@vocab": "https://layer-stage.dev/schema#",
    "nav": "https://layer-stage.dev/nav#",
    "skill": "https://layer-stage.dev/skill#"
  },

  "@id": ".",
  "@type": "SkillsIndex",

  "nav:parent": {"@id": "../../"},

  "skill:available": [
    {
      "@id": "entity-creation/",
      "@type": "Skill",
      "skill:name": "entity-creation",
      "skill:trigger": "creatingEntity",
      "skill:references": [
        {"@id": "../../../../layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/layer_stage_system/STAGES_EXPLAINED.md"}
      ]
    },
    {
      "@id": "stage-workflow/",
      "@type": "Skill",
      "skill:name": "stage-workflow",
      "skill:trigger": "workingWithStages",
      "skill:references": [
        {"@id": "../../../../layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/layer_stage_system/STAGES_EXPLAINED.md"}
      ]
    },
    {
      "@id": "context-gathering/",
      "@type": "Skill",
      "skill:name": "context-gathering",
      "skill:trigger": "needingContext",
      "skill:references": []
    }
  ]
}
```

### 3. Stages Index (layer_X_99_stages/index.jsonld)

```jsonld
{
  "@context": {
    "@vocab": "https://layer-stage.dev/schema#",
    "nav": "https://layer-stage.dev/nav#",
    "stage": "https://layer-stage.dev/stage#"
  },

  "@id": ".",
  "@type": "StagesManager",

  "nav:parent": {"@id": "../"},

  "stage:all": [
    {"@id": "stage_0_01_request_gathering/", "stage:number": 1, "stage:name": "request_gathering"},
    {"@id": "stage_0_02_research/", "stage:number": 2, "stage:name": "research"},
    {"@id": "stage_0_03_instructions/", "stage:number": 3, "stage:name": "instructions"},
    {"@id": "stage_0_04_planning/", "stage:number": 4, "stage:name": "planning"},
    {"@id": "stage_0_05_design/", "stage:number": 5, "stage:name": "design"},
    {"@id": "stage_0_06_development/", "stage:number": 6, "stage:name": "development"},
    {"@id": "stage_0_07_testing/", "stage:number": 7, "stage:name": "testing"},
    {"@id": "stage_0_08_criticism/", "stage:number": 8, "stage:name": "criticism"},
    {"@id": "stage_0_09_fixing/", "stage:number": 9, "stage:name": "fixing"},
    {"@id": "stage_0_10_current_product/", "stage:number": 10, "stage:name": "current_product"},
    {"@id": "stage_0_11_archives/", "stage:number": 11, "stage:name": "archives"}
  ],

  "stage:workflow": {
    "stage_0_01_request_gathering": {"next": "stage_0_02_research"},
    "stage_0_02_research": {"next": "stage_0_03_instructions", "prev": "stage_0_01_request_gathering"},
    "stage_0_03_instructions": {"next": "stage_0_04_planning", "prev": "stage_0_02_research"}
  }
}
```

### 4. Tree of Needs Index (tree_of_needs/index.jsonld)

```jsonld
{
  "@context": {
    "@vocab": "https://layer-stage.dev/schema#",
    "nav": "https://layer-stage.dev/nav#",
    "need": "https://layer-stage.dev/need#",
    "rel": "https://layer-stage.dev/rel#"
  },

  "@id": ".",
  "@type": "TreeOfNeeds",

  "nav:parent": {"@id": "../"},

  "need:root": {
    "@id": "00_better_layer_stage_system/",
    "@type": "RootNeed",
    "need:name": "better_layer_stage_system",
    "need:question": "How do we make a consistent, navigable layer-stage system?",

    "need:branches": [
      {
        "@id": "00_better_layer_stage_system/01_consistent_structure/",
        "@type": "Branch",
        "need:name": "consistent_structure",
        "need:question": "Is structure predictable?",
        "rel:becomesEntity": {"@id": "../../../../layer_0_features/layer_1_feature_consistent_structure/"},

        "need:children": [
          {
            "@id": "00_better_layer_stage_system/01_consistent_structure/need_01_all_stages_exist/",
            "need:name": "all_stages_exist",
            "rel:becomesEntity": {"@id": "../../../../../layer_0_features/layer_1_feature_consistent_structure/layer_2_components/layer_2_component_stage_completeness/"}
          }
        ]
      },
      {
        "@id": "00_better_layer_stage_system/02_knowledge_accessible/",
        "@type": "Branch",
        "need:name": "knowledge_accessible",
        "need:question": "Can agents find knowledge?",
        "rel:becomesEntity": {"@id": "../../../../layer_0_features/layer_1_feature_knowledge_accessible/"}
      }
    ]
  }
}
```

---

## Agent Workflow

### Current (Markdown Parsing)

```
1. Agent enters directory
2. Reads CLAUDE.md
3. Parses markdown looking for patterns
4. Finds "Load skills from .claude/skills/"
5. Navigates to that path
6. Reads SKILLS.md
7. Parses more markdown
8. Eventually finds what it needs
```

### Proposed (JSON-LD Navigation)

```
1. Agent enters directory
2. Reads index.jsonld
3. Parses JSON (reliable, standard)
4. Checks trigger:onEnter
5. Follows nav:skills @id link
6. Reads skills/index.jsonld
7. Gets structured list of skills
8. Follows skill:references @id links to knowledge
```

---

## Benefits

| Benefit | Description |
|---------|-------------|
| **Reliable parsing** | JSON is unambiguous, unlike markdown |
| **Explicit relationships** | `@id` links are machine-readable |
| **Discoverable** | Agents can crawl and build a graph |
| **Validatable** | JSON Schema can enforce structure |
| **Tool-agnostic** | Any AI tool can parse JSON-LD |
| **Standard format** | JSON-LD is a W3C standard |
| **Semantic meaning** | `@type` and vocabulary give context |

---

## Compatibility with Current System

### Coexistence Strategy

```
entity/
├── index.jsonld      ← Machine navigation (new)
├── CLAUDE.md         ← Human readable (keep, could be generated)
├── 0INDEX.md         ← Human navigation (keep, could be generated)
```

**Option A: Dual maintenance**
- Keep both, update in parallel

**Option B: Generate markdown from JSON-LD**
- index.jsonld is source of truth
- CLAUDE.md and 0INDEX.md are generated

**Option C: Gradual migration**
- Add index.jsonld alongside existing
- Agents prefer JSON-LD when available
- Fall back to markdown parsing

---

## Propagation Chain with JSON-LD

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROPAGATION CHAIN (JSON-LD)                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. KNOWLEDGE (Source of truth)                                            │
│     sub_layer_0_02_knowledge_system/index.jsonld                           │
│          │                                                                  │
│          │ referenced by (rel:references)                                  │
│          ▼                                                                  │
│  2. SKILLS                                                                 │
│     .0agnostic/skills/index.jsonld                                         │
│     └── skill:references → @id to knowledge                                │
│          │                                                                  │
│          │ synced to                                                       │
│          ▼                                                                  │
│  3. TOOL-SPECIFIC                                                          │
│     .claude/skills/index.jsonld                                            │
│     .gemini/skills/index.jsonld                                            │
│          │                                                                  │
│          │ pointed to by                                                   │
│          ▼                                                                  │
│  4. ENTRY POINTS                                                           │
│     CLAUDE.md (nav:skills → .claude/skills/)                               │
│     - or -                                                                 │
│     index.jsonld at root                                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Implementation Plan

### Phase 1: Schema Definition
1. Define vocabulary at https://layer-stage.dev/schema# (or local file)
2. Create JSON Schema for validation
3. Document all terms (nav:, trigger:, rel:, etc.)

### Phase 2: Prototype
1. Create index.jsonld for `better_layer_stage_system` feature
2. Create skills/index.jsonld
3. Create stages/index.jsonld
4. Test agent navigation

### Phase 3: Tooling
1. Script to generate markdown from JSON-LD
2. Script to validate JSON-LD structure
3. Script to build navigation graph from all index.jsonld files

### Phase 4: Migration
1. Add index.jsonld to all entities
2. Update agent instructions to prefer JSON-LD
3. Optionally: generate markdown from JSON-LD

---

## Tree of Needs Mapping

| Need | How JSON-LD Addresses It |
|------|-------------------------|
| 01_capable/need_03_discoverable | Agents can crawl @id links to discover structure |
| 02_continuous/need_01_tool_portable | JSON-LD is tool-agnostic standard |
| 03_trustworthy/need_02_predictable | Schema enforces consistent structure |
| 04_observable/need_01_transparent | Relationships are explicit, not implicit |

---

## Open Questions

1. **Local vs remote context**: Should @context be a local file or hosted URL?
2. **Generation**: Should markdown be generated from JSON-LD or maintained separately?
3. **Granularity**: Should every folder have index.jsonld or only key entities?
4. **Backwards compatibility**: How do agents handle entities without index.jsonld?

---

## Next Steps

1. [ ] Review and approve proposal
2. [ ] Create schema vocabulary file
3. [ ] Prototype on one feature
4. [ ] Test with agent navigation
5. [ ] Document in instructions stage

---

## Related Documents

| Document | Path |
|----------|------|
| Propagation Chain Architecture | `stage_-1_05_design/outputs/2026-02-03_propagation_chain_architecture.md` |
| Context Flow Constraints | `stage_-1_03_instructions/outputs/2026-02-03_context_flow_constraints.md` |
| Tree of Needs | `stage_-1_01_request_gathering/outputs/requests/tree_of_needs/` |

---

## Version

- **Proposal Version**: 1.0.0
- **Created**: 2026-02-03
- **Last Updated**: 2026-02-03
