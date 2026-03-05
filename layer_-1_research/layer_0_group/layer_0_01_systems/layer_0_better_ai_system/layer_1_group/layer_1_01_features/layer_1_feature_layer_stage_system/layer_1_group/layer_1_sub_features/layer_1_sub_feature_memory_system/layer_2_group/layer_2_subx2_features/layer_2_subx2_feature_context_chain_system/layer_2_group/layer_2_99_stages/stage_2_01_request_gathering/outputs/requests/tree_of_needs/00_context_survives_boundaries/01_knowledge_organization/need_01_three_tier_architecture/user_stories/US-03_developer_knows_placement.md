---
resource_id: "bc22f16e-2b37-4007-9db6-eeb16001a8d5"
resource_type: "output"
resource_name: "US-03_developer_knows_placement"
---
# US-03: Developer knows what goes where

**Need**: [Three-Tier Architecture](../README.md)

---

**As a** user creating new content and telling the AI where to put it,
**I want** clear rules for what belongs in 0AGNOSTIC.md vs .0agnostic/knowledge/ vs stage outputs,
**So that** I don't accidentally bloat static context or create duplicate content across tiers.

<!-- section_id: "6f8d86a3-8609-4fc6-a7bb-fa3103ad0596" -->
### What Happens

1. User creates or asks the AI to create new content (research findings, design decisions, etc.)
2. User or AI consults the tier boundary rules to decide placement
3. Content goes into the correct tier: pointers in Tier 1, distilled summaries in Tier 2, full content in Tier 3
4. No duplication between tiers; static context stays lean

<!-- section_id: "5514b560-cf60-4c06-af70-a5f6baccd210" -->
### Acceptance Criteria

- Tier boundary rules are documented with examples and anti-patterns
- Rules are unambiguous: given any piece of content, placement is deterministic
- Anti-patterns show what NOT to do (e.g., putting paragraphs of detail in 0AGNOSTIC.md)
