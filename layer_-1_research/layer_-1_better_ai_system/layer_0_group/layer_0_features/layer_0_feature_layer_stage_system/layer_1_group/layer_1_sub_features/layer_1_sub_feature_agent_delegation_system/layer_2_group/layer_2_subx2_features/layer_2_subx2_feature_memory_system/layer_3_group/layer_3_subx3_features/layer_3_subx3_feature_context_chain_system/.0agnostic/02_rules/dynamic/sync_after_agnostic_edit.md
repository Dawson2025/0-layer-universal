# Rule: Sync After Every 0AGNOSTIC.md Edit

**Status**: MANDATORY
**Applies**: After editing any `0AGNOSTIC.md` file

---

## When This Rule Activates

- Any edit to `0AGNOSTIC.md` content (Identity, Navigation, Triggers, Key Behaviors, Critical Rules)
- Adding, removing, or modifying sections in `0AGNOSTIC.md`
- Changing the Parent reference in `0AGNOSTIC.md`

## Rule

After editing `0AGNOSTIC.md`, immediately run `agnostic-sync.sh` to regenerate tool-specific files:

1. **Edit** `0AGNOSTIC.md` with the desired changes
2. **Run sync**:
   ```bash
   bash .0agnostic/agnostic-sync.sh [directory-containing-0AGNOSTIC.md]
   ```
3. **Verify** the generated files match expectations:
   ```bash
   head -20 CLAUDE.md   # check Identity section propagated
   ```
4. **Commit both** `0AGNOSTIC.md` and all generated files together

## Why Dynamic

This rule only fires after an `0AGNOSTIC.md` edit. Most sessions don't edit `0AGNOSTIC.md`, so checking sync status on every call would waste tokens.

## Common Mistakes

| Mistake | Consequence |
|---------|------------|
| Edit CLAUDE.md directly | Overwritten on next sync |
| Edit 0AGNOSTIC.md but skip sync | CLAUDE.md shows stale content |
| Commit 0AGNOSTIC.md without generated files | Tools see old context |
| Run sync on wrong directory | Wrong CLAUDE.md gets overwritten |

## Related

- Static rule: `static/single_source_of_truth.md`
- Principle: `knowledge/principles/single_source_of_truth.md`
