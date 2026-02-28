# Gemini API: Quick Reference Card

**Last Updated**: February 27, 2026

---

## Installation & Setup

| Task | Python | JavaScript |
|------|--------|-----------|
| **Install** | `pip install google-genai --upgrade` | `npm install @google/genai` |
| **Import** | `from google import genai` | `import { GoogleGenAI } from '@google/genai'` |
| **Initialize** | `client = genai.Client()` | `const ai = new GoogleGenAI({apiKey})` |
| **API Key** | Env: `GEMINI_API_KEY` | Env: `GEMINI_API_KEY` |

---

## Models & Parameters

### Available Models (2026)
- `gemini-3-flash` - Latest, fastest (NEW)
- `gemini-3-pro` - Highest intelligence (NEW)
- `gemini-2.5-flash` - Fast, cost-effective
- `gemini-2.5-pro` - Advanced reasoning
- ⚠️ Retiring June 1, 2026: `gemini-1.5-pro`, `gemini-1.5-flash`

### Generation Parameters
```python
GenerateContentConfig(
    temperature=0.7,        # 0-2, default 1.0
    top_p=0.9,             # 0-1, default 0.94
    top_k=40,              # integer
    max_output_tokens=1000,
    stop_sequences=["END"],
)
```

**Presets**:
- **Deterministic** (summaries, translation): `temperature=0.2, top_p=0.8`
- **Balanced** (general): `temperature=0.7, top_p=0.9`
- **Creative** (writing, ideas): `temperature=1.5, top_p=0.95`
- **Gemini 3**: `temperature=1.0` (don't change)

---

## Common Operations

### Basic Text Generation
```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Your prompt here"
)
print(response.text)
```

### Chat/Conversation
```python
chat = client.chats.create(model="gemini-2.5-flash")
response = chat.send_message("First message")
response = chat.send_message("Follow-up")  # History automatic
```

### System Instructions
```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="User message",
    config=GenerateContentConfig(
        system_instruction="You are a helpful assistant"
    )
)
```

### File Upload & Use
```python
file = client.files.upload(file="document.pdf")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[file, "Summarize this"]
)
client.files.delete(name=file.name)
```

### Prompt Caching (Save Costs)
```python
# Create cache
cache = client.caches.create(
    model="gemini-2.5-flash",
    contents="[Large document]",
    ttl=timedelta(hours=1)
)

# Use cache (90% discount on cached tokens)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Question",
    cache_control={"cache_resource_name": cache.name}
)
```

### Count Tokens (Before Calling API)
```python
token_count = client.models.count_tokens(
    model="gemini-2.5-flash",
    contents="Your text"
)
print(f"Tokens: {token_count.total_tokens}")
```

---

## Cost & Usage Tracking

### Pricing (February 2026)
| Model | Input | Output | Notes |
|-------|-------|--------|-------|
| gemini-3-flash | $0.075/1M | $0.30/1M | Latest, fastest |
| gemini-2.5-flash | $0.075/1M | $0.30/1M | Good default |
| gemini-2.5-pro | $1.50/1M | $6.00/1M | Advanced |
| **Cached tokens** | 90% discount | No discount | Must enable caching |

### Cost Calculation
```python
# From response usage metadata
input_cost = (tokens.input_token_count / 1_000_000) * 0.075
output_cost = (tokens.output_token_count / 1_000_000) * 0.30
cached_cost = (tokens.cached_content_input_token_count / 1_000_000) * 0.0075

total = input_cost + output_cost + cached_cost
```

### Cost Optimization Checklist
- [ ] Use `gemini-2.5-flash` (cheapest fast model)
- [ ] Enable explicit caching for repeated context
- [ ] Set `max_output_tokens` to limit output
- [ ] Batch multiple queries into one request
- [ ] Count tokens before large requests
- [ ] Monitor monthly costs (free tier: check limits)

---

## Error Handling

### Common Errors
| Error | Cause | Fix |
|-------|-------|-----|
| 400 | Bad request | Check request format |
| 401 | Unauthorized | Check API key |
| 429 | Rate limited | Exponential backoff |
| 500/503 | Server error | Retry with backoff |
| 504 | Timeout | Increase timeout or reduce prompt |

### Retry Template
```python
import time

for attempt in range(3):
    try:
        response = client.models.generate_content(...)
        return response
    except Exception as e:
        if "429" in str(e) or "503" in str(e):
            wait = 2 ** attempt + random.random()
            time.sleep(wait)
        else:
            raise
```

---

## Session Management

### Save Chat History
```python
import json

history = [
    {"role": msg.role, "content": [{"text": part.text} for part in msg.parts]}
    for msg in chat.history
]

with open("chat.json", "w") as f:
    json.dump(history, f)
```

### Resume Chat
```python
with open("chat.json") as f:
    history = json.load(f)

chat = client.chats.create(
    model="gemini-2.5-flash",
    history=[
        {"role": h["role"], "parts": h["content"]}
        for h in history
    ]
)
```

---

## File Operations

### Upload
```python
file = client.files.upload(file="path/to/file.pdf")
print(file.name)  # Use in subsequent requests
```

### List Files
```python
for f in client.files.list():
    print(f.name, f.display_name, f.mime_type)
```

### Delete File
```python
client.files.delete(name=file.name)
```

### File Limits
- **Max storage**: 20 GB/project
- **Max file size**: 2 GB
- **Retention**: 48 hours (auto-delete)
- **Use Files API when**: Total request > 100 MB

---

## Caching Strategy

### When to Use Implicit Caching
- Default behavior, no setup needed
- No guaranteed cost savings
- Good for: Most requests

### When to Use Explicit Caching
- Large repeated context (system instructions, documents)
- Same context, different questions
- Cost savings guaranteed (90% discount)
- Good for: Chatbots, document analysis at scale

### Cache Configuration
```python
cache = client.caches.create(
    model="gemini-2.5-flash",
    display_name="my_cache",
    contents="[Your large content]",
    ttl=timedelta(hours=1),  # Expires in 1 hour
)

# Use it
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Question",
    cache_control={"cache_resource_name": cache.name}
)

# Update TTL
cache = client.caches.update(name=cache.name, ttl=timedelta(hours=2))

# Delete
client.caches.delete(name=cache.name)
```

---

## Security Checklist

- [ ] Use environment variables for API keys (never hardcode)
- [ ] Don't put API keys in system instructions
- [ ] Don't upload sensitive data unless necessary
- [ ] Files auto-delete after 48 hours (no manual retention)
- [ ] Use HTTPS (SDK handles this)
- [ ] Vertex AI users: Use IAM for authentication
- [ ] Monitor API usage for unusual patterns

---

## Rate Limits & Quotas

### Free Tier
- Requests per minute: Limited
- Tokens per minute: Limited
- Check quota in Google AI Studio

### Paid Tier
- Higher limits based on account
- Monitor in Cloud Console
- Set quotas to prevent overspending

### Handling 429 (Rate Limited)
```python
# Response includes retry delay
# Example: "retryDelay": "40s"

# Always implement exponential backoff
wait_seconds = 2 ** attempt + random.random()
time.sleep(wait_seconds)
```

---

## API Reference Cheat Sheet

### Text Generation
```python
response = client.models.generate_content(
    model="string",
    contents="string or list",
    config=GenerateContentConfig(...)
)
response.text          # Model output
response.usage_metadata  # Token counts
```

### Chat
```python
chat = client.chats.create(model="string", history=[])
response = chat.send_message("message")
chat.history           # All messages
```

### Files
```python
file = client.files.upload(file="path")
file.get(name="file-id")
client.files.list()
client.files.delete(name="file-id")
```

### Caching
```python
cache = client.caches.create(model=..., contents=..., ttl=...)
client.caches.update(name=..., ttl=...)
client.caches.delete(name=...)
client.caches.list()
```

### Token Counting
```python
count = client.models.count_tokens(model="...", contents="...")
count.total_tokens
```

---

## Useful Links

- **Docs**: https://ai.google.dev/gemini-api/docs/
- **SDK (Python)**: https://github.com/google-gemini/generative-ai-python
- **SDK (JS)**: https://github.com/googleapis/js-genai
- **Cookbook**: https://github.com/google-gemini/cookbook
- **Pricing**: https://ai.google.dev/gemini-api/docs/pricing
- **Status**: https://status.cloud.google.com/

---

## Quick Template: Full Application

```python
from google import genai
from google.genai.types import GenerateContentConfig
from datetime import timedelta

class GeminiApp:
    def __init__(self):
        self.client = genai.Client()
        self.chat = self.client.chats.create(model="gemini-2.5-flash")

    def chat_with_system_instruction(self, system_msg, user_msg):
        # Reset chat with system instruction
        self.chat = self.client.chats.create(
            model="gemini-2.5-flash"
        )
        response = self.chat.send_message(user_msg)
        return response.text

    def analyze_file(self, filepath):
        file = self.client.files.upload(file=filepath)
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[file, "Analyze this document"]
        )
        self.client.files.delete(name=file.name)
        return response.text

    def cached_analysis(self, document_text, questions):
        cache = self.client.caches.create(
            model="gemini-2.5-flash",
            contents=document_text,
            ttl=timedelta(hours=1)
        )

        results = {}
        for q in questions:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=q,
                cache_control={"cache_resource_name": cache.name}
            )
            results[q] = response.text

        return results

# Usage
app = GeminiApp()
print(app.chat_with_system_instruction("You are a poet", "Write a haiku"))
```

---

## Version Info
- SDK Versions: `google-genai>=0.1.33`, `@google/genai>=1.33.0`
- Models: Latest as of February 2026
- API Version: `v1beta`, `v1`
