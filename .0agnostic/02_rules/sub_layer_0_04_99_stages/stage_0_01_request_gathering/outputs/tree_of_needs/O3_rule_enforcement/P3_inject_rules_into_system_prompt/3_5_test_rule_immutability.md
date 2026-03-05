---
resource_id: "b0b05767-1014-43f1-84da-330c4fb8a17d"
resource_type: "rule"
resource_name: "3_5_test_rule_immutability"
---
# 3.5: Test Rule Immutability

## Requirement

Test that critical rules are actually enforced on every API call and cannot be deprioritized.

## Acceptance Criteria

- [ ] Rules are enforced on 100% of API calls
- [ ] Rules cannot be ignored even in edge cases
- [ ] Rules work consistently across different tasks
- [ ] Immutability is verified through multiple tests

## Owner Stage

- **Testing**: Stage 0_07_testing

## Dependencies

- Requires: 3.4 (wrapper confirmed absent)
- Enables: O4 (full verification suite)

## Navigation

- **Parent need**: `PARENT_NEED_P3.md`
- **Previous sibling**: `3_4_confirm_no_discretionary_wrapper.md`
- **Next parent**: `../P4_create_execution_infrastructure/PARENT_NEED_P4.md`
