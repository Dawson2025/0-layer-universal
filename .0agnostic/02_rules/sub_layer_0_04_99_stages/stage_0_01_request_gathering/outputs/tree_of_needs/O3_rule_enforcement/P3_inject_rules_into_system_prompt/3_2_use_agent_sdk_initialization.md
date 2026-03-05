---
resource_id: "13f52a44-394d-46ef-975f-30f02be8e42d"
resource_type: "rule"
resource_name: "3_2_use_agent_sdk_initialization"
---
# 3.2: Use Agent SDK Initialization

<!-- section_id: "4e8826cd-166c-4f28-ba7c-2cedd9117fb4" -->
## Requirement

Use Claude Code Agent SDK with `systemPrompt` + `append: true` to inject rules into system prompt.

<!-- section_id: "449fa71c-a09c-41a6-b06c-f14091cf7a1a" -->
## Acceptance Criteria

- [ ] Agent SDK initialization code is written
- [ ] `systemPrompt` parameter is populated with formatted rules
- [ ] `append: true` is set to prepend to defaults
- [ ] Initialization is tested and works reliably
- [ ] Code follows Agent SDK best practices

<!-- section_id: "6fc81ead-e008-454d-b3cf-290b74639522" -->
## Owner Stage

- **Design**: Stage 0_05_design
- **Development**: Stage 0_06_development

<!-- section_id: "d4fe0d69-1400-485f-8475-d7ba2db5871d" -->
## Dependencies

- Requires: 3.1 (rules are formatted)
- Enables: 3.3 (can verify injection worked)

<!-- section_id: "4a96bac1-9f48-40d5-b610-7447c762f3e8" -->
## Navigation

- **Parent need**: `PARENT_NEED_P3.md`
- **Previous sibling**: `3_1_format_rules_for_injection.md`
- **Next sibling**: `3_3_verify_rules_in_system_prompt.md`
