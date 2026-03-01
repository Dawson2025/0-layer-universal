# AI Apps (04_ai_apps)

## What This Contains

AI service CLI tool configurations and setups for accessing AI services from the command line. These are the AI assistant tools you interact with programmatically.

## Supported AI Apps

| App | Command | Location | Content |
|-----|---------|----------|---------|
| Claude Code | `claude` | 04_ai_apps/claude_code/ | Authentication, config, settings |
| Codex | `codex` | 04_ai_apps/codex/ | API key, models, settings |
| Gemini | `gemini` | 04_ai_apps/gemini/ | API key, models, settings |
| Cursor Agent | `cursor-agent` | 04_ai_apps/cursor_agent/ | Config, credentials, settings |
| Perplexity | API only | 04_ai_apps/perplexity/ | API key, endpoints, settings |

## Example Structure

For Claude Code CLI:
```
04_ai_apps/claude_code/
├── installation.md      # How it was installed
├── authentication.md    # API key and auth setup
├── config.md           # Configuration settings
├── models.md           # Available models
└── usage_examples.md   # Common usage patterns
```

## Next Layer

After AI apps configuration, the next layer is **05_plugins/** (editor and AI app extensions).
