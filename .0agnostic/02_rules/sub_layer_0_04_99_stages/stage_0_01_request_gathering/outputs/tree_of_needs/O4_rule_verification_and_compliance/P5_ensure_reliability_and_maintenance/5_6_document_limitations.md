---
resource_id: "341a41d2-022f-4622-8222-c28398a08534"
resource_type: "rule"
resource_name: "5_6_document_limitations"
---
# 5.6: Document Limitations

## Requirement

Clearly document what the critical rules system can and cannot do, and any known limitations.

## Acceptance Criteria

- [ ] All limitations are listed
- [ ] Rationale for each limitation is explained
- [ ] Workarounds (if any) are documented
- [ ] Future enhancements are noted
- [ ] Users understand scope boundaries

## Expected Limitations

- Works with Agent SDK (not direct CLI in some scenarios)
- Requires Node.js installed
- Rules persist only within a session
- Cannot override rules marked as [CRITICAL] (by design)
- Depends on Anthropic maintaining Agent SDK API

## Owner Stage

- **Documentation**: Stage 0_10_current_product

## Dependencies

- Requires: O4 completion (system is complete)
- Final documentation task

## Navigation

- **Parent need**: `PARENT_NEED_P5.md`
- **Previous sibling**: `5_5_create_upgrade_procedure.md`
- **Complete**: All needs documented!
