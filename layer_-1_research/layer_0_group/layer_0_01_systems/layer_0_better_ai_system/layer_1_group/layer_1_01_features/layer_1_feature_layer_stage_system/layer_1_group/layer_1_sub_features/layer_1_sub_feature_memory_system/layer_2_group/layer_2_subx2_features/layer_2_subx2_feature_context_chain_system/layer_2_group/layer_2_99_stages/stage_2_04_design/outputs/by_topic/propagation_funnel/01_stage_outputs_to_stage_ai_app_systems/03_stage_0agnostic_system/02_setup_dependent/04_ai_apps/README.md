---
resource_id: "e9688528-9029-4e62-8d8c-b985d17bec1b"
resource_type: "readme
output"
resource_name: "README"
---
# AI Apps (04_ai_apps)

<!-- section_id: "76da0cbc-6d22-4bbf-8e67-9cd3607242d0" -->
## What This Contains

AI service CLI tool configurations and setups for accessing AI services from the command line. These are the AI assistant tools you interact with programmatically.

<!-- section_id: "59f125c5-c78a-4ac6-a788-7efd3e7700cc" -->
## Supported AI Apps

| App | Command | Location | Content |
|-----|---------|----------|---------|
| Claude Code | `claude` | 04_ai_apps/claude_code/ | Authentication, config, settings |
| Codex | `codex` | 04_ai_apps/codex/ | API key, models, settings |
| Gemini | `gemini` | 04_ai_apps/gemini/ | API key, models, settings |
| Cursor Agent | `cursor-agent` | 04_ai_apps/cursor_agent/ | Config, credentials, settings |
| Perplexity | API only | 04_ai_apps/perplexity/ | API key, endpoints, settings |

<!-- section_id: "d447404c-71bc-41a5-bfaf-bc978d643f2c" -->
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

<!-- section_id: "41bf0b2d-0f34-4614-8bde-66f094e231ac" -->
## Next Layer

After AI apps configuration, the next layer is **05_plugins/** (editor and AI app extensions).
