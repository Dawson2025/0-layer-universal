---
resource_id: "543ee1e1-b9be-4d26-a689-8f66d8fd5c1f"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-102106-IF2WOGZ"
---
# Stage 01: Instructions

## Purpose
Define WHAT needs to be done. This stage transforms gathered requests into clear, actionable instructions and requirements documentation.

## Entry Criteria
- Request gathering complete
- Initial requirements captured
- Stakeholder availability confirmed

## Exit Criteria
- Clear instructions documented
- Scope explicitly defined
- Acceptance criteria established
- Handoff document prepared for Planning

## Typical Tasks
- Analyze gathered requests
- Define clear requirements
- Document constraints and dependencies
- Identify success criteria
- Create instruction documents
- **Evaluate optimal OS/environment for the task** (see below)

## Environment Assessment Checklist

Before starting implementation, evaluate which OS/environment is best suited:

### GUI Automation Tasks
| OS | Tool | Ease | Electron App Support |
|----|------|------|---------------------|
| **Windows** | AutoHotkey | ⭐⭐⭐ Best | ✅ Excellent |
| **macOS** | AppleScript | ⭐⭐ Medium | ⚠️ Fair |
| **Linux** | xdotool | ⭐ Lowest | ❌ Poor (Electron issues) |

**Key insight:** If task involves automating Electron apps (VS Code, Termius, Slack, Discord, etc.), **prefer Windows with AutoHotkey**.

### Development Tasks
- **Cross-platform CLI tools**: Any OS works
- **Linux-specific tools**: Use Linux or WSL
- **Windows-specific tools**: Use Windows
- **GPU-intensive (ML, Unreal)**: Check GPU passthrough support

### Questions to Ask
1. Does this task involve GUI automation? → Consider Windows
2. Is the target app Electron-based? → Strongly consider Windows
3. Are there CLI alternatives? → CLI is more portable than GUI automation
4. Is there an API? → API > GUI automation always
5. What OS has the best tooling for this specific task?

### Research Before Implementation
- Search for existing automation guides/scripts for the target application
- Check if CLI/API alternatives exist (often more reliable than GUI automation)
- Verify tool compatibility (e.g., xdotool doesn't work on Wayland)
- Document findings before proceeding

## Handoffs
- **From Previous (00_request_gathering)**: REQUEST_DOCUMENT
- **To Next (02_planning)**: INSTRUCTIONS document with requirements

## Directory Structure
```
stage_0_03_instructions/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
└── hand_off_documents/   # Stage handoffs
```

## AI Agent Guidelines
When working in this stage:
- Transform vague requests into specific requirements
- Ensure requirements are testable
- Document all assumptions
- Identify gaps in requirements early
- Create clear, unambiguous instructions
