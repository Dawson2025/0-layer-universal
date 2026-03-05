---
resource_id: "b2763a8d-28f0-4ea9-a51f-075f9f866e59"
resource_type: "document"
resource_name: "GITHUB_MCP_VS_CLI"
---
# GitHub MCP Server vs gh CLI in Claude Code

<!-- section_id: "6a6b9401-e1a3-4793-a3f8-bf2a0e247bd6" -->
## TL;DR

**Use the `gh` CLI.** This is Anthropic's official recommendation **specifically for Claude Code**.

> **Note**: This recommendation is specific to Claude Code. Other AI CLI tools (Codex CLI, Gemini CLI) have different integration approaches. See the `_shared` directory for cross-tool documentation.

<!-- section_id: "c2a033fc-4c88-42cf-9658-e373be469564" -->
## Official Recommendation

From [Anthropic's Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices):

> "For using Claude Code with GitHub operations, Anthropic's official best practices recommend installing and using the `gh` CLI over the GitHub MCP server."

<!-- section_id: "3cac2fa2-c359-4021-ad43-b49e9e113638" -->
## Comparison

| Feature | gh CLI | GitHub MCP Server |
|---------|--------|-------------------|
| **Recommended** | ✅ Yes | ❌ Fallback only |
| **Setup Complexity** | Simple | More complex |
| **Authentication** | Local OAuth | Token + server config |
| **Claude Training** | Trained on gh | Less emphasis |
| **Native Integration** | Yes | Requires MCP protocol |
| **Reliability** | High | Depends on server |

<!-- section_id: "205d31bc-1082-43f2-9f2b-08128dba9627" -->
## gh CLI Advantages

1. **Native Support**: Claude Code "knows how to use the `gh` CLI" directly in terminal workflows
2. **Simpler Setup**: No extra servers or tokens beyond local authentication
3. **Efficient Operations**: Handles PR creation, issue management, commits, rebases, builds
4. **Training Alignment**: Claude is specifically trained on gh CLI usage
5. **No Server Overhead**: Runs locally without additional processes

<!-- section_id: "f8e8e5ec-0f5a-4e9f-85da-45c3543fbcf0" -->
## GitHub MCP Server Use Cases

The MCP server is appropriate **only** when:
- `gh` CLI cannot be installed
- You need specific GitHub API calls not supported by gh
- You're building custom integrations requiring MCP protocol

<!-- section_id: "4bbb8e4e-be7d-4129-ba0e-3c637d3a19fe" -->
## When NOT to Use GitHub MCP Server

- For standard Claude Code workflows
- When gh CLI is available
- For common operations (issues, PRs, repos, actions)
- When simplicity is preferred

<!-- section_id: "1a74b9c0-1ef4-43d5-9dfc-ba956e88f50c" -->
## Setup Comparison

<!-- section_id: "1ed11023-fe91-453a-a3ab-0d7890adb5d7" -->
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

<!-- section_id: "217af3df-6519-40f7-8dda-75866e670693" -->
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

<!-- section_id: "381f1786-4686-4237-b9cb-7d1a444ec82f" -->
## Conclusion

For Claude Code on Linux (or any platform):
1. **Install gh CLI** - simple, one command
2. **Authenticate** - `gh auth login`
3. **Configure git** - `gh auth setup-git`
4. **Use Claude Code** - it will use gh automatically

The GitHub MCP server adds unnecessary complexity for no additional benefit in standard workflows.

<!-- section_id: "1244ec2b-3147-4e48-9fa6-8a5de056b4b0" -->
## References

- [Anthropic Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [GitHub CLI Documentation](https://cli.github.com/)
- [GitHub MCP Server](https://github.com/anthropics/github-mcp-server) (for reference only)
