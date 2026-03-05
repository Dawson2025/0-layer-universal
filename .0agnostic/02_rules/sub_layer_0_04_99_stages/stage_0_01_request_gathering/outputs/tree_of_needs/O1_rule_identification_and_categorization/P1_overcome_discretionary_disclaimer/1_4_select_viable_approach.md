---
resource_id: "d6053490-7c69-4ced-b25c-694d5068e75b"
resource_type: "rule"
resource_name: "1_4_select_viable_approach"
---
# 1.4: Select Viable Approach

<!-- section_id: "493def34-34d4-4676-bc77-467dec001709" -->
## What This Need Covers

Selecting the best viable approach from those evaluated in 1.3, with clear rationale and decision documentation.

<!-- section_id: "b2e42f0b-6561-453b-bed8-7a3ed40507f3" -->
## Requirement

Based on the evaluation of all approaches, select one approach as the primary solution and document:
- Which approach was selected
- Why it was selected over alternatives
- What trade-offs were accepted
- What risks exist with this approach
- How risks will be mitigated

<!-- section_id: "e4c89baf-25d2-4bec-8963-856efafc5704" -->
## Selected Approach

**Agent SDK `systemPrompt` + `append: true`**

<!-- section_id: "28ea5a4b-bd05-4354-a193-024d23d82795" -->
### Rationale

- ✅ Proven to work (documented in Agent SDK)
- ✅ Rules appear in actual system prompt (not wrapped)
- ✅ No risk to core Claude Code functionality
- ✅ Can be version controlled
- ✅ Dynamic - rules extracted at runtime
- ✅ Works with wrapper scripts for interactive use
- ✅ Lower risk than complete systemPrompt replacement

<!-- section_id: "76fcff6d-1c2e-4c7c-93ba-4070deffe767" -->
### Trade-offs Accepted

- ⚠️ Requires running via Node.js/Agent SDK (not direct CLI)
- ⚠️ Initial setup required (create wrapper scripts)
- ⚠️ Depends on Anthropic maintaining Agent SDK API

<!-- section_id: "7ed578b5-424c-43b8-9355-7af0a8f804b2" -->
### Mitigation Strategies

- Monitor Claude Code releases for breaking changes
- Version-lock dependencies
- Create compatibility wrapper if API changes
- Plan for fallback approaches if needed

<!-- section_id: "eba84330-7d7d-4fb3-b8c4-ab1cd11be455" -->
## Acceptance Criteria (Satisfied When)

- [x] Approach is selected
- [x] Rationale is documented
- [x] Trade-offs are listed
- [x] Risks are identified
- [x] Mitigation strategies are planned
- [x] Decision is approved by stakeholders
- [ ] Implementation begins (moves to design phase)

<!-- section_id: "10a6b817-1cb7-49d4-b889-83d97043c46e" -->
## Owner Stage

- **Research**: Stage 0_02_research (recommendation based on research)
- **Instruction**: Stage 0_03_instructions (refine selection into requirements)

<!-- section_id: "c3cd262a-8821-4826-a521-c5921573f670" -->
## Dependencies

- Requires: 1.3 (evaluation of all approaches)
- Enables: 1.5 (planning how to implement the selected approach)

<!-- section_id: "1eedddce-48bb-4b38-b348-d0c9a0e826a8" -->
## Cross-References

- Parent need: `PARENT_NEED_P1.md`
- Sibling need 1.3: `1_3_evaluate_customization_approaches.md`
- Sibling need 1.5: `1_5_plan_implementation_path.md`
- Research recommendation: Section 3.1 of research findings

<!-- section_id: "36581788-39d2-4d78-8f5e-7278acfa55c7" -->
## Navigation

- **Parent need**: `PARENT_NEED_P1.md`
- **Previous sibling**: `1_3_evaluate_customization_approaches.md`
- **Next sibling**: `1_5_plan_implementation_path.md`
