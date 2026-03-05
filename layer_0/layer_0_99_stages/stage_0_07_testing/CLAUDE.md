<!-- derived_from: "aa24709f-a54e-43db-ac3b-f2b61b2bbaac" -->
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

### Outputs Organization (by_purpose pattern)

All test outputs MUST follow this numbered scaffolding structure:

```
outputs/
└── by_purpose/
    └── {test_purpose}/                    # e.g., "daemon_persistence_restart_fix"
        ├── 01_design/                     # Test design & methodology
        │   ├── 00_overview.md
        │   └── [design docs].md
        ├── 02_implementation/             # Test implementation & setup scripts
        │   ├── solution_1/
        │   │   ├── test_setup.sh
        │   │   └── [setup docs].md
        │   ├── solution_2/
        │   ├── solution_3/
        │   └── validate-all-solutions.sh
        ├── 03_runs/                       # Test execution logs
        │   ├── sol_1_run_TIMESTAMP.log
        │   ├── sol_2_run_TIMESTAMP.log
        │   └── sol_3_run_TIMESTAMP.log
        ├── 04_results/                    # Test results & findings
        │   ├── solution_1_results.md
        │   ├── solution_2_results.md
        │   └── solution_3_results.md
        └── 05_insights/                   # Analysis & lessons learned
            └── [analysis].md
```

### Standard Stage Layout
```
stage_0_07_testing/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
├── hand_off_documents/   # Stage handoffs
└── outputs/              # Test outputs (REQUIRED)
    └── by_purpose/       # Organized by test purpose (REQUIRED)
```

## Test Output Scaffolding (MANDATORY)

Every test purpose MUST create the 5-directory structure:
1. **01_design/** — Test methodology, design decisions, approach documentation
2. **02_implementation/** — Test setup scripts, implementation details, how to run tests
3. **03_runs/** — Execution logs, stdout/stderr from test runs, timestamps
4. **04_results/** — Test result summaries, pass/fail status, metrics
5. **05_insights/** — Analysis, lessons learned, recommendations, root cause analysis

**Numbering serves two purposes:**
- Shows progression through the testing workflow
- Makes it easy to find outputs (everything is under `by_purpose/[test_name]/`)

For multiple test solutions (as in daemon_persistence example):
- `02_implementation/` contains `solution_1/`, `solution_2/`, `solution_3/` subdirectories
- `04_results/` has separate result docs for each solution
- `05_insights/` provides comparative analysis

## AI Agent Guidelines
When working in this stage:
- **Always create the 5-directory scaffolding** for any test outputs (01_design → 05_insights)
- Organize tests by purpose, not by solution or approach
- Test against requirements, not assumptions
- Document reproduction steps clearly
- Prioritize defects by severity
- Test boundary conditions
- Consider security and performance
- Maintain test coverage metrics
- Number subdirectories (01_, 02_, 03_...) to show workflow progression
