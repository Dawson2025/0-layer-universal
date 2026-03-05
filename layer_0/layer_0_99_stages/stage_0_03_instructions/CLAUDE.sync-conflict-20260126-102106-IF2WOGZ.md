---
resource_id: "543ee1e1-b9be-4d26-a689-8f66d8fd5c1f"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-102106-IF2WOGZ"
---
# Stage 01: Instructions

<!-- section_id: "29ae2efa-c327-4696-bf41-04f160ed4b00" -->
## Purpose
Define WHAT needs to be done. This stage transforms gathered requests into clear, actionable instructions and requirements documentation.

<!-- section_id: "8470e01a-b457-4db6-979c-82c9472663d5" -->
## Entry Criteria
- Request gathering complete
- Initial requirements captured
- Stakeholder availability confirmed

<!-- section_id: "acb67e5e-1dae-4706-a4fc-639200b9473e" -->
## Exit Criteria
- Clear instructions documented
- Scope explicitly defined
- Acceptance criteria established
- Handoff document prepared for Planning

<!-- section_id: "f9d95a47-d1b8-44b0-8ce0-308ede9358c8" -->
## Typical Tasks
- Analyze gathered requests
- Define clear requirements
- Document constraints and dependencies
- Identify success criteria
- Create instruction documents
- **Evaluate optimal OS/environment for the task** (see below)

<!-- section_id: "69180796-c263-47a1-809b-2e8f12a92e83" -->
## Environment Assessment Checklist

Before starting implementation, evaluate which OS/environment is best suited:

<!-- section_id: "efc80d1c-7006-404d-a627-79c85277825e" -->
### GUI Automation Tasks
| OS | Tool | Ease | Electron App Support |
|----|------|------|---------------------|
| **Windows** | AutoHotkey | ⭐⭐⭐ Best | ✅ Excellent |
| **macOS** | AppleScript | ⭐⭐ Medium | ⚠️ Fair |
| **Linux** | xdotool | ⭐ Lowest | ❌ Poor (Electron issues) |

**Key insight:** If task involves automating Electron apps (VS Code, Termius, Slack, Discord, etc.), **prefer Windows with AutoHotkey**.

<!-- section_id: "01c91833-cf73-4876-8ba3-eb2e633c6c8e" -->
### Development Tasks
- **Cross-platform CLI tools**: Any OS works
- **Linux-specific tools**: Use Linux or WSL
- **Windows-specific tools**: Use Windows
- **GPU-intensive (ML, Unreal)**: Check GPU passthrough support

<!-- section_id: "0d083f51-8d50-4e52-9677-0e5f495628a0" -->
### Questions to Ask
1. Does this task involve GUI automation? → Consider Windows
2. Is the target app Electron-based? → Strongly consider Windows
3. Are there CLI alternatives? → CLI is more portable than GUI automation
4. Is there an API? → API > GUI automation always
5. What OS has the best tooling for this specific task?

<!-- section_id: "18307ce3-e59e-4617-ab16-736de67254f1" -->
### Research Before Implementation
- Search for existing automation guides/scripts for the target application
- Check if CLI/API alternatives exist (often more reliable than GUI automation)
- Verify tool compatibility (e.g., xdotool doesn't work on Wayland)
- Document findings before proceeding

<!-- section_id: "1a1980b3-16f2-4060-aff2-aebbfc7c7551" -->
## Handoffs
- **From Previous (00_request_gathering)**: REQUEST_DOCUMENT
- **To Next (02_planning)**: INSTRUCTIONS document with requirements

<!-- section_id: "1dbf5d25-b50e-452f-b1b2-24459c3f23cb" -->
## Directory Structure
```
stage_0_03_instructions/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
└── hand_off_documents/   # Stage handoffs
```

<!-- section_id: "a40b5644-0a73-401a-9331-d5baa9a822f6" -->
## AI Agent Guidelines
When working in this stage:
- Transform vague requests into specific requirements
- Ensure requirements are testable
- Document all assumptions
- Identify gaps in requirements early
- Create clear, unambiguous instructions
