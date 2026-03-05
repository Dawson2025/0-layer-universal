---
resource_id: "e2c4e271-60d1-4767-8df1-612ee0d59016"
resource_type: "rule"
resource_name: "browser_automation_rules"
---
# Browser Automation Rules — Claude in Chrome

**Importance**: I1 (High)
**Scope**: All browser automation via Claude in Chrome MCP server

<!-- section_id: "589418c6-e32a-4e31-8390-02a533b37775" -->
## R1: Tab Context First

MUST call `tabs_context_mcp` before any other Claude in Chrome tool in a session. Stale tab IDs cause silent failures.

<!-- section_id: "7b8d9838-57bd-4421-b564-b301cf30ca90" -->
## R2: Fresh Tabs Per Session

MUST create a new tab with `tabs_create_mcp()` for each new task. Never reuse tab IDs from prior sessions or conversations.

<!-- section_id: "25f19ccd-d2c4-4706-90d0-f3049a812fb4" -->
## R3: No JavaScript Dialogs

MUST NOT trigger `alert()`, `confirm()`, or `prompt()` — these block all extension communication. Use `console.log()` + `read_console_messages` for debugging.

<!-- section_id: "635f67be-42e3-4ede-9643-b605b61b268d" -->
## R4: Wait After Navigation

MUST wait 2-3 seconds after `navigate()` before reading page content. Dynamic pages (React, SPA) need time to render.

<!-- section_id: "d33751d1-5aaa-4cd7-a7f1-2ba0b54a3503" -->
## R5: Element References Over Coordinates

SHOULD use `ref` parameter (from `read_page` or `find`) instead of pixel coordinates for clicks. References are viewport-independent.

<!-- section_id: "613d18c4-d906-474c-8fbe-c98117ba9483" -->
## R6: Scroll Before Extraction

MUST scroll through all content before extracting from pages with React virtualization (Perplexity, infinite scroll, lazy-loaded content). Unrendered DOM = missing data.

<!-- section_id: "56101d87-cc34-4215-a171-f3ee41846f8b" -->
## R7: Screenshot-Action-Screenshot Pattern

SHOULD take screenshots before and after complex interactions for verification and debugging. Use GIF recording for multi-step workflows.

<!-- section_id: "3b964dd9-b7ee-404d-9715-35eb3873fbde" -->
## R8: Depth Limits on Complex Pages

SHOULD use `depth` parameter on `read_page` for complex pages to avoid output overflow. Start with `depth=5`, increase if needed.

<!-- section_id: "7abc58ae-22b6-4e75-937d-caaea0c33fa0" -->
## R9: Console Pattern Filtering

MUST use `pattern` parameter with `read_console_messages` to filter results. Unfiltered console output is often overwhelming and irrelevant.

<!-- section_id: "c407dcec-21f4-44ef-ab9f-768de8a398de" -->
## R10: React Fiber for Citation Extraction

When extracting citation URLs from React-rendered pages (Perplexity, etc.), MUST use React fiber traversal (`__reactFiber$*` → `memoizedProps`). Standard `querySelectorAll('a[href]')` returns incomplete results on React apps.
