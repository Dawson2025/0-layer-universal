---
resource_id: "ddb6965c-4d8d-4229-8eb5-637935ab2f6d"
resource_type: "skill
document"
resource_name: "SKILL"
---
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
3. **Check episodic memory**: Read `memory/episodic.md` (auto-memory topic file) for recent session history across all layers. If resuming multi-session work, also read the source `.0agnostic/episodic_memory/index.md` in the working directory for full detail.
4. **Find the `.gab.jsonld` for your role** in the current directory:
   ```bash
   find [working-directory] -maxdepth 2 -name "*.gab.jsonld" -type f | head -5
   ```
5. **Read the matching `.integration.md`** (same base name as the `.gab.jsonld`):
   - e.g., `layer_5_orchestrator.gab.jsonld` → `layer_5_orchestrator.integration.md`
   - `.integration.md` files are auto-generated summaries — do not edit directly
6. **For precise mode constraints**, query the `.gab.jsonld` via jq:
   ```bash
   jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' [matching .gab.jsonld]
   ```
7. **Check for agnostic system** in the working directory:
   - If `0AGNOSTIC.md` exists, it is the **source of truth** — edit it, not `CLAUDE.md`
   - If `.0agnostic/` exists, it contains on-demand resources (rules, skills, agents, knowledge)
   - If `.1merge/` exists, it provides tool-specific overrides (3-tier: synced → overrides → additions)
   - After modifying `0AGNOSTIC.md`, run `agnostic-sync.sh` to regenerate tool-specific files
8. **Check status.json** for current state
9. **Check applicable rules** in `.claude/rules/`

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
