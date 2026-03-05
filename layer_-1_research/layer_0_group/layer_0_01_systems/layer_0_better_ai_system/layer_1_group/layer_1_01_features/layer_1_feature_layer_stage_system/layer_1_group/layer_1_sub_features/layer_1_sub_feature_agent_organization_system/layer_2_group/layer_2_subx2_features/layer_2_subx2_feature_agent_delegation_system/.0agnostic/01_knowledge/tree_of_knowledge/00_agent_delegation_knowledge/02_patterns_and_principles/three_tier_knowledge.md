---
resource_id: "6e4bc921-9567-48cc-80ed-686ebd5fd29a"
resource_type: "knowledge"
resource_name: "three_tier_knowledge"
---
# Topic: Three-Tier Knowledge

## Summary

Knowledge flows through three tiers in the layer-stage hierarchy:

1. **Pointers** (0AGNOSTIC.md) — what this entity/stage IS, where things are. Loaded as static context.
2. **Distilled** (.0agnostic/01_knowledge/) — domain knowledge, principles, summaries with references. Loaded on demand.
3. **Full** (stage outputs) — complete research, design specs, test results, requirements. Stays within stages.

Managers work at the pointer tier. Stage agents load distilled knowledge on demand. Full detail stays within stages and is accessed only when needed for specific work.

This tree of knowledge itself is a distilled-tier artifact — it provides organized summaries and points to where the full detail lives.

## Key Points

- Formalized as **Principle 3** in the Stage Delegation Principles
- Also informed by **Principle 7** (Selective Context Loading: never load all parent knowledge at once)
- The two-halves pattern makes the pointer tier functional by adding current state to 0AGNOSTIC.md
- The tree of knowledge makes the distilled tier functional by organizing summaries with references

## References

| What | Where |
|------|-------|
| Principle 3 (Three-Tier Knowledge) | `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` |
| Principle 7 (Selective Context Loading) | Same file |
| Research findings | Stage 02: `../../../../../../layer_1_group/layer_1_99_stages/stage_1_02_research/0AGNOSTIC.md` → Key Findings |
