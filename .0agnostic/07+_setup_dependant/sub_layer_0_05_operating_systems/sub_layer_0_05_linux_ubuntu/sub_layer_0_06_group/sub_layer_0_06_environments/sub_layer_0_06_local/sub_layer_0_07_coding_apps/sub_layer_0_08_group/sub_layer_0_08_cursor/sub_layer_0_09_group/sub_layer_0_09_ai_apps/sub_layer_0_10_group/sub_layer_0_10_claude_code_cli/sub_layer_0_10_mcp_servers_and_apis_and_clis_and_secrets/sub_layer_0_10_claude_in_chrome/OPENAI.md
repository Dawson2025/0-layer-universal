# OpenAI Context

## Identity

**Entity**: Claude in Chrome
**Type**: Feature (MCP Server within Claude Code CLI)
**Parent**: Claude Code CLI (sub_layer_0_10)
**Scope**: Browser automation via the Claude in Chrome Chrome extension — page navigation, content extraction, form automation, interactive browsing, GIF recording, and React fiber-based data extraction

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → AI Apps (09) → Claude Code CLI (10) → **Claude in Chrome (feature)**

## Key Behaviors

- Provides browser automation capabilities to Claude Code CLI via MCP protocol
- Tools include: navigation, page reading (accessibility tree), element finding, JS execution, form input, screenshots, console/network monitoring, GIF recording
- React fiber traversal is the primary method for extracting data from React-rendered pages (Perplexity citations, SPA content)
- Tab context must be established before any browser interaction
- Session startup pattern: `tabs_context_mcp` → `tabs_create_mcp` → `navigate` → `wait`

## Inputs

- Perplexity search URLs for content/citation extraction
- Target web page URLs for analysis, interaction, or automation
- Browser automation instructions from user or parent entities

## Outputs

- Extracted page content (text, citations, structured data)
- Accessibility tree snapshots
- Screenshots and GIF recordings
- Console and network monitoring data
- Form submission results

## Triggers

| Situation | Action |
|-----------|--------|
| Perplexity URL provided | Use `/perplexity-extract` skill with React fiber method |
| Web page analysis needed | Follow page analysis workflow in `.0agnostic/03_protocols/` |
| Form automation requested | Follow interactive browsing workflow in `.0agnostic/03_protocols/` |
| Content extraction needed | Follow content extraction workflow in `.0agnostic/03_protocols/` |
| Setup/troubleshooting | Read `.0agnostic/01_knowledge/setup/` |
| Entering this directory | Read `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/REGISTRY.md` |

## Resources Available

On-demand resources in `.0agnostic/` — read as needed:

### Skills
| Skill | Trigger | Definition |
|-------|---------|------------|
| `/perplexity-extract` | Perplexity URL provided | `.claude/skills/perplexity-extract/SKILL.md` |

### Rules (`.0agnostic/02_rules/static/`)
| Rule | Importance | Description |
|------|------------|-------------|
| `browser_automation_rules.md` | I1 (High) | 10 rules: tab context first, fresh tabs, no JS dialogs, wait after nav, ref over coords, scroll before extract, etc. |

### Knowledge (`.0agnostic/01_knowledge/`)
| Topic | Description |
|-------|-------------|
| `perplexity_extraction/` | React fiber method — the ONLY way to extract citation URLs from Perplexity |
| `browser_automation/` | Tool reference for all Claude in Chrome MCP tools and computer actions |
| `setup/` | MCP server setup, troubleshooting, concurrent browser config, 3 Python scripts |

### Protocols (`.0agnostic/03_protocols/`)
| Protocol | Description |
|----------|-------------|
| `content_extraction_workflow.md` | Extract content from articles, products, search results, docs |
| `page_analysis_workflow.md` | Analyze page structure, accessibility, forms, navigation |
| `interactive_browsing_workflow.md` | Form filling, multi-step nav, clicking, keyboard, GIF recording |

### Context Registry
Full avenue manifest: `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/REGISTRY.md`


## Current Status

- **State**: Migrated to .0agnostic convention (2026-02-23)
- **Scope**: 3 workflow protocols (content extraction, page analysis, interactive browsing), setup docs (README, troubleshooting, concurrent browser, MCP fix), 3 setup scripts, Perplexity React fiber extraction knowledge, 10 browser automation rules
- **Content**: Legacy `sub_layer_0_13_protocols/` and `setup/` migrated to `.0agnostic/03_protocols/` and `.0agnostic/01_knowledge/setup/` respectively. Old empty dirs (`sub_layer_0_12_universal_tools`, `sub_layer_0_14_agent_setup`) removed
- **Key Discovery**: React fiber traversal (`__reactFiber$*` → `memoizedProps.children.props`) is the ONLY reliable method for extracting citation URLs from Perplexity (standard DOM queries fail)
- **Skill**: `/perplexity-extract` registered and available — depends on this MCP server's `javascript_tool` for React fiber access

## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
