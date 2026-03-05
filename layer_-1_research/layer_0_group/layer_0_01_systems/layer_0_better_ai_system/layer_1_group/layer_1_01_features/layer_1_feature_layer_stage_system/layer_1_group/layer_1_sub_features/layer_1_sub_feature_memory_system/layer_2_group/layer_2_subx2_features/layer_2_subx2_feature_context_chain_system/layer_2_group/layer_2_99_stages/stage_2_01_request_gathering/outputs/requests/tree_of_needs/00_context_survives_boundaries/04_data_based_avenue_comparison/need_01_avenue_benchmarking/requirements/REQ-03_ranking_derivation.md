---
resource_id: "b77862e2-bd9d-4e67-8574-7a23f17d88c9"
resource_type: "output"
resource_name: "REQ-03_ranking_derivation"
---
# Ranking Derivation

**Need**: [Avenue Benchmarking](../README.md)

---

- MUST compute rankings from normalized benchmark scores, not assign them manually
- MUST support ranking by individual capability (best avenue for speed, best for cost, etc.)
- MUST support aggregate ranking across all capabilities
- MUST handle ties in ranking gracefully
- MUST allow re-ranking when benchmarks are updated (rankings are always derived, never static)
