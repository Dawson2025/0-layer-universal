---
resource_id: "29fe8e9b-2a89-4401-859f-ea2838b5cfa4"
resource_type: "document"
resource_name: "school-context"
---
---
paths: layer_1/layer_1_projects/layer_1_project_school/**
---

# School Project Context

## Required Reading

When working in school project directories:
1. Find the `.gab.jsonld` for your role (e.g., `layer_5_orchestrator.gab.jsonld`)
2. Read the matching `.integration.md` (same base name, e.g., `layer_5_orchestrator.integration.md`)
3. For precise mode constraints, query the `.gab.jsonld` via jq:
   ```
   jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' [matching .gab.jsonld]
   ```
4. Read `.claude/skills/*/SKILL.md` — check WHEN/WHEN NOT conditions

## Skill Usage

| Situation | Skill | When |
|-----------|-------|------|
| Starting assignment work | `/context-gathering` | Identify the class, assignment, stage |
| Following assignment stages | `/stage-workflow` | Navigate through research → planning → development |
| Creating new assignments | `/entity-creation` | Set up proper layer/stage structure |
| Ending session | `/handoff-creation` | Preserve progress for next session |

## Episodic Memory

- **Session start**: Check `memory/episodic.md` (auto-memory topic file) for recent school session history
- **Session end**: Update `.0agnostic/episodic_memory/index.md` in the working assignment/module directory, then run `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh`

## Agnostic System

- **Source of truth**: `0AGNOSTIC.md` is the source — edit this, NOT `CLAUDE.md` (which is auto-generated)
- **On-demand resources**: `.0agnostic/` contains rules, skills, agents, knowledge, scripts
- **After changes**: Run `agnostic-sync.sh` to regenerate tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md)
- **Tool overrides**: `.1merge/` (if present) provides tool-specific overrides via 3-tier merge (synced → overrides → additions)

## Canvas MCP Integration

- Canvas tools are available as `mcp__canvas__*` (course list, assignments, modules, grades, etc.)
- **Config file**: `~/.claude.json` → `mcpServers.canvas` block
- **API token location**: `~/.claude.json` line containing `CANVAS_API_TOKEN`
- **Setup & troubleshooting docs**: `.0agnostic/07+_setup_dependant/sub_layer_0_05_operating_systems/sub_layer_0_05_linux_ubuntu/sub_layer_0_06_group/sub_layer_0_06_environments/sub_layer_0_06_local/sub_layer_0_07_coding_apps/sub_layer_0_07_cursor/sub_layer_0_09_ai_apps/sub_layer_0_09_claude_code_cli/sub_layer_0_10_mcp_servers_and_apis_and_clis_and_secrets/sub_layer_0_10_canvas-mcp/setup/canvas-mcp-setup.md`
- **Server source**: `/home/dawson/mcp-servers/canvas-mcp-developer/`
- **Token refresh**: Canvas → Account → Settings → Approved Integrations → New Access Token
- **If 401 errors**: Token likely expired — regenerate and update `~/.claude.json`

## School-Specific Rules

- Check assignment requirements before starting work
- Follow academic writing standards — cite sources properly
- Each class is a nested layer (layer_2 sub-project → layer_3 class → layer_4+ assignments)
- Assignments have their own stage hierarchy — use all 11 stages
