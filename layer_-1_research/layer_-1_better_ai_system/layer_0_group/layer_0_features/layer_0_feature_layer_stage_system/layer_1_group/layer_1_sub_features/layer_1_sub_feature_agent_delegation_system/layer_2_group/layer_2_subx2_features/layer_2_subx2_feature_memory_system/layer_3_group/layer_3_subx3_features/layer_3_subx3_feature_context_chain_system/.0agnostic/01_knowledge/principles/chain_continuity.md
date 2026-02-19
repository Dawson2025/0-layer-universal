# Principle: Chain Continuity

**Type**: Structural Integrity
**Severity**: Critical
**Date**: 2026-02-17

---

## Statement

**Every entity in the layer-stage system must maintain an unbroken parent reference chain from itself to the system root.**

A broken chain means an entity is orphaned — it cannot inherit context, rules, or knowledge from its ancestors, and agents cannot traverse upward for escalation or scope validation.

---

## Rationale

The parent chain is the backbone of the context inheritance system. When an agent arrives at an entity:
1. It reads `0AGNOSTIC.md` for local identity
2. It follows `Parent:` to get broader scope
3. It continues upward to understand the full hierarchy

If any link is broken, the agent works with incomplete context. This leads to:
- Missing rules that should have been inherited
- Incorrect scope assumptions
- Failed escalation paths
- Inconsistent behavior across sessions

---

## Requirements

### Must

- Every `0AGNOSTIC.md` (except root) **must** have a `**Parent**:` line
- The parent path **must** resolve to an existing `0AGNOSTIC.md`
- The parent file **must** have an `## Identity` section
- Container directories (groups, feature registries) **must** have `0AGNOSTIC.md` even if minimal

### Must Not

- Never delete an `0AGNOSTIC.md` that is referenced as a parent by any child
- Never change a parent path without updating all children that reference the old path
- Never create an entity without establishing its parent reference

---

## Verification

Chain continuity is tested by `test_context_chain_traversal.sh`:
- Verifies each parent reference resolves
- Walks the full chain from leaf to root
- Checks for Identity section at each level
- Reports chain depth

---

## Recovery

If a chain break is discovered:
1. Identify the missing node (which `0AGNOSTIC.md` doesn't exist)
2. Create a minimum viable `0AGNOSTIC.md` with Identity + Parent
3. Run `agnostic-sync.sh` to generate tool-specific files
4. Re-test the chain

---

## Related Principles

- Single Source of Truth — the chain relies on 0AGNOSTIC.md being canonical
- Graceful Degradation — avenue redundancy mitigates partial chain failures
