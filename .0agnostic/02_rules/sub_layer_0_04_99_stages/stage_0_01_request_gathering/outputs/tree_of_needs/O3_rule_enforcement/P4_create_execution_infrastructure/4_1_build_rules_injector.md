---
resource_id: "94d71d2a-c113-4505-b663-b731df0bed5a"
resource_type: "rule"
resource_name: "4_1_build_rules_injector"
---
# 4.1: Build Critical-Rules-Injector.js

<!-- section_id: "c8298ddc-f51e-4937-a87a-04c9a552316d" -->
## Requirement

Create Node.js module that extracts rules from CLAUDE.md hierarchy and prepares them for system prompt injection.

<!-- section_id: "91fda35d-420e-42e9-befe-45df37a50a2a" -->
## Acceptance Criteria

- [ ] Module implements rule extraction logic from O2
- [ ] Module formats rules for system prompt
- [ ] Module initializes Claude Code Agent SDK with enhanced prompt
- [ ] Module is well-documented with JSDoc
- [ ] Error handling for missing/malformed files
- [ ] Performance is acceptable (< 500ms startup overhead)

<!-- section_id: "c34c8ab9-2dbf-4be4-9aee-5572d18094ce" -->
## Owner Stage

- **Development**: Stage 0_06_development
- **Testing**: Stage 0_07_testing

<!-- section_id: "615f1d3a-cab9-470d-9c43-6d5e5eda67a9" -->
## Dependencies

- Requires: O2 completion (extraction logic), P3 completion (injection mechanism)
- Enables: 4.2 (wrapper script uses this module)

<!-- section_id: "6da1484f-1c98-4ad8-9618-853158eec44f" -->
## Navigation

- **Parent need**: `PARENT_NEED_P4.md`
- **Next sibling**: `4_2_create_wrapper_script.md`
