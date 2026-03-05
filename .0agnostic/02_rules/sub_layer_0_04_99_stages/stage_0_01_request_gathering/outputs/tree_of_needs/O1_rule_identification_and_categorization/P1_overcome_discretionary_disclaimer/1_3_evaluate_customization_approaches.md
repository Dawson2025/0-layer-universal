---
resource_id: "8525f349-b425-4a47-bb86-18c7d9826be7"
resource_type: "rule"
resource_name: "1_3_evaluate_customization_approaches"
---
# 1.3: Evaluate Customization Approaches

<!-- section_id: "5ee7e130-83ae-4f68-9423-538a3ce33e3a" -->
## What This Need Covers

Evaluating all viable approaches to customize Claude Code's system prompt and move critical rules out of the discretionary wrapper.

<!-- section_id: "3bb927f8-b20a-4844-bfb4-af454d9ea276" -->
## Requirement

Research and fairly evaluate all available customization approaches:
- Agent SDK `systemPrompt` + `append` flag
- Output styles configuration
- Managed settings (organizational)
- Complete systemPrompt replacement

For each approach, document:
- How it works
- Viability for this use case
- Advantages and disadvantages
- Risks and limitations
- Implementation complexity

<!-- section_id: "051e8dff-dd72-4b73-b501-be0b0c78fad4" -->
## Acceptance Criteria (Satisfied When)

- [x] 4 approaches identified and researched
- [x] Each approach is fairly evaluated
- [x] Viability for moving rules to system prompt is assessed
- [x] Advantages/disadvantages documented for each
- [x] Risks identified for each
- [x] Implementation complexity compared
- [x] Findings are documented in research

<!-- section_id: "6092d268-09d2-46ca-be49-2c4e71757a6e" -->
## Source

Research findings: `../../../../stage_0_02_research/outputs/claude_code_system_prompt_research_findings.md` - Section 3: "Research Findings: System Prompt Customization Approaches"

<!-- section_id: "1659d0fd-7023-4f68-b4ce-f7aa3ddf63e1" -->
## Key Approaches Evaluated

| Approach | Viable? | Notes |
|----------|---------|-------|
| Agent SDK `systemPrompt` + `append` | ✅ YES | Recommended approach |
| Output styles | ⚠️ LIMITED | Supplementary only |
| Managed settings | ⚠️ LIMITED | Enterprise only |
| Complete replacement | ❌ NO | Too risky |

<!-- section_id: "7aa5b375-d101-40e7-a5aa-3c63c1f34ac5" -->
## Owner Stage

- **Research**: Stage 0_02_research (already completed)
- **Instruction**: Stage 0_03_instructions (formalize into constraints)

<!-- section_id: "911694be-dddd-4adc-ad4b-da18854d463d" -->
## Dependencies

- Requires: 1.2 (understanding system prompt architecture)
- Enables: 1.4 (selecting the best approach)

<!-- section_id: "c74cafd5-6819-4438-ae9b-897e8ff99c00" -->
## Cross-References

- Parent need: `PARENT_NEED_P1.md`
- Sibling need 1.2: `1_2_identify_system_prompt_architecture.md`
- Sibling need 1.4: `1_4_select_viable_approach.md`
- Research section: Section 3 of research findings

<!-- section_id: "438f8e3b-a6c2-4ab9-af30-2d53f752f7ee" -->
## Navigation

- **Parent need**: `PARENT_NEED_P1.md`
- **Previous sibling**: `1_2_identify_system_prompt_architecture.md`
- **Next sibling**: `1_4_select_viable_approach.md`
