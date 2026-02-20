# US-4: Developer verifies tier-agent alignment

**Need**: [Three-Tier Delegation](../README.md)

---

**As a** user who wants to verify that the three-tier knowledge system is correctly mapped to agent types,
**I want** a clear document showing which agent type accesses which tier,
**So that** I can audit whether agents are staying within their intended context scope.

### What Happens

1. User wants to review the system's knowledge architecture
2. User reads the tier-to-agent mapping document
3. Document shows: managers use Tier 1 (pointers), stage agents use Tier 2 (distilled) + own Tier 3, nobody loads another stage's Tier 3
4. User verifies the mapping matches the intended design
5. User can identify violations if any agent is loading the wrong tier

### Acceptance Criteria

- Tier-to-agent mapping document exists with clear rules and no ambiguity
- Document covers all agent types and all three tiers
- Rules are specific enough to detect violations (not vague descriptions)
