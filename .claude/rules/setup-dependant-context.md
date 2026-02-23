---
paths: .0agnostic/07+_setup_dependant/**
---

# Setup-Dependant Sub-Layer Context

## Required Reading

When working in `.0agnostic/07+_setup_dependant/` directories (OS, environment, app, AI tool sub-layers):

1. **Read the nearest `0AGNOSTIC.md`** — source of truth for identity, scope, triggers, and available resources
2. **Read `.0agnostic/02_rules/static/`** — mandatory rules that always apply at this level
3. **Check `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/`** — manifest of all available context avenues

## Specificity Chain

Sub-layers in `07+_setup_dependant/` follow an increasing-specificity pattern:
- Level 05: Operating Systems → Level 06: Environments → Level 07: Coding Apps → Level 08: Specific App → Level 09: AI Apps → Level 10: Specific AI App → Features

Each level narrows scope. Content cascades downward — a rule at level 09 applies to all level 10 entities beneath it.

## Skill Discovery

1. Check the `Triggers` section in the nearest CLAUDE.md/0AGNOSTIC.md for skill references
2. Check `.0agnostic/06_context_avenue_web/01_file_based/05_skills/` for skill registrations
3. Skills registered here are available via `/skill-name` invocation

## Available Skills in This Tree

| Skill | Scope | Trigger |
|-------|-------|---------|
| `/perplexity-extract` | Claude in Chrome (level 10 feature) | User provides a Perplexity URL |
| `/context-gathering` | All levels | Entering a new directory |
| `/entity-creation` | All levels | Creating new sub-layer entities |

## Knowledge Discovery

- `.0agnostic/01_knowledge/` — domain knowledge organized by topic
- `.0agnostic/03_protocols/` — execution workflows and procedures
- Each topic has `principles/`, `docs/`, `resources/{templates, tools/scripts}/`

## Agnostic System

- **Source of truth**: `0AGNOSTIC.md` — edit this, NOT tool files
- **On-demand**: `.0agnostic/` — read resources as needed
- **Tool adapters**: `.1merge/` — tool-specific overrides
- **Regenerate**: `agnostic-sync.sh` after editing `0AGNOSTIC.md`
