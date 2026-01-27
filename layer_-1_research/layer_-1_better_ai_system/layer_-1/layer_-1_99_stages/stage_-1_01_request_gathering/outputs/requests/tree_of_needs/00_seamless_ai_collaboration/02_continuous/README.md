# Branch: Work is CONTINUOUS

**Parent**: [00_seamless_ai_collaboration](../)

---

## Core Question

> "Does work keep going without interruption?"

---

## Description

For work to be continuous, it must not be blocked by:
1. **Tool limits** - Token limits, tool crashes, tool unavailability
2. **Session limits** - Context windows, time away, needing to restart
3. **Failures** - Errors, broken configs, migration issues
4. **Technology evolution** - AI tools change, models improve, APIs update
5. **Platform differences** - Different OS, different machines

---

## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| [need_01_tool_portable](./need_01_tool_portable/) | "Can I switch tools?" | Not locked to one AI app |
| [need_02_session_resilient](./need_02_session_resilient/) | "Can I pick up where I left off?" | Work continues across sessions |
| [need_03_failure_recoverable](./need_03_failure_recoverable/) | "What happens when something goes wrong?" | System recovers gracefully |
| [need_04_evolvable](./need_04_evolvable/) | "Will this still work as AI evolves?" | System adapts to technology changes |
| [need_05_cross_platform](./need_05_cross_platform/) | "Does it work on Mac, Linux, Windows?" | Works across OS and machines |
| [need_06_universal_rules_and_cross_device_access](./need_06_universal_rules_and_cross_device_access/) | "Are rules consistent everywhere? Can AI access system from any machine?" | Universal rules across all users/locations/machines, cross-device skill/memory access |

---

## Key Insight

Continuity comes from **portability**, **state capture**, **resilience**, **evolvability**, and **platform independence**. The system itself becomes the memory, not the AI's context window.

The solution is:
- Agnostic source of truth (works with any AI app)
- Tool-specific derivations (optimized for each tool)
- Handoff documents (capture state for continuation)
- Self-describing structure (new session can understand current state)
- Idempotent operations (safe to retry)
- Rollback capability (can recover from failures)
- Modular architecture (components replaceable independently)
- Forward-compatible formats (extensible without breaking)
- Cross-platform abstractions (works on any OS)
