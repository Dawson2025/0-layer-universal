## Codex Discovery Triggers

When requests mention context-chain operations, load these next:

1. Contract: `.0agnostic/01_knowledge/codex_cli_context_contract.md`
2. Rules: `.0agnostic/02_rules/static/` then `.0agnostic/02_rules/dynamic/`
3. Protocols: `.0agnostic/03_protocols/chain_validation_protocol.md`
4. Skills: `.0agnostic/05_skills/chain-validate/SKILL.md` and `.0agnostic/05_skills/avenue-check/SKILL.md`

## Codex Merge Diagnostics

If projection looks wrong:
- Verify `.1merge/.1codex_merge/1_overrides/tool_boilerplate.md` is non-empty.
- Verify `.1merge/.1codex_merge/2_additions/tool_additions.md` is non-empty.
- Re-run `.0agnostic/agnostic-sync.sh` for this entity.
- Re-run `stage_2_07_testing/outputs/test_codex_projection.sh`.
