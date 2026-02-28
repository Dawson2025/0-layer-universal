# US-03: Developer knows what goes where

**Need**: [Three-Tier Architecture](../README.md)

---

**As a** user creating new content and telling the AI where to put it,
**I want** clear rules for what belongs in 0AGNOSTIC.md vs .0agnostic/knowledge/ vs stage outputs,
**So that** I don't accidentally bloat static context or create duplicate content across tiers.

### What Happens

1. User creates or asks the AI to create new content (research findings, design decisions, etc.)
2. User or AI consults the tier boundary rules to decide placement
3. Content goes into the correct tier: pointers in Tier 1, distilled summaries in Tier 2, full content in Tier 3
4. No duplication between tiers; static context stays lean

### Acceptance Criteria

- Tier boundary rules are documented with examples and anti-patterns
- Rules are unambiguous: given any piece of content, placement is deterministic
- Anti-patterns show what NOT to do (e.g., putting paragraphs of detail in 0AGNOSTIC.md)
