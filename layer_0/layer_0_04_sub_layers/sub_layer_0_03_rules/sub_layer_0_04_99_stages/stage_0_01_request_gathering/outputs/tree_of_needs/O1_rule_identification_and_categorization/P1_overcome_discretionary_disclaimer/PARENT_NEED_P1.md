# P1: OVERCOME DISCRETIONARY DISCLAIMER

## Tactical Objective

**Understand and overcome Anthropic's discretionary context filtering mechanism.**

## Context

The core problem is that Claude Code wraps user-provided CLAUDE.md files with a disclaimer allowing Claude to decide whether to apply them based on perceived relevance. This undermines mandatory governance rules.

To overcome this, we must:
1. Deeply understand how the mechanism works
2. Identify where in the system architecture it manifests
3. Evaluate all available solutions
4. Select the most viable approach
5. Plan a clear implementation path

## Parent Overarching Need

**O1: Rule Identification & Categorization** - Understanding the problem and selecting the right solution

## Child Needs

| ID | Need | Description |
|----|------|-------------|
| 1.1 | Understand discretionary wrapper mechanism | What is it, how does it work, why does Anthropic do it? |
| 1.2 | Identify system prompt vs. foundational context | Where in the system prompt architecture does the wrapper apply? |
| 1.3 | Evaluate customization approaches | What are all viable ways to customize system prompts? |
| 1.4 | Select viable approach | Which approach is best for our use case? |
| 1.5 | Plan implementation path | How will we implement the selected approach? |

## Acceptance Criteria (Need Satisfied When)

- [x] Discretionary disclaimer mechanism is documented and understood
- [x] System prompt architecture is mapped (system prompt vs. foundational context)
- [x] All 4 customization approaches are evaluated (Agent SDK, output styles, managed settings, complete replacement)
- [x] Approach is selected: Agent SDK `systemPrompt` + `append: true`
- [x] Viability is confirmed through research
- [x] Implementation path is documented
- [ ] Implementation begins (moves to O2-O4 planning)

## Dependencies

### Requires
- Research findings from stage_0_02_research
- Understanding of Claude Code architecture
- Access to Claude Code and Agent SDK documentation

### Enables
- O2: Rule Management design
- O3: Rule Enforcement design
- O4: Rule Verification design

## Success Metrics

This parent need succeeds when:
1. **Understanding**: Anyone can read research and understand the discretionary disclaimer
2. **Selection**: Agent SDK approach is confirmed as viable and documented
3. **Path**: Clear, step-by-step implementation path exists
4. **Confidence**: Team has high confidence in the selected approach

## Cross-References

- Research findings: `../../../../stage_0_02_research/outputs/claude_code_system_prompt_research_findings.md`
- Overarching need: `../OVERARCHING_O1.md`
- Root need: `../../root_need/ROOT_NEED_enforce_critical_rules.md`

## Navigation

- **Overarching need**: `../OVERARCHING_O1.md`
- **Child need 1.1**: `1_1_understand_discretionary_wrapper.md`
- **Child need 1.2**: `1_2_identify_system_prompt_architecture.md`
- **Child need 1.3**: `1_3_evaluate_customization_approaches.md`
- **Child need 1.4**: `1_4_select_viable_approach.md`
- **Child need 1.5**: `1_5_plan_implementation_path.md`
