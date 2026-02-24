# Agnostic System Edit Rule

**Applies to**: Any file path matching `.0agnostic/**`

When editing files inside `.0agnostic/`, you MUST follow the agnostic update protocol:

## Before Editing

Read the full protocol: `.0agnostic/02_rules/static/agnostic_update_protocol.md`

## After Every `.0agnostic/` Edit

1. **Update `0AGNOSTIC.md`** — add/modify references for the content you changed:
   - Knowledge → Resources Available → Knowledge table
   - Rules → Resources Available → Rules table + Triggers table if applicable
   - Protocols → Resources Available → Protocols table
   - Skills → Resources Available → Skills table + Triggers table
2. **Run `agnostic-sync.sh`** — regenerates CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, copilot-instructions.md
3. **Review sync warnings** — any unreferenced content warnings mean 0AGNOSTIC.md is missing entries
4. **Commit both** — the `.0agnostic/` content AND the regenerated tool files

## Why This Matters

The propagation chain is: `.0agnostic/ content → 0AGNOSTIC.md references it → agnostic-sync.sh → CLAUDE.md → agent reads it`. Break any link and the content is invisible to agents.
