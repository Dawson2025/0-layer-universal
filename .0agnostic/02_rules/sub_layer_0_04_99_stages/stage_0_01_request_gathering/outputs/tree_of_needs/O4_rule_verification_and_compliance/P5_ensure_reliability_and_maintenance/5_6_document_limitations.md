---
resource_id: "341a41d2-022f-4622-8222-c28398a08534"
resource_type: "rule"
resource_name: "5_6_document_limitations"
---
# 5.6: Document Limitations

<!-- section_id: "22989b98-3652-4fcf-9f9d-96dc4cb6a343" -->
## Requirement

Clearly document what the critical rules system can and cannot do, and any known limitations.

<!-- section_id: "7f3e9a10-5cf0-4f99-83cc-b532f91a1bc7" -->
## Acceptance Criteria

- [ ] All limitations are listed
- [ ] Rationale for each limitation is explained
- [ ] Workarounds (if any) are documented
- [ ] Future enhancements are noted
- [ ] Users understand scope boundaries

<!-- section_id: "de91bbbd-8562-4f6e-b7d7-070500552905" -->
## Expected Limitations

- Works with Agent SDK (not direct CLI in some scenarios)
- Requires Node.js installed
- Rules persist only within a session
- Cannot override rules marked as [CRITICAL] (by design)
- Depends on Anthropic maintaining Agent SDK API

<!-- section_id: "f42b2d68-2c3a-46a2-bf75-cb46f08eb8b4" -->
## Owner Stage

- **Documentation**: Stage 0_10_current_product

<!-- section_id: "33a97278-c42b-4ff9-8d68-e70a05d8563d" -->
## Dependencies

- Requires: O4 completion (system is complete)
- Final documentation task

<!-- section_id: "c6ebadc1-3d42-44ca-baf1-117422ae2a53" -->
## Navigation

- **Parent need**: `PARENT_NEED_P5.md`
- **Previous sibling**: `5_5_create_upgrade_procedure.md`
- **Complete**: All needs documented!
