---
resource_id: "26a3a927-250a-4c4c-bf23-cb617bb4375d"
resource_type: "document"
resource_name: "REGISTRY"
---
# Context Avenue Web Registry — Claude in Chrome

**Entity**: Claude in Chrome (MCP Server Feature)
**Last Updated**: 2026-02-23

<!-- section_id: "8128ec08-219d-433e-8bca-486ffb99bb0c" -->
## Available Context Avenues

<!-- section_id: "bfc6f411-8daf-4c3b-9445-8c2f787b9670" -->
### File-Based Avenues (01-08)

| # | Avenue | Status | Content |
|---|--------|--------|---------|
| 01 | AALang | Empty | No agent definitions yet |
| 02 | AALang Markdown Integration | Empty | No integration summaries yet |
| 03 | Auto Memory | Empty | No auto-memory topic files yet |
| 04 | @Import References | Empty | No cross-references yet |
| **05** | **Skills** | **Active** | `/perplexity-extract` skill registration |
| 06 | Agents | Empty | No lightweight agent stubs yet |
| 07 | Path-Specific Rules | Empty | Rules live in `.claude/rules/setup-dependant-context.md` |
| 08 | Hooks | Empty | No event-triggered scripts yet |

<!-- section_id: "0527ca00-8949-4ff8-8a21-34e31fb0143a" -->
### Data-Based Avenues (09-13)

| # | Avenue | Status | Content |
|---|--------|--------|---------|
| 09 | Knowledge Graph | Empty | Not implemented |
| 10 | Relational Index | Empty | Not implemented |
| 11 | Vector Embeddings | Empty | Not implemented |
| 12 | Temporal Index | Empty | Not implemented |
| 13 | Shimi Structures | Empty | Not implemented |

<!-- section_id: "5439521c-7aac-4b97-a20c-67620555c97c" -->
## Quick Resource Index

<!-- section_id: "006453d8-c629-4abc-81f2-d7500c3ad934" -->
### Rules (02_rules/)
| File | Type | Importance | Description |
|------|------|------------|-------------|
| `static/browser_automation_rules.md` | Static | I1 (High) | 10 rules for Claude in Chrome browser automation |

<!-- section_id: "be25b5da-66a4-4d09-ac8b-dad9e1d9c39c" -->
### Knowledge (01_knowledge/)
| Topic | Description |
|-------|-------------|
| `setup/` | MCP server setup, troubleshooting, concurrent browser config, scripts |
| `perplexity_extraction/` | React fiber extraction method — the ONLY way to get citation URLs from Perplexity |
| `browser_automation/` | Tool reference for all Claude in Chrome MCP tools and actions |

<!-- section_id: "bf665d81-b6dd-49f7-99f7-dcf3f9f0c4ed" -->
### Protocols (03_protocols/)
| Protocol | Description |
|----------|-------------|
| `content_extraction_workflow.md` | Patterns for extracting content from web pages (articles, products, search results) |
| `page_analysis_workflow.md` | Analyzing page structure, accessibility, forms, navigation |
| `interactive_browsing_workflow.md` | Form filling, multi-step navigation, clicking, keyboard, GIF recording |

<!-- section_id: "30a97a41-f3c9-46f9-9fc9-2c66fe0962a2" -->
### Skills (06_context_avenue_web/01_file_based/05_skills/)
| Skill | Trigger | Location |
|-------|---------|----------|
| `/perplexity-extract` | User provides Perplexity URL | `.claude/skills/perplexity-extract/SKILL.md` |

<!-- section_id: "bd1377fa-47b7-4a8f-ba8c-6ae45a84d4f2" -->
## Inheritance Chain

This feature inherits context from (read bottom-up):
```
~/.0agnostic/                           ← User-level (highest priority)
0_layer_universal/.0agnostic/           ← Root (cascades everywhere)
  └── 07+_setup_dependant/
      └── sub_layer_0_07_coding_apps/.0agnostic/    ← Coding apps shared
          └── sub_layer_0_08_cursor/.0agnostic/     ← Cursor-specific
              └── sub_layer_0_09_ai_apps/.0agnostic/ ← AI apps shared (rules, protocols, handoffs)
                  └── sub_layer_0_10_claude_code_cli/.0agnostic/ ← Claude Code CLI
                      └── claude_in_chrome/.0agnostic/           ← THIS LEVEL (most specific)
```

Rules/knowledge from higher levels cascade down. This level can override or extend.
