---
resource_id: "12762781-d216-44c3-a554-2eea1bcc59e0"
resource_type: "document"
resource_name: "multi_tab_workflow"
---
# Multi-Tab Workflow (Browser MCP)

<!-- section_id: "0ed572fc-deb5-4878-a000-cb9f8eabfb5a" -->
## Overview

This protocol defines standard procedures for managing multiple browser tabs using Browser MCP tools. Multi-tab workflows are useful for comparing content, performing parallel research, or maintaining separate contexts.

<!-- section_id: "9519aa46-f96f-428d-b884-08cb3f798d23" -->
## Prerequisites

1. Browser MCP server running and accessible
2. Sufficient system memory for multiple tabs (each tab uses ~100-300MB)
3. Understanding of tab ID system (tabs are referenced by numeric ID)

<!-- section_id: "c783b986-bdab-4bf4-b7f6-35010db8a456" -->
## Tab Management Fundamentals

<!-- section_id: "e5a04187-06ae-4c5a-ae80-0deb577dbfa1" -->
### Tab Identification
- Each tab has a unique numeric ID
- Tab IDs are assigned when tabs are created
- IDs persist until the tab is closed
- Use `browser_tabs` with action "list" to get current tab IDs

<!-- section_id: "755c5834-bf99-45f3-8c20-e5de92dfe0ca" -->
### Tab States
- **Active**: Currently focused tab
- **Background**: Open but not focused
- **Loading**: Page navigation in progress

---

<!-- section_id: "3b685009-b96d-49c9-8e85-17ebf7db5f35" -->
## Protocol 1: Create and Switch Between Tabs

<!-- section_id: "b033395b-997b-4619-8795-8831ccd25192" -->
### Purpose
Open multiple tabs and switch between them for different tasks.

<!-- section_id: "8b53a06e-7882-4197-8bf9-a834abae72b2" -->
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

<!-- section_id: "2b854e55-e237-4407-979a-35bf7ae2293b" -->
### Tab Switching Notes
- Switching tabs changes which tab receives subsequent commands
- Always verify active tab with snapshot before important operations
- Tab indices may shift when tabs are closed

---

<!-- section_id: "706e0e55-1739-4ff8-9d03-ad32b0dc6b2c" -->
## Protocol 2: Parallel Research Workflow

<!-- section_id: "70b94a4c-7ac1-4fd2-8cd1-45306b017fbf" -->
### Purpose
Research multiple sources simultaneously by opening each in a separate tab.

<!-- section_id: "956d7e38-c55d-4e23-a15a-fc02eaa93ab0" -->
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

<!-- section_id: "47401b58-773c-4933-80d9-d15ba13a278c" -->
### Research Workflow Best Practices
- Open all tabs before starting extraction
- Maintain consistent tab order for easy reference
- Close tabs when done to free resources
- Use descriptive notes about each tab's content

---

<!-- section_id: "4417afc2-7d4a-4bfd-ab27-28224ae379cb" -->
## Protocol 3: Comparison Workflow

<!-- section_id: "f3be5918-60fc-474f-8cfd-a1ec78d07fb3" -->
### Purpose
Compare content between two or more pages side by side.

<!-- section_id: "98b84831-fb3d-472c-ac5e-efe02a6020e4" -->
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

<!-- section_id: "f82c7f83-bf5f-4961-9fd9-5b86505249f0" -->
### Comparison Use Cases
- A/B testing analysis
- Before/after documentation
- Price comparison across sites
- Feature comparison between products
- Code diff visualization

---

<!-- section_id: "446d7aca-6c30-44be-82a8-0f1d9948b926" -->
## Protocol 4: Session Isolation Workflow

<!-- section_id: "ee50dd68-4844-4a8e-9a85-06dafd0203e5" -->
### Purpose
Maintain separate browsing contexts (e.g., logged in as different users).

<!-- section_id: "dde8df29-4976-488b-b8ba-c0d8191b9dca" -->
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

<!-- section_id: "e47f357d-8d5b-4b1d-bdd9-8e8166542116" -->
### Session Isolation Notes
- Standard tabs share cookies and session storage
- True session isolation requires separate browser profiles
- See CONCURRENT_BROWSER_SETUP.md for multi-profile setup
- Some actions may affect all tabs (logout, cookie clearing)

---

<!-- section_id: "c5759337-8f55-462d-9852-6f6a6cdc3fe9" -->
## Protocol 5: Tab Cleanup Workflow

<!-- section_id: "4ad97ce8-c04d-4161-ad00-1613b6bf5c4c" -->
### Purpose
Clean up tabs after completing a multi-tab workflow.

<!-- section_id: "7819d71a-337a-4a1a-a91e-25aa93ffd07e" -->
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

<!-- section_id: "4ef5fa70-71bc-4141-b453-1aac9f44ac70" -->
### Tab Cleanup Best Practices
- Close tabs in reverse order (highest index first)
- Always list tabs before closing to verify indices
- Keep at least one tab open (browser needs at least one)
- Close unused tabs promptly to free memory

---

<!-- section_id: "b26c524a-afb9-483c-8bca-774c4419be60" -->
## Protocol 6: Form Continuation Across Tabs

<!-- section_id: "75653a87-5360-44db-818e-fd435bc4976f" -->
### Purpose
Complete a form that spans multiple pages using tabs to preserve state.

<!-- section_id: "d5042c68-d543-42d1-b406-b2793276ce7e" -->
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

<!-- section_id: "163826e1-e515-4977-9e07-67914e2a66e5" -->
## Error Handling

<!-- section_id: "36a39918-bc28-402a-b362-42df508abc9e" -->
### "Tab not found" Error

**Cause**: Tab was closed or index is out of range

**Solution**:
```
1. browser_tabs action: "list" to get current tabs
2. Verify target tab still exists
3. Use correct index from fresh list
```

<!-- section_id: "51583550-26cd-4ccd-91f5-13233f389f6c" -->
### "Multiple tabs have same content"

**Cause**: Navigation happened in wrong tab

**Solution**:
```
1. Always verify active tab before navigation
2. Use browser_tabs action: "select" explicitly
3. Take snapshot to confirm correct tab
```

<!-- section_id: "01c48a07-055d-4d2c-8185-93cb3b863555" -->
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

<!-- section_id: "7662d1d7-4df7-4435-aa88-ef2f7495cb8c" -->
## Tab Management Reference

<!-- section_id: "83b57be1-0ec4-4d44-bcf2-eb9f2e728bc3" -->
### Quick Commands

| Action | Tool Call |
|--------|-----------|
| List all tabs | `browser_tabs action: "list"` |
| New tab | `browser_tabs action: "new"` |
| Switch to tab N | `browser_tabs action: "select" index: N` |
| Close current tab | `browser_tabs action: "close"` |
| Close tab N | `browser_tabs action: "close" index: N` |

<!-- section_id: "96c4186c-f5d2-4832-9f3d-14d71f00209a" -->
### Tab Index Rules
- Indices are 0-based (first tab is 0)
- Indices update when tabs are closed
- Newly created tab becomes active
- Closing active tab selects adjacent tab

<!-- section_id: "b836d4d4-e714-4251-b0b5-e29891f1a264" -->
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
