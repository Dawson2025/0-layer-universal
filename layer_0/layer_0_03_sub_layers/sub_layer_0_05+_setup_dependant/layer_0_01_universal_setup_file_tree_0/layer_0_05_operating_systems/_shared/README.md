# Cross-OS Setup (_shared)

This directory contains setup documentation that applies across **all operating systems**.

## When to Use This Directory

Use this directory for:
- Setup steps that work identically on Linux, macOS, Windows, and WSL
- General configuration that doesn't depend on OS-specific tools
- Cross-platform tool setup (Node.js, Python, Git when using cross-platform patterns)
- Universal environment variables or configuration patterns

## When NOT to Use This Directory

Don't use this directory for:
- OS-specific package managers (apt, brew, winget)
- OS-specific paths or file structures
- OS-specific permissions or security models
- Platform-specific tools or dependencies

If setup varies by OS, place it in the specific OS directory instead.

## Next Level

Navigate to `0.06_environments/` to continue down the setup hierarchy.


---

## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0.05_os_setup/README.md`

# Sub Layer 0.05: OS Setup

**Purpose**: Operating system setup, configuration, and platform-specific issues.

## ⚠️ Linux/Ubuntu-Specific MCP Issues

**CRITICAL**: If using Linux/Ubuntu with Cursor IDE and MCP servers, read:

- **[Linux/Ubuntu MCP Issues](trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md)**: OS-level MCP limitations and solutions

**Key Issues**:
- Browser path detection fails on Linux
- NVM/Node.js requires explicit configuration in MCP servers
- Display/graphics environment setup required
- File permissions and path conventions differ

## Related Documentation

- **Cursor IDE Issues**: `../sub_layer_0.07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **AI Apps Issues**: `../sub_layer_0.09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0.10_mcp_servers_and_tools_setup/`
- **Environment Setup (GitHub SSO / PAT)**: `../sub_layer_0.06_environment_setup/trickle_down_0.5_setup/0_instruction_docs/github/github_sso_token_setup.md`

## Notes
- Add slot-specific docs here over time.
- Keep mappings up to date if paths change.
