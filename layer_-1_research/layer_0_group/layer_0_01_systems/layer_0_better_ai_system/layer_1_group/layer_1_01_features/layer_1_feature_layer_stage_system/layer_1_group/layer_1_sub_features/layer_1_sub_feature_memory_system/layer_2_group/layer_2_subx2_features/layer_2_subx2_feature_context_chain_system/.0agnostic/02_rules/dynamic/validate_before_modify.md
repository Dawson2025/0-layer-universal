---
resource_id: "c1c37ba9-a1a9-42ab-824a-6113ad41b330"
resource_type: "rule"
resource_name: "validate_before_modify"
---
# Rule: Validate Chain Before Structural Modifications

**Status**: MANDATORY
**Applies**: When modifying entity structure, renaming directories, or changing parent references

---

<!-- section_id: "d0dedd7c-40fb-41e8-b21a-706113f53000" -->
## When This Rule Activates

- Moving or renaming any entity directory
- Editing the `**Parent**:` line in any `0AGNOSTIC.md`
- Deleting any `0AGNOSTIC.md` file
- Creating a new entity that will become a parent or child
- Restructuring the layer-stage hierarchy

<!-- section_id: "82cb6a89-e285-450d-9af2-3008d2fef10c" -->
## Rule

Before making structural changes, validate the affected chain segment:

1. **Identify affected nodes** — which entities reference the target as parent?
2. **Run chain validation** on affected nodes:
   ```bash
   ./tests/test_context_chain_traversal.sh
   ```
3. **Record current state** — note the chain depth and all resolved parent paths
4. **Make the change**
5. **Re-validate** — run chain validation again, confirm no new breaks
6. **Update children** — if parent path changed, update all child `0AGNOSTIC.md` files

<!-- section_id: "ecc0c5ac-d8d5-473f-b217-88c0bfdb9ed8" -->
## Why Only on Modification

This rule is dynamic because chain validation is expensive (reads multiple files up the hierarchy). Running it on every task wastes tokens. It only matters when the chain itself is being changed.

<!-- section_id: "72b55b9e-2322-46a2-ac14-d21a6ab9efa1" -->
## Failure Response

If validation fails after modification:
1. Revert the change immediately
2. Create a minimum viable `0AGNOSTIC.md` at any missing node
3. Re-validate until the chain is intact
4. Only then proceed with the original modification using the correct approach

<!-- section_id: "327984f3-11f2-45eb-8dea-315895fefe85" -->
## Related

- Static rule: `static/chain_integrity.md`
- Protocol: `../protocols/chain_repair_protocol.md`
- Skill: `skills/chain-validate/SKILL.md`
