---
resource_id: "7bf2a2dd-cbcb-406c-945d-314e169216c7"
resource_type: "rule"
resource_name: "1_1_understand_discretionary_wrapper"
---
# 1.1: Understand Discretionary Wrapper Mechanism

## What This Need Covers

Understanding what the discretionary wrapper is, how it works, why Anthropic implemented it, and how it affects rule enforcement.

## Requirement

The team must have comprehensive understanding of:
- What the discretionary disclaimer says and where it appears
- Why Anthropic created this mechanism
- What problem it was designed to solve
- How it manifests in the system
- Why it undermines critical governance rules

## Acceptance Criteria (Satisfied When)

- [x] Discretionary disclaimer text is documented verbatim
- [x] Origin and purpose are explained (Anthropic's design decision)
- [x] How it works technically is documented
- [x] Why it affects governance rules is explained
- [x] Real examples of how rules could be filtered are provided
- [x] This understanding is captured in research findings

## Source

Research findings: `../../../../stage_0_02_research/outputs/claude_code_system_prompt_research_findings.md` - Section 2: "The Anthropic Discretionary Disclaimer"

## Owner Stage

- **Research**: Stage 0_02_research (already completed)
- **Instruction**: Stage 0_03_instructions (refine understanding into constraints)

## Dependencies

- Requires: Research findings from stage_0_02_research
- Enables: 1.2, 1.3 (understanding the broader context)

## Cross-References

- Parent need: `PARENT_NEED_P1.md`
- Sibling need 1.2: `1_2_identify_system_prompt_architecture.md`
- Research section: Section 2 of research findings

## Navigation

- **Parent need**: `PARENT_NEED_P1.md`
- **Next sibling**: `1_2_identify_system_prompt_architecture.md`
