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

## Executive Summary

This research documents a critical architectural constraint in Claude Code's system prompt design and proposes a solution for enforcing immutable governance rules.

**The Problem**: Anthropic's Claude Code wraps all user-provided context (CLAUDE.md files) with a discretionary disclaimer stating "this context may or may not be relevant to your task." This allows Claude to deprioritize critical governance rules based on perceived relevance.

**The Impact**: Universal rules that MUST be followed on every API request (AI Context Modification Protocol, safety governance rules) can be filtered or ignored by the model.

**The Solution**: Dynamically extract [CRITICAL] rules from CLAUDE.md hierarchy and inject them directly into the system prompt via Agent SDK, bypassing the discretionary wrapper.

**Current Status**: Research and architecture complete. Ready for implementation planning.

---

## 1. Background: Claude Code Architecture

### 1.1 What is Claude Code?

Claude Code is Anthropic's command-line interface for AI-assisted development. It:
- Manages context across multiple files (CLAUDE.md hierarchy)
- Maintains tool definitions and permissions (.claude/ directories)
- Loads foundational context into every API request
- Supports Agent SDK for custom initialization

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

## 2. The Anthropic Discretionary Disclaimer: Origin and Purpose

### 2.1 What Does It Say?

When Claude Code loads a CLAUDE.md file, it wraps it with:

```
"IMPORTANT: this context may or may not be relevant to your tasks.
You should not respond to this context unless it is highly relevant
to your task."
```

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

### 2.3 Why This Is Problematic for Governance

The discretionary disclaimer directly undermines governance structures that REQUIRE mandatory enforcement:

- **AI Context Modification Protocol**: Specifies that changes to AI context must be diagrammed and approved. A rule to "show diagrams before modifying context files" could be filtered as "not relevant" if Claude decides to just make the changes.

- **Safety Governance**: Critical security rules like "never enter financial account numbers" could be filtered if Claude decides "this form doesn't look suspicious."

- **AI Commit/Push Rule**: The rule requiring git commits after AI context changes could be skipped if Claude decides "not relevant to this task."

**The core issue**: Rules that are conditionally applied based on relevance ≠ rules that are MANDATORY.

### 2.4 The Discretionary Disclaimer is Intentional Design

This is NOT a bug or oversight:
- Anthropic made this choice deliberately
- It's documented in Claude Code behavior
- It reflects a design philosophy prioritizing flexibility over rigid rule enforcement
- There is NO toggle to disable it in standard Claude Code

---

## 3. Research Findings: System Prompt Customization Approaches

This research evaluated four distinct approaches to overcome the discretionary disclaimer limitation:

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

## 4. Proposed Solution: Dynamic Critical Rules Injection System

Based on research findings, the recommended solution is:

**Dynamically extract [CRITICAL] rules from CLAUDE.md hierarchy and inject them into the system prompt via Agent SDK at initialization time.**

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

## 5. Implementation Roadmap

### Phase 1: Foundation (Current - Research Complete)
- ✅ Research system prompt architecture
- ✅ Evaluate customization approaches
- ✅ Design solution
- **Next**: Define implementation specifications

### Phase 2: Preparation (Next - Specifications & Planning)
- [ ] Define implementation constraints
- [ ] Create detailed task breakdown
- [ ] Specify required dependencies

### Phase 3: Development (Following - Code Implementation)
- [ ] Build rule extraction logic
- [ ] Create wrapper scripts
- [ ] Test extraction on real CLAUDE.md files
- [ ] Verify system prompt injection

### Phase 4: Validation (Later - Testing & Review)
- [ ] Test that critical rules are enforced
- [ ] Verify no Claude Code functionality is broken
- [ ] Performance testing
- [ ] Edge case testing

### Phase 5: Deployment (Final - Production Ready)
- [ ] Documentation complete
- [ ] Deployment procedure finalized
- [ ] Usage guide written
- [ ] Troubleshooting guide created

---

## 6. Risk Analysis and Mitigation

### Risk 1: Agent SDK Incompatibility

**Risk**: Future Claude Code updates might change Agent SDK API, breaking the injection system.

**Mitigation**:
- Monitor Claude Code releases
- Maintain compatibility wrapper
- Version-lock Agent SDK in package.json
- Test after each Claude Code update

### Risk 2: Rule Extraction Failures

**Risk**: Malformed CLAUDE.md could cause rule extraction to fail.

**Mitigation**:
- Validate CLAUDE.md structure before parsing
- Use strict regex for [CRITICAL] section detection
- Provide clear error messages
- Include fallback behavior for malformed files

### Risk 3: Performance Overhead

**Risk**: Extraction and injection logic adds startup delay.

**Mitigation**:
- Cache extracted rules to avoid re-parsing
- Only re-extract when CLAUDE.md files change
- Profile to measure overhead
- Optimize hot paths

### Risk 4: Rule Conflicts

**Risk**: Multiple [CRITICAL] sections could conflict with each other.

**Mitigation**:
- Document rule naming conventions
- Implement rule conflict detection
- Provide warning when conflicts found
- Define resolution strategy (child overrides parent)

---

## 7. Alternatives Considered and Rejected

### Alternative 1: Request Anthropic to Add [IMMUTABLE] Tag Support

**Approach**: File feature request with Anthropic to add [IMMUTABLE] tag support to Claude Code.

**Why Rejected**:
- Long timeline (months to years)
- Anthropic may prioritize differently
- No guarantee of acceptance
- Doesn't solve immediate need

**Status**: Recommend filing as future feature request, but not as primary solution.

### Alternative 2: Modified CLAUDE.md Format with Markers

**Approach**: Use special markers to make certain sections "more mandatory" (e.g., `[!!!CRITICAL!!!]`).

**Why Rejected**:
- Still subject to discretionary disclaimer
- Model can still filter marked content
- Doesn't address root cause
- Only cosmetic change

### Alternative 3: Separate Rules File Outside Discretionary Wrapper

**Approach**: Create `.claude/CRITICAL_RULES.md` file that gets loaded specially.

**Why Rejected**:
- Claude Code doesn't support special file loading for rules
- Still wrapped by foundational context
- Creates duplicate source of truth
- Adds maintenance burden

---

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

## 9. Recommendations and Next Steps

### Immediate (This Month)

1. **Proceed with Phase 2**: Define implementation specifications and constraints
2. **Prepare CLAUDE.md**: Add [CRITICAL] tags to universal rules that should be immutable
3. **Plan task breakdown**: Create detailed subtasks for implementation

### Short Term (Next Month)

1. **Implement Phase 3**: Build the critical rules injection system
2. **Test extensively**: Verify critical rules are properly enforced
3. **Document procedures**: Create usage guide and troubleshooting

### Long Term (This Year)

1. **File feature request**: Request Anthropic add native [IMMUTABLE] rule support
2. **Monitor Claude Code updates**: Maintain compatibility
3. **Gather feedback**: Iterate on system based on usage

---

## 10. Conclusion

The research confirms that Anthropic's discretionary disclaimer is a fundamental architectural constraint of Claude Code's system prompt design. This constraint prevents reliable enforcement of critical governance rules through standard CLAUDE.md mechanisms.

The recommended solution—dynamically extracting [CRITICAL] rules and injecting them into the system prompt via Agent SDK—directly addresses this constraint by placing critical rules in the actual system prompt where they cannot be filtered.

**The system is ready to proceed to implementation.**

---

## References and Resources

### Claude Code Documentation
- Claude Code User Guide: https://claude.com/claude-code
- Agent SDK Documentation: https://anthropic.com/sdk
- System Prompt Customization: https://docs.anthropic.com/api/system-prompt

### Technical Resources
- Node.js Agent SDK: `@anthropic-ai/claude-code`
- Claude Code Configuration: `.claude/config` format
- CLAUDE.md Specification: Layer-stage framework documentation

### Research Artifacts
- Stage location: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_0/layer_0_04_sub_layers/sub_layer_0_02_rules/sub_layer_0_04_99_stages/stage_0_02_research/`
- Related stages: All 12 stages (00_registry through 11_archives)
- Implementation roadmap: Phases 1-5 defined above

---

**Research Document Created**: 2026-01-28
**Current Phase**: 1 - Research Complete
**Next Phase**: 2 - Implementation Specifications
**Status**: Ready for handoff to Phase 2
