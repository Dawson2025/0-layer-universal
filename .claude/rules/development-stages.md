---
paths: "**/stage_*_06_development/**"
---

# Development Stage Context

## Required Reading

When working in development stages:
1. Find the `.gab.jsonld` for your role (e.g., `layer_N_orchestrator.gab.jsonld`)
2. Read the matching `.integration.md` (same base name, e.g., `layer_N_orchestrator.integration.md`)
3. For precise mode constraints, query the `.gab.jsonld` via jq:
   ```
   jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' [matching .gab.jsonld]
   ```
4. Read `.claude/skills/*/SKILL.md` — check WHEN/WHEN NOT conditions

## Skill Usage

| Situation | Skill | When |
|-----------|-------|------|
| Starting development | `/context-gathering` | Understand what's being built and prior stages |
| Stage transitions | `/stage-workflow` | When moving to testing (07) or back to design (05) |
| Creating components | `/entity-creation` | When new code modules/features needed |
| Session end | `/handoff-creation` | Preserve implementation progress |

## Agnostic System

- **Source of truth**: `0AGNOSTIC.md` is the source — edit this, NOT `CLAUDE.md` (which is auto-generated)
- **On-demand resources**: `.0agnostic/` contains rules, skills, agents, knowledge, scripts
- **After changes**: Run `agnostic-sync.sh` to regenerate tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md)
- **Tool overrides**: `.1merge/` (if present) provides tool-specific overrides via 3-tier merge (synced → overrides → additions)

## Development Rules

- All output goes in `outputs/` within the stage directory
- Reference design decisions from `stage_*_04_design/outputs/`
- Reference requirements from `stage_*_01_request_gathering/outputs/`
- Follow commit conventions: `[AI Context]` prefix for AI context changes
- Test before marking development complete — next stage is `stage_*_07_testing`
- Do not skip stages — if development reveals design issues, go back to stage 04

## Episodic Memory

- **Session start**: Check `memory/episodic.md` (auto-memory topic file) for recent development session history
- **Session end**: Update `.0agnostic/episodic_memory/index.md` in the working stage directory, then run `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh`
