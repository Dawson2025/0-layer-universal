# organization — Stages Manager

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

You are the **Stages Manager** for the organization sub-feature.

- **Role**: Coordinate research stages for how entities, layers, and stages are structurally organized
- **Scope**: Stage orchestration only — delegates to individual stage agents for actual work
- **Parent**: `../../0AGNOSTIC.md` (organization entity)
- **Layer**: 1

## Key Behaviors

### Stage Overview

| Stage | Name | Status | Key Output |
|-------|------|--------|------------|
| 01 | Request Gathering | **active** | Tree of needs: research/production/instantiation pattern |
| 02 | Research | pending | Investigation of organizational patterns |
| 03 | Instructions | empty | Constraints and rules |
| 04 | Design | **active** | Design decisions for R/P/I architecture |
| 05 | Planning | empty | Implementation breakdown |
| 06 | Development | empty | Artifacts and implementations |
| 07 | Testing | empty | Validation |
| 08 | Criticism | empty | Review |
| 09 | Fixing | empty | Corrections |
| 10 | Current Product | empty | Deliverables |
| 11 | Archives | empty | History |

### How Stage Delegation Works

1. Receive task from entity manager (parent 0AGNOSTIC.md)
2. Identify which stage(s) the task belongs to
3. Delegate to stage agent: point to stage directory, let agent read its own 0AGNOSTIC.md
4. Track stage status and dependencies

### Stage Dependencies

```
01_request_gathering ──→ 02_research ──→ 04_design ──→ 05_planning ──→ 06_development
                                                                          ↓
                                          08_criticism ←── 07_testing ←──┘
                                              ↓
                                          09_fixing ──→ 10_current_product ──→ 11_archives
```

Stage 03 (instructions) can be populated at any point when constraints are identified.

## Triggers

Load when:
- Entity manager delegates stage-level work
- Entering `layer_1_99_stages/`
- Need to check stage status or dependencies

# ── Current Status ──

## Current Status

**Phase**: initializing — stages 01 and 04 active | **Last Updated**: 2026-02-25

Stage 01 (request_gathering) has a tree of needs with 3 branches covering research/production lifecycle, instantiation patterns, and universal applicability. Stage 04 (design) has 3 design decisions documenting the R/P/I architecture, school system example, and stage scaffolding defaults. Remaining stages are empty scaffolds.

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail

### Active Stages

| Stage | What's There | Entry Point |
|-------|-------------|-------------|
| 01 | Tree of needs: 3 branches, ~12 needs | `stage_1_01_request_gathering/0AGNOSTIC.md` |
| 04 | 3 design decisions | `stage_1_04_design/0AGNOSTIC.md` |

### Domain Context

The organization sub-feature researches the structural patterns for how any system — AI or otherwise — can be organized. The core insight: **every system should support three versions**:

1. **Research** (layer_-1): Experimental features, exploratory work
2. **Production** (standard entity): Stable, tried-and-true patterns
3. **Instantiations** (children): Per-user or per-context instances

School system is the concrete example: the AI system researches better teaching features, production contains proven patterns, and each student gets a personalized instantiation.

# ── References ──

## Navigation

| Content | Location |
|---------|----------|
| Entity context | `../../0AGNOSTIC.md` |
| Stage 01 (requests) | `stage_1_01_request_gathering/0AGNOSTIC.md` |
| Stage 04 (design) | `stage_1_04_design/0AGNOSTIC.md` |
| Stage registry | `stage_1_00_stage_registry/` |
| Entity children | `../../layer_2_group/layer_2_subx2_features/` |
