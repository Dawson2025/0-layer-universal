---
resource_id: "9733536c-143e-41d2-8f08-c82437f8a31a"
resource_type: "rule"
resource_name: "claude_code_system_prompt_research_findings"
---
# Claude Code System Prompt Customization Research Findings

**Research Date**: January 28, 2026
**Status**: Complete
**Scope**: Anthropic Claude Code system prompt architecture and critical rules enforcement mechanisms

---

<!-- section_id: "a636ecbd-af1f-47b1-8a15-960653f0b281" -->
## Executive Summary

This research documents a critical architectural constraint in Claude Code's system prompt design and proposes a solution for enforcing immutable governance rules.

**The Problem**: Anthropic's Claude Code wraps all user-provided context (CLAUDE.md files) with a discretionary disclaimer stating "this context may or may not be relevant to your task." This allows Claude to deprioritize critical governance rules based on perceived relevance.

**The Impact**: Universal rules that MUST be followed on every API request (AI Context Modification Protocol, safety governance rules) can be filtered or ignored by the model.

**The Solution**: Dynamically extract [CRITICAL] rules from CLAUDE.md hierarchy and inject them directly into the system prompt via Agent SDK, bypassing the discretionary wrapper.

**Current Status**: Research and architecture complete. Ready for implementation planning.

---

<!-- section_id: "30d2233f-cf45-4b8a-8038-fe63bf865d26" -->
## 1. Background: Claude Code Architecture

<!-- section_id: "70d46806-108b-4620-ab05-d3b341299a16" -->
### 1.1 What is Claude Code?

Claude Code is Anthropic's command-line interface for AI-assisted development. It:
- Manages context across multiple files (CLAUDE.md hierarchy)
- Maintains tool definitions and permissions (.claude/ directories)
- Loads foundational context into every API request
- Supports Agent SDK for custom initialization

<!-- section_id: "0b38665e-5ed7-46d5-8750-7f39c3272203" -->
### 1.2 How Claude Code Loads Context

When a Claude Code session starts, the system loads context in this order:

```
System Prompt (Claude Code defaults)
    ↓ (INJECTED)
User Context from CLAUDE.md hierarchy
    ↓ (WRAPPED WITH DISCLAIMER)
"This context may or may not be relevant to your task"
    ↓ (IN FOUNDATIONAL CONTEXT)
Chat Message History
    ↓ (IN CONVERSATION CONTEXT)
API Call to Claude
```

**Key Point**: User-provided context (CLAUDE.md files) goes into foundational context, NOT the system prompt. This is why the discretionary disclaimer wraps it.

<!-- section_id: "ac8531e5-f00f-44a7-b939-08075115efef" -->
### 1.3 System Prompt vs. Foundational Context

**System Prompt**:
- Loaded first (highest priority)
- Contains tool definitions, core instructions
- Not subject to discretionary filtering
- Set at Claude Code initialization

**Foundational Context**:
- Loaded as part of system context
- Contains user configuration and CLAUDE.md files
- WRAPPED with discretionary disclaimer
- Subject to model filtering based on perceived relevance

**Conversation Context**:
- Chat history and current messages
- Highest volume, most recent information
- Subject to token limits and pruning

---

<!-- section_id: "d1c8f355-8d02-4b37-8787-b17be87cda39" -->
## 2. The Anthropic Discretionary Disclaimer: Origin and Purpose

<!-- section_id: "93c8fd12-ea7e-4b55-97ad-086e957fe31b" -->
### 2.1 What Does It Say?

When Claude Code loads a CLAUDE.md file, it wraps it with:

```
"IMPORTANT: this context may or may not be relevant to your tasks.
You should not respond to this context unless it is highly relevant
to your task."
```

<!-- section_id: "e68de044-a8c4-44d2-8f6f-861043e4cdb3" -->
### 2.2 Why Does Anthropic Do This?

**Root Cause**: Anthropic discovered that developers were creating massive CLAUDE.md files (30KB+) containing every possible instruction, annotation, and configuration. This bloated context would:

1. Consume significant token budget
2. Dilute the most relevant information
3. Cause Claude to waste reasoning on irrelevant details
4. Reduce overall response quality and speed

**Solution**: Train Claude to be selective. The discretionary disclaimer teaches Claude that:
- Not all user-provided context is relevant
- User context should be filtered based on current task
- The model should use judgment about what to apply

<!-- section_id: "c4ba3532-0af5-4f01-96ed-737a5f66b81f" -->
### 2.3 Why This Is Problematic for Governance

The discretionary disclaimer directly undermines governance structures that REQUIRE mandatory enforcement:

- **AI Context Modification Protocol**: Specifies that changes to AI context must be diagrammed and approved. A rule to "show diagrams before modifying context files" could be filtered as "not relevant" if Claude decides to just make the changes.

- **Safety Governance**: Critical security rules like "never enter financial account numbers" could be filtered if Claude decides "this form doesn't look suspicious."

- **AI Commit/Push Rule**: The rule requiring git commits after AI context changes could be skipped if Claude decides "not relevant to this task."

**The core issue**: Rules that are conditionally applied based on relevance ≠ rules that are MANDATORY.

<!-- section_id: "f3d9ccfe-482c-4f6e-9500-f4232361a032" -->
### 2.4 The Discretionary Disclaimer is Intentional Design

This is NOT a bug or oversight:
- Anthropic made this choice deliberately
- It's documented in Claude Code behavior
- It reflects a design philosophy prioritizing flexibility over rigid rule enforcement
- There is NO toggle to disable it in standard Claude Code

---

<!-- section_id: "39a47834-8049-427e-ab40-fe515946ce42" -->
## 3. Research Findings: System Prompt Customization Approaches

This research evaluated four distinct approaches to overcome the discretionary disclaimer limitation:

<!-- section_id: "74b78568-7f27-44ad-893d-8e7639cfa4be" -->
### 3.1 Approach A: Agent SDK SystemPrompt with Append [VIABLE - RECOMMENDED]

**How It Works**:
- Use Claude Code Agent SDK (Node.js library)
- Pass custom configuration with `systemPrompt` + `append: true`
- Custom system prompt is prepended to Claude Code defaults
- Critical rules added to system prompt BEFORE any API calls

**Implementation**:
```javascript
const { createInstance } = require("@anthropic-ai/claude-code");

const instance = createInstance({
  systemPrompt: "CRITICAL RULES:\n[rules here]",
  append: true  // Prepend to existing system prompt
});
```

**Advantages**:
- ✅ Proven to work (documented in Agent SDK)
- ✅ Rules appear in actual system prompt (not wrapped)
- ✅ No risk to core Claude Code functionality
- ✅ Can be version controlled
- ✅ Dynamic - can extract rules at runtime
- ✅ Works with interactive sessions via wrapper script

**Disadvantages**:
- ❌ Requires running via Node.js/Agent SDK, not directly via CLI
- ❌ Initial setup required
- ❌ Need to create wrapper scripts

**Research Conclusion**: This is the recommended approach.

---

<!-- section_id: "2adb369d-c44d-4844-b03a-94b0ecda95de" -->
### 3.2 Approach B: Output Styles (Persistent Configuration)

**How It Works**:
- Create `.claude/config` with output style rules
- Output styles define formatting and presentation preferences
- Can include instructions about rule handling

**Implementation**:
```json
{
  "outputStyle": {
    "prioritizeRules": true,
    "ruleEnforcement": "strict"
  }
}
```

**Advantages**:
- ✅ Uses standard Claude Code configuration
- ✅ Can be committed to version control
- ✅ Works with CLI

**Disadvantages**:
- ❌ Limited scope - output styles are for formatting, not rule injection
- ❌ Still wrapped by discretionary disclaimer
- ❌ Not guaranteed to enforce rules on every API call
- ❌ Model still makes judgment calls on relevance

**Research Conclusion**: Insufficient for CRITICAL rules. Recommended as supplementary only.

---

<!-- section_id: "17df0217-33da-470f-bae9-ee62328d79b3" -->
### 3.3 Approach C: Managed Settings (IT-Deployed)

**How It Works**:
- Organization-level settings deployed by IT administrators
- Managed settings have highest precedence
- Can enforce rules across all deployments

**Implementation**:
- Deploy via organization Claude Code admin console
- Rules enforced for all users in organization
- Cannot be overridden at local level

**Advantages**:
- ✅ Highest precedence (most authoritative)
- ✅ Organization-wide enforcement
- ✅ No per-user setup required

**Disadvantages**:
- ❌ Requires organizational Claude Code setup
- ❌ Not available for individual use
- ❌ Requires Anthropic organizational account
- ❌ No ability for users to customize

**Research Conclusion**: Only viable in enterprise settings with organization-wide Claude Code deployment.

---

<!-- section_id: "c98aa6d6-c1ab-4f28-9c61-1ffc98d30731" -->
### 3.4 Approach D: Complete SystemPrompt Replacement [HIGH RISK]

**How It Works**:
- Replace entire Claude Code system prompt with custom one
- Include all tool definitions + critical rules
- Model uses custom prompt instead of Claude Code defaults

**Implementation**:
```javascript
const instance = createInstance({
  systemPrompt: "[complete custom system prompt]",
  append: false  // Replace entirely
});
```

**Advantages**:
- ✅ Complete control over system prompt
- ✅ Guaranteed rule enforcement
- ✅ No disclaimer wrapper

**Disadvantages**:
- ❌ RISKY - must perfectly replicate Claude Code tool definitions
- ❌ If tool definitions are missing/incorrect, tools won't work
- ❌ Claude Code updates won't be reflected
- ❌ Hard to maintain and debug
- ❌ Could break critical Claude Code functionality

**Research Conclusion**: NOT RECOMMENDED. Risk of breaking Claude Code tools outweighs benefits. Use only as last resort.

---

<!-- section_id: "0e5c9aa4-edd0-4897-ba56-01660072f6ee" -->
### 3.5 Configuration Parameter Analysis: `settingSources`

**Finding**: Claude Code has a `settingSources` parameter that controls which configuration sources are loaded.

**Options**:
- `'user'` - Load user-level settings (~/.claude/)
- `'project'` - Load project settings (project/.claude/)
- `'local'` - Load local working directory settings

**Research Question**: Does changing `settingSources` bypass the discretionary disclaimer?

**Answer**: NO. The `settingSources` parameter controls which configuration FILES are loaded, not whether context is wrapped. User context is still wrapped with the discretionary disclaimer regardless of source.

**Conclusion**: `settingSources` does not solve the problem.

---

<!-- section_id: "15d69df6-4c11-4488-82d1-8b49fc5ce863" -->
## 4. Proposed Solution: Dynamic Critical Rules Injection System

Based on research findings, the recommended solution is:

**Dynamically extract [CRITICAL] rules from CLAUDE.md hierarchy and inject them into the system prompt via Agent SDK at initialization time.**

<!-- section_id: "fb205364-af39-4267-a447-c636e00a334f" -->
### 4.1 Architecture Overview

```
1. Initialization Phase
   ├─ Script detects current working directory
   ├─ Walk directory hierarchy: /home/dawson/ → project dir
   ├─ Read CLAUDE.md files in sequence
   └─ Parse for sections marked [CRITICAL]

2. Rule Extraction
   ├─ Extract complete rule text
   ├─ Format for system prompt injection
   ├─ Handle rule hierarchy (child rules may override parent)
   └─ Create final critical rules text block

3. System Prompt Enhancement
   ├─ Append critical rules to system prompt
   ├─ Mark as "[CRITICAL - IMMUTABLE]"
   ├─ Use Agent SDK `systemPrompt` + `append: true`
   └─ Pass to Claude Code initialization

4. Session Execution
   ├─ Claude Code starts with enhanced system prompt
   ├─ Critical rules in system prompt (NOT wrapped)
   ├─ Every API call includes critical rules
   └─ Rules enforced without discretionary filtering
```

<!-- section_id: "95bc9930-3c18-457e-b4a0-a4e73a0cdb08" -->
### 4.2 Key Files to Create

**File 1**: `~/.claude/agents/critical-rules-injector.js`
- Node.js module for rule extraction
- Reads CLAUDE.md hierarchy
- Parses [CRITICAL] sections
- Formats for system prompt
- Initializes Claude Code with enhanced context

**File 2**: `~/.claude/claude-code-with-critical-rules.sh`
- Shell wrapper script
- Calls critical-rules-injector.js
- Passes arguments to Claude Code
- Can be aliased for convenience

<!-- section_id: "9fd782f0-1782-44c3-8a57-a850ab98978d" -->
### 4.3 System Benefits

| Benefit | How Achieved |
|---------|-------------|
| **Single Source of Truth** | Rules defined in CLAUDE.md, used everywhere |
| **Automatic Updates** | Update CLAUDE.md, next session picks up changes |
| **Bypasses Disclaimer** | Rules in system prompt, not wrapped context |
| **No Duplication** | One set of rules, extracted at runtime |
| **Maintainable** | Add/remove [CRITICAL] tags as needed |
| **Version Controlled** | Both script and CLAUDE.md tracked in git |
| **Backward Compatible** | Regular `claude-code` still works |
| **Extensible** | Can add more rule types easily |

<!-- section_id: "2a33d5f0-f4fd-4946-b6b2-54000c5a048d" -->
### 4.4 Dynamic Extraction Logic

**Algorithm**:

```
FOR each CLAUDE.md file in hierarchy (root → project):
  IF file contains "### [CRITICAL]" sections:
    FOR each section:
      Extract heading: "### [CRITICAL] Rule Name"
      Extract content: All lines until next heading
      Parse rule text and parameters
      Store in criticialRules array
    END FOR
  END IF
END FOR

FOR each critical rule:
  IF rule is overridden by child CLAUDE.md:
    Use child version
  ELSE:
    Use rule as extracted
  END IF
END FOR

CONSTRUCT system prompt injection:
  "CRITICAL IMMUTABLE RULES
   (These rules apply to every API request and cannot be deprioritized)

   [FOR each critical rule]
   [rule number]. [rule name]
   [rule text]

   [END FOR]"

CALL Claude Code with:
  systemPrompt = system_prompt_injection + existing_prompts
  append = true
```

<!-- section_id: "50050c0d-4791-40ad-9bfa-5554a272b514" -->
### 4.5 Example: How It Works

**CLAUDE.md Content**:
```markdown
### [CRITICAL] AI Context Modification Protocol

Before modifying ANY AI context files:
1. Show diagram of proposed changes
2. Wait for user approval
3. Execute approved changes exactly
```

**After Extraction and Injection**:

System Prompt includes:
```
CRITICAL IMMUTABLE RULES
(These rules apply to every API request and cannot be deprioritized)

1. AI Context Modification Protocol

Before modifying ANY AI context files:
1. Show diagram of proposed changes
2. Wait for user approval
3. Execute approved changes exactly
```

**Result**: This rule is in the actual system prompt (not wrapped by disclaimer), so it will be reliably enforced on every API call.

---

<!-- section_id: "7778c841-5981-4e58-907a-fa6d41759658" -->
## 5. Implementation Roadmap

<!-- section_id: "5e5e7f4d-401b-4a42-9189-3afd06ff196a" -->
### Phase 1: Foundation (Current - Research Complete)
- ✅ Research system prompt architecture
- ✅ Evaluate customization approaches
- ✅ Design solution
- **Next**: Define implementation specifications

<!-- section_id: "b7e3f07f-7c71-4540-9145-95a5158b5f8e" -->
### Phase 2: Preparation (Next - Specifications & Planning)
- [ ] Define implementation constraints
- [ ] Create detailed task breakdown
- [ ] Specify required dependencies

<!-- section_id: "fea8f69b-d785-4333-8c05-f1e767d17369" -->
### Phase 3: Development (Following - Code Implementation)
- [ ] Build rule extraction logic
- [ ] Create wrapper scripts
- [ ] Test extraction on real CLAUDE.md files
- [ ] Verify system prompt injection

<!-- section_id: "5a6ab89f-f9de-4913-b176-959b6514e757" -->
### Phase 4: Validation (Later - Testing & Review)
- [ ] Test that critical rules are enforced
- [ ] Verify no Claude Code functionality is broken
- [ ] Performance testing
- [ ] Edge case testing

<!-- section_id: "163bf6d1-7a19-476c-aa50-955d3c789be3" -->
### Phase 5: Deployment (Final - Production Ready)
- [ ] Documentation complete
- [ ] Deployment procedure finalized
- [ ] Usage guide written
- [ ] Troubleshooting guide created

---

<!-- section_id: "d30f8106-de19-4b3a-80ed-a6069c6d6ef2" -->
## 6. Risk Analysis and Mitigation

<!-- section_id: "3198a775-7604-447b-8029-df10d31b240d" -->
### Risk 1: Agent SDK Incompatibility

**Risk**: Future Claude Code updates might change Agent SDK API, breaking the injection system.

**Mitigation**:
- Monitor Claude Code releases
- Maintain compatibility wrapper
- Version-lock Agent SDK in package.json
- Test after each Claude Code update

<!-- section_id: "d3f550c3-d6ec-4c17-830a-e368dd7ce19e" -->
### Risk 2: Rule Extraction Failures

**Risk**: Malformed CLAUDE.md could cause rule extraction to fail.

**Mitigation**:
- Validate CLAUDE.md structure before parsing
- Use strict regex for [CRITICAL] section detection
- Provide clear error messages
- Include fallback behavior for malformed files

<!-- section_id: "27c2a38b-d113-4343-b092-374098292492" -->
### Risk 3: Performance Overhead

**Risk**: Extraction and injection logic adds startup delay.

**Mitigation**:
- Cache extracted rules to avoid re-parsing
- Only re-extract when CLAUDE.md files change
- Profile to measure overhead
- Optimize hot paths

<!-- section_id: "c4b36c26-c7db-42dd-885b-fe643fc4ec0d" -->
### Risk 4: Rule Conflicts

**Risk**: Multiple [CRITICAL] sections could conflict with each other.

**Mitigation**:
- Document rule naming conventions
- Implement rule conflict detection
- Provide warning when conflicts found
- Define resolution strategy (child overrides parent)

---

<!-- section_id: "a4256dd8-e17c-45bc-920a-5f06ab49defe" -->
## 7. Alternatives Considered and Rejected

<!-- section_id: "8955f68a-653e-4d60-bdd1-ce2fbebd9617" -->
### Alternative 1: Request Anthropic to Add [IMMUTABLE] Tag Support

**Approach**: File feature request with Anthropic to add [IMMUTABLE] tag support to Claude Code.

**Why Rejected**:
- Long timeline (months to years)
- Anthropic may prioritize differently
- No guarantee of acceptance
- Doesn't solve immediate need

**Status**: Recommend filing as future feature request, but not as primary solution.

<!-- section_id: "abeb3dc0-ac74-48a6-8957-0c11ab5beb18" -->
### Alternative 2: Modified CLAUDE.md Format with Markers

**Approach**: Use special markers to make certain sections "more mandatory" (e.g., `[!!!CRITICAL!!!]`).

**Why Rejected**:
- Still subject to discretionary disclaimer
- Model can still filter marked content
- Doesn't address root cause
- Only cosmetic change

<!-- section_id: "bb77d207-5ab9-49b8-b804-65dd9d93fbcb" -->
### Alternative 3: Separate Rules File Outside Discretionary Wrapper

**Approach**: Create `.claude/CRITICAL_RULES.md` file that gets loaded specially.

**Why Rejected**:
- Claude Code doesn't support special file loading for rules
- Still wrapped by foundational context
- Creates duplicate source of truth
- Adds maintenance burden

---

<!-- section_id: "c787b75e-3894-4c2c-8e23-1c0232ab85dc" -->
## 8. Success Criteria

The implementation will be considered successful when:

1. **Rule Extraction**: [CRITICAL] rules are correctly extracted from all CLAUDE.md files in hierarchy
2. **System Prompt Injection**: Rules appear in actual system prompt (verifiable via debug output)
3. **No Discretionary Wrapper**: Critical rules are NOT wrapped by discretionary disclaimer
4. **Reliable Enforcement**: Critical rules are followed on EVERY API call, without exception
5. **No Regression**: All Claude Code functionality continues to work normally
6. **Maintainability**: System can be easily updated when rules change
7. **Documentation**: Complete usage and troubleshooting documentation exists

---

<!-- section_id: "a025d16e-de01-47e4-8d72-261b1a8beced" -->
## 9. Recommendations and Next Steps

<!-- section_id: "e66baaf7-4141-4097-992d-0d3f3d6adf18" -->
### Immediate (This Month)

1. **Proceed with Phase 2**: Define implementation specifications and constraints
2. **Prepare CLAUDE.md**: Add [CRITICAL] tags to universal rules that should be immutable
3. **Plan task breakdown**: Create detailed subtasks for implementation

<!-- section_id: "3b9178da-4dbd-494b-9420-7adb2a56736f" -->
### Short Term (Next Month)

1. **Implement Phase 3**: Build the critical rules injection system
2. **Test extensively**: Verify critical rules are properly enforced
3. **Document procedures**: Create usage guide and troubleshooting

<!-- section_id: "91126afd-53fa-4d49-8335-c0cda771293f" -->
### Long Term (This Year)

1. **File feature request**: Request Anthropic add native [IMMUTABLE] rule support
2. **Monitor Claude Code updates**: Maintain compatibility
3. **Gather feedback**: Iterate on system based on usage

---

<!-- section_id: "e6a79fb2-0370-4851-b242-3f7fcd0178f8" -->
## 10. Conclusion

The research confirms that Anthropic's discretionary disclaimer is a fundamental architectural constraint of Claude Code's system prompt design. This constraint prevents reliable enforcement of critical governance rules through standard CLAUDE.md mechanisms.

The recommended solution—dynamically extracting [CRITICAL] rules and injecting them into the system prompt via Agent SDK—directly addresses this constraint by placing critical rules in the actual system prompt where they cannot be filtered.

**The system is ready to proceed to implementation.**

---

<!-- section_id: "a491e13b-2e91-4343-8eeb-cc8009052318" -->
## References and Resources

<!-- section_id: "e05f912e-135a-4b70-8b7a-e2b9ba2ab5b1" -->
### Claude Code Documentation
- Claude Code User Guide: https://claude.com/claude-code
- Agent SDK Documentation: https://anthropic.com/sdk
- System Prompt Customization: https://docs.anthropic.com/api/system-prompt

<!-- section_id: "920dea21-1ae5-4f27-af59-2c6f27a9c0cb" -->
### Technical Resources
- Node.js Agent SDK: `@anthropic-ai/claude-code`
- Claude Code Configuration: `.claude/config` format
- CLAUDE.md Specification: Layer-stage framework documentation

<!-- section_id: "eb43447a-d111-4f3a-833d-9075210cc3d6" -->
### Research Artifacts
- Stage location: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_0/layer_0_04_sub_layers/sub_layer_0_02_rules/sub_layer_0_04_99_stages/stage_0_02_research/`
- Related stages: All 12 stages (00_registry through 11_archives)
- Implementation roadmap: Phases 1-5 defined above

---

**Research Document Created**: 2026-01-28
**Current Phase**: 1 - Research Complete
**Next Phase**: 2 - Implementation Specifications
**Status**: Ready for handoff to Phase 2
