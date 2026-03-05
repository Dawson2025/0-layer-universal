---
resource_id: "7cef3c8b-c3a2-492a-abf7-37c0991bd57b"
resource_type: "output"
resource_name: "US-02_stage_agent_works_from_distilled"
---
# US-2: Stage agent works from distilled knowledge

**Need**: [Three-Tier Delegation](../README.md)

---

**As a** user who expects the AI to build on prior research without re-reading all raw research files,
**I want** stage agents to work from distilled knowledge summaries (Tier 2), not raw stage outputs,
**So that** the AI uses actionable summaries rather than wading through unprocessed research.

### What Happens

1. User tells the AI to design a feature (stage 04)
2. Manager spawns a design stage agent
3. Design stage agent reads Tier 2 knowledge files from `.0agnostic/knowledge/` (distilled summaries)
4. Agent does NOT read raw stage_02 research outputs (Tier 3 of another stage)
5. Agent has actionable domain understanding and begins design work efficiently

### Acceptance Criteria

- Stage agent reads distilled knowledge files, not raw stage_02 research outputs
- Distilled knowledge is sufficient for the agent to do its work
- Tier 2 content is a curated summary, not a copy of Tier 3
