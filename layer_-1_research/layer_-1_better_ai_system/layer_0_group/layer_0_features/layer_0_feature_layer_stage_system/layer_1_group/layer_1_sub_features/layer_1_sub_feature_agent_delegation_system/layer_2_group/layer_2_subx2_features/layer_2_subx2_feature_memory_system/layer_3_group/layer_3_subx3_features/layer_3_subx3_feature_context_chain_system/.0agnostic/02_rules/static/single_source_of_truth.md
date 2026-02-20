# Rule: Single Source of Truth

**Status**: MANDATORY
**Applies**: Every session, every modification

---

## Rule

`0AGNOSTIC.md` is the single source of truth for every entity's context. All tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md) are derived from it.

1. **Never edit generated files directly** — edit `0AGNOSTIC.md` instead
2. **Run `agnostic-sync.sh` after every edit** to regenerate tool-specific files
3. **Commit generated files alongside the source** — both must stay in sync
4. **Use `.1merge/` for tool-specific additions** — never put tool-only content in `0AGNOSTIC.md`

## Scope

This rule applies to every entity that has an `0AGNOSTIC.md`:
- `0AGNOSTIC.md` — edit this
- `CLAUDE.md` — generated, do not edit
- `AGENTS.md` — generated, do not edit
- `GEMINI.md` — generated, do not edit
- `OPENAI.md` — generated, do not edit

## Detection

Generated files have the footer: `*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*`

If a file has this footer, it is generated. Do not edit it.

## Verification

```bash
# Content should match (modulo formatting)
diff <(grep "^## Identity" -A 20 CLAUDE.md) <(grep "^## Identity" -A 20 0AGNOSTIC.md)
```

## Related

- Principle: `knowledge/principles/single_source_of_truth.md`
- Sync script: `.0agnostic/agnostic-sync.sh`
