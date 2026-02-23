# Agnostic Update Protocol

**Type**: Static (always loaded)
**Importance**: I1 (High)
**Scope**: All agents at all levels

## Rule

When adding, modifying, or removing ANY content in `.0agnostic/`, the agent MUST also update `0AGNOSTIC.md` to keep it in sync as the discovery index.

## Required Updates by Content Type

### Adding/modifying in `.0agnostic/01_knowledge/`
Update `0AGNOSTIC.md` → **Resources Available → Knowledge** table:
- Add the topic name and description
- Update **Current Status → Scope** with new content count

### Adding/modifying in `.0agnostic/02_rules/`
Update `0AGNOSTIC.md` → **Resources Available → Rules** table:
- Add the rule filename, importance level, and description
- If the rule adds new trigger conditions → also update **Triggers** table

### Adding/modifying in `.0agnostic/03_protocols/`
Update `0AGNOSTIC.md` → **Resources Available → Protocols** table:
- Add the protocol filename and description
- If the protocol is triggered by a situation → also update **Triggers** table

### Adding/modifying in `.0agnostic/06_context_avenue_web/`
Update:
- **Resources Available → Context Registry** section
- The avenue's `REGISTRY.md` in `00_context_avenue_web_registry/`
- If adding a skill → also update **Resources Available → Skills** table + **Triggers**

### Removing content from `.0agnostic/`
- Remove the corresponding entry from all relevant sections in `0AGNOSTIC.md`
- Update **Current Status → Scope** with corrected counts
- Run `agnostic-sync.sh` to regenerate tool files

## After Every Update

1. **Edit `0AGNOSTIC.md`** — update relevant sections as described above
2. **Run `agnostic-sync.sh`** — regenerates all tool files (CLAUDE.md, AGENTS.md, etc.)
3. **Review warnings** — the sync script will warn about unreferenced `.0agnostic/` content
4. **If Claude-specific**: also update `.1merge/.1claude_merge/2_additions/tool_additions.md` if the new content should only appear in Claude Code contexts
5. **Commit** — both the `.0agnostic/` content AND the regenerated tool files

## Why This Matters

`0AGNOSTIC.md` is the **discovery index** for all agents. Its STATIC section becomes the CLAUDE.md (and other tool files) that agents read on every session. If `.0agnostic/` has content that 0AGNOSTIC.md doesn't reference, agents will never discover it — the knowledge is invisible.

The chain is:
```
.0agnostic/ content → 0AGNOSTIC.md references it → agnostic-sync.sh → CLAUDE.md includes it → agent reads it
```

Break any link and the content is orphaned.
