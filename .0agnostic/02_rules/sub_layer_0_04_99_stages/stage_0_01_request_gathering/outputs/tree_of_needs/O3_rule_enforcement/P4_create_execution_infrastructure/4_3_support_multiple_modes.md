---
resource_id: "99d57221-ac2e-4c57-ad9f-6ea40df0a65b"
resource_type: "rule"
resource_name: "4_3_support_multiple_modes"
---
# 4.3: Support Multiple Execution Modes

<!-- section_id: "8879483d-25f1-4906-a12b-c3a20ccb20bf" -->
## Requirement

Wrapper and injector must work in both interactive CLI mode and script mode.

<!-- section_id: "c823ef62-0f7a-4b68-b1fd-72f41383c75b" -->
## Acceptance Criteria

- [ ] Works when run interactively: `cc [args]`
- [ ] Works when called from scripts: `claude-code-with-critical-rules.sh [args]`
- [ ] Works in Claude Code Agent SDK context
- [ ] Detects mode automatically
- [ ] Behavior is consistent across modes

<!-- section_id: "864a9338-464a-4de2-beff-05d7e25410f9" -->
## Owner Stage

- **Development**: Stage 0_06_development
- **Testing**: Stage 0_07_testing

<!-- section_id: "a7f7f542-0019-4f95-a9d7-3ffcf6a7abc7" -->
## Dependencies

- Requires: 4.2 (wrapper script)
- Enables: 4.4 (aliases depend on this)

<!-- section_id: "d95bbbd9-b8e8-45d3-b129-ec5f0470a6ec" -->
## Navigation

- **Parent need**: `PARENT_NEED_P4.md`
- **Previous sibling**: `4_2_create_wrapper_script.md`
- **Next sibling**: `4_4_add_shell_aliases.md`
