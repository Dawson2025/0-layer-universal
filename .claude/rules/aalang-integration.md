---
paths: layer_0/layer_0_01_ai_manager_system/**
---

# AALang/GAB Integration Context

## Required Reading

When working in the AI manager system:
1. Read the nearest `.integration.md` for agent behavior summary
2. Navigate the JSON-LD graph via jq:
   ```
   jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' [nearest .gab.jsonld]
   ```
3. Read `.claude/skills/*/SKILL.md` — check WHEN/WHEN NOT conditions

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

## AALang Conventions

- JSON-LD files are the **source of truth** for agent definitions
- `.integration.md` files are **auto-generated** — do not edit directly
- Use jq to navigate JSON-LD graphs selectively (2-5% of file)
- The professor submodule is upstream — work on the `dawson` branch
- Mode-Actor pattern: modes define WHAT to do, actors define WHO does it
