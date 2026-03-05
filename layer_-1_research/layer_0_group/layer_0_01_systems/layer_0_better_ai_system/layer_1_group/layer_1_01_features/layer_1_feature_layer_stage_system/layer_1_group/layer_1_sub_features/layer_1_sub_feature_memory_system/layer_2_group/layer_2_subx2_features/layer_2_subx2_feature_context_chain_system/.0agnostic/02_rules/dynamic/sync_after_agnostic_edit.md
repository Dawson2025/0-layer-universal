---
resource_id: "4e6e0c7d-91a7-4ca0-bbd6-ff230d8cf586"
resource_type: "rule"
resource_name: "sync_after_agnostic_edit"
---
# Rule: Sync After Every 0AGNOSTIC.md Edit

**Status**: MANDATORY
**Applies**: After editing any `0AGNOSTIC.md` file

---

<!-- section_id: "4a382b3c-91f1-49c3-894a-f317f8c26cc3" -->
## When This Rule Activates

- Any edit to `0AGNOSTIC.md` content (Identity, Navigation, Triggers, Key Behaviors, Critical Rules)
- Adding, removing, or modifying sections in `0AGNOSTIC.md`
- Changing the Parent reference in `0AGNOSTIC.md`

<!-- section_id: "e699dfac-f7ab-4217-a91b-8dd5f7650c6d" -->
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

<!-- section_id: "9de17797-c6f5-4ec1-9a84-b7879bd574e4" -->
## Why Dynamic

This rule only fires after an `0AGNOSTIC.md` edit. Most sessions don't edit `0AGNOSTIC.md`, so checking sync status on every call would waste tokens.

<!-- section_id: "f1108a57-712c-48fb-9e92-23caab0477c9" -->
## Common Mistakes

| Mistake | Consequence |
|---------|------------|
| Edit CLAUDE.md directly | Overwritten on next sync |
| Edit 0AGNOSTIC.md but skip sync | CLAUDE.md shows stale content |
| Commit 0AGNOSTIC.md without generated files | Tools see old context |
| Run sync on wrong directory | Wrong CLAUDE.md gets overwritten |

<!-- section_id: "22120862-15f2-467d-9e62-e4d0b54c8b79" -->
## Related

- Static rule: `static/single_source_of_truth.md`
- Principle: `knowledge/principles/single_source_of_truth.md`
