---
resource_id: "e2c4e271-60d1-4767-8df1-612ee0d59016"
resource_type: "rule"
resource_name: "browser_automation_rules"
---
# Browser Automation Rules — Claude in Chrome

**Importance**: I1 (High)
**Scope**: All browser automation via Claude in Chrome MCP server

## R1: Tab Context First

MUST call `tabs_context_mcp` before any other Claude in Chrome tool in a session. Stale tab IDs cause silent failures.

## R2: Fresh Tabs Per Session

MUST create a new tab with `tabs_create_mcp()` for each new task. Never reuse tab IDs from prior sessions or conversations.

## R3: No JavaScript Dialogs

MUST NOT trigger `alert()`, `confirm()`, or `prompt()` — these block all extension communication. Use `console.log()` + `read_console_messages` for debugging.

## R4: Wait After Navigation

MUST wait 2-3 seconds after `navigate()` before reading page content. Dynamic pages (React, SPA) need time to render.

## R5: Element References Over Coordinates

SHOULD use `ref` parameter (from `read_page` or `find`) instead of pixel coordinates for clicks. References are viewport-independent.

## R6: Scroll Before Extraction

MUST scroll through all content before extracting from pages with React virtualization (Perplexity, infinite scroll, lazy-loaded content). Unrendered DOM = missing data.

## R7: Screenshot-Action-Screenshot Pattern

SHOULD take screenshots before and after complex interactions for verification and debugging. Use GIF recording for multi-step workflows.

## R8: Depth Limits on Complex Pages

SHOULD use `depth` parameter on `read_page` for complex pages to avoid output overflow. Start with `depth=5`, increase if needed.

## R9: Console Pattern Filtering

MUST use `pattern` parameter with `read_console_messages` to filter results. Unfiltered console output is often overwhelming and irrelevant.

## R10: React Fiber for Citation Extraction

When extracting citation URLs from React-rendered pages (Perplexity, etc.), MUST use React fiber traversal (`__reactFiber$*` → `memoizedProps`). Standard `querySelectorAll('a[href]')` returns incomplete results on React apps.
