# Delivery Avenues

## Summary

An avenue is an independent path through which context reaches an AI agent. The context chain system uses 8 redundant avenues to ensure critical context is never lost even if one delivery mechanism fails. Each avenue operates through a different mechanism (filesystem walk, directory matching, jq query, manual read), so a failure in one does not cascade to others.

The 8 avenues are: A1 System Prompt (CLAUDE.md cascade, static/automatic), A2 Path Rules (.claude/rules/, triggered by directory), A3 Skills (listed statically, full content on invocation), A4 Parent References (0AGNOSTIC.md chain, explicit traversal), A5 JSON-LD Agent Defs (.gab.jsonld, mode/actor constraints), A6 Integration Summaries (.integration.md, readable markdown), A7 Episodic Memory (session history), A8 Agnostic System (.0agnostic/ on-demand resources).

Avenues can be categorized by timing (static: A1; semi-static: A2; dynamic: A3-A8) and by ownership (fixed: A1 cascade order, A2 matching; configurable: all content). The avenue redundancy principle requires 3+ avenues for critical context items like entity identity and applicable rules. Some avenues function as intentional pairs: A5+A6 (structured + readable), A1+A4 (generated + source), A2+A8 (auto-loaded + manual).

## Key Concepts

- **Avenue independence**: Each avenue uses a different mechanism; one failure does not affect others
- **8 avenues**: System Prompt, Path Rules, Skills, Parent Refs, JSON-LD, Integration MDs, Episodic Memory, Agnostic System
- **Redundancy target**: 3+ avenues for critical context (identity, rules)
- **Paired avenues**: A5+A6, A1+A4, A2+A8 provide same content through two formats
- **Test coverage**: `test_avenue_coverage_functional.sh` validates all 8 avenues are functional

## Reference Table

| What | Where | Notes |
|------|-------|-------|
| Full avenue architecture | `.0agnostic/01_knowledge/avenue_web_architecture.md` | All 8 avenues, categories, redundancy matrix, health metrics |
| Avenue redundancy principle | `.0agnostic/01_knowledge/principles/avenue_redundancy.md` | Coverage targets and how to add redundancy |
| Graceful degradation | `.0agnostic/01_knowledge/principles/graceful_degradation.md` | What happens when avenues fail |
| Stage 02 research | `layer_3_99_stages/stage_3_02_research/outputs/by_topic/integration/` | Original research on delivery mechanisms |
| Avenue test script | `layer_3_99_stages/stage_3_07_testing/outputs/test_avenue_coverage_functional.sh` | Automated validation |
