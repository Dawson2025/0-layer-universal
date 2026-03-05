---
resource_id: "0c5af084-e2ff-47e7-a0e7-c88c985eeca0"
resource_type: "protocol"
resource_name: "page_analysis_workflow"
---
# Page Analysis Workflow

<!-- section_id: "c4ab4635-f821-4540-a311-ce89f1328ace" -->
## Overview

This workflow describes the standardized process for analyzing web pages using the Claude in Chrome MCP server. Page analysis involves understanding page structure, identifying key elements, and extracting meaningful information for decision-making.

<!-- section_id: "8e0e4de2-6b9f-444a-90b0-fe2758915d41" -->
## Use Cases

- Understanding page layout and structure
- Identifying interactive elements for automation
- Auditing page accessibility
- Debugging UI issues
- Preparing for form automation
- Content verification

<!-- section_id: "6f61f9f0-55e7-45f4-8cc4-f126f72eb6e1" -->
## Workflow Steps

<!-- section_id: "7971044e-1bfb-459f-b62e-a2161b68829e" -->
### Step 1: Initialize Tab Context

Before any page analysis, establish the tab context to get valid tab IDs.

```python
# Get current tab context or create new if empty
result = mcp__claude-in-chrome__tabs_context_mcp(createIfEmpty=True)

# Extract the tab ID from result
# tab_id = result.tabs[0].id (example structure)
```

**Expected Output**: List of available tabs with their IDs, URLs, and titles.

**Failure Handling**: If no tabs exist and createIfEmpty is True, a new window with MCP tab group will be created.

<!-- section_id: "428346e6-799f-4f9b-bfaf-295705924bdb" -->
### Step 2: Navigate to Target Page (if needed)

If the target page is not already loaded, navigate to it.

```python
# Navigate to the target URL
mcp__claude-in-chrome__navigate(
    url="https://example.com/page-to-analyze",
    tabId=TAB_ID
)
```

**Wait Consideration**: Allow time for page to fully load before analysis.

```python
# Optional: Wait for page to stabilize
mcp__claude-in-chrome__computer(
    action="wait",
    duration=2,
    tabId=TAB_ID
)
```

<!-- section_id: "20fc615f-96bd-4b96-8fb3-43ae01097d5c" -->
### Step 3: Capture Initial State

Take a screenshot to visually understand the current page state.

```python
# Capture viewport screenshot
mcp__claude-in-chrome__computer(
    action="screenshot",
    tabId=TAB_ID
)
```

**Use Cases for Screenshots**:
- Visual verification of page load
- Documentation of page state
- Identifying visual elements not captured in accessibility tree
- Debugging layout issues

<!-- section_id: "8a9d020f-b9ca-4f3b-97d2-fd9eac642103" -->
### Step 4: Get Accessibility Tree

The accessibility tree provides structural understanding of the page.

```python
# Get full accessibility tree
mcp__claude-in-chrome__read_page(
    tabId=TAB_ID
)

# Or filter for interactive elements only
mcp__claude-in-chrome__read_page(
    tabId=TAB_ID,
    filter="interactive"
)
```

**Understanding the Output**:

The accessibility tree returns elements with:
- `ref_id`: Reference ID for targeting the element in actions
- `role`: ARIA role (button, textbox, link, etc.)
- `name`: Accessible name/label
- `value`: Current value (for inputs)
- `children`: Nested child elements

**Depth Control**: For complex pages, limit depth to avoid overwhelming output:

```python
mcp__claude-in-chrome__read_page(
    tabId=TAB_ID,
    depth=5  # Limit to 5 levels deep
)
```

<!-- section_id: "128052d7-0f49-4cc6-b17a-e0b6dba8f6fd" -->
### Step 5: Find Specific Elements

Use natural language queries to locate elements of interest.

```python
# Find by purpose
mcp__claude-in-chrome__find(
    query="login button",
    tabId=TAB_ID
)

# Find by content
mcp__claude-in-chrome__find(
    query="text containing 'Sign Up'",
    tabId=TAB_ID
)

# Find form fields
mcp__claude-in-chrome__find(
    query="email input field",
    tabId=TAB_ID
)
```

**Result Interpretation**: Returns up to 20 matching elements with reference IDs that can be used in subsequent actions.

<!-- section_id: "20fcc7e6-98aa-4505-9bc1-66dcc0e750e7" -->
### Step 6: Extract Page Text

Get raw text content for content analysis.

```python
# Extract main text content
mcp__claude-in-chrome__get_page_text(
    tabId=TAB_ID
)
```

**Best For**:
- Article content extraction
- Blog post analysis
- Documentation pages
- Content verification

<!-- section_id: "c0a23b2e-ffa3-4b5a-aaf1-d0fc1298c742" -->
### Step 7: Execute Custom Analysis (Optional)

Use JavaScript for custom analysis needs.

```python
# Get page metadata
mcp__claude-in-chrome__javascript_tool(
    action="javascript_exec",
    text="({ title: document.title, url: window.location.href, lang: document.documentElement.lang })",
    tabId=TAB_ID
)

# Count specific elements
mcp__claude-in-chrome__javascript_tool(
    action="javascript_exec",
    text="document.querySelectorAll('form').length",
    tabId=TAB_ID
)

# Get computed styles
mcp__claude-in-chrome__javascript_tool(
    action="javascript_exec",
    text="window.getComputedStyle(document.body).backgroundColor",
    tabId=TAB_ID
)
```

<!-- section_id: "f33e07d2-3eec-447c-8820-b65160d427b6" -->
### Step 8: Monitor Console and Network (Optional)

For debugging and deeper analysis.

```python
# Check for console errors
mcp__claude-in-chrome__read_console_messages(
    tabId=TAB_ID,
    onlyErrors=True
)

# Monitor API calls
mcp__claude-in-chrome__read_network_requests(
    tabId=TAB_ID,
    urlPattern="/api/"
)
```

<!-- section_id: "4b7781e9-bb79-4ea9-bede-7ec69979f7ae" -->
## Analysis Patterns

<!-- section_id: "e5283bed-424d-4e36-b735-c94343e79649" -->
### Pattern 1: Form Analysis

```python
# 1. Get all form elements
read_page(tabId=TAB_ID, filter="interactive")

# 2. Find specific form fields
find(query="username field", tabId=TAB_ID)
find(query="password field", tabId=TAB_ID)
find(query="submit button", tabId=TAB_ID)

# 3. Verify form structure with JavaScript
javascript_tool(
    action="javascript_exec",
    text="Array.from(document.forms).map(f => ({ id: f.id, action: f.action, method: f.method, fields: f.elements.length }))",
    tabId=TAB_ID
)
```

<!-- section_id: "95b93fba-00df-48e2-bb9e-068ccd06b9a3" -->
### Pattern 2: Navigation Structure Analysis

```python
# 1. Find all navigation elements
find(query="navigation menu", tabId=TAB_ID)
find(query="header links", tabId=TAB_ID)

# 2. Get all links
javascript_tool(
    action="javascript_exec",
    text="Array.from(document.querySelectorAll('nav a')).map(a => ({ text: a.textContent.trim(), href: a.href }))",
    tabId=TAB_ID
)
```

<!-- section_id: "26ea9d28-1cad-4e3c-86a2-386afd0fde1f" -->
### Pattern 3: Content Structure Analysis

```python
# 1. Get text content
get_page_text(tabId=TAB_ID)

# 2. Analyze heading structure
javascript_tool(
    action="javascript_exec",
    text="Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6')).map(h => ({ level: h.tagName, text: h.textContent.trim() }))",
    tabId=TAB_ID
)

# 3. Check for main content area
find(query="main content area", tabId=TAB_ID)
```

<!-- section_id: "118547d4-ef38-4a95-a111-3f75b7f6217f" -->
### Pattern 4: Accessibility Audit

```python
# 1. Get full accessibility tree
read_page(tabId=TAB_ID)

# 2. Check for missing alt text
javascript_tool(
    action="javascript_exec",
    text="Array.from(document.images).filter(img => !img.alt).map(img => img.src)",
    tabId=TAB_ID
)

# 3. Check for form labels
javascript_tool(
    action="javascript_exec",
    text="Array.from(document.querySelectorAll('input:not([type=hidden])')).filter(input => !input.labels.length && !input.ariaLabel).map(input => input.name || input.id)",
    tabId=TAB_ID
)
```

<!-- section_id: "f7fea295-b8ac-4d7d-a55a-687d5ae32cf7" -->
## Output Documentation Template

After completing analysis, document findings in this format:

```markdown
## Page Analysis Report

**URL**: [page URL]
**Analyzed**: [timestamp]
**Tab ID**: [tab ID used]

### Page Overview
- Title: [page title]
- Type: [form, article, dashboard, etc.]
- Load Status: [complete/partial/errors]

### Structure Summary
- Main Sections: [list major sections]
- Navigation Elements: [count and types]
- Forms: [count and purposes]
- Interactive Elements: [count]

### Key Elements Identified
| Element | Ref ID | Purpose | Notes |
|---------|--------|---------|-------|
| ... | ... | ... | ... |

### Accessibility Notes
- [any accessibility concerns]

### Console Errors (if any)
- [list relevant errors]

### Recommendations
- [suggestions for automation or improvements]
```

<!-- section_id: "c3d8e06a-3983-4dbf-b68d-c7d6014ea405" -->
## Error Handling

<!-- section_id: "56095199-6a8b-4343-8634-d027cfc60545" -->
### Page Not Loaded
```python
# Verify page loaded
result = javascript_tool(
    action="javascript_exec",
    text="document.readyState",
    tabId=TAB_ID
)
# Should return "complete"
```

<!-- section_id: "2083d922-7832-4c27-a4c2-8dccfa4f9dc5" -->
### Timeout on Large Pages
```python
# Use depth limiting for large pages
read_page(tabId=TAB_ID, depth=3)

# Focus on specific sections
read_page(tabId=TAB_ID, ref_id="ref_5")  # Start from specific element
```

<!-- section_id: "9688f411-8268-47d4-a50c-6c002786f7ad" -->
### Dynamic Content
```python
# Wait for dynamic content to load
computer(action="wait", duration=3, tabId=TAB_ID)

# Or wait for specific text to appear
# (requires monitoring approach)
```

<!-- section_id: "63e981f1-8e20-4dae-a7bc-b3198dff677d" -->
## Best Practices

1. **Always get tab context first** - Stale tab IDs cause failures
2. **Take screenshots before and after** - Visual documentation aids debugging
3. **Use depth limits on complex pages** - Prevents output overflow
4. **Filter for interactive elements when appropriate** - Reduces noise
5. **Combine multiple analysis methods** - Accessibility tree + JavaScript for completeness
6. **Document ref_ids** - They're needed for subsequent interactions
7. **Check console errors** - They often explain page behavior issues

---

**Related Workflows**:
- [Interactive Browsing Workflow](./interactive_browsing_workflow.md)
- [Content Extraction Workflow](./content_extraction_workflow.md)

**Last Updated**: 2026-01-13
