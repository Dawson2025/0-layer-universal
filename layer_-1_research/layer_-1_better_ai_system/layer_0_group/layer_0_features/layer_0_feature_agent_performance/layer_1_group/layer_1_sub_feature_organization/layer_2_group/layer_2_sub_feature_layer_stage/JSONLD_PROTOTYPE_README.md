# JSON-LD Navigation System Prototype

## Overview

This prototype demonstrates how JSON-LD files can provide machine-readable navigation, triggers, and pointers throughout the layer-stage hierarchy.

---

## Files Created

```
layer_0_feature_better_layer_stage_system/
├── index.jsonld                          ← Root navigation for the feature
├── JSONLD_PROTOTYPE_README.md            ← This file
├── .claude/
│   ├── schema/
│   │   └── layer-stage-schema.jsonld     ← Vocabulary definitions
│   └── skills/
│       └── index.jsonld                  ← Skills index as linked data
├── layer_0_group/
│   ├── index.jsonld                      ← Layer 0 group navigation
│   └── layer_0_99_stages/
│       ├── index.jsonld                  ← All 11 stages indexed
│       └── stage_0_01_request_gathering/
│           ├── index.jsonld              ← Stage navigation
│           └── outputs/requests/tree_of_needs/
│               └── index.jsonld          ← Needs as linked data
└── layer_1_group/
    └── index.jsonld                      ← Layer 1 group navigation
```

---

## Key Concepts

### 1. Navigation (`nav:`)

```json
"nav:parent": {"@id": "../", "name": "parent_entity"},
"nav:children": [{"@id": "child/", "@type": "..."}],
"nav:skills": {"@id": ".claude/skills/"},
"nav:treeOfNeeds": {"@id": "outputs/requests/tree_of_needs/"}
```

Agents can follow `@id` links to traverse the hierarchy without parsing markdown.

### 2. Triggers (`trigger:`)

```json
"trigger:onSessionStart": [
  {"action": "read", "target": "CLAUDE.md"},
  {"action": "read", "target": "index.jsonld"}
],
"trigger:skill": {"@id": ".claude/skills/01_request_gathering-workflow/"}
```

Agents know what to load and when based on structured triggers.

### 3. Relationships (`rel:`)

```json
"rel:satisfiesNeed": {"@id": "path/to/need/"},
"rel:siblings": [{"@id": "../sibling/", "relationship": "related"}],
"rel:informsFurtherLayering": {"pattern": {"branch": "+1", "need": "+2"}}
```

Entities are linked to what they satisfy and relate to.

---

## How Agents Would Use This

### Session Start

1. Agent reads `index.jsonld` at target entity
2. Follows `trigger:onSessionStart` actions
3. Has full navigation graph available

### Finding Skills

```
index.jsonld → nav:skills → .claude/skills/index.jsonld → skills[]
```

### Traversing Hierarchy

```
index.jsonld → nav:parent/@id → ../index.jsonld
index.jsonld → nav:children[]/@id → child/index.jsonld
```

### Understanding Requirements

```
index.jsonld → nav:treeOfNeeds → tree_of_needs/index.jsonld → rootNeed.branches[]
```

### Stage Workflows

```
layer_0_99_stages/index.jsonld → stages[].trigger:skill → skill path
```

---

## Benefits Over Markdown Parsing

| Aspect | Markdown (Current) | JSON-LD (Proposed) |
|--------|-------------------|-------------------|
| Navigation | Parse text for patterns | Follow `@id` links |
| Triggers | Find "Load when..." text | Read `trigger:` properties |
| Relationships | Interpret prose | Query `rel:` links |
| Validation | Manual checking | Schema enforcement |
| Discovery | Traverse folders | Build graph from `index.jsonld` |

---

## Schema

The vocabulary is defined in `.claude/schema/layer-stage-schema.jsonld`:

- **Types**: Feature, LayerGroup, Stage, TreeOfNeeds, SkillsIndex
- **Navigation**: `nav:parent`, `nav:children`, `nav:skills`, `nav:stages`, `nav:previous`, `nav:next`
- **Triggers**: `trigger:onSessionStart`, `trigger:onEnter`, `trigger:skill`, `trigger:when`
- **Relationships**: `rel:satisfiesNeed`, `rel:siblings`, `rel:mapsTo`, `rel:informsFurtherLayering`

---

## Next Steps

1. **Validate**: Test agent navigation using these files
2. **Extend**: Add index.jsonld to other features
3. **Tool Support**: Create tool to generate/validate index.jsonld
4. **CLAUDE.md Integration**: Optionally generate CLAUDE.md from index.jsonld

---

## Version

- **Prototype Version**: 1.0.0
- **Created**: 2026-02-04
