---
resource_id: "f8844b6b-f40c-400e-8f85-84752ec18833"
resource_type: "output"
resource_name: "US-01_agent_defaults_to_production"
---
# Agent Defaults to Production

**As an** AI agent beginning a new session,
**I want** the context chain to automatically load production content without any manual configuration,
**So that** I start every task with stable, proven patterns and only access research content when explicitly directed.

## Acceptance Criteria

**Scenario 1: Fresh session loads production only**
- **Given** a user opens a new Claude Code session in `0_layer_universal/`,
- **When** the agent reads CLAUDE.md files along the context chain,
- **Then** all loaded context references production entities (`layer_0/`, `layer_1/`) and none reference `layer_-1_research/` — the agent is in production mode by default.

**Scenario 2: No setup required for production mode**
- **Given** the user has not issued any mode-switching commands,
- **When** the agent checks its operating mode,
- **Then** production mode is active implicitly — there is no "activate production" command because it is the default state.

**Scenario 3: Research content is not accidentally loaded**
- **Given** both production and research entities exist for the same topic (e.g., `layer_0_feature_X/` and `layer_-1_research/layer_-1_feature_X/`),
- **When** the agent loads context for that topic,
- **Then** only the production entity's context is loaded — the research entity is not discovered or loaded unless the user activates research mode.
