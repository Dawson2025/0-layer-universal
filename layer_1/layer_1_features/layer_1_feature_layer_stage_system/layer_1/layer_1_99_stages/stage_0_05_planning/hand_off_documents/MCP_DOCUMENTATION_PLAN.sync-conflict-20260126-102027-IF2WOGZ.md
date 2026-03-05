---
resource_id: "82a25fa6-73d0-4242-b15b-9cf8391eef8f"
resource_type: "document"
resource_name: "MCP_DOCUMENTATION_PLAN.sync-conflict-20260126-102027-IF2WOGZ"
---
# MCP Servers & APIs Documentation Plan

<!-- section_id: "3db01b1b-3ae2-41c3-aff3-0fdd36b8b41f" -->
## Overview

**Goal:** Rename `0.06_mcp_servers` → `0.06_mcp_servers_and_apis` and create comprehensive documentation for all MCP servers, while ensuring API keys/secrets are not exposed when sharing the repo.

<!-- section_id: "39b9c3e3-104c-44a3-80ce-cc3449de5a8b" -->
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

<!-- section_id: "067c483a-f28b-4cc0-8878-432efcf3d75e" -->
## Directory Structure Pattern

```
0.06_mcp_servers_and_apis_and_secrets/
├── _mcp_core/                    # Core MCP config (shared)
├── _shared/                      # Shared across all MCP servers
├── playwright-mcp/
│   ├── README.md                 # Overview, features, quick start
│   ├── setup/
│   │   ├── README.md             # Setup instructions
│   │   ├── TROUBLESHOOTING.md    # Common issues & fixes
│   │   └── scripts/              # Setup scripts
│   ├── 0.07_universal_tools/     # Tools specific to this MCP
│   ├── 0.08_protocols/           # Usage protocols & workflows
│   └── 0.09_agent_setup/         # Agent configuration
├── browser-mcp/
│   └── ... (same structure)
└── ... (other MCP servers)
```

<!-- section_id: "9e20c409-4160-41f8-9127-be8a71bf7332" -->
## Documentation Template (per MCP server)

<!-- section_id: "9373161b-1ced-4fb7-9bc8-b7623f538014" -->
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

<!-- section_id: "337b9a91-384e-47d0-82bb-713148073380" -->
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

<!-- section_id: "f6a2fde9-e9d6-4459-8253-c37f2dc58910" -->
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

<!-- section_id: "066353d7-4ebd-4649-9595-bb62fad7b7b5" -->
### 0.08_protocols/ (Skills/Workflows)
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

<!-- section_id: "c724fca3-0e59-4c45-833d-8d46166e3ad9" -->
## Secrets/API Keys Strategy

<!-- section_id: "fd07c04e-c676-4eda-9565-1c9ac2b582d4" -->
### Problem
The repo contains API keys that shouldn't be exposed when shared.

<!-- section_id: "85f9b17e-4af2-41ce-ace2-6e7d178677b4" -->
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

<!-- section_id: "d85873b3-464b-4aa3-b924-958306b8d877" -->
### Files to Add to .gitignore
```
*.local.json
.secrets/
config.local.*
```

---

<!-- section_id: "1fed726c-e2d3-4dc3-a4ec-cb0b0bf5cb5d" -->
## Subagent Breakdown

<!-- section_id: "0cdfd283-dac4-4700-98ad-941532682bec" -->
### Phase 1: Analysis & Planning

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 1** | Explore | Analyze all MCP directories, list existing docs, identify gaps | ~5 min |
| **Agent 2** | Plan | Create documentation templates, finalize structure | ~3 min |

<!-- section_id: "e0f00e9c-4f48-47de-8b06-0424681100ab" -->
### Phase 2: Rename Operations

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 3** | Bash | Rename all `0.06_mcp_servers` → `0.06_mcp_servers_and_apis` | ~2 min |

<!-- section_id: "b8cebf27-48c8-4eed-81ac-cd4c8bc0ba85" -->
### Phase 3: Core Documentation

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 4** | Docs | Document `_mcp_core` - Core MCP setup | ~5 min |
| **Agent 5** | Docs | Create secrets/API template pattern | ~5 min |

<!-- section_id: "ce6ab9b2-9bb0-4c85-acdf-b4de640310d4" -->
### Phase 4: MCP Server Documentation (Parallel)

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 6** | Docs | Document `playwright-mcp` | ~10 min |
| **Agent 7** | Docs | Document `browser-mcp` | ~10 min |
| **Agent 8** | Docs | Document `chrome-devtools-mcp` | ~10 min |
| **Agent 9** | Docs | Document `claude_in_chrome` | ~10 min |
| **Agent 10** | Docs | Document `context7-mcp` | ~10 min |
| **Agent 11** | Docs | Document `tavily-mcp` | ~10 min |

<!-- section_id: "5167daf5-b601-4389-8f6c-535e24ebddd5" -->
### Phase 5: Integration & Verification

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 12** | Verify | Verify all docs, check for missing API key refs | ~5 min |

---

<!-- section_id: "536f1600-f675-4b80-af09-b43ff47d4a20" -->
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

<!-- section_id: "b3bb5839-6ad4-47d2-837b-7f19ffa36189" -->
## Questions to Resolve

1. Should `_shared` documentation be at the root level or replicated?
2. Are there any MCP servers not in the list above?
3. Which API keys are currently hardcoded and need templating?
4. Should we document for all OS/environment combos or just one canonical location?

---

<!-- section_id: "2d7ccd2f-64b0-4ab8-8a65-b60c608e65be" -->
## Next Steps

1. [ ] User approves this plan
2. [ ] Run Phase 1 agents to gather more info
3. [ ] Refine plan based on findings
4. [ ] Execute Phases 2-5
