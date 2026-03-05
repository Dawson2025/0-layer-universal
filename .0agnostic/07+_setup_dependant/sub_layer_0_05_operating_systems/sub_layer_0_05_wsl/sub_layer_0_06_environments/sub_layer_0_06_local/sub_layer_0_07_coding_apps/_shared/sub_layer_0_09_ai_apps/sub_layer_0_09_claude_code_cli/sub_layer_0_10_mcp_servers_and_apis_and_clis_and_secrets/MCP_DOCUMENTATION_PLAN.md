---
resource_id: "6486577d-cd8d-4db4-ae56-b44c2679014c"
resource_type: "document"
resource_name: "MCP_DOCUMENTATION_PLAN"
---
# MCP Servers & APIs Documentation Plan

<!-- section_id: "d1929ccb-db25-4a75-a4c0-fbb4272b6c53" -->
## Overview

**Goal:** Rename `0.10_mcp_servers` → `0.10_mcp_servers_and_apis` and create comprehensive documentation for all MCP servers, while ensuring API keys/secrets are not exposed when sharing the repo.

<!-- section_id: "104b4769-4683-42cc-84ab-c1e104bc05c4" -->
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

<!-- section_id: "8bef96f6-8984-40c0-97db-4bd831f475ad" -->
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

<!-- section_id: "b9ddcb89-add3-4b97-9847-fde05ad2dc2d" -->
## Documentation Template (per MCP server)

<!-- section_id: "a074d46e-5f82-4ced-a9d0-ae41690b2c95" -->
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

<!-- section_id: "77e68a76-0e19-4170-a1f6-8d95a14f9847" -->
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

<!-- section_id: "623a5126-c052-4e87-aa4a-d7e724461421" -->
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

<!-- section_id: "c3d3d89b-d397-4bca-803a-b682bdfe2158" -->
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

<!-- section_id: "27d3743c-b3c0-4fd7-8e34-965761a71a77" -->
## Secrets/API Keys Strategy

<!-- section_id: "c579faa4-d8c3-4951-9af7-a53245cf2ca1" -->
### Problem
The repo contains API keys that shouldn't be exposed when shared.

<!-- section_id: "f87ef88b-bf91-4d29-9344-e6b099397c00" -->
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

<!-- section_id: "77e2b330-7508-47c7-be0e-b1aea3028fd3" -->
### Files to Add to .gitignore
```
*.local.json
.secrets/
config.local.*
```

---

<!-- section_id: "09688fa4-5f09-4cb3-9c52-756e21f8da99" -->
## Subagent Breakdown

<!-- section_id: "727c78cf-1066-4605-a5df-8cc8cb83be42" -->
### Phase 1: Analysis & Planning

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 1** | Explore | Analyze all MCP directories, list existing docs, identify gaps | ~5 min |
| **Agent 2** | Plan | Create documentation templates, finalize structure | ~3 min |

<!-- section_id: "871448a6-1d1a-45fc-8c4a-de316379ef2d" -->
### Phase 2: Rename Operations

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 3** | Bash | Rename all `0.10_mcp_servers` → `0.10_mcp_servers_and_apis` | ~2 min |

<!-- section_id: "95f7dd2b-3a0e-45aa-8529-5ede7052552c" -->
### Phase 3: Core Documentation

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 4** | Docs | Document `_mcp_core` - Core MCP setup | ~5 min |
| **Agent 5** | Docs | Create secrets/API template pattern | ~5 min |

<!-- section_id: "23bc4ac0-66e8-444d-a9a6-e755c30d9971" -->
### Phase 4: MCP Server Documentation (Parallel)

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 6** | Docs | Document `playwright-mcp` | ~10 min |
| **Agent 7** | Docs | Document `browser-mcp` | ~10 min |
| **Agent 8** | Docs | Document `chrome-devtools-mcp` | ~10 min |
| **Agent 9** | Docs | Document `claude_in_chrome` | ~10 min |
| **Agent 10** | Docs | Document `context7-mcp` | ~10 min |
| **Agent 11** | Docs | Document `tavily-mcp` | ~10 min |

<!-- section_id: "4b4599a5-b447-444b-980a-e2013c58817e" -->
### Phase 5: Integration & Verification

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 12** | Verify | Verify all docs, check for missing API key refs | ~5 min |

---

<!-- section_id: "e0e29bab-2dd6-40e2-a7f6-121714e19c74" -->
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

<!-- section_id: "0dbd6647-df4a-4d18-b7e0-cfe5ae327508" -->
## Questions to Resolve

1. Should `_shared` documentation be at the root level or replicated?
2. Are there any MCP servers not in the list above?
3. Which API keys are currently hardcoded and need templating?
4. Should we document for all OS/environment combos or just one canonical location?

---

<!-- section_id: "90fb8edc-70f7-424c-95c3-c186cdac01ca" -->
## Next Steps

1. [ ] User approves this plan
2. [ ] Run Phase 1 agents to gather more info
3. [ ] Refine plan based on findings
4. [ ] Execute Phases 2-5
