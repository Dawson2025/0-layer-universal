---
resource_id: "dd9f8c0c-5d2f-4832-bc04-91871a42f240"
resource_type: "document"
resource_name: "ai-agent-setup"
---
# AI Agent Environment Configuration for This Project
*Trickle-Down Level 0.5: Environment-Specific Configuration*

<!-- section_id: "6ca0f059-79e4-466c-b7d3-55a863f2e9b5" -->
## This Project's Environment Choice: WSL Ubuntu

**Project-Specific Decision:** This Language Tracker project is being developed within a WSL Ubuntu environment.

**Important Context:** These environment rules apply because we CHOSE WSL Ubuntu for this project.
Other projects might use different environments (native Linux, macOS, native Windows, Docker, etc.)

<!-- section_id: "d7ff2f23-c3ea-48e0-9f9f-e2b60a6882e0" -->
## Environment Setup for AI Agents (WSL Ubuntu Context)

Since this project uses WSL Ubuntu, AI agents must adapt to this environment:

<!-- section_id: "8a2169cf-3394-430a-87cc-beb9f094bd4a" -->
### Warp AI Assistant (for this WSL Ubuntu project):
- Must enter WSL environment: wsl command if starting from Windows
- Add Warp integration: Auto-warpify configuration (as we did)
- Verify location: pwd should show /home/dawson/code/lang-trak-in-progress

<!-- section_id: "5c1014d1-a6fb-403b-b16b-bb305b82021c" -->
### Other AI Agents (Claude Code, Copilot, Cursor, etc.):
- Must work within this project's chosen WSL Ubuntu environment
- Project location: /home/dawson/code/lang-trak-in-progress/ (NOT Windows paths)
- Use WSL Ubuntu development tools (Node.js, Python, Firebase CLI, etc.)

<!-- section_id: "d4b3ed31-e557-48b3-a815-5acb011d4e2d" -->
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
