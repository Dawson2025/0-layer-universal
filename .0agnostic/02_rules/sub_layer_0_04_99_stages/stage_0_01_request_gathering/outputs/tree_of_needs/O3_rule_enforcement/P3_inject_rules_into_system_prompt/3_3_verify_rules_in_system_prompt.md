---
resource_id: "80010f0e-cfe5-4bd1-a01a-02c2b22adda7"
resource_type: "rule"
resource_name: "3_3_verify_rules_in_system_prompt"
---
# 3.3: Verify Rules in System Prompt

<!-- section_id: "12a0f40d-ed14-4ee0-9dea-985cc8ffc87a" -->
## Requirement

Verify that injected rules actually appear in the system prompt used for API calls.

<!-- section_id: "434d1c02-7edd-4a56-8bd4-10a6e5d7ee9a" -->
## Acceptance Criteria

- [ ] Debug output shows rules in system prompt
- [ ] Rules can be inspected during initialization
- [ ] Verification is reliable and reproducible
- [ ] Procedure for verifying is documented

<!-- section_id: "b20169d2-4a9b-4b39-9daf-ec8548fcafe0" -->
## Owner Stage

- **Development**: Stage 0_06_development
- **Testing**: Stage 0_07_testing

<!-- section_id: "84fcadbb-64ba-4805-83ef-836813a49d4c" -->
## Dependencies

- Requires: 3.2 (injection mechanism)
- Enables: 3.4 (verify no wrapper)

<!-- section_id: "39550f6c-b888-42be-9c9c-23578b179b95" -->
## Navigation

- **Parent need**: `PARENT_NEED_P3.md`
- **Previous sibling**: `3_2_use_agent_sdk_initialization.md`
- **Next sibling**: `3_4_confirm_no_discretionary_wrapper.md`
