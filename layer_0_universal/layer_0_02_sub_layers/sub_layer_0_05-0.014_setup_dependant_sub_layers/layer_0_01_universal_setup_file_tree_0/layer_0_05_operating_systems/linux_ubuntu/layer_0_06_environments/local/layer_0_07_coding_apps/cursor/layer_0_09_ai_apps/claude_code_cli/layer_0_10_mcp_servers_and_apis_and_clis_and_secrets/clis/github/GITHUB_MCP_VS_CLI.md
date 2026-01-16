# GitHub MCP Server vs gh CLI in Claude Code

## TL;DR

**Use the `gh` CLI.** This is Anthropic's official recommendation **specifically for Claude Code**.

> **Note**: This recommendation is specific to Claude Code. Other AI CLI tools (Codex CLI, Gemini CLI) have different integration approaches. See the `_shared` directory for cross-tool documentation.

## Official Recommendation

From [Anthropic's Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices):

> "For using Claude Code with GitHub operations, Anthropic's official best practices recommend installing and using the `gh` CLI over the GitHub MCP server."

## Comparison

| Feature | gh CLI | GitHub MCP Server |
|---------|--------|-------------------|
| **Recommended** | ✅ Yes | ❌ Fallback only |
| **Setup Complexity** | Simple | More complex |
| **Authentication** | Local OAuth | Token + server config |
| **Claude Training** | Trained on gh | Less emphasis |
| **Native Integration** | Yes | Requires MCP protocol |
| **Reliability** | High | Depends on server |

## gh CLI Advantages

1. **Native Support**: Claude Code "knows how to use the `gh` CLI" directly in terminal workflows
2. **Simpler Setup**: No extra servers or tokens beyond local authentication
3. **Efficient Operations**: Handles PR creation, issue management, commits, rebases, builds
4. **Training Alignment**: Claude is specifically trained on gh CLI usage
5. **No Server Overhead**: Runs locally without additional processes

## GitHub MCP Server Use Cases

The MCP server is appropriate **only** when:
- `gh` CLI cannot be installed
- You need specific GitHub API calls not supported by gh
- You're building custom integrations requiring MCP protocol

## When NOT to Use GitHub MCP Server

- For standard Claude Code workflows
- When gh CLI is available
- For common operations (issues, PRs, repos, actions)
- When simplicity is preferred

## Setup Comparison

### gh CLI Setup (Recommended)
```bash
# Install
sudo apt install gh

# Authenticate
gh auth login

# Configure git
gh auth setup-git

# Done!
```

### GitHub MCP Server Setup (Not Recommended)
```bash
# Install MCP server
npm install -g @anthropic/github-mcp-server

# Generate GitHub token
# (requires going to GitHub settings)

# Configure in claude settings
# Add to ~/.claude.json mcpServers section

# Restart Claude Code

# Debug if issues occur...
```

## Conclusion

For Claude Code on Linux (or any platform):
1. **Install gh CLI** - simple, one command
2. **Authenticate** - `gh auth login`
3. **Configure git** - `gh auth setup-git`
4. **Use Claude Code** - it will use gh automatically

The GitHub MCP server adds unnecessary complexity for no additional benefit in standard workflows.

## References

- [Anthropic Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [GitHub CLI Documentation](https://cli.github.com/)
- [GitHub MCP Server](https://github.com/anthropics/github-mcp-server) (for reference only)
