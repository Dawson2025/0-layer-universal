# Claude Code Context

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


## Current Status

**Phase**: initializing — stages 01 and 04 active | **Last Updated**: 2026-02-25

Stage 01 (request_gathering) has a tree of needs with 3 branches covering research/production lifecycle, instantiation patterns, and universal applicability. Stage 04 (design) has 3 design decisions documenting the R/P/I architecture, school system example, and stage scaffolding defaults. Remaining stages are empty scaffolds.

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
