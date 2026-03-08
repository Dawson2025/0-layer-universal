---
resource_id: "811567e9-f386-44ae-a3da-a64e01418641"
resource_type: "readme_document"
resource_name: "README"
---
# sub_layer_0_13_agent_setup

**Purpose**: Agent configuration and setup for AI applications and tools.

<!-- section_id: "b757c3e0-2907-415e-b9bb-a7261afdf5f6" -->
## Overview

This sublayer contains documentation and configuration for setting up AI agents across different AI applications and tools. Agent setup is dependent on:
- **AI App/Tool** (sub_layer_0_09): Which AI application or CLI tool is being used
- **MCP Servers** (sub_layer_0_10): Which MCP servers are configured and available
- **AI Models** (sub_layer_0_11): Which AI models are available and approved for use

<!-- section_id: "9284ab20-c376-4654-b9fa-8769474e58a5" -->
## Agent Configuration Features

<!-- section_id: "78489212-9140-41ef-8fcc-faa9043d3f36" -->
### Model Selection and Fallbacks
- Instructions for configuring agents with specific AI models
- Fallback model ordering when primary models are unavailable
- Model-specific agent instructions and capabilities

<!-- section_id: "0c8d607c-d237-4ef5-b8b9-25f47dc3b635" -->
### App-Specific Agent Setup
- **Cursor IDE**: Agent configurations for Cursor-specific workflows
- **Claude Code**: Agent configurations for Claude Code CLI
- **Other AI Tools**: Configurations for other AI applications

<!-- section_id: "3c198651-6230-4641-a918-be855bee48a1" -->
### MCP Integration
- Agent instructions for using specific MCP servers
- MCP tool availability and agent capabilities
- Browser automation agent setup
- Documentation agent setup (Context7, etc.)

<!-- section_id: "e73a5da4-ffae-4786-848d-5d9ce0d69542" -->
## Structure

```
sub_layer_0_13_agent_setup/
└── trickle_down_0.75_universal_tools/
    └── 0_instruction_docs/
        ├── agent-configs/          # Agent configuration files
        ├── model-fallbacks/        # Model fallback configurations
        ├── app-specific-agents/    # App-specific agent setups
        └── mcp-agent-integration/  # MCP server agent integration
```

<!-- section_id: "4962af22-382e-4bac-96b1-705c4f27a55a" -->
## Dependency Chain

Agent setup follows this dependency order:

```
0.08_ai_apps_tools_setup
    ↓
0.10_mcp_servers_and_tools_setup (depends on 0.09)
    ↓
0.11_ai_models
    ↓
0.12_universal_tools
    ↓
0.13_agent_setup (depends on 0.09, 0.10, 0.11, 0.12) ← You are here
```

<!-- section_id: "b320eb47-296d-4019-a55e-9efc8ba81d9e" -->
## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Agents run within AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Agents use MCP servers for capabilities
  - `sub_layer_0_11_ai_models` - Agents require models to function
  - `sub_layer_0_12_universal_tools` - Agents use universal tools for capabilities
- **Provides to**: All layers that need configured agents for work

<!-- section_id: "6446be58-ed05-47f3-8472-f3ddd72d0db1" -->
## Key Concepts

<!-- section_id: "a9c3fa3b-b557-46b6-ae9a-5a729e3f628a" -->
### Model Fallback Strategy
Agents should be configured with:
1. **Primary model(s)**: Preferred models for the agent's tasks
2. **Fallback order**: Sequence of models to try if primary is unavailable
3. **Model-specific instructions**: Instructions that vary by model capabilities

<!-- section_id: "8b3c428e-30ef-4c13-aaa4-3fabf1f87c53" -->
### Agent Capabilities Matrix
- **Browser Automation Agents**: Require browser MCP servers (0.09)
- **Documentation Agents**: Require documentation MCP servers (Context7, etc.)
- **Development Agents**: Require development tools and MCP servers
- **Testing Agents**: Require testing frameworks and MCP servers

<!-- section_id: "959aa308-f1a3-479d-b7e9-f5a79c33fb43" -->
## Notes

- Agent configurations are app-specific and model-specific
- MCP server availability determines agent capabilities
- Model fallbacks ensure agents can continue working even if preferred models are unavailable
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
