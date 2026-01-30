# 4.2: Create Wrapper Script

## Requirement

Create bash/shell wrapper script (`claude-code-with-critical-rules.sh`) that runs the injector before launching Claude Code.

## Acceptance Criteria

- [ ] Script detects current working directory
- [ ] Script calls critical-rules-injector.js
- [ ] Script passes all arguments to Claude Code
- [ ] Script handles errors gracefully
- [ ] Works in both bash and zsh
- [ ] Can be run from any directory

## Owner Stage

- **Development**: Stage 0_06_development
- **Testing**: Stage 0_07_testing

## Dependencies

- Requires: 4.1 (injector module)
- Enables: 4.3 (multiple execution modes)

## Navigation

- **Parent need**: `PARENT_NEED_P4.md`
- **Previous sibling**: `4_1_build_rules_injector.md`
- **Next sibling**: `4_3_support_multiple_modes.md`
