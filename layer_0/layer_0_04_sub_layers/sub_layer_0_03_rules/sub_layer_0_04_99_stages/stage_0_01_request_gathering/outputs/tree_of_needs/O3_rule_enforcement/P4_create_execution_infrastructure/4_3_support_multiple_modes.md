# 4.3: Support Multiple Execution Modes

## Requirement

Wrapper and injector must work in both interactive CLI mode and script mode.

## Acceptance Criteria

- [ ] Works when run interactively: `cc [args]`
- [ ] Works when called from scripts: `claude-code-with-critical-rules.sh [args]`
- [ ] Works in Claude Code Agent SDK context
- [ ] Detects mode automatically
- [ ] Behavior is consistent across modes

## Owner Stage

- **Development**: Stage 0_06_development
- **Testing**: Stage 0_07_testing

## Dependencies

- Requires: 4.2 (wrapper script)
- Enables: 4.4 (aliases depend on this)

## Navigation

- **Parent need**: `PARENT_NEED_P4.md`
- **Previous sibling**: `4_2_create_wrapper_script.md`
- **Next sibling**: `4_4_add_shell_aliases.md`
