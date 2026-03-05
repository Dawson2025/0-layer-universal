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

## Definition

A mechanism to detect when distilled knowledge files (Tier 2) have drifted from their source stage outputs (Tier 3). Staleness = the source has changed but the summary hasn't been updated.

---

## Why This Matters

- A stale knowledge file is worse than no knowledge file -- it gives agents false confidence
- Stage outputs evolve (new research, revised designs) but knowledge files don't auto-update
- Without detection, staleness is invisible until an agent acts on wrong information

---

## Acceptance Criteria

- [ ] Staleness check runs and produces a report
- [ ] Stale knowledge files are identified with their source references
- [ ] Report is actionable (developer knows what to update)
- [ ] Integrates with existing validation tooling

---

## Requirements

See [requirements/](./requirements/) for individual requirements.

## User Stories

See [user_stories/](./user_stories/) for individual stories.
