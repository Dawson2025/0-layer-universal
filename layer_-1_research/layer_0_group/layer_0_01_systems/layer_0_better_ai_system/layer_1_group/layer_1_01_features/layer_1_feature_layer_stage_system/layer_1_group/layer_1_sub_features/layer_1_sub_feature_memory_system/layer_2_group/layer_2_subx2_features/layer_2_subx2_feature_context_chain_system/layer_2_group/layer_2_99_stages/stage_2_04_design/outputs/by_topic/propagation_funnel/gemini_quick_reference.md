---
resource_id: "648882b6-c82e-4d4c-ac61-70b2d907655c"
resource_type: "output"
resource_name: "gemini_quick_reference"
---
# Gemini API: Quick Reference Card

**Last Updated**: February 27, 2026

---

<!-- section_id: "5b0218e3-3486-4803-902a-3bc0f9289f1b" -->
## Installation & Setup

| Task | Python | JavaScript |
|------|--------|-----------|
| **Install** | `pip install google-genai --upgrade` | `npm install @google/genai` |
| **Import** | `from google import genai` | `import { GoogleGenAI } from '@google/genai'` |
| **Initialize** | `client = genai.Client()` | `const ai = new GoogleGenAI({apiKey})` |
| **API Key** | Env: `GEMINI_API_KEY` | Env: `GEMINI_API_KEY` |

---

<!-- section_id: "452fd6dc-f239-4223-b113-1414977ffd1c" -->
## Models & Parameters

<!-- section_id: "05ba43cb-f5a3-43fd-88b0-951d80951f27" -->
### Available Models (2026)
- `gemini-3-flash` - Latest, fastest (NEW)
- `gemini-3-pro` - Highest intelligence (NEW)
- `gemini-2.5-flash` - Fast, cost-effective
- `gemini-2.5-pro` - Advanced reasoning
- ⚠️ Retiring June 1, 2026: `gemini-1.5-pro`, `gemini-1.5-flash`

<!-- section_id: "43b42bac-2462-44eb-b413-3611379607d8" -->
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

<!-- section_id: "d51dfdca-cc83-480c-a06e-36579446ffbf" -->
## Common Operations

<!-- section_id: "01791773-a698-4363-b3da-84afc8066fec" -->
### Basic Text Generation
```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Your prompt here"
)
print(response.text)
```

<!-- section_id: "52541094-573e-4610-8fd1-95e1a7fd16f0" -->
### Chat/Conversation
```python
chat = client.chats.create(model="gemini-2.5-flash")
response = chat.send_message("First message")
response = chat.send_message("Follow-up")  # History automatic
```

<!-- section_id: "705428a0-2c1a-450e-997d-22de0d4a89c5" -->
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

<!-- section_id: "e2e29db2-7e7e-4da6-8da5-85844ee23cdd" -->
### File Upload & Use
```python
file = client.files.upload(file="document.pdf")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[file, "Summarize this"]
)
client.files.delete(name=file.name)
```

<!-- section_id: "84ef1124-c7a1-41e4-ba70-368177149116" -->
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

<!-- section_id: "0bb52cf7-f2fb-48ac-999f-dce6fe1c60da" -->
### Count Tokens (Before Calling API)
```python
token_count = client.models.count_tokens(
    model="gemini-2.5-flash",
    contents="Your text"
)
print(f"Tokens: {token_count.total_tokens}")
```

---

<!-- section_id: "39f7d5d6-f4f0-4b5b-a283-29e86a900bc1" -->
## Cost & Usage Tracking

<!-- section_id: "4f525b94-0c6e-4de7-b32e-91f6235967d6" -->
### Pricing (February 2026)
| Model | Input | Output | Notes |
|-------|-------|--------|-------|
| gemini-3-flash | $0.075/1M | $0.30/1M | Latest, fastest |
| gemini-2.5-flash | $0.075/1M | $0.30/1M | Good default |
| gemini-2.5-pro | $1.50/1M | $6.00/1M | Advanced |
| **Cached tokens** | 90% discount | No discount | Must enable caching |

<!-- section_id: "7319abb9-b719-45b2-8808-b20882e1cde3" -->
### Cost Calculation
```python
# From response usage metadata
input_cost = (tokens.input_token_count / 1_000_000) * 0.075
output_cost = (tokens.output_token_count / 1_000_000) * 0.30
cached_cost = (tokens.cached_content_input_token_count / 1_000_000) * 0.0075

total = input_cost + output_cost + cached_cost
```

<!-- section_id: "9e59ff40-b0fa-49c4-b862-51e54d60b280" -->
### Cost Optimization Checklist
- [ ] Use `gemini-2.5-flash` (cheapest fast model)
- [ ] Enable explicit caching for repeated context
- [ ] Set `max_output_tokens` to limit output
- [ ] Batch multiple queries into one request
- [ ] Count tokens before large requests
- [ ] Monitor monthly costs (free tier: check limits)

---

<!-- section_id: "b97d7369-f208-49aa-8f20-818f65e7a30c" -->
## Error Handling

<!-- section_id: "fcf2c814-15e4-45e7-9209-302927195ddd" -->
### Common Errors
| Error | Cause | Fix |
|-------|-------|-----|
| 400 | Bad request | Check request format |
| 401 | Unauthorized | Check API key |
| 429 | Rate limited | Exponential backoff |
| 500/503 | Server error | Retry with backoff |
| 504 | Timeout | Increase timeout or reduce prompt |

<!-- section_id: "e817c8ba-782c-417e-b229-cde94f6c80c0" -->
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

<!-- section_id: "fa780d49-2a31-4d51-9972-2c571c9f1691" -->
## Session Management

<!-- section_id: "ded21a97-ba8b-49ea-af55-0a671de2251d" -->
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

<!-- section_id: "4bf8b036-d10c-4a26-b5ec-53440d2e4ee5" -->
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

<!-- section_id: "36e0636f-b021-488e-b8fa-65f5ae9eb1a4" -->
## File Operations

<!-- section_id: "57729b4f-71d8-4ef1-a524-d180fa102bd9" -->
### Upload
```python
file = client.files.upload(file="path/to/file.pdf")
print(file.name)  # Use in subsequent requests
```

<!-- section_id: "696a7a6f-cdaf-4461-ba5d-f83d4852da27" -->
### List Files
```python
for f in client.files.list():
    print(f.name, f.display_name, f.mime_type)
```

<!-- section_id: "89895d5d-9873-46c8-ab31-8e7bdf361b99" -->
### Delete File
```python
client.files.delete(name=file.name)
```

<!-- section_id: "6cc094e1-bfbb-4075-8273-86adbbe7a7e1" -->
### File Limits
- **Max storage**: 20 GB/project
- **Max file size**: 2 GB
- **Retention**: 48 hours (auto-delete)
- **Use Files API when**: Total request > 100 MB

---

<!-- section_id: "4b8b7d4c-090c-42e8-b7b6-4a8b90c699ca" -->
## Caching Strategy

<!-- section_id: "ad581afb-3935-4069-af29-3e67c5b88bfb" -->
### When to Use Implicit Caching
- Default behavior, no setup needed
- No guaranteed cost savings
- Good for: Most requests

<!-- section_id: "45251da5-7170-4e09-9abb-d7d5ed82b9bc" -->
### When to Use Explicit Caching
- Large repeated context (system instructions, documents)
- Same context, different questions
- Cost savings guaranteed (90% discount)
- Good for: Chatbots, document analysis at scale

<!-- section_id: "2095235e-93df-4b99-8702-deff8d13437c" -->
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

<!-- section_id: "ed470102-587b-4efd-88e3-87cb51015c9c" -->
## Security Checklist

- [ ] Use environment variables for API keys (never hardcode)
- [ ] Don't put API keys in system instructions
- [ ] Don't upload sensitive data unless necessary
- [ ] Files auto-delete after 48 hours (no manual retention)
- [ ] Use HTTPS (SDK handles this)
- [ ] Vertex AI users: Use IAM for authentication
- [ ] Monitor API usage for unusual patterns

---

<!-- section_id: "185d0ad7-0746-4ade-902c-08fc2b45b9e8" -->
## Rate Limits & Quotas

<!-- section_id: "1a6617f8-8254-4765-b404-0f8415405e5c" -->
### Free Tier
- Requests per minute: Limited
- Tokens per minute: Limited
- Check quota in Google AI Studio

<!-- section_id: "dd524319-06c4-453c-80e1-8cbffe9101a1" -->
### Paid Tier
- Higher limits based on account
- Monitor in Cloud Console
- Set quotas to prevent overspending

<!-- section_id: "0e65a573-12a3-43e6-978f-37918cd45dba" -->
### Handling 429 (Rate Limited)
```python
# Response includes retry delay
# Example: "retryDelay": "40s"

# Always implement exponential backoff
wait_seconds = 2 ** attempt + random.random()
time.sleep(wait_seconds)
```

---

<!-- section_id: "b5c9ffdf-0823-4b0e-9767-43feccf112af" -->
## API Reference Cheat Sheet

<!-- section_id: "84a6cdae-0295-4770-8497-7a3aff36285c" -->
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

<!-- section_id: "c119826d-a2ac-40cf-a28a-d92a02b5668b" -->
### Chat
```python
chat = client.chats.create(model="string", history=[])
response = chat.send_message("message")
chat.history           # All messages
```

<!-- section_id: "743e86de-a9d8-44a3-9d24-3f1fc94bffca" -->
### Files
```python
file = client.files.upload(file="path")
file.get(name="file-id")
client.files.list()
client.files.delete(name="file-id")
```

<!-- section_id: "da6abc32-49d0-40bf-8e4c-160a0e6d45a1" -->
### Caching
```python
cache = client.caches.create(model=..., contents=..., ttl=...)
client.caches.update(name=..., ttl=...)
client.caches.delete(name=...)
client.caches.list()
```

<!-- section_id: "a4545826-aab6-4684-8244-ad1c0d959118" -->
### Token Counting
```python
count = client.models.count_tokens(model="...", contents="...")
count.total_tokens
```

---

<!-- section_id: "bd37b95e-6a8b-4b8a-afe4-6bca802cbe6d" -->
## Useful Links

- **Docs**: https://ai.google.dev/gemini-api/docs/
- **SDK (Python)**: https://github.com/google-gemini/generative-ai-python
- **SDK (JS)**: https://github.com/googleapis/js-genai
- **Cookbook**: https://github.com/google-gemini/cookbook
- **Pricing**: https://ai.google.dev/gemini-api/docs/pricing
- **Status**: https://status.cloud.google.com/

---

<!-- section_id: "aa339d24-7183-480c-8615-2ff4b4da0c97" -->
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

<!-- section_id: "c96af33b-5b7b-4347-a6ed-2fb3059e3faa" -->
## Version Info
- SDK Versions: `google-genai>=0.1.33`, `@google/genai>=1.33.0`
- Models: Latest as of February 2026
- API Version: `v1beta`, `v1`
