---
resource_id: "a9b4b576-30d8-4431-8728-97fccc22590c"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-035819-IF2WOGZ"
---
# Stage 01: Instructions

<!-- section_id: "ca0dd35b-3b61-48b7-871a-209789f71dcd" -->
## Purpose
Define WHAT needs to be done. This stage transforms gathered requests into clear, actionable instructions and requirements documentation.

<!-- section_id: "840850c5-abfd-4429-83a2-0a9c9f9c946e" -->
## Entry Criteria
- Request gathering complete
- Initial requirements captured
- Stakeholder availability confirmed

<!-- section_id: "94a50fdb-0816-4fd8-8adc-d656163fd66c" -->
## Exit Criteria
- Clear instructions documented
- Scope explicitly defined
- Acceptance criteria established
- Handoff document prepared for Planning

<!-- section_id: "caa7b5ed-6063-4f80-bc7d-cf6ed51cb165" -->
## Typical Tasks
- Analyze gathered requests
- Define clear requirements
- Document constraints and dependencies
- Identify success criteria
- Create instruction documents
- **Evaluate optimal OS/environment for the task** (see below)

<!-- section_id: "8ebe9cc6-4f7b-4a5a-a4b7-e1395d844c22" -->
## Environment Assessment Checklist

Before starting implementation, evaluate which OS/environment is best suited:

<!-- section_id: "92d9c37b-9de7-40f9-aee4-d3884eaac928" -->
### GUI Automation Tasks
| OS | Tool | Ease | Electron App Support |
|----|------|------|---------------------|
| **Windows** | AutoHotkey | ⭐⭐⭐ Best | ✅ Excellent |
| **macOS** | AppleScript | ⭐⭐ Medium | ⚠️ Fair |
| **Linux** | xdotool | ⭐ Lowest | ❌ Poor (Electron issues) |

**Key insight:** If task involves automating Electron apps (VS Code, Termius, Slack, Discord, etc.), **prefer Windows with AutoHotkey**.

<!-- section_id: "d9e115a0-0fdf-4601-81f7-91dea2aef42d" -->
### Development Tasks
- **Cross-platform CLI tools**: Any OS works
- **Linux-specific tools**: Use Linux or WSL
- **Windows-specific tools**: Use Windows
- **GPU-intensive (ML, Unreal)**: Check GPU passthrough support

<!-- section_id: "ad40611a-1752-473e-a8af-74169baebb8a" -->
### Questions to Ask
1. Does this task involve GUI automation? → Consider Windows
2. Is the target app Electron-based? → Strongly consider Windows
3. Are there CLI alternatives? → CLI is more portable than GUI automation
4. Is there an API? → API > GUI automation always
5. What OS has the best tooling for this specific task?

<!-- section_id: "bf9a9cdc-8caa-4457-8408-b25dc334470d" -->
### Research Before Implementation
- Search for existing automation guides/scripts for the target application
- Check if CLI/API alternatives exist (often more reliable than GUI automation)
- Verify tool compatibility (e.g., xdotool doesn't work on Wayland)
- Document findings before proceeding

<!-- section_id: "3fca06de-059f-4a8a-b056-9ddfb8ca910c" -->
## Handoffs
- **From Previous (00_request_gathering)**: REQUEST_DOCUMENT
- **To Next (02_planning)**: INSTRUCTIONS document with requirements

<!-- section_id: "b5d1c8bd-bcea-46ea-a093-d256a260dffa" -->
## Directory Structure
```
stage_0_03_instructions/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
└── hand_off_documents/   # Stage handoffs
```

<!-- section_id: "c9fcba10-596e-4e4c-8d25-048b22de3f3f" -->
## AI Agent Guidelines
When working in this stage:
- Transform vague requests into specific requirements
- Ensure requirements are testable
- Document all assumptions
- Identify gaps in requirements early
- Create clear, unambiguous instructions
