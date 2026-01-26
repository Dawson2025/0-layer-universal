# Guiding Principles: Tree of Needs

Cross-cutting principles that apply to ALL needs and the system as a whole.

---

## P1: Future-Proof by Design

> The AI system must be designed to evolve with technology changes.

### Why This Matters
- AI tools evolve rapidly (new models, new capabilities, new APIs)
- What works today may be obsolete tomorrow
- Lock-in to specific technologies limits longevity
- The system should get better as AI improves, not become obsolete

### Implications for All Needs

| Need | Future-Proofing Implication |
|------|----------------------------|
| persistent_knowledge | Knowledge format should be tool-agnostic |
| scalable_context | Delegation patterns should work with future AI capabilities |
| discoverable | Structure should accommodate new entity types |
| tool_portable | Must easily add support for new AI tools |
| session_resilient | Handoff format should be AI-model-agnostic |
| failure_recoverable | Recovery mechanisms should handle unknown failures |
| rule_compliant | Rule system should accommodate new rule types |
| predictable | Behavior contracts should survive model upgrades |
| bounded | Scope definitions should adapt to new capabilities |
| transparent | State visibility should expose new AI features |
| debuggable | Diagnostics should catch novel failure modes |
| auditable | Audit trails should capture evolving action types |

### Design Guidelines

1. **Abstraction over Implementation**
   - Define interfaces, not implementations
   - Use agnostic formats that any AI can understand
   - Avoid hard-coding AI-specific behaviors

2. **Modularity**
   - Components should be replaceable
   - New capabilities should be additive, not requiring rewrites
   - Clear boundaries between system parts

3. **Graceful Degradation**
   - System should work with varying AI capabilities
   - Missing features should fail gracefully, not catastrophically
   - Older implementations should still function

4. **Forward Compatibility**
   - Leave room for extension points
   - Use schemas that allow additional fields
   - Document upgrade paths

---

## P2: Technology Agnostic

> The core system should not depend on any specific AI tool, model, or vendor.

### Why This Matters
- Vendor lock-in is risky
- Best tool for a task may change
- Competition improves options
- Users should have choice

### Implications
- AGNOSTIC.md as source of truth, not CLAUDE.md
- Formats readable by any AI (plain text, markdown, YAML)
- No proprietary features required for core functionality
- Tool-specific features as optional enhancements

---

## P3: Incremental Adoption

> The system should be adoptable piece by piece, not all-or-nothing.

### Why This Matters
- Large migrations are risky
- Different parts mature at different rates
- Users have varying needs
- Partial adoption is better than no adoption

### Implications
- Each need should be independently valuable
- Dependencies should be soft where possible
- Default behaviors should be sensible
- Advanced features should be opt-in

---

## P4: Human-AI Partnership

> The system augments human capability, it doesn't replace human judgment.

### Why This Matters
- AI makes mistakes
- Humans have context AI lacks
- Trust requires oversight
- Collaboration > automation

### Implications
- Human approval for significant actions
- Transparency into AI decisions
- Easy override mechanisms
- AI as assistant, not autonomous agent

---

## P5: Simplicity Over Cleverness

> Prefer simple, understandable solutions over clever, complex ones.

### Why This Matters
- Simple systems are easier to debug
- Simple systems are easier to evolve
- Simple systems are easier to understand
- Cleverness often hides bugs

### Implications
- Plain text over complex formats
- Explicit over implicit
- Convention over configuration (where sensible)
- Document the "why" not just the "what"

---

## Applying Principles

When designing or evaluating any requirement:

1. **Check against principles**: Does this support or violate our principles?
2. **Prefer principle-aligned solutions**: When choosing between approaches
3. **Document trade-offs**: When principles conflict, explain the choice
4. **Update principles**: If they prove wrong or incomplete

---

## Principle Hierarchy

If principles conflict:

1. **P1: Future-Proof** - Long-term viability trumps short-term convenience
2. **P4: Human-AI Partnership** - Safety trumps automation
3. **P2: Technology Agnostic** - Flexibility trumps optimization
4. **P3: Incremental Adoption** - Pragmatism trumps perfection
5. **P5: Simplicity** - Clarity trumps cleverness
