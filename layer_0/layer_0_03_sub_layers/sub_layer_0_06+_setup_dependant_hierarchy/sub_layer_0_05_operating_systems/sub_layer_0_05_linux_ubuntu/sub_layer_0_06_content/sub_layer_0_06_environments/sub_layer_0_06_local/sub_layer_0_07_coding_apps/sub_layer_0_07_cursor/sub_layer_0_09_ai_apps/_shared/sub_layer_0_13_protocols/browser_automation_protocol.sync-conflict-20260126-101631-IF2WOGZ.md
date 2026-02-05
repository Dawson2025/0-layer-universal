# Browser Automation Protocol (Shared - All AI Apps)

## Overview

This protocol defines standard procedures for browser automation across all AI applications (Claude Code CLI, Cursor AI, etc.) using available MCP servers (Playwright, Claude-in-Chrome, etc.).

## Available Browser Automation Tools

### 1. Playwright MCP
- **Best for**: Headless automation, scripted workflows, CI/CD
- **Tools prefix**: `mcp__playwright__*`
- **Key tools**: `browser_navigate`, `browser_click`, `browser_type`, `browser_snapshot`

### 2. Claude-in-Chrome MCP
- **Best for**: Interactive browsing, real user sessions, complex web apps
- **Tools prefix**: `mcp__claude-in-chrome__*`
- **Key tools**: `navigate`, `computer`, `read_page`, `find`

## Tool Selection Guidelines

| Scenario | Recommended Tool |
|----------|------------------|
| Creating GitHub repos | Playwright (scripted) |
| Form filling | Either (Playwright for simple, Chrome for complex) |
| Reading dynamic content | Claude-in-Chrome |
| Screenshots for user | Either |
| Long-running sessions | Claude-in-Chrome |
| Parallel automation | Playwright (supports isolation) |

---

## Common Browser Operations

### Navigation

**Playwright:**
```
mcp__playwright__browser_navigate
  url: "https://example.com"
```

**Claude-in-Chrome:**
```
mcp__claude-in-chrome__navigate
  url: "https://example.com"
  tabId: {tab_id}
```

### Clicking Elements

**Playwright:**
```
mcp__playwright__browser_click
  element: "Submit button"
  ref: "e123"
```

**Claude-in-Chrome:**
```
mcp__claude-in-chrome__computer
  action: "left_click"
  coordinate: [x, y]
  tabId: {tab_id}
```

### Typing Text

**Playwright:**
```
mcp__playwright__browser_type
  element: "Search input"
  ref: "e456"
  text: "search query"
```

**Claude-in-Chrome:**
```
mcp__claude-in-chrome__form_input
  ref: "ref_123"
  value: "input value"
  tabId: {tab_id}
```

### Taking Screenshots

**Playwright:**
```
mcp__playwright__browser_take_screenshot
  filename: "screenshot.png"
```

**Claude-in-Chrome:**
```
mcp__claude-in-chrome__computer
  action: "screenshot"
  tabId: {tab_id}
```

### Reading Page Content

**Playwright:**
```
mcp__playwright__browser_snapshot
```

**Claude-in-Chrome:**
```
mcp__claude-in-chrome__read_page
  tabId: {tab_id}
  filter: "interactive"  # or "all"
```

---

## Session Management

### Playwright

**Starting a session:**
- Sessions start automatically on first navigation
- Use `browser_install` if browser not installed

**Ending a session:**
```
mcp__playwright__browser_close
```

**Handling conflicts:**
```bash
# Kill stuck browser processes
pkill -f "chrome.*mcp-chrome" || pkill -f "chromium.*mcp"
```

### Claude-in-Chrome

**Getting tab context (REQUIRED first):**
```
mcp__claude-in-chrome__tabs_context_mcp
  createIfEmpty: true
```

**Creating new tabs:**
```
mcp__claude-in-chrome__tabs_create_mcp
```

**Closing tabs:**
```
mcp__claude-in-chrome__browser_tabs
  action: "close"
  index: {tab_index}
```

---

## GitHub-Specific Operations

### Creating a Repository (Private by Default)

1. Navigate to `https://github.com/new`
2. Select owner from dropdown
3. Enter repository name
4. **CRITICAL: Set visibility to PRIVATE**
5. Click "Create repository"
6. Verify "Private" badge appears

### Changing Repository Visibility

1. Navigate to `https://github.com/{owner}/{repo}/settings`
2. Scroll to "Danger Zone"
3. Click "Change visibility"
4. Select "Change to private" (or public if explicitly requested)
5. Confirm through multi-step modal
6. Verify lock icon appears

### Renaming a Repository

1. Navigate to `https://github.com/{owner}/{repo}/settings`
2. Find "Repository name" field
3. Clear and enter new name
4. Click "Rename"
5. Update local git remote URL

---

## Error Handling

### Browser Not Responding

**Playwright:**
```bash
pkill -f "chrome.*mcp"
# Then retry
```

**Claude-in-Chrome:**
- Check if tab still exists with `tabs_context_mcp`
- Create new tab if needed

### Element Not Found

1. Take a snapshot to see current page state
2. Scroll if element might be off-screen
3. Wait for dynamic content to load
4. Use alternative selector/reference

### Authentication Required

1. Inform user that authentication is needed
2. Wait for user to complete login/2FA
3. Resume operation after confirmation

### Rate Limiting

1. Wait 60 seconds
2. Retry operation
3. If persistent, inform user and suggest waiting longer

---

## Best Practices

### Before Operations
- [ ] Get tab context (Chrome) or verify browser available (Playwright)
- [ ] Check current URL matches expected starting point
- [ ] Take snapshot to understand page state

### During Operations
- [ ] Use element references from snapshots, not hardcoded selectors
- [ ] Wait for page loads between navigation
- [ ] Verify each step before proceeding

### After Operations
- [ ] Verify expected outcome (check for success indicators)
- [ ] Take final snapshot/screenshot if needed
- [ ] Clean up (close tabs/browser if done)

### Security
- [ ] Never enter passwords or sensitive credentials
- [ ] Don't submit financial information
- [ ] Verify URLs before entering data
- [ ] Respect user privacy settings

---

## Parallel Automation

When running multiple browser automations:

1. **Same tool**: Use isolated instances (Playwright supports `--isolated`)
2. **Different tools**: Can run Playwright and Claude-in-Chrome simultaneously
3. **Avoid race conditions**: Don't target same page/elements from multiple agents

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Browser already in use" | Kill process with pkill, then retry |
| "Tab not found" | Call `tabs_context_mcp` to refresh tab list |
| "Element reference invalid" | Take new snapshot, use updated refs |
| "Navigation timeout" | Check network, retry with longer timeout |
| "Permission denied" | Check if action requires user confirmation |

---

**Last Updated**: 2026-01-12
**Applies To**: All AI apps using browser automation on Linux/Ubuntu
