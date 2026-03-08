---
resource_id: "904ddf77-2897-4e07-8385-0db86ef5dc47"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# Claude in Chrome MCP Server

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "7af7646b-4313-402d-ab55-01e7bba52dae" -->
## Identity

**Entity**: Claude in Chrome
**Type**: Feature (MCP Server within Claude Code CLI)
**Parent**: Claude Code CLI (sub_layer_0_10)
**Scope**: Browser automation via the Claude in Chrome Chrome extension — page navigation, content extraction, form automation, interactive browsing, GIF recording, and React fiber-based data extraction

**Specificity Chain**: OS (05) → Linux Ubuntu (05) → Environments (06) → Local (06) → Coding Apps (07) → Cursor (08) → AI Apps (09) → Claude Code CLI (10) → **Claude in Chrome (feature)**

<!-- section_id: "afd4b298-0d9b-4a48-96b3-d15449006298" -->
## Key Behaviors

- Provides browser automation capabilities to Claude Code CLI via MCP protocol
- Tools include: navigation, page reading (accessibility tree), element finding, JS execution, form input, screenshots, console/network monitoring, GIF recording
- React fiber traversal is the primary method for extracting data from React-rendered pages (Perplexity citations, SPA content)
- Tab context must be established before any browser interaction
- Session startup pattern: `tabs_context_mcp` → `tabs_create_mcp` → `navigate` → `wait`

<!-- section_id: "4b55060f-44ab-4d7f-9014-89c09d7c572f" -->
## Inputs

- Perplexity search URLs for content/citation extraction
- Target web page URLs for analysis, interaction, or automation
- Browser automation instructions from user or parent entities

<!-- section_id: "4f9832ce-cd4f-442b-bf76-abcd495a644b" -->
## Outputs

- Extracted page content (text, citations, structured data)
- Accessibility tree snapshots
- Screenshots and GIF recordings
- Console and network monitoring data
- Form submission results

<!-- section_id: "ea118ebd-7732-45f9-940b-ed9ec16070aa" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Perplexity URL provided | Use `/perplexity-extract` skill with React fiber method |
| Web page analysis needed | Follow page analysis workflow in `.0agnostic/03_protocols/` |
| Form automation requested | Follow interactive browsing workflow in `.0agnostic/03_protocols/` |
| Content extraction needed | Follow content extraction workflow in `.0agnostic/03_protocols/` |
| Setup/troubleshooting | Read `.0agnostic/01_knowledge/setup/` |
| Entering this directory | Read `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/REGISTRY.md` |

<!-- section_id: "c06d6978-a968-4207-be17-0806ea284152" -->
## Resources Available

On-demand resources in `.0agnostic/` — read as needed:

<!-- section_id: "ed7cba60-dbd6-43dc-991e-75a7be13197b" -->
### Skills
| Skill | Trigger | Definition |
|-------|---------|------------|
| `/perplexity-extract` | Perplexity URL provided | `.claude/skills/perplexity-extract/SKILL.md` |

<!-- section_id: "3211dbd4-f7ed-4267-bf45-1b8e2458e14b" -->
### Rules (`.0agnostic/02_rules/static/`)
| Rule | Importance | Description |
|------|------------|-------------|
| `browser_automation_rules.md` | I1 (High) | 10 rules: tab context first, fresh tabs, no JS dialogs, wait after nav, ref over coords, scroll before extract, etc. |

<!-- section_id: "0de67b06-c1fe-4af1-be03-32bb411cbd86" -->
### Knowledge (`.0agnostic/01_knowledge/`)
| Topic | Description |
|-------|-------------|
| `perplexity_extraction/` | React fiber method — the ONLY way to extract citation URLs from Perplexity |
| `browser_automation/` | Tool reference for all Claude in Chrome MCP tools and computer actions |
| `setup/` | MCP server setup, troubleshooting, concurrent browser config, 3 Python scripts |

<!-- section_id: "f0cddc89-91f8-400d-a299-85554d51251f" -->
### Protocols (`.0agnostic/03_protocols/`)
| Protocol | Description |
|----------|-------------|
| `content_extraction_workflow.md` | Extract content from articles, products, search results, docs |
| `page_analysis_workflow.md` | Analyze page structure, accessibility, forms, navigation |
| `interactive_browsing_workflow.md` | Form filling, multi-step nav, clicking, keyboard, GIF recording |

<!-- section_id: "015c996f-410e-441d-b3a7-b62de9106319" -->
### Context Registry
Full avenue manifest: `.0agnostic/06_context_avenue_web/00_context_avenue_web_registry/REGISTRY.md`

# ── Current Status ──

<!-- section_id: "ff124f41-7463-4a3f-9f73-c8ddfa868482" -->
## Current Status

- **State**: Migrated to .0agnostic convention (2026-02-23)
- **Scope**: 3 workflow protocols (content extraction, page analysis, interactive browsing), setup docs (README, troubleshooting, concurrent browser, MCP fix), 3 setup scripts, Perplexity React fiber extraction knowledge, 10 browser automation rules
- **Content**: Legacy `sub_layer_0_13_protocols/` and `setup/` migrated to `.0agnostic/03_protocols/` and `.0agnostic/01_knowledge/setup/` respectively. Old empty dirs (`sub_layer_0_12_universal_tools`, `sub_layer_0_14_agent_setup`) removed
- **Key Discovery**: React fiber traversal (`__reactFiber$*` → `memoizedProps.children.props`) is the ONLY reliable method for extracting citation URLs from Perplexity (standard DOM queries fail)
- **Skill**: `/perplexity-extract` registered and available — depends on this MCP server's `javascript_tool` for React fiber access

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "412787c3-bb7a-4375-a408-9d8374d7dfde" -->
## Architecture

Claude in Chrome is a Chrome extension that exposes browser automation capabilities via MCP (Model Context Protocol). It runs as an MCP server that Claude Code CLI connects to, enabling:

1. **Page Navigation**: URL navigation, history back/forward, tab management
2. **Page Reading**: Accessibility tree snapshots, natural language element search, raw text extraction
3. **Interaction**: Click, type, scroll, hover, drag, form input, keyboard actions
4. **JavaScript Execution**: Arbitrary JS in page context (key for React fiber access)
5. **Monitoring**: Console messages, network requests
6. **Recording**: Screenshot capture, GIF creation with click indicators and action labels
7. **File Operations**: Image upload to page elements or file inputs

<!-- section_id: "d309a6fc-e8c5-4908-a24f-6839c4160718" -->
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

<!-- section_id: "a5762979-c4b5-49c3-a123-8dee6642b666" -->
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
