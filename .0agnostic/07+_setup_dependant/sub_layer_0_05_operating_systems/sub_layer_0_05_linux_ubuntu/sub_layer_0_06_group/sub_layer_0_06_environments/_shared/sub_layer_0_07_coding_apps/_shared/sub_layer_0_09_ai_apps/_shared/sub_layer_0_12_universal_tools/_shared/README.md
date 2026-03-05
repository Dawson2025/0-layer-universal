---
resource_id: "5affa9ea-7958-4809-8e8a-1f8b88f44431"
resource_type: "readme
document"
resource_name: "README"
---
# ⚠️ DEPRECATED - This Sublayer Has Been Consolidated

**Deprecation Date**: 2026-01-01
**Replaced By**: `sub_layer_0_05-0.014_setup`

This sublayer has been consolidated into the unified setup sublayer for better organization and discoverability.

<!-- section_id: "592b24e4-bcf2-400a-a7ca-b5f7971412e4" -->
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

<!-- section_id: "0f17aa2d-83e8-4389-bead-ea0fb298bec1" -->
## Why Consolidate?

- **Single entry point** for all setup docs
- **Better discoverability** through hierarchical file tree
- **Cross-cutting organization** with `_shared/` folders at every level
- **Easier maintenance** - one structure instead of 10

<!-- section_id: "0ba268c9-1b33-40d6-a8a4-cb20c51d1a85" -->
## Legacy Content Below

The original content of this sublayer is preserved below for reference, but should not be updated. All new setup documentation should go into the consolidated sublayer.

---

# sub_layer_0_12_universal_tools

**Purpose**: Cross-project scripts, utilities, and universal tools.

<!-- section_id: "54766b95-9358-4919-a9d5-3cc3003f43c3" -->
## Overview

This sublayer contains universal tools, scripts, and utilities that can be used across multiple projects. This includes browser automation tools, Claude Code configuration, AI development frameworks, and other cross-cutting utilities.

<!-- section_id: "11ae8720-3199-4203-b97c-108b3ba7235c" -->
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

<!-- section_id: "f1ab4166-812e-44b5-9984-c92a8d236efb" -->
## Relationship to Other Sublayers

- **Depends on**:
  - `sub_layer_0_09_ai_apps_tools_setup` - Tools may require AI apps to be set up first
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some tools may use MCP servers
- **Provides to**: All layers that need universal utilities and scripts

<!-- section_id: "b5d80ef8-81c4-43a0-a934-e762bc9cdaac" -->
## Tool Context Files and OS Variants

Universal tools integrate with the **OS Variant and Quartet Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "c97f5d9a-d6ab-406a-b75e-a7ce0576c8c2" -->
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

<!-- section_id: "68dceda9-1e1f-40a0-a082-606858ceb34f" -->
### Implementation Locations

OS variant context files have been implemented at:
- `layer_0/layer_0_99_stages/stage_0_03_instructions/ai_agent_system/os/`
- `layer_1_project/1.99_stages/stage_1.01_instructions/ai_agent_system/os/`
- `layer_2_features/2.99_stages/stage_2.01_instructions/ai_agent_system/os/`
- `layer_3_components/3.99_stages/stage_3.01_instructions/ai_agent_system/os/`

<!-- section_id: "bc5a7247-f9ba-4c04-9b3a-813c41359b77" -->
### Tool-Specific Context

Universal tools should be aware of:
- **OS detection**: Supervisors detect OS and select appropriate context
- **Context cascade**: Layer N inherits from Layer 0...N-1
- **Tool specialization**: Each tool reads its specific context file
- **Extensibility**: New tools add their own context file pattern to the quartet/N-tuple

<!-- section_id: "d16482a3-2722-4f55-859b-20e50cae8636" -->
## Key Documentation

- **[Browser Automation](trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/README.md)**: Browser automation tools and guides
- **[Claude Code Config](trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md)**: Claude Code CLI configuration
- **[AI Development Frameworks](trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/README.md)**: AI coding assistant frameworks

<!-- section_id: "0e35636b-a851-49d9-8f40-11eab88f72a6" -->
## AI Manager Hierarchy Integration

This sub-layer integrates with the AI Manager Hierarchy System for orchestration and CLI patterns:

<!-- section_id: "c125b01b-3986-4406-9c40-e433d0dbe405" -->
### Framework Orchestration
For guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the hierarchy, see:
- **[Framework Orchestration Overview](../sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md)**: When to use framework-based orchestration vs. simple handoff coordination
- **Existing Framework Docs**: `trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/` (complementary guidance on Spec Kit, BMAD Method, and AI coding assistants)

<!-- section_id: "cf0f04ac-e945-4a00-bbd3-008ce3414971" -->
### CLI Recursion Patterns
For patterns on using CLI recursion to spawn deep agent hierarchies, see:
- **[CLI Recursion Syntax](../sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md)**: Concrete examples of managers spawning workers via Claude Code, Codex CLI, and Gemini CLI
- OS-adapted examples for WSL/Ubuntu
- Tool selection, parallel execution, and error handling patterns

<!-- section_id: "daa35b70-e4a2-4956-8ec7-0621d1b5e97e" -->
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

<!-- section_id: "ac16a510-d805-46d8-999c-73bace03661b" -->
## Notes

- MCP-related tools have been moved to `sub_layer_0_10_mcp_servers_and_tools_setup`
- Universal tools are used by agents configured in `sub_layer_0_13_agent_setup`
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0


---

<!-- section_id: "bc687d8f-7bbb-4f62-aae5-47fd16999ff4" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/README.md`

# sub_layer_0_12_universal_tools

**Purpose**: Cross-project scripts, utilities, and universal tools.

<!-- section_id: "285b76dc-79fb-40ed-aa17-cda89c46e932" -->
## Overview

This sublayer contains universal tools, scripts, and utilities that can be used across multiple projects. This includes browser automation tools, Claude Code configuration, AI development frameworks, and other cross-cutting utilities.

<!-- section_id: "76daf3b4-b4ee-4890-8d04-f77ab5602b9f" -->
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

<!-- section_id: "3c11a036-fb21-42f8-87f9-39fc87c7c675" -->
## Relationship to Other Sublayers

- **Depends on**:
  - `sub_layer_0_09_ai_apps_tools_setup` - Tools may require AI apps to be set up first
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some tools may use MCP servers
- **Provides to**: All layers that need universal utilities and scripts

<!-- section_id: "2b19d957-f28f-4e24-aaf5-9c23134a7f15" -->
## Tool Context Files and OS Variants

Universal tools integrate with the **OS Variant and Quartet Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "b9f3d50f-2b6f-418f-a2a7-27f20f02d80a" -->
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

<!-- section_id: "5dc1da13-5546-4912-851a-d032b6e016c1" -->
### Implementation Locations

OS variant context files have been implemented at:
- `layer_0/layer_0_99_stages/stage_0_03_instructions/ai_agent_system/os/`
- `layer_1_project/1.99_stages/stage_1.01_instructions/ai_agent_system/os/`
- `layer_2_features/2.99_stages/stage_2.01_instructions/ai_agent_system/os/`
- `layer_3_components/3.99_stages/stage_3.01_instructions/ai_agent_system/os/`

<!-- section_id: "a01b00e5-64be-4131-b1a0-04831d950615" -->
### Tool-Specific Context

Universal tools should be aware of:
- **OS detection**: Supervisors detect OS and select appropriate context
- **Context cascade**: Layer N inherits from Layer 0...N-1
- **Tool specialization**: Each tool reads its specific context file
- **Extensibility**: New tools add their own context file pattern to the quartet/N-tuple

<!-- section_id: "256151aa-f6a8-47a8-aa07-98faf3a27188" -->
## Key Documentation

- **[Browser Automation](trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/README.md)**: Browser automation tools and guides
- **[Claude Code Config](trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/README.md)**: Claude Code CLI configuration
- **[AI Development Frameworks](trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/README.md)**: AI coding assistant frameworks

<!-- section_id: "5501fc25-0a80-48bc-a178-625d17b7a74c" -->
## AI Manager Hierarchy Integration

This sub-layer integrates with the AI Manager Hierarchy System for orchestration and CLI patterns:

<!-- section_id: "90a67924-7c55-40af-94c4-7f47ca02fc67" -->
### Framework Orchestration
For guidance on integrating multi-agent frameworks (LangGraph, AutoGen, CrewAI, MetaGPT) with the hierarchy, see:
- **[Framework Orchestration Overview](../sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md)**: When to use framework-based orchestration vs. simple handoff coordination
- **Existing Framework Docs**: `trickle_down_0.75_universal_tools/0_instruction_docs/ai-development-frameworks/` (complementary guidance on Spec Kit, BMAD Method, and AI coding assistants)

<!-- section_id: "c3ca4e0f-6938-431c-9027-7d12f3d6e904" -->
### CLI Recursion Patterns
For patterns on using CLI recursion to spawn deep agent hierarchies, see:
- **[CLI Recursion Syntax](../sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md)**: Concrete examples of managers spawning workers via Claude Code, Codex CLI, and Gemini CLI
- OS-adapted examples for WSL/Ubuntu
- Tool selection, parallel execution, and error handling patterns

<!-- section_id: "4cce0749-2a35-4a0f-bd2f-5b8a6dcc6b22" -->
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

<!-- section_id: "7f7944e4-2f8a-4f95-9386-29ac5efa957f" -->
## Notes

- MCP-related tools have been moved to `sub_layer_0_10_mcp_servers_and_tools_setup`
- Universal tools are used by agents configured in `sub_layer_0_13_agent_setup`
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
