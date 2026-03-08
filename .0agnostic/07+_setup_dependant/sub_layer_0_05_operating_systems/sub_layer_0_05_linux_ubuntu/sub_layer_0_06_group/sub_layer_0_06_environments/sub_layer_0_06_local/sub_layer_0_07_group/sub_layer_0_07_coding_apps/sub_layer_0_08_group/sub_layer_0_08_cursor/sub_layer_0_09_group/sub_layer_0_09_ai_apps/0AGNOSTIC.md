---
resource_id: "13c2fcd6-74a1-4331-8a55-845819b52197"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "ff7063c9-fb84-4c10-a37c-3d1b11cc5cd7" -->
## Identity

**Entity**: AI Apps Category
**Sub-Layer**: 0.09
**Type**: Increased Specificity (narrows from Coding Apps → AI-powered coding tools)
**Scope**: All AI-powered coding assistants and their shared infrastructure

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → **AI Apps (09)**

<!-- section_id: "03abacdc-2eba-4d0c-aa6c-507b69e45e2b" -->
## Key Behaviors

- Shared protocols, knowledge, and rules cascade to all child AI app entities (level 10)
- MCP server knowledge shared across AI apps lives in `.0agnostic/01_knowledge/mcp_servers/`
- **MCP API cost tracking** — protocol and budget enforcement rule at this level apply to ALL paid MCP API calls across all child AI apps
- Browser automation protocol applies to all AI apps that use browser-based tools
- **Two entity types at level 10**: *Features* (numbered, shared infrastructure) and *Further Specificity* (unnumbered, app-specific config). Features provide shared tools, models, protocols, and agent setup; app-specific entities inherit from and can override shared features.

<!-- section_id: "65725336-b256-4061-8952-424442c9c17f" -->
## Triggers

| Situation | Action |
|-----------|--------|
| About to call a paid MCP API tool | Read `.0agnostic/02_rules/dynamic/MCP_API_BUDGET_ENFORCEMENT/` — check budget before calling |
| After calling a paid MCP API tool | Follow `.0agnostic/03_protocols/mcp_api_cost_tracking_protocol.md` — log usage |
| User asks about API spending | Read `memory/mcp_api_usage.md` and report budget status |
| Extracting content from Perplexity | Read `.0agnostic/02_rules/static/perplexity_extraction_rules.md` |

<!-- section_id: "fd36bf53-222a-493e-9149-55d63c58d8b0" -->
## Delegation Contract

**Children** (level 10):
- *Features* (numbered, shared): 01_tools_and_services, 02_ai_models, 03_universal_tools, 04_protocols, 05_agent_setup
- *Further Specificity* (app-specific): claude_code_cli, codex_cli, cursor_agent, gemini_cli
**Parent** (level 08): Cursor

# ── Current Status ──

<!-- section_id: "b9f3d131-628a-4e8c-99d4-e4020d720bad" -->
## Current Status

**State**: Active
**Scope**: 5 shared feature entities + 4 AI app entities at level 10
**Content**: Shared features contain MCP servers, AI models, universal tools, protocols, agent setup. App-specific entities contain per-app config and overrides.
**Readiness**: Restructured 2026-02-25: features extracted from Claude Code CLI to shared level

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "0cb9ac10-1807-47c6-8ee4-7cb89c97152f" -->
## Open Items

- Session handoff to be created in `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/`

# ── References ──

<!-- section_id: "3eb3ad94-834e-4f2e-87e0-0fd5487fa4fb" -->
## Navigation

| Path | Purpose |
|------|---------|
| `.0agnostic/01_knowledge/mcp_servers/` | Shared MCP server knowledge (migrated from `_shared/`) |
| `.0agnostic/01_knowledge/mcp_cost_tracking/` | Cost tracking knowledge, templates for monthly summaries |
| `.0agnostic/02_rules/static/perplexity_extraction_rules.md` | Perplexity React fiber extraction rules |
| `.0agnostic/02_rules/dynamic/MCP_API_BUDGET_ENFORCEMENT/` | Budget enforcement — $20/mo limit, warn at 80%, confirm at 100% |
| `.0agnostic/03_protocols/mcp_api_cost_tracking_protocol.md` | How to track and enforce MCP API spending |
| `.0agnostic/03_protocols/perplexity_extraction_protocol.md` | Browser-based Perplexity content extraction |
| `.0agnostic/03_protocols/browser_automation_protocol.md` | Browser automation protocol (migrated from `_shared/`) |
| `sub_layer_0_09_group/sub_layer_0_09_99_stages/` | Internal stages (12 stages) |
| `sub_layer_0_10_group/` | Children: AI app entities |
| `sub_layer_0_10_group/sub_layer_0_10_00_layer_registry/` | Layer Registry |
| `sub_layer_0_10_group/sub_layer_0_10_01_tools_and_services/` | Tools & Services |
| `sub_layer_0_10_group/sub_layer_0_10_02_ai_models/` | AI Models |
| `sub_layer_0_10_group/sub_layer_0_10_03_universal_tools/` | Universal Tools |
| `sub_layer_0_10_group/sub_layer_0_10_04_protocols/` | Protocols |
| `sub_layer_0_10_group/sub_layer_0_10_05_agent_setup/` | Agent Setup |
| `sub_layer_0_10_group/sub_layer_0_10_claude_code_cli/` | Claude Code CLI entity |
| `sub_layer_0_10_group/sub_layer_0_10_codex_cli/` | Codex CLI entity |
| `sub_layer_0_10_group/sub_layer_0_10_cursor_agent/` | Cursor Agent entity |
| `sub_layer_0_10_group/sub_layer_0_10_gemini_cli/` | Gemini CLI entity |
