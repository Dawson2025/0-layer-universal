# P3: INJECT RULES INTO SYSTEM PROMPT

## Tactical Objective

**Get critical rules into the actual Claude Code system prompt using Agent SDK.**

## Context

Rules extracted by O2 must now be injected into the system prompt where they cannot be wrapped by discretionary disclaimer. This is the technical heart of the solution.

## Parent Overarching Need

**O3: Rule Enforcement** - Ensuring rules execute reliably

## Child Needs

| ID | Need | Description |
|----|------|-------------|
| 3.1 | Format rules for injection | Prepare rules in format suitable for system prompt |
| 3.2 | Use Agent SDK initialization | Use `systemPrompt` + `append: true` pattern |
| 3.3 | Verify rules in system prompt | Confirm rules appear in actual system prompt |
| 3.4 | Confirm no discretionary wrapper | Verify rules NOT wrapped by disclaimer |
| 3.5 | Test rule immutability | Verify rules are enforced on every API call |

## Acceptance Criteria (Need Satisfied When)

- [ ] Rules formatted for system prompt injection
- [ ] Agent SDK initialization works with custom systemPrompt
- [ ] Rules appear in actual system prompt (verified)
- [ ] No discretionary disclaimer wraps critical rules
- [ ] Rules execute reliably on every API call
- [ ] Rule immutability is confirmed through testing

## Dependencies

### Requires
- O2 completion (extracted rules available)
- O1 completion (understand the approach)
- Agent SDK documentation

### Enables
- P4 (infrastructure uses this injection mechanism)
- O4 (verification tests this mechanism)

## Success Metrics

This parent need succeeds when:
1. **Injection Works**: Rules appear in system prompt
2. **No Wrapper**: Discretionary disclaimer is confirmed absent
3. **Reliable**: Rules work on 100% of API calls
4. **Testable**: Injection can be verified and debugged
5. **Documented**: How injection works is documented

## Cross-References

- Overarching need: `../OVERARCHING_O3.md`
- Root need: `../../root_need/ROOT_NEED_enforce_critical_rules.md`
- Related parent: `../P4_create_execution_infrastructure/PARENT_NEED_P4.md`

## Navigation

- **Overarching need**: `../OVERARCHING_O3.md`
- **Child need 3.1**: `3_1_format_rules_for_injection.md`
- **Child need 3.2**: `3_2_use_agent_sdk_initialization.md`
- **Child need 3.3**: `3_3_verify_rules_in_system_prompt.md`
- **Child need 3.4**: `3_4_confirm_no_discretionary_wrapper.md`
- **Child need 3.5**: `3_5_test_rule_immutability.md`
- **Parent sibling P4**: `../P4_create_execution_infrastructure/PARENT_NEED_P4.md`
