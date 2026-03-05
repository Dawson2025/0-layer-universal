---
resource_id: "a6efa005-05a6-4762-92e5-5d1581ac276f"
resource_type: "rule"
resource_name: "3_1_format_rules_for_injection"
---
# 3.1: Format Rules for Injection

## Requirement

Rules must be formatted correctly for injection into Claude Code's system prompt via Agent SDK.

## Acceptance Criteria

- [ ] Rules formatted as text block in system prompt
- [ ] Markdown structure is preserved
- [ ] Rule names and descriptions are clear
- [ ] No formatting conflicts with system prompt
- [ ] Injection format is documented

## Owner Stage

- **Design**: Stage 0_05_design
- **Development**: Stage 0_06_development

## Dependencies

- Requires: O2 completion (rules exist)
- Enables: 3.2 (injection uses formatted rules)

## Navigation

- **Parent need**: `PARENT_NEED_P3.md`
- **Next sibling**: `3_2_use_agent_sdk_initialization.md`
