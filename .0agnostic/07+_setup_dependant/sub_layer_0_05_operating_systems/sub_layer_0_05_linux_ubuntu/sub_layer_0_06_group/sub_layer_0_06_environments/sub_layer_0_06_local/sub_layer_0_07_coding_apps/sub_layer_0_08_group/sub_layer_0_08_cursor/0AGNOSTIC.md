# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

**Entity**: Cursor IDE
**Sub-Layer**: 0.08
**Type**: Increased Specificity (narrows from Coding Apps → Cursor IDE specifically)
**Scope**: Cursor IDE configuration, extensions, AI features, and child AI app integrations

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → **Cursor (08)**

## Key Behaviors

- Cursor-specific setup, configuration, and extensions live at this level
- AI app integrations (Claude Code CLI, Codex, Gemini, etc.) are children at level 09→10
- Rules and protocols here cascade to all AI apps running within Cursor
- Setup knowledge migrated from legacy `setup/` directory

### Cursor AI Capabilities (2026)

- **Agent Mode**: Autonomous coding with subagents, auto-context pulling, file editing, terminal execution
- **Plan Mode**: Structured planning before implementation with user approval
- **Rules System**: `.cursor/rules/*.mdc` with YAML frontmatter (replaces deprecated `.cursorrules`)
- **Rule Types**: Team Rules > Project Rules > User Rules > AGENTS.md (priority order)
- **MCP Support**: Model Context Protocol servers for extended tool access
- **Background Agents**: Long-running agents that work asynchronously
- **Hooks**: Pre/post execution hooks for agent actions
- **Onboard Testing**: Visual demo verification (screenshots, video recordings, logs)

### Layer-Stage Integration

`agnostic-sync.sh` generates `.cursorrules` (lean format). Migration to `.cursor/rules/*.mdc` documented in `cursor_context_mapping.md`.

**Reference docs** (in this directory):
- `cursor_capabilities.md` — Full AI capabilities reference
- `cursor_context_mapping.md` — How agnostic system maps to Cursor rules

## Delegation Contract

**Children** (level 09): AI Apps category (sub_layer_0_09_ai_apps)
**Parent** (level 07): Coding Apps

# ── Current Status ──

## Current Status

**State**: Knowledge populated
**Scope**: Cursor IDE entity with 1 child category (AI Apps) containing 4 AI app entities
**Content**: Entity structure created, AI capabilities documented, context mapping defined, .cursorrules deprecation noted
**Readiness**: Active — capabilities reference and migration guide ready
**Last Updated**: 2026-02-24

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

## Navigation

| Path | Purpose |
|------|---------|
| `sub_layer_0_08_group/sub_layer_0_08_99_stages/` | Internal stages (12 stages) |
| `sub_layer_0_09_group/sub_layer_0_09_ai_apps/` | Child: AI Apps category entity |
| `.0agnostic/01_knowledge/` | Cursor-specific knowledge |
| `.0agnostic/03_protocols/` | Cursor-specific protocols |
| `cursor_capabilities.md` | Full AI capabilities reference (Agent mode, rules, Plan mode) |
| `cursor_context_mapping.md` | How agnostic system maps to Cursor's rule types |
