---
resource_id: "7bf2a2dd-cbcb-406c-945d-314e169216c7"
resource_type: "rule"
resource_name: "1_1_understand_discretionary_wrapper"
---
# 1.1: Understand Discretionary Wrapper Mechanism

<!-- section_id: "7233484f-2f5a-41df-850a-a492be126766" -->
## What This Need Covers

Understanding what the discretionary wrapper is, how it works, why Anthropic implemented it, and how it affects rule enforcement.

<!-- section_id: "3d819232-0a44-4557-840c-77f4cc4255d8" -->
## Requirement

The team must have comprehensive understanding of:
- What the discretionary disclaimer says and where it appears
- Why Anthropic created this mechanism
- What problem it was designed to solve
- How it manifests in the system
- Why it undermines critical governance rules

<!-- section_id: "e272aa34-8a54-4d0b-8770-72f9ebea0ad4" -->
## Acceptance Criteria (Satisfied When)

- [x] Discretionary disclaimer text is documented verbatim
- [x] Origin and purpose are explained (Anthropic's design decision)
- [x] How it works technically is documented
- [x] Why it affects governance rules is explained
- [x] Real examples of how rules could be filtered are provided
- [x] This understanding is captured in research findings

<!-- section_id: "d524d029-4004-4436-baae-d99bbf311903" -->
## Source

Research findings: `../../../../stage_0_02_research/outputs/claude_code_system_prompt_research_findings.md` - Section 2: "The Anthropic Discretionary Disclaimer"

<!-- section_id: "2300b375-1c55-4af5-9b54-5369527598ae" -->
## Owner Stage

- **Research**: Stage 0_02_research (already completed)
- **Instruction**: Stage 0_03_instructions (refine understanding into constraints)

<!-- section_id: "818545e6-5e75-4b5d-a23e-5a7bd736dac2" -->
## Dependencies

- Requires: Research findings from stage_0_02_research
- Enables: 1.2, 1.3 (understanding the broader context)

<!-- section_id: "0aec1f3a-a49f-4cf6-8d9a-b2d8bcb4cad3" -->
## Cross-References

- Parent need: `PARENT_NEED_P1.md`
- Sibling need 1.2: `1_2_identify_system_prompt_architecture.md`
- Research section: Section 2 of research findings

<!-- section_id: "3f7bca27-c1a5-42a9-9a6e-b48cbf667a2e" -->
## Navigation

- **Parent need**: `PARENT_NEED_P1.md`
- **Next sibling**: `1_2_identify_system_prompt_architecture.md`
