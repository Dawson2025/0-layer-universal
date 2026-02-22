# Multi-Tab Workflow (Browser MCP)

## Overview

This protocol defines standard procedures for managing multiple browser tabs using Browser MCP tools. Multi-tab workflows are useful for comparing content, performing parallel research, or maintaining separate contexts.

## Prerequisites

1. Browser MCP server running and accessible
2. Sufficient system memory for multiple tabs (each tab uses ~100-300MB)
3. Understanding of tab ID system (tabs are referenced by numeric ID)

## Tab Management Fundamentals

### Tab Identification
- Each tab has a unique numeric ID
- Tab IDs are assigned when tabs are created
- IDs persist until the tab is closed
- Use `browser_tabs` with action "list" to get current tab IDs

### Tab States
- **Active**: Currently focused tab
- **Background**: Open but not focused
- **Loading**: Page navigation in progress

---

## Protocol 1: Create and Switch Between Tabs

### Purpose
Open multiple tabs and switch between them for different tasks.

### Steps

1. **List current tabs**
   ```
   Tool: browser_tabs
   Parameters:
     action: "list"
   ```
   Output: Array of tab objects with IDs and URLs

2. **Create a new tab**
   ```
   Tool: browser_tabs
   Parameters:
     action: "new"
   ```
   Output: New tab ID

3. **Navigate new tab to URL**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com"
   ```
   Note: Navigation happens in the currently active tab

4. **Switch to a different tab**
   ```
   Tool: browser_tabs
   Parameters:
     action: "select"
     index: 0  # Tab index (0-based)
   ```

5. **Verify active tab**
   ```
   Tool: browser_snapshot
   ```

### Tab Switching Notes
- Switching tabs changes which tab receives subsequent commands
- Always verify active tab with snapshot before important operations
- Tab indices may shift when tabs are closed

---

## Protocol 2: Parallel Research Workflow

### Purpose
Research multiple sources simultaneously by opening each in a separate tab.

### Steps

1. **Create tabs for each source**
   ```
   For each URL in research_urls:
     a. browser_tabs action: "new"
     b. browser_navigate to URL
     c. Record tab ID and URL mapping
   ```

2. **Build tab reference map**
   ```
   Tab Map Example:
   - Tab 0: https://source1.com (Wikipedia)
   - Tab 1: https://source2.com (Official docs)
   - Tab 2: https://source3.com (Tutorial)
   ```

3. **Gather content from each tab**
   ```
   For each tab:
     a. browser_tabs action: "select" index: N
     b. browser_wait_for page content
     c. browser_snapshot to capture content
     d. Extract relevant information
   ```

4. **Compile findings**
   - Cross-reference information from multiple sources
   - Note which tab/source provided each piece of information
   - Resolve conflicts between sources

### Research Workflow Best Practices
- Open all tabs before starting extraction
- Maintain consistent tab order for easy reference
- Close tabs when done to free resources
- Use descriptive notes about each tab's content

---

## Protocol 3: Comparison Workflow

### Purpose
Compare content between two or more pages side by side.

### Steps

1. **Open comparison targets**
   ```
   # First page
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/version-a"

   # Create second tab
   Tool: browser_tabs
   Parameters:
     action: "new"

   # Second page
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/version-b"
   ```

2. **Capture both pages**
   ```
   # Tab 0 (Version A)
   Tool: browser_tabs
   Parameters:
     action: "select"
     index: 0
   Tool: browser_snapshot
   # Save as snapshot_a

   # Tab 1 (Version B)
   Tool: browser_tabs
   Parameters:
     action: "select"
     index: 1
   Tool: browser_snapshot
   # Save as snapshot_b
   ```

3. **Compare snapshots**
   - Identify differences in structure
   - Note content changes
   - Compare element presence/absence
   - Check for visual differences (if using screenshots)

### Comparison Use Cases
- A/B testing analysis
- Before/after documentation
- Price comparison across sites
- Feature comparison between products
- Code diff visualization

---

## Protocol 4: Session Isolation Workflow

### Purpose
Maintain separate browsing contexts (e.g., logged in as different users).

### Steps

1. **First session (Tab 0)**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/login"
   # Log in as User A
   ```

2. **Second session (New Tab)**
   ```
   Tool: browser_tabs
   Parameters:
     action: "new"
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/login"
   # Log in as User B (may need incognito/profile separation)
   ```

### Session Isolation Notes
- Standard tabs share cookies and session storage
- True session isolation requires separate browser profiles
- See CONCURRENT_BROWSER_SETUP.md for multi-profile setup
- Some actions may affect all tabs (logout, cookie clearing)

---

## Protocol 5: Tab Cleanup Workflow

### Purpose
Clean up tabs after completing a multi-tab workflow.

### Steps

1. **List all open tabs**
   ```
   Tool: browser_tabs
   Parameters:
     action: "list"
   ```

2. **Identify tabs to close**
   - Note indices of completed work tabs
   - Keep tabs that are still needed
   - Be careful with index shifts after closing

3. **Close tabs from highest to lowest index**
   ```
   # Close tab 3 first, then 2, etc.
   # This prevents index shifting issues
   Tool: browser_tabs
   Parameters:
     action: "close"
     index: 3

   Tool: browser_tabs
   Parameters:
     action: "close"
     index: 2
   ```

4. **Verify final state**
   ```
   Tool: browser_tabs
   Parameters:
     action: "list"
   ```

### Tab Cleanup Best Practices
- Close tabs in reverse order (highest index first)
- Always list tabs before closing to verify indices
- Keep at least one tab open (browser needs at least one)
- Close unused tabs promptly to free memory

---

## Protocol 6: Form Continuation Across Tabs

### Purpose
Complete a form that spans multiple pages using tabs to preserve state.

### Steps

1. **Open form in main tab**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/multi-step-form"
   ```

2. **Open reference page in new tab** (for looking up information)
   ```
   Tool: browser_tabs
   Parameters:
     action: "new"
   Tool: browser_navigate
   Parameters:
     url: "https://reference-site.com/data"
   ```

3. **Switch between tabs as needed**
   ```
   # Get reference data
   Tool: browser_tabs
   Parameters:
     action: "select"
     index: 1
   Tool: browser_snapshot
   # Extract needed information

   # Return to form
   Tool: browser_tabs
   Parameters:
     action: "select"
     index: 0
   # Fill form fields with extracted data
   ```

4. **Complete form submission from main tab**

---

## Error Handling

### "Tab not found" Error

**Cause**: Tab was closed or index is out of range

**Solution**:
```
1. browser_tabs action: "list" to get current tabs
2. Verify target tab still exists
3. Use correct index from fresh list
```

### "Multiple tabs have same content"

**Cause**: Navigation happened in wrong tab

**Solution**:
```
1. Always verify active tab before navigation
2. Use browser_tabs action: "select" explicitly
3. Take snapshot to confirm correct tab
```

### Memory issues with many tabs

**Symptoms**: Slow performance, browser crashes

**Solution**:
```
1. Limit concurrent tabs (recommend max 5-8)
2. Close completed tabs promptly
3. Use headless mode to reduce memory
4. Monitor system memory: free -h
```

---

## Tab Management Reference

### Quick Commands

| Action | Tool Call |
|--------|-----------|
| List all tabs | `browser_tabs action: "list"` |
| New tab | `browser_tabs action: "new"` |
| Switch to tab N | `browser_tabs action: "select" index: N` |
| Close current tab | `browser_tabs action: "close"` |
| Close tab N | `browser_tabs action: "close" index: N` |

### Tab Index Rules
- Indices are 0-based (first tab is 0)
- Indices update when tabs are closed
- Newly created tab becomes active
- Closing active tab selects adjacent tab

### Memory Guidelines

| Number of Tabs | Expected Memory | Performance |
|----------------|-----------------|-------------|
| 1-3 | 300-900 MB | Excellent |
| 4-6 | 1-2 GB | Good |
| 7-10 | 2-3 GB | Moderate |
| 10+ | 3+ GB | May degrade |

---

**Last Updated**: 2026-01-13
**Applies To**: Browser MCP for Claude Code CLI on Linux/Ubuntu
