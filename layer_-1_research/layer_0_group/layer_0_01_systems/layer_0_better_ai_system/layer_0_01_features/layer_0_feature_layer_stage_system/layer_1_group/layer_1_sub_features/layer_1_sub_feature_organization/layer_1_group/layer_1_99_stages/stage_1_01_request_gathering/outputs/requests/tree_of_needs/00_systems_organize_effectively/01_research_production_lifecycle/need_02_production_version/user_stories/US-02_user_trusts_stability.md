# User Trusts Production Stability

**As a** user who depends on the system for daily work,
**I want** production content to be clearly distinguished from research content and to change only through a controlled promotion process,
**So that** I can trust that the system's behavior is predictable and that outputs won't suddenly change due to unvalidated experiments.

## Acceptance Criteria

**Scenario 1: Production and research are visually distinguishable**
- **Given** I browse the directory structure of the system,
- **When** I look at entity paths,
- **Then** production entities live under `layer_0/` or `layer_1/` and research entities live under `layer_-1_research/` — the naming convention makes the distinction unambiguous.

**Scenario 2: Production changes require promotion**
- **Given** a research finding has been validated and is ready for production,
- **When** someone attempts to copy research content directly into a production directory,
- **Then** the promotion protocol requires an explicit approval step (documented in `research_promotion_protocol.md`) before the content is accepted as production.

**Scenario 3: Last-updated information is available**
- **Given** I want to verify when a production pattern was last changed,
- **When** I read the production entity's `0AGNOSTIC.md` Current Status section,
- **Then** I find a `Last Updated` date and a summary of what changed, allowing me to assess recency and relevance.
