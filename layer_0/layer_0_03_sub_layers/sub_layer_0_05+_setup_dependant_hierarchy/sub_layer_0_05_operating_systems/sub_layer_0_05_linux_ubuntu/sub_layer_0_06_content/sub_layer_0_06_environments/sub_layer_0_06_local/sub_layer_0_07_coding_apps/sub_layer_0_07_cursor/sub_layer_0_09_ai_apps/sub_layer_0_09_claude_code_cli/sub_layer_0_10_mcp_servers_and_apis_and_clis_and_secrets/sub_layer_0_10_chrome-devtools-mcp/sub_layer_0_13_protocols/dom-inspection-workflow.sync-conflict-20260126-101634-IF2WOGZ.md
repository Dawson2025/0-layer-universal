# DOM Inspection Workflow

This workflow describes how to use Chrome DevTools MCP to inspect, query, and manipulate the Document Object Model (DOM) of web pages.

## Overview

The DOM domain of Chrome DevTools Protocol provides comprehensive access to the page's document structure. This workflow covers querying elements, reading attributes, observing mutations, and executing JavaScript in page context.

## Prerequisites

1. Chrome running with remote debugging enabled
2. Chrome DevTools MCP server connected
3. Target page loaded in browser

## Workflow Steps

### Step 1: Enable DOM Domain

Enable the DOM domain to access document structure:

```
Action: Enable DOM access
CDP Domain: DOM
Method: DOM.enable
```

This enables:
- Document tree traversal
- Element queries
- Attribute access
- DOM mutation observation

### Step 2: Get Document Root

Retrieve the document root node:

```
Action: Get document
CDP Method: DOM.getDocument
Output: Root node with children
```

The document node provides:
- `nodeId`: Unique identifier for the node
- `nodeName`: Tag name (e.g., "HTML", "DIV")
- `nodeType`: Type of node (1=element, 3=text, etc.)
- `children`: Child nodes

### Step 3: Query Elements

Find elements using CSS selectors or XPath:

**CSS Selector Query:**
```
Method: DOM.querySelector / DOM.querySelectorAll
Input: nodeId (document root), selector (CSS selector)
Output: nodeId(s) of matching elements
```

**XPath Query:**
```
Method: DOM.performSearch
Input: query (XPath expression)
Output: searchId, resultCount
```

### Step 4: Inspect Element Properties

For each element, retrieve:

**Attributes:**
```
Method: DOM.getAttributes
Input: nodeId
Output: Array of [name, value] pairs
```

**Computed Styles:**
```
Method: CSS.getComputedStyleForNode
Input: nodeId
Output: Computed CSS properties
```

**Box Model:**
```
Method: DOM.getBoxModel
Input: nodeId
Output: content, padding, border, margin boxes
```

### Step 5: Observe DOM Changes

Monitor DOM mutations in real-time:

```
Method: DOM.setChildNodesRequested
Events: DOM.childNodeInserted, DOM.childNodeRemoved, DOM.attributeModified
```

## Common Use Cases

### Use Case 1: Find Elements by Selector

**Scenario:** Locate specific elements on the page

**Workflow:**
1. Enable DOM domain
2. Get document root
3. Query with CSS selector:
   - `#elementId` - By ID
   - `.className` - By class
   - `div.class` - Tag with class
   - `[data-attribute]` - By attribute
   - `parent > child` - Direct child

**Example Selectors:**
```
"button.submit"           - Submit buttons
"input[type='email']"     - Email input fields
"#main-content p"         - Paragraphs in main content
"[data-testid='login']"   - Elements with test ID
"nav a[href^='/']"        - Navigation links
```

### Use Case 2: Verify Element State

**Scenario:** Check if element has expected attributes/content

**Workflow:**
1. Query element by selector
2. Get element attributes
3. Verify:
   - Required attributes present
   - Attribute values correct
   - Element visible (computed styles)
   - Text content matches

**Verification Checks:**
- Is element present in DOM?
- Does it have expected classes?
- Is it visible (display, visibility)?
- Does text content match expected?
- Are ARIA attributes correct?

### Use Case 3: Monitor Dynamic Content

**Scenario:** Track DOM changes as application runs

**Workflow:**
1. Enable DOM domain
2. Set up mutation observation
3. Perform actions that modify DOM
4. Capture mutation events:
   - Nodes added
   - Nodes removed
   - Attributes changed
   - Character data modified

**Use For:**
- Verifying UI updates
- Tracking dynamic content loading
- Monitoring AJAX-driven changes
- Debugging rendering issues

### Use Case 4: Accessibility Inspection

**Scenario:** Verify accessibility tree structure

**Workflow:**
1. Enable Accessibility domain
2. Get accessibility tree
3. Analyze:
   - ARIA roles
   - ARIA labels
   - Focus order
   - Interactive elements

**Key Accessibility Checks:**
- Images have alt text
- Form fields have labels
- Buttons have accessible names
- Landmarks properly defined
- Focus order logical

### Use Case 5: Form State Analysis

**Scenario:** Inspect form field values and states

**Workflow:**
1. Query form element
2. Get all form fields
3. For each field, check:
   - Current value
   - Validation state
   - Disabled/enabled
   - Required attribute

**Form Analysis:**
```
Query: "form#loginForm input, form#loginForm select"
Check: value, validity, disabled, required, type
```

## Advanced Techniques

### Execute JavaScript in Page Context

Run JavaScript and interact with DOM directly:

```
Method: Runtime.evaluate
Input: JavaScript expression
Output: Return value from expression
```

**Examples:**
```javascript
// Get element text content
document.querySelector('#title').textContent

// Check element visibility
getComputedStyle(document.querySelector('#modal')).display

// Get form field value
document.querySelector('input[name="email"]').value

// Count list items
document.querySelectorAll('ul.items li').length
```

### Capture Element Screenshot

Screenshot a specific element:

```
Method: DOM.getBoxModel (get element bounds)
Method: Page.captureScreenshot (with clip region)
```

### Set Element Attributes

Modify element attributes:

```
Method: DOM.setAttributeValue
Input: nodeId, name, value
```

**Use Cases:**
- Add test markers
- Modify form values
- Change visibility for testing
- Add/remove classes

### Remove Elements

Remove elements from DOM:

```
Method: DOM.removeNode
Input: nodeId
```

**Use For:**
- Remove interfering elements
- Hide popups/modals
- Clean up test artifacts

## Output Examples

### Document Node

```json
{
  "root": {
    "nodeId": 1,
    "backendNodeId": 1,
    "nodeType": 9,
    "nodeName": "#document",
    "localName": "",
    "nodeValue": "",
    "childNodeCount": 2,
    "children": [
      {
        "nodeId": 2,
        "nodeType": 10,
        "nodeName": "html"
      },
      {
        "nodeId": 3,
        "nodeType": 1,
        "nodeName": "HTML",
        "localName": "html",
        "attributes": ["lang", "en"],
        "childNodeCount": 2
      }
    ]
  }
}
```

### Element with Attributes

```json
{
  "nodeId": 42,
  "nodeType": 1,
  "nodeName": "BUTTON",
  "localName": "button",
  "attributes": [
    "class", "btn btn-primary",
    "type", "submit",
    "id", "submitBtn",
    "data-action", "login"
  ],
  "childNodeCount": 1
}
```

### Box Model

```json
{
  "model": {
    "content": [100, 200, 300, 200, 300, 250, 100, 250],
    "padding": [95, 195, 305, 195, 305, 255, 95, 255],
    "border": [94, 194, 306, 194, 306, 256, 94, 256],
    "margin": [84, 184, 316, 184, 316, 266, 84, 266],
    "width": 200,
    "height": 50
  }
}
```

### Computed Styles

```json
{
  "computedStyle": [
    {"name": "display", "value": "block"},
    {"name": "visibility", "value": "visible"},
    {"name": "opacity", "value": "1"},
    {"name": "color", "value": "rgb(33, 37, 41)"},
    {"name": "font-size", "value": "16px"},
    {"name": "position", "value": "relative"}
  ]
}
```

## Element Query Reference

### CSS Selector Syntax

| Selector | Description | Example |
|----------|-------------|---------|
| `#id` | By ID | `#main` |
| `.class` | By class | `.btn` |
| `tag` | By tag name | `div` |
| `[attr]` | Has attribute | `[required]` |
| `[attr=val]` | Attribute equals | `[type="submit"]` |
| `[attr^=val]` | Attribute starts with | `[href^="https"]` |
| `[attr$=val]` | Attribute ends with | `[src$=".png"]` |
| `[attr*=val]` | Attribute contains | `[class*="btn"]` |
| `parent child` | Descendant | `div p` |
| `parent > child` | Direct child | `ul > li` |
| `el + sibling` | Adjacent sibling | `h1 + p` |
| `el ~ sibling` | General sibling | `h1 ~ p` |
| `:first-child` | First child | `li:first-child` |
| `:last-child` | Last child | `li:last-child` |
| `:nth-child(n)` | Nth child | `tr:nth-child(odd)` |
| `:not(sel)` | Negation | `input:not([disabled])` |

### XPath Syntax

| XPath | Description | Example |
|-------|-------------|---------|
| `//tag` | All tags | `//div` |
| `/html/body` | Absolute path | `/html/body/main` |
| `//tag[@attr]` | With attribute | `//input[@required]` |
| `//tag[@attr='val']` | Attribute value | `//button[@type='submit']` |
| `//tag[text()='val']` | Text content | `//h1[text()='Title']` |
| `//tag[contains(@attr,'val')]` | Attribute contains | `//div[contains(@class,'card')]` |
| `//tag[contains(text(),'val')]` | Text contains | `//p[contains(text(),'error')]` |
| `//parent/child` | Child | `//ul/li` |
| `//ancestor//descendant` | Descendant | `//form//input` |
| `//tag[1]` | First match | `//li[1]` |
| `//tag[last()]` | Last match | `//li[last()]` |

## Troubleshooting

### Element Not Found

**Problem:** querySelector returns null

**Solutions:**
1. Verify selector syntax is correct
2. Check if element is in an iframe (different document)
3. Element may be dynamically loaded - wait for it
4. Shadow DOM elements need special handling
5. Use broader selector then narrow down

### Stale Node ID

**Problem:** nodeId no longer valid

**Solutions:**
1. Re-query the document after DOM changes
2. Page navigation invalidates all nodeIds
3. Use DOM.resolveNode to get JavaScript reference
4. Cache selectors, not nodeIds

### Cannot Access Shadow DOM

**Problem:** Elements inside shadow DOM not accessible

**Solutions:**
1. Use DOM.describeNode with pierce option
2. Get shadow root and query within it
3. Use JavaScript evaluation to access shadow DOM

### Computed Styles Not Available

**Problem:** CSS.getComputedStyleForNode fails

**Solutions:**
1. Ensure CSS domain is enabled
2. Element must be in the DOM (not detached)
3. Document must be fully loaded

---

## Related Workflows

- [Network Inspection Workflow](./network-inspection-workflow.md)
- [Console Log Capture Workflow](./console-log-capture-workflow.md)

---

**Last Updated**: 2025-01-13
**CDP Domains**: DOM, CSS, Accessibility
**Reference**:
- https://chromedevtools.github.io/devtools-protocol/tot/DOM/
- https://chromedevtools.github.io/devtools-protocol/tot/CSS/
- https://chromedevtools.github.io/devtools-protocol/tot/Accessibility/
