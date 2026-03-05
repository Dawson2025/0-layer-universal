---
resource_id: "8525f349-b425-4a47-bb86-18c7d9826be7"
resource_type: "rule"
resource_name: "1_3_evaluate_customization_approaches"
---
# 1.3: Evaluate Customization Approaches

## What This Need Covers

Evaluating all viable approaches to customize Claude Code's system prompt and move critical rules out of the discretionary wrapper.

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

## Acceptance Criteria (Satisfied When)

- [x] 4 approaches identified and researched
- [x] Each approach is fairly evaluated
- [x] Viability for moving rules to system prompt is assessed
- [x] Advantages/disadvantages documented for each
- [x] Risks identified for each
- [x] Implementation complexity compared
- [x] Findings are documented in research

## Source

Research findings: `../../../../stage_0_02_research/outputs/claude_code_system_prompt_research_findings.md` - Section 3: "Research Findings: System Prompt Customization Approaches"

## Key Approaches Evaluated

| Approach | Viable? | Notes |
|----------|---------|-------|
| Agent SDK `systemPrompt` + `append` | ✅ YES | Recommended approach |
| Output styles | ⚠️ LIMITED | Supplementary only |
| Managed settings | ⚠️ LIMITED | Enterprise only |
| Complete replacement | ❌ NO | Too risky |

## Owner Stage

- **Research**: Stage 0_02_research (already completed)
- **Instruction**: Stage 0_03_instructions (formalize into constraints)

## Dependencies

- Requires: 1.2 (understanding system prompt architecture)
- Enables: 1.4 (selecting the best approach)

## Cross-References

- Parent need: `PARENT_NEED_P1.md`
- Sibling need 1.2: `1_2_identify_system_prompt_architecture.md`
- Sibling need 1.4: `1_4_select_viable_approach.md`
- Research section: Section 3 of research findings

## Navigation

- **Parent need**: `PARENT_NEED_P1.md`
- **Previous sibling**: `1_2_identify_system_prompt_architecture.md`
- **Next sibling**: `1_4_select_viable_approach.md`
