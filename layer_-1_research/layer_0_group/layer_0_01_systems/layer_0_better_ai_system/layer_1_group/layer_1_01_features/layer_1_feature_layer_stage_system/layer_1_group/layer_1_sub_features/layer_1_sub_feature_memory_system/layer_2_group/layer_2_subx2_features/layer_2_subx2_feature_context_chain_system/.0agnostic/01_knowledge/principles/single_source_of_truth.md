---
resource_id: "5f9089b8-10b0-436d-b9a4-5d16683b00ad"
resource_type: "knowledge"
resource_name: "single_source_of_truth"
---
# Principle: Single Source of Truth

**Type**: Consistency
**Severity**: Critical
**Date**: 2026-02-17

---

## Statement

**`0AGNOSTIC.md` is the single source of truth for every entity's context. All tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md) are derived from it. Edit 0AGNOSTIC.md, never the generated files.**

---

## Rationale

Without a single source, context drifts:
- CLAUDE.md says one thing, GEMINI.md says another
- Manual edits to CLAUDE.md are overwritten on next sync
- No canonical version exists to resolve conflicts
- Different tools see different context for the same entity

The agnostic system solves this by establishing a single editable source (`0AGNOSTIC.md`) and a deterministic transformation (`agnostic-sync.sh`) that produces consistent output for all tools.

---

## The Source Chain

```
0AGNOSTIC.md          ← EDIT THIS (source of truth)
     │
     ▼ agnostic-sync.sh
     │
     ├── CLAUDE.md     ← GENERATED (do not edit)
     ├── AGENTS.md     ← GENERATED (do not edit)
     ├── GEMINI.md     ← GENERATED (do not edit)
     └── OPENAI.md     ← GENERATED (do not edit)
```

### What agnostic-sync.sh Does

1. Extracts specific h2 sections from 0AGNOSTIC.md (Identity, Navigation, Triggers, Key Behaviors, Critical Rules)
2. Wraps them in tool-specific headers and footers
3. Adds Claude-Specific Rules / OpenAI-Specific Notes / Gemini-Specific Notes sections
4. Writes the generated files with auto-generated footer markers

---

## Requirements

### Must

- All context changes go through `0AGNOSTIC.md` first
- Run `agnostic-sync.sh` after every edit to 0AGNOSTIC.md
- Generated files must have the auto-generated footer: `*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*`
- Commit generated files alongside the source

### Must Not

- Never edit CLAUDE.md, AGENTS.md, GEMINI.md, or OPENAI.md directly
- Never have context in a generated file that isn't derived from 0AGNOSTIC.md (use `.1merge/` for tool-specific additions)
- Never skip the sync step after editing 0AGNOSTIC.md

---

## The .1merge/ Exception

Some tools need content that isn't in 0AGNOSTIC.md. The `.1merge/` system handles this with a 3-tier merge:

```
.1merge/
├── claude/
│   ├── 0_synced/      ← Matches agnostic-sync output (for diff)
│   ├── 1_overrides/   ← Override synced sections
│   └── 2_additions/   ← Add sections not in 0AGNOSTIC.md
├── cursor/
│   └── (same tiers)
└── (other tools)
```

**Priority**: `2_additions` > `1_overrides` > `0_synced`

This allows tool-specific customization while keeping 0AGNOSTIC.md as the primary source.

---

## Verification

The single-source-of-truth property is verified by:
- `test_agnostic_sync.sh`: Confirms sync produces correct output
- Auto-generated footer check: All generated files must end with the marker
- Content diff: `diff <(extract_identity CLAUDE.md) <(extract_identity 0AGNOSTIC.md)` should show only formatting differences

---

## Related Principles

- Chain Continuity — the Parent: reference in 0AGNOSTIC.md is the canonical chain link
- Lean Static Context — 0AGNOSTIC.md sections determine what enters CLAUDE.md (static)
