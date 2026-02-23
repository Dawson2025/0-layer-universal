# Claude in Chrome MCP Server

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

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

# ── Current Status ──

## Current Status

- **State**: Migrated to .0agnostic convention (2026-02-23)
- **Scope**: 3 workflow protocols (content extraction, page analysis, interactive browsing), setup docs (README, troubleshooting, concurrent browser, MCP fix), 3 setup scripts, Perplexity React fiber extraction knowledge, 10 browser automation rules
- **Content**: Legacy `sub_layer_0_13_protocols/` and `setup/` migrated to `.0agnostic/03_protocols/` and `.0agnostic/01_knowledge/setup/` respectively. Old empty dirs (`sub_layer_0_12_universal_tools`, `sub_layer_0_14_agent_setup`) removed
- **Key Discovery**: React fiber traversal (`__reactFiber$*` → `memoizedProps.children.props`) is the ONLY reliable method for extracting citation URLs from Perplexity (standard DOM queries fail)
- **Skill**: `/perplexity-extract` registered and available — depends on this MCP server's `javascript_tool` for React fiber access

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Architecture

Claude in Chrome is a Chrome extension that exposes browser automation capabilities via MCP (Model Context Protocol). It runs as an MCP server that Claude Code CLI connects to, enabling:

1. **Page Navigation**: URL navigation, history back/forward, tab management
2. **Page Reading**: Accessibility tree snapshots, natural language element search, raw text extraction
3. **Interaction**: Click, type, scroll, hover, drag, form input, keyboard actions
4. **JavaScript Execution**: Arbitrary JS in page context (key for React fiber access)
5. **Monitoring**: Console messages, network requests
6. **Recording**: Screenshot capture, GIF creation with click indicators and action labels
7. **File Operations**: Image upload to page elements or file inputs

## Known Limitations

| Limitation | Workaround |
|-----------|------------|
| JS alerts/confirms/prompts block extension | Use `console.log` + `read_console_messages` |
| React virtualization unloads offscreen DOM | Scroll slowly through all content before extraction |
| Stale tab IDs from old sessions | Always call `tabs_context_mcp` first |
| `querySelectorAll('a[href]')` fails on React apps | Use React fiber traversal |
| YouTube/GitHub citations disappear on scroll | Extract before scrolling past them |
| Perplexity "Links" tab is per-answer only | Switch between answers to get all links |

# ── References ──

## Navigation

| Resource | Location |
|----------|----------|
| Feature README | `README.md` |
| Setup docs | `.0agnostic/01_knowledge/setup/` |
| React fiber extraction | `.0agnostic/01_knowledge/perplexity_extraction/react_fiber_extraction.md` |
| Tool reference | `.0agnostic/01_knowledge/browser_automation/tool_reference.md` |
| Browser automation rules | `.0agnostic/02_rules/static/browser_automation_rules.md` |
| Content extraction protocol | `.0agnostic/03_protocols/content_extraction_workflow.md` |
| Page analysis protocol | `.0agnostic/03_protocols/page_analysis_workflow.md` |
| Interactive browsing protocol | `.0agnostic/03_protocols/interactive_browsing_workflow.md` |
| Perplexity extract skill | `.claude/skills/perplexity-extract/SKILL.md` |
| Avenue registration | `.0agnostic/06_context_avenue_web/01_file_based/05_skills/perplexity-extract.md` |
