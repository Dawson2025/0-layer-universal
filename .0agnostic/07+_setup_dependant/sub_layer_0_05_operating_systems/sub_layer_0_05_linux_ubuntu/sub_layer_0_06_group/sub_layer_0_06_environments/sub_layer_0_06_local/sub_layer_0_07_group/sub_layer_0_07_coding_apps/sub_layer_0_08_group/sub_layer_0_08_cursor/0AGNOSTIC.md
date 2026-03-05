---
resource_id: "1e293f61-ba04-4885-9765-2b1817ec4f4e"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "7f9bfae6-b48f-4d5e-8b43-ae14011c41cf" -->
## Identity

**Entity**: Cursor IDE
**Sub-Layer**: 0.08
**Type**: Increased Specificity (narrows from Coding Apps → Cursor IDE specifically)
**Scope**: Cursor IDE configuration, extensions, AI features, and child AI app integrations

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → **Cursor (08)**

<!-- section_id: "7e995fd4-94bc-4dad-833b-cf5a83b5954a" -->
## Key Behaviors

- Cursor-specific setup, configuration, and extensions live at this level
- AI app integrations (Claude Code CLI, Codex, Gemini, etc.) are children at level 09→10
- Rules and protocols here cascade to all AI apps running within Cursor
- Setup knowledge migrated from legacy `setup/` directory

<!-- section_id: "0ada8fbf-69c8-4822-babc-2885b1cf2456" -->
### Cursor AI Capabilities (2026)

- **Agent Mode**: Autonomous coding with subagents, auto-context pulling, file editing, terminal execution
- **Plan Mode**: Structured planning before implementation with user approval
- **Rules System**: `.cursor/rules/*.mdc` with YAML frontmatter (replaces deprecated `.cursorrules`)
- **Rule Types**: Team Rules > Project Rules > User Rules > AGENTS.md (priority order)
- **MCP Support**: Model Context Protocol servers for extended tool access
- **Background Agents**: Long-running agents that work asynchronously
- **Hooks**: Pre/post execution hooks for agent actions
- **Onboard Testing**: Visual demo verification (screenshots, video recordings, logs)

<!-- section_id: "23c70e06-1448-4c32-854e-1d70df96fe8c" -->
### Layer-Stage Integration

`agnostic-sync.sh` generates `.cursorrules` (lean format). Migration to `.cursor/rules/*.mdc` documented in `cursor_context_mapping.md`.

**Reference docs** (in this directory):
- `cursor_capabilities.md` — Full AI capabilities reference
- `cursor_context_mapping.md` — How agnostic system maps to Cursor rules

<!-- section_id: "151bfa22-9722-4775-a561-a8393d8450fb" -->
## Delegation Contract

**Children** (level 09): AI Apps category (sub_layer_0_09_ai_apps)
**Parent** (level 07): Coding Apps

# ── Current Status ──

<!-- section_id: "05c72b35-8518-45b2-bdc5-a5430d675450" -->
## Current Status

**State**: Knowledge populated
**Scope**: Cursor IDE entity with 1 child category (AI Apps) containing 4 AI app entities
**Content**: Entity structure created, AI capabilities documented, context mapping defined, .cursorrules deprecation noted
**Readiness**: Active — capabilities reference and migration guide ready
**Last Updated**: 2026-02-24

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

<!-- section_id: "84173508-2c36-4cf4-a2f7-77d462370aab" -->
## Navigation

| Path | Purpose |
|------|---------|
| `sub_layer_0_08_group/sub_layer_0_08_99_stages/` | Internal stages (12 stages) |
| `sub_layer_0_09_group/sub_layer_0_09_ai_apps/` | Child: AI Apps category entity |
| `.0agnostic/01_knowledge/` | Cursor-specific knowledge |
| `.0agnostic/03_protocols/` | Cursor-specific protocols |
| `cursor_capabilities.md` | Full AI capabilities reference (Agent mode, rules, Plan mode) |
| `cursor_context_mapping.md` | How agnostic system maps to Cursor's rule types |
