---
resource_id: "446be2a7-bf0d-4ff4-9505-2913cc7c9f07"
resource_type: "rule"
resource_name: "2_3_validate_rule_syntax"
---
# 2.3: Validate Rule Syntax and Structure

<!-- section_id: "cfeb2544-40f1-4b5d-b097-b73c00f82b33" -->
## Requirement

Rules must be validated for correct syntax and structure before being injected into the system prompt.

<!-- section_id: "a561a219-79ed-4982-8ad2-591dcc08f04f" -->
## Acceptance Criteria

- [ ] Rules have required elements (ID, name, description)
- [ ] Rule text is properly formatted
- [ ] Invalid rules are rejected with clear error messages
- [ ] Validation errors prevent injection
- [ ] Warnings are issued for malformed but usable rules
- [ ] Validation rules are documented

<!-- section_id: "b4ef715b-7da6-4ba1-a89b-ec3ec6730d40" -->
## Validation Rules

- Rules must have markdown heading (### [CRITICAL] Name)
- Rules must have content (not empty)
- Rule text must be valid markdown
- Reserved characters are escaped properly
- No circular dependencies between rules

<!-- section_id: "d36e58f3-133c-41b8-9605-b9ac949987a6" -->
## Owner Stage

- **Instruction**: Stage 0_03_instructions (specify validation rules)
- **Design**: Stage 0_05_design (validation logic)
- **Development**: Stage 0_06_development (implement)

<!-- section_id: "513bbeb1-dd59-4672-b4b9-0d111e941445" -->
## Dependencies

- Requires: 2.2 (hierarchy handled)
- Enables: 2.4 (caching only valid rules)

<!-- section_id: "46d049de-5bc7-4421-8852-70e20b743de5" -->
## Navigation

- **Parent need**: `PARENT_NEED_P2.md`
- **Previous sibling**: `2_2_handle_rule_hierarchy.md`
- **Next sibling**: `2_4_cache_rules_for_performance.md`
