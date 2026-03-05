---
resource_id: "3057d446-b838-4ef1-96d9-376d48e71dfb"
resource_type: "document"
resource_name: "CLAUDE_CODE_CLI_GUIDE"
---
# Claude Code CLI Quick Reference

<!-- section_id: "21027fcc-554f-4ec7-b8aa-59e2483a04ae" -->
## ✅ Setup Complete!

Claude Code CLI is now installed and ready to use in your terminal.

<!-- section_id: "1a9a2a3f-cd9d-4632-bbd8-3390298f6431" -->
## 🚀 Quick Start

<!-- section_id: "dfba89c9-c768-4a54-8b11-3ff0178f4209" -->
### Load the Environment
Before using Claude Code, load the environment:
```bash
source .claude_alias
```

<!-- section_id: "c23fbb6f-7758-4448-b409-31fc56785495" -->
### Start Claude Code
```bash
claude
```

This will start an interactive session where you can chat with Claude about your code!

<!-- section_id: "460c9277-24a3-4eb6-a44c-9c4f92743403" -->
## 📖 Available Commands

| Command | Description |
|---------|-------------|
| `claude` | Start interactive mode |
| `claude "task"` | Run a one-time task |
| `claude -c` | Continue most recent conversation |
| `claude -r` | Resume a previous conversation |
| `claude commit` | Create a git commit |
| `claude --help` | Show all available options |

<!-- section_id: "829ec9dd-4ad9-41d2-bf0f-1d674d1ae782" -->
## 💡 Example Usage

<!-- section_id: "1c37853c-9f61-47f5-92f6-b03be1226e56" -->
### Interactive Mode
```bash
# Start interactive session
claude

# Then you can ask things like:
> refactor this function to use async/await
> add error handling to my API calls
> explain what this code does
> help me debug this issue
```

<!-- section_id: "319796fc-e383-4c05-a224-1d91dc559c39" -->
### One-time Tasks
```bash
# Quick code help
claude "help me write a function to sort an array"

# Code review
claude "review my latest changes for potential bugs"

# Documentation
claude "add documentation comments to my functions"
```

<!-- section_id: "cf3e74a9-d575-4cb4-a39a-4b136648f98a" -->
### Git Integration
```bash
# Auto-generate commit messages
claude commit
```

<!-- section_id: "b0d2d08e-a4e8-4045-a9e5-111c7a77ca12" -->
## 🔧 Environment Setup

<!-- section_id: "9f09a1aa-f840-4724-9ebb-5ad9421243ae" -->
### Option 1: Manual Setup (each session)
```bash
source .claude_alias
claude
```

<!-- section_id: "c5b89d30-3eb1-4995-806b-f82badd37bc0" -->
### Option 2: Auto-load (recommended)
Add to your `~/.bashrc` for automatic loading:
```bash
echo "source /home/runner/workspace/.claude_alias" >> ~/.bashrc
```

<!-- section_id: "86eaa0c5-836c-4e41-8f45-5f1dc30f78fb" -->
## 🎯 Inside Interactive Mode

Once you run `claude`, you'll be in an interactive session. Here are the available commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `exit` or `Ctrl+C` | Exit Claude Code |

<!-- section_id: "fd277137-4ff3-4da3-99f9-deaa0265e209" -->
## 🛠️ Troubleshooting

<!-- section_id: "5983a338-946b-49e7-a2b5-fb97895ce8bb" -->
### "command not found: claude"
```bash
# Load the environment first
source .claude_alias
```

<!-- section_id: "27f92c45-d356-4230-b394-862e37df22c6" -->
### "node: command not found"
```bash
# The environment setup should handle this, but if needed:
export NVM_DIR="$HOME/workspace/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

<!-- section_id: "f7a934d3-0b4b-4745-8865-5d56a019faa7" -->
### Authentication Issues
On first run, Claude Code will prompt you to authenticate:
- You can use your Claude.ai account (recommended)
- Or your Anthropic Console account
- Follow the prompts to log in

<!-- section_id: "c335f720-3d65-4595-8579-5f5e234a9469" -->
## 🎉 You're Ready!

Just run:
```bash
source .claude_alias
claude
```

And start coding with Claude! 🚀
