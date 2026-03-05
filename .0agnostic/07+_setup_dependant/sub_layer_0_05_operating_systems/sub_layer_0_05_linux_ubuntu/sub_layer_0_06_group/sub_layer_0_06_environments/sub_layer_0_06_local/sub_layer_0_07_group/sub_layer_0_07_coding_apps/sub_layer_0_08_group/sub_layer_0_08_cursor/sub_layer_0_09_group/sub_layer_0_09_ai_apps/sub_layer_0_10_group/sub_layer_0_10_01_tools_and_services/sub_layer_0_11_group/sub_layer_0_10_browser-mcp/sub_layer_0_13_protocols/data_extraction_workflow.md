---
resource_id: "608d5164-dfe2-4f5b-a92a-d15913c8905e"
resource_type: "document"
resource_name: "data_extraction_workflow"
---
# Data Extraction Workflow (Browser MCP)

## Overview

This protocol defines standard procedures for extracting content and data from web pages using Browser MCP tools. Data extraction workflows are essential for web scraping, research, and content analysis tasks.

## Prerequisites

1. Browser MCP server running and accessible
2. Target page accessible and loaded
3. Understanding of page structure (DOM elements, accessibility tree)
4. Awareness of site's terms of service regarding scraping

## Extraction Methods Overview

| Method | Tool | Best For |
|--------|------|----------|
| Accessibility Snapshot | `browser_snapshot` | Structured page content, interactive elements |
| Page Text | `get_page_text` | Article content, raw text extraction |
| JavaScript Evaluation | `browser_evaluate` | Custom data extraction, complex queries |
| Screenshot | `browser_take_screenshot` | Visual content, image capture |
| Network Requests | `browser_network_requests` | API responses, data endpoints |

---

## Protocol 1: Basic Text Extraction

### Purpose
Extract readable text content from a web page.

### Steps

1. **Navigate to target page**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/article"
   ```

2. **Wait for content to load**
   ```
   Tool: browser_wait_for
   Parameters:
     text: "Article Title"  # Wait for expected content
   ```

3. **Get accessibility snapshot**
   ```
   Tool: browser_snapshot
   ```
   Output: Structured representation of page content

4. **Extract specific text sections**
   - Parse snapshot output for relevant sections
   - Identify heading hierarchy
   - Extract paragraph content
   - Note any interactive elements

### Text Extraction Notes
- Snapshot returns accessibility tree format
- Elements include type, name, and ref ID
- Text content appears in element labels
- Hidden elements may not appear in snapshot

---

## Protocol 2: Structured Data Extraction

### Purpose
Extract data from tables, lists, or repeated elements.

### Steps

1. **Navigate and load page**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/data-table"
   Tool: browser_wait_for
   Parameters:
     text: "Data"
   ```

2. **Capture page structure**
   ```
   Tool: browser_snapshot
   ```

3. **Identify data patterns**
   - Look for table elements in snapshot
   - Find repeated list items
   - Note element references for iteration

4. **Extract using JavaScript** (for complex structures)
   ```
   Tool: browser_evaluate
   Parameters:
     function: "() => {
       const rows = document.querySelectorAll('table tr');
       return Array.from(rows).map(row => {
         const cells = row.querySelectorAll('td, th');
         return Array.from(cells).map(cell => cell.textContent.trim());
       });
     }"
   ```

### Table Extraction Example

```javascript
// Extract table as array of objects
() => {
  const table = document.querySelector('table');
  const headers = Array.from(table.querySelectorAll('th'))
    .map(th => th.textContent.trim());
  const rows = Array.from(table.querySelectorAll('tbody tr'));
  return rows.map(row => {
    const cells = Array.from(row.querySelectorAll('td'));
    return headers.reduce((obj, header, i) => {
      obj[header] = cells[i]?.textContent.trim() || '';
      return obj;
    }, {});
  });
}
```

---

## Protocol 3: Link Extraction

### Purpose
Extract all links from a page for further crawling or analysis.

### Steps

1. **Navigate to page**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/resources"
   ```

2. **Extract links via JavaScript**
   ```
   Tool: browser_evaluate
   Parameters:
     function: "() => {
       return Array.from(document.querySelectorAll('a[href]'))
         .map(a => ({
           text: a.textContent.trim(),
           href: a.href,
           rel: a.rel || null
         }))
         .filter(link => link.href.startsWith('http'));
     }"
   ```

3. **Filter and categorize**
   - Internal vs external links
   - Navigation vs content links
   - Links by domain
   - Links by type (pdf, doc, etc.)

### Link Filtering Patterns

```javascript
// Get only internal links
() => {
  const baseUrl = window.location.origin;
  return Array.from(document.querySelectorAll('a[href]'))
    .map(a => a.href)
    .filter(href => href.startsWith(baseUrl));
}

// Get only PDF links
() => {
  return Array.from(document.querySelectorAll('a[href$=".pdf"]'))
    .map(a => ({
      text: a.textContent.trim(),
      url: a.href
    }));
}
```

---

## Protocol 4: Form Data Extraction

### Purpose
Extract form field information for analysis or automated filling.

### Steps

1. **Navigate to page with form**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/form"
   ```

2. **Get form structure**
   ```
   Tool: browser_snapshot
   ```
   Look for: textbox, combobox, checkbox, radio elements

3. **Extract detailed form info**
   ```
   Tool: browser_evaluate
   Parameters:
     function: "() => {
       const forms = document.querySelectorAll('form');
       return Array.from(forms).map(form => ({
         action: form.action,
         method: form.method,
         fields: Array.from(form.elements).map(el => ({
           type: el.type,
           name: el.name,
           id: el.id,
           required: el.required,
           placeholder: el.placeholder || null,
           options: el.tagName === 'SELECT'
             ? Array.from(el.options).map(o => o.value)
             : null
         }))
       }));
     }"
   ```

### Form Analysis Output
```json
{
  "action": "/submit",
  "method": "POST",
  "fields": [
    {"type": "text", "name": "username", "required": true},
    {"type": "email", "name": "email", "required": true},
    {"type": "select", "name": "country", "options": ["US", "UK", "CA"]}
  ]
}
```

---

## Protocol 5: API/Network Data Extraction

### Purpose
Capture data from API calls and network requests made by the page.

### Steps

1. **Navigate and trigger data load**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/dashboard"
   Tool: browser_wait_for
   Parameters:
     time: 5  # Wait for API calls to complete
   ```

2. **Get network requests**
   ```
   Tool: browser_network_requests
   ```
   Output: List of all network requests with URLs and methods

3. **Filter for API endpoints**
   - Look for `/api/` paths
   - JSON responses
   - XHR/Fetch requests

4. **Extract API response data**
   ```
   Tool: browser_evaluate
   Parameters:
     function: "async () => {
       const response = await fetch('/api/data');
       return await response.json();
     }"
   ```

### Network Request Filtering
```javascript
// Get only API requests from network log
// (conceptual - actual implementation depends on tool output format)
networkRequests.filter(req =>
  req.url.includes('/api/') &&
  req.method === 'GET'
)
```

---

## Protocol 6: Visual Content Extraction

### Purpose
Capture visual content and screenshots for analysis or archival.

### Steps

1. **Navigate to page**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/gallery"
   ```

2. **Wait for images to load**
   ```
   Tool: browser_wait_for
   Parameters:
     time: 5
   ```

3. **Take full page screenshot**
   ```
   Tool: browser_take_screenshot
   Parameters:
     fullPage: true
     filename: "gallery_capture.png"
   ```

4. **Take element-specific screenshot**
   ```
   Tool: browser_snapshot
   # Find ref for target element

   Tool: browser_take_screenshot
   Parameters:
     ref: "ref_XX"
     element: "Product Image"
     filename: "product_image.png"
   ```

5. **Extract image URLs**
   ```
   Tool: browser_evaluate
   Parameters:
     function: "() => {
       return Array.from(document.querySelectorAll('img'))
         .map(img => ({
           src: img.src,
           alt: img.alt,
           width: img.naturalWidth,
           height: img.naturalHeight
         }));
     }"
   ```

---

## Protocol 7: Dynamic Content Extraction

### Purpose
Extract content from pages that load data dynamically (infinite scroll, lazy loading).

### Steps

1. **Navigate to page**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/feed"
   ```

2. **Initial extraction**
   ```
   Tool: browser_snapshot
   # Record initial content
   ```

3. **Trigger more content loading**
   ```
   # Scroll to bottom
   Tool: browser_evaluate
   Parameters:
     function: "() => window.scrollTo(0, document.body.scrollHeight)"

   # Wait for new content
   Tool: browser_wait_for
   Parameters:
     time: 3
   ```

4. **Extract additional content**
   ```
   Tool: browser_snapshot
   # Record new content
   ```

5. **Repeat until complete or limit reached**

### Infinite Scroll Handling

```javascript
// Scroll and wait pattern
async () => {
  let previousHeight = 0;
  let currentHeight = document.body.scrollHeight;

  while (currentHeight > previousHeight) {
    previousHeight = currentHeight;
    window.scrollTo(0, currentHeight);
    await new Promise(r => setTimeout(r, 2000));
    currentHeight = document.body.scrollHeight;
  }

  return document.body.innerText;
}
```

---

## Protocol 8: Console Log Extraction

### Purpose
Capture console output for debugging or data that's logged to console.

### Steps

1. **Navigate to page**
   ```
   Tool: browser_navigate
   Parameters:
     url: "https://example.com/app"
   ```

2. **Interact to trigger console output**

3. **Get console messages**
   ```
   Tool: browser_console_messages
   Parameters:
     level: "info"  # Or "error", "warning", "debug"
   ```

4. **Filter relevant messages**
   - Look for specific prefixes
   - Filter by level
   - Parse JSON logs if applicable

---

## Data Validation Checklist

After extraction, verify data quality:

- [ ] Data structure matches expected format
- [ ] No missing required fields
- [ ] Dates/numbers in correct format
- [ ] Character encoding correct (no garbled text)
- [ ] Removed unwanted whitespace/formatting
- [ ] Links are absolute (not relative)
- [ ] Data is complete (no pagination issues)

---

## Error Handling

### Empty extraction results

**Causes**:
- Page not fully loaded
- Content in iframe
- Content loaded via JavaScript after snapshot
- Elements hidden or not rendered

**Solutions**:
```
1. Increase wait time
2. Check for iframes: browser_evaluate to access iframe content
3. Trigger scroll/interaction to load content
4. Use JavaScript evaluation for dynamic content
```

### Encoding issues

**Symptoms**: Strange characters, garbled text

**Solutions**:
```javascript
// Normalize text encoding
() => {
  const text = document.body.innerText;
  return text.normalize('NFC');
}
```

### Rate limiting / blocking

**Symptoms**: Empty responses, captcha pages, blocked

**Solutions**:
- Add delays between requests
- Reduce request frequency
- Check robots.txt compliance
- Consider headless detection countermeasures

---

## Best Practices

1. **Respect robots.txt and ToS**
   - Check site policies before scraping
   - Honor rate limits
   - Identify your bot appropriately

2. **Handle pagination properly**
   - Track current page/offset
   - Detect end of data
   - Avoid duplicate extraction

3. **Validate extracted data**
   - Check for expected structure
   - Handle missing fields gracefully
   - Log extraction statistics

4. **Cache when appropriate**
   - Store extracted data locally
   - Avoid re-extracting unchanged content
   - Use timestamps for freshness

5. **Handle errors gracefully**
   - Retry transient failures
   - Log and skip persistent errors
   - Continue with partial results when possible

---

**Last Updated**: 2026-01-13
**Applies To**: Browser MCP for Claude Code CLI on Linux/Ubuntu
