---
resource_id: "ad0a8da3-2e51-4191-9ac2-a9dec2cfc2c0"
resource_type: "output"
resource_name: "US-04_chain_loads_identity_not_detail"
---
# US-4: Chain loads identity, not detail

**Need**: [Context Chain Support](../README.md)

---

**As a** user who wants the AI to have hierarchical awareness without wasting tokens,
**I want** ancestor levels in the context chain to include only identity and scope, not full detail,
**So that** the AI gets orientation about its place in the hierarchy without context bloat.

<!-- section_id: "33143d23-e8c8-46db-acac-9abad08f9699" -->
### What Happens

1. User starts a session and the AI loads its context chain
2. The agent's own level loads full 0AGNOSTIC.md (identity, methodology, outputs)
3. Parent level loads identity and scope only (name, role, children pointers)
4. Grandparent level (if included) loads only a brief scope statement
5. Each ancestor level loads progressively less content, preserving context window

<!-- section_id: "73944791-8fb2-4909-8ef2-63199776212b" -->
### Acceptance Criteria

- Each ancestor level loads progressively less content than the level below it
- Grandparent level includes only identity and scope, not full 0AGNOSTIC.md
- Total chain content is bounded and predictable regardless of hierarchy depth
