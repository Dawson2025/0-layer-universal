---
resource_id: "95cf1bc5-91ea-4798-8164-ba4ba26ad47c"
resource_type: "document"
resource_name: "MCP_DOCUMENTATION_PLAN"
---
# MCP Servers & APIs Documentation Plan

<!-- section_id: "74196616-738d-4a0b-9d81-9acc5d88406b" -->
## Overview

**Goal:** Rename `0.10_mcp_servers` → `0.10_mcp_servers_and_apis` and create comprehensive documentation for all MCP servers, while ensuring API keys/secrets are not exposed when sharing the repo.

<!-- section_id: "9c992947-2032-41b6-8dda-2d42cbc283bc" -->
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

<!-- section_id: "07655192-130e-4700-9ead-530957af578c" -->
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

<!-- section_id: "d9efa430-0b0b-4daa-a39e-5935f9cf7270" -->
## Documentation Template (per MCP server)

<!-- section_id: "89fb87bd-6d9f-49bd-8fad-51d6096f5824" -->
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

<!-- section_id: "9300d4cd-5a34-4b1b-bdc7-47962aa75ce0" -->
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

<!-- section_id: "f6e8b09d-f3f8-45f8-b3fd-0627cd0991b2" -->
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

<!-- section_id: "ad0a57b9-0255-4a3b-a7f8-6ed150c0d47d" -->
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

<!-- section_id: "e3648e2e-2a24-4b5a-96a6-a270381ee3d1" -->
## Secrets/API Keys Strategy

<!-- section_id: "8c08e9b5-edf1-44ae-905e-9b2cedd7e2e1" -->
### Problem
The repo contains API keys that shouldn't be exposed when shared.

<!-- section_id: "25d6b221-b02e-4aef-b16a-81e2ca5c7bb4" -->
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

<!-- section_id: "6cec999f-9016-4776-a311-dbdcd7ed11a0" -->
### Files to Add to .gitignore
```
*.local.json
.secrets/
config.local.*
```

---

<!-- section_id: "a90e17f6-1618-4d0b-8b75-18d0f2dfbdba" -->
## Subagent Breakdown

<!-- section_id: "e0264359-c8c1-4ba6-887b-1d416e14f34a" -->
### Phase 1: Analysis & Planning

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 1** | Explore | Analyze all MCP directories, list existing docs, identify gaps | ~5 min |
| **Agent 2** | Plan | Create documentation templates, finalize structure | ~3 min |

<!-- section_id: "a77d3fe5-de6a-481a-92b0-ba8cf2934dbd" -->
### Phase 2: Rename Operations

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 3** | Bash | Rename all `0.10_mcp_servers` → `0.10_mcp_servers_and_apis` | ~2 min |

<!-- section_id: "e8592661-500d-4d2e-84b2-e1e0f429e836" -->
### Phase 3: Core Documentation

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 4** | Docs | Document `_mcp_core` - Core MCP setup | ~5 min |
| **Agent 5** | Docs | Create secrets/API template pattern | ~5 min |

<!-- section_id: "e3884a36-1a44-4747-b985-37d8d597bf4d" -->
### Phase 4: MCP Server Documentation (Parallel)

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 6** | Docs | Document `playwright-mcp` | ~10 min |
| **Agent 7** | Docs | Document `browser-mcp` | ~10 min |
| **Agent 8** | Docs | Document `chrome-devtools-mcp` | ~10 min |
| **Agent 9** | Docs | Document `claude_in_chrome` | ~10 min |
| **Agent 10** | Docs | Document `context7-mcp` | ~10 min |
| **Agent 11** | Docs | Document `tavily-mcp` | ~10 min |

<!-- section_id: "c5d50c94-4ea8-4063-9a85-3878d20061d5" -->
### Phase 5: Integration & Verification

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 12** | Verify | Verify all docs, check for missing API key refs | ~5 min |

---

<!-- section_id: "2ec1db93-2621-4deb-9905-26583bd907ae" -->
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

<!-- section_id: "d20226be-4521-4545-be73-69a8c4a44ed6" -->
## Questions to Resolve

1. Should `_shared` documentation be at the root level or replicated?
2. Are there any MCP servers not in the list above?
3. Which API keys are currently hardcoded and need templating?
4. Should we document for all OS/environment combos or just one canonical location?

---

<!-- section_id: "3daeee30-a685-4208-b8d9-4ae2ec151f9f" -->
## Next Steps

1. [ ] User approves this plan
2. [ ] Run Phase 1 agents to gather more info
3. [ ] Refine plan based on findings
4. [ ] Execute Phases 2-5
