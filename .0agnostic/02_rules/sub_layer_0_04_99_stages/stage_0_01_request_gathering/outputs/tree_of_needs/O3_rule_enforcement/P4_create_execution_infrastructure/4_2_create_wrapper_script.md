---
resource_id: "69951c9d-11bc-46dc-a3a3-7d620e64531a"
resource_type: "rule"
resource_name: "4_2_create_wrapper_script"
---
# 4.2: Create Wrapper Script

<!-- section_id: "a4d8545c-8b78-49de-b676-1e166fb4baa1" -->
## Requirement

Create bash/shell wrapper script (`claude-code-with-critical-rules.sh`) that runs the injector before launching Claude Code.

<!-- section_id: "2501d96e-3803-4224-a03d-b7e1332ebd18" -->
## Acceptance Criteria

- [ ] Script detects current working directory
- [ ] Script calls critical-rules-injector.js
- [ ] Script passes all arguments to Claude Code
- [ ] Script handles errors gracefully
- [ ] Works in both bash and zsh
- [ ] Can be run from any directory

<!-- section_id: "7ec31b7b-bb1c-4a01-af37-c98e6e76342a" -->
## Owner Stage

- **Development**: Stage 0_06_development
- **Testing**: Stage 0_07_testing

<!-- section_id: "e2ec5801-b45c-4714-be5b-5121ce257d04" -->
## Dependencies

- Requires: 4.1 (injector module)
- Enables: 4.3 (multiple execution modes)

<!-- section_id: "ad6489f0-41a6-4376-89e1-70d2b60f5f19" -->
## Navigation

- **Parent need**: `PARENT_NEED_P4.md`
- **Previous sibling**: `4_1_build_rules_injector.md`
- **Next sibling**: `4_3_support_multiple_modes.md`
