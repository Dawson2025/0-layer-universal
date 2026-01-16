# MCP Servers & APIs Documentation Plan

## Overview

**Goal:** Rename `0.10_mcp_servers` → `0.10_mcp_servers_and_apis` and create comprehensive documentation for all MCP servers, while ensuring API keys/secrets are not exposed when sharing the repo.

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

## Documentation Template (per MCP server)

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

## Secrets/API Keys Strategy

### Problem
The repo contains API keys that shouldn't be exposed when shared.

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

### Files to Add to .gitignore
```
*.local.json
.secrets/
config.local.*
```

---

## Subagent Breakdown

### Phase 1: Analysis & Planning

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 1** | Explore | Analyze all MCP directories, list existing docs, identify gaps | ~5 min |
| **Agent 2** | Plan | Create documentation templates, finalize structure | ~3 min |

### Phase 2: Rename Operations

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 3** | Bash | Rename all `0.10_mcp_servers` → `0.10_mcp_servers_and_apis` | ~2 min |

### Phase 3: Core Documentation

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 4** | Docs | Document `_mcp_core` - Core MCP setup | ~5 min |
| **Agent 5** | Docs | Create secrets/API template pattern | ~5 min |

### Phase 4: MCP Server Documentation (Parallel)

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 6** | Docs | Document `playwright-mcp` | ~10 min |
| **Agent 7** | Docs | Document `browser-mcp` | ~10 min |
| **Agent 8** | Docs | Document `chrome-devtools-mcp` | ~10 min |
| **Agent 9** | Docs | Document `claude_in_chrome` | ~10 min |
| **Agent 10** | Docs | Document `context7-mcp` | ~10 min |
| **Agent 11** | Docs | Document `tavily-mcp` | ~10 min |

### Phase 5: Integration & Verification

| Agent | Type | Task | Estimated Scope |
|-------|------|------|-----------------|
| **Agent 12** | Verify | Verify all docs, check for missing API key refs | ~5 min |

---

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

## Questions to Resolve

1. Should `_shared` documentation be at the root level or replicated?
2. Are there any MCP servers not in the list above?
3. Which API keys are currently hardcoded and need templating?
4. Should we document for all OS/environment combos or just one canonical location?

---

## Next Steps

1. [ ] User approves this plan
2. [ ] Run Phase 1 agents to gather more info
3. [ ] Refine plan based on findings
4. [ ] Execute Phases 2-5
