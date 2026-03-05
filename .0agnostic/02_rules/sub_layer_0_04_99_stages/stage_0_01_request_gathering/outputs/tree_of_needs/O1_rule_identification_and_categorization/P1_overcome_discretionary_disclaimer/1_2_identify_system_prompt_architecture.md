---
resource_id: "918ec1d1-0a67-4097-b926-8f6075466393"
resource_type: "rule"
resource_name: "1_2_identify_system_prompt_architecture"
---
# 1.2: Identify System Prompt vs. Foundational Context

## What This Need Covers

Understanding the architectural distinction between system prompt and foundational context, and where the discretionary wrapper applies.

## Requirement

The team must understand:
- What is the system prompt and where it comes from
- What is foundational context and how it's loaded
- What is conversation context and how it differs
- Where in this architecture the discretionary wrapper applies
- Why this distinction matters for solving the problem

## Acceptance Criteria (Satisfied When)

- [x] System prompt definition is documented
- [x] Foundational context definition is documented
- [x] Conversation context definition is documented
- [x] Loading order and priority are documented
- [x] Where discretionary wrapper applies is identified
- [x] Why this distinction is critical to solution is explained
- [x] Architecture diagram is created showing these layers

## Source

Research findings: `../../../../stage_0_02_research/outputs/claude_code_system_prompt_research_findings.md` - Section 1.2: "How Claude Code Loads Context"

## Key Insight

**The solution must move critical rules FROM foundational context (wrapped) TO system prompt (not wrapped).**

## Owner Stage

- **Research**: Stage 0_02_research (already completed)
- **Instruction**: Stage 0_03_instructions (convert to constraints)

## Dependencies

- Requires: Understanding from 1.1 (what the wrapper is)
- Enables: 1.3 (evaluating which approach moves rules to system prompt)

## Cross-References

- Parent need: `PARENT_NEED_P1.md`
- Sibling need 1.1: `1_1_understand_discretionary_wrapper.md`
- Sibling need 1.3: `1_3_evaluate_customization_approaches.md`
- Research section: Section 1.2 of research findings

## Navigation

- **Parent need**: `PARENT_NEED_P1.md`
- **Previous sibling**: `1_1_understand_discretionary_wrapper.md`
- **Next sibling**: `1_3_evaluate_customization_approaches.md`
