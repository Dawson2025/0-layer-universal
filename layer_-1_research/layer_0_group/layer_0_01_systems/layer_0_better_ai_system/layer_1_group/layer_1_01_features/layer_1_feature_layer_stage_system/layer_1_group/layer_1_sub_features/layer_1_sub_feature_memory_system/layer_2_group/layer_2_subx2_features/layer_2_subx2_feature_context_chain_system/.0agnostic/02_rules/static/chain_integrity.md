---
resource_id: "970b14ee-f55a-4b40-b789-6b3dd7a02c65"
resource_type: "rule"
resource_name: "chain_integrity"
---
# Chain Integrity Rule

## Rule: Never Break a Parent Reference in 0AGNOSTIC.md

Parent references in 0AGNOSTIC.md files form the backbone of the context chain. A broken parent reference severs the chain and makes all ancestor context unreachable.

## What Constitutes a Break

| Action | Result | Severity |
|--------|--------|----------|
| Deleting a 0AGNOSTIC.md file | Child loses parent link | CRITICAL |
| Changing Parent path to nonexistent file | Chain terminates early | CRITICAL |
| Removing the Parent line entirely | Chain terminates at this node | CRITICAL |
| Renaming a directory without updating child refs | Children point to old path | HIGH |
| Moving a directory without updating parent refs | Parent path resolves to nothing | HIGH |

## Prevention Protocol

Before modifying, moving, or deleting any entity:

1. **Search for references**: Check if any child 0AGNOSTIC.md files reference this entity as their Parent
2. **Update children first**: If references exist, update all child Parent paths before making changes
3. **Verify after changes**: Run `/chain-validate` to confirm the full chain is intact
4. **Never delete without checking**: Even "empty" entities may be chain links

## Detection

The test suite (`test_context_chain_traversal.sh`) validates the full parent chain. Run it after any structural changes:

```
./tests/test_context_chain_traversal.sh
```

A broken chain produces: `FAIL: Parent path does not exist: [path]`

## Recovery

If a parent reference is broken:

1. Identify the broken link from test output
2. Create a minimum viable 0AGNOSTIC.md at the expected path:
   ```markdown
   ## Identity
   **Role**: [entity name]
   **Scope**: [brief description]

   ## Parent
   [path to parent 0AGNOSTIC.md]
   ```
3. Re-run validation to confirm the chain is restored
4. Fill in remaining sections as time permits
