---
resource_id: "1d56e791-83be-4757-9d00-0ebffe30bf7c"
resource_type: "output"
resource_name: "08_discovery_temperature_model"
---
# Discovery Temperature Model

**Date**: 2026-02-23
**Status**: Approved and implemented
**Scope**: How context reaches agents at different "temperatures" — Hot (always loaded), Warm (on directory entry), Cold (on demand/trigger)

---

## Overview

Not all context should be loaded the same way. Some must always be present (identity, critical rules). Some should appear when an agent enters a relevant directory. Some should only load when a specific trigger fires.

The **discovery temperature model** categorizes context delivery into three tiers based on when and how context reaches the agent.

---

## The Three Temperatures

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│   HOT  ████████████████████  Always loaded. Zero agent effort.  │
│                                                                  │
│   WARM ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  On directory entry. Automatic     │
│                              but scoped.                         │
│                                                                  │
│   COLD ░░░░░░░░░░░░░░░░░░░  On demand or trigger. Agent must   │
│                              actively seek or be triggered.      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Hot Context (Always Loaded)

**Mechanism**: CLAUDE.md cascade (filesystem walk from root to working directory)

**What's hot**:
- Entity identity (from 0AGNOSTIC.md STATIC → agnostic-sync.sh → CLAUDE.md)
- Critical rules (from root CLAUDE.md — modification protocol, commit rules, stage completeness)
- Promoted rules (from `promote: hot` frontmatter → agnostic-sync.sh injects into Promoted Rules table)
- Navigation pointers (triggers table, resources table, children list)
- Current status (1-2 line summary of entity state)

**Properties**:
- Loaded at session start, before agent takes any action
- Cannot be bypassed — Claude Code always loads CLAUDE.md chain
- Token cost is paid every session, so must be lean (<400 lines total chain)
- The most reliable delivery tier — if hot context is wrong, everything is wrong

**Token budget**: Target <170 lines per entity CLAUDE.md. Total chain (root to leaf) target <400 lines.

### Warm Context (On Directory Entry)

**Mechanism**: `.claude/rules/` path-specific rules (auto-loaded when agent enters matching directory)

**What's warm**:
- Directory-scoped behavioral rules (e.g., "when in .0agnostic/, follow agnostic update protocol")
- Research context rules (e.g., "when in research directories, check episodic memory")
- Development stage rules (e.g., "when in development stages, follow commit conventions")
- Skill routing hints (e.g., "when entering entity, use /context-gathering first")

**Properties**:
- Loaded automatically when agent enters a matching directory path
- Scoped — only fires for specific path patterns
- Lower token cost than hot (not loaded unless path matches)
- Good for context that's important within a scope but not universally

**Current warm rules** (at root level):
- `agnostic-edits.md` — fires on `.0agnostic/**` paths, reminds of update protocol
- `research-context.md` — fires in research directories, loads research workflow
- `development-stages.md` — fires in development stages, loads dev workflow

### Cold Context (On Demand / On Trigger)

**Mechanism**: Agent explicitly reads files, or dynamic rules fire on specific conditions

**What's cold**:
- Full knowledge documents (`.0agnostic/01_knowledge/`)
- Dynamic rules that fire on specific scenarios (`.0agnostic/02_rules/dynamic/`)
- Protocols that are invoked for specific procedures (`.0agnostic/03_protocols/`)
- Skills that match specific WHEN conditions (`.claude/skills/`)
- Episodic memory (`.0agnostic/04_episodic_memory/`)
- JSON-LD agent definitions (`.gab.jsonld` — loaded via jq selectively)
- Integration summaries (`.integration.md`)
- Handoff documents (`.0agnostic/05_handoff_documents/`)

**Properties**:
- Zero token cost until needed
- Requires agent action (explicit read) or trigger match
- Can be arbitrarily detailed — no token budget constraint
- The bulk of all context lives at this temperature

---

## Temperature Assignment Criteria

| Criterion | Hot | Warm | Cold |
|-----------|-----|------|------|
| **Needed every session?** | Yes | Sometimes | Rarely |
| **Universal or scoped?** | Universal | Scoped to path | Scoped to task |
| **Token cost acceptable?** | Must be lean | Moderate | Unlimited |
| **Failure impact?** | Agent can't function | Agent misses workflow | Agent misses detail |
| **Can agent discover it?** | Doesn't need to — always there | Automatic on path entry | Must know to look or be triggered |

### Decision flowchart

```
Is this context needed EVERY session, for EVERY task?
├── YES → HOT (put in 0AGNOSTIC.md STATIC / promote: hot rule)
└── NO
    Is this context needed whenever agent enters a specific directory?
    ├── YES → WARM (put in .claude/rules/ with path matcher)
    └── NO
        Is this context needed for a specific task type or trigger?
        ├── YES → COLD with trigger (dynamic rule or skill WHEN condition)
        └── NO → COLD on-demand (knowledge doc, protocol, episodic)
```

---

## Hot Rule Promotion System

Rules that are too detailed for CLAUDE.md but too important to be purely cold can be **promoted**. The promotion system puts a 1-line pointer in hot context while keeping the full rule cold.

### Frontmatter format

```yaml
---
promote: hot
hot_trigger: "When this condition is met"
hot_summary: "Do this thing. Full rule: .0agnostic/02_rules/static/rule_name.md"
---
```

### How it works

1. Rule file lives in `.0agnostic/02_rules/static/` or `.0agnostic/02_rules/dynamic/` (cold storage)
2. agnostic-sync.sh scans for `promote: hot` frontmatter during generation
3. Promoted rules appear as a `## Promoted Rules` table in ALL generated tool files
4. Table has two columns: `When` (trigger condition) and `Rule` (1-line summary + path)
5. Agent sees the trigger in hot context → reads the full rule from cold storage on match

### Current promoted rules

| When | Rule |
|------|------|
| Modifying `.0agnostic/` files | Follow agnostic update protocol: `.0agnostic/02_rules/static/agnostic_update_protocol.md` |
| Any turn that modifies files | Report all file changes with full paths: `.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING.md` |

---

## PostToolUse Hook System

A third enforcement mechanism beyond hot and warm: **hooks** that fire after specific tool operations.

### agnostic-edit-guard.sh

| Property | Value |
|----------|-------|
| **Trigger** | PostToolUse on Edit or Write operations |
| **Condition** | File path contains `.0agnostic/` |
| **Action** | Returns `additionalContext` reminding agent of the agnostic update protocol |
| **Location** | `.0agnostic/06_context_avenue_web/01_file_based/08_hooks/scripts/agnostic-edit-guard.sh` |

This catches the case where an agent modifies .0agnostic/ content without having read the warm rule (e.g., if the agent was spawned directly into a deep path).

### Three-layer defense in depth

```
Layer 1: HOT (agnostic-sync.sh Promoted Rules table)
  → Agent always sees "when modifying .0agnostic/, follow protocol"
  → Fires: every session, every entity

Layer 2: WARM (.claude/rules/agnostic-edits.md)
  → Agent sees full instructions on entering .0agnostic/ path
  → Fires: on directory entry matching .0agnostic/**

Layer 3: HOOK (PostToolUse agnostic-edit-guard.sh)
  → Agent gets reminded AFTER editing a .0agnostic/ file
  → Fires: after every Edit/Write to .0agnostic/ path
```

If any one layer fails, the other two still catch it.

---

## Empirical Validation

The discovery temperature model was validated through the `/perplexity-extract` skill discovery chain test (2026-02-22):

1. **Hot validated**: A fresh agent given a Perplexity URL immediately found the `/perplexity-extract` skill via the CLAUDE.md hot context (Browser Extraction Capabilities section injected by .1merge `2_additions/`)

2. **Warm validated**: The research-context.md path rule fired when the agent entered research directories, loading research workflow context automatically

3. **Cold validated**: The agent followed the skill's WHEN condition to load the full SKILL.md, which referenced detailed knowledge in `.0agnostic/07+_setup_dependant/.../perplexity_extraction/`

4. **Hook validated**: The agnostic-edit-guard.sh hook correctly returned `additionalContext` when an agent edited a .0agnostic/ file, and returned empty JSON for non-.0agnostic/ paths

---

## Related Documents

- **Propagation chain**: `03_propagation_chain_architecture.md` (4-layer top-down flow)
- **Inheritance model**: `05_hierarchy_inheritance_model.md` (what propagates across levels)
- **Avenue web design**: `01_context_chain_system_design.md` (8-avenue MVP)
- **Source-to-avenue flow**: `06_source_of_truth_to_avenue_flow.md` (numbering and ordering)
