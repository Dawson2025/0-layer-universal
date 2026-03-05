---
resource_id: "1676069e-3759-4c93-9dc5-bd395ae73a49"
resource_type: "document"
resource_name: "context-chain-context"
---
---
paths: layer_2_subx2_feature_context_chain_system/**
---

# Context Chain System Context

<!-- section_id: "9af88de3-a90c-4fa1-b3f2-a9d6e42de950" -->
## Required Reading

When working in context_chain_system directories:
1. Read `0AGNOSTIC.md` — entity identity, parent reference, triggers
2. Read `.gab.jsonld` + `.integration.md` — agent modes and constraints
3. Read `.0agnostic/rules/` — context_traversal, avenue_redundancy, chain_integrity

<!-- section_id: "71887961-fe9c-40b9-963c-fa72efd248e9" -->
## Skill Usage

| Situation | Skill | When |
|-----------|-------|------|
| Validating parent chain | `/chain-validate` | Before modifying parents, after creating entities |
| Checking avenue coverage | `/avenue-check` | After creating entities, during audits |

<!-- section_id: "fc7d96b1-740b-4f6a-8f66-cf1f0f1c57a4" -->
## Context Chain Rules

Three rules govern this system (in `.0agnostic/rules/`):

- **context_traversal.md** — Traverse the full 7-level parent chain before working
- **avenue_redundancy.md** — Every context item must be reachable via 3+ avenues
- **chain_integrity.md** — Never break a parent reference in 0AGNOSTIC.md

<!-- section_id: "865082db-2c46-40e9-b55a-a0d2372f428c" -->
## Agnostic System

- **Source of truth**: `0AGNOSTIC.md` — edit this, NOT `CLAUDE.md`
- **On-demand resources**: `.0agnostic/` contains rules, skills, episodic memory
- **After changes**: Run `agnostic-sync.sh` to regenerate tool-specific files
