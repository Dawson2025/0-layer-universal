---
resource_id: "afdefad9-2b33-44ca-961d-3ca3efa86142"
resource_type: "document"
resource_name: "ai-agent-setup"
---
# AI Agent Environment Configuration for This Project
*Trickle-Down Level 0.5: Environment-Specific Configuration*

<!-- section_id: "77237533-d2f2-4f97-a897-1848668e1a76" -->
## This Project's Environment Choice: WSL Ubuntu

**Project-Specific Decision:** This Language Tracker project is being developed within a WSL Ubuntu environment.

**Important Context:** These environment rules apply because we CHOSE WSL Ubuntu for this project.
Other projects might use different environments (native Linux, macOS, native Windows, Docker, etc.)

<!-- section_id: "48af5d4f-69f5-43da-ae09-05135dd7641d" -->
## Environment Setup for AI Agents (WSL Ubuntu Context)

Since this project uses WSL Ubuntu, AI agents must adapt to this environment:

<!-- section_id: "88b707bc-89e8-43f1-9941-78f5c84dfbce" -->
### Warp AI Assistant (for this WSL Ubuntu project):
- Must enter WSL environment: wsl command if starting from Windows
- Add Warp integration: Auto-warpify configuration (as we did)
- Verify location: pwd should show /home/dawson/code/lang-trak-in-progress

<!-- section_id: "148ae1af-b73a-4669-80d9-1eb83167fb72" -->
### Other AI Agents (Claude Code, Copilot, Cursor, etc.):
- Must work within this project's chosen WSL Ubuntu environment
- Project location: /home/dawson/code/lang-trak-in-progress/ (NOT Windows paths)
- Use WSL Ubuntu development tools (Node.js, Python, Firebase CLI, etc.)

<!-- section_id: "6c83fd72-4286-45e9-be99-1186b1fdb3eb" -->
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
