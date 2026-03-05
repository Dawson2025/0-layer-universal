---
resource_id: "13f52a44-394d-46ef-975f-30f02be8e42d"
resource_type: "rule"
resource_name: "3_2_use_agent_sdk_initialization"
---
# 3.2: Use Agent SDK Initialization

## Requirement

Use Claude Code Agent SDK with `systemPrompt` + `append: true` to inject rules into system prompt.

## Acceptance Criteria

- [ ] Agent SDK initialization code is written
- [ ] `systemPrompt` parameter is populated with formatted rules
- [ ] `append: true` is set to prepend to defaults
- [ ] Initialization is tested and works reliably
- [ ] Code follows Agent SDK best practices

## Owner Stage

- **Design**: Stage 0_05_design
- **Development**: Stage 0_06_development

## Dependencies

- Requires: 3.1 (rules are formatted)
- Enables: 3.3 (can verify injection worked)

## Navigation

- **Parent need**: `PARENT_NEED_P3.md`
- **Previous sibling**: `3_1_format_rules_for_injection.md`
- **Next sibling**: `3_3_verify_rules_in_system_prompt.md`
