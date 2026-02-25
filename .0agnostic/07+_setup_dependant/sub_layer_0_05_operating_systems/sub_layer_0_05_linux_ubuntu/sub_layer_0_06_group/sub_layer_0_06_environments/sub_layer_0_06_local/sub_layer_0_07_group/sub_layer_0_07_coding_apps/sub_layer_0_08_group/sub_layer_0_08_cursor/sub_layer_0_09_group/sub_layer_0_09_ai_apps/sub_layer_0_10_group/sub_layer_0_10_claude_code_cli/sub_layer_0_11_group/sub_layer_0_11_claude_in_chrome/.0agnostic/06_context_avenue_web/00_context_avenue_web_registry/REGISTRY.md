# Context Avenue Web Registry — Claude in Chrome

**Entity**: Claude in Chrome (MCP Server Feature)
**Last Updated**: 2026-02-23

## Available Context Avenues

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

### Data-Based Avenues (09-13)

| # | Avenue | Status | Content |
|---|--------|--------|---------|
| 09 | Knowledge Graph | Empty | Not implemented |
| 10 | Relational Index | Empty | Not implemented |
| 11 | Vector Embeddings | Empty | Not implemented |
| 12 | Temporal Index | Empty | Not implemented |
| 13 | Shimi Structures | Empty | Not implemented |

## Quick Resource Index

### Rules (02_rules/)
| File | Type | Importance | Description |
|------|------|------------|-------------|
| `static/browser_automation_rules.md` | Static | I1 (High) | 10 rules for Claude in Chrome browser automation |

### Knowledge (01_knowledge/)
| Topic | Description |
|-------|-------------|
| `setup/` | MCP server setup, troubleshooting, concurrent browser config, scripts |
| `perplexity_extraction/` | React fiber extraction method — the ONLY way to get citation URLs from Perplexity |
| `browser_automation/` | Tool reference for all Claude in Chrome MCP tools and actions |

### Protocols (03_protocols/)
| Protocol | Description |
|----------|-------------|
| `content_extraction_workflow.md` | Patterns for extracting content from web pages (articles, products, search results) |
| `page_analysis_workflow.md` | Analyzing page structure, accessibility, forms, navigation |
| `interactive_browsing_workflow.md` | Form filling, multi-step navigation, clicking, keyboard, GIF recording |

### Skills (06_context_avenue_web/01_file_based/05_skills/)
| Skill | Trigger | Location |
|-------|---------|----------|
| `/perplexity-extract` | User provides Perplexity URL | `.claude/skills/perplexity-extract/SKILL.md` |

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
