---
resource_id: "ab8b5634-7f5c-4a2a-a6f7-f46da87a227b"
resource_type: "rule"
resource_name: "3_4_confirm_no_discretionary_wrapper"
---
# 3.4: Confirm No Discretionary Wrapper

<!-- section_id: "619597c5-083f-4b84-8150-3f2286dcdfab" -->
## Requirement

Verify that critical rules in system prompt are NOT wrapped by discretionary disclaimer.

<!-- section_id: "d032d261-29bc-4868-ba29-81ca1de8cdf3" -->
## Acceptance Criteria

- [ ] Rules do not appear with discretionary wrapper text
- [ ] Rules are in system prompt (not foundational context)
- [ ] Absence of wrapper is confirmed through inspection
- [ ] Testing confirms rules are mandatory (not optional)

<!-- section_id: "cef49f69-57bf-4e61-b36a-104abb2f78b3" -->
## Owner Stage

- **Testing**: Stage 0_07_testing (verify this critical property)

<!-- section_id: "fb405117-5dbf-4ca7-a2dd-e4e8466af8a8" -->
## Dependencies

- Requires: 3.3 (can see what's in system prompt)
- Enables: 3.5 (test actual enforcement)

<!-- section_id: "6637feb9-f900-4da4-96c5-02f23e260f95" -->
## Navigation

- **Parent need**: `PARENT_NEED_P3.md`
- **Previous sibling**: `3_3_verify_rules_in_system_prompt.md`
- **Next sibling**: `3_5_test_rule_immutability.md`
