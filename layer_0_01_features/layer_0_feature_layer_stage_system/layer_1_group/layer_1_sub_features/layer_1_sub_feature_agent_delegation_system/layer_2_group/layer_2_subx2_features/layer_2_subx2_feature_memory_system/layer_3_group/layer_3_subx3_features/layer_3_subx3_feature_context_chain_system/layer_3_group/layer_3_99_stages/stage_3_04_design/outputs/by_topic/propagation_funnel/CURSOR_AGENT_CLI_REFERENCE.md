# Cursor Agent CLI Reference Guide

**Last Updated:** 2026-02-27
**Tool Status:** Active (Beta)
**Official Docs:** https://cursor.com/docs/cli/

---

<!-- section_id: "e10d853a-4df9-42d3-9358-fa41bf115f05" -->
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

<!-- section_id: "b03fc584-fd00-4038-a10a-8eba489044f3" -->
## Installation & Setup

<!-- section_id: "81be82d2-5029-46e1-9f5d-e0b2c401589f" -->
### Quick Install

**macOS, Linux, and Windows (WSL):**
```bash
curl https://cursor.com/install -fsS | bash
```

**Windows (PowerShell):**
```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

<!-- section_id: "fc47c11a-465e-4cb8-8e13-f1e88e4907a0" -->
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

<!-- section_id: "b2c8806d-a732-4d50-b4d7-aeeec0896d7d" -->
### Verify Installation

```bash
agent --version
```

<!-- section_id: "3b10951d-cb6a-44c7-aa72-b8acfe0a5670" -->
### Updates

Manually trigger updates:
```bash
agent update
```

---

<!-- section_id: "e78087a4-143b-40cf-9a4c-36a20598f2fa" -->
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

<!-- section_id: "e7859700-0b59-44ad-96d6-813b773640a3" -->
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

<!-- section_id: "1e7d7e2b-4611-4870-b113-efd83928fb9b" -->
## CLI Flags & Parameters

<!-- section_id: "905d266f-d1fb-47f3-99dc-83dc6c8e7bb2" -->
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

<!-- section_id: "5cf535ee-a6d8-430a-8b3c-963ff3b6b7ae" -->
### Environment Variables

| Variable | Purpose |
|----------|---------|
| `CURSOR_API_KEY` | API key for authentication |
| `CURSOR_CONFIG_DIR` | Override config directory path |
| `XDG_CONFIG_HOME` | Linux/BSD alternative for config path |

<!-- section_id: "12c6b5aa-1fc3-48cb-8574-b5b7816a261b" -->
### Example: Non-Interactive Usage

```bash
# Run in non-interactive mode, output to JSON
agent -p --output-format json "Analyze this codebase structure"

# Parse JSON output
agent -p --output-format json "Generate unit tests" | jq '.response'
```

---

<!-- section_id: "a432373d-591f-47a1-aca5-88433d97ff7f" -->
## Operating Modes

<!-- section_id: "228d1e91-aa02-4672-ad0f-522b12ce4476" -->
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

<!-- section_id: "852bbed5-5cbf-4bd3-a2a6-ab13d98f0e15" -->
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

<!-- section_id: "db001516-a90a-422f-a76a-93636efe3e40" -->
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

<!-- section_id: "7a5bedb3-329c-478d-b116-bdebc2dc39f4" -->
## Configuration Files

<!-- section_id: "8ac00f0d-173b-4d0b-a723-0e8c4ad2cf4f" -->
### Global Configuration

**macOS/Linux:**
```
~/.cursor/cli-config.json
```

**Windows:**
```
$env:USERPROFILE\.cursor\cli-config.json
```

<!-- section_id: "3882d571-c23f-4bc0-a8b8-1389b6e43ce6" -->
### Project-Level Configuration

```
<project>/.cursor/cli.json
```

<!-- section_id: "d9389030-95c8-4ab7-aa8d-f97ded0cdf85" -->
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

<!-- section_id: "56c8c5d0-1fce-4808-8ce9-95894c9e2594" -->
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

<!-- section_id: "cc5e56c0-a5b2-4fb6-ab87-8de9f15f8b12" -->
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

<!-- section_id: "044b94bd-2eba-42c7-8d60-7f5ee92bb21c" -->
## MCP Server Integration

<!-- section_id: "48495588-0db2-4df6-966c-4c70d7be2b9f" -->
### Available Commands

| Command | Purpose |
|---------|---------|
| `agent mcp list` | Show all configured MCP servers and connection status |
| `agent mcp list-tools <identifier>` | Show available tools from a specific server |
| `agent mcp enable <identifier>` | Enable a specific MCP server |
| `agent mcp disable <identifier>` | Disable a specific MCP server |
| `agent mcp login <identifier>` | Authenticate with an MCP server |

<!-- section_id: "5f023f89-a82b-45ad-bd92-63564b9c724f" -->
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

<!-- section_id: "2dd6c6dc-a643-410d-b271-759d6bd739bc" -->
### Configuration Format

MCP servers are configured in the same location as editor configuration. The CLI automatically respects:
- `mcp.json` (project-level)
- `.cursor/` configuration directory
- Global MCP settings from Cursor editor

<!-- section_id: "87534b6b-a5f5-4911-b54f-7c0bcf81c6b0" -->
### Auto-Discovery

The agent automatically:
- Discovers configured MCP servers
- Detects available tools
- Applies MCP tools when relevant to requests
- Uses `--approve-mcps` flag to skip approval prompts

<!-- section_id: "70fe46ec-7acd-4054-b546-54e94c16dcf3" -->
### Server Connection Status

When listing servers (`agent mcp list`), output shows:
- Server name and identifier
- Connection status (connected/disconnected)
- Transport method (stdio, SSE, etc.)

<!-- section_id: "bef80dfe-6411-414f-92fc-f490a7c2ed32" -->
### Best Practices

1. **Configure servers first:** Set up MCP servers in Cursor editor, they'll work in CLI
2. **Test connections:** Use `agent mcp list` to verify servers are accessible
3. **Authenticate when needed:** Use `agent mcp login` for servers requiring auth
4. **Use approval flag for CI:** Use `--approve-mcps` in automated environments

---

<!-- section_id: "1acb1a48-6487-42c6-bb0b-b9ed1aa739f6" -->
## Shell Mode

<!-- section_id: "2dfb3adc-d0f3-40e7-8f0b-ee360947266e" -->
### Overview

Execute shell commands directly from CLI with built-in safety checks and output display.

<!-- section_id: "b34d3f25-a341-4909-a5c8-5c87cb7a9445" -->
### How It Works

- Commands execute in your login shell (`$SHELL`)
- Uses CLI's current working directory and environment
- Output displays automatically in conversation
- Safety permissions checking before execution
- 30-second command timeout (not adjustable)

<!-- section_id: "80d9a714-988b-4ee8-8233-fb251a9b5620" -->
### Supported Commands

Ideal for:
- Status checks (`git status`, `ls -la`)
- Quick builds (`npm run build`)
- File operations (`cp`, `mv`, `mkdir`)
- Environment inspection (`echo $PATH`)

<!-- section_id: "823531cb-b16b-49a5-9db1-b8dca4ebb674" -->
### Limitations

**Cannot:**
- Run long-running processes (>30 seconds)
- Execute interactive applications
- Run servers or daemons
- Handle commands requiring user input
- Persist directory changes between commands

<!-- section_id: "fe4fc221-7ee0-41fc-a030-165b04d070b0" -->
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

<!-- section_id: "705467d5-fecd-48a3-8fea-88a2ef2cc5d3" -->
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

<!-- section_id: "b3ae844f-7705-4d2b-b832-48e1acc5f92c" -->
### Troubleshooting

| Issue | Solution |
|-------|----------|
| Command hangs | Press `Ctrl+C` to cancel |
| Output truncated | Use `Ctrl+O` to expand in interactive mode |
| Command rejected | Check admin policies or use `--force` flag |
| 30-second timeout | Split into smaller commands or use background agents |

---

<!-- section_id: "a693cbeb-87b3-47dd-a5d1-041e38c7269b" -->
## Cloud & Background Agents

<!-- section_id: "ba5bb5ae-4102-4244-896b-06560f7a7619" -->
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

<!-- section_id: "3d6995e8-12dc-43ba-a78b-a7167cc4930d" -->
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

<!-- section_id: "5628de1c-318d-413b-a87e-124c3d3d2acf" -->
## State & Persistence

<!-- section_id: "48cc7c8c-271d-4e21-b297-11a4c7366f15" -->
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

<!-- section_id: "811247e2-453f-400a-86a4-be92ef5e7b3c" -->
### Secrets Management

**For Cloud Agents:**
- Secrets are stored encrypted-at-rest (using KMS) in Cursor's database
- Provided in cloud environment automatically
- Do NOT use `.env.local` files
- Configure through Cursor's **Secrets tab** in UI

**For Local Agents:**
- Use environment variables
- Load from `.env` files locally

<!-- section_id: "665b14f3-687f-4575-a598-f7321710f645" -->
### Configuration Persistence

Configuration persists in:
- Global: `~/.cursor/cli-config.json`
- Project: `<project>/.cursor/cli.json`

<!-- section_id: "33d5df56-1f94-4ffa-a441-70012b2e1017" -->
### Disk Caching

Cursor caches disk state for performance:
- Initial install caches state
- Speeds up subsequent startups
- Automatically managed

<!-- section_id: "915a319e-6196-41d3-b1cc-a31a5aec4d26" -->
### State Reset

If you encounter issues, reset state:

```bash
# Remove state files
rm -rf ~/.cursor-cli/state
rm -rf ~/.cursor-cli/cache

# Reinitialize with verbose logging
agent init --verbose --force
```

<!-- section_id: "4d2e9009-d6d0-4e09-b4d0-a208272dd789" -->
### Data Retention

Background agents require data retention on the order of a few days. Cloud infrastructure maintains conversation history and agent state for this period.

---

<!-- section_id: "8d713ee0-06c2-4ce1-985a-778be690da26" -->
## Error Handling & Debugging

<!-- section_id: "94c74dbd-1b19-483a-8e9c-c2855154320b" -->
### Verbose Initialization

```bash
# Reinitialize with verbose logging for troubleshooting
agent init --verbose --force
```

<!-- section_id: "590a3fa5-601e-4356-8aa3-637214e8ddbd" -->
### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `Error: Subagent connection timeout` | Connection lost to AI service | Run `agent init --verbose --force`, check internet |
| `Failed to initialize AI context` | Configuration issue | Reset state: `rm -rf ~/.cursor-cli/{state,cache}` |
| Incompatible CLI version | Version mismatch | Run `agent update` |
| Subagent connection failed | Network/firewall issue | Verify `api.cursor.sh:443` and `:8443` accessible |

<!-- section_id: "b7d39a70-35f1-4027-ae58-36211f4f1637" -->
### Network Requirements

Cursor CLI requires outbound connections to:
- **Host:** `api.cursor.sh`
- **Ports:** `443` (HTTPS), `8443` (WebSocket)

Verify connectivity:
```bash
curl -v https://api.cursor.sh
```

<!-- section_id: "dacfb363-370e-4243-8245-fb076521c970" -->
### Testing Connection

```bash
# Test subagent connection
agent agent test
```

<!-- section_id: "a1b36e75-aefc-49ff-817c-f2af06f5870e" -->
### Verbose Logging

The CLI supports verbosity levels for debugging. To see more detailed logs:

```bash
# Initialize with verbose output
agent init --verbose --force

# Run command with verbose flag
agent --verbose "your prompt here"
```

<!-- section_id: "431e06f3-0866-43fb-b92a-c817d962e6ac" -->
### Log Output

Logs are typically displayed in console output. For persistent debugging with hooks, use:

```javascript
// In your hooks, use console.error instead of console.log
// to direct output to stderr (visible in Cursor)
console.error("Debug message:", value);
```

<!-- section_id: "ccf619d7-d913-4c94-87cf-f282baddb50d" -->
### File-Based Logging

For production debugging with persistent logs:
```javascript
// Write logs to a file
const fs = require('fs');
fs.appendFileSync('/tmp/cursor-debug.log', `[${new Date().toISOString()}] ${message}\n`);
```

---

<!-- section_id: "abdab279-4fc8-44be-ae05-a8cd2816715e" -->
## Rules & AGENT.md Integration

<!-- section_id: "2f8a71bf-f7ca-4b67-87ff-42daac210a65" -->
### Project Rules Directory

Create rules in your project to guide the agent:

```
<project>/.cursor/rules/
├── coding-standards.md
├── architecture.md
└── testing-requirements.md
```

<!-- section_id: "9e185116-9079-4d5c-b169-842f312c193f" -->
### AGENT.md Support

Cursor respects the `AGENTS.md` specification. Create at project root:

```
<project>/AGENTS.md
```

<!-- section_id: "6f53aab6-bdba-4d62-b1b8-4f463d05d844" -->
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

<!-- section_id: "bdb3938d-f74c-4ca7-beb0-d1dbcc5b9624" -->
### Rules Priority

Rules are loaded automatically based on this hierarchy:
1. **Project Rules:** `.cursor/rules/` and `AGENTS.md`
2. **Team Rules:** Shared team configuration (if configured)
3. **User Rules:** Global user preferences

<!-- section_id: "fbadcced-9ac7-46a7-b590-f6dc0f83428f" -->
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

<!-- section_id: "d5d1e1da-b562-4448-b5f0-519cfe39b222" -->
### Updating Rules

Edit `.cursor/rules/` or `AGENTS.md` directly. The CLI reads rules on every invocation, so changes take effect immediately.

```bash
# Edit project rules
echo "## New Guideline" >> .cursor/rules/coding-standards.md

# Next agent invocation will use updated rules
agent "follow the new guideline"
```

---

<!-- section_id: "81ea6695-9312-4868-ae0b-0fe98174f0bf" -->
## Practical Examples

<!-- section_id: "f86642e7-9c9f-425d-a0ba-6e99b3c88a5e" -->
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

<!-- section_id: "711f62bf-6ac1-4193-8683-931cee3f2d08" -->
### Example 2: Non-Interactive CI/CD Usage

```bash
# Generate code, output JSON for parsing
agent -p --output-format json "Generate authentication service" > output.json

# Parse the response
jq '.response' output.json
jq '.files_created[]' output.json
```

<!-- section_id: "eeb14685-0d89-4dbe-881c-4e6c63814342" -->
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

<!-- section_id: "2d4f2df8-5f65-43ca-a5a1-ef7f5829b798" -->
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

<!-- section_id: "9c0b0a32-67b7-4ea7-a056-a7518a4fc477" -->
### Example 5: Resuming Work

```bash
# List recent conversations
agent ls

# Resume specific conversation
agent --resume eaf2c4c8

# Continue conversation
agent --continue
```

<!-- section_id: "bbbb779e-38bf-48a7-b7e7-65501be0785a" -->
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

<!-- section_id: "7f956221-1fc8-413e-9f9a-54ba6c1f1b1b" -->
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

<!-- section_id: "36f21ec2-cbeb-43c1-a5c9-9fa82e0cbdd3" -->
### Example 8: Working with Specific Models

```bash
# Check available models
agent models

# Use specific model
agent --model claude-3-5-sonnet "write this algorithm"

# Or set model in config and it persists
```

<!-- section_id: "8db32a32-2853-4ad1-8d31-e2e4566dc0f1" -->
### Example 9: Custom Workspace

```bash
# Run agent on a specific project
agent -w /path/to/project "refactor the auth module"

# Equivalent to:
cd /path/to/project && agent "refactor the auth module"
```

<!-- section_id: "eef71c25-6cff-4057-8878-c9c2f36d0f12" -->
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

<!-- section_id: "4ac12449-e5e4-4b78-ab89-e57324d3259c" -->
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

<!-- section_id: "3cbb07a2-c158-455c-8b69-31a1f22af506" -->
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
