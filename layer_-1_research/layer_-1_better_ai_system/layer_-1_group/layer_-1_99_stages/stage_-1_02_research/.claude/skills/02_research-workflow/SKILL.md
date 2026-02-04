---
name: 02_research-workflow
description: Workflow skill for Research stage - explore problem space, gather information
---

# Research Workflow Skill

## Purpose

This skill guides research activities at Stage 02 (Research) in the layer-stage system.

## When to Use

- Starting research on a need
- Unsure how to structure research output
- Need to understand research templates

---

## Research Process

### 1. Understand the Need
- Read the need's `requirements.md` from Tree of Needs
- Check dependencies in `_meta/DEPENDENCIES.md`
- Identify research questions

### 2. Gather Information

**Internal Research**:
- Search codebase with Glob/Grep
- Read existing documentation
- Check `outputs/` for prior research

**External Research**:
- Use Perplexity for academic/industry patterns
- WebSearch for existing solutions
- Always document sources

### 3. Analyze Options

For each option discovered:
- Document pros/cons
- Assess complexity
- Check alignment with principles (P1-P5)

### 4. Document Findings

Create in `outputs/by_need/[need_name]/`:

| File | Content |
|------|---------|
| `options_analysis.md` | All options with comparison |
| `recommended_approach.md` | Selected option + justification |
| `implementation_sketch.md` | High-level design |

### 5. Cross-Reference

If research reveals patterns for multiple needs:
- Document in `outputs/by_topic/`
- Reference from individual need research

---

## Output Templates

### Options Analysis Template

```markdown
# Options Analysis: [Need Name]

## Option A: [Name]
- **Description**: ...
- **Pros**: ...
- **Cons**: ...
- **Complexity**: Low/Medium/High

## Option B: [Name]
...

## Comparison Matrix
| Criteria | Option A | Option B | Option C |
|----------|----------|----------|----------|
```

### Recommended Approach Template

```markdown
# Recommended Approach: [Need Name]

## Selected Option
[Which option and why]

## Justification
[Why this option best satisfies the need]

## Trade-offs Accepted
[What we're giving up]
```

### Implementation Sketch Template

```markdown
# Implementation Sketch: [Need Name]

## High-Level Design
[Architecture/structure]

## Key Components
[What needs to be built]

## Integration Points
[How it connects to other needs]

## Open Questions
[Remaining unknowns]
```

---

## Research Quality Checklist

Before completing research on a need:

- [ ] Multiple options explored (not just first idea)
- [ ] External research conducted with sources cited
- [ ] Options compared against principles (P1-P5)
- [ ] Trade-offs explicitly documented
- [ ] Implementation sketch is actionable
- [ ] Cross-cutting patterns extracted to `by_topic/`

---

## References

- Tree of Needs: `../../stage_-1_01_request_gathering/outputs/tree_of_needs/`
- Principles: See handoff document for P1-P5
