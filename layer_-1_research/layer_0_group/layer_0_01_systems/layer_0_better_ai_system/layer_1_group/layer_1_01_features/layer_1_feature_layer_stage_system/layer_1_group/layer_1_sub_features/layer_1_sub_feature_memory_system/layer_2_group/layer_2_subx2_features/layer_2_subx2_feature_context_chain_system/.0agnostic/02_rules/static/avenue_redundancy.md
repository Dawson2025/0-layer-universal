---
resource_id: "a6414b4a-572f-4831-85ab-9778529052be"
resource_type: "rule"
resource_name: "avenue_redundancy"
---
# Avenue Redundancy Rule

<!-- section_id: "b45e117c-53ea-4081-8396-6538fd6147fd" -->
## Rule: Minimum 3-Avenue Redundancy for All Critical Context

Every piece of critical context MUST be reachable via at least 3 independent avenues. If fewer than 3 avenues reach a context item, add references in the missing avenue types.

<!-- section_id: "66450c58-6d2f-42bb-8ba0-1852cab32b0a" -->
## The 8 Avenues

| # | Avenue | Location Pattern | Loaded |
|---|--------|-----------------|--------|
| 1 | System Prompt | `CLAUDE.md` (auto-generated) | Static |
| 2 | Path Rules | `.claude/rules/*.md` | Dynamic (path match) |
| 3 | Skills | `.0agnostic/skills/` or `.claude/skills/` | Dynamic (invoked) |
| 4 | Parent References | `0AGNOSTIC.md` parent chain | Dynamic (traversal) |
| 5 | JSON-LD Agent Defs | `*.gab.jsonld` | Dynamic (read) |
| 6 | Integration Summaries | `*.integration.md` | Dynamic (read) |
| 7 | Episodic Memory | `.0agnostic/episodic_memory/` | Dynamic (read) |
| 8 | Agnostic System | `.0agnostic/rules/`, `.0agnostic/skills/` | Dynamic (read) |

<!-- section_id: "2cad2c01-5e94-493c-bc7b-a8af49b267fa" -->
## Verification Procedure

For each critical context item:

1. List the item (e.g., "chain integrity rule")
2. Check which avenues reference it
3. Record coverage: `[1,2,4,8]` = 4 avenues = PASS
4. If coverage < 3, flag for remediation

<!-- section_id: "7ff9436e-9512-48ab-bdaf-fa39c3aac6dc" -->
## Remediation

When a context item has fewer than 3 avenues:

- **Missing System Prompt**: Ensure 0AGNOSTIC.md mentions it (agnostic-sync propagates to CLAUDE.md)
- **Missing Path Rule**: Create a `.claude/rules/*.md` file referencing it
- **Missing Skill**: Add a skill or add the item to an existing skill's protocol
- **Missing Parent Ref**: Add to the nearest 0AGNOSTIC.md in the chain
- **Missing JSON-LD**: Add to the agent's `.gab.jsonld` mode constraints
- **Missing Integration**: Regenerate `.integration.md` via `tools/jsonld-to-md.sh`

<!-- section_id: "fe402258-f32a-46b2-9aef-366125cdeabf" -->
## Minimum Viable Coverage

- **3+ avenues**: PASS — context is reliably discoverable
- **2 avenues**: WARNING — add one more avenue
- **1 avenue**: FAIL — single point of failure, must remediate immediately
- **0 avenues**: CRITICAL — context is unreachable, create it
