---
resource_id: "00df51bb-1795-41dc-acfa-91591585a4d2"
resource_type: "output"
resource_name: "US-03_developer_verifies_consolidation_quality"
---
# US-03: Developer verifies consolidation quality

**Need**: [Consolidation Process](../README.md)

---

**As a** user reviewing a consolidation the AI just performed,
**I want** a checklist to verify that knowledge files are genuinely distilled (not just copied) and reference their sources,
**So that** the three-tier pattern is maintained and agents get real summaries, not bloated duplicates.

<!-- section_id: "e2591948-50dd-4ee0-bfc7-d2d5c29e2353" -->
### What Happens

1. User or AI completes a consolidation (distilling stage outputs into knowledge files)
2. User runs through the quality checklist on each new knowledge file
3. Checklist verifies: sources are referenced, content is distilled not copied, file size is within bounds
4. Any failing items are fixed before the knowledge files are considered ready

<!-- section_id: "d85f79c0-daa3-4caf-b93c-63a89953bb98" -->
### Acceptance Criteria

- Quality checklist exists with specific, verifiable items
- Every knowledge file passes the checklist
- Checklist catches common problems: missing references, verbatim copying, oversized files
