# 1.4: Select Viable Approach

## What This Need Covers

Selecting the best viable approach from those evaluated in 1.3, with clear rationale and decision documentation.

## Requirement

Based on the evaluation of all approaches, select one approach as the primary solution and document:
- Which approach was selected
- Why it was selected over alternatives
- What trade-offs were accepted
- What risks exist with this approach
- How risks will be mitigated

## Selected Approach

**Agent SDK `systemPrompt` + `append: true`**

### Rationale

- ✅ Proven to work (documented in Agent SDK)
- ✅ Rules appear in actual system prompt (not wrapped)
- ✅ No risk to core Claude Code functionality
- ✅ Can be version controlled
- ✅ Dynamic - rules extracted at runtime
- ✅ Works with wrapper scripts for interactive use
- ✅ Lower risk than complete systemPrompt replacement

### Trade-offs Accepted

- ⚠️ Requires running via Node.js/Agent SDK (not direct CLI)
- ⚠️ Initial setup required (create wrapper scripts)
- ⚠️ Depends on Anthropic maintaining Agent SDK API

### Mitigation Strategies

- Monitor Claude Code releases for breaking changes
- Version-lock dependencies
- Create compatibility wrapper if API changes
- Plan for fallback approaches if needed

## Acceptance Criteria (Satisfied When)

- [x] Approach is selected
- [x] Rationale is documented
- [x] Trade-offs are listed
- [x] Risks are identified
- [x] Mitigation strategies are planned
- [x] Decision is approved by stakeholders
- [ ] Implementation begins (moves to design phase)

## Owner Stage

- **Research**: Stage 0_02_research (recommendation based on research)
- **Instruction**: Stage 0_03_instructions (refine selection into requirements)

## Dependencies

- Requires: 1.3 (evaluation of all approaches)
- Enables: 1.5 (planning how to implement the selected approach)

## Cross-References

- Parent need: `PARENT_NEED_P1.md`
- Sibling need 1.3: `1_3_evaluate_customization_approaches.md`
- Sibling need 1.5: `1_5_plan_implementation_path.md`
- Research recommendation: Section 3.1 of research findings

## Navigation

- **Parent need**: `PARENT_NEED_P1.md`
- **Previous sibling**: `1_3_evaluate_customization_approaches.md`
- **Next sibling**: `1_5_plan_implementation_path.md`
