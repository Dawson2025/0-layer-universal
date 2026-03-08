---
resource_id: "be6caf0c-c399-409b-abb7-4cf4c19608bd"
resource_type: "skill_document"
resource_name: "SKILL"
name: perplexity-extract
description: "Extract structured content and citation source URLs from Perplexity search pages using Claude in Chrome browser automation. Navigates to Perplexity, scrolls to render virtualized content, extracts citations via React fiber traversal, and outputs structured markdown with all source links preserved."
---

# Perplexity Extract Skill

<!-- section_id: "e3ede2d1-eece-49fe-a87d-113826e7fbfd" -->
## WHEN to Use
- User provides a Perplexity search URL (`perplexity.ai/search/*`)
- User wants to extract research findings with preserved source/citation links
- Building a knowledge base from Perplexity research threads
- Need to capture a multi-turn Perplexity conversation with full citations

<!-- section_id: "7f178059-b625-44a9-b440-9da22d1af7b1" -->
## WHEN NOT to Use
- URL is not a Perplexity search page
- User just wants to read a simple web page (use WebFetch instead)
- User wants to make a NEW Perplexity query (use the Perplexity MCP server instead)
- Content is behind authentication

<!-- section_id: "2237442e-5e37-4e36-bbc9-0024dfad9029" -->
## Prerequisites
- Claude in Chrome MCP server must be active and responding
- A browser tab available for automation (create one with `tabs_create_mcp`)

<!-- section_id: "b32ea073-ba10-4278-912f-3ddc4974e31e" -->
## Protocol

<!-- section_id: "663b65f5-71ab-4b0e-a0fd-646fd741ad12" -->
### Step 1: Get Browser Context
```
mcp__claude-in-chrome__tabs_context_mcp
mcp__claude-in-chrome__tabs_create_mcp   # Create a fresh tab
```

<!-- section_id: "5a082e1a-bfee-49af-84a3-f343179b4f65" -->
### Step 2: Navigate to Perplexity URL
```
mcp__claude-in-chrome__navigate(url=<perplexity_url>, tabId=<tab>)
```
Wait 3 seconds for the page to fully load.

<!-- section_id: "7a6dd90c-474e-4e38-a163-2b3e4dbad823" -->
### Step 3: Switch to Answer View
Click the "Answer" tab if not already active. The Answer view contains all conversation turns with inline citations.

<!-- section_id: "b6f4f1ad-a8ff-4c61-b353-6da27159effa" -->
### Step 4: Scroll Through All Answers
**CRITICAL**: Perplexity uses React virtualization — elements NOT in viewport may NOT be in DOM. You MUST scroll slowly through each answer section to force React to render citation elements.

- Scroll down incrementally (3 ticks at a time)
- Wait 1 second between scrolls
- Continue until you've reached all answer sections

<!-- section_id: "d70edfb7-095b-45c5-99b0-bf627955fded" -->
### Step 5: Extract Citations via React Fiber

**This is the ONLY reliable extraction method.** Standard `document.querySelectorAll('a[href]')` returns almost nothing on Perplexity.

Execute this JavaScript via `mcp__claude-in-chrome__javascript_tool`:

```javascript
// Extract ALL citation URLs from React fiber props
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

**Key props available on citation children**: `domain`, `url`, `href`, `source`, `overflowCount`, `linkBehavior`

<!-- section_id: "1330792a-3496-4104-ba83-af98ae102c27" -->
### Step 6: Check the "Links" Tab (Supplementary)

The "Links" tab exposes source cards as real `<a href>` elements, but ONLY for the currently active/last answer. Click the "Links" tab and extract URLs:

```javascript
const allLinks = document.querySelectorAll('a[href]');
const hrefs = [];
allLinks.forEach(a => {
  const href = a.getAttribute('href');
  if (href && href.startsWith('http') && !href.includes('perplexity.ai') && !hrefs.includes(href)) {
    hrefs.push(href);
  }
});
JSON.stringify(hrefs);
```

Check for a "View More" button and click it to expand additional sources.

Combine these with the React fiber results and deduplicate.

<!-- section_id: "ef07ce85-9eb6-4db0-8c29-0ec8fbbd06b7" -->
### Step 7: Capture Answer Text

Switch back to the Answer tab, then:
```
mcp__claude-in-chrome__get_page_text(tabId=<tab>)
```

This returns the full text of all answers, though citation markers appear as inline text (e.g., `ubuntu+3`, `gnome+2`).

<!-- section_id: "510d7d43-8205-4882-9e43-959d42c44247" -->
### Step 8: Output Structured Markdown

Create a markdown file with this structure:

```markdown
# Perplexity Extraction: <Topic>

**Source**: <perplexity_url>
**Extracted**: <YYYY-MM-DD>
**Method**: Claude in Chrome (React fiber citation extraction)

---

## Thread Summary
<2-3 sentence summary of the conversation>

---

## Answer 1: <Title>
<Content summary — do NOT reproduce copyrighted text verbatim>

## Answer 2: <Title>
<Content summary>

[... for each answer in the thread]

---

## All Citation Sources (<N> unique URLs)

### <Category 1>
1. [<Title>](<URL>)
2. [<Title>](<URL>)

### <Category 2>
...

### Not Captured from DOM
- <Any citations referenced in text but not found in React fiber, with explanation>

---

## Extraction Method Notes
- **What worked**: <brief notes>
- **Limitations**: <any issues encountered>
```

<!-- section_id: "d19e428e-accc-426c-98ff-d4d06b3de273" -->
### Step 9: Save to Trajectory Store

Save the output file to the trajectory store:
- **Location**: The appropriate `.0agnostic/01_knowledge/perplexity_extractions/` directory
- **Naming**: `YYYY-MM-DD_<topic-slug>.md`

<!-- section_id: "e419cfb7-20c8-4e68-baf1-d5518e824161" -->
## Known Limitations

| Issue | Detail |
|-------|--------|
| Standard DOM queries fail | `document.querySelectorAll('a[href]')` returns nearly nothing — Perplexity barely uses real `<a>` tags in Answer view |
| React virtualization | Earlier answers' DOM gets unloaded when scrolled past — YouTube/GitHub citations may disappear |
| Links tab is per-answer | The "Links" tab only shows sources for the currently selected/last answer, not all answers |
| React fiber key varies | The `__reactFiber$` suffix changes per page load (e.g., `__reactFiber$aj3ehc5uz3i`) — always use `.find(k => k.startsWith('__reactFiber'))` |
| Citation label != full URL | Labels like `ubuntu+3` mean "ubuntu domain, 3 more related sources" — extract the actual URL from fiber props |

<!-- section_id: "7a7f6581-866f-4b98-8440-4ea773f040d8" -->
## References

| Resource | Purpose |
|----------|---------|
| Test extraction output | `layer_-1_research/layer_-1_better_ai_system/perplexity_extraction_2026-02-22_tts-research.md` |
| Claude in Chrome docs | MCP server tools: `tabs_context_mcp`, `navigate`, `javascript_tool`, `get_page_text` |

<!-- section_id: "32097eb7-666c-48ac-a152-9ce0bbc0f89d" -->
## AALang Reference

This skill can be registered as avenue 05 (skills) in any entity's `.0agnostic/06_context_avenue_web/01_file_based/05_skills/`.
