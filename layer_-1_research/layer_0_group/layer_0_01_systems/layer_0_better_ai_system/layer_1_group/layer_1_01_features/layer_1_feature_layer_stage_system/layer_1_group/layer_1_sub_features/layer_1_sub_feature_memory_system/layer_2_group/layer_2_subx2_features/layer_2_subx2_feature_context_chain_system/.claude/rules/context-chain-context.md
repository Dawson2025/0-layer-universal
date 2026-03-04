---
paths: layer_2_subx2_feature_context_chain_system/**
---

# Context Chain System Context

## Required Reading

When working in context_chain_system directories:
1. Read `0AGNOSTIC.md` — entity identity, parent reference, triggers
2. Read `.gab.jsonld` + `.integration.md` — agent modes and constraints
3. Read `.0agnostic/rules/` — context_traversal, avenue_redundancy, chain_integrity

## Skill Usage

| Situation | Skill | When |
|-----------|-------|------|
| Validating parent chain | `/chain-validate` | Before modifying parents, after creating entities |
| Checking avenue coverage | `/avenue-check` | After creating entities, during audits |

## Context Chain Rules

Three rules govern this system (in `.0agnostic/rules/`):

- **context_traversal.md** — Traverse the full 7-level parent chain before working
- **avenue_redundancy.md** — Every context item must be reachable via 3+ avenues
- **chain_integrity.md** — Never break a parent reference in 0AGNOSTIC.md

## Agnostic System

- **Source of truth**: `0AGNOSTIC.md` — edit this, NOT `CLAUDE.md`
- **On-demand resources**: `.0agnostic/` contains rules, skills, episodic memory
- **After changes**: Run `agnostic-sync.sh` to regenerate tool-specific files
