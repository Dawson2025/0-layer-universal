---
resource_id: "608d5164-dfe2-4f5b-a92a-d15913c8905e"
resource_type: "document"
resource_name: "data_extraction_workflow"
---
# Data Extraction Workflow (Browser MCP)

<!-- section_id: "eb69ba00-c9d3-415b-be24-5cfec6965971" -->
## Overview

This protocol defines standard procedures for extracting content and data from web pages using Browser MCP tools. Data extraction workflows are essential for web scraping, research, and content analysis tasks.

<!-- section_id: "decd6c44-032f-44f0-99e6-c71787bbeef4" -->
## Prerequisites

1. Browser MCP server running and accessible
2. Target page accessible and loaded
3. Understanding of page structure (DOM elements, accessibility tree)
4. Awareness of site's terms of service regarding scraping

<!-- section_id: "3e3e63d3-ca61-47eb-96bc-49e84d43f3ce" -->
## Extraction Methods Overview

| Method | Tool | Best For |
|--------|------|----------|
| Accessibility Snapshot | `browser_snapshot` | Structured page content, interactive elements |
| Page Text | `get_page_text` | Article content, raw text extraction |
| JavaScript Evaluation | `browser_evaluate` | Custom data extraction, complex queries |
| Screenshot | `browser_take_screenshot` | Visual content, image capture |
| Network Requests | `browser_network_requests` | API responses, data endpoints |

---

<!-- section_id: "d9adaab5-a354-4f07-ba89-0cc3e40ab8ed" -->
## Protocol 1: Basic Text Extraction

<!-- section_id: "851851bd-35e6-4c4d-b317-08e35aa15020" -->
### Purpose
Extract readable text content from a web page.

<!-- section_id: "d5180482-b14f-473e-a291-bc7ae7d612dc" -->
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

<!-- section_id: "a684576c-b2aa-4997-a484-dc93ac9cbf16" -->
### Text Extraction Notes
- Snapshot returns accessibility tree format
- Elements include type, name, and ref ID
- Text content appears in element labels
- Hidden elements may not appear in snapshot

---

<!-- section_id: "d268443d-61aa-4b31-bbcc-871cddab2cda" -->
## Protocol 2: Structured Data Extraction

<!-- section_id: "11d99c70-1819-49d2-a6d7-88a67b10b5c3" -->
### Purpose
Extract data from tables, lists, or repeated elements.

<!-- section_id: "0954bb83-e4fb-4f56-8875-6495f2347a50" -->
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

<!-- section_id: "306ed763-8458-49a1-b23d-21208e411b2e" -->
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

<!-- section_id: "dc61bd6a-96a6-492e-ba7f-b02802d979c8" -->
## Protocol 3: Link Extraction

<!-- section_id: "d38d240f-de54-4fd5-b479-47f1b0e889ee" -->
### Purpose
Extract all links from a page for further crawling or analysis.

<!-- section_id: "6c7362c0-7c7d-4f23-a91b-eda291762328" -->
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

<!-- section_id: "5687d155-ba95-4f04-988d-528794cfafaf" -->
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

<!-- section_id: "4e88fa8d-392e-499b-8858-82ca27bb2752" -->
## Protocol 4: Form Data Extraction

<!-- section_id: "1cc36b9e-9121-420f-9405-cdc464817749" -->
### Purpose
Extract form field information for analysis or automated filling.

<!-- section_id: "d76c0589-b6fa-4b39-90fe-399d81799f05" -->
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

<!-- section_id: "c95a6b2a-d65f-49a5-9eac-157fd9ae8977" -->
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

<!-- section_id: "01b258de-815e-4b0b-a024-0433ce973651" -->
## Protocol 5: API/Network Data Extraction

<!-- section_id: "48b53959-4203-4ec2-9dba-9b543d839b09" -->
### Purpose
Capture data from API calls and network requests made by the page.

<!-- section_id: "b11c8986-f703-4f77-a390-0865f788b731" -->
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

<!-- section_id: "96d29e4e-b302-4c6b-a127-17e428df8d1f" -->
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

<!-- section_id: "229a658c-d3a0-4e2e-a187-38d4642b2e97" -->
## Protocol 6: Visual Content Extraction

<!-- section_id: "f8a96df0-9ff3-415c-8b74-52a859e3126b" -->
### Purpose
Capture visual content and screenshots for analysis or archival.

<!-- section_id: "60d7cfd7-f81a-494c-ba57-481763cfe252" -->
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

<!-- section_id: "95cc3d7b-b6a6-4208-9b1a-77ad862b21d1" -->
## Protocol 7: Dynamic Content Extraction

<!-- section_id: "5c516ce8-49b8-4062-ac8e-da1fb5e3043f" -->
### Purpose
Extract content from pages that load data dynamically (infinite scroll, lazy loading).

<!-- section_id: "971b1359-e887-4c2f-8f8e-cf645e09e779" -->
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

<!-- section_id: "2b13e2c3-9bec-4a52-bbc6-1384bf9ac347" -->
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

<!-- section_id: "1cb603b5-fcc3-428b-b2a7-8c293db46e02" -->
## Protocol 8: Console Log Extraction

<!-- section_id: "e21e9a7b-2361-4bd0-a5b1-a4b3ce0996ca" -->
### Purpose
Capture console output for debugging or data that's logged to console.

<!-- section_id: "29272887-8270-47a9-a2cc-75f1feed7fa6" -->
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

<!-- section_id: "64a25eed-b0d7-460e-89a3-d8ce54186a4b" -->
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

<!-- section_id: "9a86a090-b976-464e-9301-65e2baec8f79" -->
## Error Handling

<!-- section_id: "a28128c0-95e8-4cb3-8112-d1d15b2dd0a5" -->
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

<!-- section_id: "1f7495d6-ed63-44c6-806c-0bae28d9a381" -->
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

<!-- section_id: "19ceb2c9-7a91-4a4c-a137-76aabca593e5" -->
### Rate limiting / blocking

**Symptoms**: Empty responses, captcha pages, blocked

**Solutions**:
- Add delays between requests
- Reduce request frequency
- Check robots.txt compliance
- Consider headless detection countermeasures

---

<!-- section_id: "0276fe30-1fbd-448c-962e-af568ee53872" -->
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
