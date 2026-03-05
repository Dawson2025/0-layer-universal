---
resource_id: "8df131e3-cc78-4391-b6ff-44e18892884b"
resource_type: "readme
rule"
resource_name: "README"
---
# Universal Rules Sublayer - Stage Structure

<!-- section_id: "cffbc01c-2ed4-4ec2-a9b4-d1b2ff6edcf7" -->
## Overview

This directory contains the stage-based development structure for universal rules research, design, implementation, and deployment.

<!-- section_id: "25ddf1d8-4db2-486e-952e-57b61a60bb4e" -->
## Purpose

The universal rules system needs to overcome Anthropic's discretionary context wrapper that allows critical governance rules to be deprioritized. This staged approach documents the research, designs the solution, and tracks implementation.

<!-- section_id: "5bf66006-fa34-46cc-8ef5-45e1912cf526" -->
## Stage Directories

Each stage directory contains:

- `CLAUDE.md` - Stage-specific context and role
- `hand_off_documents/` - Communication between stages (incoming/outgoing)
- `outputs/` - Deliverables, research, documentation
- `ai_agent_system/` - Agent-specific configuration for stage

<!-- section_id: "07dad005-b599-49ee-bba1-29637ac34fc1" -->
## Current Stage: 02_research

**Location**: `stage_0_02_research/outputs/`

**Deliverable**:
- `claude_code_system_prompt_research_findings.md` - Comprehensive research on system prompt customization approaches

**Key topics**:
- Anthropic's discretionary disclaimer and why it exists
- Claude Code system prompt architecture and initialization
- Available customization approaches (Agent SDK, output styles, managed settings)
- Proposed solution: Dynamic critical rules injection
- Implementation architecture and benefits

<!-- section_id: "9f3335e5-d6ae-4ff4-8512-4a6cd436edf8" -->
## Stage Progression

```
01_request_gathering
    ↓ (Problem defined: discretionary disclaimer prevents rule enforcement)
02_research (CURRENT)
    ↓ (Research findings documented)
03_instructions
    ↓ (Implementation constraints defined)
04_design
    ↓ (Architecture finalized)
05_planning
    ↓ (Tasks broken into subtasks)
06_development
    ↓ (Code written and integrated)
07_testing
    ↓ (Rules verified as immutable)
08_criticism
    ↓ (Review and feedback)
09_fixing
    ↓ (Issues addressed)
10_current_product (DELIVERABLE)
    ↓ (Ready for deployment)
11_archives (HISTORY)
```

<!-- section_id: "f0bad3e9-c710-44b3-a81d-8d445f001657" -->
## Key Concepts

**Problem Being Solved**:
- Claude Code wraps user-provided CLAUDE.md content with: "this context may or may not be relevant to your task"
- This allows Claude to deprioritize critical governance rules
- Critical rules (AI Context Modification Protocol, safety governance) must not be deprioritizable

**Solution Approach**:
- Extract [CRITICAL] rules from CLAUDE.md hierarchy dynamically
- Inject critical rules directly into the system prompt (not wrapped foundational context)
- Create wrapper scripts and initialization logic to apply on every session

<!-- section_id: "6c278551-fe20-490b-b7c2-569dbb623692" -->
## Navigation

- **Parent**: `../CLAUDE.md`
- **Research output**: `stage_0_02_research/outputs/claude_code_system_prompt_research_findings.md`
- **Status**: See `status.json` for current stage tracking
