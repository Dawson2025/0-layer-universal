---
resource_id: "edc0b547-c522-45f6-9414-618dce4ea679"
resource_type: "rule"
resource_name: "PARENT_NEED_P3"
---
# P3: INJECT RULES INTO SYSTEM PROMPT

<!-- section_id: "11ad775f-67b9-4444-a030-d62f958d6734" -->
## Tactical Objective

**Get critical rules into the actual Claude Code system prompt using Agent SDK.**

<!-- section_id: "dc7a9161-dd6a-43ca-b0ee-81ee9b53bd9b" -->
## Context

Rules extracted by O2 must now be injected into the system prompt where they cannot be wrapped by discretionary disclaimer. This is the technical heart of the solution.

<!-- section_id: "f625d4a5-805e-438c-b307-5b8bb35d9b38" -->
## Parent Overarching Need

**O3: Rule Enforcement** - Ensuring rules execute reliably

<!-- section_id: "54513d9a-5c13-4003-9b5b-2855b20ca031" -->
## Child Needs

| ID | Need | Description |
|----|------|-------------|
| 3.1 | Format rules for injection | Prepare rules in format suitable for system prompt |
| 3.2 | Use Agent SDK initialization | Use `systemPrompt` + `append: true` pattern |
| 3.3 | Verify rules in system prompt | Confirm rules appear in actual system prompt |
| 3.4 | Confirm no discretionary wrapper | Verify rules NOT wrapped by disclaimer |
| 3.5 | Test rule immutability | Verify rules are enforced on every API call |

<!-- section_id: "215a1c10-d422-445a-bb03-57a602589bf9" -->
## Acceptance Criteria (Need Satisfied When)

- [ ] Rules formatted for system prompt injection
- [ ] Agent SDK initialization works with custom systemPrompt
- [ ] Rules appear in actual system prompt (verified)
- [ ] No discretionary disclaimer wraps critical rules
- [ ] Rules execute reliably on every API call
- [ ] Rule immutability is confirmed through testing

<!-- section_id: "301d75e5-45bf-48d9-9627-96a48cf7f665" -->
## Dependencies

<!-- section_id: "2e96e322-85bf-4c5c-9519-2e00483be0e8" -->
### Requires
- O2 completion (extracted rules available)
- O1 completion (understand the approach)
- Agent SDK documentation

<!-- section_id: "d1dca368-d7fd-4471-b13d-8b3fb4c9693c" -->
### Enables
- P4 (infrastructure uses this injection mechanism)
- O4 (verification tests this mechanism)

<!-- section_id: "461c5a71-3040-46f4-8eba-32aeab5b572a" -->
## Success Metrics

This parent need succeeds when:
1. **Injection Works**: Rules appear in system prompt
2. **No Wrapper**: Discretionary disclaimer is confirmed absent
3. **Reliable**: Rules work on 100% of API calls
4. **Testable**: Injection can be verified and debugged
5. **Documented**: How injection works is documented

<!-- section_id: "65b76981-c5eb-4de4-bea7-4e82dbc22f43" -->
## Cross-References

- Overarching need: `../OVERARCHING_O3.md`
- Root need: `../../root_need/ROOT_NEED_enforce_critical_rules.md`
- Related parent: `../P4_create_execution_infrastructure/PARENT_NEED_P4.md`

<!-- section_id: "ae15b39b-7761-4853-92a5-0d7dbebfe34b" -->
## Navigation

- **Overarching need**: `../OVERARCHING_O3.md`
- **Child need 3.1**: `3_1_format_rules_for_injection.md`
- **Child need 3.2**: `3_2_use_agent_sdk_initialization.md`
- **Child need 3.3**: `3_3_verify_rules_in_system_prompt.md`
- **Child need 3.4**: `3_4_confirm_no_discretionary_wrapper.md`
- **Child need 3.5**: `3_5_test_rule_immutability.md`
- **Parent sibling P4**: `../P4_create_execution_infrastructure/PARENT_NEED_P4.md`
