---
resource_id: "81105654-e472-44c3-9ad4-dc2de80acc63"
resource_type: "readme_document"
resource_name: "README"
---
# sub_layer_0_13_agent_setup

**Purpose**: Agent configuration and setup for AI applications and tools.

<!-- section_id: "e31a78ab-bf98-4630-a218-54a4a46a2e63" -->
## Overview

This sublayer contains documentation and configuration for setting up AI agents across different AI applications and tools. Agent setup is dependent on:
- **AI App/Tool** (sub_layer_0_09): Which AI application or CLI tool is being used
- **MCP Servers** (sub_layer_0_10): Which MCP servers are configured and available
- **AI Models** (sub_layer_0_11): Which AI models are available and approved for use

<!-- section_id: "63a29820-eabf-442c-bece-b7108936599e" -->
## Agent Configuration Features

<!-- section_id: "1e59dd25-2ac3-4cf9-8418-d67accc4bdee" -->
### Model Selection and Fallbacks
- Instructions for configuring agents with specific AI models
- Fallback model ordering when primary models are unavailable
- Model-specific agent instructions and capabilities

<!-- section_id: "ac814937-05ae-4467-bac1-998dc29d4e4a" -->
### App-Specific Agent Setup
- **Cursor IDE**: Agent configurations for Cursor-specific workflows
- **Claude Code**: Agent configurations for Claude Code CLI
- **Other AI Tools**: Configurations for other AI applications

<!-- section_id: "9b7ba361-4496-4339-a68d-bbc0aee242dd" -->
### MCP Integration
- Agent instructions for using specific MCP servers
- MCP tool availability and agent capabilities
- Browser automation agent setup
- Documentation agent setup (Context7, etc.)

<!-- section_id: "27e7947f-0ea3-45a7-87f4-1cc932e1a46e" -->
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

<!-- section_id: "6718a066-c06c-4881-9775-b6e82caa687d" -->
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

<!-- section_id: "d76bcbbb-6738-491b-8d7a-fecf6e0bd059" -->
## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Agents run within AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Agents use MCP servers for capabilities
  - `sub_layer_0_11_ai_models` - Agents require models to function
  - `sub_layer_0_12_universal_tools` - Agents use universal tools for capabilities
- **Provides to**: All layers that need configured agents for work

<!-- section_id: "0557269a-27d3-410a-b6c6-ca7a25616ad7" -->
## Key Concepts

<!-- section_id: "7e31b325-5593-4413-9e47-8490089399cc" -->
### Model Fallback Strategy
Agents should be configured with:
1. **Primary model(s)**: Preferred models for the agent's tasks
2. **Fallback order**: Sequence of models to try if primary is unavailable
3. **Model-specific instructions**: Instructions that vary by model capabilities

<!-- section_id: "fafad5cd-750d-4388-b9aa-d17fc59e2214" -->
### Agent Capabilities Matrix
- **Browser Automation Agents**: Require browser MCP servers (0.09)
- **Documentation Agents**: Require documentation MCP servers (Context7, etc.)
- **Development Agents**: Require development tools and MCP servers
- **Testing Agents**: Require testing frameworks and MCP servers

<!-- section_id: "7d91271e-c57e-4322-98e2-49ca694e07b6" -->
## Notes

- Agent configurations are app-specific and model-specific
- MCP server availability determines agent capabilities
- Model fallbacks ensure agents can continue working even if preferred models are unavailable
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
