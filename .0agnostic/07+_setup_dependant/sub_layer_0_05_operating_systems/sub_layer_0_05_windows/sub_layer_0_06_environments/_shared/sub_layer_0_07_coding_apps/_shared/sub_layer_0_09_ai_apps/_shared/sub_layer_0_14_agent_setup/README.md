---
resource_id: "4aa2de6b-ef8c-4b5a-9197-81fbff1abffd"
resource_type: "readme
document"
resource_name: "README"
---
# sub_layer_0_13_agent_setup

**Purpose**: Agent configuration and setup for AI applications and tools.

<!-- section_id: "614bd3ac-878a-44cf-8331-b20bf6f7d293" -->
## Overview

This sublayer contains documentation and configuration for setting up AI agents across different AI applications and tools. Agent setup is dependent on:
- **AI App/Tool** (sub_layer_0_09): Which AI application or CLI tool is being used
- **MCP Servers** (sub_layer_0_10): Which MCP servers are configured and available
- **AI Models** (sub_layer_0_11): Which AI models are available and approved for use

<!-- section_id: "85e55a4e-b4be-4add-92bd-abffcb67b0d4" -->
## Agent Configuration Features

<!-- section_id: "30ca29e1-3e7c-4f69-81c7-21ea472e7c0a" -->
### Model Selection and Fallbacks
- Instructions for configuring agents with specific AI models
- Fallback model ordering when primary models are unavailable
- Model-specific agent instructions and capabilities

<!-- section_id: "d42a09f7-5403-4d24-b4ff-a90e048a575a" -->
### App-Specific Agent Setup
- **Cursor IDE**: Agent configurations for Cursor-specific workflows
- **Claude Code**: Agent configurations for Claude Code CLI
- **Other AI Tools**: Configurations for other AI applications

<!-- section_id: "7f5ab2b5-a4ca-4104-81d8-fd57bffeb585" -->
### MCP Integration
- Agent instructions for using specific MCP servers
- MCP tool availability and agent capabilities
- Browser automation agent setup
- Documentation agent setup (Context7, etc.)

<!-- section_id: "8e5e28fd-dec9-4508-9763-f869e5f95eaa" -->
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

<!-- section_id: "deb0da47-e106-4bad-9d2f-2a085bd90293" -->
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

<!-- section_id: "f3afb701-7dd4-4862-92b4-a4cf7d1ae5bb" -->
## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Agents run within AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Agents use MCP servers for capabilities
  - `sub_layer_0_11_ai_models` - Agents require models to function
  - `sub_layer_0_12_universal_tools` - Agents use universal tools for capabilities
- **Provides to**: All layers that need configured agents for work

<!-- section_id: "45007709-64f4-4588-a726-621b89f36b6a" -->
## Key Concepts

<!-- section_id: "44020580-7703-4ae7-a7b3-663391e4f650" -->
### Model Fallback Strategy
Agents should be configured with:
1. **Primary model(s)**: Preferred models for the agent's tasks
2. **Fallback order**: Sequence of models to try if primary is unavailable
3. **Model-specific instructions**: Instructions that vary by model capabilities

<!-- section_id: "b76b464b-d6a0-467d-8d04-c730ded46585" -->
### Agent Capabilities Matrix
- **Browser Automation Agents**: Require browser MCP servers (0.09)
- **Documentation Agents**: Require documentation MCP servers (Context7, etc.)
- **Development Agents**: Require development tools and MCP servers
- **Testing Agents**: Require testing frameworks and MCP servers

<!-- section_id: "5aabb676-ae33-4c41-b4e0-5db537fb87d0" -->
## Notes

- Agent configurations are app-specific and model-specific
- MCP server availability determines agent capabilities
- Model fallbacks ensure agents can continue working even if preferred models are unavailable
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
