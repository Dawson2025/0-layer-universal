---
resource_id: "8e8f32e9-f2b6-4c47-816a-bb64debfa07e"
resource_type: "document"
resource_name: "dom-inspection-workflow"
---
# DOM Inspection Workflow

This workflow describes how to use Chrome DevTools MCP to inspect, query, and manipulate the Document Object Model (DOM) of web pages.

<!-- section_id: "56f58b11-2390-4455-9c39-f22bac9e8068" -->
## Overview

The DOM domain of Chrome DevTools Protocol provides comprehensive access to the page's document structure. This workflow covers querying elements, reading attributes, observing mutations, and executing JavaScript in page context.

<!-- section_id: "c65563a8-3c64-4f3b-a7d6-4dace3e93b5b" -->
## Prerequisites

1. Chrome running with remote debugging enabled
2. Chrome DevTools MCP server connected
3. Target page loaded in browser

<!-- section_id: "291cf8c7-9546-4264-a3c4-8b890a584ea0" -->
## Workflow Steps

<!-- section_id: "f86f83b8-1ca7-4fb3-b4ff-975134de59b4" -->
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

<!-- section_id: "736fbb29-af32-4a1e-a441-f6316be98d92" -->
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

<!-- section_id: "8dcb84e9-2fb3-41ac-b1b5-6df35f5d1cdc" -->
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

<!-- section_id: "4576ab84-f17c-4f4f-b73b-0960c14dc1dc" -->
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

<!-- section_id: "9f73135e-dfcf-40e5-9d03-5b20bb1fe203" -->
### Step 5: Observe DOM Changes

Monitor DOM mutations in real-time:

```
Method: DOM.setChildNodesRequested
Events: DOM.childNodeInserted, DOM.childNodeRemoved, DOM.attributeModified
```

<!-- section_id: "61761570-20e2-4626-a2d5-47559821506f" -->
## Common Use Cases

<!-- section_id: "889abca3-69a7-4916-b128-c3a9f4305106" -->
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

<!-- section_id: "324a8a93-357b-44ed-98d0-dadc72dcb9d7" -->
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

<!-- section_id: "97307d14-e2c7-45a8-aa09-f9fd48ecb013" -->
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

<!-- section_id: "ab28304e-7fc5-495e-bf11-468446c46942" -->
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

<!-- section_id: "7bfde103-2902-4c4f-83b3-d57ff202c31a" -->
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

<!-- section_id: "6c2d4126-2ff1-4e49-9bdd-07eb77833c60" -->
## Advanced Techniques

<!-- section_id: "253276a9-60a2-4603-a04a-864c0c2b3157" -->
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

<!-- section_id: "7c1c26d6-a51e-4add-b0fc-b8ad89976206" -->
### Capture Element Screenshot

Screenshot a specific element:

```
Method: DOM.getBoxModel (get element bounds)
Method: Page.captureScreenshot (with clip region)
```

<!-- section_id: "2f5f8ac3-8e46-40b9-b0e7-63bb5d844694" -->
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

<!-- section_id: "501aef4d-8d77-45cf-8f26-6b7ef7ff80ca" -->
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

<!-- section_id: "4085a959-2f9a-461c-a6d1-bca41f3dcb96" -->
## Output Examples

<!-- section_id: "89792ce8-f6d0-4016-b9d9-6afe6846ae46" -->
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

<!-- section_id: "d712dc4c-a3c8-49e2-86cd-78bb420c155e" -->
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

<!-- section_id: "f18e4ed5-7628-4c56-8a79-0988fc68aa93" -->
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

<!-- section_id: "70481878-2bf4-4a91-b319-0b91de1f47a4" -->
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

<!-- section_id: "4455668d-ba6e-43a8-be50-305257ac99f7" -->
## Element Query Reference

<!-- section_id: "5029b0a0-c54b-4bd2-89af-e3e24c426349" -->
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

<!-- section_id: "d4be05b5-8e7c-486d-b8a7-e761290a4648" -->
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

<!-- section_id: "499a40ca-55ab-461c-bd7a-0d8777729cc8" -->
## Troubleshooting

<!-- section_id: "caf7de4d-edcb-41dd-a3c4-2195e05eac60" -->
### Element Not Found

**Problem:** querySelector returns null

**Solutions:**
1. Verify selector syntax is correct
2. Check if element is in an iframe (different document)
3. Element may be dynamically loaded - wait for it
4. Shadow DOM elements need special handling
5. Use broader selector then narrow down

<!-- section_id: "97707b1a-2900-4204-ba04-ef4b18df649b" -->
### Stale Node ID

**Problem:** nodeId no longer valid

**Solutions:**
1. Re-query the document after DOM changes
2. Page navigation invalidates all nodeIds
3. Use DOM.resolveNode to get JavaScript reference
4. Cache selectors, not nodeIds

<!-- section_id: "89926f76-7956-4635-8578-e7056b0ed0cd" -->
### Cannot Access Shadow DOM

**Problem:** Elements inside shadow DOM not accessible

**Solutions:**
1. Use DOM.describeNode with pierce option
2. Get shadow root and query within it
3. Use JavaScript evaluation to access shadow DOM

<!-- section_id: "3c29efa1-3d93-464e-bfd1-f64f72cfd801" -->
### Computed Styles Not Available

**Problem:** CSS.getComputedStyleForNode fails

**Solutions:**
1. Ensure CSS domain is enabled
2. Element must be in the DOM (not detached)
3. Document must be fully loaded

---

<!-- section_id: "25c6ce20-bc5c-441e-8b25-2fb9b8c3685a" -->
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
