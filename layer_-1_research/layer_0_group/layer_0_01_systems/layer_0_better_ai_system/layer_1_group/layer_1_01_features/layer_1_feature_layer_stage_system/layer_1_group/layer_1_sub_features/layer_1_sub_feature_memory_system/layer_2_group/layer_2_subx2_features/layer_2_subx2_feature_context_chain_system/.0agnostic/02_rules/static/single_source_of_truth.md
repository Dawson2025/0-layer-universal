---
resource_id: "d7a60949-b285-4694-a184-59d5ad6514d4"
resource_type: "rule"
resource_name: "single_source_of_truth"
---
# Rule: Single Source of Truth

**Status**: MANDATORY
**Applies**: Every session, every modification

---

<!-- section_id: "38fb711e-d3eb-4724-9ae4-aac074597459" -->
## Rule

`0AGNOSTIC.md` is the single source of truth for every entity's context. All tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md) are derived from it.

1. **Never edit generated files directly** — edit `0AGNOSTIC.md` instead
2. **Run `agnostic-sync.sh` after every edit** to regenerate tool-specific files
3. **Commit generated files alongside the source** — both must stay in sync
4. **Use `.1merge/` for tool-specific additions** — never put tool-only content in `0AGNOSTIC.md`

<!-- section_id: "ba160d5d-3652-4c8e-8427-fe429222c97e" -->
## Scope

This rule applies to every entity that has an `0AGNOSTIC.md`:
- `0AGNOSTIC.md` — edit this
- `CLAUDE.md` — generated, do not edit
- `AGENTS.md` — generated, do not edit
- `GEMINI.md` — generated, do not edit
- `OPENAI.md` — generated, do not edit

<!-- section_id: "edfcb3ec-98ba-4a56-958f-13622b777024" -->
## Detection

Generated files have the footer: `*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*`

If a file has this footer, it is generated. Do not edit it.

<!-- section_id: "2cd1a1a8-fc29-49f9-b873-477e07af0442" -->
## Verification

```bash
# Content should match (modulo formatting)
diff <(grep "^## Identity" -A 20 CLAUDE.md) <(grep "^## Identity" -A 20 0AGNOSTIC.md)
```

<!-- section_id: "c2bc83e5-7cfa-4a63-8a19-8bd4e696a50b" -->
## Related

- Principle: `knowledge/principles/single_source_of_truth.md`
- Sync script: `.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh`
