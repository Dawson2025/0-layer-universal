---
resource_id: "06117fc9-9bc0-486f-98a3-3b1e90e45fc3"
resource_type: "rule"
resource_name: "2_2_handle_rule_hierarchy"
---
# 2.2: Handle Rule Hierarchy and Inheritance

<!-- section_id: "9e1fa11a-374c-4a48-9890-0f2968e0a50c" -->
## Requirement

The system must respect rule hierarchy where child CLAUDE.md files can override parent rules marked as [CRITICAL].

<!-- section_id: "54e96200-e98a-4f7b-b039-f91e131c7736" -->
## Acceptance Criteria

- [ ] Parent rules from root CLAUDE.md are identified
- [ ] Child rules from project CLAUDE.md are identified
- [ ] When same rule [CRITICAL] tag appears in both, child version is used
- [ ] Rule override logic is documented
- [ ] No data loss when rules are overridden
- [ ] Previous versions of overridden rules are accessible

<!-- section_id: "56d1409d-5880-41ca-b4c7-d4078eba8e3c" -->
## Hierarchy Order

```
/home/dawson/CLAUDE.md (parent)
├── /home/dawson/.claude/CLAUDE.md (parent)
├── /home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md
├── /home/dawson/dawson-workspace/code/0_layer_universal/layer_0/CLAUDE.md
└── /home/dawson/[working_directory]/CLAUDE.md (child - overrides all above)
```

<!-- section_id: "c1f43ee6-dfc0-4f74-a3b0-dcc40e8d0324" -->
## Owner Stage

- **Instruction**: Stage 0_03_instructions (define override rules)
- **Design**: Stage 0_05_design (architecture for hierarchy handling)
- **Development**: Stage 0_06_development (implement)

<!-- section_id: "fe1dacc1-c759-4eff-aa76-55e02819535a" -->
## Dependencies

- Requires: 2.1 (rules are parsed)
- Enables: 2.3 (validation must account for overrides)

<!-- section_id: "40334263-59ac-44ca-adda-9d8a457bf83a" -->
## Navigation

- **Parent need**: `PARENT_NEED_P2.md`
- **Previous sibling**: `2_1_parse_critical_sections.md`
- **Next sibling**: `2_3_validate_rule_syntax.md`
