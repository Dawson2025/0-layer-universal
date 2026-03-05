---
resource_id: "c802e356-534f-490f-a9c8-07c3975f561f"
resource_type: "document"
resource_name: "web_scraping_workflow"
---
# Web Scraping Workflow (Playwright MCP)

<!-- section_id: "79dfce19-3e6b-4e93-b51d-b9aaebf399be" -->
## Overview

This protocol defines standard procedures for extracting data from websites using Playwright MCP. Web scraping involves navigating to pages, identifying content, and extracting structured data.

<!-- section_id: "96722ed8-9b5b-4771-8f19-14c730c61eb9" -->
## Prerequisites

1. Playwright MCP server must be running and accessible
2. Target website must be accessible (not blocked/rate-limited)
3. Respect robots.txt and website terms of service

---

<!-- section_id: "22f4fd11-f0f2-44da-99d8-18f51c5c9c9f" -->
## Workflow 1: Basic Page Content Extraction

<!-- section_id: "cc75091d-287a-4cac-88cb-7439ffae6847" -->
### Use Case
Extract main text content from a single page (articles, blog posts, documentation).

<!-- section_id: "13f44c19-bb05-46dc-8c2d-c1016d34acf7" -->
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

<!-- section_id: "b73b5b64-ca69-4c02-86bf-1355aed5c3b5" -->
### Output
- Structured text content from the accessibility tree
- Element references for further interaction

---

<!-- section_id: "1894cd77-8493-4b3b-a7a2-9576308328ce" -->
## Workflow 2: Table Data Extraction

<!-- section_id: "373b433d-4a66-4748-8ede-91b84e189bc8" -->
### Use Case
Extract tabular data from HTML tables (pricing, specifications, lists).

<!-- section_id: "af408f2c-c691-4129-90ed-39be086fb3b2" -->
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

<!-- section_id: "78cb2162-e1ba-42f9-b260-388a6b730782" -->
### Best Practices
- Handle header rows separately from data rows
- Account for merged cells (colspan/rowspan)
- Validate data types after extraction

---

<!-- section_id: "db970ad7-7ce7-496d-b7f0-9d4c4d1a31c4" -->
## Workflow 3: Multi-Page Scraping (Pagination)

<!-- section_id: "a401d16d-8940-4b2a-b724-5699ad4959a7" -->
### Use Case
Extract data from multiple pages with pagination (search results, product listings).

<!-- section_id: "571edcd0-da83-499e-81db-ebce8536023c" -->
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

<!-- section_id: "7e910a4a-fe42-4e83-88c1-f6ce0cf4f354" -->
### Rate Limiting
- Add delays between page requests: `browser_wait_for(time=2)`
- Monitor for rate limit responses (429 errors)
- Respect website's crawl-delay in robots.txt

---

<!-- section_id: "5ccd19d5-6ae7-44e4-9e78-f43b18f45b1b" -->
## Workflow 4: Dynamic Content Scraping (SPA/JavaScript)

<!-- section_id: "b290c042-c3b2-4c59-8a60-22619f6c4da3" -->
### Use Case
Extract data from single-page applications where content loads via JavaScript.

<!-- section_id: "83f48856-548b-480d-8bda-e560e799c75b" -->
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

<!-- section_id: "86684259-2eaa-4a20-a6aa-7593eb78d72a" -->
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

<!-- section_id: "b5e9bf47-6b53-4cde-b5d5-e9fabf10dba2" -->
## Workflow 5: Form-Based Search Scraping

<!-- section_id: "8b737922-9009-4a38-8022-8720101ba3c4" -->
### Use Case
Search for specific data using website search functionality.

<!-- section_id: "f7f9ea97-df79-49e1-951c-98b0cd817f42" -->
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

<!-- section_id: "21d6be7e-0794-480d-9496-32c523b82230" -->
## Workflow 6: Network Request Monitoring

<!-- section_id: "a90ac998-4fbf-408c-8ab9-69ffb6b0b692" -->
### Use Case
Capture API responses that contain data (useful when data comes from AJAX calls).

<!-- section_id: "13802a8a-0423-439f-b185-dfa87ee0a5c6" -->
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

<!-- section_id: "da894633-3cff-4aa9-867a-e6575c774641" -->
## Data Extraction Patterns

<!-- section_id: "56f75ea0-41ed-48f6-b5c2-b10b2de7f68f" -->
### Common Element Selectors (via JavaScript)

| Data Type | JavaScript Selector |
|-----------|-------------------|
| Page title | `document.title` |
| Main heading | `document.querySelector('h1').innerText` |
| All links | `Array.from(document.querySelectorAll('a')).map(a => ({text: a.innerText, href: a.href}))` |
| Images | `Array.from(document.querySelectorAll('img')).map(img => ({alt: img.alt, src: img.src}))` |
| Prices | `Array.from(document.querySelectorAll('[class*="price"]')).map(el => el.innerText)` |
| List items | `Array.from(document.querySelectorAll('li')).map(li => li.innerText)` |

<!-- section_id: "86fa6aec-90e7-40bd-8931-3ffc4942f8d5" -->
### Using Accessibility Snapshot

The `browser_snapshot()` output provides:
- Text content with semantic structure
- Interactive element references (ref_1, ref_2, etc.)
- Form field values
- Button and link labels

---

<!-- section_id: "461e5655-8931-4999-8299-354940e10248" -->
## Error Handling

<!-- section_id: "d7e0b0c1-f140-4873-8ae0-0844dbf1d2f0" -->
### Page Load Failures
```
# Check network requests for errors
mcp__playwright__browser_network_requests()

# Take screenshot for debugging
mcp__playwright__browser_take_screenshot()
```

<!-- section_id: "8d6c19fd-8bc5-455c-b3c5-a64c383bcbdc" -->
### Content Not Found
1. Verify page loaded completely
2. Check if content is in iframe (may need to switch context)
3. Verify content is not behind authentication

<!-- section_id: "451f8724-3fed-441b-b448-56a509357c00" -->
### Rate Limiting (429 Errors)
1. Add longer delays between requests
2. Implement exponential backoff
3. Consider rotating user agents (via config)

---

<!-- section_id: "6fe1be5d-541b-477f-910a-7e5f6b9f842e" -->
## Best Practices

1. **Respect robots.txt**: Check allowed paths before scraping
2. **Rate limiting**: Add delays between requests (2-5 seconds minimum)
3. **User-Agent**: Use realistic user agent strings
4. **Error handling**: Always have fallback for failed extractions
5. **Data validation**: Verify extracted data structure matches expectations
6. **Caching**: Avoid re-scraping same content unnecessarily
7. **Legal compliance**: Ensure scraping complies with website ToS

---

<!-- section_id: "fe18891b-cbb8-46a1-a74c-8ffab0c8ea45" -->
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
