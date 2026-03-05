---
resource_id: "f4b2a706-c043-4372-91fd-fbe3b2e45f2d"
resource_type: "rule"
resource_name: "ROOT_NEED_enforce_critical_rules"
---
# ROOT NEED: Enforce Critical Rules Without Deprioritization

<!-- section_id: "c8d87e42-deb3-47d4-a9ac-8bf105290cc9" -->
## Problem Statement

Anthropic's Claude Code wraps all user-provided context (CLAUDE.md files) with a discretionary disclaimer: "this context may or may not be relevant to your task." This architectural design choice allows Claude to deprioritize or ignore critical governance rules based on perceived relevance to the current task.

<!-- section_id: "47531424-86f5-4497-9ea2-91db0f2659cc" -->
### Impact

Critical governance rules that MUST be followed on every API request (such as AI Context Modification Protocol, safety governance rules, commit/push discipline) can be filtered or deprioritized:

- **AI Context Modification Protocol** could be skipped if Claude decides modifications aren't relevant
- **Safety Governance** rules could be ignored if a task seems benign
- **Commit/Push Rule** could be bypassed if Claude decides documentation isn't relevant

This undermines the entire system of mandatory governance.

<!-- section_id: "800c1aa7-484b-4b58-80b3-a38f119e5a2c" -->
## Root Cause

The discretionary disclaimer is intentional Anthropic design:
- Addresses problem of bloated CLAUDE.md files overwhelming context
- Trains Claude to be selective about what user context to apply
- No toggle to disable it in standard Claude Code
- Reflects architectural choice to prioritize flexibility over rigid rule enforcement

<!-- section_id: "cc7c4aab-ca51-452e-a2a6-7554b1df192f" -->
## Objective

**Create a system that enforces critical governance rules without subject to Anthropic's discretionary context filtering.**

Critical rules must:
- Be identified and marked as [CRITICAL]
- Be extracted dynamically from CLAUDE.md hierarchy
- Be injected into the system prompt (not wrapped foundational context)
- Be guaranteed to apply on every API request
- Not be deprioritizable by the model

<!-- section_id: "6fc2d594-ca0e-4881-a7fa-20bfae8cb94d" -->
## Success Criteria

The system will be successful when:

1. **Rule Identification**: [CRITICAL] rules are clearly marked in CLAUDE.md files
2. **Dynamic Extraction**: System automatically finds and extracts all [CRITICAL] rules
3. **System Prompt Injection**: Rules are placed in actual system prompt via Agent SDK
4. **No Wrapper**: Critical rules appear without discretionary disclaimer
5. **Reliable Enforcement**: Rules are followed on EVERY API call
6. **No Regression**: All existing Claude Code functionality continues to work
7. **Maintainable**: System can be updated when rules change
8. **Documented**: Complete usage guide and troubleshooting documentation exists

<!-- section_id: "8e23cd42-7366-4a09-af82-b2ae500df95e" -->
## Scope

This requirement is for the universal rules system, specifically addressing how to enforce [CRITICAL] rules reliably across all layers and projects.

<!-- section_id: "ec5df1af-b9d4-4d16-96c7-bf32d6fec983" -->
## Constraints

- Must work with standard Claude Code (cannot require Anthropic modifications)
- Cannot require organizational/enterprise-level settings
- Should not significantly impact startup time or performance
- Must be maintainable by users without extensive CLI/scripting knowledge

<!-- section_id: "60b0a853-7760-40c5-8df8-14a82de9241f" -->
## Assumptions

- Agent SDK with `systemPrompt` + `append: true` is viable and stable
- [CRITICAL] tag convention can be consistently applied in CLAUDE.md files
- Users will adopt wrapper script to launch Claude Code
- Rules can be safely extracted and injected without breaking tool definitions

<!-- section_id: "a8c94b6c-79a5-4f1d-9bcc-225a0f48261a" -->
## Research Basis

- Research findings in Stage 0_02_research: `claude_code_system_prompt_research_findings.md`
- Architecture analysis of Claude Code system prompt loading
- Evaluation of 4 different customization approaches
- Agent SDK documentation review

<!-- section_id: "8f5cb1d5-551d-42ce-b6f1-8a929cec8052" -->
## Strategic Dimensions

This root need decomposes into 4 overarching branches:

1. **O1: Rule Identification & Categorization** - How do we identify and understand what a critical rule is?
2. **O2: Rule Management** - How are critical rules stored, organized, extracted, and maintained?
3. **O3: Rule Enforcement** - How are critical rules guaranteed to execute?
4. **O4: Rule Verification & Compliance** - How do we know critical rules are working?

<!-- section_id: "c90582ac-3f3c-44f2-ab6c-3a72c15be8ae" -->
## Next Steps

Proceed to stage_0_02_research findings to inform detailed requirements in the overarching branches.

<!-- section_id: "938d93d2-16ac-40c5-9d12-58c45820969e" -->
## Navigation

- **Parent**: `../CLAUDE.md` (tree manager)
- **Children**: All O1-O4 overarching branches
- **Next**: `../O1_rule_identification_and_categorization/OVERARCHING_O1.md`
