---
resource_id: "a3c054f9-ec5b-4283-b8e3-4fcd30f1273a"
resource_type: "output"
resource_name: "US-01_project_custom_recommendation"
---
# US-01: Project gets custom recommendation

**Need**: [Customizable Importance](../README.md)

---

**As a** developer configuring a HighThroughputAPI project,
**I want** to define that speed and scalability matter most, while cost and maintenance are secondary,
**So that** the decision matrix recommends the best avenue for my specific priorities.

<!-- section_id: "83ed3463-24cc-45c6-96f5-be6c77fd256f" -->
### What Happens

1. Developer creates a project context (HighThroughputAPI, priority: speed + scalability)
2. Developer overrides importance weights for speed-related operations (higher) and cost-related operations (lower)
3. System computes weighted scores: performance_score x importance_weight for each avenue
4. Decision matrix shows: "HighThroughputAPI -> Best: Vector Databases (score: 87.3)"

<!-- section_id: "4c344f41-91ca-4a25-bffa-22c5afe9786f" -->
### Acceptance Criteria

- Project-specific weights override general importance correctly
- Decision matrix produces different recommendations for different project profiles
- Same benchmark data, different recommendations based on project priorities
