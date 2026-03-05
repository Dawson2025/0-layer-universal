---
resource_id: "3c78b104-7731-457a-8cf1-3bba7acc8d1b"
resource_type: "protocol"
resource_name: "content_extraction_workflow"
---
# Content Extraction Workflow

<!-- section_id: "b7107778-c79c-4ec4-b7ab-ec93516ef703" -->
## Overview

This workflow describes the standardized process for extracting content from web pages using the Claude in Chrome MCP server. Content extraction involves retrieving text, data, and structured information from websites for analysis, archival, or processing purposes.

<!-- section_id: "d5d7a7e7-6b10-4d52-a333-e2d9f6ca5e26" -->
## Use Cases

- Article and blog post extraction
- Data scraping from tables and lists
- Metadata collection
- Product information gathering
- Documentation capture
- Research data collection
- Price and availability checking

<!-- section_id: "81de7ae5-a1c6-4f0b-a795-a3a3caf5f1e6" -->
## Legal and Ethical Considerations

Before extracting content:

1. **Respect robots.txt** - Check if scraping is allowed
2. **Review Terms of Service** - Some sites prohibit automated access
3. **Copyright Compliance** - Do not redistribute copyrighted content
4. **Rate Limiting** - Avoid overwhelming servers with requests
5. **Personal Data** - Be careful with PII extraction (GDPR, CCPA)
6. **No Facial Data** - Never scrape or analyze facial images

<!-- section_id: "a94502a1-837b-4958-a972-82ca700ce780" -->
## Workflow Steps

<!-- section_id: "4b33d1dd-0998-483b-97db-36aa2a93f7ac" -->
### Step 1: Initialize and Navigate

Set up the browser session and navigate to the target page.

```python
# Get tab context
result = mcp__claude-in-chrome__tabs_context_mcp(createIfEmpty=True)
TAB_ID = result.tabs[0].id

# Navigate to target page
mcp__claude-in-chrome__navigate(
    url="https://example.com/article",
    tabId=TAB_ID
)

# Wait for page to load
mcp__claude-in-chrome__computer(
    action="wait",
    duration=3,
    tabId=TAB_ID
)
```

<!-- section_id: "196d16ed-99f5-4684-9435-4eea835d2c2d" -->
### Step 2: Assess Page Structure

Understand what content is available and how it's organized.

```python
# Take screenshot for visual reference
mcp__claude-in-chrome__computer(
    action="screenshot",
    tabId=TAB_ID
)

# Get accessibility tree overview
mcp__claude-in-chrome__read_page(
    tabId=TAB_ID,
    depth=3
)

# Check for main content areas
mcp__claude-in-chrome__find(
    query="main content area",
    tabId=TAB_ID
)

mcp__claude-in-chrome__find(
    query="article body",
    tabId=TAB_ID
)
```

<!-- section_id: "c18b9926-a352-4b1f-be0d-d605f6a0ab47" -->
### Step 3: Extract Text Content

Get the main text content from the page.

```python
# Primary method: get_page_text (prioritizes article content)
mcp__claude-in-chrome__get_page_text(
    tabId=TAB_ID
)
```

This method:
- Extracts readable text
- Prioritizes main content over navigation/ads
- Removes HTML formatting
- Returns clean plain text

<!-- section_id: "5ec22316-0ac1-412a-b902-52ec80ed5a08" -->
### Step 4: Extract Structured Data

Use JavaScript to extract specific data structures.

#### Metadata Extraction

```python
# Get page metadata
mcp__claude-in-chrome__javascript_tool(
    action="javascript_exec",
    text="""({
        title: document.title,
        description: document.querySelector('meta[name="description"]')?.content,
        author: document.querySelector('meta[name="author"]')?.content,
        publishDate: document.querySelector('meta[property="article:published_time"]')?.content,
        modifiedDate: document.querySelector('meta[property="article:modified_time"]')?.content,
        canonical: document.querySelector('link[rel="canonical"]')?.href,
        ogImage: document.querySelector('meta[property="og:image"]')?.content
    })""",
    tabId=TAB_ID
)
```

#### Article Content Extraction

```python
# Extract article structure
mcp__claude-in-chrome__javascript_tool(
    action="javascript_exec",
    text="""({
        title: document.querySelector('h1')?.textContent?.trim(),
        subtitle: document.querySelector('h2')?.textContent?.trim(),
        byline: document.querySelector('.author, .byline, [rel="author"]')?.textContent?.trim(),
        date: document.querySelector('time, .date, .published')?.textContent?.trim(),
        content: document.querySelector('article, .article-body, .post-content, main')?.innerText
    })""",
    tabId=TAB_ID
)
```

#### Table Data Extraction

```python
# Extract table data as JSON
mcp__claude-in-chrome__javascript_tool(
    action="javascript_exec",
    text="""
    (function() {
        const table = document.querySelector('table');
        if (!table) return null;

        const headers = Array.from(table.querySelectorAll('th'))
            .map(th => th.textContent.trim());

        const rows = Array.from(table.querySelectorAll('tbody tr'))
            .map(row => {
                const cells = Array.from(row.querySelectorAll('td'))
                    .map(td => td.textContent.trim());
                return headers.reduce((obj, header, i) => {
                    obj[header] = cells[i];
                    return obj;
                }, {});
            });

        return { headers, rows, rowCount: rows.length };
    })()
    """,
    tabId=TAB_ID
)
```

#### List Extraction

```python
# Extract list items
mcp__claude-in-chrome__javascript_tool(
    action="javascript_exec",
    text="""
    Array.from(document.querySelectorAll('ul.product-list li, ol.items li'))
        .map(li => ({
            text: li.textContent.trim(),
            link: li.querySelector('a')?.href
        }))
    """,
    tabId=TAB_ID
)
```

#### Link Collection

```python
# Get all links from a specific section
mcp__claude-in-chrome__javascript_tool(
    action="javascript_exec",
    text="""
    Array.from(document.querySelectorAll('main a, article a'))
        .filter(a => a.href && !a.href.startsWith('javascript:'))
        .map(a => ({
            text: a.textContent.trim(),
            href: a.href,
            isExternal: !a.href.includes(window.location.hostname)
        }))
    """,
    tabId=TAB_ID
)
```

<!-- section_id: "d3bea981-86ae-422f-b1d8-b4af255aefdb" -->
### Step 5: Handle Pagination

For multi-page content, navigate through pages.

```python
# Check for pagination
mcp__claude-in-chrome__find(
    query="next page button",
    tabId=TAB_ID
)

# Extract current page
content_page_1 = get_page_text(tabId=TAB_ID)

# Navigate to next page
mcp__claude-in-chrome__computer(
    action="left_click",
    ref="ref_next_button",
    tabId=TAB_ID
)

# Wait for page load
mcp__claude-in-chrome__computer(
    action="wait",
    duration=2,
    tabId=TAB_ID
)

# Extract next page
content_page_2 = get_page_text(tabId=TAB_ID)
```

<!-- section_id: "2c21a6c3-9c5d-493f-a6c5-cd59a1e5d5cc" -->
### Step 6: Handle Infinite Scroll

For pages with infinite scroll, load more content before extraction.

```python
# Scroll to load more content
for i in range(5):  # Scroll 5 times
    mcp__claude-in-chrome__computer(
        action="scroll",
        scroll_direction="down",
        scroll_amount=10,
        coordinate=[500, 400],
        tabId=TAB_ID
    )
    mcp__claude-in-chrome__computer(
        action="wait",
        duration=2,  # Wait for content to load
        tabId=TAB_ID
    )

# Now extract all loaded content
mcp__claude-in-chrome__get_page_text(tabId=TAB_ID)
```

<!-- section_id: "77128dc8-ee8b-4173-99f4-3cb1a67b5223" -->
### Step 7: Handle Dynamic Content

For JavaScript-rendered content, ensure it's loaded.

```python
# Check document ready state
mcp__claude-in-chrome__javascript_tool(
    action="javascript_exec",
    text="document.readyState",
    tabId=TAB_ID
)

# Wait for specific element to appear
mcp__claude-in-chrome__javascript_tool(
    action="javascript_exec",
    text="""
    new Promise(resolve => {
        const check = () => {
            if (document.querySelector('.dynamic-content')) {
                resolve(true);
            } else {
                setTimeout(check, 500);
            }
        };
        check();
        setTimeout(() => resolve(false), 10000); // Timeout after 10s
    })
    """,
    tabId=TAB_ID
)
```

<!-- section_id: "c380217a-dbe1-4c4a-abef-b37db9a4b536" -->
## Extraction Patterns

<!-- section_id: "b560e47a-85da-463d-b108-17d276fa7449" -->
### Pattern 1: Article Extraction

Complete workflow for extracting a blog post or news article.

```python
# 1. Navigate and wait
navigate(url="https://example.com/article/123", tabId=TAB_ID)
computer(action="wait", duration=3, tabId=TAB_ID)

# 2. Extract metadata
metadata = javascript_tool(
    action="javascript_exec",
    text="""({
        title: document.querySelector('h1')?.textContent?.trim(),
        author: document.querySelector('[rel="author"], .author')?.textContent?.trim(),
        date: document.querySelector('time')?.getAttribute('datetime'),
        category: document.querySelector('.category, .tag')?.textContent?.trim()
    })""",
    tabId=TAB_ID
)

# 3. Extract main content
content = get_page_text(tabId=TAB_ID)

# 4. Extract images (URLs only - do not scrape actual images)
images = javascript_tool(
    action="javascript_exec",
    text="""
    Array.from(document.querySelectorAll('article img'))
        .map(img => ({
            src: img.src,
            alt: img.alt,
            caption: img.closest('figure')?.querySelector('figcaption')?.textContent
        }))
    """,
    tabId=TAB_ID
)

# Result: { metadata, content, images }
```

<!-- section_id: "367ad4e2-cb10-43d0-8449-d0ae3f15dad7" -->
### Pattern 2: Product Information

Extract product details from e-commerce pages.

```python
# 1. Navigate to product page
navigate(url="https://shop.example.com/product/xyz", tabId=TAB_ID)
computer(action="wait", duration=3, tabId=TAB_ID)

# 2. Extract product data
product = javascript_tool(
    action="javascript_exec",
    text="""({
        name: document.querySelector('h1, .product-title')?.textContent?.trim(),
        price: document.querySelector('.price, [itemprop="price"]')?.textContent?.trim(),
        currency: document.querySelector('[itemprop="priceCurrency"]')?.content,
        availability: document.querySelector('.availability, [itemprop="availability"]')?.textContent?.trim(),
        description: document.querySelector('.description, [itemprop="description"]')?.textContent?.trim(),
        sku: document.querySelector('[itemprop="sku"]')?.content,
        brand: document.querySelector('[itemprop="brand"]')?.textContent?.trim(),
        rating: document.querySelector('.rating, [itemprop="ratingValue"]')?.textContent?.trim(),
        reviewCount: document.querySelector('[itemprop="reviewCount"]')?.textContent?.trim()
    })""",
    tabId=TAB_ID
)

# 3. Extract specifications table
specs = javascript_tool(
    action="javascript_exec",
    text="""
    (function() {
        const specTable = document.querySelector('.specifications, .product-specs');
        if (!specTable) return null;
        const specs = {};
        specTable.querySelectorAll('tr').forEach(row => {
            const label = row.querySelector('th, td:first-child')?.textContent?.trim();
            const value = row.querySelector('td:last-child')?.textContent?.trim();
            if (label && value) specs[label] = value;
        });
        return specs;
    })()
    """,
    tabId=TAB_ID
)
```

<!-- section_id: "e577964c-00f5-457b-b05d-94cda8632f84" -->
### Pattern 3: Search Results

Extract search results from a search engine or site search.

```python
# 1. Navigate to search results
navigate(url="https://example.com/search?q=keyword", tabId=TAB_ID)
computer(action="wait", duration=3, tabId=TAB_ID)

# 2. Extract result count
count = javascript_tool(
    action="javascript_exec",
    text="document.querySelector('.result-count, .search-stats')?.textContent?.trim()",
    tabId=TAB_ID
)

# 3. Extract individual results
results = javascript_tool(
    action="javascript_exec",
    text="""
    Array.from(document.querySelectorAll('.search-result, .result-item'))
        .map(item => ({
            title: item.querySelector('h2, h3, .title')?.textContent?.trim(),
            url: item.querySelector('a')?.href,
            snippet: item.querySelector('.snippet, .description, p')?.textContent?.trim(),
            date: item.querySelector('.date, time')?.textContent?.trim()
        }))
    """,
    tabId=TAB_ID
)
```

<!-- section_id: "7edbc771-5632-4321-84c5-5ce1881a7f74" -->
### Pattern 4: Contact Information

Extract contact details from a contact page.

```python
# Note: Be careful with PII - only extract publicly displayed information

contacts = javascript_tool(
    action="javascript_exec",
    text="""({
        email: document.querySelector('a[href^="mailto:"]')?.href?.replace('mailto:', ''),
        phone: document.querySelector('a[href^="tel:"]')?.href?.replace('tel:', ''),
        address: document.querySelector('address, .address')?.textContent?.trim(),
        socialLinks: Array.from(document.querySelectorAll('a[href*="twitter"], a[href*="linkedin"], a[href*="facebook"]'))
            .map(a => ({ platform: new URL(a.href).hostname, url: a.href }))
    })""",
    tabId=TAB_ID
)
```

<!-- section_id: "92b60197-41d1-4d76-bbd6-075730252747" -->
### Pattern 5: Documentation/Wiki Pages

Extract structured documentation content.

```python
# 1. Get table of contents
toc = javascript_tool(
    action="javascript_exec",
    text="""
    Array.from(document.querySelectorAll('nav.toc a, .table-of-contents a'))
        .map(a => ({
            text: a.textContent.trim(),
            href: a.href,
            level: parseInt(a.closest('li')?.className?.match(/level-(\\d)/)?.[1] || 1)
        }))
    """,
    tabId=TAB_ID
)

# 2. Get main content with structure
content = javascript_tool(
    action="javascript_exec",
    text="""
    (function() {
        const article = document.querySelector('article, .documentation, main');
        if (!article) return null;

        const sections = [];
        let currentSection = null;

        article.querySelectorAll('h1, h2, h3, h4, p, pre, ul, ol').forEach(el => {
            if (el.tagName.match(/^H[1-4]$/)) {
                if (currentSection) sections.push(currentSection);
                currentSection = {
                    heading: el.textContent.trim(),
                    level: parseInt(el.tagName[1]),
                    content: []
                };
            } else if (currentSection) {
                currentSection.content.push({
                    type: el.tagName.toLowerCase(),
                    text: el.textContent.trim()
                });
            }
        });

        if (currentSection) sections.push(currentSection);
        return sections;
    })()
    """,
    tabId=TAB_ID
)
```

<!-- section_id: "2bf7e6a7-719a-4334-a2a7-74264af9f3b5" -->
## Network Request Monitoring

Monitor API calls to understand data sources.

```python
# Start monitoring network requests
# (Note: should be done before navigation for best results)

# Check for API calls after page load
api_calls = mcp__claude-in-chrome__read_network_requests(
    tabId=TAB_ID,
    urlPattern="/api/"
)

# Look at specific endpoints
data_requests = mcp__claude-in-chrome__read_network_requests(
    tabId=TAB_ID,
    urlPattern="products.json"
)
```

<!-- section_id: "e11e6602-c770-401f-9e61-cb86e0530df4" -->
## Error Handling

<!-- section_id: "aa1303ab-2260-46f7-ba51-ac72373417d2" -->
### Content Not Found

```python
# Check if content exists before extraction
result = javascript_tool(
    action="javascript_exec",
    text="!!document.querySelector('article')",
    tabId=TAB_ID
)

if not result:
    # Try alternative selectors
    content = javascript_tool(
        action="javascript_exec",
        text="document.querySelector('main, .content, #content')?.innerText",
        tabId=TAB_ID
    )
```

<!-- section_id: "c15c6308-a78c-40eb-b63d-3e14b5c4211d" -->
### Page Requires Login

```python
# Check for login wall
is_login_required = javascript_tool(
    action="javascript_exec",
    text="!!document.querySelector('.login-wall, .paywall, .signin-required')",
    tabId=TAB_ID
)

if is_login_required:
    # Notify user - cannot proceed without authentication
    pass
```

<!-- section_id: "67e0b603-b6da-4ac2-8247-ab344c988240" -->
### Rate Limiting / Blocking

```python
# Check for rate limit messages
is_blocked = javascript_tool(
    action="javascript_exec",
    text="""
    document.body.innerText.toLowerCase().includes('rate limit') ||
    document.body.innerText.toLowerCase().includes('blocked') ||
    document.body.innerText.toLowerCase().includes('captcha')
    """,
    tabId=TAB_ID
)

if is_blocked:
    # Wait before retrying or notify user
    computer(action="wait", duration=60, tabId=TAB_ID)
```

<!-- section_id: "29682b12-3040-46be-8f6e-9ebc56b3e118" -->
## Output Formats

<!-- section_id: "e1bec70e-b206-4ff4-96be-34c47578079f" -->
### JSON Structure

```json
{
    "url": "https://example.com/article/123",
    "extractedAt": "2026-01-13T10:30:00Z",
    "metadata": {
        "title": "Article Title",
        "author": "John Doe",
        "publishDate": "2026-01-10",
        "category": "Technology"
    },
    "content": {
        "text": "Full article text...",
        "wordCount": 1500,
        "sections": [
            {"heading": "Introduction", "content": "..."},
            {"heading": "Main Topic", "content": "..."}
        ]
    },
    "links": [
        {"text": "Related Article", "href": "https://..."}
    ]
}
```

<!-- section_id: "9d32ded0-cf9a-42b8-b477-c3f0093352ac" -->
### Markdown Output

```python
# Convert extracted content to Markdown
markdown_output = javascript_tool(
    action="javascript_exec",
    text="""
    (function() {
        const article = document.querySelector('article');
        if (!article) return '';

        let md = '';
        article.querySelectorAll('h1,h2,h3,h4,p,ul,ol,pre').forEach(el => {
            switch(el.tagName) {
                case 'H1': md += '# ' + el.textContent.trim() + '\\n\\n'; break;
                case 'H2': md += '## ' + el.textContent.trim() + '\\n\\n'; break;
                case 'H3': md += '### ' + el.textContent.trim() + '\\n\\n'; break;
                case 'H4': md += '#### ' + el.textContent.trim() + '\\n\\n'; break;
                case 'P': md += el.textContent.trim() + '\\n\\n'; break;
                case 'PRE': md += '```\\n' + el.textContent + '\\n```\\n\\n'; break;
                case 'UL':
                case 'OL':
                    el.querySelectorAll('li').forEach(li => {
                        md += '- ' + li.textContent.trim() + '\\n';
                    });
                    md += '\\n';
                    break;
            }
        });
        return md;
    })()
    """,
    tabId=TAB_ID
)
```

<!-- section_id: "a7046e7e-db4e-4106-a77f-406d43124e7c" -->
## Best Practices

1. **Respect website terms** - Check robots.txt and ToS before scraping
2. **Use get_page_text first** - It's optimized for article content
3. **Handle errors gracefully** - Pages may not have expected structure
4. **Add delays between requests** - Avoid overloading servers
5. **Validate extracted data** - Check for empty or malformed results
6. **Cache results when possible** - Reduce redundant requests
7. **Document selectors used** - CSS selectors may change over time
8. **Test with screenshots** - Verify you're extracting the right content
9. **Never extract passwords or financial data** - Security and privacy concern
10. **Store extracted data securely** - Especially if it contains any PII

---

**Related Workflows**:
- [Page Analysis Workflow](./page_analysis_workflow.md)
- [Interactive Browsing Workflow](./interactive_browsing_workflow.md)

**Last Updated**: 2026-01-13
