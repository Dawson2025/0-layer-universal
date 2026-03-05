---
resource_id: "0bc20995-449f-4b82-a2bd-f0ebf0769396"
resource_type: "rule"
resource_name: "browser_opening_rule"
---
# Browser Opening Rule

<!-- section_id: "35327d68-9b55-43c6-8bae-ad299978e959" -->
## Rule: Always Use MCP Browser Servers for Browser Automation

Whenever opening a browser instance for automation or interaction, it MUST be done through MCP browser servers, NOT by launching standalone chromium processes via the terminal.

<!-- section_id: "bb0cc42d-a995-4678-ba7d-2195f9aa0ca2" -->
### Preferred Browser MCP Servers

1. **cursor-browser-extension** (Primary) - Full-featured browser automation with persistent sessions
2. **mcp_browser** (Alternative) - Comprehensive browser automation with Playwright
3. **mcp_playwright** (Legacy) - Original Playwright integration

<!-- section_id: "a9df1d06-b979-4b85-aeef-39c4148960f2" -->
### Rationale

- **Interactability**: MCP-controlled browsers allow full programmatic control (clicking, filling forms, navigating, taking screenshots, etc.)
- **Tab Management**: Can open and manage multiple tabs within a single browser instance
- **Persistent Access**: Browser instances remain accessible and interactable across chat sessions
- **Session Persistence**: Browser state persists across AI chat sessions (authentication, cookies, etc.)
- **Integration**: Seamlessly integrates with other MCP tools and automation workflows
- **Cross-Session Continuity**: Same browser instance can be reused in future conversations

<!-- section_id: "8602b845-a3a1-438f-8ed9-04d258f09363" -->
### Implementation

Instead of:
```bash
chromium --user-data-dir="/tmp/chromium-instance1" file.html &
```

Use MCP Browser Tools:

#### cursor-browser-extension (Recommended)
- `mcp_cursor-browser-extension_browser_navigate` - Navigate to URLs
- `mcp_cursor-browser-extension_browser_snapshot` - Capture page state for interaction
- `mcp_cursor-browser-extension_browser_click` - Click elements on page
- `mcp_cursor-browser-extension_browser_type` - Type text into fields
- `mcp_cursor-browser-extension_browser_tabs` - Manage multiple tabs
- `mcp_cursor-browser-extension_browser_take_screenshot` - Capture screenshots
- And other cursor-browser-extension tools for full browser control

#### mcp_browser (Alternative)
- `mcp_browser_browser_navigate` - Navigate to URLs
- `mcp_browser_browser_get_clickable_elements` - Get interactive elements
- `mcp_browser_browser_click` - Click elements
- `mcp_browser_browser_form_input_fill` - Fill forms
- And other mcp_browser interaction tools

#### Key Benefits of MCP Browser Servers
- **Persistent Sessions**: Browser stays open across multiple AI chat sessions
- **Authenticated Sessions**: Login once, use across many conversations
- **State Preservation**: Cookies, local storage, and session data persist
- **No Re-authentication**: Resume where you left off in the next session

<!-- section_id: "a8bb9cc9-3567-4b0c-9e33-172cab7dd102" -->
### Exception

The ONLY time to use standalone chromium processes is when you need a temporary browser window that the user will manually interact with directly (e.g., for them to authenticate or manually browse), and even then, MCP browser servers should be preferred if programmatic interaction will be needed afterward.

<!-- section_id: "9e8e6b7f-ca49-43be-83de-483050351bef" -->
## Best Practices

1. **Start of Session**: Use MCP browser tools to navigate to required URLs
2. **During Session**: Interact with the browser using MCP tools (snapshot, click, type, etc.)
3. **End of Session**: Leave browser open - DO NOT close it
4. **Next Session**: Browser is still running and authenticated, ready to continue
5. **User Request**: Only close browser if explicitly requested by user

<!-- section_id: "6a73f5a8-8a4e-4a15-ab21-3377e481a422" -->
## Example Use Cases

<!-- section_id: "cb05697b-5302-4ba6-904f-2e568df8cdd5" -->
### GitHub Authentication (Today's Example)
1. Navigate to GitHub SSO authorization page
2. User completes Duo authentication on their phone
3. Browser redirects to success page
4. Git operations now work with the authorized token
5. Browser remains open for future GitHub interactions

<!-- section_id: "de3320b0-e274-44d7-bf89-d042abb395ce" -->
### Multi-Session Workflows
1. **Session 1**: Login to application, navigate to dashboard
2. **Session 2**: Continue from dashboard, browser still authenticated
3. **Session 3**: Access protected resources without re-authentication
4. **Session N**: Browser persists indefinitely until explicitly closed

