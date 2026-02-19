---
paths: layer_0/layer_0_01_ai_manager_system/**
---

# AALang/GAB Integration Context

## Required Reading

When working in the AI manager system:
1. Find the `.gab.jsonld` for your role (e.g., `layer_0_orchestrator.gab.jsonld`)
2. Read the matching `.integration.md` (same base name, e.g., `layer_0_orchestrator.integration.md`)
3. For precise mode constraints, query the `.gab.jsonld` via jq:
   ```
   jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' [matching .gab.jsonld]
   ```
4. Read `.claude/skills/*/SKILL.md` — check WHEN/WHEN NOT conditions

## Key Files

| File | Purpose | When to Read |
|------|---------|--------------|
| `professor/gab.jsonld` | AALang language spec | Understanding AALang patterns |
| `professor/gab-runtime.jsonld` | Runtime spec | Understanding execution model |
| `professor/gab-formats.jsonld` | Format definitions | Creating new agents |
| `personal/layer_0_orchestrator.gab.jsonld` | Orchestrator definition | Multi-agent coordination |
| `personal/layer_0_orchestrator.integration.md` | Readable orchestrator summary | Quick reference |

## Skill Usage

| Situation | Skill | When |
|-----------|-------|------|
| Understanding AI system | `/context-gathering` | First action when entering this directory |
| Creating new agents | `/entity-creation` | Follow GAB format from professor/ |
| Stage-based AI work | `/stage-workflow` | When working through AI system stages |

## Agnostic System

- **Source of truth**: `0AGNOSTIC.md` is the source — edit this, NOT `CLAUDE.md` (which is auto-generated)
- **On-demand resources**: `.0agnostic/` contains rules, skills, agents, knowledge, scripts
- **After changes**: Run `agnostic-sync.sh` to regenerate tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md)
- **Tool overrides**: `.1merge/` (if present) provides tool-specific overrides via 3-tier merge (synced → overrides → additions)

## AALang Conventions

- JSON-LD files are the **source of truth** for agent definitions
- `.integration.md` files are **auto-generated** — do not edit directly
- Use jq to navigate JSON-LD graphs selectively (2-5% of file)
- The professor submodule is upstream — work on the `dawson` branch
- Mode-Actor pattern: modes define WHAT to do, actors define WHO does it

## Episodic Memory

- **Session start**: Check `memory/episodic.md` (auto-memory topic file) for recent session history across all layers
- **Session end**: Update `.0agnostic/episodic_memory/index.md` in the working directory, then run `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh`
