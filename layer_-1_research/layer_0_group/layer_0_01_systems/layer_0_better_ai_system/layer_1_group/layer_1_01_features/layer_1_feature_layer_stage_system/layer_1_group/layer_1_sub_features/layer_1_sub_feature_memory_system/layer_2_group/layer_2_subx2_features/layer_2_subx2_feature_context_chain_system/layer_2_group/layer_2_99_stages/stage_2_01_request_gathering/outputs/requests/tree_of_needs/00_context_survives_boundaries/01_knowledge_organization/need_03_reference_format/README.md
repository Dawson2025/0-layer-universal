---
resource_id: "8be5cb48-1cf6-49ed-8748-12e094c76a75"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Reference Format Standard

**Branch**: [01_knowledge_organization](../)
**Question**: "How do tiers reference each other consistently?"
**Version**: 1.0.0

---

## Definition

A standard format for how knowledge files (Tier 2) reference stage outputs (Tier 3), and how pointers (Tier 1) reference knowledge files. Without this, every file invents its own reference style, making automated validation impossible.

---

## Why This Matters

- Inconsistent references can't be validated by scripts
- Agents need predictable reference patterns to follow links
- Staleness detection requires parseable references to check source freshness

---

## Acceptance Criteria

- [ ] Reference format is documented with examples
- [ ] A script can parse references from any knowledge file
- [ ] All existing knowledge files follow the format (or are migrated)
- [ ] Directional rules are enforced (no upward references)

---

## Requirements

See [requirements/](./requirements/) for individual requirements.

## User Stories

See [user_stories/](./user_stories/) for individual stories.
