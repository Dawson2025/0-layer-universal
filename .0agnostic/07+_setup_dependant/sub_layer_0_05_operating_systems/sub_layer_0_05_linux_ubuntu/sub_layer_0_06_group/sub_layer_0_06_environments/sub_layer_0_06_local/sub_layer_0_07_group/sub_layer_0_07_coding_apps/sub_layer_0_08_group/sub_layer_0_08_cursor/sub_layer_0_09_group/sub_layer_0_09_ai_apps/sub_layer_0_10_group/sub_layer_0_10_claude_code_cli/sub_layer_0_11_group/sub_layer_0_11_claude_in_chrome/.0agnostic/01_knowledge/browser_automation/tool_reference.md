---
resource_id: "c5bc0746-9b9b-429f-9fa4-3a3f8ef03339"
resource_type: "knowledge"
resource_name: "tool_reference"
---
# Claude in Chrome — Tool Reference

## Core Tools

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| `tabs_context_mcp` | Get/create tab context | `createIfEmpty` |
| `tabs_create_mcp` | Create new tab in MCP group | — |
| `navigate` | Go to URL or back/forward | `url`, `tabId` |
| `computer` | Mouse/keyboard/screenshot | `action`, `tabId`, `coordinate`/`ref` |
| `read_page` | Accessibility tree snapshot | `tabId`, `filter`, `depth`, `ref_id` |
| `find` | Natural language element search | `query`, `tabId` |
| `get_page_text` | Extract raw page text | `tabId` |
| `javascript_tool` | Execute JS in page context | `text`, `tabId` |
| `form_input` | Set form field values | `ref`, `value`, `tabId` |
| `read_console_messages` | Read browser console | `tabId`, `pattern` |
| `read_network_requests` | Read HTTP requests | `tabId`, `urlPattern` |
| `gif_creator` | Record/export GIF | `action`, `tabId` |
| `resize_window` | Set browser dimensions | `width`, `height`, `tabId` |
| `upload_image` | Upload screenshot/image | `imageId`, `tabId` |
| `shortcuts_list` | List available shortcuts | `tabId` |
| `shortcuts_execute` | Run a shortcut | `command`, `tabId` |

## Computer Action Types

| Action | Description | Required Params |
|--------|-------------|-----------------|
| `left_click` | Left mouse click | `coordinate` or `ref` |
| `right_click` | Right click (context menu) | `coordinate` or `ref` |
| `double_click` | Double left click | `coordinate` or `ref` |
| `triple_click` | Triple left click | `coordinate` or `ref` |
| `type` | Type text string | `text` |
| `key` | Press keyboard key(s) | `text` (space-separated keys) |
| `screenshot` | Capture viewport | — |
| `zoom` | Zoom into region | `region` [x0,y0,x1,y1] |
| `scroll` | Scroll page | `scroll_direction`, `coordinate` |
| `scroll_to` | Scroll element into view | `ref` |
| `hover` | Move mouse without clicking | `coordinate` or `ref` |
| `wait` | Wait N seconds | `duration` |
| `left_click_drag` | Drag from A to B | `start_coordinate`, `coordinate` |

## Session Startup Pattern

Every browser session MUST start with:
```
1. tabs_context_mcp(createIfEmpty=True)  → get valid tab IDs
2. tabs_create_mcp()                      → create fresh tab (don't reuse old)
3. navigate(url=..., tabId=NEW_TAB)       → go to target
4. computer(action="wait", duration=2)    → wait for load
```

## Critical Rules

1. **Never reuse tab IDs** from previous sessions
2. **Always call `tabs_context_mcp` first** before any other tool
3. **Avoid triggering JS alerts/confirms/prompts** — they block the extension
4. **Use `read_page` over screenshots** for structured analysis
5. **Use `ref` over coordinates** for clicks — more reliable across viewport sizes
6. **Console debugging**: use `console.log()` + `read_console_messages` (not `alert()`)
