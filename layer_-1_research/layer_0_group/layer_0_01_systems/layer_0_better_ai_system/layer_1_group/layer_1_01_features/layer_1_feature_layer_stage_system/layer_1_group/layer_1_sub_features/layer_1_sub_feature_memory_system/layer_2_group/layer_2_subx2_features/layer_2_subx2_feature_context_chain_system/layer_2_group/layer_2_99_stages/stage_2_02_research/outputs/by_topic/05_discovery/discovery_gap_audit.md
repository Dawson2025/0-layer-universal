---
resource_id: "f3f6a6e5-0fa4-4f05-ba9f-6ca9fe5b661e"
resource_type: "output"
resource_name: "discovery_gap_audit"
---
# Discovery Gap Audit: Context Chain Auto-Discoverability

**Date**: 2026-02-22
**Method**: Systematic audit of all auto-loaded context files vs cold-context resources
**Scope**: Whether a fresh agent will automatically discover and follow context chain update protocols

---

## Question

When an agent starts a session and modifies `.0agnostic/` content, will it automatically know to:
1. Update `0AGNOSTIC.md` to reference the new content
2. Run `agnostic-sync.sh` to regenerate tool files
3. Run `user-level-sync.sh` to propagate to `~/.0agnostic/`
4. Update stage reports and `0INDEX.md`
5. Follow the full propagation chain

**Without the user giving specific instructions or showing them where to find things?**

---

## Findings

### Discovery Temperature Model (Validated)

Context in the system has three "temperatures" based on when it's loaded:

| Temperature | When Loaded | Mechanism | Examples |
|-------------|-------------|-----------|----------|
| **Hot** | Every session, automatically | CLAUDE.md chain, MEMORY.md, `.claude/rules/` | Root identity, critical rules, .1merge additions |
| **Warm** | On directory entry | Path-specific rules (`.claude/rules/*.md`) | Research context, development rules, AALang integration |
| **Cold** | On trigger or manual read | `.0agnostic/02_rules/`, `.0agnostic/03_protocols/` | agnostic_update_protocol, browser_extraction_rule |

### Audit Matrix: What a Fresh Agent Sees

| Concept | `~/.claude/CLAUDE.md` | Root `CLAUDE.md` | `MEMORY.md` | `.claude/rules/*` | Cold (`.0agnostic/`) |
|---------|:---:|:---:|:---:|:---:|:---:|
| `agnostic-sync.sh` | Found | Found | Found | Found (6 files) | Found |
| `user-level-sync.sh` | **Missing** | **Missing** | Found | **Missing** | **Missing** |
| "Edit 0AGNOSTIC.md" | Found | Found | Found | Found (6 files) | Found |
| `agnostic_update_protocol` | **Missing** | **Missing** | **Missing** | **Missing** | Found |
| Stage reports | **Missing** | **Missing** | Found | **Missing** | N/A |
| Propagation chain | **Missing** | **Missing** | **Missing** | **Missing** | Found |
| `0INDEX.md` updates | **Missing** | **Missing** | **Missing** | **Missing** | **Missing** |

### The Core Gap

The **agnostic update protocol** (`agnostic_update_protocol.md`) is an I1 (High importance) static rule that:
- Describes the full propagation chain: `.0agnostic/ → 0AGNOSTIC.md → agnostic-sync → CLAUDE.md → agent`
- Documents exactly what to update when modifying each type of .0agnostic/ content
- Includes a 5-step "After Every Update" procedure

**But it lives entirely in cold context.** No auto-loaded file points to it. An agent must:
1. Follow the Context Traversal Rule (read `.0agnostic/02_rules/`)
2. Find the protocol file
3. Read it

This is a 2-hop manual discovery chain that agents frequently skip.

### The Irony

The agnostic_update_protocol.md **describes the problem of orphaned content** — and is itself orphaned from hot context. It exemplifies the very failure mode it warns about.

---

## What Works

1. **"Edit 0AGNOSTIC.md, not CLAUDE.md"** — in hot context everywhere. Agents know the source-of-truth pattern.
2. **"Run agnostic-sync.sh after changes"** — in hot context. Agents know to regenerate.
3. **Skill discovery chain** — proven working end-to-end (6/6 checkpoints PASS). Content that IS referenced propagates correctly.
4. **agnostic-sync validation** — catches orphaned content when run, but only as warnings.

## What Doesn't Work

1. **Update protocol invisible** — agents don't know the full chain or the "After Every Update" procedure
2. **user-level-sync.sh unknown** — only in MEMORY.md (not in any CLAUDE.md or rule)
3. **Stage reports advisory** — no enforcement mechanism
4. **0INDEX.md updates never mentioned** — manager dashboards go stale
5. **No pre-commit enforcement** — nothing blocks commits with orphaned .0agnostic/ content

---

## Implications

### For the Agnostic System (Tool-Agnostic)

The problem is architectural: **the system has good static rules but no mechanism to promote critical rules to hot context**. The `.0agnostic/02_rules/static/` directory assumes agents will read it on every session, but Claude Code (and likely other tools) only auto-load specific files.

**Needed**: A way to mark certain `.0agnostic/` content as "must be in hot context" and have the sync system automatically promote it.

### For AI App Adapters (Claude Code CLI)

Claude Code has specific mechanisms that could enforce the protocol:
- **Hooks** (`.claude/hooks/`): Pre-commit hooks that run shell commands
- **Path-specific rules** (`.claude/rules/`): Auto-loaded when working in matching paths
- **Skills** (`.claude/skills/`): Invokable procedures
- **MEMORY.md**: Auto-loaded first 200 lines

**Needed**: The `.1merge/.1claude_merge/` adapter should promote critical agnostic rules into Claude Code-specific enforcement mechanisms (hooks, rules).

### For Other AI Tools

Each tool has different auto-loading mechanisms:
- **Cursor**: `.cursorrules` (single file, always loaded)
- **Gemini CLI**: `GEMINI.md` (chain like CLAUDE.md)
- **Codex CLI**: `AGENTS.md` + `codex.md`

**Needed**: Each `.1merge/.1{tool}_merge/` adapter needs to map critical agnostic rules to that tool's enforcement mechanisms.

---

## Open Questions

1. Should critical `.0agnostic/` rules be injected into generated CLAUDE.md via `.1merge` additions? (Pro: hot context. Con: bloats CLAUDE.md)
2. Should `agnostic-sync.sh` be extended to auto-generate pre-commit hooks from rules marked as enforceable?
3. Is MEMORY.md a reliable hot context channel? (It's auto-loaded but may be at the 200-line limit)
4. Should the agnostic system have an explicit "hot context registry" in `.0agnostic/` that lists what MUST appear in generated tool files?

---

## Sources

- Audit conducted using systematic grep across all auto-loaded files
- agnostic_update_protocol.md: `.0agnostic/02_rules/static/agnostic_update_protocol.md`
- Skill discovery chain test: `../stage_2_07_testing/outputs/test_skill_discovery_chain.md`
- agnostic-sync.sh validation: `.0agnostic/agnostic-sync.sh` (lines 298-390)
