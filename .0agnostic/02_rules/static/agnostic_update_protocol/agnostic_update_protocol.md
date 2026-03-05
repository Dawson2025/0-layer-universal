---
resource_id: "aa768b5f-9657-4fd1-81ea-3862cc7a052e"
resource_type: "rule"
resource_name: "agnostic_update_protocol"
promote: hot
hot_summary: "When modifying .0agnostic/ files, also update 0AGNOSTIC.md and run agnostic-sync.sh. Full protocol: .0agnostic/02_rules/static/agnostic_update_protocol.md"
hot_trigger: "Modifying any file in .0agnostic/"
---

# Agnostic Update Protocol

**Type**: Static (always loaded)
**Importance**: I1 (High)
**Scope**: All agents at all levels

<!-- section_id: "23e23624-fc91-47c4-9eab-247e6daf6947" -->
## Rule

When adding, modifying, or removing ANY content in `.0agnostic/`, the agent MUST also update `0AGNOSTIC.md` to keep it in sync as the discovery index.

<!-- section_id: "e53b0f3c-51a8-4142-98ca-6e7dcc2de146" -->
## Required Updates by Content Type

<!-- section_id: "65ce6086-311a-4f7e-8602-926b7d342fb1" -->
### Adding/modifying in `.0agnostic/01_knowledge/`
Update `0AGNOSTIC.md` → **Resources Available → Knowledge** table:
- Add the topic name and description
- Update **Current Status → Scope** with new content count

<!-- section_id: "b4d88c46-18af-438b-ae00-4fee570289d1" -->
### Adding/modifying in `.0agnostic/02_rules/`
Update `0AGNOSTIC.md` → **Resources Available → Rules** table:
- Add the rule filename, importance level, and description
- If the rule adds new trigger conditions → also update **Triggers** table

<!-- section_id: "d766056d-ac3f-4c79-8e30-cdb0e2ae1be8" -->
### Adding/modifying in `.0agnostic/03_protocols/`
Update `0AGNOSTIC.md` → **Resources Available → Protocols** table:
- Add the protocol filename and description
- If the protocol is triggered by a situation → also update **Triggers** table

<!-- section_id: "e0986518-6360-4570-bfc2-918f3eb69b67" -->
### Adding/modifying in `.0agnostic/06_context_avenue_web/`
Update:
- **Resources Available → Context Registry** section
- The avenue's `REGISTRY.md` in `00_context_avenue_web_registry/`
- If adding a skill → also update **Resources Available → Skills** table + **Triggers**

<!-- section_id: "4206a088-fede-4122-9b45-bab2141e5583" -->
### Removing content from `.0agnostic/`
- Remove the corresponding entry from all relevant sections in `0AGNOSTIC.md`
- Update **Current Status → Scope** with corrected counts
- Run `agnostic-sync.sh` to regenerate tool files

<!-- section_id: "53597e4b-1efb-46eb-a0ca-11ff7a867bd4" -->
## After Every Update

1. **Edit `0AGNOSTIC.md`** — update relevant sections as described above
2. **Run `agnostic-sync.sh`** — regenerates all tool files (CLAUDE.md, AGENTS.md, etc.)
3. **Review warnings** — the sync script will warn about unreferenced `.0agnostic/` content
4. **If Claude-specific**: also update `.1merge/.1claude_merge/2_additions/tool_additions.md` if the new content should only appear in Claude Code contexts
5. **Commit** — both the `.0agnostic/` content AND the regenerated tool files

<!-- section_id: "da075bb2-2b38-4357-b386-5d41ae8eab6c" -->
## Why This Matters

`0AGNOSTIC.md` is the **discovery index** for all agents. Its STATIC section becomes the CLAUDE.md (and other tool files) that agents read on every session. If `.0agnostic/` has content that 0AGNOSTIC.md doesn't reference, agents will never discover it — the knowledge is invisible.

The chain is:
```
.0agnostic/ content → 0AGNOSTIC.md references it → agnostic-sync.sh → CLAUDE.md includes it → agent reads it
```

Break any link and the content is orphaned.
