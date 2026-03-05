---
resource_id: "c9874be5-fff4-4473-9a44-920488c8868e"
resource_type: "knowledge"
resource_name: "react_fiber_extraction"
---
# React Fiber Extraction Method — Perplexity

<!-- section_id: "88f4a5af-4636-47f9-9720-6c54180d8c3c" -->
## Why React Fiber?

Perplexity renders citation links via React components, NOT standard HTML anchors. Running `document.querySelectorAll('a[href]')` returns nearly zero external URLs because:
- Citation elements are `<span>` tags, not `<a>` tags
- URLs are stored in React component props, not DOM attributes
- The rendered DOM has no `href` attributes on citations

<!-- section_id: "ed665ec6-0ea2-4ad1-9e8e-3bb7255585f7" -->
## Extraction Path

```
span.citation.inline-flex
  → element.__reactFiber$*
    → memoizedProps.children.props
      → { url, href, domain, source, overflowCount, linkBehavior }
```

<!-- section_id: "269a3fe8-b312-4aeb-baf9-9e3bb6ed5f18" -->
## JavaScript Extraction Code

```javascript
const citations = document.querySelectorAll('span.citation.inline-flex');
const seen = new Set();
const results = [];
citations.forEach(cit => {
  const fiberKey = Object.keys(cit).find(k => k.startsWith('__reactFiber'));
  if (!fiberKey) return;
  const fiber = cit[fiberKey];
  const childProps = fiber.memoizedProps?.children?.props;
  if (!childProps) return;
  const url = childProps.url || childProps.href || '';
  const domain = childProps.domain || '';
  const label = cit.textContent.trim();
  if (url && !seen.has(url)) {
    seen.add(url);
    results.push({ label, domain, url });
  }
});
JSON.stringify(results, null, 2);
```

<!-- section_id: "c9134923-638c-4734-95cb-692db6263260" -->
## Key Properties in `children.props`

| Property | Description |
|----------|-------------|
| `url` | Full URL of the citation source |
| `href` | Alternative URL field (fallback) |
| `domain` | Display domain (e.g., "arxiv.org") |
| `source` | Source metadata object |
| `overflowCount` | Number of additional grouped citations |
| `linkBehavior` | How the link opens (new tab, etc.) |

<!-- section_id: "f7dd993d-046f-4d02-a049-46e6cbc4bffc" -->
## React Virtualization Caveat

Perplexity uses React virtualization — DOM elements for out-of-viewport answers are unloaded. Before extraction:
1. Scroll slowly through ALL answers (3 scroll ticks, 1-second pause between)
2. YouTube and GitHub citations are especially prone to disappearing when scrolled past
3. The "Links" tab only shows sources for the currently active answer

<!-- section_id: "ea706b8a-65a0-4527-bfea-222e09b6bcf1" -->
## Proven Results

- Test extraction (2026-02-22): 21 citation elements found, 18 unique URLs extracted
- Standard DOM query comparison: `document.querySelectorAll('a[href]')` returned ~0 external links
- React fiber method: 100% citation URL recovery rate for rendered citations

<!-- section_id: "3dd53854-2cbd-4b92-bff1-9fed2f65ce97" -->
## Tool Dependency

This method requires **Claude in Chrome MCP server** — specifically the `javascript_tool` for executing React fiber traversal in the page context.
