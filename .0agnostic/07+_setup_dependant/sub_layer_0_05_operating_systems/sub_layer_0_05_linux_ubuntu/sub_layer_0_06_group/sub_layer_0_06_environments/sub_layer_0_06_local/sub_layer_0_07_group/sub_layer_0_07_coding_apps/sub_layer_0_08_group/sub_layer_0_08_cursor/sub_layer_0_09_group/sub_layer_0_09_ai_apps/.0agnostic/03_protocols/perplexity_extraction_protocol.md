---
resource_id: "2271b8cd-0fef-481c-8a3c-c9f40ce51014"
resource_type: "protocol"
resource_name: "perplexity_extraction_protocol"
---
# Perplexity Extraction Protocol

**Scope**: Extracting structured content and citations from Perplexity search pages
**Method**: Claude in Chrome browser automation with React fiber traversal
**Skill**: `/perplexity-extract` (see `.claude/skills/perplexity-extract/SKILL.md`)

## Protocol Steps

### 1. Setup
- Get browser context via `tabs_context_mcp`
- Create fresh tab via `tabs_create_mcp`

### 2. Navigate
- Navigate to Perplexity URL
- Wait 3 seconds for full page load
- Click "Answer" tab if not already active

### 3. Scroll (CRITICAL)
- Scroll incrementally (3 ticks at a time)
- Wait 1 second between scrolls
- Continue until all answer sections have been in viewport
- This forces React to render virtualized citation elements

### 4. Extract Citations (React Fiber)
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

### 5. Supplement from Links Tab
- Click "Links" tab
- Extract `<a href>` elements (these are real anchors, unlike Answer view)
- Click "View More" if present
- Merge with fiber results, deduplicate

### 6. Capture Answer Text
- Switch back to Answer tab
- Use `get_page_text` for full text extraction
- Citation markers appear inline as `domain+N` format

### 7. Output
- Create structured markdown per skill template
- Save to appropriate `.0agnostic/01_knowledge/` directory
- Name: `YYYY-MM-DD_topic-slug.md`

## Known Limitations

| Issue | Workaround |
|-------|-----------|
| Standard DOM queries fail | Use React fiber traversal exclusively |
| Virtualized DOM | Scroll slowly to force rendering |
| Links tab per-answer only | Use fiber method for comprehensive extraction |
| React fiber key varies per load | Always use `.find(k => k.startsWith('__reactFiber'))` |
| YouTube/GitHub citations may vanish | Scroll to those answers right before extraction |
