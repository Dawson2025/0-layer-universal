---
paths: layer_-1_research/**
---

# Research Context

## Required Reading

When working in research directories:
1. Find the `.gab.jsonld` for your role (e.g., `agent_orchestrator.gab.jsonld`)
2. Read the matching `.integration.md` (same base name, e.g., `agent_orchestrator.integration.md`)
3. For precise mode constraints, query the `.gab.jsonld` via jq:
   ```
   jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' [matching .gab.jsonld]
   ```
4. Read `.claude/skills/*/SKILL.md` — check WHEN/WHEN NOT conditions

## Skill Usage

| Situation | Skill | When |
|-----------|-------|------|
| Starting research | `/context-gathering` | First action — identify layer, stage, project |
| Following research stages | `/stage-workflow` | When stage transitions are needed |
| Creating research entities | `/entity-creation` | When new features/sub-features needed |
| Ending session | `/handoff-creation` | Before closing, to preserve research state |

## Research-Specific Rules

- Always include a **Sources:** section with any research output
- Use Perplexity, WebSearch, or WebFetch for facts — do not assume
- Document findings in the correct stage directory (`stage_*_02_research/outputs/`)
- Research content belongs in `layer_-1_research/`, NOT in `layer_0/` or `layer_1/`
- Follow the output-first protocol: produce deliverables, not just notes
