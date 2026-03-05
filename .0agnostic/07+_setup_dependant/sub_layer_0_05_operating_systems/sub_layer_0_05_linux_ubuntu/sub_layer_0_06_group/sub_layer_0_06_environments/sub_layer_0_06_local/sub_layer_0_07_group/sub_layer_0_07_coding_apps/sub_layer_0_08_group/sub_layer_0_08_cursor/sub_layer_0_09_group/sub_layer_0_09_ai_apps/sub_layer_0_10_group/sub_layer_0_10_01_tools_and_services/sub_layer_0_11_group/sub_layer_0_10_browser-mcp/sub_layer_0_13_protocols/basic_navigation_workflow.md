---
resource_id: "2808fa82-75db-4723-839c-335b2d0b186a"
resource_type: "document"
resource_name: "basic_navigation_workflow"
---
# Basic Navigation Workflow (Browser MCP)

<!-- section_id: "3416de4a-44d0-415f-bd30-e6ab2d86cc06" -->
## Overview

This protocol defines standard procedures for basic web navigation using Browser MCP tools. These operations form the foundation for more complex browser automation workflows.

<!-- section_id: "7d4e7e5a-e646-4003-be4e-f845b4232cda" -->
## Prerequisites

1. Browser MCP server must be running and accessible
2. Playwright browsers installed (`~/.cache/ms-playwright/`)
3. For headed mode: working display (DISPLAY variable set)
4. Environment variables configured in MCP config

<!-- section_id: "a4408637-aa4c-498f-9a2b-2f4dd84b0854" -->
## Pre-Flight Check

Before starting navigation, verify the browser is ready:

```
1. Use browser_snapshot to check current page state
2. If no page is loaded, navigate to initial URL
3. Confirm browser response with status check
```

---

<!-- section_id: "0709322d-83c6-4031-9d7c-e240921cdada" -->
## Protocol 1: Simple Page Navigation

<!-- section_id: "3a070106-bb35-43c1-9a5d-def375cdb1f3" -->
### Purpose
Navigate to a single URL and verify the page loaded successfully.

<!-- section_id: "376933e3-7687-4640-a948-4c5ae02cad16" -->
### Steps

1. **Navigate to URL**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com"
   ```

2. **Wait for page load**
   ```
   Tool: browser_wait_for
   Parameters:
     text: "Expected content"  # OR
     time: 3                   # Wait 3 seconds
   ```

3. **Verify page state**
   ```
   Tool: browser_snapshot
   Parameters: (none - captures current page)
   ```

<!-- section_id: "9a92bd99-9094-406e-b982-8e59e65fa1c3" -->
### Success Criteria
- Page URL matches expected destination
- Expected content visible in snapshot
- No error messages or failed resource loads

<!-- section_id: "bc5b6c32-5f64-4549-ac71-c2e6489b2db4" -->
### Error Handling
- **Timeout**: Increase wait time or check network connectivity
- **404/Error page**: Verify URL is correct
- **Redirect**: Check final URL in snapshot

---

<!-- section_id: "d85c5be3-15fc-42bc-93f0-a41bb983e83a" -->
## Protocol 2: Navigate with Element Verification

<!-- section_id: "15658aeb-7ac2-4c4e-9d2a-258464f211b2" -->
### Purpose
Navigate to a page and confirm specific elements are present before proceeding.

<!-- section_id: "34bf731a-6b79-4932-9380-172e0799f294" -->
### Steps

1. **Navigate**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/login"
   ```

2. **Wait for specific element**
   ```
   Tool: browser_wait_for
   Parameters:
     text: "Sign In"  # Button or heading text
   ```

3. **Take snapshot for verification**
   ```
   Tool: browser_snapshot
   ```

4. **Verify element presence**
   - Check snapshot output for expected elements
   - Look for ref IDs that can be used for interaction

<!-- section_id: "98efb748-2b8b-4130-b55c-6c749fadad1e" -->
### Element Verification Checklist
- [ ] Target element appears in snapshot
- [ ] Element has valid ref ID for interaction
- [ ] No overlapping elements blocking interaction
- [ ] Page is fully loaded (no loading indicators)

---

<!-- section_id: "f036ecbe-7844-48bd-82f9-0509d21a36b5" -->
## Protocol 3: Sequential Page Navigation

<!-- section_id: "7ee312c2-98e5-4ea2-b368-47cae437515c" -->
### Purpose
Navigate through multiple pages in sequence (e.g., multi-step form, wizard).

<!-- section_id: "1f6fab9d-7843-43dc-85fc-33f44bfc8670" -->
### Steps

1. **Navigate to starting page**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/step1"
   ```

2. **Complete page 1 actions** (clicking, form filling)

3. **Navigate to next page via link/button**
   ```
   Tool: browser_click
   Parameters:
     ref: "ref_XX"        # Next button reference
     element: "Next Step" # Human-readable description
   ```

4. **Wait for page transition**
   ```
   Tool: browser_wait_for
   Parameters:
     text: "Step 2"
   ```

5. **Verify new page loaded**
   ```
   Tool: browser_snapshot
   ```

6. **Repeat for subsequent pages**

<!-- section_id: "a967952d-69ff-4291-bed2-560a8453f738" -->
### Navigation State Tracking
Track progress through multi-page flows:
- Current page/step number
- Completed actions on each page
- Data entered (if applicable)
- Expected final destination

---

<!-- section_id: "f054b41c-fa8e-43ea-99c9-02d35517b8d8" -->
## Protocol 4: Navigation with History

<!-- section_id: "1c3fc86e-1302-49f8-bbed-4510d4db5845" -->
### Purpose
Navigate forward and backward through browser history.

<!-- section_id: "3f133eeb-086a-4c54-ae77-e0b1123273b3" -->
### Steps

1. **Navigate to page A**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/page-a"
   ```

2. **Navigate to page B**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/page-b"
   ```

3. **Go back to page A**
   ```
   Tool: browser_navigate
   Parameters:
     url: "back"
   ```

4. **Verify returned to page A**
   ```
   Tool: browser_snapshot
   ```

5. **Go forward to page B**
   ```
   Tool: browser_navigate
   Parameters:
     url: "forward"
   ```

<!-- section_id: "270eb7ef-6f61-4f1f-862b-be11e394df39" -->
### History Navigation Notes
- "back" and "forward" are special URL values
- Browser must have history to navigate
- Some sites may not work with history navigation (SPAs with client-side routing)

---

<!-- section_id: "60ab4719-d62e-406b-8b24-ac7652359e66" -->
## Protocol 5: Handle Page Redirects

<!-- section_id: "03362358-d321-47c2-8f6e-84aa75b8c877" -->
### Purpose
Navigate to a URL that may redirect and verify final destination.

<!-- section_id: "4275d848-2a31-48a0-99c5-aadf1b040e57" -->
### Steps

1. **Navigate to potentially redirecting URL**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/redirect-me"
   ```

2. **Wait for redirect to complete**
   ```
   Tool: browser_wait_for
   Parameters:
     time: 5  # Give redirects time to complete
   ```

3. **Capture final page state**
   ```
   Tool: browser_snapshot
   ```

4. **Verify final destination**
   - Check URL in snapshot output
   - Confirm expected content is present
   - Handle unexpected redirects appropriately

<!-- section_id: "28d63f7d-58e2-4711-8f4a-5030da6804db" -->
### Redirect Handling
- Allow sufficient wait time for multi-hop redirects
- Check for authentication redirects (login pages)
- Handle cookie consent redirects
- Verify HTTPS redirect completion

---

<!-- section_id: "36ad91dd-1d7c-43dd-9aa6-5b5d372fde2c" -->
## Common Navigation Patterns

<!-- section_id: "0781312a-eb0d-40f5-b608-abf6c79cd84a" -->
### Pattern: Authenticated Navigation

```
1. Navigate to login page
2. Enter credentials (separate form workflow)
3. Submit login
4. Wait for redirect to dashboard/home
5. Verify authentication succeeded
6. Continue with authenticated navigation
```

<!-- section_id: "8bafbaea-be0a-4580-9090-3ef0ec380e9d" -->
### Pattern: Error Recovery Navigation

```
1. Navigate to target URL
2. If error page detected:
   a. Wait 2-3 seconds
   b. Refresh page (navigate to same URL)
   c. If still error, report failure
3. If timeout:
   a. Check network status
   b. Try navigation again
   c. Consider headless vs headed mode
```

<!-- section_id: "57ccb3c6-0165-4fad-8ec5-25a900e30224" -->
### Pattern: SPA (Single Page Application) Navigation

```
1. Navigate to SPA root
2. Wait for initial load (longer than static sites)
3. Use click navigation instead of URL navigation
4. Wait for route change indicators
5. Verify new content loaded (not just URL change)
```

---

<!-- section_id: "0c799d0e-db16-4a5a-a84b-0d0ca984dfbc" -->
## Best Practices

1. **Always wait after navigation**
   - Pages need time to load and render
   - Use `browser_wait_for` with expected content

2. **Verify before interacting**
   - Take snapshot before clicking
   - Confirm element is visible and not obscured

3. **Handle popups proactively**
   - Cookie consent banners
   - Newsletter modals
   - Chat widgets
   - Dismiss or close before main navigation

4. **Track navigation state**
   - Note current URL
   - Record navigation history for debugging
   - Keep track of authentication state

5. **Use appropriate waits**
   - Text-based waits for specific content
   - Time-based waits for unknown content
   - Avoid fixed waits when possible (slower)

---

<!-- section_id: "44dcdcea-a523-4719-aa2e-16a319071b4a" -->
## Error Reference

| Error | Likely Cause | Solution |
|-------|--------------|----------|
| Navigation timeout | Slow network/page | Increase timeout or check connectivity |
| Page not found (404) | Invalid URL | Verify URL spelling and structure |
| SSL/Certificate error | Invalid cert | Check site certificate or use --ignore-certificate-errors |
| Connection refused | Site down | Verify site is accessible manually |
| Too many redirects | Redirect loop | Check URL for issues, may need manual intervention |

---

**Last Updated**: 2026-01-13
**Applies To**: Browser MCP for Claude Code CLI on Linux/Ubuntu
