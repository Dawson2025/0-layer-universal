---
resource_id: "102ff7f6-f349-4a07-bfb6-457c4ec9587f"
resource_type: "rule"
resource_name: "PARENT_NEED_P2"
---
# P2: EXTRACT CRITICAL RULES DYNAMICALLY

<!-- section_id: "7c90768c-0a7d-49be-8096-e3dbff345781" -->
## Tactical Objective

**Automatically discover, parse, and manage critical rules from the CLAUDE.md file hierarchy.**

<!-- section_id: "eb886113-256e-4c8d-97c7-4ee752502418" -->
## Context

Rules are defined in CLAUDE.md files using [CRITICAL] tags. The system must be able to:
- Find all [CRITICAL] sections across the directory hierarchy
- Extract the complete rule text
- Handle rule inheritance and overrides
- Validate syntax
- Cache for performance
- Support versioning

<!-- section_id: "33c828f4-8d3c-442b-95f6-626f34302587" -->
## Parent Overarching Need

**O2: Rule Management** - How rules are stored, extracted, and managed

<!-- section_id: "3ff919da-965c-4454-a985-61ca49cc6854" -->
## Child Needs

| ID | Need | Description |
|----|------|-------------|
| 2.1 | Parse [CRITICAL] sections | Extract all [CRITICAL] rule sections from CLAUDE.md files |
| 2.2 | Handle rule hierarchy | Support parent/child rule relationships and overrides |
| 2.3 | Validate rule syntax | Ensure rules are well-formed and usable |
| 2.4 | Cache rules | Store extracted rules for performance |
| 2.5 | Support versioning | Allow rules to change between sessions |

<!-- section_id: "bdda893c-aa75-4a52-a856-c133851ff47d" -->
## Acceptance Criteria (Need Satisfied When)

- [ ] Rules can be reliably extracted from CLAUDE.md files
- [ ] All [CRITICAL] sections in hierarchy are found
- [ ] Rule text is correctly parsed and preserved
- [ ] Child rules can override parent rules
- [ ] Rules are validated before caching
- [ ] Caching improves performance measurably
- [ ] Rules can be updated by changing CLAUDE.md
- [ ] Cache invalidation works when rules change

<!-- section_id: "98ea9e02-d59a-4dfc-8a8d-05ba1096e033" -->
## Dependencies

<!-- section_id: "74d20472-3ef6-43aa-ad58-48f14f3ee940" -->
### Requires
- O1 completion (understanding the approach)
- CLAUDE.md files marked with [CRITICAL] tags
- Specification of rule format/syntax

<!-- section_id: "a2257404-5809-4a1b-a6f0-4a806dae9268" -->
### Enables
- O3: Rule Enforcement (has rules to inject)
- O4: Rule Verification (can verify extracted rules)

<!-- section_id: "7824f69f-bcc4-4d89-b6d7-97174dee2fb6" -->
## Success Metrics

This parent need succeeds when:
1. **Extraction**: 100% of [CRITICAL] rules are found and extracted
2. **Accuracy**: Extracted rules match original text exactly
3. **Hierarchy**: Parent/child relationships are respected
4. **Performance**: Caching provides measurable speedup
5. **Validation**: Invalid rules are caught before injection
6. **Versioning**: Rule updates are reflected on next session

<!-- section_id: "ee8ebe7c-0511-465f-9e2c-0d77e5a8b821" -->
## Cross-References

- Overarching need: `../OVERARCHING_O2.md`
- Root need: `../../root_need/ROOT_NEED_enforce_critical_rules.md`
- Implementation: Will inform O3 injection design

<!-- section_id: "5f405625-d2b5-4059-a43d-1dd50070b4fa" -->
## Navigation

- **Overarching need**: `../OVERARCHING_O2.md`
- **Child need 2.1**: `2_1_parse_critical_sections.md`
- **Child need 2.2**: `2_2_handle_rule_hierarchy.md`
- **Child need 2.3**: `2_3_validate_rule_syntax.md`
- **Child need 2.4**: `2_4_cache_rules_for_performance.md`
- **Child need 2.5**: `2_5_support_rule_versioning.md`
