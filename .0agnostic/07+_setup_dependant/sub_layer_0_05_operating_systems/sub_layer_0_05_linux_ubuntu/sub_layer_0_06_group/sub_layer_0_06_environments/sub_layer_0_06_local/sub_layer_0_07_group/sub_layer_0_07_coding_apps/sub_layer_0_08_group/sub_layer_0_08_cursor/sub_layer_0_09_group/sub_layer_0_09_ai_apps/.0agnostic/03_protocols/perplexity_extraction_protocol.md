---
resource_id: "2271b8cd-0fef-481c-8a3c-c9f40ce51014"
resource_type: "protocol"
resource_name: "perplexity_extraction_protocol"
---
# Perplexity Extraction Protocol

**Scope**: Extracting structured content and citations from Perplexity search pages
**Method**: Claude in Chrome browser automation with React fiber traversal
**Skill**: `/perplexity-extract` (see `.claude/skills/perplexity-extract/SKILL.md`)

<!-- section_id: "37125672-2a17-411a-ac95-68e606cffc10" -->
## Protocol Steps

<!-- section_id: "34f8bc58-e957-494e-8b32-832d10ecdc2a" -->
### 1. Setup
- Get browser context via `tabs_context_mcp`
- Create fresh tab via `tabs_create_mcp`

<!-- section_id: "cf258d0c-3970-4d0c-83c0-87fe7095c6e2" -->
### 2. Navigate
- Navigate to Perplexity URL
- Wait 3 seconds for full page load
- Click "Answer" tab if not already active

<!-- section_id: "2b83d8e7-7a98-4e66-9cfe-6bceb8673445" -->
### 3. Scroll (CRITICAL)
- Scroll incrementally (3 ticks at a time)
- Wait 1 second between scrolls
- Continue until all answer sections have been in viewport
- This forces React to render virtualized citation elements

<!-- section_id: "3b36a634-2812-4bb6-9f0b-750475d89a4d" -->
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

<!-- section_id: "a272d098-0472-41c0-917b-b2b3e2b9718f" -->
### 5. Supplement from Links Tab
- Click "Links" tab
- Extract `<a href>` elements (these are real anchors, unlike Answer view)
- Click "View More" if present
- Merge with fiber results, deduplicate

<!-- section_id: "7eb2e883-909c-4bd8-a9e7-487317317c42" -->
### 6. Capture Answer Text
- Switch back to Answer tab
- Use `get_page_text` for full text extraction
- Citation markers appear inline as `domain+N` format

<!-- section_id: "1a9266ad-0854-49d4-bffe-4ee16839c6d8" -->
### 7. Output
- Create structured markdown per skill template
- Save to appropriate `.0agnostic/01_knowledge/` directory
- Name: `YYYY-MM-DD_topic-slug.md`

<!-- section_id: "3e03edb1-96a9-4f2a-aa45-a20c3724843b" -->
## Known Limitations

| Issue | Workaround |
|-------|-----------|
| Standard DOM queries fail | Use React fiber traversal exclusively |
| Virtualized DOM | Scroll slowly to force rendering |
| Links tab per-answer only | Use fiber method for comprehensive extraction |
| React fiber key varies per load | Always use `.find(k => k.startsWith('__reactFiber'))` |
| YouTube/GitHub citations may vanish | Scroll to those answers right before extraction |
