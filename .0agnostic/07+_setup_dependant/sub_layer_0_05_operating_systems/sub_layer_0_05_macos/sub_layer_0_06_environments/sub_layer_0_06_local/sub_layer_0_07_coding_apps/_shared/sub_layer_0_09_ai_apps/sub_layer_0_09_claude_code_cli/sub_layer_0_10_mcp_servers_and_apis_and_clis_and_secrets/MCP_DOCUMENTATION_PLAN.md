---
resource_id: "32c58b7a-c7cb-4000-b963-a426f183f18e"
resource_type: "document"
resource_name: "MCP_DOCUMENTATION_PLAN"
---
# MCP Servers & APIs Documentation Plan

<!-- section_id: "9d12c35c-53b5-48c8-89be-6ffbf49fa6ec" -->
## Overview

**Goal:** Rename `0.10_mcp_servers` → `0.10_mcp_servers_and_apis` and create comprehensive documentation for all MCP servers, while ensuring API keys/secrets are not exposed when sharing the repo.

<!-- section_id: "8900fa61-e1fa-46ea-9a67-ab6c37ca8059" -->
## Current State

- **1590 MCP-related directories** across the hierarchical structure
- **7 unique MCP servers:**
  - `playwright-mcp` - Browser automation via Playwright
  - `browser-mcp` - General browser control
  - `chrome-devtools-mcp` - Chrome DevTools integration
  - `claude_in_chrome` - Claude browser extension integration
  - `context7-mcp` - Context management
  - `tavily-mcp` - Web search API
  - `_mcp_core` - Core MCP configuration

<!-- section_id: "bf6b4ac0-411f-4912-a4e7-72380b1fe045" -->
## Directory Structure Pattern

```
0.10_mcp_servers_and_apis_and_secrets/
├── _mcp_core/                    # Core MCP config (shared)
├── _shared/                      # Shared across all MCP servers
├── playwright-mcp/
│   ├── README.md                 # Overview, features, quick start
│   ├── setup/
│   │   ├── README.md             # Setup instructions
│   │   ├── TROUBLESHOOTING.md    # Common issues & fixes
│   │   └── scripts/              # Setup scripts
│   ├── 0.12_universal_tools/     # Tools specific to this MCP
│   ├── 0.13_protocols/           # Usage protocols & workflows
│   └── 0.14_agent_setup/         # Agent configuration
├── browser-mcp/
│   └── ... (same structure)
└── ... (other MCP servers)
```

<!-- section_id: "568fdea8-ac6e-4c0a-a91c-9e15a7303672" -->
## Documentation Template (per MCP server)

<!-- section_id: "3f1e1c7d-c20b-404f-9c61-5c7229ddb4ad" -->
### README.md
```markdown
# [MCP Server Name]

## Overview
Brief description of what this MCP server does.

## Features
- Feature 1
- Feature 2

## Quick Start
1. Step 1
2. Step 2

## Configuration
Link to setup docs.

## API Keys Required
- `KEY_NAME` - Description (see secrets setup)
```

<!-- section_id: "cbc5b7b7-3655-46c7-83d3-1dc7821f3765" -->
### setup/README.md
```markdown
# Setup Guide

## Prerequisites
- Requirement 1
- Requirement 2

## Installation
Step-by-step installation.

## Configuration
How to configure.

## Verification
How to verify it's working.
```

<!-- section_id: "553f8546-2293-4261-a85f-2946389aba14" -->
### setup/TROUBLESHOOTING.md
```markdown
# Troubleshooting

## Common Issues

### Issue 1: Description
**Symptoms:** What you see
**Cause:** Why it happens
**Solution:** How to fix

### Issue 2: Description
...
```

<!-- section_id: "34c8858c-303f-404c-b30e-713c297ac910" -->
### 0.13_protocols/ (Skills/Workflows)
```markdown
# [Workflow Name]

## Purpose
What this workflow accomplishes.

## When to Use
Situations where this applies.

## Steps
1. Step 1
2. Step 2

## Examples
Concrete examples.
```

<!-- section_id: "7b994fa2-fa1d-4dc6-83a5-c15e55ca8ae5" -->
## Secrets/API Keys Strategy

<!-- section_id: "b9155b95-8b1f-47b0-a724-c8ebaa0cf354" -->
### Problem
The repo contains API keys that shouldn't be exposed when shared.

<!-- section_id: "60f20249-da23-49c5-b84f-0917f12558be" -->
### Solution: Template + Local Override Pattern

1. **In repo (shareable):** `config.template.json`
```json
{
  "api_key": "${TAVILY_API_KEY}",
  "other_setting": "value"
}
```

2. **Local (gitignored):** `config.local.json`
```json
{
  "api_key": "actual-api-key-here",
  "other_setting": "value"
}
```

3. **Documentation:** Clear instructions on how to:
   - Copy template to local
   - Set up required API keys
   - Where to get API keys

<!-- section_id: "894ae1ed-6ee8-423e-9752-737d576d8123" -->
### Files to Add to .gitignore
```
*.local.json
.secrets/
config.local.*
```

---

<!-- section_id: "42991189-6008-4182-91e1-29a2b1718cf8" -->
## Subagent Breakdown

<!-- section_id: "373be0a1-7cde-45af-8c48-23ed5add6d65" -->
### Phase 1: Analysis & Planning

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 1** | Explore | Analyze all MCP directories, list existing docs, identify gaps | ~5 min |
| **Agent 2** | Plan | Create documentation templates, finalize structure | ~3 min |

<!-- section_id: "3a8c4958-4aef-4ab3-8a4d-ec1608e44637" -->
### Phase 2: Rename Operations

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 3** | Bash | Rename all `0.10_mcp_servers` → `0.10_mcp_servers_and_apis` | ~2 min |

<!-- section_id: "5c16b575-0f11-4de5-9195-986015895dc0" -->
### Phase 3: Core Documentation

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 4** | Docs | Document `_mcp_core` - Core MCP setup | ~5 min |
| **Agent 5** | Docs | Create secrets/API template pattern | ~5 min |

<!-- section_id: "ec474cb4-f94b-4840-85fc-4bc25b12df58" -->
### Phase 4: MCP Server Documentation (Parallel)

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 6** | Docs | Document `playwright-mcp` | ~10 min |
| **Agent 7** | Docs | Document `browser-mcp` | ~10 min |
| **Agent 8** | Docs | Document `chrome-devtools-mcp` | ~10 min |
| **Agent 9** | Docs | Document `claude_in_chrome` | ~10 min |
| **Agent 10** | Docs | Document `context7-mcp` | ~10 min |
| **Agent 11** | Docs | Document `tavily-mcp` | ~10 min |

<!-- section_id: "11acb46a-24d6-47b4-bb98-719a15b69ef0" -->
### Phase 5: Integration & Verification

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 12** | Verify | Verify all docs, check for missing API key refs | ~5 min |

---

<!-- section_id: "e71ab365-1095-4ab3-8eb8-cbcac8351583" -->
## Execution Order

```
Phase 1 (Sequential)
    ↓
Phase 2 (Sequential)
    ↓
Phase 3 (Sequential - core first)
    ↓
Phase 4 (Parallel - all 6 MCP servers simultaneously)
    ↓
Phase 5 (Sequential - verification)
```

<!-- section_id: "95062472-50d5-4bd0-91d6-90e79ef7c926" -->
## Questions to Resolve

1. Should `_shared` documentation be at the root level or replicated?
2. Are there any MCP servers not in the list above?
3. Which API keys are currently hardcoded and need templating?
4. Should we document for all OS/environment combos or just one canonical location?

---

<!-- section_id: "922b47b0-4541-4d30-b753-08726a8c0897" -->
## Next Steps

1. [ ] User approves this plan
2. [ ] Run Phase 1 agents to gather more info
3. [ ] Refine plan based on findings
4. [ ] Execute Phases 2-5
