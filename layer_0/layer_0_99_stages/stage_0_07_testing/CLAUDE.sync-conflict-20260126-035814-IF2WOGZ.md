---
resource_id: "72550690-dd1d-4459-a509-95e70e82f6d7"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-035814-IF2WOGZ"
---
# Stage 05: Testing

<!-- section_id: "7e0c5b74-cd97-4ba1-b6ce-a56e67ea99ab" -->
## Purpose
Verify the implementation meets requirements. This stage performs systematic testing to identify defects and validate functionality.

<!-- section_id: "88680e18-ca50-429e-8e5f-d3a70834cca3" -->
## Entry Criteria
- Implementation received
- Unit tests passing
- Test environment available
- Test data prepared

<!-- section_id: "fd2846f0-a021-4595-b6f5-510e8157b15f" -->
## Exit Criteria
- All test cases executed
- Test results documented
- Defects logged and categorized
- Quality metrics collected
- Handoff prepared for Criticism

<!-- section_id: "81e8507a-556f-4784-bddc-8f067d05604c" -->
## Typical Tasks
- Execute test plans
- Perform integration testing
- Conduct regression testing
- Test edge cases
- Document test results
- Log defects with reproduction steps

<!-- section_id: "286b466a-6731-49e5-9da2-3c5677c5b84c" -->
## Handoffs
- **From Previous (04_development)**: IMPLEMENTATION
- **To Next (06_criticism)**: TEST_RESULTS with defects and metrics

<!-- section_id: "fb17c27f-dd06-477a-8c9c-d3fee888866f" -->
## Directory Structure
```
stage_0_07_testing/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
└── hand_off_documents/   # Stage handoffs
```

<!-- section_id: "3b42ecd7-d0cc-460a-b969-b57564fab352" -->
## AI Agent Guidelines
When working in this stage:
- Test against requirements, not assumptions
- Document reproduction steps clearly
- Prioritize defects by severity
- Test boundary conditions
- Consider security and performance
- Maintain test coverage metrics
