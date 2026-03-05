---
resource_id: "866a8377-79db-4854-884d-2ead14e9bd5c"
resource_type: "rule"
resource_name: "2_1_parse_critical_sections"
---
# 2.1: Parse [CRITICAL] Sections from CLAUDE.md

<!-- section_id: "5a972c5f-4151-4ee9-85d4-e9b2bc0a088a" -->
## Requirement

The system must reliably parse all `### [CRITICAL]` sections from CLAUDE.md files across the directory hierarchy.

<!-- section_id: "a9f24f2c-8857-4355-8a0d-eb9dd8543e17" -->
## Acceptance Criteria

- [x] Regex pattern correctly identifies `### [CRITICAL]` section headers
- [x] Complete rule text is extracted (from header to next heading)
- [x] Multiple [CRITICAL] sections in one file are all found
- [x] Works across files in entire directory hierarchy
- [x] Preserves exact formatting and content
- [x] Handles edge cases (rules at end of file, nested content, etc.)

<!-- section_id: "16ac6eaf-2b7b-4f08-8eb9-5c0942c36229" -->
## Owner Stage

- **Instruction**: Stage 0_03_instructions (specify exact format)
- **Design**: Stage 0_05_design (design parser logic)
- **Development**: Stage 0_06_development (implement parser)

<!-- section_id: "07d20bfe-84e5-4241-b336-c4a8d2a2a400" -->
## Dependencies

- Requires: Parent need P2 context
- Enables: 2.2 (hierarchy handling)

<!-- section_id: "03f85f94-1c26-4586-af63-0c889b52e251" -->
## Navigation

- **Parent need**: `PARENT_NEED_P2.md`
- **Next sibling**: `2_2_handle_rule_hierarchy.md`
