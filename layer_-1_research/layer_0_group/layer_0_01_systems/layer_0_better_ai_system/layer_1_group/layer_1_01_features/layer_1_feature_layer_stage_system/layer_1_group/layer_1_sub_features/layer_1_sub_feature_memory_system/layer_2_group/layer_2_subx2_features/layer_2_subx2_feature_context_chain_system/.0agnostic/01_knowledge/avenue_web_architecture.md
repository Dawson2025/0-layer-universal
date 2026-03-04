# Avenue Web Architecture

**Layer**: layer_2 (Research Sub-Feature)
**Stage**: 02_research → 05_design
**Date**: 2026-02-17
**Topic**: The multiple independent avenues through which context reaches AI agents

---

## Overview

An **avenue** is an independent path through which context can reach an AI agent. The context chain system uses multiple redundant avenues to ensure critical context is never lost, even if one delivery mechanism fails.

---

## The 8 Primary Avenues

| # | Avenue | Mechanism | Static/Dynamic |
|---|--------|-----------|----------------|
| A1 | System Prompt (CLAUDE.md) | Auto-loaded cascade from root to cwd | Static |
| A2 | Path Rules (.claude/rules/) | Loaded when AI enters matching directory | Static/Dynamic |
| A3 | Skills (.0agnostic/skills/) | Listed statically; full content on invocation | Both |
| A4 | Parent References (0AGNOSTIC.md) | Explicit `Parent:` chain traversal | Dynamic |
| A5 | JSON-LD Agent Defs (.gab.jsonld) | Mode/actor/persona definitions | Dynamic |
| A6 | Integration Summaries (.integration.md) | Markdown summaries of .gab.jsonld | Dynamic |
| A7 | Episodic Memory (.0agnostic/episodic_memory/) | Session history and decisions | Dynamic |
| A8 | Agnostic System (.0agnostic/) | On-demand rules, knowledge, scripts | Dynamic |

### Avenue Independence

Each avenue operates through a **different mechanism**:

```
A1: CLAUDE.md     → Claude Code filesystem walk (automatic)
A2: Path rules    → Claude Code directory-match rules (automatic)
A3: Skills        → Skill listing + invocation (semi-automatic)
A4: 0AGNOSTIC     → Agent reads and follows Parent refs (manual)
A5: .gab.jsonld   → Agent queries via jq (manual)
A6: .integration  → Agent reads markdown summary (manual)
A7: Episodic      → Agent reads session history (manual)
A8: .0agnostic/   → Agent loads on-demand resources (manual)
```

This independence means a failure in one avenue (e.g., A5 JSON-LD parsing error) does not affect others.

---

## Avenue Categories

### By Timing

| Category | Avenues | Token Cost |
|----------|---------|-----------|
| **Static** (always loaded) | A1 (CLAUDE.md) | Every API call |
| **Semi-static** (loaded on directory entry) | A2 (Path rules) | When in directory |
| **Dynamic** (loaded on-demand) | A3-A8 | Only when invoked |

### By Ownership

| Category | Avenues | Who controls |
|----------|---------|-------------|
| **Fixed** (system-determined) | A1 cascade order, A2 matching | Claude Code runtime |
| **Configurable** (user-controlled) | A1 content, A3-A8 content | Project author |

---

## Redundancy Matrix

For the context_chain_system entity, critical context is delivered via:

| Context Item | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | Count |
|-------------|----|----|----|----|----|----|----|----|-------|
| Identity/Role | x | | | x | x | x | | | 4 |
| Parent chain | x | | | x | | | | | 2 |
| Available skills | | x | x | | | | | x | 3 |
| Mode constraints | | | | | x | x | | | 2 |
| Session history | | | | | | | x | | 1 |
| Rules | | x | | | | | | x | 2 |

### Minimum Redundancy Target

The avenue redundancy principle requires **3+ avenues** for critical context. Items with fewer than 3 avenues need additional references added.

---

## Avenue Health Metrics

Test results (2026-02-17):

| Avenue | Status | Detail |
|--------|--------|--------|
| A1 System Prompt | PASS | CLAUDE.md has Identity section (27 lines) |
| A2 Path Rules | PASS | 1 rule file (33 lines) |
| A3 Skills | PASS | 2 SKILL.md files |
| A4 Parent References | PASS | Chain traverses 7 levels |
| A5 JSON-LD | PASS | .gab.jsonld has @graph with 5 modes |
| A6 Integration | PASS | .integration.md has 38 lines |
| A7 Episodic Memory | SCAFFOLDED | Directory exists, sessions empty |
| A8 Agnostic System | PASS | Rules and skills populated |

**Overall**: 88% functional coverage (16 PASS, 2 SCAFFOLDED, 0 FAIL)

---

## Related Documents

- Context chain architecture: `./context_chain_architecture.md`
- Static/dynamic dimensions: `./static_dynamic_context.md`
- Avenue coverage test: `layer_2_group/.../stage_2_07_testing/outputs/test_avenue_coverage_functional.sh`
- Context chain default view: `layer_3_group/.../chain_visualization/diagrams/current/context_chain/default_view.md`
