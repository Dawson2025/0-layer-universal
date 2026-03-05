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

<!-- section_id: "a5308470-451f-4502-98fe-4f6062b6de3f" -->
## Statement

**`0AGNOSTIC.md` is the single source of truth for every entity's context. All tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md) are derived from it. Edit 0AGNOSTIC.md, never the generated files.**

---

<!-- section_id: "541f216c-2852-4046-bae3-b89e206b8030" -->
## Rationale

Without a single source, context drifts:
- CLAUDE.md says one thing, GEMINI.md says another
- Manual edits to CLAUDE.md are overwritten on next sync
- No canonical version exists to resolve conflicts
- Different tools see different context for the same entity

The agnostic system solves this by establishing a single editable source (`0AGNOSTIC.md`) and a deterministic transformation (`agnostic-sync.sh`) that produces consistent output for all tools.

---

<!-- section_id: "76175e66-40da-49c7-9e75-f47a0233783e" -->
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

<!-- section_id: "f644d6e2-e454-4bdc-9bc3-76fb7840beb9" -->
### What agnostic-sync.sh Does

1. Extracts specific h2 sections from 0AGNOSTIC.md (Identity, Navigation, Triggers, Key Behaviors, Critical Rules)
2. Wraps them in tool-specific headers and footers
3. Adds Claude-Specific Rules / OpenAI-Specific Notes / Gemini-Specific Notes sections
4. Writes the generated files with auto-generated footer markers

---

<!-- section_id: "171053bc-c26b-4ea3-b5d7-46fe3d334881" -->
## Requirements

<!-- section_id: "492b20c7-938b-442a-bcdb-53c5628696fe" -->
### Must

- All context changes go through `0AGNOSTIC.md` first
- Run `agnostic-sync.sh` after every edit to 0AGNOSTIC.md
- Generated files must have the auto-generated footer: `*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*`
- Commit generated files alongside the source

<!-- section_id: "9b86b4e4-a6b9-40a0-90e6-b89b9f3d0163" -->
### Must Not

- Never edit CLAUDE.md, AGENTS.md, GEMINI.md, or OPENAI.md directly
- Never have context in a generated file that isn't derived from 0AGNOSTIC.md (use `.1merge/` for tool-specific additions)
- Never skip the sync step after editing 0AGNOSTIC.md

---

<!-- section_id: "9a708e54-dcf8-43f7-9483-31970437d31a" -->
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

<!-- section_id: "a0f64437-3e69-4582-a9b0-9360ce8ba608" -->
## Verification

The single-source-of-truth property is verified by:
- `test_agnostic_sync.sh`: Confirms sync produces correct output
- Auto-generated footer check: All generated files must end with the marker
- Content diff: `diff <(extract_identity CLAUDE.md) <(extract_identity 0AGNOSTIC.md)` should show only formatting differences

---

<!-- section_id: "dafcc3df-87c6-478a-8edf-2405b02f1540" -->
## Related Principles

- Chain Continuity — the Parent: reference in 0AGNOSTIC.md is the canonical chain link
- Lean Static Context — 0AGNOSTIC.md sections determine what enters CLAUDE.md (static)
