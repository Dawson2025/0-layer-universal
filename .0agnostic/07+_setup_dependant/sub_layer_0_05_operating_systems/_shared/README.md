---
resource_id: "519eb071-2beb-4846-926e-82bc70a946c1"
resource_type: "readme
document"
resource_name: "README"
---
# Cross-OS Setup (_shared)

This directory contains setup documentation that applies across **all operating systems**.

<!-- section_id: "cc7b668c-86ff-44ee-9495-48f91489f7c5" -->
## When to Use This Directory

Use this directory for:
- Setup steps that work identically on Linux, macOS, Windows, and WSL
- General configuration that doesn't depend on OS-specific tools
- Cross-platform tool setup (Node.js, Python, Git when using cross-platform patterns)
- Universal environment variables or configuration patterns

<!-- section_id: "45976601-c733-4ec1-9a04-a75428e8a3e1" -->
## When NOT to Use This Directory

Don't use this directory for:
- OS-specific package managers (apt, brew, winget)
- OS-specific paths or file structures
- OS-specific permissions or security models
- Platform-specific tools or dependencies

If setup varies by OS, place it in the specific OS directory instead.

<!-- section_id: "36e8a3b0-f742-41a1-a185-5e9fd9577793" -->
## Next Level

Navigate to `0.06_environments/` to continue down the setup hierarchy.


---

<!-- section_id: "54008768-59b3-4096-97bc-91bb7e5b3cb1" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/README.md`

# Sub Layer 0.05: OS Setup

**Purpose**: Operating system setup, configuration, and platform-specific issues.

<!-- section_id: "9605ba5f-67a6-420e-90e1-f44e5066fce7" -->
## ⚠️ Linux/Ubuntu-Specific MCP Issues

**CRITICAL**: If using Linux/Ubuntu with Cursor IDE and MCP servers, read:

- **[Linux/Ubuntu MCP Issues](trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md)**: OS-level MCP limitations and solutions

**Key Issues**:
- Browser path detection fails on Linux
- NVM/Node.js requires explicit configuration in MCP servers
- Display/graphics environment setup required
- File permissions and path conventions differ

<!-- section_id: "01ffad4e-5987-45ec-a451-308cce780ee1" -->
## Related Documentation

- **Cursor IDE Issues**: `../sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **AI Apps Issues**: `../sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`
- **Environment Setup (GitHub SSO / PAT)**: `../sub_layer_0_06_environment_setup/trickle_down_0.5_setup/0_instruction_docs/github/github_sso_token_setup.md`

<!-- section_id: "8f243a67-c7f0-4f46-a551-ec7c67b8da5a" -->
## Notes
- Add slot-specific docs here over time.
- Keep mappings up to date if paths change.
