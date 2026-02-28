# Cross-Entity Porting Bridge Validation Design

## Goal
Validate the contract between upstream `tool_and_app_agnostic` and downstream `context_chain_system`.

## Checks
1. Bridge contract docs exist in both entities.
2. Upstream agnostic sync design artifact exists.
3. Downstream codex contract artifact exists.
4. Both bridge docs cross-reference each other correctly.
5. Downstream bridge captures Codex max-permission runtime policy.
