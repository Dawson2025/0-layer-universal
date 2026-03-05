---
resource_id: "274a6804-044b-4b55-9bc0-2db4b8f6e5bf"
resource_type: "rule"
resource_name: "perplexity_extraction_rules"
---
# Perplexity Page Extraction Rules

**Scope**: All AI apps that extract content from Perplexity search pages
**Importance**: I1 (High)

<!-- section_id: "7c71e2cc-ce80-48a3-b912-27f83326015d" -->
## Rules

<!-- section_id: "67f11f59-7c7e-4de3-af4b-3708945235d8" -->
### R1: React Fiber is the ONLY Reliable Extraction Method

Standard DOM queries (`document.querySelectorAll('a[href]')`) return almost nothing on Perplexity pages. The ONLY working method is React fiber traversal:

```
span.citation.inline-flex → __reactFiber$* → memoizedProps.children.props → url/href/domain
```

**MUST NOT** rely on standard anchor tags, data attributes, or accessibility tree for citation URLs.

<!-- section_id: "7ef9f67c-2879-4407-8f2e-3f3cedf73ee7" -->
### R2: Scroll Before Extracting

Perplexity uses React virtualization. Citation elements NOT in viewport may NOT exist in DOM. **MUST** scroll slowly through each answer section (3 ticks, 1s pause) before running extraction.

<!-- section_id: "dbb31000-a7ce-47ae-8495-18886f4bdcd6" -->
### R3: Citation Label != URL

Citation labels like `ubuntu+3` mean "ubuntu domain, 3 more related sources". Always extract the actual URL from fiber `memoizedProps.children.props.url`, never try to reconstruct from labels.

<!-- section_id: "f0f89345-60a4-41c2-b989-471934ac12d0" -->
### R4: Links Tab is Per-Answer Only

The "Links" tab shows sources ONLY for the currently active/last answer. Use it as supplementary to React fiber extraction, not as primary source.

<!-- section_id: "46bfa3dc-6150-4c4d-a4a2-3ddbff3cf2a8" -->
### R5: Preserve All Source URLs

Every extraction output MUST include a complete deduplicated citation list with full URLs. Missing citations must be documented in a "Not Captured" section with explanation.

<!-- section_id: "05aa541e-4c65-45b4-8b64-4cf0ce073048" -->
### R6: Output Format

Extraction outputs follow the template in `/perplexity-extract` skill: metadata header, per-answer summaries (not verbatim), categorized citation URLs.
