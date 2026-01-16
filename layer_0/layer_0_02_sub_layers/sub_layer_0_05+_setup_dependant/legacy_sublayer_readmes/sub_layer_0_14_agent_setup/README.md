# ⚠️ DEPRECATED - This Sublayer Has Been Consolidated

**Deprecation Date**: 2026-01-01
**Replaced By**: `sub_layer_0.05-0.014_setup`

This sublayer has been consolidated into the unified setup sublayer for better organization and discoverability.

## Migration Path

All setup documentation is now located in:
```
sub_layer_0.05-0.014_setup/0.01_universal_setup_file_tree_0/
```

Navigate the file tree by your configuration:
1. Choose your OS: `0.05_operating_systems/<os>/`
2. Choose your environment: `0.06_environments/<env>/`
3. Choose your coding app: `0.07_coding_apps/<app>/`
4. Continue through all levels to find your specific setup documentation

## Why Consolidate?

- **Single entry point** for all setup docs
- **Better discoverability** through hierarchical file tree
- **Cross-cutting organization** with `_shared/` folders at every level
- **Easier maintenance** - one structure instead of 10

## Legacy Content Below

The original content of this sublayer is preserved below for reference, but should not be updated. All new setup documentation should go into the consolidated sublayer.

---

# sub_layer_0.13_agent_setup

**Purpose**: Agent configuration and setup for AI applications and tools.

## Overview

This sublayer contains documentation and configuration for setting up AI agents across different AI applications and tools. Agent setup is dependent on:
- **AI App/Tool** (sub_layer_0.09): Which AI application or CLI tool is being used
- **MCP Servers** (sub_layer_0.10): Which MCP servers are configured and available
- **AI Models** (sub_layer_0.11): Which AI models are available and approved for use

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
sub_layer_0.13_agent_setup/
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
0.10_mcp_servers_and_tools_setup (depends on 0.09)
    ↓
0.11_ai_models
    ↓
0.12_universal_tools
    ↓
0.13_agent_setup (depends on 0.09, 0.10, 0.11, 0.12) ← You are here
```

## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0.09_ai_apps_tools_setup` - Agents run within AI apps/tools
  - `sub_layer_0.10_mcp_servers_and_tools_setup` - Agents use MCP servers for capabilities
  - `sub_layer_0.11_ai_models` - Agents require models to function
  - `sub_layer_0.12_universal_tools` - Agents use universal tools for capabilities
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
