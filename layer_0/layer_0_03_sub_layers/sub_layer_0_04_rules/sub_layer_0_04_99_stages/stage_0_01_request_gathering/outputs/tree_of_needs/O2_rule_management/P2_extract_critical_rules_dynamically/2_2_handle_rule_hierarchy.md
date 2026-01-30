# 2.2: Handle Rule Hierarchy and Inheritance

## Requirement

The system must respect rule hierarchy where child CLAUDE.md files can override parent rules marked as [CRITICAL].

## Acceptance Criteria

- [ ] Parent rules from root CLAUDE.md are identified
- [ ] Child rules from project CLAUDE.md are identified
- [ ] When same rule [CRITICAL] tag appears in both, child version is used
- [ ] Rule override logic is documented
- [ ] No data loss when rules are overridden
- [ ] Previous versions of overridden rules are accessible

## Hierarchy Order

```
/home/dawson/CLAUDE.md (parent)
├── /home/dawson/.claude/CLAUDE.md (parent)
├── /home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md
├── /home/dawson/dawson-workspace/code/0_layer_universal/layer_0/CLAUDE.md
└── /home/dawson/[working_directory]/CLAUDE.md (child - overrides all above)
```

## Owner Stage

- **Instruction**: Stage 0_03_instructions (define override rules)
- **Design**: Stage 0_05_design (architecture for hierarchy handling)
- **Development**: Stage 0_06_development (implement)

## Dependencies

- Requires: 2.1 (rules are parsed)
- Enables: 2.3 (validation must account for overrides)

## Navigation

- **Parent need**: `PARENT_NEED_P2.md`
- **Previous sibling**: `2_1_parse_critical_sections.md`
- **Next sibling**: `2_3_validate_rule_syntax.md`
