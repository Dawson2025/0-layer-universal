---
resource_id: "8be5cb48-1cf6-49ed-8748-12e094c76a75"
resource_type: "readme_output"
resource_name: "README"
---
# Need: Reference Format Standard

**Branch**: [01_knowledge_organization](../)
**Question**: "How do tiers reference each other consistently?"
**Version**: 1.0.0

---

<!-- section_id: "481db411-b6be-4779-a21e-eda3aeaf56fa" -->
## Definition

A standard format for how knowledge files (Tier 2) reference stage outputs (Tier 3), and how pointers (Tier 1) reference knowledge files. Without this, every file invents its own reference style, making automated validation impossible.

---

<!-- section_id: "c06eba2b-3ae1-47df-8513-ef495111b9ac" -->
## Why This Matters

- Inconsistent references can't be validated by scripts
- Agents need predictable reference patterns to follow links
- Staleness detection requires parseable references to check source freshness

---

<!-- section_id: "5e758338-acb8-48fd-8715-1185d05a7baa" -->
## Acceptance Criteria

- [ ] Reference format is documented with examples
- [ ] A script can parse references from any knowledge file
- [ ] All existing knowledge files follow the format (or are migrated)
- [ ] Directional rules are enforced (no upward references)

---

<!-- section_id: "1698bcd1-42b0-4e15-911b-88ceb09ee0a9" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

<!-- section_id: "448c34d9-a4a8-4ab2-80b3-71bb27ee11e8" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.
