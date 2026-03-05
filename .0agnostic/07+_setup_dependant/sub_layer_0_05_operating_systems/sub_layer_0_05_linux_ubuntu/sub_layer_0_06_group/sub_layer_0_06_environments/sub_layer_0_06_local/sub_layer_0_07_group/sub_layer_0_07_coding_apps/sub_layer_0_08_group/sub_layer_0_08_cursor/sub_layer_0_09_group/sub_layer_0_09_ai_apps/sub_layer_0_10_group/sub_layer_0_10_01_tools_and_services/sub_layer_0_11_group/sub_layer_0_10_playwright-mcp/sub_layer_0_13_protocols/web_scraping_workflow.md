---
resource_id: "c802e356-534f-490f-a9c8-07c3975f561f"
resource_type: "document"
resource_name: "web_scraping_workflow"
---
# Web Scraping Workflow (Playwright MCP)

## Overview

This protocol defines standard procedures for extracting data from websites using Playwright MCP. Web scraping involves navigating to pages, identifying content, and extracting structured data.

## Prerequisites

1. Playwright MCP server must be running and accessible
2. Target website must be accessible (not blocked/rate-limited)
3. Respect robots.txt and website terms of service

---

## Workflow 1: Basic Page Content Extraction

### Use Case
Extract main text content from a single page (articles, blog posts, documentation).

### Steps

1. **Navigate to target page:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/article")
   ```

2. **Wait for content to load:**
   ```
   mcp__playwright__browser_wait_for(time=2)
   ```

3. **Get accessibility snapshot:**
   ```
   mcp__playwright__browser_snapshot()
   ```
   The snapshot provides structured content with element references.

4. **Extract specific content (optional):**
   If you need to evaluate JavaScript for dynamic content:
   ```
   mcp__playwright__browser_evaluate(
     function="() => document.querySelector('article').innerText"
   )
   ```

### Output
- Structured text content from the accessibility tree
- Element references for further interaction

---

## Workflow 2: Table Data Extraction

### Use Case
Extract tabular data from HTML tables (pricing, specifications, lists).

### Steps

1. **Navigate and wait:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/pricing")
   mcp__playwright__browser_wait_for(time=2)
   ```

2. **Get page snapshot:**
   ```
   mcp__playwright__browser_snapshot()
   ```

3. **Identify table elements:**
   Look for table, row, and cell elements in the snapshot.

4. **Extract table data via JavaScript:**
   ```
   mcp__playwright__browser_evaluate(
     function="() => {
       const table = document.querySelector('table');
       const rows = Array.from(table.querySelectorAll('tr'));
       return rows.map(row => {
         const cells = Array.from(row.querySelectorAll('td, th'));
         return cells.map(cell => cell.innerText.trim());
       });
     }"
   )
   ```

### Best Practices
- Handle header rows separately from data rows
- Account for merged cells (colspan/rowspan)
- Validate data types after extraction

---

## Workflow 3: Multi-Page Scraping (Pagination)

### Use Case
Extract data from multiple pages with pagination (search results, product listings).

### Steps

1. **Navigate to first page:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/products?page=1")
   ```

2. **Extract current page data:**
   ```
   mcp__playwright__browser_snapshot()
   ```

3. **Process and store current page data**

4. **Check for next page:**
   Look for "Next" button or pagination links in snapshot.

5. **Navigate to next page:**
   ```
   mcp__playwright__browser_click(element="Next page button", ref="ref_X")
   ```
   Or navigate directly:
   ```
   mcp__playwright__browser_navigate(url="https://example.com/products?page=2")
   ```

6. **Wait for new content:**
   ```
   mcp__playwright__browser_wait_for(time=2)
   ```

7. **Repeat steps 2-6** until no more pages or limit reached.

### Rate Limiting
- Add delays between page requests: `browser_wait_for(time=2)`
- Monitor for rate limit responses (429 errors)
- Respect website's crawl-delay in robots.txt

---

## Workflow 4: Dynamic Content Scraping (SPA/JavaScript)

### Use Case
Extract data from single-page applications where content loads via JavaScript.

### Steps

1. **Navigate to page:**
   ```
   mcp__playwright__browser_navigate(url="https://spa-example.com/data")
   ```

2. **Wait for specific content to appear:**
   ```
   mcp__playwright__browser_wait_for(text="Loading complete")
   ```
   Or wait for element:
   ```
   mcp__playwright__browser_wait_for(time=5)
   ```

3. **Scroll to trigger lazy loading (if needed):**
   ```
   mcp__playwright__browser_evaluate(
     function="() => window.scrollTo(0, document.body.scrollHeight)"
   )
   mcp__playwright__browser_wait_for(time=2)
   ```

4. **Extract data after full load:**
   ```
   mcp__playwright__browser_snapshot()
   ```

### Handling Infinite Scroll
```
mcp__playwright__browser_evaluate(
  function="() => {
    return new Promise((resolve) => {
      let lastHeight = document.body.scrollHeight;
      const scroll = () => {
        window.scrollTo(0, document.body.scrollHeight);
        setTimeout(() => {
          if (document.body.scrollHeight > lastHeight) {
            lastHeight = document.body.scrollHeight;
            scroll();
          } else {
            resolve(document.body.innerHTML.length);
          }
        }, 1000);
      };
      scroll();
    });
  }"
)
```

---

## Workflow 5: Form-Based Search Scraping

### Use Case
Search for specific data using website search functionality.

### Steps

1. **Navigate to search page:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/search")
   ```

2. **Get page snapshot to find search form:**
   ```
   mcp__playwright__browser_snapshot()
   ```

3. **Fill search field:**
   ```
   mcp__playwright__browser_type(
     element="Search input",
     ref="ref_search",
     text="search query"
   )
   ```

4. **Submit search:**
   ```
   mcp__playwright__browser_click(element="Search button", ref="ref_submit")
   ```
   Or press Enter:
   ```
   mcp__playwright__browser_press_key(key="Enter")
   ```

5. **Wait for results:**
   ```
   mcp__playwright__browser_wait_for(text="results found")
   ```

6. **Extract search results:**
   ```
   mcp__playwright__browser_snapshot()
   ```

---

## Workflow 6: Network Request Monitoring

### Use Case
Capture API responses that contain data (useful when data comes from AJAX calls).

### Steps

1. **Navigate to page:**
   ```
   mcp__playwright__browser_navigate(url="https://example.com/dashboard")
   ```

2. **Wait for requests to complete:**
   ```
   mcp__playwright__browser_wait_for(time=3)
   ```

3. **Get network requests:**
   ```
   mcp__playwright__browser_network_requests()
   ```

4. **Filter for API endpoints:**
   Look for XHR/Fetch requests to API endpoints in the results.

5. **Extract data from relevant requests:**
   The network requests include response bodies for JSON APIs.

---

## Data Extraction Patterns

### Common Element Selectors (via JavaScript)

| Data Type | JavaScript Selector |
|-----------|-------------------|
| Page title | `document.title` |
| Main heading | `document.querySelector('h1').innerText` |
| All links | `Array.from(document.querySelectorAll('a')).map(a => ({text: a.innerText, href: a.href}))` |
| Images | `Array.from(document.querySelectorAll('img')).map(img => ({alt: img.alt, src: img.src}))` |
| Prices | `Array.from(document.querySelectorAll('[class*="price"]')).map(el => el.innerText)` |
| List items | `Array.from(document.querySelectorAll('li')).map(li => li.innerText)` |

### Using Accessibility Snapshot

The `browser_snapshot()` output provides:
- Text content with semantic structure
- Interactive element references (ref_1, ref_2, etc.)
- Form field values
- Button and link labels

---

## Error Handling

### Page Load Failures
```
# Check network requests for errors
mcp__playwright__browser_network_requests()

# Take screenshot for debugging
mcp__playwright__browser_take_screenshot()
```

### Content Not Found
1. Verify page loaded completely
2. Check if content is in iframe (may need to switch context)
3. Verify content is not behind authentication

### Rate Limiting (429 Errors)
1. Add longer delays between requests
2. Implement exponential backoff
3. Consider rotating user agents (via config)

---

## Best Practices

1. **Respect robots.txt**: Check allowed paths before scraping
2. **Rate limiting**: Add delays between requests (2-5 seconds minimum)
3. **User-Agent**: Use realistic user agent strings
4. **Error handling**: Always have fallback for failed extractions
5. **Data validation**: Verify extracted data structure matches expectations
6. **Caching**: Avoid re-scraping same content unnecessarily
7. **Legal compliance**: Ensure scraping complies with website ToS

---

## Example: Complete Product Scraping

```
# 1. Navigate to product page
mcp__playwright__browser_navigate(url="https://shop.example.com/product/123")

# 2. Wait for page load
mcp__playwright__browser_wait_for(time=2)

# 3. Get structured content
mcp__playwright__browser_snapshot()

# 4. Extract specific data
mcp__playwright__browser_evaluate(
  function="() => ({
    title: document.querySelector('h1').innerText,
    price: document.querySelector('.price').innerText,
    description: document.querySelector('.description').innerText,
    images: Array.from(document.querySelectorAll('.product-image')).map(img => img.src),
    specs: Array.from(document.querySelectorAll('.spec-row')).map(row => ({
      name: row.querySelector('.spec-name').innerText,
      value: row.querySelector('.spec-value').innerText
    }))
  })"
)

# 5. Take screenshot for reference
mcp__playwright__browser_take_screenshot(filename="product-123.png")

# 6. Close browser when done
mcp__playwright__browser_close()
```

---

**Last Updated**: 2026-01-13
**Applies To**: Playwright MCP Server for Claude Code CLI
