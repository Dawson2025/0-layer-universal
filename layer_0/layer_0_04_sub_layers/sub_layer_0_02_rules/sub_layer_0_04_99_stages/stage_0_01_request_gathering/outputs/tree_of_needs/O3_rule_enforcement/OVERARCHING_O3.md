# O3: RULE ENFORCEMENT

## Strategic Question

**How are critical rules guaranteed to execute?**

## Purpose

This overarching branch addresses how critical rules are injected into the system prompt and how the execution infrastructure ensures they're applied on every API call.

## What This Branch Covers

- Formatting rules for system prompt injection
- Using Agent SDK to initialize Claude Code with enhanced prompt
- Verifying rules appear in actual system prompt
- Confirming rules have no discretionary wrapper
- Testing that rules work correctly
- Building the infrastructure (scripts, modules)
- Supporting multiple execution modes
- Installation and setup

## Parent Tactical Needs

**P3: Inject Rules into System Prompt**
- Technical mechanism for getting rules into system prompt

**P4: Create Execution Infrastructure**
- Scripts and tools for users to run Claude Code with critical rules

## Strategic Value

Rules mean nothing if they're not actually injected and enforced. This branch ensures:
- Rules get into the system prompt correctly
- The discretionary wrapper is bypassed
- Rules are tested to actually work
- Users have convenient way to run enhanced Claude Code

## Child Needs Summary

**P3 (Injection)**:
- 3.1: Format rules for injection
- 3.2: Use Agent SDK initialization
- 3.3: Verify rules in system prompt
- 3.4: Confirm no discretionary wrapper
- 3.5: Test rule immutability

**P4 (Infrastructure)**:
- 4.1: Build critical-rules-injector.js
- 4.2: Create wrapper script
- 4.3: Support multiple modes
- 4.4: Add shell aliases
- 4.5: Create installation guide

## Acceptance Criteria

This branch is complete when:
- Rules are reliably injected into system prompt
- Discretionary wrapper is confirmed absent
- Execution infrastructure is built and tested
- Rules work correctly on every API call
- Users can easily run enhanced Claude Code

## Dependencies

- Depends on: O2 completion (have rules to inject)
- Enables: O4 (verification of enforcement)

## Cross-References

- Parent need P3: `P3_inject_rules_into_system_prompt/PARENT_NEED_P3.md`
- Parent need P4: `P4_create_execution_infrastructure/PARENT_NEED_P4.md`
- Previous branch: `../O2_rule_management/OVERARCHING_O2.md`
- Next branch: `../O4_rule_verification_and_compliance/OVERARCHING_O4.md`

## Navigation

- **Root need**: `../root_need/ROOT_NEED_enforce_critical_rules.md`
- **Parent need P3**: `P3_inject_rules_into_system_prompt/PARENT_NEED_P3.md`
- **Parent need P4**: `P4_create_execution_infrastructure/PARENT_NEED_P4.md`
- **Child needs**: Individual files in both P3 and P4 directories
- **Previous branch**: `../O2_rule_management/OVERARCHING_O2.md`
- **Next branch**: `../O4_rule_verification_and_compliance/OVERARCHING_O4.md`
