---
resource_id: "1df569a3-45c9-47c4-bec8-e2fbd7cc7890"
resource_type: "document"
resource_name: "ai-agent-setup"
---
# AI Agent Environment Configuration for This Project
*Trickle-Down Level 0.5: Environment-Specific Configuration*

<!-- section_id: "02773cc6-e8e3-4003-984d-9c22430201c5" -->
## This Project's Environment Choice: WSL Ubuntu

**Project-Specific Decision:** This Language Tracker project is being developed within a WSL Ubuntu environment.

**Important Context:** These environment rules apply because we CHOSE WSL Ubuntu for this project.
Other projects might use different environments (native Linux, macOS, native Windows, Docker, etc.)

<!-- section_id: "c59ce42b-b274-4613-8548-6d4d78f5a019" -->
## Environment Setup for AI Agents (WSL Ubuntu Context)

Since this project uses WSL Ubuntu, AI agents must adapt to this environment:

<!-- section_id: "44a388ac-55f4-4174-aecb-0c900be6ad18" -->
### Warp AI Assistant (for this WSL Ubuntu project):
- Must enter WSL environment: wsl command if starting from Windows
- Add Warp integration: Auto-warpify configuration (as we did)
- Verify location: pwd should show /home/dawson/code/lang-trak-in-progress

<!-- section_id: "220e4bc8-4acd-4663-abc1-8cc25dae0bfd" -->
### Other AI Agents (Claude Code, Copilot, Cursor, etc.):
- Must work within this project's chosen WSL Ubuntu environment
- Project location: /home/dawson/code/lang-trak-in-progress/ (NOT Windows paths)
- Use WSL Ubuntu development tools (Node.js, Python, Firebase CLI, etc.)

<!-- section_id: "21f8360e-bf28-4096-90cb-b98e92a5509f" -->
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
