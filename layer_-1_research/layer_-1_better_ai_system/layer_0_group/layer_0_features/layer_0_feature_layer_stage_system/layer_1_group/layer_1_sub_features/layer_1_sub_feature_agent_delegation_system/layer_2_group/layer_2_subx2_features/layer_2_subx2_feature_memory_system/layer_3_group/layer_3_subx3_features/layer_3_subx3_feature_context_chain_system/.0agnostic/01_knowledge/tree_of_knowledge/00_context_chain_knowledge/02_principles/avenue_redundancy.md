# Principle: Avenue Redundancy

## Summary

Critical context must be reachable through at least 3 independent avenues. No single point of failure should prevent an agent from accessing essential information. This is a reliability principle -- AI agents operate in unpredictable conditions where CLAUDE.md might not be in the cascade path, a .gab.jsonld might fail to parse, or episodic memory might be empty.

The 8 avenues each operate through different mechanisms (filesystem walk, directory matching, skill invocation, jq query, manual file read), so a failure in one does not cascade. The minimum coverage targets are: 3+ avenues for entity identity and applicable rules, 2+ for available skills and mode constraints, and 1 for session history (episodic memory is the sole avenue, acceptable since it is not critical for first sessions).

Avenue coverage is tested by `test_avenue_coverage_functional.sh`, which checks each avenue for functional content and reports PASS / SCAFFOLDED / FAIL with an overall coverage percentage. Target is 100% PASS on all 8 avenues.

## Key Concepts

- **3+ avenues** for critical context (identity, rules)
- **8 avenues**: System Prompt, Path Rules, Skills, Parent Refs, JSON-LD, Integration MDs, Episodic, Agnostic System
- **Independence**: Each avenue uses a different mechanism; failures do not cascade
- **How to add redundancy**: Mention in 0AGNOSTIC.md (A1), create path rule (A2), create skill (A3), add to .gab.jsonld (A5)
- **Measurement**: Automated test script validates functional coverage

## Reference Table

| What | Where | Notes |
|------|-------|-------|
| Full principle doc | `.0agnostic/01_knowledge/principles/avenue_redundancy.md` | Coverage targets, how to add redundancy, measurement |
| Avenue architecture | `.0agnostic/01_knowledge/avenue_web_architecture.md` | All 8 avenues with redundancy matrix |
| Avenue test script | `layer_3_99_stages/stage_3_07_testing/outputs/test_avenue_coverage_functional.sh` | Automated validation |
