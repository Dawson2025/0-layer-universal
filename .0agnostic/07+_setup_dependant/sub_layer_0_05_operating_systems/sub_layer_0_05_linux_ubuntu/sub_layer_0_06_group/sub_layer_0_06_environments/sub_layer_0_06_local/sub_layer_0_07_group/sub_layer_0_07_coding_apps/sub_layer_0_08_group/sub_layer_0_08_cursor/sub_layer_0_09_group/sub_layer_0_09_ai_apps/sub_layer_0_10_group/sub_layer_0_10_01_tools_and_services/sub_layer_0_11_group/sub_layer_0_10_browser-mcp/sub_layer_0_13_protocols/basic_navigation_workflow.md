---
resource_id: "2808fa82-75db-4723-839c-335b2d0b186a"
resource_type: "document"
resource_name: "basic_navigation_workflow"
---
# Basic Navigation Workflow (Browser MCP)

## Overview

This protocol defines standard procedures for basic web navigation using Browser MCP tools. These operations form the foundation for more complex browser automation workflows.

## Prerequisites

1. Browser MCP server must be running and accessible
2. Playwright browsers installed (`~/.cache/ms-playwright/`)
3. For headed mode: working display (DISPLAY variable set)
4. Environment variables configured in MCP config

## Pre-Flight Check

Before starting navigation, verify the browser is ready:

```
1. Use browser_snapshot to check current page state
2. If no page is loaded, navigate to initial URL
3. Confirm browser response with status check
```

---

## Protocol 1: Simple Page Navigation

### Purpose
Navigate to a single URL and verify the page loaded successfully.

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

### Success Criteria
- Page URL matches expected destination
- Expected content visible in snapshot
- No error messages or failed resource loads

### Error Handling
- **Timeout**: Increase wait time or check network connectivity
- **404/Error page**: Verify URL is correct
- **Redirect**: Check final URL in snapshot

---

## Protocol 2: Navigate with Element Verification

### Purpose
Navigate to a page and confirm specific elements are present before proceeding.

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

### Element Verification Checklist
- [ ] Target element appears in snapshot
- [ ] Element has valid ref ID for interaction
- [ ] No overlapping elements blocking interaction
- [ ] Page is fully loaded (no loading indicators)

---

## Protocol 3: Sequential Page Navigation

### Purpose
Navigate through multiple pages in sequence (e.g., multi-step form, wizard).

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

### Navigation State Tracking
Track progress through multi-page flows:
- Current page/step number
- Completed actions on each page
- Data entered (if applicable)
- Expected final destination

---

## Protocol 4: Navigation with History

### Purpose
Navigate forward and backward through browser history.

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

### History Navigation Notes
- "back" and "forward" are special URL values
- Browser must have history to navigate
- Some sites may not work with history navigation (SPAs with client-side routing)

---

## Protocol 5: Handle Page Redirects

### Purpose
Navigate to a URL that may redirect and verify final destination.

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

### Redirect Handling
- Allow sufficient wait time for multi-hop redirects
- Check for authentication redirects (login pages)
- Handle cookie consent redirects
- Verify HTTPS redirect completion

---

## Common Navigation Patterns

### Pattern: Authenticated Navigation

```
1. Navigate to login page
2. Enter credentials (separate form workflow)
3. Submit login
4. Wait for redirect to dashboard/home
5. Verify authentication succeeded
6. Continue with authenticated navigation
```

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

### Pattern: SPA (Single Page Application) Navigation

```
1. Navigate to SPA root
2. Wait for initial load (longer than static sites)
3. Use click navigation instead of URL navigation
4. Wait for route change indicators
5. Verify new content loaded (not just URL change)
```

---

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
