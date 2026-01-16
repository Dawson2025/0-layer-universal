---
name: context-gathering
description: Use this skill when you need to understand the current location in the layer-stage hierarchy
---

# Context Gathering Skill

## When to Use
- When starting work in a new location
- When the user asks about current context
- When you need to understand project structure

## Steps
1. Read the current directory's CLAUDE.md
2. Traverse up to find parent init_prompt.md files
3. Check status files for current stage
4. Identify related siblings if needed

## Output Format
Provide a summary including:
- Current layer position
- Current stage
- Relevant ancestor context
- Active tasks or goals
