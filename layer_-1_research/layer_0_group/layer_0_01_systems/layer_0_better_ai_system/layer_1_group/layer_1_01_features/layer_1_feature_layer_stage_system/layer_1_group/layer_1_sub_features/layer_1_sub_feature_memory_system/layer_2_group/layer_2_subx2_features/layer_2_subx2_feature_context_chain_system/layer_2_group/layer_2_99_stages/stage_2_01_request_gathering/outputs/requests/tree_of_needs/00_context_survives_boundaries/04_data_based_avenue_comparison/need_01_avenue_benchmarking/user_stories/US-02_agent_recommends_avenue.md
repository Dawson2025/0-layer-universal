---
resource_id: "57b875cd-a686-44eb-b4fb-6eaef63106d7"
resource_type: "output"
resource_name: "US-02_agent_recommends_avenue"
---
# US-02: Agent recommends avenue based on benchmarks

**Need**: [Avenue Benchmarking](../README.md)

---

**As a** manager agent making avenue selection decisions,
**I want** benchmark-backed rankings for each capability,
**So that** my recommendations are grounded in measured data, not guesses.

<!-- section_id: "d4523aa0-379e-45d8-99e7-3f742b8e60f9" -->
### What Happens

1. Agent loads capability benchmarks from the database
2. Agent identifies which capabilities matter most for the current context
3. Agent ranks avenues by relevant capability scores
4. Agent provides recommendation with supporting benchmark data

<!-- section_id: "ea3696d5-0a2b-4875-84be-72485cc40050" -->
### Acceptance Criteria

- Agent can query benchmarks programmatically
- Recommendations cite specific raw values and normalized scores
