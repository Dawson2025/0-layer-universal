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

Content that only applies to a specific tool, or that overrides agnostic content for a particular tool.

**Each `.1{tool}_merge/` mirrors the `.0agnostic/` structure** — same subdirectories, but with content that is specific to that tool. This can mean extra sections added for that tool, sections redacted/removed for that tool, or entirely tool-specific content with no agnostic equivalent.

```
.1merge/
├── .1claude_merge/         # Claude Code-specific
├── .1cursor_merge/         # Cursor-specific
├── .1codex_merge/          # Codex CLI-specific
├── .1gemini_merge/         # Gemini CLI-specific
├── .1aider_merge/          # Aider-specific
└── .1copilot_merge/        # Copilot-specific
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

## .1merge/ Internal Structure — Mirrors .0agnostic/

Each `.1{tool}_merge/` has three internal tiers (`0_synced/`, `1_overrides/`, `2_additions/`), and **each tier mirrors the `.0agnostic/` directory structure** — same subdirectories for knowledge, rules, protocols, skills, agents, etc.

### Full Structure

```
.1claude_merge/
│
├── 0_synced/                           # Synced from a central/parent .1merge
│   ├── knowledge/                      # Synced knowledge for this tool
│   │   ├── principles/
│   │   └── resources/
│   ├── rules/
│   │   ├── static/
│   │   └── dynamic/
│   ├── protocols/
│   ├── skills/
│   ├── agents/
│   ├── hooks/
│   │   └── scripts/
│   └── scripts/
│
├── 1_overrides/                        # Override agnostic content for Claude
│   ├── knowledge/                      # Claude-specific knowledge overrides
│   │   ├── principles/                 # Principles with Claude-specific additions
│   │   └── resources/                  # Claude-specific templates/resources
│   ├── rules/
│   │   ├── static/                     # Rules that REPLACE agnostic static rules
│   │   └── dynamic/                    # Rules that REPLACE agnostic dynamic rules
│   ├── protocols/                      # Protocols with Claude-specific steps
│   ├── skills/                         # Skills overridden for Claude features
│   └── agents/                         # Agent definitions overridden for Claude
│
├── 2_additions/                        # Add-only content (no agnostic equivalent)
│   ├── knowledge/                      # Claude-only knowledge docs
│   │   ├── principles/                 # Claude-specific principles
│   │   └── resources/                  # Claude-specific resources
│   ├── rules/
│   │   ├── static/                     # Additional always-loaded Claude-only rules
│   │   └── dynamic/                    # Additional path-scoped Claude-only rules
│   ├── protocols/                      # Claude-only protocols (become Claude-only skills)
│   ├── skills/                         # Claude-only skills (no agnostic version)
│   ├── agents/                         # Claude-only agent definitions
│   └── settings.json                   # Claude Code settings (hooks, permissions)
│
└── tool_config/                        # Tool-native config (outside the mirror)
    └── settings.json                   # settings.json → .claude/settings.json
```

### How the Three Tiers Work

#### 0_synced/ — Inherited from parent

Content synced from a central or parent `.1merge/`. This is for content that is shared across multiple entities but is still tool-specific (not agnostic).

**Example:** A hook script that all Claude Code sessions should have — synced from the root `.1merge/.1claude_merge/0_synced/hooks/scripts/`.

**Rule:** Never edit files in `0_synced/` locally. They're overwritten by the parent sync.

#### 1_overrides/ — Replace agnostic content

Content that **replaces** the equivalent file from `.0agnostic/`. Same filename, same subdirectory, but with tool-specific modifications.

**How it works:**
```
.0agnostic/rules/static/testing.md          ← Agnostic version (applies to all tools)
.1merge/.1claude_merge/1_overrides/rules/static/testing.md  ← Claude override

Result: .claude/rules/testing.md            ← Uses the override version
```

**Use cases for overrides:**
- A rule that needs extra Claude-specific steps added
- A protocol that uses Claude-specific tool calls (Read, Edit, Task)
- Knowledge that includes Claude-specific examples or caveats
- A rule that needs a section redacted because it doesn't apply to Claude

**Key principle:** An override file replaces its agnostic counterpart entirely for that tool. If you only need to add a few lines, copy the agnostic file and add the tool-specific content — don't just put the additions (that's what `2_additions/` is for).

#### 2_additions/ — Tool-exclusive content

Content that has **no agnostic equivalent** — it exists only for this specific tool.

**How it works:**
```
.1merge/.1claude_merge/2_additions/rules/static/claude_hooks.md  ← Claude-only rule

Result: .claude/rules/claude_hooks.md       ← Added (no agnostic version exists)
```

**Use cases for additions:**
- `settings.json` — Claude Code hooks and permissions (no equivalent in other tools)
- Rules about Claude-specific features (Agent Teams, auto-memory, @imports)
- Skills that use Claude-only capabilities (Task tool, progressive disclosure)
- Knowledge about Claude Code internals (context compaction, skill char budget)

### Merge Priority

When the sync runs, priority order is:

```
2_additions/  >  1_overrides/  >  0_synced/  >  .0agnostic/
(additions)     (overrides)      (inherited)   (agnostic default)

Highest priority ──────────────────────────→ Lowest priority
```

If the same file exists in multiple tiers:
1. `2_additions/` wins (tool-exclusive additions take precedence)
2. `1_overrides/` wins over `0_synced/` and `.0agnostic/`
3. `0_synced/` wins over `.0agnostic/`
4. `.0agnostic/` is the default when no override exists

### Per-Tool Examples

#### Claude Code (.1claude_merge/)

```
1_overrides/
├── protocols/entity_creation.md          # Entity creation with Claude-specific steps
│                                           (uses Read, Write, Task tools explicitly)
└── rules/dynamic/research_context.md     # Research context rule with Claude-specific
                                            skill references (/context-gathering, etc.)

2_additions/
├── rules/static/claude_hooks.md          # Rule: use hooks for deterministic enforcement
├── skills/claude-project-setup/SKILL.md  # Skill: set up Claude Projects on claude.ai
├── agents/researcher.md                  # Claude-specific agent definition
└── settings.json                         # Hooks, permissions, tool settings
```

#### Cursor (.1cursor_merge/)

```
1_overrides/
├── rules/static/                         # Agnostic rules transformed to .mdc format
│   └── commit_push.mdc                   # Same rule, Cursor metadata format
└── rules/dynamic/
    └── research_context.mdc              # Same trigger, with auto-attach glob metadata

2_additions/
├── rules/static/cursor_composer.mdc      # Cursor Composer-specific rules
└── knowledge/resources/                  # Cursor-specific templates
    └── mdc_template.mdc                  # Template for creating .mdc files
```

#### Codex CLI (.1codex_merge/)

```
1_overrides/
├── protocols/entity_creation.md          # Entity creation without Claude-specific steps
└── rules/static/commit_push.md           # Commit rule adapted for Codex sandbox

2_additions/
├── knowledge/codex_sandbox.md            # Knowledge: how Codex sandboxing works
└── tool_config/
    └── config.toml                       # Codex CLI configuration
```

#### Gemini CLI (.1gemini_merge/)

```
1_overrides/
└── protocols/context_loading.md          # Context loading adapted for Gemini extensions

2_additions/
├── knowledge/gemini_extensions.md        # Knowledge: how Gemini extensions work
└── tool_config/
    └── extensions/                       # Gemini extension definitions
```

#### Aider (.1aider_merge/)

```
2_additions/
├── rules/static/aider_conventions.md     # Rules inlined into conventions.md
└── tool_config/
    └── conventions.md                    # Aider conventions file (generated)
```

### Sparse Structure Is Normal

Not every `.1{tool}_merge/` needs all subdirectories. Most will be sparse:

- **Claude Code**: Fullest — has overrides, additions, settings, agents, skills
- **Cursor**: Moderate — has format overrides (.mdc) and some additions
- **Codex CLI**: Moderate — has config.toml and protocol overrides
- **Gemini CLI**: Light — has extensions and some protocol overrides
- **Aider**: Minimal — mostly just conventions.md generation
- **Copilot**: Minimal — mostly passive

**Principle:** Only create subdirectories and files when there's actual tool-specific content. Empty directories add noise without value.

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
