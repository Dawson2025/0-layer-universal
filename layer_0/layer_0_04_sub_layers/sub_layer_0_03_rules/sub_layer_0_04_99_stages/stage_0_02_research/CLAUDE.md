# stage_0_02_research

## Role

**Researcher** - Explores and documents approaches to system prompt customization and critical rules enforcement.

## Status

**ACTIVE** - Currently documenting research findings on Claude Code system prompt customization.

## Purpose

Research available techniques for injecting critical rules into the system prompt and bypassing the discretionary context wrapper. Document findings to inform architecture decisions.

## Key Research Areas

- Claude Code system prompt architecture and initialization process
- Anthropic's discretionary context disclaimer: purpose, implementation, scope
- Agent SDK customization approaches (`systemPrompt`, `append` flag)
- Output styles and managed settings alternatives
- Risk analysis for each approach

## Deliverables

**Location**: `outputs/`

- `claude_code_system_prompt_research_findings.md` - Comprehensive research document (~4000-5000 words)

## Key Findings (To Be Documented)

1. **The Discretionary Disclaimer**: Anthropic intentionally wraps user context with "may or may not be relevant"
2. **Why It Exists**: Training measure to prevent bloated CLAUDE.md files from overwhelming the model
3. **The Problem**: Prevents mandatory governance rules from being reliably enforced
4. **Available Solutions**:
   - Agent SDK `systemPrompt` + `append: true` (VIABLE)
   - Output styles (limited scope)
   - Managed settings (IT-controlled)
   - Custom systemPrompt replacement (risky)
5. **Proposed Solution**: Dynamic extraction of [CRITICAL] rules, injection into system prompt via Agent SDK

## Navigation

- **Parent**: `../CLAUDE.md` (Stages Manager)
- **Previous stage**: `../stage_0_01_request_gathering/`
- **Next stage**: `../stage_0_03_instructions/`
- **Research output**: `outputs/claude_code_system_prompt_research_findings.md`
