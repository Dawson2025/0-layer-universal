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

## Requirements

### Reference Format
- MUST define a standard reference syntax for cross-tier links
- MUST include: target file path, target section (if applicable), one-line description
- MUST be parseable by scripts (not just human-readable prose)
- SHOULD use relative paths from the referencing file
- SHOULD follow existing markdown link conventions where possible

### Directional Rules
- MUST define: knowledge files reference stage outputs (downward)
- MUST define: 0AGNOSTIC.md references knowledge files and stage index (downward)
- MUST NOT: stage outputs reference knowledge files (upward references create coupling)
- SHOULD: stage outputs be self-contained (readable without knowledge files)

---

## Acceptance Criteria

- [ ] Reference format is documented with examples
- [ ] A script can parse references from any knowledge file
- [ ] All existing knowledge files follow the format (or are migrated)
- [ ] Directional rules are enforced (no upward references)

---

## User Stories

See [user_stories.md](./user_stories.md)
