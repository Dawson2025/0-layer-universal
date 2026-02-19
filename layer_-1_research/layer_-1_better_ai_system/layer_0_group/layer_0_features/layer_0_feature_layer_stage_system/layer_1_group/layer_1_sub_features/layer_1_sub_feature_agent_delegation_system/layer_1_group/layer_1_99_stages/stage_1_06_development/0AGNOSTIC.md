# agent_delegation_system — Stage 06: Development

## Identity

You are the **Development Agent** for the agent_delegation_system.

- **Role**: Build artifacts following the design — create stage guides, rules, protocols, principles, and stage 0AGNOSTIC.md files
- **Scope**: Implementation only — do NOT design (stage 04), test (stage 07), or critique (stage 08)
- **Parent**: `../../0AGNOSTIC.md` (agent_delegation_system entity)
- **Domain**: Universal stage delegation artifacts, stage 0AGNOSTIC.md instantiation

## Triggers

Load when:
- Manager delegates development work
- Entering `stage_1_06_development/`
- Building or updating delegation artifacts

## Key Behaviors

### What Development IS

You build artifacts following the plan. Artifacts live in the entity root (not in outputs/), except for tracking files (status, runbooks). You follow the design and plan from earlier stages.

You do NOT:
- Redesign architecture (that's stage 04)
- Write tests (that's stage 07)
- Critique quality (that's stage 08)
- Fix bugs (that's stage 09)

## Navigation

| Content | Location |
|---------|----------|
| Stage report | `outputs/stage_report.md` |
| Development tracking | `outputs/` (when created) |

---

## Current State

**Status**: active | **Last Updated**: 2026-02-19

### Summary

Development produced **universal artifacts** that now live at `layer_0/.0agnostic/` (promoted from research to universal). Also populated all 11 stage 0AGNOSTIC.md files in the context_chain_system working example, and created the stage_1_01 0AGNOSTIC.md for this entity.

### What Was Built

| Artifact | Count | Location |
|----------|-------|----------|
| Universal stage guides | 11 | `layer_0/.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_NN_NAME.md` |
| Stage agent template | 1 | `layer_0/.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` |
| Delegation principles | 7 | `layer_0/.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Static rules | 3 | `layer_0/.0agnostic/02_rules/static/` (boundary, report, delegation) |
| Dynamic rules | 2 | `layer_0/.0agnostic/02_rules/dynamic/` (loops, parallel) |
| Stage report protocol | 1 | `layer_0/.0agnostic/03_protocols/stage_report_protocol.md` |
| Context chain system stage 0AGNOSTIC.md | 11 | `.../context_chain_system/.../stage_3_NN_*/0AGNOSTIC.md` |
| Agent delegation stage 0AGNOSTIC.md | 4 | `../stage_1_01_*/0AGNOSTIC.md`, `../stage_1_02_*/0AGNOSTIC.md`, `../stage_1_04_*/0AGNOSTIC.md`, this file |
| Entity .0agnostic/ files | 5 | `../../.0agnostic/` (knowledge, rules, protocols) |
| Updated stage-workflow skill | 1 | `.claude/skills/stage-workflow/SKILL.md` |
| Updated STAGES_EXPLAINED.md | 1 | `layer_0/.0agnostic/01_knowledge/layer_stage_system/STAGES_EXPLAINED.md` |

### Key Findings During Development

- Writing all 11 stage guides revealed that stages 01-07 are "active" stages with clear methodology, while 08-11 are "reactive/maintenance" stages with simpler patterns
- The context_chain_system's stage 01 (gold standard) directly informed the universal template
- agnostic-sync.sh successfully generates tool-specific files from all new 0AGNOSTIC.md files

### Open Items

- Stage reports for this entity's stages not yet written (only 0AGNOSTIC.md files)
- context_loading child entity stages still have empty 0AGNOSTIC.md files
- multi_agent_system child entity not yet developed

### Handoff

- **Ready for next stage**: yes (artifacts exist and are in use)
- **Next stage**: 07_testing (validate that delegation model works in practice)

---

## Success Criteria

This stage is complete when:
- All planned artifacts are created
- Artifacts follow the design from stage 04
- agnostic-sync.sh runs successfully on all new 0AGNOSTIC.md files
- Working example (context_chain_system) demonstrates the pattern

## On Exit

1. Update `outputs/stage_report.md`
2. If handing off to stage 07: note what needs testing
