---
resource_id: "918ec1d1-0a67-4097-b926-8f6075466393"
resource_type: "rule"
resource_name: "1_2_identify_system_prompt_architecture"
---
# 1.2: Identify System Prompt vs. Foundational Context

<!-- section_id: "82979b40-3edb-474c-8235-9b4f124f0f51" -->
## What This Need Covers

Understanding the architectural distinction between system prompt and foundational context, and where the discretionary wrapper applies.

<!-- section_id: "4b3155e6-0015-44a5-9e73-0c1989c12fd5" -->
## Requirement

The team must understand:
- What is the system prompt and where it comes from
- What is foundational context and how it's loaded
- What is conversation context and how it differs
- Where in this architecture the discretionary wrapper applies
- Why this distinction matters for solving the problem

<!-- section_id: "af9a9318-0aa4-4f5e-b62b-8ab07284fb48" -->
## Acceptance Criteria (Satisfied When)

- [x] System prompt definition is documented
- [x] Foundational context definition is documented
- [x] Conversation context definition is documented
- [x] Loading order and priority are documented
- [x] Where discretionary wrapper applies is identified
- [x] Why this distinction is critical to solution is explained
- [x] Architecture diagram is created showing these layers

<!-- section_id: "e51a049c-8789-4c7d-a2ef-98155fc3a577" -->
## Source

Research findings: `../../../../stage_0_02_research/outputs/claude_code_system_prompt_research_findings.md` - Section 1.2: "How Claude Code Loads Context"

<!-- section_id: "aec9ad54-ca26-4617-9349-044925032996" -->
## Key Insight

**The solution must move critical rules FROM foundational context (wrapped) TO system prompt (not wrapped).**

<!-- section_id: "ec50d74f-b247-4951-a780-725b726377a0" -->
## Owner Stage

- **Research**: Stage 0_02_research (already completed)
- **Instruction**: Stage 0_03_instructions (convert to constraints)

<!-- section_id: "d3acdf8d-6170-49f5-baa0-f8fc6b33b5ca" -->
## Dependencies

- Requires: Understanding from 1.1 (what the wrapper is)
- Enables: 1.3 (evaluating which approach moves rules to system prompt)

<!-- section_id: "8638a823-a7b2-4b0c-8955-f3964b6a154d" -->
## Cross-References

- Parent need: `PARENT_NEED_P1.md`
- Sibling need 1.1: `1_1_understand_discretionary_wrapper.md`
- Sibling need 1.3: `1_3_evaluate_customization_approaches.md`
- Research section: Section 1.2 of research findings

<!-- section_id: "27786b02-77e3-4428-a58a-26b91090cf82" -->
## Navigation

- **Parent need**: `PARENT_NEED_P1.md`
- **Previous sibling**: `1_1_understand_discretionary_wrapper.md`
- **Next sibling**: `1_3_evaluate_customization_approaches.md`
