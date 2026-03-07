---
resource_id: "e9919392-2de8-4899-9939-248fbcb63b36"
resource_type: "knowledge"
resource_name: "single_source_of_truth"
---
# Principle: Single Source of Truth

<!-- section_id: "e8ee2448-1e52-4c74-80ff-d19b528a0110" -->
## Summary

`0AGNOSTIC.md` is the single source of truth for every entity's context. All tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md) are derived from it via `agnostic-sync.sh`. Edit 0AGNOSTIC.md, never the generated files. Without a single source, context drifts across tools -- CLAUDE.md says one thing, GEMINI.md says another, and manual edits to generated files get overwritten on the next sync.

The source chain is: 0AGNOSTIC.md (edit this) -> agnostic-sync.sh (transforms) -> CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md (generated, do not edit). The sync script extracts specific h2 sections (Identity, Navigation, Triggers, Key Behaviors, Critical Rules) and wraps them in tool-specific headers. Generated files carry an auto-generated footer marker for verification.

The `.1merge/` system handles the exception of tool-specific content not in 0AGNOSTIC.md, using a 3-tier merge: synced (matches agnostic-sync output), overrides (replace synced sections), additions (new sections). This allows customization while keeping 0AGNOSTIC.md canonical.

<!-- section_id: "5bc1dff6-eba8-4c5e-bcfe-425bd89a5829" -->
## Key Concepts

- **Edit 0AGNOSTIC.md, never CLAUDE.md** -- generated files are overwritten by sync
- **agnostic-sync.sh**: Deterministic transformation from source to tool-specific outputs
- **Always sync after edits**: Run agnostic-sync.sh after every 0AGNOSTIC.md change
- **.1merge/ exception**: 3-tier merge for tool-specific additions (synced > overrides > additions)
- **Verification**: Auto-generated footer marker confirms file origin

<!-- section_id: "e835e385-73d2-4506-85b3-ab37722c6489" -->
## Reference Table

| What | Where | Notes |
|------|-------|-------|
| Full principle doc | `.0agnostic/01_knowledge/principles/single_source_of_truth.md` | Source chain diagram, requirements, .1merge/ details |
| agnostic-sync.sh | `.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh` | The sync script itself |
| Production agnostic system | `.0agnostic/` | Live implementation |
