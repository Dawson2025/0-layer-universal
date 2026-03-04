# Context Chain Porting Bridge Contract

## Purpose
Define how context-chain propagation consumes upstream agnostic porting contracts and enforces tool-specific projection behavior.

## Dependency Model
- Upstream contract owner:
  - `../../../../../../layer_1_sub_feature_tool_and_app_agnostic/.0agnostic/01_knowledge/overview/docs/agnostic_to_tool_porting_bridge_contract.md`
- Downstream executor:
  - `layer_2_subx2_feature_context_chain_system`

## Consumption Contract
1. Context chain reads upstream agnostic porting contract artifacts as input specifications.
2. Context chain validates projection outputs used by tool-specific agents (Codex included).
3. Context chain tests enforce propagation funnel compatibility for stage/layer reports.

## Required Runtime Mode
For Codex runtime bridge tests and behavior validation:
- `codex exec --dangerously-bypass-approvals-and-sandbox`

## Validation Expectations
Bridge tests in testing stages should verify:
1. Upstream and downstream contract docs both exist.
2. Upstream agnostic sync design remains available.
3. Downstream codex contract remains available.
4. Test output taxonomy includes a bridge-validation purpose suite.
