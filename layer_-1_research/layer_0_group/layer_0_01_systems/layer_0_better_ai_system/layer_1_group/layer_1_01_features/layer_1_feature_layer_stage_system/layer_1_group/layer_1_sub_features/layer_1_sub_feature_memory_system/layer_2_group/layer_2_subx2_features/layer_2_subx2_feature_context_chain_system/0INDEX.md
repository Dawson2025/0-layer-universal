---
resource_id: "c82ce4da-d7b6-45e5-ab9d-c67c34107be3"
resource_type: "index
document"
resource_name: "0INDEX"
---
# Context Chain System — Manager Dashboard

## Entity Status
**Phase**: active research and development
**Last Updated**: 2026-02-22

## Stage Summary

| # | Stage | Status | Key Output | Files | Updated |
|---|-------|--------|-----------|-------|---------|
| 01 | request_gathering | active | Tree of needs: 1 root, 3 branches, 9 leaf needs (added need_03_auto_discovery) | 22+ | 2026-02-22 |
| 02 | research | active | 25+ research files + discovery gap audit, temperature model, .1merge injection | 26+ | 2026-02-22 |
| 03 | instructions | scaffolded | — | 0 | — |
| 04 | design | active | 8 design docs: chain system, avenue web, propagation chain, funnel, inheritance, source-to-avenue, sync, discovery temps | 9 | 2026-02-23 |
| 05 | planning | active | Implementation plan for .0agnostic/avenue web MVP | 2 | 2026-02-18 |
| 06 | development | active | MVP + agnostic-sync validation + user-level-sync + .1merge injection + skill discovery chain | 10+ | 2026-02-22 |
| 07 | testing | active | 76 PASS core + skill discovery chain (6 checkpoints all PASS) | 9+ | 2026-02-22 |
| 08-11 | criticism-archives | scaffolded | — | 0 | — |

**Stage reports**: each active stage has `outputs/reports/stage_report.md` — read for details.

## How Stages Connect

```
01 request_gathering ──→ Defined 8 needs in tree of needs
        │
02 research ───────────→ Investigated context chain patterns, 25+ files
        │
04 design ─────────────→ Architecture: 8 design docs (chain, funnel, inheritance, sync, temps)
        │
05 planning ───────────→ MVP-first implementation plan
        │
06 development ────────→ Built .0agnostic/ structure, all 8 avenues
        │
07 testing ────────────→ Validated: 76 PASS, 0 FAIL
```

Stages 01 and 02 ran in parallel (research informed requirements and vice versa). Stages 04→05→06→07 were sequential.

## Current Focus

- **Skill discovery chain**: End-to-end propagation from .0agnostic/ content → 0AGNOSTIC.md → agnostic-sync → .1merge → CLAUDE.md → agent discovery — proven working with /perplexity-extract skill
- **Context chain extension**: user-level-sync.sh extends chain beyond repo to ~/.0agnostic/ for system-wide context
- **Discovery temperature model**: Hot (CLAUDE.md) → Warm (path rules) → Cold (dynamic rules, skills) — validated empirically
- **agnostic-sync validation**: New quality gate warns when .0agnostic/ content isn't referenced in 0AGNOSTIC.md

## Children

| Sub-Feature | Purpose | Status |
|-------------|---------|--------|
| chain_visualization | Visual diagrams of context chain flows | scaffolded |
| context_loading | How context is loaded at runtime | scaffolded |

**Location**: `layer_3_group/layer_3_subx3_features/`

## Quick Access

| Content | Location |
|---------|----------|
| Entity source of truth | `0AGNOSTIC.md` |
| Knowledge base | `.0agnostic/knowledge/` (4 docs, 5 principles) |
| Rules | `.0agnostic/rules/` (5 static, 4 dynamic) |
| Protocols | `.0agnostic/protocols/` (4 + stage_report_protocol) |
| Skills | `.0agnostic/skills/` (chain-validate, avenue-check) |
| Orchestrator | `layer_2_orchestrator.gab.jsonld` + `.integration.md` |
| Stage directories | `layer_2_group/layer_2_99_stages/stage_2_*` |

## Delegation

To work on a specific stage, spawn a stage agent:
```
Task tool → subagent_type: general-purpose
prompt: "Work on stage_2_XX_[name] for the context chain system.
         Read 0AGNOSTIC.md in that stage directory first."
```
The stage agent has its own 0AGNOSTIC.md with operational knowledge for that stage.
Read the stage's `outputs/reports/stage_report.md` for current status before delegating.
