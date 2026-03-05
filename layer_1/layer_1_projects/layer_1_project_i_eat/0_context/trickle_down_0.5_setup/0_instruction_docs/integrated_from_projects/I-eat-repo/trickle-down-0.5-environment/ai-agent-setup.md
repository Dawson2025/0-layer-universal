---
resource_id: "7d242a8f-914b-4a25-a3e3-7e19a6d5045c"
resource_type: "document"
resource_name: "ai-agent-setup"
---
# AI Agent Environment Configuration for This Project
*Trickle-Down Level 0.5: Environment-Specific Configuration*

<!-- section_id: "94aaa52d-2972-4d76-b686-85b35c6869ba" -->
## This Project's Environment Choice: WSL Ubuntu

**Project-Specific Decision:** This Language Tracker project is being developed within a WSL Ubuntu environment.

**Important Context:** These environment rules apply because we CHOSE WSL Ubuntu for this project.
Other projects might use different environments (native Linux, macOS, native Windows, Docker, etc.)

<!-- section_id: "6c97f5ba-5f33-4996-b7fd-c96066ae1ce7" -->
## Environment Setup for AI Agents (WSL Ubuntu Context)

Since this project uses WSL Ubuntu, AI agents must adapt to this environment:

<!-- section_id: "cf74e801-edd3-40bf-bf43-e69fd68f4581" -->
### Warp AI Assistant (for this WSL Ubuntu project):
- Must enter WSL environment: wsl command if starting from Windows
- Add Warp integration: Auto-warpify configuration (as we did)
- Verify location: pwd should show /home/dawson/dawson-workspace/code/lang-trak-in-progress

<!-- section_id: "3c5f9b19-d8e7-4609-9f48-d0fbee039072" -->
### Other AI Agents (Claude Code, Copilot, Cursor, etc.):
- Must work within this project's chosen WSL Ubuntu environment
- Project location: /home/dawson/dawson-workspace/code/lang-trak-in-progress/ (NOT Windows paths)
- Use WSL Ubuntu development tools (Node.js, Python, Firebase CLI, etc.)

<!-- section_id: "a15e38ae-0c5f-49dd-bb03-e745fb77758e" -->
## Why These Environment Rules Exist for THIS Project

**Project Decision:** We chose WSL Ubuntu because:
- Better performance for SQLite operations
- Optimal Firebase CLI and emulator performance
- Native Linux Python development environment
- Consistent team development environment

**Important Note:** If this were a different project using a different environment
(native Windows, macOS, Docker, etc.), the AI agent setup would be different.

---
*Environment: WSL Ubuntu (project-specific choice)*
*Project: Language Tracker*
