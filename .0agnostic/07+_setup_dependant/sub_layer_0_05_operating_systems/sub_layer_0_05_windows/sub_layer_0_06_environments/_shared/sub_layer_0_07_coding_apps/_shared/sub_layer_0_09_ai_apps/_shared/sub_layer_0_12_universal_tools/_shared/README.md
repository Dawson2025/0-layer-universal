---
resource_id: "f45cf186-7507-448d-82da-dcf55d3222a4"
resource_type: "readme
document"
resource_name: "README"
---
# ⚠️ DEPRECATED - This Sublayer Has Been Consolidated

**Deprecation Date**: 2026-01-01
**Replaced By**: `sub_layer_0_05-0.014_setup`

This sublayer has been consolidated into the unified setup sublayer for better organization and discoverability.

<!-- section_id: "f36dfe50-6911-45c3-ae28-31aae9ab6e47" -->
## Migration Path

All setup documentation is now located in:
```
sub_layer_0_05-0.014_setup/0.01_universal_setup_file_tree_0/
```

Navigate the file tree by your configuration:
1. Choose your OS: `0.05_operating_systems/<os>/`
2. Choose your environment: `0.06_environments/<env>/`
3. Choose your coding app: `0.07_coding_apps/<app>/`
4. Continue through all levels to find your specific setup documentation

<!-- section_id: "c716fab3-b66b-4248-b2fe-c29ba5cfcc6b" -->
## Why Consolidate?

- **Single entry point** for all setup docs
- **Better discoverability** through hierarchical file tree
- **Cross-cutting organization** with `_shared/` folders at every level
- **Easier maintenance** - one structure instead of 10

<!-- section_id: "3c18b909-ff53-4a56-a082-0f901967e051" -->
## Legacy Content Below

The original content of this sublayer is preserved below for reference, but should not be updated. All new setup documentation should go into the consolidated sublayer.

---

# sub_layer_0_12_universal_tools

**Purpose**: Cross-project scripts, utilities, and universal tools.

<!-- section_id: "6358eca6-0e0b-4922-ad6a-41a35a1339ad" -->
## Overview

This sublayer contains universal tools, scripts, and utilities that can be used across multiple projects. This includes browser automation tools, Claude Code configuration, AI development frameworks, and other cross-cutting utilities.

<!-- section_id: "61a132b7-1a3d-49cf-af56-97902b23fc01" -->
## Structure

```
sub_layer_0_12_universal_tools/
└── trickle_down_0.75_universal_tools/
    └── 0_instruction_docs/
        ├── browser-automation/
        ├── claude-code-config/
        ├── ai-development-frameworks/
        ├── platform-version-control/
        └── ...
```

<!-- section_id: "ab92ac2d-9e8e-4e8b-adc4-c274384da39d" -->
## Relationship to Other Sublayers

- **Depends on**:
  - `sub_layer_0_09_ai_apps_tools_setup` - Tools may require AI apps to be set up first
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some tools may use MCP servers
- **Provides to**: All layers that need universal utilities and scripts

<!-- section_id: "b966e17e-7d72-4e26-a07a-4678ce6d3ca9" -->
## Tool Context Files and OS Variants

Universal tools integrate with the **OS Variant and Quartet Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "a29aea91-08d0-4fa7-aed6-eb9a8babdbbe" -->
### Quartet Pattern Overview

Each layer/stage location can have OS-specific context files organized as **quartets** (or N-tuples):

- `CLAUDE.md` - Claude Code specific instructions
- `AGENTS.md` - General agent instructions (Codex CLI, etc.)
- `GEMINI.md` - Gemini CLI specific instructions
- `.cursor/rules/*.mdc` - Cursor IDE rules (future)

These files are organized under `os/<os-id>/` directories where `<os-id>` can be:
- `wsl` - Windows Subsystem for Linux
- `linux_ubuntu` - Native Ubuntu Linux
- `windows` - Native Windows
- `macos` - macOS
- Custom variants as needed

<!-- section_id: "624bce9f-7b9f-4467-a8a3-3fdd3cb8d2e1" -->
### Implementation Locations

OS variant context files have been implemented at:
- `layer_0/layer_0_99_stages/stage_0_03_instructions/ai_agent_system/os/`
- `layer_1_project/1.99_stages/stage_1.01_instructions/ai_agent_system/os/`
- `layer_2_features/2.99_stages/stage_2.01_instructions/ai_agent_system/os/`
- `layer_3_components/3.99_stages/stage_3.01_instructions/ai_agent_system/os/`

<!-- section_id: "83d64305-c21c-46a1-bda1-bfeee17cb12a" -->
### Tool-Specific Context

Universal tools should be aware of:
- **OS detection**: Supervisors detect OS and select appropriate context
- **Context cascade**: Layer N inherits from Layer 0...N-1
- **Tool specialization**: Each tool reads its specific context file
- **Extensibility**: New tools add their own context file pattern to the quartet/N-tuple

<!-- section_id: "daf3f736-c4ab-40b6-a079-53a36a863c2f" -->
## Key Documentation

- **[Browser Automation](trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/README.md)**: Browser automation tools and guides
- **[Claude Code Config](trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md)**: Claude Code CLI configuration
- **[AI Development Frameworks](trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/README.md)**: AI coding assistant frameworks

<!-- section_id: "3626372e-e6db-4cc4-8b95-c99f3a73f571" -->
## AI Manager Hierarchy Integration

This sub-layer integrates with the AI Manager Hierarchy System for orchestration and CLI patterns:

<!-- section_id: "241a0cd0-24ab-4591-9883-c902099fbbbe" -->
### Framework Orchestration
For guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the hierarchy, see:
- **[Framework Orchestration Overview](../sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md)**: When to use framework-based orchestration vs. simple handoff coordination
- **Existing Framework Docs**: `trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/` (complementary guidance on Spec Kit, BMAD Method, and AI coding assistants)

<!-- section_id: "249c6dcf-11dd-4e80-8da7-731219c38f29" -->
### CLI Recursion Patterns
For patterns on using CLI recursion to spawn deep agent hierarchies, see:
- **[CLI Recursion Syntax](../sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md)**: Concrete examples of managers spawning workers via Claude Code, Codex CLI, and Gemini CLI
- OS-adapted examples for WSL/Ubuntu
- Tool selection, parallel execution, and error handling patterns

<!-- section_id: "e2edeb93-9685-4c9e-8535-6857eea49553" -->
## ⚠️ Linux/Ubuntu-Specific Tool Access Issues

**CRITICAL**: Universal tools that depend on MCP have Linux-specific limitations. Read:

- **[Linux/Ubuntu Tool Access Issues](trickle_down_0.75_universal_tools/0_instruction_docs/LINUX_UBUNTU_TOOL_ACCESS_ISSUES.md)**: Universal tool access limitations on Linux

**Key Issues**:
- Browser automation tools must use `mcp_browser_*` instead of `mcp_playwright_*`
- Development frameworks need Linux-specific adaptations
- Cross-cutting utilities may require tool name updates
- Tool migration guide available for Playwright → Browser MCP

**Related Documentation**:
- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `../sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "931d6aad-d21c-4f24-825b-44f44f1dc679" -->
## Notes

- MCP-related tools have been moved to `sub_layer_0_10_mcp_servers_and_tools_setup`
- Universal tools are used by agents configured in `sub_layer_0_13_agent_setup`
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0


---

<!-- section_id: "a4faf633-8673-437f-9543-d331afc5ef7e" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/README.md`

# sub_layer_0_12_universal_tools

**Purpose**: Cross-project scripts, utilities, and universal tools.

<!-- section_id: "240d3089-1306-4b84-9cd3-94743aec54bf" -->
## Overview

This sublayer contains universal tools, scripts, and utilities that can be used across multiple projects. This includes browser automation tools, Claude Code configuration, AI development frameworks, and other cross-cutting utilities.

<!-- section_id: "91c4d1fe-52fa-4469-a6ea-b8134c8b36a5" -->
## Structure

```
sub_layer_0_12_universal_tools/
└── trickle_down_0.75_universal_tools/
    └── 0_instruction_docs/
        ├── browser-automation/
        ├── claude-code-config/
        ├── ai-development-frameworks/
        ├── platform-version-control/
        └── ...
```

<!-- section_id: "803c1a9e-c2ff-4319-91d6-d66b77bffca8" -->
## Relationship to Other Sublayers

- **Depends on**:
  - `sub_layer_0_09_ai_apps_tools_setup` - Tools may require AI apps to be set up first
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some tools may use MCP servers
- **Provides to**: All layers that need universal utilities and scripts

<!-- section_id: "a54ea062-620c-4fc1-b786-f3a81f62d6dd" -->
## Tool Context Files and OS Variants

Universal tools integrate with the **OS Variant and Quartet Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "b85dcbfc-4deb-4179-a5c0-301215b1c3ce" -->
### Quartet Pattern Overview

Each layer/stage location can have OS-specific context files organized as **quartets** (or N-tuples):

- `CLAUDE.md` - Claude Code specific instructions
- `AGENTS.md` - General agent instructions (Codex CLI, etc.)
- `GEMINI.md` - Gemini CLI specific instructions
- `.cursor/rules/*.mdc` - Cursor IDE rules (future)

These files are organized under `os/<os-id>/` directories where `<os-id>` can be:
- `wsl` - Windows Subsystem for Linux
- `linux_ubuntu` - Native Ubuntu Linux
- `windows` - Native Windows
- `macos` - macOS
- Custom variants as needed

<!-- section_id: "3c0d936d-e541-43ce-8e48-1edbcd5ac519" -->
### Implementation Locations

OS variant context files have been implemented at:
- `layer_0/layer_0_99_stages/stage_0_03_instructions/ai_agent_system/os/`
- `layer_1_project/1.99_stages/stage_1.01_instructions/ai_agent_system/os/`
- `layer_2_features/2.99_stages/stage_2.01_instructions/ai_agent_system/os/`
- `layer_3_components/3.99_stages/stage_3.01_instructions/ai_agent_system/os/`

<!-- section_id: "7a9b7b1b-cd0f-4ebf-8d0a-35f04dce5684" -->
### Tool-Specific Context

Universal tools should be aware of:
- **OS detection**: Supervisors detect OS and select appropriate context
- **Context cascade**: Layer N inherits from Layer 0...N-1
- **Tool specialization**: Each tool reads its specific context file
- **Extensibility**: New tools add their own context file pattern to the quartet/N-tuple

<!-- section_id: "031b01fd-87ac-4ef6-8074-957b6aabb893" -->
## Key Documentation

- **[Browser Automation](trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/README.md)**: Browser automation tools and guides
- **[Claude Code Config](trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md)**: Claude Code CLI configuration
- **[AI Development Frameworks](trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/README.md)**: AI coding assistant frameworks

<!-- section_id: "1079571f-45a0-437b-b07b-b32901540fc7" -->
## AI Manager Hierarchy Integration

This sub-layer integrates with the AI Manager Hierarchy System for orchestration and CLI patterns:

<!-- section_id: "58403bf7-77dc-4f0d-a50e-7fb491990ff2" -->
### Framework Orchestration
For guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the hierarchy, see:
- **[Framework Orchestration Overview](../sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md)**: When to use framework-based orchestration vs. simple handoff coordination
- **Existing Framework Docs**: `trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/` (complementary guidance on Spec Kit, BMAD Method, and AI coding assistants)

<!-- section_id: "02ea80db-3c79-468d-be95-e38a82082bb8" -->
### CLI Recursion Patterns
For patterns on using CLI recursion to spawn deep agent hierarchies, see:
- **[CLI Recursion Syntax](../sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md)**: Concrete examples of managers spawning workers via Claude Code, Codex CLI, and Gemini CLI
- OS-adapted examples for WSL/Ubuntu
- Tool selection, parallel execution, and error handling patterns

<!-- section_id: "89db6279-cebd-4ff0-a466-896e7413bbc1" -->
## ⚠️ Linux/Ubuntu-Specific Tool Access Issues

**CRITICAL**: Universal tools that depend on MCP have Linux-specific limitations. Read:

- **[Linux/Ubuntu Tool Access Issues](trickle_down_0.75_universal_tools/0_instruction_docs/LINUX_UBUNTU_TOOL_ACCESS_ISSUES.md)**: Universal tool access limitations on Linux

**Key Issues**:
- Browser automation tools must use `mcp_browser_*` instead of `mcp_playwright_*`
- Development frameworks need Linux-specific adaptations
- Cross-cutting utilities may require tool name updates
- Tool migration guide available for Playwright → Browser MCP

**Related Documentation**:
- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `../sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "f11074f7-836c-4f55-8e9a-c901b1db6882" -->
## Notes

- MCP-related tools have been moved to `sub_layer_0_10_mcp_servers_and_tools_setup`
- Universal tools are used by agents configured in `sub_layer_0_13_agent_setup`
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
