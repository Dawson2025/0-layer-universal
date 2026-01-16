---
name: entity-creation
description: Use this skill to create new projects, features, or components
---

# Entity Creation Skill

## When to Use
- When user requests a new project
- When creating a new feature
- When adding a component to existing entity

## Entity Types
- **Project**: Top-level entity in layer_1/
- **Feature**: Child of a project
- **Component**: Child of a feature

## Required Structure
```
layer_N_XX_name/
├── CLAUDE.md
├── status_N.json
├── sub_layer_N_01_prompts/
├── sub_layer_N_02_knowledge_system/
├── sub_layer_N_03_principles/
├── sub_layer_N_04_rules/
└── stage_N_00_request_gathering/
```

## Steps
1. Determine entity type and parent
2. Calculate next available number (XX)
3. Create directory structure
4. Initialize CLAUDE.md with context
5. Create initial status file
6. Update parent's children list
