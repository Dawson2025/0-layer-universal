---
resource_id: "366d7dd8-3cc5-4ffd-9326-9756b26d2790"
resource_type: "rule"
resource_name: "audit_avenues_on_creation"
---
# Rule: Audit Avenue Coverage When Creating Entities

**Status**: MANDATORY
**Applies**: When creating new entities, adding new context items, or scaffolding new features

---

## When This Rule Activates

- Creating a new entity (directory with `0AGNOSTIC.md`)
- Adding a new `.gab.jsonld` agent definition
- Adding new rules or knowledge that should be discoverable
- Scaffolding a new feature or sub-feature

## Rule

After creating a new entity, verify that critical context is reachable through at least 3 independent avenues:

1. **Check avenue presence**:
   - A1: Does `CLAUDE.md` exist? (run `agnostic-sync.sh` if not)
   - A2: Are there `.claude/rules/*.md` files?
   - A3: Are there `.0agnostic/skills/*/SKILL.md` files?
   - A4: Does `0AGNOSTIC.md` have a valid `**Parent**:` reference?
   - A5: Does a `.gab.jsonld` exist?
   - A6: Does a matching `.integration.md` exist?
   - A8: Does `.0agnostic/` have rules and knowledge?

2. **Count functional avenues** (exclude A7 episodic — empty on first creation)
3. **Target**: 5+ avenues functional at creation time
4. **Minimum**: 3 avenues functional (identity reachable through 3 paths)

## What to Create at Minimum

| Avenue | Minimum File | Lines |
|--------|-------------|-------|
| A1 | `CLAUDE.md` (via agnostic-sync) | Auto |
| A4 | `0AGNOSTIC.md` with Identity + Parent | 10 |
| A8 | `.0agnostic/rules/.gitkeep` | 0 |

## Related

- Static rule: `static/avenue_redundancy.md`
- Protocol: `../protocols/entity_chain_setup_protocol.md`
- Skill: `skills/avenue-check/SKILL.md`
