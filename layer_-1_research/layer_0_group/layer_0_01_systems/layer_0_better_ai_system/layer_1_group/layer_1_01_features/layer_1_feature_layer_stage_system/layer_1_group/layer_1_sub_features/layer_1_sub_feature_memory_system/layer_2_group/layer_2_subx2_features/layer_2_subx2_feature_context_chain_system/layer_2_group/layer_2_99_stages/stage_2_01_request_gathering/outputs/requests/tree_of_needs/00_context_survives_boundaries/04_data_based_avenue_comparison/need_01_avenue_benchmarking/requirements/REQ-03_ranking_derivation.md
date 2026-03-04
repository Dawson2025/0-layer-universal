# Ranking Derivation

**Need**: [Avenue Benchmarking](../README.md)

---

- MUST compute rankings from normalized benchmark scores, not assign them manually
- MUST support ranking by individual capability (best avenue for speed, best for cost, etc.)
- MUST support aggregate ranking across all capabilities
- MUST handle ties in ranking gracefully
- MUST allow re-ranking when benchmarks are updated (rankings are always derived, never static)
