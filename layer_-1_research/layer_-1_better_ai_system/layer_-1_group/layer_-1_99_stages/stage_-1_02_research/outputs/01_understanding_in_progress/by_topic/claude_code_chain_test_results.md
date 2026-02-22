# Claude Code Context & Reference Chain Test Results

**Layer**: layer_-1 (Research)
**Stage**: 02_research
**Date**: 2026-02-08
**Topic**: Testing whether Claude Code's context/reference chains actually guide agents to use the three avenues

---

## Test Overview

Comprehensive test of Claude Code's context chain and reference chain against three avenues:
1. **Avenue 1: AALang/GAB/JSON-LD** — `.gab.jsonld` agent definitions
2. **Avenue 2: Integration MDs** — `.integration.md` auto-generated summaries
3. **Avenue 3: Skills** — `.claude/skills/*/SKILL.md` action triggers

Plus a fourth dimension:
4. **Agnostic System** — `0AGNOSTIC.md`, `.0agnostic/`, `.1merge/`, `agnostic-sync.sh`

---

## Results Summary

| Category | Passed | Failed | Warnings | Total |
|----------|--------|--------|----------|-------|
| Avenue 1: .gab.jsonld | 10 | 1 | 0 | 11 |
| Avenue 2: .integration.md | 8 | 0 | 0 | 8 |
| Avenue 3: Skills | 5 | 2 | 0 | 7 |
| Agnostic: 0AGNOSTIC.md | 0 | 10 | 0 | 10 |
| Agnostic: .0agnostic/ | 0 | 10 | 0 | 10 |
| Agnostic: .1merge/ | 0 | 10 | 0 | 10 |
| Agnostic: agnostic-sync.sh | 0 | 10 | 0 | 10 |
| Reference: .gab↔.integration | 17 | 0 | 0 | 17 |
| Reference: 0AGNOSTIC↔CLAUDE.md | 160 | 2 | 0 | 162 |
| Layer CLAUDE.md↔.0agnostic | 2 | 1 | 0 | 3 |
| Skills: all avenues | 4 | 0 | 4 | 8 |
| **TOTAL** | **31** | **46** | **4** | **81** |

---

## Detailed Results

### TEST 1: Context Chain → Avenue 1 (.gab.jsonld references)

Files in the Claude Code context chain that mention `.gab.jsonld`:

| File | Status |
|------|--------|
| `.claude/rules/universal-layer.md` | PASS |
| `.claude/rules/aalang-integration.md` | PASS |
| `.claude/rules/research-context.md` | PASS |
| `.claude/rules/school-context.md` | PASS |
| `.claude/rules/development-stages.md` | PASS |
| `.claude/skills/context-gathering/SKILL.md` | PASS |
| `.claude/skills/stage-workflow/SKILL.md` | PASS |
| `.claude/skills/entity-creation/SKILL.md` | **FAIL** — does not mention .gab.jsonld |
| `.claude/skills/handoff-creation/SKILL.md` | PASS |
| `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/session_workflow.md` | PASS |
| `CLAUDE.md` (root) | PASS |

### TEST 2: Context Chain → Avenue 2 (.integration.md references)

| File | Status |
|------|--------|
| `.claude/rules/universal-layer.md` | PASS |
| `.claude/rules/aalang-integration.md` | PASS |
| `.claude/rules/research-context.md` | PASS |
| `.claude/rules/school-context.md` | PASS |
| `.claude/rules/development-stages.md` | PASS |
| `.claude/skills/context-gathering/SKILL.md` | PASS |
| `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/session_workflow.md` | PASS |
| `CLAUDE.md` (root) | PASS |

### TEST 3: Context Chain → Avenue 3 (Skills references)

| File | Status |
|------|--------|
| `.claude/rules/universal-layer.md` | PASS |
| `.claude/rules/aalang-integration.md` | PASS |
| `.claude/rules/research-context.md` | PASS |
| `.claude/rules/school-context.md` | PASS |
| `.claude/rules/development-stages.md` | PASS |
| `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/session_workflow.md` | **FAIL** — does not mention skills |
| `CLAUDE.md` (root) | **FAIL** — does not mention skills |

### TEST 4: Context Chain → Agnostic System

**4a: 0AGNOSTIC.md references** — 0/10 PASS (complete failure)

No file in the Claude Code context chain mentions `0AGNOSTIC`:
- `~/.claude/CLAUDE.md` — FAIL
- `~/CLAUDE.md` — FAIL
- `0_layer_universal/CLAUDE.md` — FAIL
- All 5 `.claude/rules/*.md` — FAIL
- `.claude/skills/context-gathering/SKILL.md` — FAIL
- `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/session_workflow.md` — FAIL

**4b: .0agnostic/ directory references** — 0/10 PASS (complete failure)

Same pattern — zero mentions across the entire Claude Code context chain.

**4c: .1merge/ references** — 0/10 PASS (complete failure)

Not mentioned anywhere in the context chain.

**4d: agnostic-sync.sh references** — 0/10 PASS (complete failure)

Not mentioned anywhere in the context chain.

### TEST 5: Reference Chain — .gab.jsonld ↔ .integration.md

All 17 `.gab.jsonld` files have matching `.integration.md` files. **17/17 PASS.**

### TEST 6: Auto-generated CLAUDE.md files reference 0AGNOSTIC.md

| File | Status |
|------|--------|
| `layer_0/CLAUDE.md` | **FAIL** — auto-generated but doesn't reference 0AGNOSTIC.md |
| Root `CLAUDE.md` | **FAIL** — auto-generated but doesn't reference 0AGNOSTIC.md |
| All 158 others | PASS |

### TEST 7: Every 0AGNOSTIC.md has a matching CLAUDE.md

All 160 `0AGNOSTIC.md` files have matching `CLAUDE.md`. **160/160 PASS.**

### TEST 8: Layer CLAUDE.md files mention .0agnostic/

| File | Status |
|------|--------|
| `layer_0/CLAUDE.md` | **FAIL** — does NOT mention .0agnostic/ |
| `layer_1/CLAUDE.md` | PASS |
| `layer_-1_research/CLAUDE.md` | PASS |

### TEST 9: Skills reference all three avenues

| Skill | .gab.jsonld | .integration.md |
|-------|:-----------:|:---------------:|
| context-gathering | PASS | PASS |
| entity-creation | WARN | WARN |
| handoff-creation | PASS | WARN |
| stage-workflow | PASS | WARN |

---

## Key Findings

### What Works Well
- **Avenue 1 (GAB/JSON-LD)**: 10/11 context chain files reference it. Strong coverage.
- **Avenue 2 (Integration MD)**: 8/8 tested files reference it. Complete coverage.
- **Reference integrity**: 17/17 .gab↔.integration pairs exist. 160/160 0AGNOSTIC↔CLAUDE pairs exist.

### Critical Gaps
1. **Agnostic system is invisible to Claude Code** — 40/40 failures. The entire agnostic infrastructure (0AGNOSTIC.md, .0agnostic/, .1merge/, agnostic-sync.sh) is not mentioned in any Claude Code context chain file.
2. **Skills avenue partially covered** — `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/session_workflow.md` and root `CLAUDE.md` don't mention skills.
3. **entity-creation skill** missing references to .gab.jsonld and .integration.md.
4. **layer_0/CLAUDE.md** doesn't reference .0agnostic/ (but layer_1 and layer_-1 do).

### Impact Assessment
- An agent starting a new session via Claude Code will **never be told** about 0AGNOSTIC.md, .0agnostic/, .1merge/, or agnostic-sync.sh
- It will correctly find .gab.jsonld and .integration.md files (avenues 1-2 work)
- It may miss skill triggers in some contexts (avenue 3 has gaps)
- It will never know to "edit 0AGNOSTIC.md instead of CLAUDE.md" unless it happens to read the footer of an auto-generated file

---

## Recommended Fixes

### Priority 1: Agnostic System Integration (40 failures)
Add agnostic system references to:
- All 5 `.claude/rules/*.md` files
- `.claude/skills/context-gathering/SKILL.md`
- `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/session_workflow.md`
- Root `CLAUDE.md`
- `~/.claude/CLAUDE.md` (global)

### Priority 2: Skills Gap (2 failures)
Add skills references to:
- `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/session_workflow.md`
- Root `CLAUDE.md`

### Priority 3: Skill Avenue Completeness (4 warnings)
Add .gab.jsonld/.integration.md references to:
- `entity-creation/SKILL.md`
- `handoff-creation/SKILL.md` (just .integration.md)
- `stage-workflow/SKILL.md` (just .integration.md)

### Priority 4: layer_0 References (2 failures)
- `layer_0/CLAUDE.md` should reference .0agnostic/
- Root `CLAUDE.md` and `layer_0/CLAUDE.md` should reference 0AGNOSTIC.md

---

## Test Script Location

The test script is preserved at: `/tmp/test_chains.sh`
Can be re-run via: `bash /tmp/test_chains.sh`

---

*This document is part of the episodic research system for the better_ai_system project.*
