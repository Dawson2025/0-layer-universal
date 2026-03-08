---
resource_id: "9e94b0ca-5a4e-47cf-8c5b-d179daf112de"
resource_type: "readme_document"
resource_name: "README"
---
# Trigger Pointer System

A sub-feature of the context chain system that automates pointer file synchronization.

<!-- section_id: "86c12d00-4a00-4a63-a1d7-26b208463c9e" -->
## What It Does

Pointer files reference canonical content locations using relative paths. When directories are moved or renamed, these paths break silently. This system:

1. **Detects** pointer files via YAML frontmatter (`pointer_to:` field)
2. **Resolves** canonical locations by searching for entity directories
3. **Updates** relative paths automatically
4. **Triggers** validation via Claude Code hooks after edits
5. **Integrates** with agnostic-sync.sh for routine validation

<!-- section_id: "5130bbb6-652e-4da4-af02-0aab3ede4f88" -->
## Production Artifacts

All promoted to root `.0agnostic/`:
- `pointer-sync.sh` — main sync script
- `03_protocols/pointer_sync_protocol/pointer_sync_protocol.md` — usage protocol
- `01_knowledge/pointer_sync/pointer_sync_knowledge.md` — system knowledge
- `02_rules/static/pointer_sync_rule/` — format rule
- `06_.../08_hooks/scripts/pointer-edit-guard.sh` — edit-time hook

<!-- section_id: "cb65ff8a-a405-424f-a923-184d144797f4" -->
## Parent

Part of `layer_2_subx2_feature_context_chain_system` — the pointer system automates the first tier (Pointers) of the three-tier knowledge architecture.
