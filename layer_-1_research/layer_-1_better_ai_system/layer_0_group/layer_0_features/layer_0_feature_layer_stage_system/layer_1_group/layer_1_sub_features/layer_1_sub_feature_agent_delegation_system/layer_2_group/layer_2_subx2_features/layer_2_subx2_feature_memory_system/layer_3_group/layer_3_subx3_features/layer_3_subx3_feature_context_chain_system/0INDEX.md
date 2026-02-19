# Context Chain System — Manager Dashboard

## Entity Status
**Phase**: active research and development
**Last Updated**: 2026-02-18

## Stage Summary

| # | Stage | Status | Key Output | Files | Updated |
|---|-------|--------|-----------|-------|---------|
| 01 | request_gathering | active | Tree of needs: 1 root, 3 branches, 8 leaf needs | 21 | 2026-02-18 |
| 02 | research | active | 25+ research files: vision, problems, design, architecture | 25 | 2026-02-18 |
| 03 | instructions | scaffolded | — | 0 | — |
| 04 | design | active | 2 design docs: chain system design, avenue web integration | 3 | 2026-02-18 |
| 05 | planning | active | Implementation plan for .0agnostic/avenue web MVP | 2 | 2026-02-18 |
| 06 | development | active | MVP implemented: .0agnostic/ with rules, knowledge, protocols, skills | 3 | 2026-02-18 |
| 07 | testing | active | 76 PASS, 0 FAIL, 7 SKIP, 2 SCAFFOLDED | 8 | 2026-02-18 |
| 08-11 | criticism-archives | scaffolded | — | 0 | — |

**Stage reports**: each active stage has `outputs/stage_report.md` — read for details.

## How Stages Connect

```
01 request_gathering ──→ Defined 8 needs in tree of needs
        │
02 research ───────────→ Investigated context chain patterns, 25+ files
        │
04 design ─────────────→ Architecture: 4-layer system, avenue web integration
        │
05 planning ───────────→ MVP-first implementation plan
        │
06 development ────────→ Built .0agnostic/ structure, all 8 avenues
        │
07 testing ────────────→ Validated: 76 PASS, 0 FAIL
```

Stages 01 and 02 ran in parallel (research informed requirements and vice versa). Stages 04→05→06→07 were sequential.

## Current Focus

- **Agent context model**: designing how the manager delegates to stage agents, what each stage agent knows in its static/dynamic context
- **Stage report system**: implemented this session — each stage now has `outputs/stage_report.md`
- **Three-tier knowledge architecture**: applying the pointer → distilled → full pattern

## Children

| Sub-Feature | Purpose | Status |
|-------------|---------|--------|
| chain_visualization | Visual diagrams of context chain flows | scaffolded |
| context_loading | How context is loaded at runtime | scaffolded |

**Location**: `layer_4_group/layer_4_subx4_features/`

## Quick Access

| Content | Location |
|---------|----------|
| Entity source of truth | `0AGNOSTIC.md` |
| Knowledge base | `.0agnostic/knowledge/` (4 docs, 5 principles) |
| Rules | `.0agnostic/rules/` (5 static, 4 dynamic) |
| Protocols | `.0agnostic/protocols/` (4 + stage_report_protocol) |
| Skills | `.0agnostic/skills/` (chain-validate, avenue-check) |
| Orchestrator | `layer_3_orchestrator.gab.jsonld` + `.integration.md` |
| Stage directories | `layer_3_group/layer_3_99_stages/stage_3_*` |

## Delegation

To work on a specific stage, spawn a stage agent:
```
Task tool → subagent_type: general-purpose
prompt: "Work on stage_3_XX_[name] for the context chain system.
         Read 0AGNOSTIC.md in that stage directory first."
```
The stage agent has its own 0AGNOSTIC.md with operational knowledge for that stage.
Read the stage's `outputs/stage_report.md` for current status before delegating.
