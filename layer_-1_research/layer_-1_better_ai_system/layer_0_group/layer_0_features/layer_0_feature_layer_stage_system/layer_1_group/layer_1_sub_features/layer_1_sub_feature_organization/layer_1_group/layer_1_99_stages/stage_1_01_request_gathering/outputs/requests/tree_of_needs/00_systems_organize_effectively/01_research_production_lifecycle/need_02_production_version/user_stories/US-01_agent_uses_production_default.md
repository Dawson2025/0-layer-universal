# Agent Uses Production by Default

**As an** AI agent starting a new task with no special instructions,
**I want to** automatically load production context from the standard entity hierarchy,
**So that** I operate with stable, proven patterns without needing to evaluate or filter experimental alternatives.

## Acceptance Criteria

**Scenario 1: Default context chain excludes research**
- **Given** a user starts a new session and asks the agent to work in `layer_1/layer_1_projects/`,
- **When** the agent traverses the context chain (reading CLAUDE.md files from root to working directory),
- **Then** every CLAUDE.md in the chain references production content only — no `layer_-1_research/` paths appear in any loaded context.

**Scenario 2: Production patterns are self-sufficient**
- **Given** the agent loads a production entity's `0AGNOSTIC.md`,
- **When** the agent reads the Identity, Key Behaviors, and Methodology sections,
- **Then** all referenced resources (knowledge, rules, protocols) exist and are accessible without needing to consult research entities.

**Scenario 3: Research content is invisible by default**
- **Given** a research entity has produced outputs that overlap with production topics,
- **When** the agent searches for relevant context (e.g., via Glob or Grep),
- **Then** the agent's working directory scope does not include `layer_-1_research/` paths unless the user has explicitly activated research mode.
