# sub_layer_0.11_agent_setup

**Purpose**: Agent configuration and setup for AI applications and tools.

## Overview

This sublayer contains documentation and configuration for setting up AI agents across different AI applications and tools. Agent setup is dependent on:
- **AI App/Tool** (sub_layer_0.08): Which AI application or CLI tool is being used
- **MCP Servers** (sub_layer_0.09): Which MCP servers are configured and available
- **AI Models** (sub_layer_0.10): Which AI models are available and approved for use

## Agent Configuration Features

### Model Selection and Fallbacks
- Instructions for configuring agents with specific AI models
- Fallback model ordering when primary models are unavailable
- Model-specific agent instructions and capabilities

### App-Specific Agent Setup
- **Cursor IDE**: Agent configurations for Cursor-specific workflows
- **Claude Code**: Agent configurations for Claude Code CLI
- **Other AI Tools**: Configurations for other AI applications

### MCP Integration
- Agent instructions for using specific MCP servers
- MCP tool availability and agent capabilities
- Browser automation agent setup
- Documentation agent setup (Context7, etc.)

## Structure

```
sub_layer_0.11_agent_setup/
└── trickle_down_0.75_universal_tools/
    └── 0_instruction_docs/
        ├── agent-configs/          # Agent configuration files
        ├── model-fallbacks/        # Model fallback configurations
        ├── app-specific-agents/    # App-specific agent setups
        └── mcp-agent-integration/  # MCP server agent integration
```

## Dependency Chain

Agent setup follows this dependency order:

```
0.08_ai_apps_tools_setup
    ↓
0.09_mcp_servers_and_tools (depends on 0.08)
    ↓
0.10_ai_models
    ↓
0.11_agent_setup (depends on 0.08, 0.09, 0.10) ← You are here
```

## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0.08_ai_apps_tools_setup` - Agents run within AI apps/tools
  - `sub_layer_0.09_mcp_servers_and_tools_setup` - Agents use MCP servers for capabilities
  - `sub_layer_0.10_ai_models` - Agents require models to function
- **Provides to**: All layers that need configured agents for work

## Key Concepts

### Model Fallback Strategy
Agents should be configured with:
1. **Primary model(s)**: Preferred models for the agent's tasks
2. **Fallback order**: Sequence of models to try if primary is unavailable
3. **Model-specific instructions**: Instructions that vary by model capabilities

### Agent Capabilities Matrix
- **Browser Automation Agents**: Require browser MCP servers (0.09)
- **Documentation Agents**: Require documentation MCP servers (Context7, etc.)
- **Development Agents**: Require development tools and MCP servers
- **Testing Agents**: Require testing frameworks and MCP servers

## Notes

- Agent configurations are app-specific and model-specific
- MCP server availability determines agent capabilities
- Model fallbacks ensure agents can continue working even if preferred models are unavailable
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0

