---
paths: "**/stage_*_06_development/**"
---

# Development Stage Context

## Required Reading

When working in development stages:
1. Read the nearest `.integration.md` file for agent behavior context
2. Read the nearest `.gab.jsonld` via jq for mode constraints:
   ```
   jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' [nearest .gab.jsonld]
   ```
3. Read `.claude/skills/*/SKILL.md` — check WHEN/WHEN NOT conditions

## Skill Usage

| Situation | Skill | When |
|-----------|-------|------|
| Starting development | `/context-gathering` | Understand what's being built and prior stages |
| Stage transitions | `/stage-workflow` | When moving to testing (07) or back to design (05) |
| Creating components | `/entity-creation` | When new code modules/features needed |
| Session end | `/handoff-creation` | Preserve implementation progress |

## Development Rules

- All output goes in `outputs/` within the stage directory
- Reference design decisions from `stage_*_05_design/outputs/`
- Reference requirements from `stage_*_01_request_gathering/outputs/`
- Follow commit conventions: `[AI Context]` prefix for AI context changes
- Test before marking development complete — next stage is `stage_*_07_testing`
- Do not skip stages — if development reveals design issues, go back to stage 05
