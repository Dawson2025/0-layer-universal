# US-01: Agent Creates New Pointer

**Need**: [Pointer Format](../README.md)

---

**As an** AI agent encountering duplicate content,
**I want** to replace it with a pointer file using the standard frontmatter format,
**So that** the canonical content has a single source of truth and the pointer auto-updates if the target moves.

### What Happens

1. Agent identifies content that duplicates a canonical source
2. Agent writes a pointer file with YAML frontmatter (`pointer_to:`, `canonical_entity:`, etc.)
3. Agent adds `> **Canonical location**:` line and description
4. Agent runs `pointer-sync.sh --validate` to confirm it resolves
5. Hook reminds agent to validate if they forget

### Acceptance Criteria

- Pointer file passes `pointer-sync.sh --validate`
- Canonical location line is auto-filled with correct relative path
- Original duplicate content is removed
