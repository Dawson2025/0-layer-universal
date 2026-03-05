---
resource_id: "365da4f6-b5c3-4cda-aef9-bbedf3f44d9f"
resource_type: "output"
resource_name: "NATIVE_FEATURES"
---
# Gemini API — Native Features

**Date**: 2026-02-27
**Focus**: What Gemini provides natively (the mechanisms)

---

<!-- section_id: "7c9b98df-063b-49a3-97bd-13e3fcb33e58" -->
## Overview

Google's Gemini provides these built-in mechanisms:

1. **Multiple Context Modes** (1M and 2M token context windows)
2. **System Instructions** (prompt-based role definition)
3. **Multimodal Input** (text, images, video, audio, PDFs, documents)
4. **File Upload & Storage** (48-hour ephemeral storage)
5. **Session Management** (conversation history & resumption)
6. **Context Caching** (implicit + explicit for cost reduction)
7. **Function Calling** (structured output & tool integration)
8. **Streaming Output** (real-time token delivery)
9. **Model Selection** (Gemini 3, 2.5, 1.5 with different capabilities)
10. **Safety & Content Filtering** (built-in safety settings)

---

<!-- section_id: "9dcef698-4ae0-41a4-9027-99a47fd22eb1" -->
## 1. Multiple Context Modes

<!-- section_id: "bf89dd87-d1ba-4894-9a40-0f794cf62b45" -->
### The Mechanism

Gemini handles two context window sizes:

**1M Token Window** (~50K lines of code, 8 novels, 200+ podcasts):
- Default for most applications
- Sufficient for most tasks
- Lower cost

**2M Token Window** (~100K lines of code, 16 novels, 400+ podcasts):
- Double capacity
- For large codebases or long documents
- Higher cost
- 99%+ retrieval accuracy

<!-- section_id: "d08ae622-b601-4296-92b0-32a744648927" -->
### What Gemini Does

- **Accepts** context up to 1M or 2M tokens
- **Processes** entire context in a single request
- **Manages** token counting internally
- **Applies** context window limits per request

<!-- section_id: "2767a69a-6c2f-4a26-9a50-3945da975223" -->
### What Gemini Does NOT Do

- Doesn't auto-split context (you manage what goes in)
- Doesn't compress old messages (you handle retention)
- Doesn't warn when approaching limits (you count tokens yourself)
- Doesn't retrieve partial context (all-or-nothing per request)

---

<!-- section_id: "eda58a64-41f9-4b76-8b24-3adcc0129c2c" -->
## 2. System Instructions

<!-- section_id: "2346a0a4-502c-410d-be55-f1c18a040293" -->
### The Mechanism

You provide system instructions to define Gemini's role and behavior:

```python
system_instruction = """
You are an expert Python developer specializing in data analysis.
Always provide clean, documented code.
Prefer pandas for data manipulation.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_message,
    system_instruction=system_instruction,
)
```

<!-- section_id: "aff2add0-10f3-48c3-b6f9-5c7d7025db85" -->
### What Gemini Does

- **Accepts** system instructions (no character limit, token-counted)
- **Applies** instructions to every response in a session
- **Combines** system instructions with user messages
- **Respects** instruction priority (system > user)

<!-- section_id: "9587be34-e813-4fe6-8627-28a915477c5d" -->
### What Gemini Does NOT Do

- Doesn't validate instruction quality
- Doesn't warn about conflicting instructions
- Doesn't auto-update instructions mid-conversation
- Doesn't expose instruction token count separately

---

<!-- section_id: "ee4f47a8-baa7-4be3-ab5b-4785ec041b85" -->
## 3. Multimodal Input

<!-- section_id: "d5d35c8a-1c72-40f5-b6d1-15ac30847481" -->
### The Mechanism

Gemini accepts 5 types of input modality:

| Modality | Format | Token Cost | Limits |
|----------|--------|------------|--------|
| **Text** | Plain string | ~4 chars = 1 token | None |
| **Images** | PNG, JPEG, GIF, WebP | 258-1,120 tokens | <20MB |
| **Video** | MP4, MPEG, MOV, AVI | ~263 tokens/sec | 2 minutes |
| **Audio** | WAV, MP3, AIFF, AAC | ~32 tokens/sec | 15 minutes |
| **PDFs** | PDF documents | Variable | 2GB |

<!-- section_id: "05db931e-b091-4d7d-b1f9-431b38f84496" -->
### What Gemini Does

- **Accepts** any combination of modalities in single request
- **Processes** each modality appropriately
- **Counts** tokens for each modality
- **Returns** analysis of all input types

<!-- section_id: "6fa8b782-7b70-4ab0-a7fd-4ec7cfaf4761" -->
### What Gemini Does NOT Do

- Doesn't transcribe audio (reads content directly)
- Doesn't extract PDFs (analyzes whole document)
- Doesn't optimize image resolution (you control via parameters)
- Doesn't support all video codecs (limited format support)

---

<!-- section_id: "57d72d3e-2cd2-4605-9b4c-06b50c545514" -->
## 4. File Upload & Storage

<!-- section_id: "8240f41d-54d7-43b1-af03-e1dae36bdd5f" -->
### The Mechanism

Files are uploaded and stored temporarily:

**Storage Duration**: 48 hours (auto-deletion)
**Storage Quota**: 20GB per project
**File Size Limit**: 2GB per file
**Upload Methods**: Base64 (<100MB), Files API (>100MB), external URLs

<!-- section_id: "3e2ae445-6aa7-4c3d-90b7-29a3f4197c72" -->
### What Gemini Does

- **Accepts** file uploads via Files API
- **Stores** files for 48 hours
- **Returns** file references for use in requests
- **Deletes** files automatically after 48 hours

<!-- section_id: "bfb508f8-8848-42f4-82f2-c8874a596a1a" -->
### What Gemini Does NOT Do

- Doesn't offer permanent storage
- Doesn't support file deletion before 48 hours (except quota management)
- Doesn't cache files (fresh access each time)
- Doesn't encrypt files (plain storage)

---

<!-- section_id: "335ace83-102e-4a80-a9e2-5f0261183a0d" -->
## 5. Session Management

<!-- section_id: "b70da7e3-2d9c-4d80-8345-7d693ab7c15d" -->
### The Mechanism

Gemini supports two session models:

**Stateless API** (default):
- Single request-response
- No conversation history
- Fastest, simplest

**Stateful API (Chat)** (with Interactions API):
- Conversation history maintained server-side
- Sessions can be resumed with tokens
- Token valid for 2 hours post-termination

<!-- section_id: "e661cd5b-51f0-45aa-8334-8c0e2fa5297b" -->
### What Gemini Does

- **Creates** sessions on-demand
- **Stores** conversation history server-side
- **Generates** resumption tokens (2-hour expiry)
- **Returns** history on session resume

<!-- section_id: "491764f3-2bbb-41f1-b725-73828a56a67f" -->
### What Gemini Does NOT Do

- Doesn't auto-resume (you must explicitly resume)
- Doesn't guarantee history beyond 2 hours
- Doesn't provide offline session caching
- Doesn't support session-level permissions

---

<!-- section_id: "b32497b5-2fc8-485d-a8de-ab4bb81af8e6" -->
## 6. Context Caching

<!-- section_id: "dd29def7-1756-40ad-a7ca-99d9f7a2e082" -->
### The Mechanism

Two caching strategies:

**Implicit Caching** (automatic):
- Minimum 4,096 tokens required
- Automatic after first request with same prefix
- ~50% cost reduction on cached tokens

**Explicit Caching** (developer-managed):
- Minimum 1,024 tokens
- Guaranteed availability for TTL duration
- ~90% cost reduction on cached tokens

<!-- section_id: "a041a06d-c6cb-48a4-843c-a85d05068355" -->
### What Gemini Does

- **Detects** identical prefixes (implicit)
- **Stores** explicitly created caches (explicit)
- **Reduces** costs on cache hits
- **Expires** caches after TTL

<!-- section_id: "02b672e8-4749-4881-9fd1-206aa26bfcf7" -->
### What Gemini Does NOT Do

- Doesn't guarantee cache persistence beyond TTL
- Doesn't support partial cache invalidation
- Doesn't provide cache statistics per request
- Doesn't allow manual cache warming

---

<!-- section_id: "1614fdb8-b962-49fd-a8fe-600044c6b0b3" -->
## 7. Function Calling

<!-- section_id: "b3b87b43-1011-4158-b04f-4edd094df51d" -->
### The Mechanism

Gemini can generate structured function calls:

```python
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    tools=tools,
)
```

<!-- section_id: "87872708-51d1-4f27-801d-7d06c460ad35" -->
### What Gemini Does

- **Accepts** JSON Schema tool definitions
- **Generates** function calls when appropriate
- **Supports** parallel function execution
- **Returns** tool call results in conversation

<!-- section_id: "3f830bab-7dc8-46e0-add1-607c8a6e42c7" -->
### What Gemini Does NOT Do

- Doesn't execute functions (you execute them)
- Doesn't validate function parameters
- Doesn't manage function state
- Doesn't handle function failures (you report back)

---

<!-- section_id: "7be373b6-65bc-467e-af2f-fbc9e6ff2520" -->
## 8. Streaming Output

<!-- section_id: "19e7e8b0-63cf-466a-8cda-c240b6a6c3b2" -->
### The Mechanism

Responses can stream tokens in real-time:

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    stream=True,
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

<!-- section_id: "f5231c34-078a-41bc-92d2-1d8abd1d7d0a" -->
### What Gemini Does

- **Streams** tokens as they're generated
- **Maintains** consistency with non-streaming (same final output)
- **Allows** early termination
- **Enables** progressive display

<!-- section_id: "cad717fd-e761-4cef-9803-d70a9735ffa1" -->
### What Gemini Does NOT Do

- Doesn't guarantee token order (stream order may vary)
- Doesn't support partial response cancellation
- Doesn't provide token-level confidence scores
- Doesn't offer stream-specific optimizations

---

<!-- section_id: "f1bbcb21-7a3c-460f-a5ff-05aa938f6235" -->
## 9. Model Selection

<!-- section_id: "efd3f43b-eae8-498e-8db2-ae3928aedfb0" -->
### The Mechanism

Multiple models available with different capabilities:

| Model | Context | Speed | Cost | Intelligence |
|-------|---------|-------|------|--------------|
| **Gemini 3 Flash** | 1M/2M | Very Fast | $ | Good |
| **Gemini 3 Pro** | 1M/2M | Slow | $$$ | Excellent |
| **Gemini 2.5 Flash** | 1M/2M | Very Fast | $ | Good |
| **Gemini 2.5 Pro** | 1M/2M | Slow | $$$ | Excellent |

<!-- section_id: "89147df3-1961-4ea0-be40-7729b4d2ceaa" -->
### What Gemini Does

- **Accepts** model selection per request
- **Routes** to appropriate backend
- **Applies** model-specific defaults
- **Returns** model-specific outputs

<!-- section_id: "fb5f7ffe-cb30-451b-9a54-647b3704bd76" -->
### What Gemini Does NOT Do

- Doesn't auto-select models
- Doesn't provide model capability descriptions
- Doesn't warn about deprecated models
- Doesn't offer performance predictions

---

<!-- section_id: "c57814fa-1c6b-4ceb-8574-281326576f70" -->
## 10. Safety & Content Filtering

<!-- section_id: "2a3de726-4eca-4ca9-b1f2-566d4455495a" -->
### The Mechanism

Built-in safety filters for:
- Sexual content
- Hateful content
- Harassment
- Dangerous/illegal activities

<!-- section_id: "38e75d41-be4c-412b-b1b7-c0eeb9da4dc0" -->
### What Gemini Does

- **Applies** safety filters automatically
- **Blocks** harmful content generation
- **Returns** safety ratings for input/output
- **Allows** tuning safety levels

<!-- section_id: "f58fe362-dedf-4fd7-b845-1447c2c92f21" -->
### What Gemini Does NOT Do

- Doesn't expose filter thresholds
- Doesn't provide appeal mechanism
- Doesn't explain filtering decisions in detail
- Doesn't support custom safety rules

---

<!-- section_id: "4ae4cdd8-f377-4e49-9f10-760cda6c8bdf" -->
## Summary: Native = Mechanisms Provided

Gemini provides **mechanisms** (how things work), not **policies** (what to do with them):

✅ **Native**: Accepts multimodal input (text, images, video, audio, PDFs)
❌ **Not native**: You decide what modalities to use

✅ **Native**: Stores files for 48 hours automatically
❌ **Not native**: You decide what files to upload and when

✅ **Native**: Implements context caching (implicit + explicit)
❌ **Not native**: You decide whether/how to use caching

✅ **Native**: Supports multiple models
❌ **Not native**: You choose which model for each task

✅ **Native**: Applies safety filters
❌ **Not native**: You decide content policy for your app

