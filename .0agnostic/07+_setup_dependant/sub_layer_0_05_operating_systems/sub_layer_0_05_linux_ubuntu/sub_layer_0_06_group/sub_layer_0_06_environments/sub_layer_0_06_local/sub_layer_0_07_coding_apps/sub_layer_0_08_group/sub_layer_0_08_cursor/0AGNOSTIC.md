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

## Delegation Contract

**Children** (level 09): AI Apps category (sub_layer_0_09_ai_apps)
**Parent** (level 07): Coding Apps

# ── Current Status ──

## Current Status

**State**: Restructuring complete
**Scope**: Cursor IDE entity with 1 child category (AI Apps) containing 4 AI app entities
**Content**: Entity structure created, legacy content preserved, children moved to `sub_layer_0_09_group/`
**Readiness**: Structure ready, awaiting knowledge population

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

## Navigation

| Path | Purpose |
|------|---------|
| `sub_layer_0_08_group/sub_layer_0_08_99_stages/` | Internal stages (12 stages) |
| `sub_layer_0_09_group/sub_layer_0_09_ai_apps/` | Child: AI Apps category entity |
| `.0agnostic/01_knowledge/` | Cursor-specific knowledge |
| `.0agnostic/03_protocols/` | Cursor-specific protocols |
