# Cursor Agent CLI Reference Guide

**Last Updated:** 2026-02-27
**Tool Status:** Active (Beta)
**Official Docs:** https://cursor.com/docs/cli/

---

## Table of Contents

1. [Installation & Setup](#installation--setup)
2. [Core Commands](#core-commands)
3. [CLI Flags & Parameters](#cli-flags--parameters)
4. [Operating Modes](#operating-modes)
5. [Configuration Files](#configuration-files)
6. [MCP Server Integration](#mcp-server-integration)
7. [Shell Mode](#shell-mode)
8. [Cloud & Background Agents](#cloud--background-agents)
9. [State & Persistence](#state--persistence)
10. [Error Handling & Debugging](#error-handling--debugging)
11. [Rules & AGENT.md Integration](#rules--agentmd-integration)
12. [Practical Examples](#practical-examples)

---

## Installation & Setup

### Quick Install

**macOS, Linux, and Windows (WSL):**
```bash
curl https://cursor.com/install -fsS | bash
```

**Windows (PowerShell):**
```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

### Post-Installation Configuration

Update your shell's PATH variable:

**For bash (~/.bashrc):**
```bash
export PATH="$HOME/.local/bin:$PATH"
```

**For zsh (~/.zshrc):**
```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload your shell:
```bash
source ~/.bashrc  # or ~/.zshrc
```

### Verify Installation

```bash
agent --version
```

### Updates

Manually trigger updates:
```bash
agent update
```

---

## Core Commands

| Command | Purpose |
|---------|---------|
| `agent` | Start interactive Agent mode (default) |
| `agent resume` | Resume the most recent conversation |
| `agent ls` | Display list of previous conversations |
| `agent login` | Authenticate with Cursor account |
| `agent logout` | Sign out from Cursor |
| `agent status` | Check current session status |
| `agent models` | List available models |
| `agent mcp` | Manage MCP servers (see MCP section) |
| `agent update` | Update CLI to latest version |
| `agent --help` | Display help information |
| `agent --version` | Show version info |

### Session Management Commands

```bash
# Resume specific conversation by thread ID
agent --resume [thread-id]

# Continue from previous session (shorthand)
agent --continue

# List all previous conversations
agent ls
```

---

## CLI Flags & Parameters

### Global Options

| Flag | Aliases | Purpose | Example |
|------|---------|---------|---------|
| `--api-key <key>` | | API credentials | `agent --api-key sk_live_...` |
| `--mode <mode>` | `--plan`, `--ask` | Set operating mode | `agent --mode plan` |
| `--model <model>` | | Specify AI model | `agent --model claude-3-5-sonnet` |
| `-p, --print` | | Non-interactive mode (script-friendly) | `agent -p "write a function"` |
| `--output-format <format>` | | Output format (`text`, `json`, `stream-json`) | `agent --output-format json` |
| `--resume [chatId]` | `--continue` | Load prior context from thread | `agent --resume abc123` |
| `-f, --force` | `--yolo` | Allow all commands without approval | `agent -f` |
| `--approve-mcps` | | Skip MCP server approval prompts | `agent --approve-mcps` |
| `--sandbox <mode>` | | Control sandboxing (`enabled`, `disabled`) | `agent --sandbox disabled` |
| `-w, --workspace <path>` | | Specify working directory | `agent -w /path/to/project` |
| `-H, --header <header>` | | Custom headers (format: "Name: Value") | `agent -H "X-Custom: value"` |
| `-v, --version` | | Display version | `agent -v` |
| `-h, --help` | | Display help | `agent -h` |

### Environment Variables

| Variable | Purpose |
|----------|---------|
| `CURSOR_API_KEY` | API key for authentication |
| `CURSOR_CONFIG_DIR` | Override config directory path |
| `XDG_CONFIG_HOME` | Linux/BSD alternative for config path |

### Example: Non-Interactive Usage

```bash
# Run in non-interactive mode, output to JSON
agent -p --output-format json "Analyze this codebase structure"

# Parse JSON output
agent -p --output-format json "Generate unit tests" | jq '.response'
```

---

## Operating Modes

### Agent Mode (Default)

Full tool access for complex coding tasks. The agent can:
- Generate and modify files
- Run terminal commands
- Search the codebase
- Review and approve changes

Start with:
```bash
agent
```

### Plan Mode

Design approaches with clarifying questions before coding. Useful for:
- Understanding requirements
- Breaking down complex tasks
- Reviewing proposed strategies

Start with:
```bash
agent --mode=plan
# or
agent --plan
```

**In interactive mode, switch anytime:**
```
Shift+Tab  # Rotate between modes
/plan      # Switch to Plan mode
/ask       # Switch to Ask mode
```

### Ask Mode

Read-only code exploration without making changes. Useful for:
- Code review
- Understanding existing code
- Asking questions about implementation

Start with:
```bash
agent --mode=ask
# or
agent --ask
```

---

## Configuration Files

### Global Configuration

**macOS/Linux:**
```
~/.cursor/cli-config.json
```

**Windows:**
```
$env:USERPROFILE\.cursor\cli-config.json
```

### Project-Level Configuration

```
<project>/.cursor/cli.json
```

### Configuration Schema

```json
{
  "schema_version": 1,
  "vim_keybindings": false,
  "permitted_operations": [
    "write_files",
    "run_commands"
  ],
  "forbidden_operations": [
    "delete_files"
  ],
  "model": "claude-3-5-sonnet",
  "network": {
    "http_version": "1.1"
  },
  "attribution": {
    "commit_signature": true
  }
}
```

### Configurable Settings

| Setting | Type | Default | Purpose |
|---------|------|---------|---------|
| `schema_version` | number | 1 | Config schema version |
| `vim_keybindings` | boolean | false | Enable Vim keybindings |
| `permitted_operations` | array | [] | Allowed operations |
| `forbidden_operations` | array | [] | Blocked operations |
| `model` | string | (default model) | AI model to use |
| `http_version` | string | auto | HTTP version (for proxies) |
| `commit_signature` | boolean | true | Add attribution to commits |

### Overriding Configuration

**Via environment variables:**
```bash
CURSOR_CONFIG_DIR=/custom/path agent
```

**Via CLI parameter:**
```bash
agent --model gpt-4
```

**Via slash command (interactive):**
```
/model claude-3-5-sonnet
```

---

## MCP Server Integration

### Available Commands

| Command | Purpose |
|---------|---------|
| `agent mcp list` | Show all configured MCP servers and connection status |
| `agent mcp list-tools <identifier>` | Show available tools from a specific server |
| `agent mcp enable <identifier>` | Enable a specific MCP server |
| `agent mcp disable <identifier>` | Disable a specific MCP server |
| `agent mcp login <identifier>` | Authenticate with an MCP server |

### Example Commands

```bash
# List all MCP servers
agent mcp list

# See what tools playwright server offers
agent mcp list-tools playwright

# Enable an MCP server
agent mcp enable github

# Authenticate with a server
agent mcp login github

# Run agent with auto-approval of MCP tools
agent --approve-mcps "fix this bug"
```

### Configuration Format

MCP servers are configured in the same location as editor configuration. The CLI automatically respects:
- `mcp.json` (project-level)
- `.cursor/` configuration directory
- Global MCP settings from Cursor editor

### Auto-Discovery

The agent automatically:
- Discovers configured MCP servers
- Detects available tools
- Applies MCP tools when relevant to requests
- Uses `--approve-mcps` flag to skip approval prompts

### Server Connection Status

When listing servers (`agent mcp list`), output shows:
- Server name and identifier
- Connection status (connected/disconnected)
- Transport method (stdio, SSE, etc.)

### Best Practices

1. **Configure servers first:** Set up MCP servers in Cursor editor, they'll work in CLI
2. **Test connections:** Use `agent mcp list` to verify servers are accessible
3. **Authenticate when needed:** Use `agent mcp login` for servers requiring auth
4. **Use approval flag for CI:** Use `--approve-mcps` in automated environments

---

## Shell Mode

### Overview

Execute shell commands directly from CLI with built-in safety checks and output display.

### How It Works

- Commands execute in your login shell (`$SHELL`)
- Uses CLI's current working directory and environment
- Output displays automatically in conversation
- Safety permissions checking before execution
- 30-second command timeout (not adjustable)

### Supported Commands

Ideal for:
- Status checks (`git status`, `ls -la`)
- Quick builds (`npm run build`)
- File operations (`cp`, `mv`, `mkdir`)
- Environment inspection (`echo $PATH`)

### Limitations

**Cannot:**
- Run long-running processes (>30 seconds)
- Execute interactive applications
- Run servers or daemons
- Handle commands requiring user input
- Persist directory changes between commands

### Examples

```bash
# Quick status check
git status

# Chain commands with directory context
cd src && npm test

# Approve command execution
# You'll be prompted: "Approve? (y/n/always)" - respond y, n, or "always"

# Expand truncated output
Ctrl+O  # In interactive mode
```

### Permissions & Approval

When running commands, you'll see:
```
Execute: git commit -m "fix: bug"?
→ (y)es / (n)o / (a)lways
```

Options:
- `y` - Approve this command once
- `n` - Reject this command
- `a` - Approve all future commands (sets `--force`)

### Troubleshooting

| Issue | Solution |
|-------|----------|
| Command hangs | Press `Ctrl+C` to cancel |
| Output truncated | Use `Ctrl+O` to expand in interactive mode |
| Command rejected | Check admin policies or use `--force` flag |
| 30-second timeout | Split into smaller commands or use background agents |

---

## Cloud & Background Agents

### Cloud Agents

Cloud agents run in isolated cloud environments without requiring your local machine to stay connected.

#### Quick Start

**Send current conversation to cloud:**
```bash
agent
# In interactive mode:
& your next prompt here
```

The `&` prefix sends the conversation to Cloud Agent, which continues running while you can monitor progress at `cursor.com/agents` or on mobile.

#### Features

- **Parallel execution:** Run as many agents as you want simultaneously
- **No internet required locally:** Agent continues in cloud while you're offline
- **Multiple access points:**
  - Web: `cursor.com/agents`
  - Desktop app
  - Slack integration
  - GitHub integration
  - Linear integration
  - API endpoints

#### Configuration Requirements

- **Models:** Only "Max Mode-compatible models" available
- **Authentication:** Cursor account with trial or paid plan
- **Repository access:** Read-write permission to your GitHub/GitLab repo
- **Pricing:** Usage-based (requires usage-based pricing enabled)

#### How It Works

1. Agent connects to your GitHub/GitLab repository
2. Clones your code
3. Works on a separate branch
4. Pushes changes back for review
5. You can review and merge PR

### Cloud Agents API

Access Cloud Agents programmatically via REST API.

#### Authentication

```bash
# Get API key from: https://cursor.com/account/api/keys
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.cursor.sh/v1/agents
```

#### Common Endpoints

```bash
# List agents
curl https://api.cursor.sh/v1/agents \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get specific agent status
curl https://api.cursor.sh/v1/agents/{agent_id} \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get agent conversation history
curl https://api.cursor.sh/v1/agents/{agent_id}/messages \
  -H "Authorization: Bearer YOUR_API_KEY"

# Get current status and results
curl https://api.cursor.sh/v1/agents/{agent_id}/status \
  -H "Authorization: Bearer YOUR_API_KEY"
```

#### List Available Models

```bash
curl https://api.cursor.sh/v1/agents/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## State & Persistence

### Session State Storage

State is persisted to allow conversation resumption:

```bash
# List all previous conversations
agent ls

# Resume specific conversation
agent --resume <thread-id>

# Continue from last session
agent --continue
```

### Secrets Management

**For Cloud Agents:**
- Secrets are stored encrypted-at-rest (using KMS) in Cursor's database
- Provided in cloud environment automatically
- Do NOT use `.env.local` files
- Configure through Cursor's **Secrets tab** in UI

**For Local Agents:**
- Use environment variables
- Load from `.env` files locally

### Configuration Persistence

Configuration persists in:
- Global: `~/.cursor/cli-config.json`
- Project: `<project>/.cursor/cli.json`

### Disk Caching

Cursor caches disk state for performance:
- Initial install caches state
- Speeds up subsequent startups
- Automatically managed

### State Reset

If you encounter issues, reset state:

```bash
# Remove state files
rm -rf ~/.cursor-cli/state
rm -rf ~/.cursor-cli/cache

# Reinitialize with verbose logging
agent init --verbose --force
```

### Data Retention

Background agents require data retention on the order of a few days. Cloud infrastructure maintains conversation history and agent state for this period.

---

## Error Handling & Debugging

### Verbose Initialization

```bash
# Reinitialize with verbose logging for troubleshooting
agent init --verbose --force
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `Error: Subagent connection timeout` | Connection lost to AI service | Run `agent init --verbose --force`, check internet |
| `Failed to initialize AI context` | Configuration issue | Reset state: `rm -rf ~/.cursor-cli/{state,cache}` |
| Incompatible CLI version | Version mismatch | Run `agent update` |
| Subagent connection failed | Network/firewall issue | Verify `api.cursor.sh:443` and `:8443` accessible |

### Network Requirements

Cursor CLI requires outbound connections to:
- **Host:** `api.cursor.sh`
- **Ports:** `443` (HTTPS), `8443` (WebSocket)

Verify connectivity:
```bash
curl -v https://api.cursor.sh
```

### Testing Connection

```bash
# Test subagent connection
agent agent test
```

### Verbose Logging

The CLI supports verbosity levels for debugging. To see more detailed logs:

```bash
# Initialize with verbose output
agent init --verbose --force

# Run command with verbose flag
agent --verbose "your prompt here"
```

### Log Output

Logs are typically displayed in console output. For persistent debugging with hooks, use:

```javascript
// In your hooks, use console.error instead of console.log
// to direct output to stderr (visible in Cursor)
console.error("Debug message:", value);
```

### File-Based Logging

For production debugging with persistent logs:
```javascript
// Write logs to a file
const fs = require('fs');
fs.appendFileSync('/tmp/cursor-debug.log', `[${new Date().toISOString()}] ${message}\n`);
```

---

## Rules & AGENT.md Integration

### Project Rules Directory

Create rules in your project to guide the agent:

```
<project>/.cursor/rules/
├── coding-standards.md
├── architecture.md
└── testing-requirements.md
```

### AGENT.md Support

Cursor respects the `AGENTS.md` specification. Create at project root:

```
<project>/AGENTS.md
```

### Example AGENT.md

```markdown
# Agent Instructions

## Project Context
You are working on a React + TypeScript web application.

## Code Style
- Use TypeScript for all new files
- Follow Airbnb ESLint config
- Components use functional style with hooks

## Before Writing Code
1. Review existing patterns in `/src/components`
2. Check type definitions in `/types`
3. Ensure TypeScript strictness

## Testing Requirements
- All components need unit tests
- Use Jest and React Testing Library
- Maintain >80% code coverage

## Commit Format
- Use conventional commits
- Reference GitHub issues
- Keep commits atomic
```

### Rules Priority

Rules are loaded automatically based on this hierarchy:
1. **Project Rules:** `.cursor/rules/` and `AGENTS.md`
2. **Team Rules:** Shared team configuration (if configured)
3. **User Rules:** Global user preferences

### Using Rules with CLI

Rules automatically apply to:
```bash
agent "write a new component"
```

Rules guide the agent's:
- Code generation style
- File organization
- Naming conventions
- Testing approaches
- Documentation standards

### Updating Rules

Edit `.cursor/rules/` or `AGENTS.md` directly. The CLI reads rules on every invocation, so changes take effect immediately.

```bash
# Edit project rules
echo "## New Guideline" >> .cursor/rules/coding-standards.md

# Next agent invocation will use updated rules
agent "follow the new guideline"
```

---

## Practical Examples

### Example 1: Interactive Code Generation

```bash
# Start interactive session
agent

# In the interactive prompt:
> Write a React hook for managing form state
# Agent generates code, asks clarifying questions
# You review and approve/modify changes
# Ctrl+R to review, Ctrl+D to exit (double-press)
```

### Example 2: Non-Interactive CI/CD Usage

```bash
# Generate code, output JSON for parsing
agent -p --output-format json "Generate authentication service" > output.json

# Parse the response
jq '.response' output.json
jq '.files_created[]' output.json
```

### Example 3: Plan-Driven Development

```bash
# Start in plan mode
agent --plan

# Agent asks clarifying questions:
# "What's the scope?"
# "Should we refactor first?"
# "What dependencies exist?"

# Review plan, then switch to code:
/ask  # Ask more questions without coding
# Then:
/agent  # Switch back to full agent mode
```

### Example 4: Using MCP Tools

```bash
# Check available tools
agent mcp list

# See Playwright tools
agent mcp list-tools playwright

# Use tools automatically
agent "navigate to example.com and click the login button"
# Agent uses Playwright MCP to control browser

# Auto-approve MCP in scripting
agent --approve-mcps "run these tests using pytest"
```

### Example 5: Resuming Work

```bash
# List recent conversations
agent ls

# Resume specific conversation
agent --resume eaf2c4c8

# Continue conversation
agent --continue
```

### Example 6: Cloud Agent Handoff

```bash
# Start local session
agent

# Later, push to cloud:
> & Implement the full feature in the background

# Monitor progress at:
# - cursor.com/agents
# - Mobile app
# - Continue local work
```

### Example 7: Shell Commands with Approval

```bash
# Start agent
agent

# Agent proposes: "Run tests with: npm test"
# You see prompt:
# Execute: npm test?
# → (y)es / (n)o / (a)lways

# Choose "always" to approve all future commands
# Or use -f flag to skip prompts:
agent -f "run the test suite"
```

### Example 8: Working with Specific Models

```bash
# Check available models
agent models

# Use specific model
agent --model claude-3-5-sonnet "write this algorithm"

# Or set model in config and it persists
```

### Example 9: Custom Workspace

```bash
# Run agent on a specific project
agent -w /path/to/project "refactor the auth module"

# Equivalent to:
cd /path/to/project && agent "refactor the auth module"
```

### Example 10: Debugging Agent Issues

```bash
# Clear cache and reinitialize
rm -rf ~/.cursor-cli/state ~/.cursor-cli/cache

# Reinit with verbose output
agent init --verbose --force

# Test connection
agent agent test

# Try again
agent "simple test prompt"
```

---

## References

**Official Documentation:**
- [Cursor CLI Overview](https://cursor.com/docs/cli/overview)
- [Using Agent in CLI](https://cursor.com/docs/cli/using)
- [Cursor CLI Installation](https://cursor.com/docs/cli/installation)
- [Cursor CLI Parameters](https://cursor.com/docs/cli/reference/parameters)
- [Cursor CLI Configuration](https://cursor.com/docs/cli/reference/configuration)
- [MCP Integration](https://cursor.com/docs/cli/mcp)
- [Shell Mode](https://cursor.com/docs/cli/shell-mode)
- [Cloud Agents](https://cursor.com/docs/cloud-agent)
- [Cloud Agents API](https://cursor.com/docs/cloud-agent/api/endpoints)
- [Rules & AGENT.md](https://cursor.com/docs/context/rules)

---

## Quick Command Cheat Sheet

```bash
# Installation & Setup
curl https://cursor.com/install -fsS | bash
agent --version
agent update

# Session Management
agent                          # Start interactive session
agent --resume <thread-id>     # Resume conversation
agent ls                       # List all conversations
agent --continue               # Continue from last session

# Modes & Configuration
agent --plan                   # Start in plan mode
agent --ask                    # Start in ask mode
agent --model claude-3-5-sonnet # Use specific model

# Non-Interactive
agent -p "your prompt"         # Print mode
agent --output-format json "prompt" # JSON output

# MCP & Tools
agent mcp list                 # List MCP servers
agent mcp list-tools playwright # See available tools
agent --approve-mcps "prompt"  # Auto-approve MCP

# Cloud Agents
agent                          # Start local
# Then type: & your next prompt # Send to cloud

# Debugging
agent init --verbose --force   # Reinit with verbosity
agent agent test               # Test connection
rm -rf ~/.cursor-cli/{state,cache} # Reset state
```

---

**Document Status:** Complete reference as of February 27, 2026
**Beta Status:** Tool is in active development; features may change
**Last Verified:** Official Cursor documentation
