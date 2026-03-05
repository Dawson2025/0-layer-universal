---
resource_id: "90cd0a3e-0590-4a63-bcda-cd346421b0b9"
resource_type: "knowledge"
resource_name: "rules_overview"
---
# Production Rules Overview

## Summary

The production rules system lives in `.0agnostic/02_rules/` and is organized into static rules (always-apply, loaded on every relevant API request) and scenario-based rules (loaded when specific conditions are met). Rules cascade downward through the hierarchy -- all layer_0 rules apply to every entity below.

Static (always-apply) rules include: AI Context Modification Protocol, AI Context Commit/Push Rule, Context Traversal Rule, File Path Linking Rule, context priority rules, and context scope boundaries. Scenario-based rules include: safety governance, Layer Context Header Protocol, sequential development methodology, Cross-OS Compatibility Rules, AI Documentation Protocol, Context File Pattern, Location Rule Application Protocol, and Output-First Protocol.

A known issue identified in early research (2026-01-25) was the lack of a rule priority system, conflicting rule versions, and unclear rule scoping. The current production system partially addresses this by splitting into static vs scenario-based categories, but the full rule registry and conflict resolution infrastructure remains an area for improvement.

## Key Concepts

- **Static rules**: Always apply; loaded at .0agnostic/02_rules/static/ (or 0_every_api_request/)
- **Scenario-based rules**: Triggered by conditions; at .0agnostic/02_rules/1_scenario_based/ (or dynamic/)
- **Cascade**: layer_0 rules apply everywhere below
- **Known gap**: No formal rule priority/conflict resolution system yet
- **Entity-level rules**: Each entity can have its own .0agnostic/02_rules/ that extend (not override) parent rules

## Reference Table

| What | Where | Notes |
|------|-------|-------|
| Production rules root | `.0agnostic/02_rules/` | Authoritative rule location |
| Static rules | `.0agnostic/02_rules/0_every_api_request/` | Always-apply rules |
| Scenario rules | `.0agnostic/02_rules/1_scenario_based/` | Condition-triggered rules |
| Rules problems research | `.0agnostic/01_knowledge/things_learned/01_rules_problems.md` | Early audit of rule system issues |
| Context priority rules | `.0agnostic/02_rules/context_priority_rules.md` | How conflicts between context sources are resolved |
| Context scope boundaries | `.0agnostic/02_rules/context_scope_boundaries.md` | What is in/out of scope per entity |
