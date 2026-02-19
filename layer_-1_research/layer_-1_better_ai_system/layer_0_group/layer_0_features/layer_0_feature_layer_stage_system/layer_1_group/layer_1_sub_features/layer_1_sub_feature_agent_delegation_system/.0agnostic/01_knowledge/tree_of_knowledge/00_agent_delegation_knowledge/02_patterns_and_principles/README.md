# Branch 02: Patterns and Principles

**Question**: What patterns and principles govern agent delegation?

This branch covers the discovered patterns and formalized principles that emerged from building and using the delegation model. These are operational insights — they tell agents how to behave correctly.

## Topics

| Topic | Summary | Formalized As |
|-------|---------|---------------|
| `two_halves_pattern.md` | Every 0AGNOSTIC.md needs operational guidance + current state | Principle 9 |
| `scope_boundary_decisions.md` | How agents handle out-of-scope work at layer/stage boundaries | Principle 8 + Scope Boundary Rule |
| `three_tier_knowledge.md` | Pointers → distilled → full knowledge flow | Principle 3 |
| `cross_layer_stage_references.md` | Bidirectional references between parent and child layer stages | Principle 10 |

## Key Insight

These patterns are all about **context window management**. The two-halves pattern prevents wasted exploration. Scope boundary decisions prevent context overflow. Three-tier knowledge ensures agents load only what they need. The common thread: context windows are the fundamental constraint — every design decision optimizes for them.
