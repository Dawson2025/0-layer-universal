---
resource_id: "0560c270-1825-4281-a035-ec2ba65dc699"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-102106-IF2WOGZ"
---
# Stage 05: Testing

<!-- section_id: "9fe2863a-9e2a-4697-ac97-7b738f7d886e" -->
## Purpose
Verify the implementation meets requirements. This stage performs systematic testing to identify defects and validate functionality.

<!-- section_id: "83986c26-a6a7-40d7-9bf2-0c53686a50a2" -->
## Entry Criteria
- Implementation received
- Unit tests passing
- Test environment available
- Test data prepared

<!-- section_id: "8b1b6722-64ff-4e9e-9961-84f92a7fa001" -->
## Exit Criteria
- All test cases executed
- Test results documented
- Defects logged and categorized
- Quality metrics collected
- Handoff prepared for Criticism

<!-- section_id: "c0aef398-97c3-41cb-80e4-ebafccd37e44" -->
## Typical Tasks
- Execute test plans
- Perform integration testing
- Conduct regression testing
- Test edge cases
- Document test results
- Log defects with reproduction steps

<!-- section_id: "8a5907ae-5400-4074-92c1-fe495ce47b36" -->
## Handoffs
- **From Previous (04_development)**: IMPLEMENTATION
- **To Next (06_criticism)**: TEST_RESULTS with defects and metrics

<!-- section_id: "0e74500b-a2bf-4369-a124-70b120ca394a" -->
## Directory Structure
```
stage_0_07_testing/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
└── hand_off_documents/   # Stage handoffs
```

<!-- section_id: "92c3ab29-bac2-4c1a-81ea-013c4abe4c46" -->
## AI Agent Guidelines
When working in this stage:
- Test against requirements, not assumptions
- Document reproduction steps clearly
- Prioritize defects by severity
- Test boundary conditions
- Consider security and performance
- Maintain test coverage metrics
