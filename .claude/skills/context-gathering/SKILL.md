---
name: context-gathering
description: "Gather context about current position in the layer-stage hierarchy. Use when entering a new directory, starting a task, or needing to understand project structure. Reads CLAUDE.md chain, identifies layer/stage, loads relevant rules and AALang definitions."
---

# Context Gathering Skill

## WHEN to Use
- **First action** when entering any directory in the layer-stage system
- When starting work on a new task and you don't know the current layer/stage
- When the user asks about current context, project structure, or "where am I?"
- When you need to understand what rules, skills, or agents apply here
- After being spawned as a child agent (you have no inherited context)

## WHEN NOT to Use
- You already read the CLAUDE.md chain for this directory this session
- You're doing a simple edit where the layer/stage is already known
- The user explicitly said to skip context loading

## Steps

1. **Read CLAUDE.md chain**: Starting from the working directory, read each CLAUDE.md up to root
2. **Identify layer and stage**: Determine current layer (0, 1, -1) and stage (01-11)
3. **Check for AALang agent definitions**: Look for nearest `.gab.jsonld` file
   ```bash
   find [working-directory] -maxdepth 2 -name "*.gab.jsonld" -type f | head -5
   ```
4. **Read agent graph index** (if found):
   ```bash
   jq '."@graph"[] | {id: ."@id", type: ."@type", purpose: .purpose} | select(.purpose != null)' [file.jsonld]
   ```
5. **Read .integration.md** (if it exists next to the .gab.jsonld)
6. **Check status.json** for current state
7. **Check applicable rules** in `.claude/rules/`

## Output Format

Provide a summary including:
- Current layer position (layer_0, layer_1, layer_-1)
- Current stage (01-11) if applicable
- Relevant ancestor context from CLAUDE.md chain
- Active agent definition (from .gab.jsonld if found)
- Available skills for this context
- Active tasks or goals (from status.json)

## AALang Reference

This skill maps to the context loading agent defined at:
`layer_0/layer_0_03_context_agents/context_loading.gab.jsonld`

The context loading agent uses a 4-mode-13-actor pattern for systematic context traversal.
