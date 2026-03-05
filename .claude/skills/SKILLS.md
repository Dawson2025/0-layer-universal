---
resource_id: "4f4270f5-c513-4d94-b7fb-4ac0af2283ff"
resource_type: "document"
resource_name: "SKILLS"
---
# Skills Index (Claude Code)

## Purpose

Skills provide task-specific instructions with references to knowledge. Load the relevant skill before executing a task.

---

## Available Skills

| Skill | Trigger | Folder |
|-------|---------|--------|
| entity-creation | Creating layers, stages, features, projects | `entity-creation/` |
| context-gathering | Understanding current location in hierarchy | `context-gathering/` |
| handoff-creation | Creating handoff documents | `handoff-creation/` |
| stage-workflow | Working through stages | `stage-workflow/` |
| perplexity-extract | Extracting content + citations from Perplexity search pages | `perplexity-extract/` |

---

## How to Use Skills

1. Identify the task
2. Load the skill folder
3. Read `SKILL.md` for instructions
4. Read files in `references/` or follow reference paths to knowledge docs
5. Execute following the skill protocol

---

## Skill Structure

```
skill-name/
├── SKILL.md              ← Instructions and protocol
└── references/           ← Pointers to knowledge docs
```

---

## Knowledge Locations

Skills reference knowledge in:
- `layer_0/layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/` - Domain knowledge
- `layer_0/layer_0_04_sub_layers/sub_layer_0_02_rules/` - Universal rules

---

*Synced from .0agnostic/skills/ - edit source there*
