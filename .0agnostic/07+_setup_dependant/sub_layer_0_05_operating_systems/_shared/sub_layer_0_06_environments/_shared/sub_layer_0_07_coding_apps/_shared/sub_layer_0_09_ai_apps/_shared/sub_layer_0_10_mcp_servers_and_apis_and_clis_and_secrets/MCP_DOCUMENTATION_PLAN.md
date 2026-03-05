---
resource_id: "2a60da48-61f4-4322-9e45-4adbb676b596"
resource_type: "document"
resource_name: "MCP_DOCUMENTATION_PLAN"
---
# MCP Servers & APIs Documentation Plan

<!-- section_id: "c7746913-9079-4589-9d03-c3fb3c9974cc" -->
## Overview

**Goal:** Rename `0.10_mcp_servers` → `0.10_mcp_servers_and_apis` and create comprehensive documentation for all MCP servers, while ensuring API keys/secrets are not exposed when sharing the repo.

<!-- section_id: "b40337dd-5c37-4222-ae73-48e9bc319c23" -->
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

<!-- section_id: "57bf2366-b47d-4962-8426-3fd82858e75e" -->
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

<!-- section_id: "2af11595-be72-42d7-9f9f-974233d8397d" -->
## Documentation Template (per MCP server)

<!-- section_id: "fa73a024-7df2-4ed5-9ca4-bc4edc541ee9" -->
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

<!-- section_id: "ed2e4668-d6df-4351-bcea-4d8172783e78" -->
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

<!-- section_id: "294d2c8f-3045-402e-a094-000b609d1c14" -->
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

<!-- section_id: "b634299b-fc9a-4c26-acdb-9e752b244c74" -->
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

<!-- section_id: "d9f0ec46-8257-40fd-93f2-cbff5e651675" -->
## Secrets/API Keys Strategy

<!-- section_id: "ec8275b8-02f4-4c81-a58c-e46e47ce47e8" -->
### Problem
The repo contains API keys that shouldn't be exposed when shared.

<!-- section_id: "e1d55300-d487-4f0b-93ae-606cf0094883" -->
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

<!-- section_id: "296388be-7939-4e21-b5e4-79207c1c00ed" -->
### Files to Add to .gitignore
```
*.local.json
.secrets/
config.local.*
```

---

<!-- section_id: "7da3f5db-0b09-45cc-8182-51471c730ed9" -->
## Subagent Breakdown

<!-- section_id: "a05ec6a7-13ca-47ad-96b5-2b2d024ea59a" -->
### Phase 1: Analysis & Planning

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 1** | Explore | Analyze all MCP directories, list existing docs, identify gaps | ~5 min |
| **Agent 2** | Plan | Create documentation templates, finalize structure | ~3 min |

<!-- section_id: "534a7ff4-9e3b-4120-90c8-09a5b86b2355" -->
### Phase 2: Rename Operations

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 3** | Bash | Rename all `0.10_mcp_servers` → `0.10_mcp_servers_and_apis` | ~2 min |

<!-- section_id: "97e0ad05-e155-4d6e-8801-4849911c364c" -->
### Phase 3: Core Documentation

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 4** | Docs | Document `_mcp_core` - Core MCP setup | ~5 min |
| **Agent 5** | Docs | Create secrets/API template pattern | ~5 min |

<!-- section_id: "c5c32dde-83f8-4717-849d-08ea724a040a" -->
### Phase 4: MCP Server Documentation (Parallel)

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 6** | Docs | Document `playwright-mcp` | ~10 min |
| **Agent 7** | Docs | Document `browser-mcp` | ~10 min |
| **Agent 8** | Docs | Document `chrome-devtools-mcp` | ~10 min |
| **Agent 9** | Docs | Document `claude_in_chrome` | ~10 min |
| **Agent 10** | Docs | Document `context7-mcp` | ~10 min |
| **Agent 11** | Docs | Document `tavily-mcp` | ~10 min |

<!-- section_id: "d941445f-039e-45df-a4c4-af5fccfc0a6b" -->
### Phase 5: Integration & Verification

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 12** | Verify | Verify all docs, check for missing API key refs | ~5 min |

---

<!-- section_id: "b0f98b5c-60e7-4e9c-bdc7-58df49e82bb3" -->
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

<!-- section_id: "54bd5563-8f60-4d0a-9506-6b2f64fee177" -->
## Questions to Resolve

1. Should `_shared` documentation be at the root level or replicated?
2. Are there any MCP servers not in the list above?
3. Which API keys are currently hardcoded and need templating?
4. Should we document for all OS/environment combos or just one canonical location?

---

<!-- section_id: "ec365671-7d71-44c3-a91d-3c8b898cd3df" -->
## Next Steps

1. [ ] User approves this plan
2. [ ] Run Phase 1 agents to gather more info
3. [ ] Refine plan based on findings
4. [ ] Execute Phases 2-5
