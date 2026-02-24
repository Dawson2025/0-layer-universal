# Perplexity Page Extraction Rules

**Scope**: All AI apps that extract content from Perplexity search pages
**Importance**: I1 (High)

## Rules

### R1: React Fiber is the ONLY Reliable Extraction Method

Standard DOM queries (`document.querySelectorAll('a[href]')`) return almost nothing on Perplexity pages. The ONLY working method is React fiber traversal:

```
span.citation.inline-flex → __reactFiber$* → memoizedProps.children.props → url/href/domain
```

**MUST NOT** rely on standard anchor tags, data attributes, or accessibility tree for citation URLs.

### R2: Scroll Before Extracting

Perplexity uses React virtualization. Citation elements NOT in viewport may NOT exist in DOM. **MUST** scroll slowly through each answer section (3 ticks, 1s pause) before running extraction.

### R3: Citation Label != URL

Citation labels like `ubuntu+3` mean "ubuntu domain, 3 more related sources". Always extract the actual URL from fiber `memoizedProps.children.props.url`, never try to reconstruct from labels.

### R4: Links Tab is Per-Answer Only

The "Links" tab shows sources ONLY for the currently active/last answer. Use it as supplementary to React fiber extraction, not as primary source.

### R5: Preserve All Source URLs

Every extraction output MUST include a complete deduplicated citation list with full URLs. Missing citations must be documented in a "Not Captured" section with explanation.

### R6: Output Format

Extraction outputs follow the template in `/perplexity-extract` skill: metadata header, per-answer summaries (not verbatim), categorized citation URLs.
