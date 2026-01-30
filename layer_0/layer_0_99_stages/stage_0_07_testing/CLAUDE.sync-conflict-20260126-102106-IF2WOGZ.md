# Stage 05: Testing

## Purpose
Verify the implementation meets requirements. This stage performs systematic testing to identify defects and validate functionality.

## Entry Criteria
- Implementation received
- Unit tests passing
- Test environment available
- Test data prepared

## Exit Criteria
- All test cases executed
- Test results documented
- Defects logged and categorized
- Quality metrics collected
- Handoff prepared for Criticism

## Typical Tasks
- Execute test plans
- Perform integration testing
- Conduct regression testing
- Test edge cases
- Document test results
- Log defects with reproduction steps

## Handoffs
- **From Previous (04_development)**: IMPLEMENTATION
- **To Next (06_criticism)**: TEST_RESULTS with defects and metrics

## Directory Structure
```
stage_0_07_testing/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
└── hand_off_documents/   # Stage handoffs
```

## AI Agent Guidelines
When working in this stage:
- Test against requirements, not assumptions
- Document reproduction steps clearly
- Prioritize defects by severity
- Test boundary conditions
- Consider security and performance
- Maintain test coverage metrics
