---
paths: layer_1/layer_1_projects/layer_1_project_school/**
---

# School Project Context

## Required Reading

When working in school project directories:
1. Read the nearest `.integration.md` file for agent behavior context
2. Read the nearest `.gab.jsonld` via jq for precise mode constraints:
   ```
   jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' [nearest .gab.jsonld]
   ```
3. Read `.claude/skills/*/SKILL.md` — check WHEN/WHEN NOT conditions

## Skill Usage

| Situation | Skill | When |
|-----------|-------|------|
| Starting assignment work | `/context-gathering` | Identify the class, assignment, stage |
| Following assignment stages | `/stage-workflow` | Navigate through research → planning → development |
| Creating new assignments | `/entity-creation` | Set up proper layer/stage structure |
| Ending session | `/handoff-creation` | Preserve progress for next session |

## School-Specific Rules

- Canvas integration is available via MCP tools (`mcp__canvas__*`)
- Check assignment requirements before starting work
- Follow academic writing standards — cite sources properly
- Each class is a nested layer (layer_2 sub-project → layer_3 class → layer_4+ assignments)
- Assignments have their own stage hierarchy — use all 11 stages
