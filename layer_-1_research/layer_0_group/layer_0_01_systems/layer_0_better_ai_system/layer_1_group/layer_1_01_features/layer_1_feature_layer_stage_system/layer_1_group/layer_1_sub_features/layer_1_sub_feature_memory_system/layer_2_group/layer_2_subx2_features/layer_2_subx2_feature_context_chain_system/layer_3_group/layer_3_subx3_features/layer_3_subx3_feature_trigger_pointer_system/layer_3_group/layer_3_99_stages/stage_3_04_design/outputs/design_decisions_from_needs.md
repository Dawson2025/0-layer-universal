---
resource_id: "d8e9f0a1-b2c3-4d5e-6f7a-8b9c0d1e2f3a"
resource_type: "output"
resource_name: "design_decisions_from_needs"
---
# Design Decisions Extracted from Tree of Needs

> **Date**: 2026-03-07
> **Purpose**: Captures implementation-level design decisions that were removed from stage 01 (request gathering) to keep needs pure. These decisions are valid — they just belong in the design stage, not the requirements stage.

<!-- section_id: "e9f0a1b2-c3d4-4e5f-6a7b-8c9d0e1f2a3b" -->
## 1. Relative Path Computation (from REQ-02, Branch 02)

**Decision**: Use `python3 -c "import os; print(os.path.relpath(...))"` for relative path computation.

**Rationale**: `os.path.relpath` is battle-tested and handles all edge cases (same directory, parent, deeply nested, cross-branch). Available on all target platforms where python3 is in PATH.

**Alternative considered**: Pure Bash relative path computation — more complex, error-prone for deeply nested paths.

<!-- section_id: "f0a1b2c3-d4e5-4f6a-7b8c-9d0e1f2a3b4c" -->
## 2. Ambiguous Entity Resolution (from US-03, Branch 02)

**Original decision**: First-match-wins strategy using `head -1` on `find` results.

**SUPERSEDED**: The UUID identity system now provides unambiguous entity resolution. Each entity has a unique `entity_id` (UUID4), and `.entity-lookup.tsv` maps names to UUIDs to paths. When an entity name is ambiguous, the UUID is the authoritative disambiguator.

**Current approach**: Agent uses `Grep pattern="entity_name" path=".entity-lookup.tsv"` — if multiple rows match, the UUID column distinguishes them. The `find | head -1` approach remains only in `pointer-sync.sh` as a legacy fallback for script-level resolution.

**Design evolution**: See `stage_3_02_research/outputs/agent_tool_preferences_research.md` and `stage_3_04_design/outputs/agent_friendly_interface_design.md` for the TSV-based agent interface design.

<!-- section_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d" -->
## 3. Windows Line Ending Handling (from REQ-03, Branch 01)

**Decision**: Use `tr -d '\r'` to strip carriage returns in frontmatter detection and field extraction functions.

**Implementation details**:
- `has_pointer_fm()` strips `\r` when checking the first line for `---`
- `extract_fm()` strips `\r` from extracted field values
- Update mechanism writes Unix-style `\n` (may produce mixed line endings in originally Windows-formatted files)

<!-- section_id: "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e" -->
## 4. Hook Mechanism (from REQ-01, Branch 03)

**Decision**: Use Claude Code PostToolUse hooks as the primary notification mechanism.

**Implementation**: `.claude/settings.json` registers a PostToolUse hook for Edit/Write operations that detects pointer frontmatter and injects validation reminders.

**Tool-specific details**:
- Claude Code: PostToolUse hook fires after Edit/Write, outputs JSON with `additionalContext`
- Cursor: Would need equivalent CursorRules-based approach
- VS Code: Could use file save listeners

**Why PostToolUse over PreToolUse**: Non-blocking — the agent completes its edit, then sees the reminder. PreToolUse would block the edit, which is too disruptive for a reminder workflow.

<!-- section_id: "c3d4e5f6-a7b8-4c9d-0e1f-2a3b4c5d6e7f" -->
## 5. Entity Search Mechanism (from REQ-01, Branch 02)

**Original decision**: Use `find ... -type d -name` for entity directory search.

**SUPERSEDED**: The `.entity-lookup.tsv` flat file now serves as the primary entity search interface for agents. It provides name, UUID, path, and parent_UUID in a single Grep call (~80-530 tokens). The `find`-based approach remains only in `pointer-sync.sh` as a script-level fallback.

**Current approach**:
- **Agent-facing**: `Grep pattern="entity_name" path=".entity-lookup.tsv"` (preferred — matches agent tool preferences)
- **Script-facing**: `find "$ROOT" -type d -name "$canonical_entity"` (legacy, deterministic for shell scripts)
- **UUID-based**: `Grep pattern="UUID" path=".entity-lookup.tsv"` (exact match when UUID is known)

**Design evolution**: See `stage_3_04_design/outputs/operations_and_interface_design.md` for the full interface mapping and agent tool preference alignment.
