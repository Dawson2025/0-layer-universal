# 4.1: Build Critical-Rules-Injector.js

## Requirement

Create Node.js module that extracts rules from CLAUDE.md hierarchy and prepares them for system prompt injection.

## Acceptance Criteria

- [ ] Module implements rule extraction logic from O2
- [ ] Module formats rules for system prompt
- [ ] Module initializes Claude Code Agent SDK with enhanced prompt
- [ ] Module is well-documented with JSDoc
- [ ] Error handling for missing/malformed files
- [ ] Performance is acceptable (< 500ms startup overhead)

## Owner Stage

- **Development**: Stage 0_06_development
- **Testing**: Stage 0_07_testing

## Dependencies

- Requires: O2 completion (extraction logic), P3 completion (injection mechanism)
- Enables: 4.2 (wrapper script uses this module)

## Navigation

- **Parent need**: `PARENT_NEED_P4.md`
- **Next sibling**: `4_2_create_wrapper_script.md`
