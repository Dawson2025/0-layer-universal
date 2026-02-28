# US-03: Developer tunes scoring weights

**Need**: [Scored Context Retrieval](../README.md)

---

**As a** user who wants the AI to prioritize differently depending on the type of work,
**I want** to adjust the balance between recency, relevance, and importance in the scoring function,
**So that** research sessions prioritize breadth while active development sessions prioritize recent decisions.

### What Happens

1. User notices the AI is loading suboptimal context for a particular type of work
2. User adjusts the scoring weights (e.g., increase recency weight for development, increase breadth for research)
3. Scoring function applies the new weights to future context loading
4. AI loads context that better matches the current work mode

### Acceptance Criteria

- Scoring weights are configurable, not hardcoded
- Different weight profiles can be applied to different contexts (research vs development)
- Changing weights visibly changes the ranked output
