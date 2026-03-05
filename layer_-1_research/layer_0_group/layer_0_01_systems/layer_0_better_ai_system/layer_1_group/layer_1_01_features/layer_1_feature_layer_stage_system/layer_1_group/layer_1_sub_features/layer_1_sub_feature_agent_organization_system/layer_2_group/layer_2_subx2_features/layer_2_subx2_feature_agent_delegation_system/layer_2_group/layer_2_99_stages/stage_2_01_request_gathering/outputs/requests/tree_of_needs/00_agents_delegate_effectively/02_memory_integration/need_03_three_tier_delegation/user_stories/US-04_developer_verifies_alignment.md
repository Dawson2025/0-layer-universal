---
resource_id: "48ee2771-5996-4691-a945-d0a9acd28ef0"
resource_type: "output"
resource_name: "US-04_developer_verifies_alignment"
---
# US-4: Developer verifies tier-agent alignment

**Need**: [Three-Tier Delegation](../README.md)

---

**As a** user who wants to verify that the three-tier knowledge system is correctly mapped to agent types,
**I want** a clear document showing which agent type accesses which tier,
**So that** I can audit whether agents are staying within their intended context scope.

<!-- section_id: "a4afc7d4-a41b-4dc2-9c94-ee5817ac4ebe" -->
### What Happens

1. User wants to review the system's knowledge architecture
2. User reads the tier-to-agent mapping document
3. Document shows: managers use Tier 1 (pointers), stage agents use Tier 2 (distilled) + own Tier 3, nobody loads another stage's Tier 3
4. User verifies the mapping matches the intended design
5. User can identify violations if any agent is loading the wrong tier

<!-- section_id: "b40788a2-0cca-4d84-b558-76353925e58b" -->
### Acceptance Criteria

- Tier-to-agent mapping document exists with clear rules and no ambiguity
- Document covers all agent types and all three tiers
- Rules are specific enough to detect violations (not vague descriptions)
