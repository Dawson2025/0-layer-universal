# US-4: Chain loads identity, not detail

**Need**: [Context Chain Support](../README.md)

---

**As a** user who wants the AI to have hierarchical awareness without wasting tokens,
**I want** ancestor levels in the context chain to include only identity and scope, not full detail,
**So that** the AI gets orientation about its place in the hierarchy without context bloat.

### What Happens

1. User starts a session and the AI loads its context chain
2. The agent's own level loads full 0AGNOSTIC.md (identity, methodology, outputs)
3. Parent level loads identity and scope only (name, role, children pointers)
4. Grandparent level (if included) loads only a brief scope statement
5. Each ancestor level loads progressively less content, preserving context window

### Acceptance Criteria

- Each ancestor level loads progressively less content than the level below it
- Grandparent level includes only identity and scope, not full 0AGNOSTIC.md
- Total chain content is bounded and predictable regardless of hierarchy depth
