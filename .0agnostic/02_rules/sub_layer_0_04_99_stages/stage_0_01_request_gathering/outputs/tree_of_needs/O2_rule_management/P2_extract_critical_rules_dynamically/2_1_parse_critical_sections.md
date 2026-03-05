---
resource_id: "866a8377-79db-4854-884d-2ead14e9bd5c"
resource_type: "rule"
resource_name: "2_1_parse_critical_sections"
---
# 2.1: Parse [CRITICAL] Sections from CLAUDE.md

## Requirement

The system must reliably parse all `### [CRITICAL]` sections from CLAUDE.md files across the directory hierarchy.

## Acceptance Criteria

- [x] Regex pattern correctly identifies `### [CRITICAL]` section headers
- [x] Complete rule text is extracted (from header to next heading)
- [x] Multiple [CRITICAL] sections in one file are all found
- [x] Works across files in entire directory hierarchy
- [x] Preserves exact formatting and content
- [x] Handles edge cases (rules at end of file, nested content, etc.)

## Owner Stage

- **Instruction**: Stage 0_03_instructions (specify exact format)
- **Design**: Stage 0_05_design (design parser logic)
- **Development**: Stage 0_06_development (implement parser)

## Dependencies

- Requires: Parent need P2 context
- Enables: 2.2 (hierarchy handling)

## Navigation

- **Parent need**: `PARENT_NEED_P2.md`
- **Next sibling**: `2_2_handle_rule_hierarchy.md`
