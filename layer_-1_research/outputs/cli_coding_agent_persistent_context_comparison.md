---
resource_id: "bd8aaa4a-242f-4bfa-bee7-4ef2c8d86415"
resource_type: "output"
resource_name: "cli_coding_agent_persistent_context_comparison"
---
# CLI Coding Agent Tools: Persistent Context & Configuration Comparison

> **Layer**: -1 (Research) | **Stage**: 02 (Research) | **Date**: 2026-02-07

---

## Quick Comparison Table

| Feature | Claude Code | OpenAI Codex CLI | Gemini CLI | Aider | Cursor |
|---|---|---|---|---|---|
| **Context File** | `CLAUDE.md` | `AGENTS.md` | `GEMINI.md` | `CONVENTIONS.md` (via `--read`) | `.cursor/rules/*.mdc` or `AGENTS.md` |
| **Config File** | `.claude/settings.json` | `~/.codex/config.toml` | `~/.gemini/settings.json` | `.aider.conf.yml` | `.cursor/rules/` dir |
| **Persistent Across Sessions** | Yes (auto-loaded) | Yes (auto-loaded) | Yes (auto-loaded) | Yes (if in `.aider.conf.yml`) | Yes (auto-loaded) |
| **Hierarchical Loading** | Yes (managed > local > project > user) | Yes (global > repo root > CWD) | Yes (global > project root > subdirs) | Yes (home > git root > CWD) | Yes (team > project > user) |
| **Enterprise Lockdown** | Yes (`managed-settings.json`) | No native mechanism | Yes (`admin.*` settings, system overrides) | No | Team rules (limited) |
| **Structured Config Format** | JSON (`settings.json`) | TOML (`config.toml`) + YAML (`openai.yaml`) | JSON (`settings.json`) | YAML (`.aider.conf.yml`) | MDC frontmatter (YAML-like) |
| **Multi-Agent Orchestration** | Yes (subagents, TeammateTool) | Yes (Agents SDK + MCP) | Yes (extensions, Jules, experimental) | Limited (architect mode = 2-model) | Yes (Cursor 2.0 parallel agents) |
| **Skills / Commands** | Yes (`.claude/commands/`, skills) | Yes (`SKILL.md` directories) | Yes (extensions ecosystem, 70+) | No native skill system | No native skill system |
| **MCP Support** | Yes (first-class) | Yes (MCP server mode) | Yes (`mcpServers` config) | No | Yes (first-class) |
| **Override Mechanism** | `settings.local.json`, managed settings | `AGENTS.override.md` | System settings override | `--config` flag | Team rules override |
| **Max Context Size** | No documented limit | 32 KiB default (`project_doc_max_bytes`) | No documented limit | No documented limit | No documented limit |

---

## Detailed Analysis

### 1. Claude Code

**Context File**: `CLAUDE.md`
- Placed at project root, parent directories, or `~/.claude/CLAUDE.md` for global scope
- Becomes part of the system prompt; auto-loaded every session
- No required format -- plain markdown, free-form
- `/init` command auto-generates a starter CLAUDE.md by analyzing the codebase

**Settings Hierarchy** (highest to lowest priority):
1. **Managed** (`/etc/claude-code/managed-settings.json`) -- IT-deployed, cannot be overridden
2. **Command-line arguments**
3. **Local** (`.claude/settings.local.json`) -- personal, gitignored
4. **Project** (`.claude/settings.json`) -- team-shared, committed
5. **User** (`~/.claude/settings.json`) -- personal, all projects

**Enterprise Lockdown**:
- `managed-settings.json` at system paths (Linux: `/etc/claude-code/`, macOS: `/Library/Application Support/ClaudeCode/`)
- Controls: `allowManagedHooksOnly`, `allowManagedPermissionRulesOnly`, `disableBypassPermissionsMode`
- MCP server allowlisting/denylisting
- Plugin marketplace restrictions (`strictKnownMarketplaces`)

**Structured Formats**:
- `settings.json` (JSON) for permissions, env vars, model selection, hooks, sandbox config
- Permission rules use a `Tool(specifier)` syntax (e.g., `Bash(npm run *)`, `Read(./.env)`)
- Hooks system for lifecycle events

**Multi-Agent Orchestration**:
- Built-in subagents: Plan Subagent, Explore Subagent (Haiku-powered)
- Custom subagents via `.claude/agents/` directory or `--agents` flag
- Subagent config: description, prompt, tools, disallowedTools, model, permissionMode, mcpServers, hooks, maxTurns, skills, memory
- TeammateTool for agent-to-agent communication in swarm patterns
- Persistent memory directories that survive across conversations

**Skills/Commands**:
- Custom slash commands in `.claude/commands/` (markdown files)
- Skills inject domain knowledge into subagent context
- Support `$ARGUMENTS` and numbered placeholders (`$1`, `$2`)

---

### 2. OpenAI Codex CLI

**Context File**: `AGENTS.md`
- Discovered hierarchically: global (`~/.codex/`) then repo root down to CWD
- `AGENTS.override.md` takes precedence over `AGENTS.md` at each level
- Files concatenated root-downward; later files override earlier guidance
- `/init` command generates starter file

**Settings**:
- `~/.codex/config.toml` for global configuration
- Configurable: `project_doc_fallback_filenames`, `project_doc_max_bytes` (32 KiB default)
- `CODEX_HOME` env var for profile isolation
- Feature flags via `[features]` section in config.toml

**Enterprise Lockdown**: No native managed/lockdown settings mechanism documented.

**Structured Formats**:
- TOML for configuration (`config.toml`)
- YAML for skill metadata (`agents/openai.yaml`)
- YAML frontmatter in `SKILL.md` files (name, description required)

**Multi-Agent Orchestration**:
- Codex CLI can be exposed as an MCP server
- OpenAI Agents SDK integration for multi-agent workflows
- Supports patterns like Project Manager, Designer, Frontend/Backend Developer, Tester
- Deterministic, auditable workflow pipelines

**Skills System**:
- Directories with `SKILL.md` + optional scripts, references, assets
- Progressive disclosure: metadata loaded first, full instructions on use
- Discovery hierarchy: CWD > parent > repo root > user home > admin (`/etc/codex/skills`) > built-in
- Explicit activation via `/skills` or implicit via description matching
- Remote skill marketplace with `$skill-installer`
- Personal skills at `~/.agents/skills`
- Disable without deletion via config.toml

---

### 3. Gemini CLI

**Context File**: `GEMINI.md`
- Global: `~/.gemini/GEMINI.md`
- Project: `GEMINI.md` in CWD and parent dirs up to `.git` root
- Subdirectory: `GEMINI.md` in child dirs (respects `.gitignore`, `.geminiignore`)
- Modular imports via `@file.md` syntax (relative and absolute paths)
- Configurable filename via `settings.json` `context.fileName` property
- `/memory add <text>` appends to global GEMINI.md on the fly
- `/memory refresh` re-scans all context files

**Settings Hierarchy**:
1. System defaults
2. User settings (`~/.gemini/settings.json`)
3. Project settings (`.gemini/settings.json`)
4. System overrides (enterprise, highest priority)
5. Environment variables and CLI args override all files

**Enterprise Lockdown**:
- System settings override all others
- `admin.secureModeEnabled` -- disallows YOLO mode
- `admin.extensions.enabled` -- disables extension installation
- `admin.mcp.enabled` -- disables MCP servers
- `admin.skills.enabled` -- disables agent skills
- `security.auth.enforcedType` -- mandates authentication methods
- `security.blockGitExtensions`, `security.allowedExtensions` (regex allowlisting)
- Environment variable redaction for sensitive values

**Structured Formats**:
- JSON (`settings.json`) with categories: general, ui, model, tools, security, privacy, experimental
- Tools approval modes: `default`, `auto_edit`, `plan`, YOLO
- Sandbox configuration (boolean, string path, or env var)
- MCP server config with per-server tool filtering (`includeTools`, `excludeTools`)

**Multi-Agent Orchestration**:
- Experimental `experimental.enableAgents` toggle
- Local and remote subagents with YOLO-mode enforcement
- Agent-specific overrides via `agents.overrides`
- Jules extension for async task delegation (`/jules` command)
- Ralph extension for iterative self-correcting loops
- Community multi-agent orchestrator projects
- Official multi-agent architecture proposal (team lead + specialized agents)

**Extensions Ecosystem**:
- 70+ extensions as of late 2025
- Install/manage via CLI flags
- Major industry partner integrations
- MCP server support with trust flags and admin configuration

---

### 4. Aider

**Context File**: `CONVENTIONS.md` (loaded via `--read` or `.aider.conf.yml`)
- Not auto-discovered; must be explicitly loaded
- Loaded as read-only with prompt caching support
- Community-contributed conventions repository on GitHub
- Simple markdown format for coding guidelines

**Configuration**:
- `.aider.conf.yml` searched in: home dir > git root > CWD (last wins)
- YAML format supporting bulleted or inline list syntax
- Covers: model selection, API keys, cache/performance, git integration, linting, testing, voice, UI
- Override with `--config <filename>` for specific file only
- `.env` file for non-OpenAI/Anthropic API keys

**Enterprise Lockdown**: No native managed/lockdown settings mechanism.

**Structured Formats**:
- YAML (`.aider.conf.yml`) -- the most structured config among the tools
- Supports per-language lint commands, test commands, git integration settings
- Model aliases and API base URL configuration

**Multi-Agent Orchestration**:
- **Architect Mode**: Two-model pattern (architect proposes, editor implements)
- Effective with reasoning models (o1) paired with editing models (GPT-4o, Sonnet)
- Four chat modes: code, ask, architect, help
- No native multi-agent swarm or subagent system
- Third-party orchestration projects exist (e.g., 112 specialized agents community repo)

**Skills/Commands**: No native skill or custom command system.

---

### 5. Cursor

**Context File**: `.cursor/rules/` directory (`.mdc` or `.md` files) or `AGENTS.md`
- Legacy `.cursorrules` file still supported but being deprecated
- MDC format with YAML-like frontmatter: `description`, `alwaysApply`, `globs`

**Rule Types**:
1. **Always Apply** -- included in every session
2. **Apply Intelligently** -- agent decides based on description field
3. **Apply to Specific Files** -- triggered by glob pattern matches
4. **Apply Manually** -- activated via `@mention` in chat

**Settings Hierarchy**: Team Rules > Project Rules > User Rules

**Enterprise Lockdown**: Team rules provide organizational override but no system-level managed settings.

**Structured Formats**:
- MDC frontmatter (YAML-like metadata in `.mdc` files)
- Glob patterns for file-scoped rules
- Remote rules from GitHub repositories (public/private)

**Multi-Agent Orchestration**:
- Cursor 2.0: Up to 8 parallel agents on a single prompt
- Uses git worktrees or remote machines to prevent file conflicts
- Subagents with custom prompts, tool access, and model selection
- Background agents for async "fire and forget" tasks

**MCP Support**: First-class MCP integration with `/mcp enable` and `/mcp disable` commands.

**Skills/Commands**: No native skill system; relies on rules and MCP servers for extensibility.

---

## Key Insights

### Context File Naming Convention
All major tools have converged on a `TOOLNAME.md` pattern: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`. Cursor adopted `AGENTS.md` as an alternative alongside its own `.cursor/rules/` system. Aider is the outlier, requiring explicit loading of `CONVENTIONS.md`.

### Enterprise Control
Claude Code and Gemini CLI have the most mature enterprise lockdown features with system-level managed settings that cannot be overridden. Codex CLI, Aider, and Cursor lack equivalent system-level lockdown.

### Structured vs. Freeform
All tools accept freeform markdown for instructions. For structured configuration:
- Claude Code uses JSON (`settings.json`)
- Codex CLI uses TOML (`config.toml`) + YAML (`openai.yaml`)
- Gemini CLI uses JSON (`settings.json`) with the richest category structure
- Aider uses YAML (`.aider.conf.yml`) -- most traditional config approach
- Cursor uses MDC frontmatter -- unique glob-pattern-based rule targeting

### Multi-Agent Maturity
| Tool | Level | Approach |
|------|-------|----------|
| Claude Code | Advanced | Native subagents, TeammateTool, persistent memory, swarm patterns |
| Codex CLI | Advanced | Agents SDK integration, MCP server mode, skill-based orchestration |
| Gemini CLI | Moderate | Extensions (Jules, Ralph), experimental agent toggle, community orchestrators |
| Cursor | Moderate | Parallel agents (up to 8), background agents, subagents |
| Aider | Basic | Architect mode only (2-model pattern), no native multi-agent |

### Skills / Extensibility
Codex CLI has the most structured skill system (SKILL.md with YAML frontmatter, progressive disclosure, hierarchical discovery). Claude Code has custom commands and skills injected into subagents. Gemini CLI has a rich extension ecosystem (70+). Aider and Cursor have no native skill systems.

---

## Sources

- [Claude Code Settings Documentation](https://code.claude.com/docs/en/settings)
- [Using CLAUDE.md Files - Anthropic Blog](https://claude.com/blog/using-claude-md-files)
- [Claude Code Subagents Documentation](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Customization Guide](https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/)
- [OpenAI Codex AGENTS.md Guide](https://developers.openai.com/codex/guides/agents-md/)
- [OpenAI Codex Skills](https://developers.openai.com/codex/skills)
- [OpenAI Codex with Agents SDK](https://developers.openai.com/codex/guides/agents-sdk/)
- [Codex CLI Features](https://developers.openai.com/codex/cli/features/)
- [Codex Config Reference](https://developers.openai.com/codex/config-reference/)
- [Gemini CLI GEMINI.md Documentation](https://geminicli.com/docs/cli/gemini-md/)
- [Gemini CLI Configuration](https://geminicli.com/docs/get-started/configuration/)
- [Gemini CLI Extensions](https://geminicli.com/extensions/)
- [Gemini CLI Multi-Agent Architecture Proposal](https://github.com/google-gemini/gemini-cli/discussions/7637)
- [Jules Extension for Gemini CLI](https://cloud.google.com/blog/topics/developers-practitioners/master-multi-tasking-with-the-jules-extension-for-gemini-cli)
- [Aider YAML Config Documentation](https://aider.chat/docs/config/aider_conf.html)
- [Aider Conventions Documentation](https://aider.chat/docs/usage/conventions.html)
- [Aider Chat Modes](https://aider.chat/docs/usage/modes.html)
- [Aider Conventions Repository](https://github.com/Aider-AI/conventions)
- [Cursor Rules Documentation](https://cursor.com/docs/context/rules)
- [Cursor 2.0 Changelog](https://cursor.com/changelog/2-0)
- [Cursor 2.0 Multi-Agent Suite](https://skywork.ai/blog/vibecoding/cursor-2-0-multi-agent-suite/)
