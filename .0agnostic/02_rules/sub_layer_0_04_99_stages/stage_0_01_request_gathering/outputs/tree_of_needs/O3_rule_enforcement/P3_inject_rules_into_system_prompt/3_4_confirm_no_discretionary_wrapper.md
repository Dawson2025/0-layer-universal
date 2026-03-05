---
resource_id: "ab8b5634-7f5c-4a2a-a6f7-f46da87a227b"
resource_type: "rule"
resource_name: "3_4_confirm_no_discretionary_wrapper"
---
# 3.4: Confirm No Discretionary Wrapper

## Requirement

Verify that critical rules in system prompt are NOT wrapped by discretionary disclaimer.

## Acceptance Criteria

- [ ] Rules do not appear with discretionary wrapper text
- [ ] Rules are in system prompt (not foundational context)
- [ ] Absence of wrapper is confirmed through inspection
- [ ] Testing confirms rules are mandatory (not optional)

## Owner Stage

- **Testing**: Stage 0_07_testing (verify this critical property)

## Dependencies

- Requires: 3.3 (can see what's in system prompt)
- Enables: 3.5 (test actual enforcement)

## Navigation

- **Parent need**: `PARENT_NEED_P3.md`
- **Previous sibling**: `3_3_verify_rules_in_system_prompt.md`
- **Next sibling**: `3_5_test_rule_immutability.md`
