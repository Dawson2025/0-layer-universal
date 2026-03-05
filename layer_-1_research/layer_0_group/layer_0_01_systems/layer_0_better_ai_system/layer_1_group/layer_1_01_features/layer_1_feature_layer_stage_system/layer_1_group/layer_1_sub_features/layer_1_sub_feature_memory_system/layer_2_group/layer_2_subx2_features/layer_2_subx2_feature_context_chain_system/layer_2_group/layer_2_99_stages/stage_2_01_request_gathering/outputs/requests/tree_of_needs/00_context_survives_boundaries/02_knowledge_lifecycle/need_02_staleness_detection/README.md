---
resource_id: "4ab47b24-0e74-44c9-9ab3-310240c53785"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Staleness Detection

**Branch**: [02_knowledge_lifecycle](../)
**Question**: "How do we know when knowledge files are outdated?"
**Version**: 1.0.0

---

<!-- section_id: "93d08e14-9a36-4b7f-b2c9-ec8d24ee799b" -->
## Definition

A mechanism to detect when distilled knowledge files (Tier 2) have drifted from their source stage outputs (Tier 3). Staleness = the source has changed but the summary hasn't been updated.

---

<!-- section_id: "fc98cdfa-e499-48fa-a830-6a3017794a03" -->
## Why This Matters

- A stale knowledge file is worse than no knowledge file -- it gives agents false confidence
- Stage outputs evolve (new research, revised designs) but knowledge files don't auto-update
- Without detection, staleness is invisible until an agent acts on wrong information

---

<!-- section_id: "355f6aa9-565b-4e79-a367-3b1a7983489d" -->
## Acceptance Criteria

- [ ] Staleness check runs and produces a report
- [ ] Stale knowledge files are identified with their source references
- [ ] Report is actionable (developer knows what to update)
- [ ] Integrates with existing validation tooling

---

<!-- section_id: "b489bc49-a3ca-4cfe-ba7d-ed16088d3034" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

<!-- section_id: "92229045-bc4d-4c03-b2f8-9f9dd8e3c6dc" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.
