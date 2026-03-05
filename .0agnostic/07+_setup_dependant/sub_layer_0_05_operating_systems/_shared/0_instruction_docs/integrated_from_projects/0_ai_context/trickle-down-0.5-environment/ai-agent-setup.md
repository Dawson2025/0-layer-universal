---
resource_id: "3e4f3bf1-aee4-4f69-b330-103997a80305"
resource_type: "document"
resource_name: "ai-agent-setup"
---
# AI Agent Environment Configuration for This Project
*Trickle-Down Level 0.5: Environment-Specific Configuration*

<!-- section_id: "25e2d4bb-7f0d-48e2-ba85-dcaf77495ef2" -->
## This Project's Environment Choice: WSL Ubuntu

**Project-Specific Decision:** This Language Tracker project is being developed within a WSL Ubuntu environment.

**Important Context:** These environment rules apply because we CHOSE WSL Ubuntu for this project.
Other projects might use different environments (native Linux, macOS, native Windows, Docker, etc.)

<!-- section_id: "a0da0aac-1592-4aa8-88c2-fcf486311f29" -->
## Environment Setup for AI Agents (WSL Ubuntu Context)

Since this project uses WSL Ubuntu, AI agents must adapt to this environment:

<!-- section_id: "4ee3e8f3-b363-4a25-a649-f25d00169c44" -->
### Warp AI Assistant (for this WSL Ubuntu project):
- Must enter WSL environment: wsl command if starting from Windows
- Add Warp integration: Auto-warpify configuration (as we did)
- Verify location: pwd should show /home/dawson/code/lang-trak-in-progress

<!-- section_id: "f5b29c1c-d9d3-4725-b190-994c5951f115" -->
### Other AI Agents (Claude Code, Copilot, Cursor, etc.):
- Must work within this project's chosen WSL Ubuntu environment
- Project location: /home/dawson/code/lang-trak-in-progress/ (NOT Windows paths)
- Use WSL Ubuntu development tools (Node.js, Python, Firebase CLI, etc.)

<!-- section_id: "4612d63b-4fdd-42fa-ae69-7413e992d5fd" -->
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
