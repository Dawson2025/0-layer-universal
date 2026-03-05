---
resource_id: "80010f0e-cfe5-4bd1-a01a-02c2b22adda7"
resource_type: "rule"
resource_name: "3_3_verify_rules_in_system_prompt"
---
# 3.3: Verify Rules in System Prompt

## Requirement

Verify that injected rules actually appear in the system prompt used for API calls.

## Acceptance Criteria

- [ ] Debug output shows rules in system prompt
- [ ] Rules can be inspected during initialization
- [ ] Verification is reliable and reproducible
- [ ] Procedure for verifying is documented

## Owner Stage

- **Development**: Stage 0_06_development
- **Testing**: Stage 0_07_testing

## Dependencies

- Requires: 3.2 (injection mechanism)
- Enables: 3.4 (verify no wrapper)

## Navigation

- **Parent need**: `PARENT_NEED_P3.md`
- **Previous sibling**: `3_2_use_agent_sdk_initialization.md`
- **Next sibling**: `3_4_confirm_no_discretionary_wrapper.md`
