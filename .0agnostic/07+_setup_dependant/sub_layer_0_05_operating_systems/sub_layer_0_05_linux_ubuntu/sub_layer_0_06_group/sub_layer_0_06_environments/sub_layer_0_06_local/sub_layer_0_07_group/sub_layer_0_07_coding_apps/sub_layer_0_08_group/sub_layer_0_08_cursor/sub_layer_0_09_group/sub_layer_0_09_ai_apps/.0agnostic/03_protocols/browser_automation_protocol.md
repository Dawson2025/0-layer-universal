---
resource_id: "1a83fe82-1732-49a6-88cd-2bfb6d15352d"
resource_type: "protocol"
resource_name: "browser_automation_protocol"
---
# Browser Automation Protocol (Shared - All AI Apps)

<!-- section_id: "44ea0d9c-7056-4106-b825-8afe0aac49e1" -->
## Overview

This protocol defines standard procedures for browser automation across all AI applications (Claude Code CLI, Cursor AI, etc.) using available MCP servers (Playwright, Claude-in-Chrome, etc.).

<!-- section_id: "dc81aa8f-3526-4d39-97df-f6b4c5152518" -->
## Available Browser Automation Tools

<!-- section_id: "0db0d9dd-f1d0-4d32-a1c4-7f8e669178c7" -->
### 1. Playwright MCP
- **Best for**: Headless automation, scripted workflows, CI/CD
- **Tools prefix**: `mcp__playwright__*`
- **Key tools**: `browser_navigate`, `browser_click`, `browser_type`, `browser_snapshot`

<!-- section_id: "387de3b7-cdf2-439a-ac10-5bf7cc82fe6a" -->
### 2. Claude-in-Chrome MCP
- **Best for**: Interactive browsing, real user sessions, complex web apps
- **Tools prefix**: `mcp__claude-in-chrome__*`
- **Key tools**: `navigate`, `computer`, `read_page`, `find`

<!-- section_id: "7d17a6aa-8862-4eee-aa64-306eecaea1fd" -->
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

<!-- section_id: "c5cd4671-abcb-419f-8014-bb75dbd1bf19" -->
## Common Browser Operations

<!-- section_id: "f3b52169-1821-498d-badc-2475fa75bccb" -->
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

<!-- section_id: "1c2ed5ea-c318-42ba-a502-b3410f42a42d" -->
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

<!-- section_id: "ddadc1a8-db6d-426d-aeaa-a5538ac9ef72" -->
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

<!-- section_id: "896eb7ec-98d5-4367-ab5c-2ba3b237e8ec" -->
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

<!-- section_id: "21f02bc4-5866-46d7-a54d-fbc3397a0da5" -->
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

<!-- section_id: "8ceac8be-ca6e-4259-99f9-5d37c7600acc" -->
## Session Management

<!-- section_id: "0976ed8c-c741-4732-8f7d-fa0500863385" -->
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

<!-- section_id: "ed1f36c1-e7b5-4401-b89e-4ff4c7afce74" -->
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

<!-- section_id: "727bd734-fc3e-4947-82ea-5c803c1affcc" -->
## GitHub-Specific Operations

<!-- section_id: "eeaea59d-4074-4ad9-8b5c-37fe95f0fd2a" -->
### Creating a Repository (Private by Default)

1. Navigate to `https://github.com/new`
2. Select owner from dropdown
3. Enter repository name
4. **CRITICAL: Set visibility to PRIVATE**
5. Click "Create repository"
6. Verify "Private" badge appears

<!-- section_id: "32a06d7d-def8-4df5-8b2a-c20ce168fabe" -->
### Changing Repository Visibility

1. Navigate to `https://github.com/{owner}/{repo}/settings`
2. Scroll to "Danger Zone"
3. Click "Change visibility"
4. Select "Change to private" (or public if explicitly requested)
5. Confirm through multi-step modal
6. Verify lock icon appears

<!-- section_id: "801f1fbb-16d9-4ef5-9c16-f282bc78f351" -->
### Renaming a Repository

1. Navigate to `https://github.com/{owner}/{repo}/settings`
2. Find "Repository name" field
3. Clear and enter new name
4. Click "Rename"
5. Update local git remote URL

---

<!-- section_id: "a786d29c-ce23-4d70-a9f8-e829bb6770f2" -->
## Error Handling

<!-- section_id: "b27b9936-8a15-4e2f-8981-715602cec337" -->
### Browser Not Responding

**Playwright:**
```bash
pkill -f "chrome.*mcp"
# Then retry
```

**Claude-in-Chrome:**
- Check if tab still exists with `tabs_context_mcp`
- Create new tab if needed

<!-- section_id: "1331c42d-3ff5-438e-8de4-41c1834b0e5a" -->
### Element Not Found

1. Take a snapshot to see current page state
2. Scroll if element might be off-screen
3. Wait for dynamic content to load
4. Use alternative selector/reference

<!-- section_id: "dbb71108-b2a7-4057-9b22-bce0f5469794" -->
### Authentication Required

1. Inform user that authentication is needed
2. Wait for user to complete login/2FA
3. Resume operation after confirmation

<!-- section_id: "3c5caac0-fb73-423c-ad61-9d23fc3879fb" -->
### Rate Limiting

1. Wait 60 seconds
2. Retry operation
3. If persistent, inform user and suggest waiting longer

---

<!-- section_id: "785c3e41-4655-4414-b4fe-b5285d551868" -->
## Best Practices

<!-- section_id: "f27e9b55-79d2-42da-8166-6f33e6168867" -->
### Before Operations
- [ ] Get tab context (Chrome) or verify browser available (Playwright)
- [ ] Check current URL matches expected starting point
- [ ] Take snapshot to understand page state

<!-- section_id: "c22a8ccc-db71-4b91-a141-b7e7fa8b446b" -->
### During Operations
- [ ] Use element references from snapshots, not hardcoded selectors
- [ ] Wait for page loads between navigation
- [ ] Verify each step before proceeding

<!-- section_id: "ddad70e5-80b5-417e-848f-bb0e6e270577" -->
### After Operations
- [ ] Verify expected outcome (check for success indicators)
- [ ] Take final snapshot/screenshot if needed
- [ ] Clean up (close tabs/browser if done)

<!-- section_id: "8d906b4b-a31a-4e22-8b6f-85f7f8ecee7b" -->
### Security
- [ ] Never enter passwords or sensitive credentials
- [ ] Don't submit financial information
- [ ] Verify URLs before entering data
- [ ] Respect user privacy settings

---

<!-- section_id: "1c036e79-d9ee-40c4-9a70-0c198960b685" -->
## Parallel Automation

When running multiple browser automations:

1. **Same tool**: Use isolated instances (Playwright supports `--isolated`)
2. **Different tools**: Can run Playwright and Claude-in-Chrome simultaneously
3. **Avoid race conditions**: Don't target same page/elements from multiple agents

---

<!-- section_id: "f101b03f-979a-4b2a-bb54-b69cfc812b5e" -->
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
