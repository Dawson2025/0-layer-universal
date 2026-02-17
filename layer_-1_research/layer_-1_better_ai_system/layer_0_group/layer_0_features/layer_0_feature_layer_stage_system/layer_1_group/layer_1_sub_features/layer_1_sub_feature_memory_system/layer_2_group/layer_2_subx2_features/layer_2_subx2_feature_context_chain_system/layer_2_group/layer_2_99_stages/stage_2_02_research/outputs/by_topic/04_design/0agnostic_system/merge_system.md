# .1merge Override System

## Purpose

The three-tier merge system that allows tool-specific customizations without polluting the agnostic source. `.1merge/` sits between the agnostic source (`.0agnostic/`) and the generated tool-specific output (`.claude/`, `.cursor/`, etc.), providing a clean separation between universal content and tool-specific additions.

---

## The Three Tiers

```
Tier 1: .0agnostic/              ← Universal, tool-agnostic source of truth
                                    Everything here applies to ALL tools
         │
         │ agnostic-sync.sh copies/transforms
         ▼
Tier 2: .1merge/.1{tool}_merge/  ← Tool-specific overrides and additions
                                    Only applies to one specific tool
         │
         │ agnostic-sync.sh merges
         ▼
Tier 3: .claude/ / .cursor/ etc  ← Final generated output
                                    What the tool actually reads
```

### Tier 1: .0agnostic/ (Agnostic Source)

Content that applies universally across all AI tools:
- Rules that every tool should follow
- Protocols that work regardless of tool
- Skills with tool-neutral instructions
- Knowledge that any agent can reference

**Edit this tier** when the content is tool-agnostic.

### Tier 2: .1merge/.1{tool}_merge/ (Tool-Specific Overrides)

Content that only applies to a specific tool, or that overrides agnostic content for a particular tool:

```
.1merge/
├── .1claude_merge/         # Claude Code-specific content
│   ├── rules/              # Additional Claude-only rules
│   ├── skills/             # Claude-specific skills
│   └── settings.json       # Claude Code settings (hooks, permissions)
│
├── .1cursor_merge/         # Cursor-specific content
│   └── rules/              # Cursor-specific rules (.mdc format overrides)
│
├── .1codex_merge/          # Codex CLI-specific content
│   └── config.toml         # Codex configuration
│
├── .1gemini_merge/         # Gemini CLI-specific content
│   └── extensions/         # Gemini extensions
│
├── .1aider_merge/          # Aider-specific content
│   └── conventions.md      # Aider conventions file
│
└── .1copilot_merge/        # Copilot-specific content
```

**Edit this tier** when the content is tool-specific — format requirements, tool features, tool settings, or when you need to override an agnostic rule for a particular tool.

### Tier 3: Generated Output (.claude/, .cursor/, etc.)

The final output that tools actually read. **Never edit this tier directly** — it's overwritten by `agnostic-sync.sh`. Any manual edits are lost on next sync.

---

## Merge Operations

### Sync (Tier 1 → Tier 3)

Agnostic content is copied or transformed to the tool's expected location:

```
.0agnostic/rules/static/commit_push.md
  ──copy──→ .claude/rules/commit_push.md
```

### Override (Tier 2 replaces Tier 1)

If the same file exists in both `.0agnostic/` and `.1merge/.1claude_merge/`, the merge version replaces the agnostic version:

```
.0agnostic/rules/static/testing.md         ← Agnostic version
.1merge/.1claude_merge/rules/testing.md    ← Claude-specific override

Result: .claude/rules/testing.md           ← Uses the .1merge version
```

### Addition (Tier 2 adds to Tier 3)

If a file exists only in `.1merge/.1claude_merge/`, it's added to the output without replacing anything:

```
.1merge/.1claude_merge/settings.json       ← Claude-only (no agnostic equivalent)

Result: .claude/settings.json              ← Added to .claude/
```

### Priority Order

```
.1merge/.1{tool}_merge/ content  >  .0agnostic/ content
(tool override wins)                (agnostic is default)
```

---

## When to Use .1merge/ vs .0agnostic/

| Content Type | Location | Rationale |
|-------------|----------|-----------|
| Rule that all tools follow | `.0agnostic/rules/` | Universal |
| Rule only Claude needs | `.1merge/.1claude_merge/rules/` | Tool-specific |
| Skill that works everywhere | `.0agnostic/skills/` | Universal |
| Skill using Claude-specific features | `.1merge/.1claude_merge/skills/` | Tool-specific |
| Tool settings (hooks, permissions) | `.1merge/.1{tool}_merge/` | Always tool-specific |
| Format overrides (e.g., .mdc for Cursor) | `.1merge/.1cursor_merge/` | Format-specific |
| OS-specific configuration | `.1merge/.1{tool}_merge/` or `.0agnostic/knowledge/setup/` | Depends on whether it's a tool override or reference knowledge |

---

## .1merge/ Internal Structure Convention

Each `.1{tool}_merge/` directory can use a three-tier internal structure:

```
.1claude_merge/
├── 0_synced/               # Synced from a central/parent .1merge (if applicable)
│   └── hooks/scripts/      # Shared hook scripts
├── 1_overrides/            # Override agnostic content for this tool
│   └── rules/              # Rules that replace agnostic versions
└── 2_additions/            # Add-only content for this tool
    ├── settings.json       # Tool settings (no agnostic equivalent)
    └── agents/             # Tool-specific agent definitions
```

This internal convention is optional — simpler entities can just put files directly in `.1claude_merge/` without the `0_synced/`, `1_overrides/`, `2_additions/` subdirectories.

---

## Current State

- **248 `.1merge/` directories** exist across the hierarchy
- Each contains tool-specific subdirectories (`.1claude_merge/`, `.1cursor_merge/`, `.1codex_merge/`, `.1copilot_merge/`, `.1aider_merge/`, `.1gemini_merge/`)
- Most are minimal (empty or containing only synced hook scripts)
- The pattern is established and consistent — it just needs more content as the agnostic system matures

---

## Integration with Multi-Avenue Redundancy

The `.1merge/` system enables per-tool avenue optimization:

- **Claude Code** (best avenue support): Gets rules, skills, @imports, path-scoping — all avenues active
- **Cursor** (path rules + system prompt only): Gets `.mdc` rules with auto-attach globs, static rules in `.cursorrules`
- **Codex CLI** (AGENTS.md + skills): Gets rules inlined in AGENTS.md, skills in `.agents/skills/`
- **Aider** (conventions only): Gets rules inlined in conventions file, minimal avenue coverage
- **Gemini CLI** (GEMINI.md + extensions): Gets rules in GEMINI.md, protocols as extensions

Each tool gets the maximum avenue coverage its native format supports, all generated from the same agnostic source.

---

*Merge system documentation for the 0Agnostic System*
*Created: 2026-02-16*
