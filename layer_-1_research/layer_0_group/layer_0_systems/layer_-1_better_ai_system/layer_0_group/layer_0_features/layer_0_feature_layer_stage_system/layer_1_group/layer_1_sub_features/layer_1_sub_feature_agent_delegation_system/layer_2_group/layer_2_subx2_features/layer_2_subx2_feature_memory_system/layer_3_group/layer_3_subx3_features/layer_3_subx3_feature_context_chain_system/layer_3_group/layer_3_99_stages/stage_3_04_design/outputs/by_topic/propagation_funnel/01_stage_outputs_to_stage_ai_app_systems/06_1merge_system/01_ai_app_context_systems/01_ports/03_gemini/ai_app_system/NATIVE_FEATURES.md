# Gemini API — Native Features

**Date**: 2026-02-27
**Focus**: What Gemini provides natively (the mechanisms)

---

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

## 1. Multiple Context Modes

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

### What Gemini Does

- **Accepts** context up to 1M or 2M tokens
- **Processes** entire context in a single request
- **Manages** token counting internally
- **Applies** context window limits per request

### What Gemini Does NOT Do

- Doesn't auto-split context (you manage what goes in)
- Doesn't compress old messages (you handle retention)
- Doesn't warn when approaching limits (you count tokens yourself)
- Doesn't retrieve partial context (all-or-nothing per request)

---

## 2. System Instructions

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

### What Gemini Does

- **Accepts** system instructions (no character limit, token-counted)
- **Applies** instructions to every response in a session
- **Combines** system instructions with user messages
- **Respects** instruction priority (system > user)

### What Gemini Does NOT Do

- Doesn't validate instruction quality
- Doesn't warn about conflicting instructions
- Doesn't auto-update instructions mid-conversation
- Doesn't expose instruction token count separately

---

## 3. Multimodal Input

### The Mechanism

Gemini accepts 5 types of input modality:

| Modality | Format | Token Cost | Limits |
|----------|--------|------------|--------|
| **Text** | Plain string | ~4 chars = 1 token | None |
| **Images** | PNG, JPEG, GIF, WebP | 258-1,120 tokens | <20MB |
| **Video** | MP4, MPEG, MOV, AVI | ~263 tokens/sec | 2 minutes |
| **Audio** | WAV, MP3, AIFF, AAC | ~32 tokens/sec | 15 minutes |
| **PDFs** | PDF documents | Variable | 2GB |

### What Gemini Does

- **Accepts** any combination of modalities in single request
- **Processes** each modality appropriately
- **Counts** tokens for each modality
- **Returns** analysis of all input types

### What Gemini Does NOT Do

- Doesn't transcribe audio (reads content directly)
- Doesn't extract PDFs (analyzes whole document)
- Doesn't optimize image resolution (you control via parameters)
- Doesn't support all video codecs (limited format support)

---

## 4. File Upload & Storage

### The Mechanism

Files are uploaded and stored temporarily:

**Storage Duration**: 48 hours (auto-deletion)
**Storage Quota**: 20GB per project
**File Size Limit**: 2GB per file
**Upload Methods**: Base64 (<100MB), Files API (>100MB), external URLs

### What Gemini Does

- **Accepts** file uploads via Files API
- **Stores** files for 48 hours
- **Returns** file references for use in requests
- **Deletes** files automatically after 48 hours

### What Gemini Does NOT Do

- Doesn't offer permanent storage
- Doesn't support file deletion before 48 hours (except quota management)
- Doesn't cache files (fresh access each time)
- Doesn't encrypt files (plain storage)

---

## 5. Session Management

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

### What Gemini Does

- **Creates** sessions on-demand
- **Stores** conversation history server-side
- **Generates** resumption tokens (2-hour expiry)
- **Returns** history on session resume

### What Gemini Does NOT Do

- Doesn't auto-resume (you must explicitly resume)
- Doesn't guarantee history beyond 2 hours
- Doesn't provide offline session caching
- Doesn't support session-level permissions

---

## 6. Context Caching

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

### What Gemini Does

- **Detects** identical prefixes (implicit)
- **Stores** explicitly created caches (explicit)
- **Reduces** costs on cache hits
- **Expires** caches after TTL

### What Gemini Does NOT Do

- Doesn't guarantee cache persistence beyond TTL
- Doesn't support partial cache invalidation
- Doesn't provide cache statistics per request
- Doesn't allow manual cache warming

---

## 7. Function Calling

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

### What Gemini Does

- **Accepts** JSON Schema tool definitions
- **Generates** function calls when appropriate
- **Supports** parallel function execution
- **Returns** tool call results in conversation

### What Gemini Does NOT Do

- Doesn't execute functions (you execute them)
- Doesn't validate function parameters
- Doesn't manage function state
- Doesn't handle function failures (you report back)

---

## 8. Streaming Output

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

### What Gemini Does

- **Streams** tokens as they're generated
- **Maintains** consistency with non-streaming (same final output)
- **Allows** early termination
- **Enables** progressive display

### What Gemini Does NOT Do

- Doesn't guarantee token order (stream order may vary)
- Doesn't support partial response cancellation
- Doesn't provide token-level confidence scores
- Doesn't offer stream-specific optimizations

---

## 9. Model Selection

### The Mechanism

Multiple models available with different capabilities:

| Model | Context | Speed | Cost | Intelligence |
|-------|---------|-------|------|--------------|
| **Gemini 3 Flash** | 1M/2M | Very Fast | $ | Good |
| **Gemini 3 Pro** | 1M/2M | Slow | $$$ | Excellent |
| **Gemini 2.5 Flash** | 1M/2M | Very Fast | $ | Good |
| **Gemini 2.5 Pro** | 1M/2M | Slow | $$$ | Excellent |

### What Gemini Does

- **Accepts** model selection per request
- **Routes** to appropriate backend
- **Applies** model-specific defaults
- **Returns** model-specific outputs

### What Gemini Does NOT Do

- Doesn't auto-select models
- Doesn't provide model capability descriptions
- Doesn't warn about deprecated models
- Doesn't offer performance predictions

---

## 10. Safety & Content Filtering

### The Mechanism

Built-in safety filters for:
- Sexual content
- Hateful content
- Harassment
- Dangerous/illegal activities

### What Gemini Does

- **Applies** safety filters automatically
- **Blocks** harmful content generation
- **Returns** safety ratings for input/output
- **Allows** tuning safety levels

### What Gemini Does NOT Do

- Doesn't expose filter thresholds
- Doesn't provide appeal mechanism
- Doesn't explain filtering decisions in detail
- Doesn't support custom safety rules

---

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

