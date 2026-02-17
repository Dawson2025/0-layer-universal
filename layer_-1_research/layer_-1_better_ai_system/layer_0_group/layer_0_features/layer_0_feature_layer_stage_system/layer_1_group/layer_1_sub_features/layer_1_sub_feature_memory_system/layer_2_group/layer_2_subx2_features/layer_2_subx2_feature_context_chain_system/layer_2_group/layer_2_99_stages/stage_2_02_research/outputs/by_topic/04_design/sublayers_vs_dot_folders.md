# Design Research — Sub-Layers vs. Dot-Folder-Centric Context Organization

## Purpose

Should rules, knowledge, and protocols live in separate sub-layer directories or inside the tool-specific dot folders (.claude/, .0agnostic/, .codex/, .gemini/, .cursor/)? Primary research into how every major tool organizes context and what the industry is converging on.

---

## The Question

**Current setup (sub-layer hierarchy):**
```
layer_0_group/layer_0_04_sub_layers/
├── sub_layer_0_01_knowledge_system/    (knowledge + principles/)
├── sub_layer_0_02_rules/               (static/ + dynamic/)
├── sub_layer_0_03_protocols/
└── sub_layer_0_04+_setup_dependant/
```

**Alternative being evaluated (dot-folder-centric):**
```
.0agnostic/         ← Single source of truth (tool-neutral)
├── rules/
├── skills/
├── knowledge/
└── scripts/

.claude/            ← Generated/synced from .0agnostic/
├── rules/          (auto-loaded, high priority)
├── skills/         (progressive disclosure)
└── agents/

.codex/             ← Generated
.gemini/            ← Generated
.cursor/            ← Generated
```

---

## How Every Major Tool Organizes Context

### Claude Code (.claude/)

```
.claude/
├── CLAUDE.md           # Auto-loaded at session start
├── rules/              # Auto-loaded recursively, high priority
│   ├── code-style.md
│   └── testing.md
├── skills/             # Descriptions at start, full content on-demand
│   └── deploy/
│       └── SKILL.md
├── agents/             # Subagent definitions
└── settings.json       # Hooks and permissions
```

**Key behavior:** All `.md` files in `.claude/rules/` are auto-loaded recursively at session start with the **same priority as CLAUDE.md**. Path-specific rules use YAML frontmatter (`paths: src/api/**/*.ts`). Skills use progressive disclosure — only descriptions load at start.

### Codex CLI (.codex/ + .agents/)

```
~/.codex/
├── config.toml
├── AGENTS.md
└── skills/

project/
├── AGENTS.md
├── .codex/config.toml
└── .agents/skills/     # Shared skill location
```

**Key behavior:** AGENTS.md walks from project root to cwd. Skills scan `.agents/skills/` from cwd up to repo root.

### Gemini CLI (.gemini/)

```
~/.gemini/
├── GEMINI.md
├── settings.json
├── commands/
└── extensions/

project/.gemini/
├── GEMINI.md
├── commands/
└── extensions/
```

**Key behavior:** Extensions bundle skills, commands, sub-agents, and MCP servers. Skills are inside extensions, not standalone.

### Cursor (.cursor/)

```
.cursor/
└── rules/
    ├── general.mdc     # Always-loaded
    ├── typescript.mdc   # Auto-attached to *.ts files
    └── testing.mdc      # Agent-requested
```

**Key behavior:** Four activation modes: Always, Auto-Attach (by file glob), Agent Requested (AI decides), Manual. Uses `.mdc` format (not plain `.md`).

### Feature Comparison

| Feature | Claude Code | Codex CLI | Gemini CLI | Cursor |
|---------|------------|-----------|------------|--------|
| Dot folder | `.claude/` | `.codex/` | `.gemini/` | `.cursor/` |
| Rules auto-load | Yes (recursive) | N/A (in AGENTS.md) | N/A (in GEMINI.md) | Yes (by type) |
| Path-specific rules | YAML frontmatter | Proximity-based | Extension scoping | File pattern metadata |
| Skills | `.claude/skills/` | `.agents/skills/` | Extension `skills/` | N/A |
| Progressive disclosure | Yes (native) | Yes (native) | Via extensions | Partial |
| Cross-tool standard | No | AGENTS.md | AGENTS.md (partial) | AGENTS.md |

---

## The Critical Finding: Auto-Discovery

**Tools reliably read from their native dot folders.** Claude Code auto-loads all `.md` files from `.claude/rules/` recursively at session start with high priority. Codex scans `.agents/skills/`. Cursor loads `.cursor/rules/*.mdc`.

**Separate hierarchy directories are NOT auto-discovered.** If knowledge lives in `layer_0/layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/`, no tool will find it without explicit instructions in CLAUDE.md. The agent must be told to look there, and even then the content loads as standard file content (not high-priority rules).

| Aspect | In .claude/rules/ | In separate sub-layer |
|--------|-------------------|----------------------|
| Auto-loaded | Yes, at session start | No, must be explicitly read |
| Priority | High (same as CLAUDE.md) | Standard (file content level) |
| Path-scoping | Native YAML frontmatter | Manual, requires agent awareness |
| Discovery | Automatic, recursive | Requires @import or agent search |
| Context cost | Loaded once, stays in context | Read on-demand, re-read each time |

---

## Tradeoffs

### Dot-Folder Approach

**Advantages:**
- Native auto-discovery and auto-loading by the tool
- Path-specific scoping built in
- Progressive disclosure (skills load descriptions only until invoked)
- Consistent with industry patterns (every major tool does this)
- Lower context waste (tool manages what loads when)

**Disadvantages:**
- Tied to each tool's conventions (different folder names, formats)
- Maintaining parallel dot folders creates duplication
- No single human-readable overview of all rules and knowledge
- Tool-specific limitations (Cursor uses .mdc, not .md)

### Separate Sub-Layer Hierarchy

**Advantages:**
- Tool-agnostic organization
- Clear taxonomy (knowledge vs rules vs protocols)
- Single source of truth
- Serves as documentation

**Disadvantages:**
- No tool auto-discovers content from custom directories
- Requires explicit @import or agent instructions to access
- Content loads as standard file reads (not high-priority)
- No native path-scoping or progressive disclosure
- Agent must be taught the hierarchy (context cost)

### Hybrid: Agnostic Source Generating Tool-Specific Files

**Advantages:**
- Single source of truth (edit once, propagate everywhere)
- Native tool integration (each tool gets files in expected format)
- Industry trend: tools like ai-rules-sync and the .agents/ convention are emerging for exactly this

**Disadvantages:**
- Build step required (must sync after edits)
- Two copies of everything
- Debugging confusion about which is "real"

---

## What Experienced Users Recommend

### Anthropic's Official Guidance
- Use `.claude/rules/` for modular, topic-specific instructions
- Keep CLAUDE.md under 100-200 lines, move details to per-folder files
- Use skills for reference content with progressive disclosure

### Industry Convergence on AGENTS.md
The AGENTS.md specification (now under the Linux Foundation's AAIF) has been adopted by 40,000+ repos. Recommended pattern:
1. Maintain `AGENTS.md` at project root as canonical file
2. Symlink `CLAUDE.md -> AGENTS.md` for Claude Code compatibility
3. Use `.agents/skills/` for shared skills
4. Use tool-specific dot folders only for tool-specific overrides

### Three-Tier Architecture (Alexander Opalic)
1. **Always-loaded** (CLAUDE.md): Under 60 lines, project overview, pointers
2. **On-demand** (/docs folder): Domain-specific knowledge, loaded when referenced
3. **Specialized agents** (.claude/agents/): Domain experts in forked contexts

### AI-Rules-Sync Tool
The [ai-rules-sync](https://github.com/lbb00/ai-rules-sync) project supports 8 tools: one rules repository with symlinks into each tool's expected directory.

---

## Migration Mapping: Sub-Layers → Dot-Folder-Centric

| Current Sub-Layer | New Location | Rationale |
|-------------------|-------------|-----------|
| `sub_layer_0_01_knowledge_system/` | `.0agnostic/knowledge/` + referenced via @imports in skills | Knowledge docs don't need auto-loading; use progressive disclosure |
| `sub_layer_0_01_knowledge_system/principles/` | `.0agnostic/rules/principles.md` (if short) or `.0agnostic/knowledge/principles/` (if large) | Core principles should be auto-loaded rules; detailed docs stay as knowledge |
| `sub_layer_0_02_rules/static/` | `.0agnostic/rules/` → synced to `.claude/rules/` | Static rules get auto-loaded by the tool natively |
| `sub_layer_0_02_rules/dynamic/` | `.0agnostic/rules/` with path-specific YAML frontmatter | Dynamic rules become path-scoped rules in the tool's native format |
| `sub_layer_0_03_protocols/` | `.0agnostic/skills/` → synced to `.claude/skills/` | Protocols are procedural; they map perfectly to skills |
| `sub_layer_0_04+_setup_dependant/` | `.0agnostic/knowledge/setup/` or tool-specific overrides in `.1merge/` | Setup-dependent content varies by tool |

---

## Proposed Structure

```
entity/
├── 0AGNOSTIC.md                 # Master context (source of truth)
├── AGENTS.md                    # Generated from 0AGNOSTIC.md (cross-tool standard)
├── CLAUDE.md -> AGENTS.md       # Symlink for Claude Code
│
├── .0agnostic/                  # SINGLE SOURCE OF TRUTH
│   ├── rules/                   # Tool-agnostic rules (auto-synced to dot folders)
│   │   ├── code-style.md
│   │   ├── testing.md
│   │   └── principles.md        # Core principles (short, always-loaded)
│   ├── skills/                  # Tool-agnostic skills (synced to dot folders)
│   │   ├── deploy/SKILL.md
│   │   └── review/SKILL.md
│   ├── knowledge/               # Reference docs (NOT synced — accessed via @import/skills)
│   │   ├── principles/          # Detailed principle docs
│   │   ├── architecture/
│   │   └── domain/
│   ├── episodic_memory/         # Session records
│   └── scripts/
│       └── agnostic-sync.sh
│
├── .1merge/                     # Tool-specific overrides (3-tier merge)
│   ├── claude/                  # Claude Code additions
│   ├── cursor/                  # Cursor additions (.mdc format)
│   └── codex/                   # Codex additions
│
├── .claude/                     # GENERATED + Claude-specific
│   ├── rules/                   # Synced from .0agnostic/rules/
│   ├── skills/                  # Synced from .0agnostic/skills/
│   ├── agents/                  # Claude-specific
│   └── settings.json
│
├── .cursor/                     # GENERATED (transformed to .mdc)
│   └── rules/
│
└── .codex/                      # GENERATED
    └── config.toml
```

### Key Principles

1. **Rules go in dot folders** — auto-loaded, high priority, path-scoped
2. **Procedures/protocols become skills** — progressive disclosure, on-demand loading
3. **Knowledge stays in a reference directory** — accessed via @imports or skill references, not auto-loaded
4. **Agnostic source is the canonical version** — edit `.0agnostic/`, sync to dot folders
5. **Symlinks over copies where possible** — reduces sync burden
6. **Tool-specific overrides in `.1merge/`** — existing pattern is sound

### Why This Is Better Than Sub-Layers

1. **Auto-discovery**: Tools natively find and load content from their dot folders
2. **Correct priority**: Rules in `.claude/rules/` get high priority. Files from arbitrary directories get standard priority.
3. **Progressive disclosure**: Skills provide built-in lazy loading. Sub-layer directories have none.
4. **Industry alignment**: Every tool, guide, and community pattern uses dot-folder organization
5. **Reduced context waste**: Agent doesn't need context window space to remember sub-layer hierarchy
6. **The existing .0agnostic/ pattern is ahead of the curve**: The industry is converging on exactly this approach (ai-rules-sync, .agents/ convention, AGENTS.md symlinks)

---

## Sources

- [Claude Code Memory Documentation](https://code.claude.com/docs/en/memory)
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
- [Claude Code Rules Directory Guide](https://claudefa.st/blog/guide/mechanics/rules-directory)
- [Inside Claude Code Skills](https://mikhail.io/2025/10/claude-code-skills/)
- [Stop Bloating Your CLAUDE.md: Progressive Disclosure](https://alexop.dev/posts/stop-bloating-your-claude-md-progressive-disclosure-ai-coding-tools/)
- [Codex CLI Custom Instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md/)
- [Codex CLI Agent Skills](https://developers.openai.com/codex/skills/)
- [AGENTS.md Specification](https://github.com/agentsmd/agents.md)
- [Keep your AGENTS.md in sync — Kaushik Gopal](https://kau.sh/blog/agents-md/)
- [AI Rules Sync Tool](https://github.com/lbb00/ai-rules-sync)
- [AGENTS.md: One File to Guide Them All — Layer5](https://layer5.io/blog/ai/agentsmd-one-file-to-guide-them-all/)
- [AGENTS.md vs CLAUDE.md vs GEMINI.md Comparison](https://www.xugj520.cn/en/archives/ai-agent-configuration-comparison.html)
- [Gemini CLI Extensions](https://geminicli.com/docs/extensions/)
- [Cursor Rules Best Practices](https://medium.com/elementor-engineers/cursor-rules-best-practices-for-developers-16a438a4935c)
- [Cursor Rules Complete Guide](https://eastondev.com/blog/en/posts/dev/20260110-cursor-rules-complete-guide/)
- [Context Engineering for Coding Agents — Martin Fowler](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)
- [Claude Code in Large Monorepos](https://github.com/shanraisshan/claude-code-best-practice/blob/main/reports/claude-md-for-larger-mono-repos.md)
- [Claude Code Path-Specific Rules](https://paddo.dev/blog/claude-rules-path-specific-native/)
- [The Ultimate Guide to CLAUDE.md in 2026](https://www.buildcamp.io/guides/the-ultimate-guide-to-claudemd)

---

*Research: Sub-layers vs. dot-folder-centric context organization*
*Conducted: 2026-02-16*
