---
resource_id: "a6efa005-05a6-4762-92e5-5d1581ac276f"
resource_type: "rule"
resource_name: "3_1_format_rules_for_injection"
---
# 3.1: Format Rules for Injection

<!-- section_id: "ec4671c5-e964-4977-9e49-c7656585cc07" -->
## Requirement

Rules must be formatted correctly for injection into Claude Code's system prompt via Agent SDK.

<!-- section_id: "0bccf4a4-b3fd-4c0a-b304-2f5b94110a81" -->
## Acceptance Criteria

- [ ] Rules formatted as text block in system prompt
- [ ] Markdown structure is preserved
- [ ] Rule names and descriptions are clear
- [ ] No formatting conflicts with system prompt
- [ ] Injection format is documented

<!-- section_id: "06191e36-e91a-4f93-8f6a-4994b952daa5" -->
## Owner Stage

- **Design**: Stage 0_05_design
- **Development**: Stage 0_06_development

<!-- section_id: "c2254d66-f8af-4e5d-b58e-d88a538695a1" -->
## Dependencies

- Requires: O2 completion (rules exist)
- Enables: 3.2 (injection uses formatted rules)

<!-- section_id: "fc79cf19-50a5-4a48-9ed2-8f2bf5ce4f8b" -->
## Navigation

- **Parent need**: `PARENT_NEED_P3.md`
- **Next sibling**: `3_2_use_agent_sdk_initialization.md`
